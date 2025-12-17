#!/usr/bin/env python3
"""
Evil Crow RF V2 - Safe ESP32 Flashing Script

Purpose:
    Build and flash firmware with reliable settings for ESP32-PICO-D4.
    Avoids common issues: stub flasher, high baud rates, flash erase instability.

Usage:
    python flash_esp32.py
        Normal build + flash (application only @ 0x10000)

    python flash_esp32.py --build-only
        Build firmware without flashing

    python flash_esp32.py --recovery
        Recovery flash using merged firmware (NO erase, @ 0x0)

    python flash_esp32.py --port COM9
        Specify serial port manually
"""

import sys
import subprocess
import argparse
from pathlib import Path
from datetime import datetime

try:
    import serial.tools.list_ports as list_ports
except ImportError:
    list_ports = None


# =========================================================
# ESP32 FLASHER CLASS
# =========================================================

class ESP32Flasher:
    def __init__(self, port=None, baud=74880, auto_detect=True):
        self.baud = baud
        self.project_root = Path(__file__).parent
        self.build_dir = self.project_root / ".pio" / "build" / "esp32dev"
        self.log_file = self.project_root / "flash_log.txt"

        self.port = port or (self.detect_port() if auto_detect else None)

        self.firmware_bin = self.build_dir / "firmware.bin"
        self.merged_bin = self.find_merged_bin()

    # -----------------------------------------------------
    # Logging
    # -----------------------------------------------------

    def log(self, msg, level="INFO"):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{ts}] [{level}] {msg}"
        print(line)
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(line + "\n")

    def run_cmd(self, cmd, desc=""):
        if desc:
            self.log(desc)
        self.log(f"Running: {' '.join(cmd)}")
        try:
            result = subprocess.run(cmd, cwd=self.project_root)
            return result.returncode == 0
        except Exception as e:
            self.log(str(e), "ERROR")
            return False

    # -----------------------------------------------------
    # Port Detection
    # -----------------------------------------------------

    def detect_port(self):
        self.log("Auto-detecting ESP32 serial port...")
        if list_ports:
            for p in list_ports.comports():
                ident = (p.description + p.hwid).upper()
                if any(x in ident for x in ["ESP32", "CP210", "CH340", "FTDI", "SILICON"]):
                    self.log(f"Detected port: {p.device}", "SUCCESS")
                    return p.device
        self.log("Auto-detection failed. Use --port", "WARNING")
        return None

    # -----------------------------------------------------
    # File Discovery
    # -----------------------------------------------------

    def find_merged_bin(self):
        if not self.build_dir.exists():
            return None
        merged = list(self.build_dir.glob("*.merged.bin"))
        return merged[0] if merged else None

    # -----------------------------------------------------
    # Checks
    # -----------------------------------------------------

    def verify_esptool(self):
        self.log("Checking esptool availability...")
        result = subprocess.run(
            ["python", "-m", "esptool", "version"],
            capture_output=True
        )
        if result.returncode != 0:
            self.log("esptool not found. Installing...", "WARNING")
            if not self.run_cmd(
                ["pip", "install", "esptool"],
                "Installing esptool"
            ):
                return False
        self.log("esptool is available", "SUCCESS")
        return True

    def sanity_check(self):
        if not self.port:
            self.log("No serial port specified", "ERROR")
            return False

        return self.run_cmd([
            "python", "-m", "esptool",
            "--no-stub",
            "--port", self.port,
            "--baud", str(self.baud),
            "chip-id"
        ], "Performing ESP32 sanity check")

    # -----------------------------------------------------
    # Build
    # -----------------------------------------------------

    def build(self):
        self.log("Building firmware with PlatformIO...")
        if not self.run_cmd(
            ["platformio", "run", "-e", "esp32dev"],
            "PlatformIO build"
        ):
            return False

        if not self.firmware_bin.exists():
            self.log("firmware.bin not found after build", "ERROR")
            return False

        self.log("Build completed successfully", "SUCCESS")
        return True

    # -----------------------------------------------------
    # Flashing
    # -----------------------------------------------------

    def flash_normal(self):
        self.log("Flashing firmware.bin (application only)")
        return self.run_cmd([
            "python", "-m", "esptool",
            "--no-stub",
            "--port", self.port,
            "--baud", str(self.baud),
            "write-flash", "0x10000",
            str(self.firmware_bin)
        ], "Writing firmware.bin")

    def flash_recovery(self):
        if not self.merged_bin:
            self.log("Merged firmware not found", "ERROR")
            return False

        self.log(f"Recovery flashing merged firmware: {self.merged_bin.name}")
        return self.run_cmd([
            "python", "-m", "esptool",
            "--no-stub",
            "--port", self.port,
            "--baud", str(self.baud),
            "write-flash", "0x0",
            str(self.merged_bin)
        ], "Writing merged firmware")

    # -----------------------------------------------------
    # Workflow
    # -----------------------------------------------------

    def run(self, build_only=False, recovery=False):
        self.log("=" * 60)
        self.log("Evil Crow RF V2 - Flashing Workflow")
        self.log("=" * 60)
        self.log("Normal flash  : firmware.bin @ 0x10000")
        self.log("Recovery flash: merged firmware @ 0x0")
        self.log("Baud rate     : 74880 (safe default)")
        self.log("=" * 60)

        # For build-only, just build (no port needed)
        if build_only:
            return self.build()

        # For flashing, verify esptool and port
        if not self.verify_esptool():
            return False

        if not self.sanity_check():
            return False

        # Normal or recovery flash
        if recovery:
            return self.flash_recovery()
        else:
            if not self.build():
                return False
            return self.flash_normal()


# =========================================================
# MAIN
# =========================================================

def main():
    parser = argparse.ArgumentParser(
        description="Evil Crow RF V2 - Safe ESP32 Flashing Script"
    )
    parser.add_argument("--port", help="Serial port (e.g. COM9)")
    parser.add_argument("--baud", type=int, default=74880,
                        help="Baud rate (default: 74880)")
    parser.add_argument("--build-only", action="store_true",
                        help="Build firmware only, do not flash")
    parser.add_argument("--recovery", action="store_true",
                        help="Recovery flash using merged firmware (NO erase)")

    args = parser.parse_args()

    flasher = ESP32Flasher(
        port=args.port,
        baud=args.baud
    )

    success = flasher.run(
        build_only=args.build_only,
        recovery=args.recovery
    )

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
