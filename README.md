# Experiential Learning (Python Programming) — Lab Submissions

**Student Name:** VAIBHAV A JAIN  
**USN:** 25BTRAD119  
**Department:** Computer Science and Engineering (Artificial Intelligence and Data Engineering)  
**Institution:** Jain (Deemed-to-be University), Faculty of Engineering and Technology (FET)  

---

## 📌 Repository Overview

This repository contains lab exercises, problem-solving practical tasks, foundational task sheets, and experiential learning activities completed as part of the **Experiential Learning (Python Programming)** curriculum. The repository is organized into distinct modules encompassing core Python fundamentals, data structures, file and CSV manipulation, object-oriented software engineering, real-world utility mini-projects, and an enterprise-grade cryptographic hardware security application (**HWGuard**).

Each program is implemented with clean, documented Python source code, interactive terminal interfaces, and robust error handling to demonstrate comprehensive practical programming mastery.

---

## 📁 Repository Overview

| Directory / File Name | Category | Topics / Scope |
| :--- | :--- | :--- |
| **`25BTRAD119_Lab Exercises/`** | Core Lab Submissions | Comprehensive laboratory programs (Exercises 2 to 16) spanning basic I/O, operators, calculators, prime/factorial algorithms, recursion, dictionary CRUD, log file analyzers, persistent text/CSV databases, OOP banking and library systems, and probability simulation. |
| **`25BTRAD119_Problem Solving/`** | Problem Solving & Tasks | Foundational Python syntax task sheets (Tasks 1 to 18) alongside real-world problem-solving modules: Point-of-Sale (POS) bill generator, student grading system, secure 6-digit OTP generator & verifier, sales revenue analyzer, and an enterprise student attendance tracking system. |
| **`25BTRAD119_Experiential Learning Activity/`** | Capstone Major Project | **HWGuard Universal Hardware Vault**: A portable, cross-platform hardware integrity auditor and anti-tamper security suite featuring a Tkinter GUI, salted Keccak-256 cryptographic hashing, Merkle snapshot roots, and hash-chained audit logging. |

### Detailed File & Module Mapping

| File Name | Category | Topics / Scope |
| :--- | :--- | :--- |
| `25BTRAD119_TASK 1.py` to `18.py` | Foundational Tasks | Python Basics Workbook: Output formatting, escape sequences, comments, variables, type conversion, user input, temperature conversion, and modulus operations (Tasks 1–18). |
| `25BTRAD119_LAB EXERCISE 2.PY` | Lab Exercise | Environment verification, basic console output formatting, student details. |
| `25BTRAD119_LAB EXERCISE 3.PY` | Lab Exercise | Variables, type casting, input handling, and arithmetic/modulus operations. |
| `25BTRAD119_LAB EXERCISE 4.PY` | Lab Exercise | Arithmetic calculator and geometric area calculations (circle & rectangle) with f-strings. |
| `25BTRAD119_LAB EXERCISE 5.py` | Lab Exercise | Interactive Number Guessing Game implementing `random.randint`, loops, and proximity hints. |
| `25BTRAD119_LAB EXERCISE 6A.py` | Lab Exercise | Prime number validation using factor-checking algorithms and condition checks. |
| `25BTRAD119_LAB EXERCISE 6B.py` | Lab Exercise | Iterative factorial computation ($n!$) using bounded loop accumulation. |
| `25BTRAD119_LAB EXERCISE 7.py` | Lab Exercise | Fibonacci sequence generation utilizing recursive functions (`fibonacci(n)`). |
| `25BTRAD119_LAB EXERCISE 8.PY` | Lab Exercise | Interactive Contact Book utilizing Python dictionaries for complete CRUD operations. |
| `25BTRAD119_LAB EXERCISE 9.PY` | Lab Exercise | Student Grading System mapping marks to letter grades (A–F) via conditional rules. |
| `25BTRAD119_LAB EXERCISE 10.PY` | Lab Exercise | Word Frequency Counter analyzing sentence strings, total words, and unique word counts. |
| `25BTRAD119_LAB EXERCISE 11.py` | Lab Exercise | Server log file reader and analyzer parsing `app.log` for ERROR, WARNING, and INFO tallies. |
| `25BTRAD119_LAB EXERCISE 12.py` | Lab Exercise | File-based Student Data Manager with persistent storage, searching, and updates in `students.txt`. |
| `25BTRAD119_LAB EXERCISE 13.py` | Lab Exercise | CSV Payroll Management System parsing `employees.csv` using `csv.DictReader` for net salary computation. |
| `25BTRAD119_LAB EXERCISE 14.py` | Lab Exercise | Object-Oriented Bank Account System (`class BankAccount`) with private balance encapsulation. |
| `25BTRAD119_LAB EXERCISE 15.py` | Lab Exercise | Library Management System (`class Book`) managing book inventory, borrowing, and returns. |
| `25BTRAD119_LAB EXERCISE 16.py` | Lab Exercise | Dice Rolling Simulator leveraging `random.randint` for single and two-dice outcome simulations. |
| `25BTRAD119_PROBLEM SOLVING 1.py` | Problem Solving | Quick Shop Point-of-Sale (POS) billing system with item quantities, subtotal, 5% sales tax, and receipt. |
| `25BTRAD119_PROBLEM SOLVING 2.py` | Problem Solving | Student Academic Performance Evaluator calculating aggregate scores, percentage, and grade. |
| `25BTRAD119_PROBLEM SOLVING 2A.py` | Problem Solving | One-Time Password (OTP) Generator & Verifier simulating secure 6-digit authentication. |
| `25BTRAD119_PROBLEM SOLVING 3.py` | Problem Solving | Sales Data Analyzer managing inventory sales, total revenue calculation, and best-seller identification. |
| `25BTRAD119_PROBLEM SOLVING 4.py` | Problem Solving | Student Attendance Tracker: multi-student management with P/A status, percentage, threshold alerts, and summaries. |
| `FINALPROJECT.py` / `hwguard.py` | Capstone Project | HWGuard Universal Hardware Vault: Anti-tamper desktop GUI with cryptographic hash-chained audit logging. |
| `hwsnap.py` | Capstone Project | Hardware fingerprinting engine collecting Motherboard, BIOS, CPU, RAM, Disk, and battery cycles with salted Keccak-256 digests. |

---

## 📖 Detailed Content Breakdown

### 1. Lab Exercises

* **`25BTRAD119_LAB EXERCISE 2.PY` — Environment Verification & Console Output**
  * Displays verified student credentials, academic department (`CSE - AI & Data Engineering`), and institution details using formatted `print()` calls.

* **`25BTRAD119_LAB EXERCISE 3.PY` — Variables, Operators & User Input Handling**
  * Captures user input via `input()` and applies explicit type casting (`int`).
  * Computes and prints arithmetic results: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulus (`%`).

* **`25BTRAD119_LAB EXERCISE 4.PY` — Menu-Free Console Calculator & Geometric Area Computation**
  * Executes multi-operator arithmetic calculations with float precision.
  * Solves geometric area formulas for circles ($A = \pi r^2$) and rectangles ($A = l \times b$) rendered using formatted f-strings (`:.2f`).

* **`25BTRAD119_LAB EXERCISE 5.py` — Number Guessing Game (Randomization & Loops)**
  * Implements `random.randint(1, 100)` to generate a dynamic target number.
  * Utilizes a `while True` loop with conditional feedback (`"Too low!"`, `"Too high!"`) and termination upon successful guess.

* **`25BTRAD119_LAB EXERCISE 6A.py` — Prime Number Validation**
  * Validates natural numbers for primality using factor checking loops from $2$ to $n-1$.
  * Incorporates guard clauses for boundary inputs ($n \le 1$).

* **`25BTRAD119_LAB EXERCISE 6B.py` — Iterative Factorial Computation**
  * Computes the factorial ($n! = \prod_{i=1}^n i$) of a user-supplied integer using bounded `for` loops and multiplicative accumulation.

* **`25BTRAD119_LAB EXERCISE 7.py` — Recursive Fibonacci Sequence Generator**
  * Implements the recursive recurrence relation $F(n) = F(n-1) + F(n-2)$ with base cases $F(0) = 0$ and $F(1) = 1$.
  * Formats and prints the sequence horizontally for $n$ terms.

* **`25BTRAD119_LAB EXERCISE 8.PY` — Interactive Dictionary Contact Book (CRUD)**
  * Full-featured menu-driven console application leveraging Python dictionaries and lists.
  * Implements CRUD operations: **Create** (Add), **Read** (Search/Display), **Update** (Modify phone numbers), and **Delete** (Remove records).

* **`25BTRAD119_LAB EXERCISE 9.PY` — Student Grading System**
  * Collects marks for multiple students dynamically into a dictionary.
  * Evaluates letter grades (Grade A $\ge 90$, B $\ge 75$, C $\ge 60$, D/F) using multi-tier conditional branching.

* **`25BTRAD119_LAB EXERCISE 10.PY` — Sentence Word Frequency Counter**
  * Ingests sentence strings, normalizes casing via `.lower()`, and tokenizes into words with `.split()`.
  * Constructs a frequency distribution dictionary and computes metrics for total words and unique vocabulary size.

* **`25BTRAD119_LAB EXERCISE 11.py` — Server Log File Reader & Analyzer**
  * Demonstrates file I/O using Python's `with open("app.log", "r")` context manager.
  * Scans log lines sequentially and tallies keyword occurrences: `ERROR`, `WARNING`, and `INFO`.

* **`25BTRAD119_LAB EXERCISE 12.py` — Persistent Student Data Manager**
  * File-based database engine operating on `students.txt` with formatted comma-delimited record storage.
  * Menu-driven operations: Add Student (with duplicate roll number prevention and range validation $0 \le \text{marks} \le 100$), Display All, Search by Roll Number, and Persistent In-Place Record Update.

* **`25BTRAD119_LAB EXERCISE 13.py` — CSV-Based Payroll Management System**
  * Parses structured tabular data from `employees.csv` using Python's standard `csv.DictReader`.
  * Computes payroll metrics: Basic Salary, Allowances, Deductions, and Net Salary with a formatted summary table.

* **`25BTRAD119_LAB EXERCISE 14.py` — Object-Oriented Bank Account System (OOP)**
  * Encapsulation using `class BankAccount` with private attribute `__balance`.
  * Enforces business logic: deposit validation ($> 0$), insufficient balance withdrawal protection, and balance enquiry.

* **`25BTRAD119_LAB EXERCISE 15.py` — Object-Oriented Library Management System**
  * Models book entities using `class Book` tracking titles and checkout state (`available`).
  * Features book issuing, return validation, and real-time inventory availability display.

* **`25BTRAD119_LAB EXERCISE 16.py` — Dice Rolling Simulator**
  * Leverages Python's `random.randint(1, 6)` module to simulate single-die rolls and simultaneous two-dice throws with combined score summation.

---

### 2. Problem Solving Practical Tasks

* **`25BTRAD119_PROBLEM SOLVING 1.py` — Quick Shop Point-of-Sale (POS) Billing System**
  * **Description**: An interactive console-based retail billing application.
  * **Key Features**:
    * Fixed product catalog: Biscuits (₹25), Chips (₹15), and Pens (₹10).
    * Dynamic ordering loop allowing shoppers to accumulate quantities until entering `'done'`.
    * Automatic calculation of itemized subtotals, 5% sales tax, and final grand total.
    * Formatted receipt generation with borders and headers.

* **`25BTRAD119_PROBLEM SOLVING 2.py` — Student Academic Performance & Grade Analyzer**
  * **Description**: Multi-subject academic performance evaluator.
  * **Key Features**:
    * Captures scores across Python, Mathematics, and English.
    * Computes total aggregate marks and overall percentage.
    * Categorizes performance into academic grade bands (A: $\ge 90\%$, B: $\ge 75\%$, C: $\ge 60\%$, D: $\ge 40\%$, F: $< 40\%$).

* **`25BTRAD119_PROBLEM SOLVING 2A.py` — 6-Digit One-Time Password (OTP) Generator & Verifier**
  * **Description**: Authentication token generator and challenge-response verifier.
  * **Key Features**:
    * Generates cryptographically simulated 6-digit numeric OTPs via `random.randint(100000, 999999)`.
    * Interactive validation prompt verifying user input against the generated token.

* **`25BTRAD119_PROBLEM SOLVING 3.py` — Sales Data Analyzer & Business Intelligence System**
  * **Description**: Menu-driven business intelligence tool using nested dictionary data structures (`{product: [quantity, price]}`).
  * **Key Features**:
    * Data entry with numeric type checks and positive value validation.
    * Tabular revenue breakdown (`Product`, `Quantity`, `Price`, `Revenue`).
    * Cumulative sales revenue computation using Python generator expressions.
    * Dynamic identification of top-performing product using `max()` with key extraction.

* **`25BTRAD119_PROBLEM SOLVING 4.py` — Enterprise Student Attendance Management System**
  * **Description**: A comprehensive educational administration system for tracking and auditing classroom attendance.
  * **Key Features**:
    * Batch registration for multiple students using comma-separated inputs.
    * Daily attendance marking with Present (`P`) and Absent (`A`) validations.
    * Historical record modification for past class sessions with bounds checking.
    * Formatted matrix table displaying student name, total present, absent count, and attendance percentage.
    * Attendance shortage detector flagging students falling below a user-defined threshold percentage.
    * Class summary statistics reporting overall student presence across all conducted sessions.
    * Direct student record search utility.

---

### 3. Foundational Tasks (Python Basics Tasks 1–18)

Interactive exercises covering fundamental programming syntax, I/O, and mathematical constructs:

* **Tasks 1–4: Basic Output & Pattern Formatting**
  * `TASK 1.py`: Basic multi-line output printing student name, department, and university.
  * `TASK 2.py`: Character block pattern generation (`*******`).
  * `TASK 3.py`: Single-line console string output (`"Python is Easy"`).
  * `TASK 4.py`: Sequential numerical pyramid generation (`1`, `12`, `123`, `1234`, `12345`).
* **Tasks 5–6: Whitespace & Escape Sequences**
  * `TASK 5.py`: Multi-line text splitting using newline (`\n`) escape sequences (`"Computer\nScience\nEngineering"`).
  * `TASK 6.py`: Tabular column alignment using horizontal tab (`\t`) sequences (`"Name\tAge\tCity"`).
* **Tasks 7–9: Documentation Comments**
  * `TASK 7.py`: Single-line explanatory comment syntax (`#`).
  * `TASK 8.py`: Multi-line documentation comment blocks (`"""`).
  * `TASK 9.py`: Interspersed procedural inline comments across statements.
* **Tasks 10–11: Variable Initialization & Assignment**
  * `TASK 10.py`: String variable declaration and reference printing.
  * `TASK 11.py`: Multi-variable assignment and sequential numeric display (`a = 10`, `b = 20`, `c = 30`).
* **Tasks 12–13: Type Inspection & Type Casting**
  * `TASK 12.py`: String-to-integer conversion (`int("100")`) and type validation with `type()`.
  * `TASK 13.py`: Integer-to-float conversion (`float(25)`) and type inspection.
* **Tasks 14–16: User Input & String Interpolation**
  * `TASK 14.py`: Dynamic integer input capture using `input()` and `int()`.
  * `TASK 15.py`: Two-number arithmetic addition from user prompts.
  * `TASK 16.py`: Multi-field user profile capture (`name`, `age`, `cgpa`) with formatted f-string interpolation.
* **Task 17: Temperature Conversion Formula**
  * `TASK 17.py`: Celsius to Fahrenheit conversion ($F = (C \times \frac{9}{5}) + 32$) with two-decimal-place precision (`{:.2f}`).
* **Task 18: Modulus & Parity Validation**
  * `TASK 18.py`: Even/Odd parity checking using the modulus operator (`num % 2 == 0`).

---

### 4. Experiential Learning Activity (Major Capstone Project)

#### 🛡️ HWGuard — Universal Hardware Vault & Cryptographic Anti-Tamper System

* **Architecture Overview**:
  HWGuard is an enterprise-grade, portable hardware integrity audit platform engineered to protect computers against covert hardware swapping, RAM theft, motherboard tampering, and unauthorized component alterations during servicing or transit.

* **Key Cryptographic & System Architecture**:
  * **Zero-Trust Hardware Snapshot (`hwsnap.py`)**:
    * Deep hardware auditing probing Motherboard serials, BIOS UUIDs, CPU identifiers, Memory module serials/slots, and Disk drive serials via WMI/SMBIOS (Windows), `ioreg`/`system_profiler` (macOS), and `/sys/class/dmi` (Linux).
    * **Zero Raw Serial Retention**: Raw serial numbers are never stored in plain text. Every component identifier is immediately mixed with a cryptographic salt and hashed using Keccak-256 (`hashlib.sha3_256`).
    * **Merkle Snapshot Root**: Combines all component digests into a single deterministic 256-bit root hash representing total system hardware state.
  * **Tamper-Evident State Management & GUI (`FINALPROJECT.py` / `hwguard.py`)**:
    * Desktop GUI built using Python's native `tkinter` and `ttk`.
    * Key derivation using `scrypt` ($N=32768, r=8, p=1$) with HMAC-SHA256 authenticated state tagging.
    * Append-only hash-chained state ledger (`state.json`) with cryptographic integrity verification (`chain_ok`).
    * Delta comparison engine auditing hardware changes and reporting states: `OK`, `NEW`, `MISSING`, or `MISMATCH`.
    * Battery cycle anomaly tracker detecting cycle rollbacks or heavy usage while in repair.
  * **Universal Multi-OS Launchers**:
    * `HWGuard.bat`: Native Windows launcher.
    * `HWGuard.command`: macOS launcher for Apple Silicon & Intel Macs.
    * `HWGuard.sh`: Linux shell auditor and dashboard launcher.
    * `HWGuard.html`: Offline HTML/JavaScript inspector for OTG mobile devices and browser audits.

---

## 🛠️ Technologies & Concepts Used

* **Programming Language:** Python 3.x
* **GUI Framework:** `tkinter`, `ttk`, `messagebox`
* **Cryptographic Primitives:**
  * Keccak-256 / SHA3-256 (`hashlib.sha3_256`)
  * Scrypt Key Derivation Function (`hashlib.scrypt`)
  * HMAC-SHA256 Authenticated Message Authentication (`hmac`)
  * Merkle Root Aggregation & Hash-Chained Ledgers
* **System & Hardware Probing:** `subprocess`, `platform`, `os`, `sys`, `pathlib`
* **Data Serialization & File I/O:** `json`, `csv` (`DictReader`), Text File Streams (`open`, `read`, `write`, `append`)
* **Core Programming Concepts:**
  * **Variables & Type Casting:** Dynamic typing, explicit conversions (`int()`, `float()`, `str()`).
  * **Control Flow:** Conditional branching (`if-elif-else`), iterative structures (`for`, `while`, `break`, `continue`).
  * **Exception Handling:** Robust fault tolerance using `try-except` blocks handling `ValueError`, `FileNotFoundError`, and `KeyError`.
  * **Functions & Recursion:** Modular functions, recursive problem decomposition, and parameter passing.
  * **Data Structures:** Lists, Dictionaries, Tuples, Sets, List Comprehensions, Slicing, and Sorting.
  * **Object-Oriented Programming (OOP):** Class design, encapsulation with private variables (`__balance`), instance methods, state tracking, and object modeling.

---

## 🚀 Execution & Setup Guide

### 1. Clone the Repository
```bash
git clone https://github.com/vaibhavvvvjain03/25BTRAD119_PYTHON.git
cd 25BTRAD119_PYTHON
```

### 2. Run Foundational Tasks
```bash
python "25BTRAD119_Problem Solving/25BTRAD119_TASK 1.py"
python "25BTRAD119_Problem Solving/25BTRAD119_TASK 17.py"
```

### 3. Run Lab Exercises
```bash
python "25BTRAD119_Lab Exercises/25BTRAD119_LAB EXERCISE 4.PY"
python "25BTRAD119_Lab Exercises/25BTRAD119_LAB EXERCISE 14.py"
```

### 4. Run Problem Solving Applications
```bash
python "25BTRAD119_Problem Solving/25BTRAD119_PROBLEM SOLVING 1.py"
python "25BTRAD119_Problem Solving/25BTRAD119_PROBLEM SOLVING 4.py"
```

### 5. Launch HWGuard Capstone Application
```bash
python "25BTRAD119_Experiential Learning Activity/hwguard.py"
```
*On Windows, you can also double-click `25BTRAD119_Experiential Learning Activity/HWGuard.bat` to launch.*

---

**Author:** VAIBHAV A JAIN  
**USN:** 25BTRAD119  
**Department:** Computer Science and Engineering (Artificial Intelligence and Data Engineering)  
**Institution:** Jain (Deemed-to-be University), Faculty of Engineering and Technology (FET)  
