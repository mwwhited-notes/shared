# WD My Book Live

**Single-drive NAS, older generation with known security issues**

## Device Information

| Field | Value |
|-------|-------|
| Manufacturer | Western Digital |
| Model | My Book Live |
| Model Number | TBD |
| Serial Number | WMAZA7408486 |
| Generation/Year | 2010-2014 |
| Date Acquired | TBD |
| Condition | Working |
| Current Use | Network Storage |

## Network Configuration

| Setting | Value |
|---------|-------|
| IP Address | 192.168.0.97 |
| Hostname | MyBookLive |
| Network | 192.168.0.0/24 |

## Storage

| Metric | Value |
|--------|-------|
| Total Capacity | 2 TB |
| Used | 975 GB |
| Available | ~1 TB |
| Usage | ~49% |

## Specifications

| Specification | Value |
|--------------|-------|
| CPU | Applied Micro APM82181 (PowerPC, 800 MHz) |
| RAM | 256 MB DDR2 |
| Drive Bays | 1x 3.5" SATA (internal, not hot-swap) |
| Capacity | TBD (1TB, 2TB, or 3TB variants) |
| Network | 1x Gigabit Ethernet |
| USB | 1x USB 2.0 (expansion only) |
| Power | External AC adapter |
| OS | Linux-based (Debian) |

## Hackability

### Current Status

| Aspect | Status |
|--------|--------|
| SSH Access | Enable via web UI hack |
| Root Access | Available |
| Custom Firmware | Limited community support |

### Hackability Rating: ★★★☆☆

PowerPC architecture limits software options. Full Linux access but fewer packages available.

### CRITICAL SECURITY WARNING

**DO NOT CONNECT TO INTERNET**

The My Book Live has critical unpatched vulnerabilities:
- CVE-2018-18472: Unauthenticated remote command execution
- Mass wipe incidents reported in June 2021
- WD officially ended support - NO PATCHES AVAILABLE

**Safe use only on isolated network segment or completely offline.**

### Available Modifications

| Modification | Availability | Notes |
|-------------|--------------|-------|
| SSH Access | Enable via UI | Hidden option |
| Root Shell | After SSH | Full access |
| Custom packages | Limited | PowerPC architecture |
| Debian packages | Some | Via apt |

### Hackability Resources

- [WD Community Forums (archived)](https://community.wd.com/)
- [My Book Live Hacks](https://mybookworld.wikidot.com/)

## Project Ideas

Given the security issues, consider:

- [ ] Offline backup storage only
- [ ] Isolated LAN archive device
- [ ] Extract drive for use in other enclosure
- [ ] Parts/curiosity device
- [ ] Learn PowerPC Linux

## Documentation

### Official
- [WD My Book Live (EOL)](https://support-en.wd.com/)

### Security Advisories
- [WD Security Advisory](https://www.westerndigital.com/support/product-security)
- [CVE-2018-18472](https://nvd.nist.gov/vuln/detail/CVE-2018-18472)

## Local Files

*None yet*

## Notes

### Security Recommendations

1. **NEVER expose to internet** - Not even behind a firewall with port forwarding
2. **Isolate on network** - Put on separate VLAN if possible
3. **Disable remote access** - Turn off WD cloud features entirely
4. **Consider retirement** - May be safer to extract drive and use elsewhere

### Alternative Uses for Hardware

If the security risk is too high for network use:
- Extract the drive for use in USB enclosure or other NAS
- Use as learning device on completely isolated network
- Donate/recycle

### Architecture Note

PowerPC (APM82181) is unusual - most Linux packages assume x86 or ARM. Software availability is limited compared to modern NAS devices.
