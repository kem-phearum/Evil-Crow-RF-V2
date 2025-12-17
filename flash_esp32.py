#!/usr/bin/env python3
"""
Evil Crow RF V2 - PlatformIO-Compatible Flash Script

This script mimics:
    platformio run -e esp32dev -t upload

Usage:
    python flash_esp32.py
        Build + flash (recommended)

    python flash_esp32.py --build-only
        Only build firmware (no flashing)

    python flash_esp32.py --port COM3
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
# Minimal console logging
# =========================================================

def log(msg, level="INFO"):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [{level}] {msg}")


def section(title):
    print("\n" + "=" * 64)
    print(title)
    print("=" * 64)


def run(cmd, cwd=None):
    log(" ".join(cmd))
    return subprocess.run(cmd, cwd=cwd).returncode == 0


# =========================================================
# Serial port detection
# =========================================================

def detect_port():
    if not list_ports:
        return None

    for p in list_ports.comports():
        ident = (p.description + p.hwid).upper()
        if any(x in ident for x in ("ESP32", "CP210", "CH340", "FTDI", "SILICON")):
            log(f"Detected port: {p.device}", "SUCCESS")
            return p.device

    return None


# =========================================================
# PlatformIO-style flasher
# =========================================================

class PlatformIOFlasher:
    def __init__(self, port=None):
        self.root = Path(__file__).parent
        self.build = self.root / ".pio" / "build" / "esp32dev"

        self.port = port or detect_port()
        if not self.port:
            log("No serial port detected. Use --port COMx", "ERROR")
            sys.exit(1)

        # Build artifacts
        self.bootloader = self.build / "bootloader.bin"
        self.partitions = self.build / "partitions.bin"
        self.firmware = self.build / "firmware.bin"

        # PlatformIO framework boot_app0.bin
        self.boot_app0 = (
            Path.home()
            / ".platformio"
            / "packages"
            / "framework-arduinoespressif32"
            / "tools"
            / "partitions"
            / "boot_app0.bin"
        )

    # -----------------------------------------------------

    def build_firmware(self):
        section("BUILD")
        log("Building firmware with PlatformIO")

        if not run(["platformio", "run", "-e", "esp32dev"], cwd=self.root):
            log("Build failed", "ERROR")
            sys.exit(1)

        for f in (self.bootloader, self.partitions, self.boot_app0, self.firmware):
            if not f.exists():
                log(f"Missing required file: {f}", "ERROR")
                sys.exit(1)

        log("Build completed successfully", "SUCCESS")

    # -----------------------------------------------------

    def flash(self):
        section("FLASH")
        log("Flashing using PlatformIO upload sequence")

        cmd = [
            "python", "-m", "esptool",
            "--chip", "esp32",
            "--port", self.port,
            "--baud", "460800",
            "write-flash",
            "--flash-mode", "dio",
            "--flash-freq", "40m",
            "--flash-size", "4MB",
            "0x1000", str(self.bootloader),
            "0x8000", str(self.partitions),
            "0xe000", str(self.boot_app0),
            "0x10000", str(self.firmware),
        ]

        if not run(cmd):
            log("Flash failed", "ERROR")
            sys.exit(1)

        log("Flash completed successfully", "SUCCESS")


# =========================================================
# Entry point
# =========================================================

def main():
    parser = argparse.ArgumentParser(
        description="Evil Crow RF V2 – PlatformIO-compatible flasher"
    )
    parser.add_argument("--port", help="Serial port (COMx)")
    parser.add_argument("--build-only", action="store_true")

    args = parser.parse_args()

    section("NEW FLASH SESSION")
    flasher = PlatformIOFlasher(port=args.port)

    flasher.build_firmware()

    if not args.build_only:
        flasher.flash()


if __name__ == "__main__":
    main()
