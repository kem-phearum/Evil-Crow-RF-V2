# Contributing to Evil Crow RF V2

Thank you for your interest in contributing to the Evil Crow RF V2 project! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please review our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing. We are committed to providing a welcoming and respectful environment for all contributors.

## How to Contribute

### Reporting Bugs

If you find a bug, please help us by submitting an issue on GitHub:

1. **Check existing issues** - Search to see if the bug has already been reported
2. **Create a detailed report** including:
   - Clear description of the bug
   - Steps to reproduce the issue
   - Expected behavior vs. actual behavior
   - Hardware setup (ESP32 board, CC1101 modules, etc.)
   - Firmware version and date
   - Serial output or error messages
   - Attached logs if available

### Suggesting Enhancements

We welcome feature requests! Please submit suggestions as issues with:

1. Clear title and description of the enhancement
2. Explanation of the use case and why it would be beneficial
3. Possible implementation approaches (optional)
4. Examples or mockups (if applicable)

### Code Contributions

#### Prerequisites

- Familiarity with C++ and Arduino programming
- Understanding of RF signal processing concepts
- PlatformIO development setup
- Git and GitHub workflow knowledge

#### Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/EvilCrowRF-V2.git
   cd Evil-Crow-RF-V2
   ```
3. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes** following the coding standards below

#### Coding Standards

**C++ Style Guidelines:**

- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and single-responsibility
- Follow Arduino naming conventions
- Use 2-space indentation (not tabs)
- Keep lines under 100 characters when possible

**Example:**
```cpp
// Good: Clear naming and documentation
void configureRFModule(int moduleNum, float frequency, String modulation) {
  // Initialize RF parameters for specified module
  if (moduleNum < 1 || moduleNum > 2) return;
  
  // Set frequency with validation
  if (frequency >= 300 && frequency <= 928) {
    setFrequency(frequency);
  }
}

// Avoid: Unclear naming
void cfgRF(int m, float f, String mod) {
  // Set stuff
  setFrequency(f);
}
```

**Comments:**

- Use clear, English comments
- Explain the "why", not just the "what"
- Document complex algorithms or RF theory
- Add TODO comments for future improvements:
  ```cpp
  // TODO: Optimize signal smoothing algorithm for faster processing
  ```

#### Commit Messages

Follow the commit message convention:

```
[TYPE]: Brief description (50 chars max)

Detailed explanation if needed (wrap at 72 chars)
- Additional context
- Technical details
- Related issue numbers: Fixes #123
```

**Types:**
- **Add** - New feature
- **Fix** - Bug fix
- **Update** - Code improvement/refactoring
- **Remove** - Code deletion
- **Docs** - Documentation changes
- **Config** - Configuration file changes
- **Test** - Test additions/updates
- **Security** - Security fixes

**Examples:**
```bash
git commit -m "Add: Dual CC1101 simultaneous RX support

- Implements parallel signal capture on both modules
- Added module selection in RX config page
- Improved sampling accuracy with independent buffering
- Fixes #45"

git commit -m "Fix: MicroSD initialization timeout

Previously, large SD cards (>32GB) would timeout during init.
Now uses adaptive timeout based on card size.
Tested with 64GB cards successfully.

Fixes #98"
```

#### Testing

Before submitting a pull request:

1. **Build and compile** without errors:
   ```bash
   platformio run --environment esp32dev
   ```
2. **Test on physical hardware** - Verify functionality with actual ESP32 + CC1101 setup
3. **Check for warnings** and fix any compiler warnings
4. **Test edge cases** - Empty arrays, invalid inputs, boundary conditions
5. **Serial debugging** - Monitor output for unexpected behavior

#### Creating a Pull Request

1. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
2. **Create a Pull Request** on GitHub with:
   - Clear title and description
   - Reference to related issues (Fixes #123)
   - List of changes made
   - Testing performed
   - Screenshots/videos if UI changes
3. **Respond to review feedback** promptly
4. **Keep the branch updated** with the main branch

### Documentation Contributions

Improve documentation by:

- Fixing typos and grammar
- Clarifying confusing sections
- Adding new guides or tutorials
- Creating better examples
- Improving code comments

### File Structure

```
Evil-Crow-RF-V2/
├── src/
│   ├── main.cpp                    # Main firmware entry point
│   └── ELECHOUSE_CC1101_SRC_DRV.*  # CC1101 driver (minimal edits)
├── include/                        # Header files
├── SD/
│   ├── HTML/                       # Web UI files
│   ├── CONFIG/                     # Configuration templates
│   └── SUBGHZ/                     # RF signal library
├── README.md                       # Main documentation
├── CONTRIBUTING.md                 # This file
├── CODE_OF_CONDUCT.md             # Community guidelines
├── SECURITY.md                     # Security guidelines
├── LICENSE                         # License file
└── platformio.ini                  # Build configuration
```

## License

By contributing to this project, you agree that your contributions will be licensed under the same license as the project (specified in [LICENSE](LICENSE)).

## Questions or Need Help?

- **Discord Community**: [Join our Discord](https://discord.gg/evilcrowrf)
- **GitHub Issues**: Create an issue with your question
- **Twitter**: Contact [@JoelSernaMoreno](https://twitter.com/JoelSernaMoreno)

## Additional Resources

- [Evil Crow RF V2 README](README.md)
- [Troubleshooting Guide](TROUBLESHOOTING.md)
- [Security Guidelines](SECURITY.md)
- [ESP32 Documentation](https://docs.espressif.com/projects/esp-idf/en/stable/)
- [CC1101 Datasheet](https://www.ti.com/product/CC1101)

---

Thank you for contributing to Evil Crow RF V2! 🎉
