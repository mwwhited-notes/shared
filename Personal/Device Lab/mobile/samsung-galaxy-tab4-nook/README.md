# Samsung Galaxy Tab 4 Nook

**Barnes & Noble branded Android tablet, target for home automation dashboard project**

## Device Information

| Field | Value |
|-------|-------|
| Manufacturer | Samsung (B&N branded) |
| Model | Galaxy Tab 4 Nook |
| Model Number | SM-T230NU |
| Generation/Year | 2014 |
| Date Acquired | TBD |
| Condition | Working |
| Current Use | Project - Home automation dashboard |

## Specifications

| Specification | Value |
|--------------|-------|
| SoC/CPU | Qualcomm Snapdragon 410 (MSM8916) |
| Architecture | ARM (32-bit, NOT ARM64) |
| RAM | 1.5 GB |
| Storage | 8 GB |
| Display | 7" 1280x800 |
| Connectivity | WiFi 802.11 b/g/n, Bluetooth 4.0 |
| Ports | Micro-USB, microSD, 3.5mm |
| Battery | 4000 mAh |
| OS (Stock) | Android 4.4.2 KitKat |
| OS (Current) | Android 4.4.2 KitKat |
| OS (Target) | LineageOS 14.1 (Android 7.1) |

## Hackability

### Current Status

| Aspect | Status |
|--------|--------|
| Root/Jailbreak | Available |
| Bootloader | Unlockable |
| Custom Firmware | LineageOS 14.1 available |
| ADB/SSH Access | Yes (enable Developer Options) |

### Hackability Rating: ★★★★☆

Good community support, LineageOS available, straightforward flashing process.

### Available Modifications

| Modification | Availability | Notes |
|-------------|--------------|-------|
| LineageOS 14.1 | Android 7.1 | Recommended upgrade path |
| TWRP Recovery | Available | Required before flashing ROM |
| Root (Magisk) | Compatible | After LineageOS install |

### Flashing Process

1. Enable Developer Options and USB Debugging
2. Flash TWRP recovery via Odin (Samsung tool)
3. Boot into TWRP
4. Flash LineageOS 14.1
5. Flash ARM GApps (NOT ARM64 - device is 32-bit)
6. Optional: Flash Magisk for root

### Hackability Resources

- [XDA Forum - SM-T230NU](https://forum.xda-developers.com/) - Search for device
- [LineageOS Wiki](https://wiki.lineageos.org/)
- [TWRP for SM-T230NU](https://twrp.me/)

## Project: Home Automation Dashboard

**Status**: Planned

### Goal
Wall-mounted or tabletop display for home automation control.

### Dashboard Software Options

| Software | Type | Features |
|----------|------|----------|
| Fully Kiosk Browser | Commercial | Kiosk mode, motion wake, battery management |
| WallPanel | Open Source | Fully Kiosk alternative |
| Home Assistant Companion | Official HA app | Native integration |

### Related Project
See [home-automation/](../../../home-automation/) for full home automation platform setup.

### Outstanding Decisions
- [ ] Final dashboard app selection
- [ ] Battery/charging management strategy for always-on use
- [ ] Mounting solution (wall vs. tabletop)

## Documentation

### Official
- [Samsung Support](https://www.samsung.com/us/support/)

### Community
- [XDA Developers](https://forum.xda-developers.com/)
- [LineageOS Wiki](https://wiki.lineageos.org/)

## Local Files

*To be downloaded:*
- [ ] TWRP recovery image
- [ ] LineageOS 14.1 ROM
- [ ] ARM GApps package

## Notes

- **Critical**: This is ARM (32-bit), NOT ARM64. GApps must be ARM variant.
- B&N branding may affect some stock features but doesn't impact custom ROM compatibility.
- Consider battery health for always-on dashboard use - may want to use a smart plug to cycle charging.
