"""
hwguard.py - HWGuard entry point
"""
import sys
from pathlib import Path

# Ensure directory is on python path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from FINALPROJECT import App

if __name__ == "__main__":
    App().mainloop()
