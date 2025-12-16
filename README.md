# Evil Crow RF v2

![EvilCrow](https://github.com/joelsernamoreno/EvilCrowRF-V2/blob/main/images/Logo1.png)

A professional-grade radiofrequency hacking device for penetration testing and Red Team operations. This PlatformIO-based firmware for ESP32 provides RF signal capture, analysis, transmission, and jamming capabilities using CC1101 radio modules. This project enables control of various wireless devices such as doorbells, garage doors, remote controls, and other SubGHz-enabled devices.

## Credits

**Idea, development and implementation:** Joel Serna (@JoelSernaMoreno)

**Main collaborator:** Little Satan (https://github.com/LSatan/)

**Other collaborators:** Jordi Castelló (@iordic), Eduardo Blázquez (@_eblazquez), Federico Maggi (@phretor), Andrea Guglielmini (@Guglio95) and RFQuack (@rfquack)

**PCB design:** Ignacio Díaz Álvarez (@Nacon_96), Forensic Security (@ForensicSec) and April Brother (@aprbrother)

**Manufacturer and distributor:** April Brother (@aprbrother)

**Distributor from United Kingdom:** KSEC Worldwide (@KSEC_KC)

The developers and collaborators of this project do not earn money with this project. You can invite the developers for a coffee to further develop Low-Cost hacking devices. If you don't invite them for a coffee, nothing happens—development will continue.

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/E1E614OA5)

## Where to Buy

**Available with April Brother (shipping from China):**
- [Evil Crow RF V2 Tindie](https://www.tindie.com/products/aprbrother/evil-crow-rf-v2-rf-transceiver-rf/)
- [Evil Crow RF V2 Alibaba](https://www.alibaba.com/product-detail/Evil-Crow-RF2-signal-receiver-with_1600467911757.html)
- [Evil Crow RF V2 Aliexpress](https://www.aliexpress.com/item/3256807682636637.html)

**Available with SAPSAN Cybersec & Military (shipping from EU, Poland):**
- [SAPSAN Shop](https://sapsan-sklep.pl/en/products/evil-crow-rf-v2)

**Available with KSEC Worldwide (shipping from United Kingdom):**
- [Evil Crow RF V2](https://labs.ksec.co.uk/product/evil-crow-rf-v2/)
- [Evil Crow RF V2 Lite](https://labs.ksec.co.uk/product/evil-crow-rf2-lite/)

**Available with Tienda Espía (shipping from Mexico):**
- [Tienda Espía](https://tiendaespia.com.mx/producto/evil-crow-rf-v2-radiofrequency-hacking-device/)

**Community:** [Discord Group](https://discord.gg/evilcrowrf)

## ⚠️ Disclaimer

Evil Crow RF V2 is a basic device for professionals and cybersecurity enthusiasts.

**We are not responsible for the incorrect use of Evil Crow RF V2.**

**Be careful with this device and the transmission of signals. Make sure to follow the laws that apply to your country.**

We recommend using this device for testing, learning and fun. This device is intended for authorized security testing, research, and educational purposes only.

## Overview

Evil Crow RF V2 is a radiofrequency hacking device for pentest and Red Team operations. This device operates in the following radiofrequency bands:

- **300 MHz - 348 MHz**
- **387 MHz - 464 MHz**
- **779 MHz - 928 MHz**
- **2.4 GHz**

Evil Crow RF V2 has two CC1101 radiofrequency modules (configurable for simultaneous or independent operation), and optionally a NRF24L01 module for additional attack vectors.

### Supported Attacks

- Signal receiver and analyzer
- Signal transmitter and replayer
- Replay attacks
- Mousejacking (with NRF24L01)
- Jamming/DoS attacks
- And more...

**NOTE:** All devices are flashed with basic firmware before shipping. For feature requests, please develop code and submit a PR rather than requesting new implementations.

## Features

- **Dual CC1101 Radio Modules**: Support for two independent CC1101 RF transceivers operating in the SubGHz frequency range (can operate simultaneously)
- **RF Signal Capture & Analysis**: Receive and analyze RF signals with real-time sample collection and smoothing
- **Signal Replay**: Transmit captured or pre-stored RF signals
- **Jamming Capability**: Generate RF noise/jamming signals across configured frequencies
- **Web Interface**: AsyncWebServer-based web UI for configuration and control via HTTP
- **Wireless AP Mode**: Built-in WiFi Access Point mode for easy connectivity
- **MicroSD Card Support**: Persistent storage for configuration files and pre-loaded RF signal files
- **Modular RF Signal Library**: Extensive collection of pre-captured SubGHz signals organized by device type
- **OTA Updates**: Elegant OTA firmware update support via AsyncWebServer
- **Signal Library**: Over 100 pre-captured signals for doorbells, garage doors, smart devices, and more

## Hardware Requirements

- **ESP32 DevKit** (or compatible ESP32 development board)
- **2x CC1101 RF Modules** (Configurable for specific GPIO pins)
- **MicroSD Card** (For configuration storage and signal files)
- **SPI Interface** (For CC1101 communication)

### Pin Configuration

**MicroSD Card (VSPI):**
- SCLK: GPIO 18
- MISO: GPIO 19
- MOSI: GPIO 23
- CS: GPIO 22

**CC1101 Module 1 (HSPI):**
- SCK: GPIO 14
- MISO: GPIO 12
- MOSI: GPIO 13
- RX: GPIO 4
- TX: GPIO 2
- CS: GPIO 5

**CC1101 Module 2 (HSPI - Shared SPI):**
- RX: GPIO 26
- TX: GPIO 25
- CS: GPIO 27

## Project Structure

```
Evil-Crow-RF-V2/
├── src/
│   ├── main.cpp                        # Main firmware code
│   ├── ELECHOUSE_CC1101_SRC_DRV.cpp   # CC1101 driver implementation
│   └── ELECHOUSE_CC1101_SRC_DRV.h     # CC1101 driver header
├── SD/
│   ├── CONFIG/                         # Configuration files
│   │   ├── SSID.txt                   # WiFi SSID
│   │   ├── PASS.txt                   # WiFi password
│   │   ├── MODE.txt                   # WiFi mode (AP/STA)
│   │   ├── BUTTON1.txt                # Button 1 configuration
│   │   ├── BUTTON2.txt                # Button 2 configuration
│   │   ├── KAIJU_API.txt              # API endpoint configuration
│   │   ├── JAMMER_LOCAL_IP.txt        # Jammer IP settings
│   │   ├── LAST_SELECTED.txt          # Last used signal
│   │   └── PASS.txt                   # Device password
│   ├── HTML/                           # Web interface files
│   │   ├── index.html                 # Main dashboard
│   │   ├── config.html                # Configuration page
│   │   ├── rxconfig.html              # RX configuration
│   │   ├── txconfig.html              # TX configuration
│   │   ├── viewlog.html               # Log viewer
│   │   ├── javascript.js              # Frontend scripts
│   │   └── style.css                  # UI styling
│   └── SUBGHZ/                         # Pre-captured RF signals organized by type
│       ├── Doorbell/                  # Doorbell signals
│       ├── Tesla/                     # Tesla charge port signals
│       ├── Kaiju/                     # Kaiju device signals
│       ├── Fans/                      # Smart fan control signals
│       ├── Open_Sesame_EU/            # EU frequency variants
│       ├── Open_Sesame_US/            # US frequency variants
│       ├── Lift_Master_EU/            # Lift/garage door signals
│       └── Misc/                      # Miscellaneous signals
├── include/                            # Header files directory
├── lib/                                # Library dependencies
├── platformio.ini                      # PlatformIO configuration
└── README.md                           # This file
```

## Configuration

Configuration files are stored on the MicroSD card in the `SD/CONFIG/` directory:

### WiFi Configuration
- **SSID.txt**: WiFi network name (Default: "Evil Crow RF v2")
- **PASS.txt**: WiFi password (Default: "123456789ECRFv2")
- **MODE.txt**: WiFi mode - "AP" for Access Point or "STA" for Station mode

### RF Module Configuration
- **Button configuration files** for quick signal presets
- **KAIJU_API.txt**: Remote API endpoint for device integration
- **JAMMER_LOCAL_IP.txt**: Local network settings for jamming functions

### Fallback Defaults
If SD card fails, the firmware falls back to:
- SSID: "Evil Crow RF v2"
- Password: "123456789ECRFv2"
- Mode: "AP" (Access Point)

## Building & Flashing

### Quick Start

**Recommended:** Use PlatformIO CLI or PlatformIO IDE (simpler than Arduino IDE)

#### Option 1: PlatformIO with VS Code (Recommended)

PlatformIO is the modern, recommended approach for Evil Crow RF V2 development with excellent VS Code integration.

**Prerequisites:**
- VS Code (Download from [code.visualstudio.com](https://code.visualstudio.com))
- Python 3.7+ (Download from [python.org](https://www.python.org))
- Git (Download from [git-scm.com](https://git-scm.com))

**Step 1: Install PlatformIO Extension in VS Code**
1. Open VS Code
2. Go to **Extensions** (Ctrl+Shift+X / Cmd+Shift+X)
3. Search for "PlatformIO IDE"
4. Click **Install** on the official PlatformIO IDE extension by PlatformIO
5. Wait for installation to complete and reload VS Code

**Step 2: Clone the Repository**
1. Open the **PlatformIO Home** (click the PlatformIO icon in the left sidebar)
2. Click **Open Project**
3. Or use the terminal:
   ```bash
   git clone https://github.com/joelsernamoreno/EvilCrowRF-V2.git
   cd Evil-Crow-RF-V2
   ```
4. Open the cloned folder in VS Code (**File → Open Folder**)

**Step 3: Prepare MicroSD Card Content**
1. Before building, prepare your MicroSD card:
   - Copy the `SD/HTML/` folder to your MicroSD card
   - Copy the `SD/CONFIG/` folder to your MicroSD card
   - (Optional) Copy the `SD/SUBGHZ/` folder with RF signal files
2. Insert the MicroSD card into Evil Crow RF V2 after flashing

**Step 4: Build the Project**
1. PlatformIO will automatically detect `platformio.ini` and download dependencies
2. Click the **PlatformIO: Build** button in the bottom status bar (checkmark icon)
   - Or use keyboard shortcut: Press the PlatformIO icon → select **Build** → choose **esp32dev**
   - Or use terminal: `platformio run --environment esp32dev`
3. Monitor the build output in the integrated terminal
4. Build should complete successfully with no errors

**Step 5: Upload Firmware to Device**
1. Connect your ESP32 device via USB cable
2. Click the **PlatformIO: Upload** button in the bottom status bar (right arrow icon)
   - Or use terminal: `platformio run --environment esp32dev --target upload`
3. Monitor the upload progress in the terminal
4. When complete, you'll see "Uploading" finished message

**Step 6: Monitor Serial Output**
1. Click the **PlatformIO: Monitor** button in the bottom status bar (plug icon)
   - Or use terminal: `platformio device monitor --baud 115200`
2. Serial output will display in the integrated terminal
3. You'll see boot messages and initialization logs
4. This helps verify the device is working correctly

**VS Code Tips & Tricks**

**PlatformIO Buttons (Bottom Status Bar):**
- **Checkmark**: Build the project
- **Right Arrow**: Upload firmware
- **Plug Icon**: Open serial monitor
- **Trash Icon**: Clean build files
- **Home Icon**: Open PlatformIO Home

**Keyboard Shortcuts:**
- `Ctrl+Alt+B` - Build
- `Ctrl+Alt+U` - Upload
- `Ctrl+Alt+S` - Serial Monitor
- `Ctrl+Alt+C` - Clean

**Debugging:**
- Set breakpoints by clicking in the left margin of code
- Use the Debug Console for inspection
- Configure debugging in `.vscode/launch.json`

**IntelliSense & Code Completion:**
- Hover over functions to see documentation
- Press `Ctrl+Space` for autocomplete
- Press `F12` to go to definition
- Press `Ctrl+Shift+F10` to find all references

**Terminal Integration:**
- Use integrated terminal (Ctrl+`) for git commands
- Run custom platformio commands:
  ```bash
  platformio device list          # List connected devices
  platformio run --list-targets   # Show available build targets
  platformio pkg list             # List installed dependencies
  ```

**Recommended VS Code Extensions:**
- **C/C++ IntelliSense** - Better code completion
- **GitLens** - Advanced Git integration
- **Prettier** - Code formatter
- **Serial Monitor** - Alternative serial viewer
- **Cortex Debug** - Enhanced debugging (for ARM debugging)

**Troubleshooting VS Code + PlatformIO:**

| Issue | Solution |
|-------|----------|
| **Extension won't install** | Restart VS Code, check Python installation |
| **Build fails / dependencies missing** | Run `platformio pkg update`, delete `.pio` folder and rebuild |
| **Upload fails - port not found** | Check USB cable, run `platformio device list` to verify port |
| **Serial monitor won't open** | Close other serial terminal apps, check COM port in Device Manager |
| **IntelliSense not working** | Rebuild project, close and reopen VS Code |
| **Command palette shows no PlatformIO** | Ensure extension is fully installed (wait 2-3 minutes after install) |

**Project Structure in VS Code:**
```
.pio/                      # PlatformIO build artifacts
.vscode/                   # VS Code configuration
├── c_cpp_properties.json  # IntelliSense settings
└── launch.json           # Debug configuration
src/                       # Source code
include/                   # Header files
lib/                       # Local libraries
test/                      # Unit tests
platformio.ini            # PlatformIO configuration
README.md                 # This file
```

**Next Steps:**
1. After successful upload, proceed to [SD Card Setup](#sd-card-setup)
2. Copy HTML/CONFIG/SUBGHZ folders to your MicroSD card
3. Insert SD card and power on the device
4. Connect to WiFi and access the web interface

## SD Card Setup

**Critical:** Copy the HTML and CONFIG files to your MicroSD card before first use.

1. Format a MicroSD card (32GB or smaller recommended; larger cards may cause issues)
2. Create the following folder structure:
   ```
   /HTML/     (copy from SD/HTML/)
   /CONFIG/   (copy from SD/CONFIG/)
   /SUBGHZ/   (copy from SD/SUBGHZ/ - optional but recommended)
   ```
3. Insert the MicroSD card into the device
4. Power on Evil Crow RF V2

**Troubleshooting SD Card Issues:**

- **Web server won't load / blank page:** Verify you've copied the HTML folder to the SD card and the card is inserted
- **Files are on SD card but web server still won't work:** Use a smaller SD card (≤32GB). Larger cards have known compatibility issues
- **No SD card detected:** Check card insertion and verify pin configuration

## Web Interface

The device hosts a web server on port 80 when in Access Point mode. 

### First Steps

1. **Verify SD Card:** Check that you've copied the HTML folder to your MicroSD card
2. **Insert SD Card & Power On:** Insert the MicroSD card into Evil Crow RF V2 and connect to power/battery
3. **Connect to WiFi:** Look for the WiFi network:
   - **SSID:** `Evil Crow RF v2`
   - **Password:** `123456789ECRFv2`
4. **Connect from your device:** Use your laptop/phone to connect to this WiFi network
5. **Access Web Panel:** Open your browser and navigate to:
   - **Primary (mDNS):** http://evilcrow-rf.local/
   - **Fallback (IP address):** http://192.168.4.1/

**Note:** If mDNS access doesn't work on Linux:
- Install avahi-daemon: `sudo systemctl install avahi-daemon`
- Start it: `sudo systemctl start avahi-daemon && sudo systemctl enable avahi-daemon`
- Or use the direct IP address: http://192.168.4.1/

### Web Interface Pages

#### Home
Displays device information and status, including:
- Device uptime
- WiFi connection status
- Module initialization status
- Signal reception statistics

#### RX Config
Configure the CC1101 modules for receiving signals. Received signals appear in the Log Viewer.

**Parameters:**
- **Module:** Select 1 or 2 (which CC1101 module to configure)
- **Modulation:** Modulation scheme (e.g., ASK/OOK, FSK, GFSK)
- **Frequency:** RF frequency in MHz (e.g., 433.92)
- **Rx Bandwidth:** Receiver bandwidth setting
- **Deviation:** Frequency deviation
- **Data Rate:** Data rate setting

#### Log Viewer
Displays received RF signals in real-time with:
- Raw signal data
- Signal analysis and smoothing
- Frequency and modulation details
- Corrected/smoothed samples for easier signal replay

#### TX Config

##### TX Raw Data
Transmit raw RF signal data:
- **Module:** Select 1 or 2 (which CC1101 module to use for transmission)
- **Modulation:** Modulation scheme
- **Frequency:** Transmission frequency
- **RAW Data:** Raw signal data (paste corrected data from Log Viewer or pre-stored signals)
- **Deviation:** Frequency deviation

##### Jammer
Enable jamming/denial of service on specific frequencies:
- **Module:** Select 1 or 2
- **Frequency:** Target frequency to jam
- **Power:** Jamming power level (typically 1-12)

#### Config
WiFi and device configuration:
- **SSID:** WiFi network name (change from Evil Crow RF v2)
- **Password:** WiFi password (change from default)
- **Mode:** WiFi mode selection (AP/Station)
- **Reset to Defaults:** Clear stored WiFi configuration

**Note:** Evil Crow RF V2 is configured in **Station Mode by default**. Changes are saved to the MicroSD card and persist after restart. Use the reset option to return to factory defaults.

## RF Signal Files

Pre-captured signal files are stored in `.sub` format in the `SD/SUBGHZ/` directory. Organization includes:

| Category | Use Case | Example Signals |
|----------|----------|-----------------|
| **Doorbell/** | Wireless doorbell signals | Various brands (Sadotech, GE, KlikAanKlikUit, etc.) |
| **Tesla/** | Tesla Charge Port Opener | 315MHz & 433MHz variants (AM270/AM650) |
| **Kaiju/** | Kaiju remote device signals | Button 1 SYNC variants |
| **Fans/** | Smart fan controls | Power, Speed, Swing, Timer |
| **Lift_Master_EU/** | Garage door openers | 433MHz EU variant |
| **Open_Sesame_EU/US/** | Frequency-specific signals | 9/10-bit variants for different regions |
| **Misc/** | General purpose signals | Gate openers, cross-walk signals, etc. |

## Key Functionality

### Signal Capture
- Real-time RF signal sampling with configurable sample size (default 2000 samples)
- Automatic signal smoothing and filtering
- Error tolerance configuration (default ±200μs)
- Support for multiple modulation types (ASK, OOK, FSK, etc.)

### Signal Transmission
- Replay captured or pre-stored signals
- Configurable transmission power
- Supports multiple modulation schemes
- Real-time frequency and data rate configuration

### Analysis Tools
- Signal frequency analysis
- Deviation calculation
- Modulation type detection
- Data rate measurement
- Output logging to file system

### Jamming
- Configurable jamming signal parameters
- Power level adjustment
- Frequency band selection
- Local or remote control via API

## Dependencies

**PlatformIO Libraries:**
- `ESPAsyncWebServer` - Async HTTP server for ESP32
- `AsyncTCP` - Async TCP library for ESP32
- `ElegantOTA` - Over-The-Air firmware update library
- Arduino Core libraries (WiFi, SPI, SD, LittleFS, mDNS)

See `platformio.ini` for specific repository links.

## Logging & Debugging

- Serial output at 115200 baud
- File-based logging to MicroSD card
- Web-based log viewer interface
- Real-time signal analysis output via Log Viewer

## Troubleshooting

### SD Card Not Detected
- Verify MicroSD card is properly inserted
- Check pin configuration matches hardware setup
- Firmware will fall back to default WiFi credentials
- Use smaller SD cards (≤32GB) for reliability

### RF Module Not Responding
- Verify CC1101 module connections
- Check SPI pin configuration
- Ensure CS pins are correctly assigned
- Monitor serial output for initialization errors

### WiFi Connection Issues
- Verify SSID.txt and PASS.txt in SD card CONFIG folder
- Default credentials: SSID `Evil Crow RF v2` / Password `123456789ECRFv2`
- Restart the device and check WiFi AP broadcast
- Configuration is stored on SD card and persists across reboots

### Web Interface Not Loading
- Verify HTML folder is on the MicroSD card
- Check that AsyncWebServer is properly initialized
- Try accessing via IP: http://192.168.4.1/
- Verify SD card is inserted and readable
- Check that files are properly copied to SD/HTML/

### mDNS (.local) Resolution Issues
- On Linux: Install and start avahi-daemon (see Web Interface section)
- Use direct IP address as fallback: http://192.168.4.1/
- Ensure your device supports mDNS

## Technical Details

### RF Specifications
- **Operating Bands:** 300-348 MHz, 387-464 MHz, 779-928 MHz, 2.4 GHz
- **Modulation Support:** ASK/OOK, FSK, GFSK, and more
- **Sampling:** Up to 2000 samples with automatic smoothing
- **Error Tolerance:** Configurable (default ±200μs)

### Device Architecture
- **Main MCU:** ESP32 (WiFi + Bluetooth capable)
- **RF Modules:** 2x CC1101 (configurable for simultaneous dual-band operation)
- **Storage:** MicroSD card (SPI interface) + LittleFS
- **Web Server:** ESPAsyncWebServer
- **Networking:** WiFi (802.11 b/g/n), mDNS for local discovery

### API & Control

The device provides:
- Async HTTP endpoints for RF control
- Real-time web interface via AsyncWebServer
- mDNS support for local network discovery (.local domains)
- Configuration persistence via MicroSD card

## Support & Community

- **Discord Community:** [Join the Discord Group](https://discord.gg/evilcrowrf) for discussions and support
- **Issues & Questions:** Open an issue on GitHub or contact [@JoelSernaMoreno](https://twitter.com/JoelSernaMoreno) on Twitter
- **Contributing:** Code contributions and PRs are welcome! Please submit pull requests with new features or improvements

## Alternative Firmware

You can also use alternative firmware implementations for Evil Crow RF V2:

- [h-RAT/EvilCrowRF_Custom_Firmware_CC1101_FlipperZero](https://github.com/h-RAT/EvilCrowRF_Custom_Firmware_CC1101_FlipperZero)
- [realdaveblanch/Evil-Crow-RF-v2-Custom-ROM](https://github.com/realdaveblanch/Evil-Crow-RF-v2-Custom-ROM/)
- [tutejshy-bit/tut-rf](https://github.com/tutejshy-bit/tut-rf)

## Version

**v2** - Dual CC1101 module support with enhanced RF capabilities and web-based configuration

## License & Attribution

- **CC1101 Driver**: Based on ELECHOUSE CC1101 library with modifications by Little Satan
- **Framework**: PlatformIO + Arduino Core for ESP32
- **Web Server**: ESPAsyncWebServer by me-no-dev
- **OTA Updates**: ElegantOTA by ayushsharma82

## Final Disclaimer

This firmware is provided for authorized security testing, research, and educational purposes only. Users are solely responsible for ensuring compliance with local laws and regulations. Unauthorized RF transmission may be illegal in your jurisdiction. 

**Always:**
- ✅ Get explicit permission before testing devices you don't own
- ✅ Know the RF regulations in your country
- ✅ Use for authorized security research only
- ✅ Follow all applicable local and international laws

**Never:**
- ❌ Use for illegal activities or unauthorized signal transmission
- ❌ Interfere with critical infrastructure or emergency systems
- ❌ Use without proper authorization and legal compliance

---

**Project Home:** [EvilCrowRF-V2](https://github.com/joelsernamoreno/EvilCrowRF-V2)

**Last Updated:** December 2025
