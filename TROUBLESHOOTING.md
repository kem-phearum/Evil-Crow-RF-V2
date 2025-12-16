# Troubleshooting Guide

This document provides solutions for common issues encountered when using Evil Crow RF V2.

## Table of Contents

1. [SD Card Issues](#sd-card-issues)
2. [RF Module Problems](#rf-module-problems)
3. [WiFi & Network Issues](#wifi--network-issues)
4. [Web Interface Problems](#web-interface-problems)
5. [Firmware & Build Issues](#firmware--build-issues)
6. [Signal Capture & Transmission Issues](#signal-capture--transmission-issues)
7. [Performance & Stability](#performance--stability)
8. [Getting Help](#getting-help)

---

## SD Card Issues

### Problem: "SD card not detected" or "Mount failed"

**Symptoms:**
- Web server shows blank page
- Serial output shows "SD card initialization failed"
- Configuration files not loading

**Solutions:**

1. **Verify card insertion**
   - Power off the device
   - Firmly reinsert the MicroSD card
   - Ensure the card clicks into place
   - Power on again

2. **Check card compatibility**
   - Use a smaller card (≤32GB) - larger cards have known issues
   - Verify card is FAT32 formatted
   - Try a different card to isolate the problem

3. **Verify folder structure**
   - SD card must have these folders:
     ```
     /HTML/
     /CONFIG/
     /SUBGHZ/  (optional but recommended)
     ```
   - Ensure folders are at the root level (not nested)

4. **Inspect pin connections**
   - Check SD card pin soldering
   - Verify pins match configuration:
     - SCLK: GPIO 18
     - MISO: GPIO 19
     - MOSI: GPIO 23
     - CS: GPIO 22

5. **Format the card**
   ```bash
   # On Windows: Right-click → Format → FAT32
   # On macOS: Disk Utility → Erase → MS-DOS (FAT)
   # On Linux: sudo mkfs.vfat -F 32 /dev/sdX
   ```

6. **Check power supply**
   - SD card initialization requires stable power
   - Use a 3.3V regulated supply
   - Add a 10µF decoupling capacitor near the SD card

**Serial Debugging:**
```
Enable serial monitor at 115200 baud and check for:
[INFO] SD Card: Mounting...
[ERROR] SD Card: Mount failed - Check pins and card
[SUCCESS] SD Card: Mounted successfully
```

### Problem: "Files on SD card but web server won't load"

**Solutions:**

1. **Check file permissions**
   - Ensure all files are readable
   - On Linux: `chmod 644 SD/HTML/*.html`

2. **Verify HTML file integrity**
   ```bash
   # Check that all HTML files exist
   ls -la SD/HTML/
   # Expected: index.html, config.html, rxconfig.html, txconfig.html, viewlog.html
   ```

3. **Replace with fresh copy**
   - Re-copy HTML files from `SD/HTML/` folder
   - Ensure no corruption during transfer

4. **Check file size limits**
   - Some SD cards have issues with specific file sizes
   - Try copying files one at a time to identify problematic file

---

## RF Module Problems

### Problem: "CC1101 module not responding" or "RF initialization failed"

**Symptoms:**
- Serial output shows "CC1101 not detected"
- RX/TX controls don't work
- No signal data in Log Viewer

**Solutions:**

1. **Verify SPI connections**
   - Check module wiring:
     - SCK: GPIO 14
     - MISO: GPIO 12
     - MOSI: GPIO 13
   - Verify CS pins:
     - Module 1: GPIO 5
     - Module 2: GPIO 27

2. **Test with basic connectivity**
   ```cpp
   // Add this to setup() for debugging:
   Serial.println("Checking CC1101 communication...");
   // Look for initialization messages in serial output
   ```

3. **Check SPI bus conflicts**
   - CC1101 modules share SPI with SD card
   - Ensure separate CS lines for each device
   - No other SPI devices on the same pins

4. **Verify power connections**
   - Module requires stable 3.3V
   - Add 10µF + 0.1µF capacitors near module
   - Check voltage with multimeter

5. **Test individual modules**
   - Power cycle the device
   - Check if either module responds
   - One module might be defective

6. **Check module quality**
   - Inspect for cold solder joints
   - Verify module markings (should say CC1101)
   - Some counterfeit modules have compatibility issues

**Serial Debugging:**
```
[INFO] Initializing CC1101 Module 1...
[ERROR] CC1101 Module 1: SPI communication failed
[SUCCESS] CC1101 Module 1: Ready

[INFO] Initializing CC1101 Module 2...
[ERROR] CC1101 Module 2: Not responding
[WARNING] Module 2 disabled - continuing with Module 1
```

### Problem: "Received data looks corrupted" or "Signals won't transmit"

**Solutions:**

1. **Adjust receiver bandwidth**
   - In RX Config: try different Rx Bandwidth values
   - Start with 200 kHz and adjust ±50 kHz
   - Too narrow = weak signals missed
   - Too wide = noise included

2. **Configure error tolerance**
   - Default: 200 µs
   - Increase for noisy RF environment
   - Decrease for cleaner signals

3. **Check antenna connections**
   - Verify antenna is soldered correctly
   - Try different antenna length (13cm for 433MHz)
   - Remove obstacles between device and target

4. **Adjust modulation settings**
   - Verify modulation matches signal (ASK, FSK, etc.)
   - Try common settings:
     - Frequency: 433.92 MHz (most common)
     - Modulation: ASK/OOK
     - Bandwidth: 200 kHz
     - Deviation: 0

5. **Check RF environment**
   - Move away from other RF sources
   - Reduce WiFi interference (use 5GHz band on your router)
   - Test in a different location

---

## WiFi & Network Issues

### Problem: "Cannot connect to WiFi AP" or "evilcrow-rf.local not found"

**Symptoms:**
- WiFi network not visible on phone/laptop
- Can't access http://evilcrow-rf.local/
- Web interface times out

**Solutions:**

1. **Verify WiFi AP is broadcasting**
   ```bash
   # Scan for the network
   # Windows: netsh wlan show networks
   # macOS: airport -s
   # Linux: nmcli dev wifi list
   ```
   - Look for "Evil Crow RF v2" network
   - If not found, check configuration files

2. **Check WiFi credentials**
   - Default SSID: `Evil Crow RF v2`
   - Default Password: `123456789ECRFv2`
   - To change:
     - Edit `SD/CONFIG/SSID.txt`
     - Edit `SD/CONFIG/PASS.txt`
     - Restart device

3. **Verify WiFi mode**
   - Check `SD/CONFIG/MODE.txt` contains "AP"
   - If in Station mode, device connects to existing network (not AP)

4. **Restart the device**
   - Power cycle (disconnect and reconnect power)
   - Wait 30 seconds for AP to stabilize
   - Then attempt to connect

5. **Check device IP address**
   - If mDNS doesn't work, use IP address
   - Default AP IP: `192.168.4.1`
   - Access: `http://192.168.4.1`

### Problem: "mDNS (.local) doesn't work on Linux"

**Symptoms:**
- `http://evilcrow-rf.local/` times out
- IP address access works fine

**Solutions:**

1. **Install avahi-daemon (mDNS service)**
   ```bash
   # Ubuntu/Debian
   sudo apt update && sudo apt install avahi-daemon

   # Fedora/RHEL
   sudo dnf install avahi-daemon

   # Arch
   sudo pacman -S avahi
   ```

2. **Start and enable the service**
   ```bash
   sudo systemctl start avahi-daemon
   sudo systemctl enable avahi-daemon

   # Verify it's running
   sudo systemctl status avahi-daemon
   ```

3. **Test mDNS resolution**
   ```bash
   avahi-browse -r _http._tcp
   # Should list "Evil Crow RF v2" service
   ```

4. **Troubleshoot if still not working**
   ```bash
   # Check if service is advertised
   dns-sd -B _http._tcp local

   # Manually resolve the hostname
   avahi-resolve-host-name evilcrow-rf.local
   ```

5. **Fallback to IP address**
   ```bash
   # If mDNS still doesn't work, use:
   http://192.168.4.1
   ```

---

## Web Interface Problems

### Problem: "Web server shows blank page or loads but no content"

**Symptoms:**
- http://192.168.4.1 loads but shows empty/white page
- JavaScript/CSS files don't load
- Buttons and controls don't appear

**Solutions:**

1. **Verify HTML files are on SD card**
   ```bash
   # Required files:
   SD/HTML/index.html
   SD/HTML/config.html
   SD/HTML/rxconfig.html
   SD/HTML/txconfig.html
   SD/HTML/viewlog.html
   SD/HTML/javascript.js
   SD/HTML/style.css
   ```
   - If missing, copy from project repository

2. **Check browser cache**
   - Hard refresh: Ctrl+Shift+Del (Windows) or Cmd+Shift+Del (Mac)
   - Clear all cookies for 192.168.4.1
   - Try different browser (Chrome, Firefox, Safari)

3. **Check browser console for errors**
   - Press F12 to open Developer Tools
   - Go to Console tab
   - Look for error messages
   - Try `http://192.168.4.1` directly

4. **Verify AsyncWebServer is running**
   - Serial output should show port 80 listening
   - Check for server initialization errors

5. **Restart the device**
   - Power cycle the device
   - Wait 10 seconds
   - Access the web interface again

6. **Check available storage**
   - Large HTML files might exceed available memory
   - Verify SD card has free space
   - Try removing other files from SD card

### Problem: "Form submissions don't work" or "Settings won't save"

**Solutions:**

1. **Check SD card write permissions**
   - Device must be able to write to CONFIG folder
   - Verify SD card isn't read-only

2. **Verify form fields**
   - Ensure all required fields are filled
   - Check browser console for JavaScript errors

3. **Check AsyncWebServer is handling requests**
   - Enable serial debugging
   - Should see POST requests logged
   - Check for "Request received" messages

4. **Clear browser cache and cookies**
   - F12 → Application/Storage tab
   - Delete all local storage for the site

---

## Firmware & Build Issues

### Problem: "Build fails" or "Compilation errors"

**Symptoms:**
- `platformio run` shows error messages
- Red squiggly lines in VS Code editor
- Build doesn't complete

**Solutions:**

1. **Clean and rebuild**
   ```bash
   # Remove build artifacts
   platformio run --environment esp32dev --target clean

   # Rebuild everything
   platformio run --environment esp32dev
   ```

2. **Update dependencies**
   ```bash
   # Update all libraries
   platformio pkg update

   # Or reinstall specific library
   platformio lib install "AsyncTCP"
   ```

3. **Check Python environment**
   ```bash
   # Verify Python is available
   python --version

   # Should be Python 3.7 or newer
   ```

4. **Verify platformio.ini**
   - Ensure file is not corrupted
   - Check board name: `board = esp32dev`
   - Check framework: `framework = arduino`

5. **Check for missing libraries**
   - ElegantOTA build flag must be set
   - Library dependencies in platformio.ini:
     ```ini
     lib_deps =
         https://github.com/ESP32Async/ESPAsyncWebServer.git
         https://github.com/ESP32Async/AsyncTCP.git
         ayushsharma82/ElegantOTA
     ```

### Problem: "Upload fails" or "Port not found"

**Symptoms:**
- "COM port not found" error
- "Permission denied" (Linux/Mac)
- Device appears to upload but doesn't work

**Solutions:**

1. **Verify device is connected**
   ```bash
   # List connected devices
   platformio device list

   # Or use:
   # Windows: Device Manager → Ports (COM & LPT)
   # Linux: ls /dev/ttyUSB* or /dev/ttyACM*
   # Mac: ls /dev/tty.usbserial*
   ```

2. **Install USB drivers**
   - Windows: CP2104 USB driver (likely needed)
   - macOS: Usually automatic
   - Linux: Usually automatic

3. **Fix permission issues (Linux/Mac)**
   ```bash
   # Add user to dialout group
   sudo usermod -a -G dialout $USER

   # Or use sudo
   sudo platformio run --environment esp32dev --target upload
   ```

4. **Try different USB cable/port**
   - Some USB cables are data-only without power
   - Try different USB port on computer

5. **Reset ESP32**
   - Press BOOT button on ESP32
   - Hold for 2 seconds
   - Release and try upload again

### Problem: "Serial monitor shows garbage/corrupted output"

**Solutions:**

1. **Verify baud rate is 115200**
   ```bash
   platformio device monitor --baud 115200
   ```

2. **Check USB cable quality**
   - Poor quality cable can cause data corruption
   - Try different cable

3. **Reset ESP32**
   - Press EN (reset) button
   - Output should become clear

---

## Signal Capture & Transmission Issues

### Problem: "No signals appearing in Log Viewer"

**Symptoms:**
- RX Config appears to work
- But Log Viewer shows nothing or "No signals received"
- Other modules' signals work fine

**Solutions:**

1. **Verify RX is enabled**
   - Check RX Config page
   - Module should be selected (1 or 2)
   - Frequency should match target device

2. **Check RF module assignment**
   - Verify correct module is selected
   - Try the other module

3. **Verify antenna is connected**
   - Check antenna soldering
   - Try different antenna
   - Test without antenna nearby (some RF interference)

4. **Adjust RF parameters**
   - Try different modulation (ASK/OOK, FSK)
   - Adjust bandwidth (try 200-300 kHz range)
   - Verify frequency (common: 433.92, 868, 915 MHz)

5. **Test with known signal**
   - Use a commercial RF remote
   - Point at device and press button
   - Should appear in Log Viewer

6. **Check error tolerance**
   - Default: 200 µs
   - Increase to 300-500 µs if signals are weak
   - Decrease to 100 µs if signals are clean

### Problem: "Transmitted signals don't work"

**Symptoms:**
- TX Raw Data submits successfully
- But target device doesn't respond
- Signal was captured but replay fails

**Solutions:**

1. **Verify signal data format**
   - Should contain comma-separated numbers
   - Example: `1000,500,250,500,...`
   - Copy from "Corrected" data in Log Viewer

2. **Check TX module selection**
   - Verify correct module selected
   - Use same module you used for RX

3. **Verify transmission parameters**
   - Frequency should match original
   - Modulation must match original
   - Deviation must match original

4. **Test transmission power**
   - Default power level should work
   - Try increasing if no response
   - Move closer to target device

5. **Check antenna and connections**
   - Verify TX antenna is soldered
   - Test with known receiver

6. **Verify target device**
   - Test with known working remote
   - Make sure target device is powered
   - Check battery level

---

## Performance & Stability

### Problem: "Device reboots unexpectedly" or "Watchdog resets"

**Symptoms:**
- Serial output shows "Guru Meditation Error"
- Device reboots while capturing signals
- Performance degrades over time

**Solutions:**

1. **Check power supply stability**
   - Use quality 5V USB power adapter
   - Add capacitors near ESP32 (100µF + 10µF)
   - Measure voltage with multimeter (should be 5.0V ±0.3V)

2. **Monitor heap memory**
   - Serial output shows free heap
   - If approaches 0, memory leak possible
   - Try restarting device

3. **Reduce sample size**
   - Edit main.cpp: `#define samplesize 2000`
   - Try reducing to 1000 samples
   - Less memory usage = more stability

4. **Disable unused features**
   - If only using one module, disable other
   - Disable OTA updates if not needed
   - Reduce WiFi transmit power

5. **Check for infinite loops**
   - Serial debugging to identify where reboot occurs
   - Look for tight loops without delays

### Problem: "Web interface is slow" or "unresponsive"

**Solutions:**

1. **Reduce WiFi interference**
   - Move away from microwave/cordless phones
   - Use 5GHz WiFi if available
   - Check WiFi signal strength

2. **Reduce sample/data rate**
   - Capturing too much data slows web interface
   - Reduce sample size or data rate

3. **Clear browser cache**
   - Force refresh: Ctrl+Shift+F5
   - Clear cookies for 192.168.4.1

4. **Restart device**
   - Power cycle the device
   - Reconnect to WiFi

5. **Reduce simultaneous connections**
   - Only connect from one device
   - Disconnect other devices from WiFi

---

## Getting Help

If you've tried the above solutions and still have issues:

1. **Check existing GitHub issues**
   - [GitHub Issues](https://github.com/joelsernamoreno/EvilCrowRF-V2/issues)
   - Your problem might already be solved

2. **Post on Discord**
   - [Evil Crow RF Discord](https://discord.gg/evilcrowrf)
   - Helpful community members

3. **Create a detailed bug report**
   - Follow [CONTRIBUTING.md](CONTRIBUTING.md)
   - Include hardware setup, steps to reproduce, serial output
   - Use bug report template: `.github/ISSUE_TEMPLATE/bug_report.md`

4. **Contact the developer**
   - [@JoelSernaMoreno](https://twitter.com/JoelSernaMoreno) on Twitter

### Information to Provide

When asking for help, please include:

- ✅ Exact error message/symptoms
- ✅ Hardware configuration (ESP32 model, CC1101 count, etc.)
- ✅ Firmware version and build date
- ✅ Steps to reproduce the issue
- ✅ Serial output (copy paste from serial monitor)
- ✅ What you've already tried
- ✅ Screenshots if relevant

---

**Last Updated:** December 16, 2025
