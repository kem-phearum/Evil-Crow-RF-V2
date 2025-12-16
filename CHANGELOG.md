# Changelog

All notable changes to the Evil Crow RF V2 project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive project documentation (README, CONTRIBUTING, SECURITY, CODE_OF_CONDUCT)
- Git and GitHub workflow guide in README
- SD card configuration examples
- .gitignore cleanup and optimization

### Changed
- Updated platformio.ini with improved build configuration
- Enhanced .gitignore with comprehensive file exclusions
- Improved README structure and organization

### Fixed
- .gitignore duplicate entries (*.swp, *.swo, *~, etc.)
- .gitignore conflicting exclusion patterns

## [2.0.0] - Initial Release

### Added
- Dual CC1101 RF module support for simultaneous TX/RX
- Web-based configuration interface (HTTP server)
- Real-time RF signal capture and analysis
- Signal replay/transmission functionality
- RF jamming capabilities
- WiFi Access Point (AP) mode with mDNS support
- MicroSD card support for configuration and signal library
- Over-The-Air (OTA) firmware updates via ElegantOTA
- Comprehensive RF signal library (100+ pre-captured signals):
  - Doorbell signals (multiple brands)
  - Tesla Charge Port Opener signals (315/433MHz variants)
  - Garage door openers (EU/US variants)
  - Smart device signals (fans, lights, etc.)
  - Miscellaneous RF signals for testing
- ELECHOUSE CC1101 driver with Little Satan modifications
- Real-time signal smoothing and filtering algorithms
- Support for multiple modulation schemes (ASK/OOK, FSK, GFSK, etc.)
- Configurable error tolerance and sampling parameters
- Log viewer for real-time signal analysis
- Device status monitoring and statistics

### Technical Details
- **Platform:** ESP32 DevKit
- **RF Modules:** 2x CC1101 (300-928 MHz + 2.4 GHz bands)
- **Framework:** Arduino + PlatformIO
- **Storage:** MicroSD card (SPI) + LittleFS
- **Networking:** WiFi 802.11 b/g/n with mDNS
- **Web Server:** ESPAsyncWebServer

## Version History Reference

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| 2.0.0 | 2025-12-16 | Current | Latest release with full dual CC1101 support |
| 1.0.0 | Earlier | Legacy | Original Evil Crow RF V1 |

## Compatibility

### Supported Hardware
- ESP32-DevKitC
- ESP32-WROVER (with PSRAM)
- Compatible ESP32 variants with sufficient GPIO pins

### Supported RF Modules
- ELECHOUSE CC1101
- Texas Instruments CC1101 (compatible)

### Tested Operating Systems
- **Development:**
  - Windows 10/11
  - macOS 10.15+
  - Linux (Ubuntu 18.04+, Debian)
- **Deployment:**
  - Any system with WiFi support
  - Mobile devices (Android, iOS)
  - Browsers (Chrome, Firefox, Safari, Edge)

## Known Issues

- MicroSD cards larger than 32GB may have compatibility issues
- mDNS resolution requires avahi-daemon on Linux systems
- Web interface may not load with certain ISP DNS settings
- Simultaneous dual-module RX at different frequencies has minimal crosstalk

## Planned Features

### Version 2.1.0 (Planned)
- [ ] NRF24L01 module support for mousejacking attacks
- [ ] Signal recording to MicroSD in sub format
- [ ] Advanced signal analysis (FFT, spectral analysis)
- [ ] Device-specific attack templates
- [ ] Web interface dark mode
- [ ] Multi-language support

### Version 3.0.0 (Planned)
- [ ] Bluetooth module support
- [ ] SD card file browser in web interface
- [ ] Signal database with cloud sync (optional)
- [ ] Machine learning-based signal classification
- [ ] Mobile app companion (Android/iOS)
- [ ] HTTPS/SSL support for secure web interface
- [ ] User authentication and role-based access

## Deprecations

- Arduino IDE support deprecated in favor of PlatformIO
- Legacy CC1101 driver versions (pre-Little Satan modifications)

## Breaking Changes

None documented yet - project maintains backward compatibility.

## Contributors

- **Joel Serna** (@JoelSernaMoreno) - Lead developer
- **Little Satan** (https://github.com/LSatan/) - Main collaborator, CC1101 driver improvements
- **Jordi Castelló** (@iordic) - Collaborator
- **Eduardo Blázquez** (@_eblazquez) - Collaborator
- **Federico Maggi** (@phretor) - Collaborator
- **Andrea Guglielmini** (@Guglio95) - Collaborator
- **RFQuack** (@rfquack) - Collaborator
- **Ignacio Díaz Álvarez** (@Nacon_96) - PCB design
- **Forensic Security** (@ForensicSec) - PCB design
- **April Brother** (@aprbrother) - PCB design, Manufacturing

## Support

For questions, issues, or feature requests:
- **Discord:** [Evil Crow RF Community](https://discord.gg/evilcrowrf)
- **GitHub:** [Issues & Discussions](https://github.com/joelsernamoreno/EvilCrowRF-V2/issues)
- **Twitter:** [@JoelSernaMoreno](https://twitter.com/JoelSernaMoreno)

---

**Last Updated:** December 16, 2025
