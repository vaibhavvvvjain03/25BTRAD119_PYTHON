"""
hwsnap.py - Hardware Snapshot & Fingerprinting Module for HWGuard

Collects immutable hardware identifiers (Motherboard, BIOS, CPU, Memory, Disk, UUID)
and provides salted hashing, Merkle snapshot root generation, and battery tracking.
"""
import hashlib
import json
import os
import platform
import subprocess
import sys

# Maximum expected battery cycle increase between scans
MAX_CYCLE_DELTA = 15


def keccak256(data: bytes) -> str:
    """
    Computes 256-bit cryptographic digest formatted with 0x prefix.
    Uses Python's built-in sha3_256 (standard Keccak-256 family).
    """
    return "0x" + hashlib.sha3_256(data).hexdigest()


def build_components(raw, salt: str) -> list:
    """
    Builds component hash list from raw hardware audit tuples.
    Only stores salted cryptographic hashes, never raw serial numbers.
    """
    comps = []
    for c_type, slot, serial in raw:
        payload = f"{salt}:{c_type}:{slot}:{serial}".encode("utf-8", errors="replace")
        h = keccak256(payload)
        comps.append({
            "type": c_type,
            "slot": slot,
            "hash": h
        })
    return comps


def snapshot_root(comps: list) -> str:
    """
    Computes cryptographic root hash across all components in the snapshot.
    """
    if not comps:
        return "0x" + "00" * 32
    hashes = sorted(c["hash"] for c in comps)
    combined = ":".join(hashes).encode("utf-8")
    return keccak256(combined)


# ---------------- Hardware Collectors ----------------

def _collect_windows():
    raw = []
    skipped = []
    cycles = None

    def run_ps(cmd: str):
        try:
            res = subprocess.run(
                ["powershell", "-NoProfile", "-NonInteractive", "-Command", cmd],
                capture_output=True,
                text=True,
                timeout=10
            )
            out = res.stdout.strip()
            if not out:
                return []
            d = json.loads(out)
            return d if isinstance(d, list) else [d]
        except Exception:
            return []

    # 1. Motherboard (BaseBoard)
    try:
        bb = run_ps("Get-CimInstance Win32_BaseBoard | Select-Object Manufacturer, Product, SerialNumber | ConvertTo-Json")
        if bb and bb[0].get("SerialNumber"):
            mfg = str(bb[0].get("Manufacturer", "")).strip()
            prod = str(bb[0].get("Product", "")).strip()
            sn = str(bb[0].get("SerialNumber", "")).strip()
            raw.append(("Motherboard", "BaseBoard", f"{mfg} {prod} (S/N: {sn})".strip()))
        else:
            skipped.append("Motherboard")
    except Exception:
        skipped.append("Motherboard")

    # 2. BIOS
    try:
        bios = run_ps("Get-CimInstance Win32_BIOS | Select-Object SerialNumber, SMBIOSBIOSVersion, Manufacturer | ConvertTo-Json")
        if bios and bios[0].get("SerialNumber"):
            sn = str(bios[0].get("SerialNumber", "")).strip()
            ver = str(bios[0].get("SMBIOSBIOSVersion", "")).strip()
            raw.append(("BIOS", "Firmware", f"v{ver} (S/N: {sn})".strip()))
        else:
            skipped.append("BIOS")
    except Exception:
        skipped.append("BIOS")

    # 3. System UUID
    try:
        uuid_data = run_ps("Get-CimInstance Win32_ComputerSystemProduct | Select-Object UUID | ConvertTo-Json")
        if uuid_data and uuid_data[0].get("UUID"):
            raw.append(("System", "UUID", str(uuid_data[0].get("UUID", "")).strip()))
        else:
            skipped.append("System UUID")
    except Exception:
        skipped.append("System UUID")

    # 4. Processor / CPU
    try:
        cpus = run_ps("Get-CimInstance Win32_Processor | Select-Object DeviceID, Name, ProcessorId | ConvertTo-Json")
        if cpus:
            for idx, c in enumerate(cpus):
                slot = str(c.get("DeviceID") or f"CPU{idx}").strip()
                pid = str(c.get("ProcessorId", "")).strip()
                name = str(c.get("Name", "")).strip()
                raw.append(("CPU", slot, f"{name} [ID: {pid}]".strip()))
        else:
            skipped.append("CPU")
    except Exception:
        skipped.append("CPU")

    # 5. RAM Modules
    try:
        ram = run_ps("Get-CimInstance Win32_PhysicalMemory | Select-Object DeviceLocator, BankLabel, SerialNumber, Capacity, PartNumber | ConvertTo-Json")
        if ram:
            for idx, m in enumerate(ram):
                loc = str(m.get("DeviceLocator") or m.get("BankLabel") or f"DIMM{idx}").strip()
                sn = str(m.get("SerialNumber", "")).strip()
                part = str(m.get("PartNumber", "")).strip()
                cap = int(m.get("Capacity", 0))
                cap_gb = f"{round(cap / (1024**3), 1)}GB" if cap else ""
                desc = " ".join(filter(None, [part, cap_gb, f"(S/N: {sn})" if sn else ""]))
                raw.append(("Memory", loc, desc or f"Memory Module {idx}"))
        else:
            skipped.append("Memory")
    except Exception:
        skipped.append("Memory")

    # 6. Physical Disks
    try:
        disks = run_ps("Get-CimInstance Win32_DiskDrive | Select-Object Index, DeviceID, Model, SerialNumber, Size | ConvertTo-Json")
        if disks:
            for idx, d in enumerate(disks):
                slot = f"Disk {d.get('Index', idx)}"
                model = str(d.get("Model", "")).strip()
                sn = str(d.get("SerialNumber", "")).strip()
                raw.append(("Disk", slot, f"{model} (S/N: {sn})".strip()))
        else:
            skipped.append("Disks")
    except Exception:
        skipped.append("Disks")

    # 7. Battery Cycle Count
    try:
        bat = run_ps("Get-CimInstance -Namespace root/wmi -ClassName BatteryCycleCount -ErrorAction SilentlyContinue | Select-Object CycleCount | ConvertTo-Json")
        if bat and "CycleCount" in bat[0]:
            c = bat[0]["CycleCount"]
            if c is not None and str(c).isdigit():
                cycles = int(c)
    except Exception:
        pass

    return raw, cycles, skipped


def _collect_linux():
    raw = []
    skipped = []
    cycles = None

    def read_sysfs(path: str) -> str:
        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read().strip()
        except Exception:
            return ""

    mfg = read_sysfs("/sys/class/dmi/id/board_vendor")
    name = read_sysfs("/sys/class/dmi/id/board_name")
    sn = read_sysfs("/sys/class/dmi/id/board_serial")
    if sn:
        raw.append(("Motherboard", "BaseBoard", f"{mfg} {name} (S/N: {sn})".strip()))
    else:
        skipped.append("Motherboard")

    bios_ver = read_sysfs("/sys/class/dmi/id/bios_version")
    bios_date = read_sysfs("/sys/class/dmi/id/bios_date")
    if bios_ver:
        raw.append(("BIOS", "Firmware", f"v{bios_ver} ({bios_date})".strip()))
    else:
        skipped.append("BIOS")

    uuid = read_sysfs("/sys/class/dmi/id/product_uuid")
    if uuid:
        raw.append(("System", "UUID", uuid))
    else:
        skipped.append("System UUID")

    try:
        with open("/proc/cpuinfo", "r") as f:
            for line in f:
                if "model name" in line:
                    cpu_name = line.split(":", 1)[1].strip()
                    raw.append(("CPU", "Socket 0", cpu_name))
                    break
    except Exception:
        skipped.append("CPU")

    try:
        cc_str = read_sysfs("/sys/class/power_supply/BAT0/cycle_count")
        if cc_str and cc_str.isdigit():
            cycles = int(cc_str)
    except Exception:
        pass

    return raw, cycles, skipped


def _collect_darwin():
    raw = []
    skipped = []
    cycles = None

    try:
        out = subprocess.check_output(
            ["system_profiler", "SPHardwareDataType", "SPStorageDataType", "SPPowerDataType", "-json"],
            text=True, timeout=10
        )
        data = json.loads(out)
        hw = data.get("SPHardwareDataType", [{}])[0]
        if "serial_number" in hw:
            raw.append(("System", "UUID", hw.get("platform_UUID", hw.get("serial_number"))))
            raw.append(("Motherboard", "LogicBoard", f"{hw.get('machine_model', 'Mac')} (S/N: {hw.get('serial_number')})"))
        if "cpu_type" in hw:
            raw.append(("CPU", "Processor", f"{hw.get('cpu_type')} ({hw.get('number_processors', '1')} cores)"))

        pwr = data.get("SPPowerDataType", [{}])[0]
        info = pwr.get("sppower_battery_health_info", {})
        if "sppower_battery_cycle_count" in info:
            cycles = int(info["sppower_battery_cycle_count"])
    except Exception:
        skipped.append("Hardware Profiler")

    return raw, cycles, skipped


def collect():
    """
    Main hardware collection entry point. Dispatches to platform-native collector.
    Returns: (raw, cycles, skipped)
    """
    sys_name = platform.system()
    if sys_name == "Windows":
        return _collect_windows()
    elif sys_name == "Linux":
        return _collect_linux()
    elif sys_name == "Darwin":
        return _collect_darwin()
    else:
        raw = [
            ("Platform", "System", platform.system()),
            ("Platform", "Release", platform.release()),
            ("CPU", "Architecture", platform.machine()),
            ("System", "Node", platform.node()),
        ]
        return raw, None, ["SMBIOS (Unsupported OS)"]
