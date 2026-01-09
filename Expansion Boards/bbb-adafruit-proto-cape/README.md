# Adafruit Proto Cape Kit for BeagleBone

**BeagleBone Cape - Prototyping PCB**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | Adafruit Industries |
| Board | Proto Cape Kit for BeagleBone |
| Product ID | 572 |
| Platform | BeagleBone, BeagleBone Black |
| Form Factor | Cape (prototyping PCB) |
| Primary Function | Solderable prototyping / breakout board |
| Date Acquired | 2026-01 |
| Quantity | 3 |
| Price | $9.95 each |

## Compatibility

| Compatible With | Notes |
|-----------------|-------|
| BeagleBone | Original BeagleBone |
| BeagleBone Black | Full compatibility |

## Specifications

| Specification | Value |
|--------------|-------|
| PCB Material | Double-sided FR4 |
| Pin Headers | 2x 46-pin (P8 and P9 headers) |
| Power Distribution | 5V and 3.3V power strips |
| SMT Breakouts | SOIC-8 and SOT-23 footprints |
| Dimensions | 2.5" x 1.5" x 0.2" |
| Weight | 0.48 oz |
| Assembly Time | ~10 minutes (soldering required) |

## Pin Mapping

### Pin Access

The cape provides breakout access to both BeagleBone headers:

- **P8 Header** - 46 pins, individually numbered
- **P9 Header** - 46 pins, individually numbered

### Power Rails

- **5V** - Power supply strips for 5V distribution
- **3.3V** - Power supply strips for 3.3V distribution
- **GND** - Ground distribution

### Stacking Compatibility

- [x] Passes through all pins via solderable breakouts
- [ ] Pre-installed headers - requires assembly
- [x] Can stack with other capes after assembly

## Features

- Solderable prototyping area with ground plane
- Breakout to both 46-pin headers (P8 and P9)
- Individual pin numbering for easy identification
- Power distribution strips for 5V and 3.3V
- SMT breakout footprints:
  - SOIC-8 (8-pin SMT ICs)
  - SOT-23 (3-pin SMT transistors/regulators)
- Fits without obstructing Ethernet jack
- Double-sided FR4 PCB construction

## Kit Contents

- 1x Double-sided FR4 prototyping PCB
- 3x Header strips (for soldering to BeagleBone)

**Note:** BeagleBone board sold separately.

## Assembly

### Required Tools
- Soldering iron
- Solder
- Flux (optional but recommended)

### Assembly Steps

1. Insert the included header strips into your BeagleBone's P8 and P9 headers
2. Place the Proto Cape PCB onto the header pins
3. Ensure the board sits flush and doesn't obstruct the Ethernet jack
4. Solder all pins to the Proto Cape PCB
5. Trim any excess pin length if needed

**Estimated assembly time:** 10 minutes (even for beginners)

## Documentation

### Board Documentation
- [Product Page](https://www.adafruit.com/product/572)
- [GitHub Repository](https://github.com/adafruit/Adafruit-BeagleBone-ProtoBoard-PCB)

### Design Files
- Schematic: `Adafruit-BeagleBone-ProtoBoard-v0.1.sch` (available on GitHub)
- Board Layout: `Adafruit-BeagleBone-ProtoBoard-v0.1.brd` (available on GitHub)

### Learning Resources
- [LedGames - BeagleBone Black 64x64 LED Game](https://learn.adafruit.com/) (example project)

## Software & Libraries

No specific software or libraries required - this is a hardware prototyping board. Use with any BeagleBone-compatible software.

## Notes

- **Status:** Product is no longer stocked by Adafruit as of the last check
- **License:** Creative Commons Attribution/Share-Alike
- **Designers:** Limor Fried/Ladyada and Kevin Townsend for Adafruit Industries
- The PCB design is open source and available on GitHub
- Can be used to create custom capes or prototype circuits
- SMT breakouts allow surface-mount component testing

## Local Files

- `Adafruit-BeagleBone-ProtoBoard-v0.1.sch` - Board schematic (Eagle format)
