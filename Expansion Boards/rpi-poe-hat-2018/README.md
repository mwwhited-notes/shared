# Raspberry Pi PoE HAT (2018)

**Raspberry Pi HAT - Power over Ethernet (802.3af)**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | Raspberry Pi Foundation |
| Board | PoE HAT (Original) |
| Year | 2018 |
| Platform | Raspberry Pi |
| Form Factor | HAT (40-pin) |
| Primary Function | Power over Ethernet |
| Standard | IEEE 802.3af |
| Quantity | 1 |

## Compatibility

| Compatible With | Notes |
|-----------------|-------|
| Raspberry Pi 3 Model B+ | Has PoE header |
| Raspberry Pi 4 Model B | Has PoE header |
| Raspberry Pi 3 Model B | No PoE header - NOT compatible |
| Raspberry Pi 5 | NOT compatible (use PoE+ HAT for Pi 5) |

## Specifications

| Specification | Value |
|--------------|-------|
| PoE Standard | IEEE 802.3af (Type 1) |
| Input Voltage | 37-57V DC (via Ethernet) |
| Output Voltage | 5V DC |
| Output Current | Up to 2.5A |
| Max Power Output | ~13W |
| Cooling Fan | Yes (25mm, brushless) |
| Fan Control | Temperature-controlled via GPIO |
| Dimensions | 56.5mm x 65mm |

## Pin Mapping

| HAT Pin | RPi Pin | Function | Notes |
|---------|---------|----------|-------|
| PoE+ | PoE Header Pin 1 | PoE Power + | Via 4-pin PoE header |
| PoE+ | PoE Header Pin 2 | PoE Power + | Via 4-pin PoE header |
| PoE- | PoE Header Pin 3 | PoE Power - | Via 4-pin PoE header |
| PoE- | PoE Header Pin 4 | PoE Power - | Via 4-pin PoE header |
| 5V | GPIO Pin 2, 4 | 5V Output | Powers the Pi |
| GND | GPIO Pin 6, 9, etc. | Ground | Common ground |
| Fan | GPIO 18 (BCM) | Fan Control | PWM speed control |

### Pins Used

- **Power:** 5V, GND (via 40-pin header)
- **PoE:** 4-pin PoE header on Pi 3B+/4
- **Fan Control:** GPIO 18 (BCM)

### Stacking Compatibility

- [ ] Passes through all GPIO pins - Limited by fan/heatsink
- [ ] Can stack with: Low-profile HATs only
- [x] Conflicts with: Tall components, cases without PoE cutout

## Features

- Powers Raspberry Pi via Ethernet cable
- No separate power supply needed
- Integrated cooling fan (temperature-controlled)
- 802.3af compliant - works with standard PoE switches/injectors
- Fully isolated power supply
- Compact form factor

## Power Budget

| Load | Power Available |
|------|-----------------|
| Pi 4 idle | ~3W - OK |
| Pi 4 full load | ~7W - OK |
| Pi 4 + USB peripherals | Up to ~13W total |

**Note:** The original PoE HAT (802.3af) provides ~13W maximum. For higher power needs, consider the PoE+ HAT (802.3at, 25W).

## Fan Control

The fan speed is controlled via GPIO 18 using PWM. Temperature thresholds can be configured in `/boot/config.txt`:

```
# PoE HAT fan settings
dtoverlay=rpi-poe
dtparam=poe_fan_temp0=50000
dtparam=poe_fan_temp1=60000
dtparam=poe_fan_temp2=70000
dtparam=poe_fan_temp3=80000
```

## Documentation

### Board Documentation
- [Product Page](https://www.raspberrypi.com/products/poe-hat/)
- [Official Documentation](https://www.raspberrypi.com/documentation/accessories/poe-hat.html)

## Requirements

- Raspberry Pi 3 Model B+ or Raspberry Pi 4
- 802.3af compliant PoE switch or injector
- Cat5e or better Ethernet cable

## Installation

1. Power off Raspberry Pi
2. Align HAT with 40-pin GPIO and 4-pin PoE headers
3. Press down firmly to seat both connectors
4. Connect Ethernet cable from PoE switch/injector
5. Pi will power on automatically

## Safety Notice

> The device shall only be powered using 802.3af-compliant power sourcing equipment. Any external power supply used with the Raspberry Pi shall comply with relevant regulations and standards applicable in the country of intended use.

## Notes

- Do NOT connect both PoE and USB-C power simultaneously
- Fan can be noisy at high speeds - consider PoE+ HAT for quieter operation
- Some cases require modification for PoE HAT clearance
- The successor PoE+ HAT (2021) provides 25W and improved fan design
- Ensure your PoE switch provides sufficient power budget

## Local Files

*To be downloaded*

- `RPi_PoE_HAT_Schematic.pdf` - Board schematic (if available)
