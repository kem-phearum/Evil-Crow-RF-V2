# Security Policy

## Reporting Security Vulnerabilities

**Please do not report security vulnerabilities through public GitHub issues or discussions.**

If you believe you have found a security vulnerability in Evil Crow RF V2, please report it privately to:

**Email:** Contact through GitHub private message to [@JoelSernaMoreno](https://github.com/joelsernamoreno)

Please include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if available)
- Your contact information

We will acknowledge receipt of your report within 48 hours and keep you updated on the progress.

## Responsible Disclosure Timeline

1. **Report received** - We acknowledge receipt within 48 hours
2. **Assessment** - We assess the vulnerability (1-7 days)
3. **Development** - We develop and test a fix (5-14 days)
4. **Release preparation** - We prepare a security release
5. **Notification** - We notify affected users before public disclosure
6. **Public release** - We release the fix publicly

## Security Best Practices for Users

### WiFi Security

⚠️ **Important:** Evil Crow RF V2 creates a WiFi Access Point with default credentials.

**Recommendations:**
- ✅ Change default WiFi password immediately after setup
- ✅ Use a strong, unique password (12+ characters with mixed case, numbers, symbols)
- ✅ Keep the device on a secure, isolated network
- ✅ Disable AP mode when not actively using the web interface

### Configuration Files

⚠️ **Sensitive Data:** Configuration files stored on the MicroSD card contain network credentials.

**Recommendations:**
- ✅ Never share configuration files publicly
- ✅ Remove sensitive files before sharing SD card backups
- ✅ Use `.gitignore` to exclude config files from version control
- ✅ Secure physical access to the MicroSD card

### Firmware Security

**Recommendations:**
- ✅ Always use the latest firmware version
- ✅ Verify firmware integrity when updating
- ✅ Only download firmware from official GitHub repository
- ✅ Enable OTA updates for security patches

### RF Signal Security

⚠️ **Warning:** This device can capture, replay, and transmit RF signals.

**Legal & Ethical Recommendations:**
- ✅ Only test on devices you own or have explicit written permission to test
- ✅ Know and follow local RF transmission regulations
- ✅ Never interfere with critical infrastructure or emergency systems
- ✅ Use jamming capability only in authorized testing scenarios
- ✅ Obtain proper licensing/certifications if required in your jurisdiction

## Vulnerability Disclosure Statement

The developers of Evil Crow RF V2 are committed to:

1. **Timely Response** - Acknowledging and assessing reports quickly
2. **Transparent Communication** - Keeping reporters informed of progress
3. **Responsible Patching** - Developing and releasing fixes promptly
4. **Fair Attribution** - Crediting security researchers appropriately
5. **User Protection** - Notifying users before public disclosure when possible

## Scope

This security policy applies to:

- Evil Crow RF V2 firmware code
- ESP32 hardware integration
- CC1101 RF module functionality
- Web interface and API
- Configuration handling
- RF signal processing

## Out of Scope

The following are generally out of scope for security reports:

- Issues with third-party libraries (report to upstream)
- User configuration mistakes
- Physical device security
- Attacks requiring physical access
- Social engineering
- Local denial of service attacks

However, if you believe something is borderline, please report it anyway. We'd rather have a false positive than miss a real issue.

## Legal Notice

Evil Crow RF V2 is provided for:

- ✅ Authorized security testing
- ✅ Research and education
- ✅ Personal experimentation (on own devices)

⚠️ Users are **solely responsible** for ensuring legal compliance in their jurisdiction.

The Evil Crow RF V2 developers:
- Are NOT responsible for misuse of the device
- Do NOT endorse illegal activities
- Will NOT provide assistance for unauthorized testing
- Recommend consulting legal counsel regarding RF regulations

## Security Update Process

When a security vulnerability is discovered and patched:

1. **Notification** - Users are notified via GitHub Security Advisories
2. **Release** - A patched version is released with CVE assignment
3. **Documentation** - Security updates are documented in CHANGELOG.md
4. **Announcement** - Users are encouraged to update immediately

## Firmware Verification

To verify firmware integrity, we recommend:

```bash
# Check SHA256 hash
sha256sum firmware.bin

# Verify GPG signature (when available)
gpg --verify firmware.bin.sig firmware.bin
```

---

Thank you for helping us keep Evil Crow RF V2 secure! 🔒
