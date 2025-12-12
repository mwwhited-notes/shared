# USBasp

**AVR USB Programmer**

## Unit Information

| Field | Value |
|-------|-------|
| Manufacturer | Clone (generic) |
| Model | USBasp |
| Hardware Revision | Unknown |
| Firmware Version | Unknown |
| Condition | Working |

## Specifications

| Specification | Value |
|--------------|-------|
| Target MCUs | Atmel AVR (ATmega, ATtiny, AT90) |
| Interface | USB 1.1 |
| Programming | ISP (In-System Programming) |
| Connector | 10-pin IDC header |
| Voltage | 5V or 3.3V (jumper selectable on some boards) |
| Speed | Up to 375 kHz (5 kHz slow mode) |

## Features

- USB powered (no external supply needed)
- Directly supported by AVRDUDE
- Works with Arduino IDE (as "USBasp" programmer)
- Based on Thomas Fischl's open-source design

## Accessories

- **6-pin adapter** - 10-pin to 6-pin ISP adapter
- **6-pin pogo adapter** - Pogo pin adapter for 6-pin ISP

## Pinout (10-pin IDC)

```
        ┌─────────┐
  MOSI  │ 1     2 │  VCC
        │         │
  N/C   │ 3     4 │  GND
        │         │
 RESET  │ 5     6 │  GND
        │         │
   SCK  │ 7     8 │  GND
        │         │
  MISO  │ 9    10 │  GND
        └─────────┘
```

## Pinout (6-pin ISP)

```
        ┌─────────┐
  MISO  │ 1     2 │  VCC
        │         │
   SCK  │ 3     4 │  MOSI
        │         │
 RESET  │ 5     6 │  GND
        └─────────┘
```

## Documentation

- [USBasp Official Site (Thomas Fischl)](https://www.fischl.de/usbasp/)
- [AVRDUDE Documentation](https://avrdude.nongnu.org/)

## Software

- **AVRDUDE** - Command-line programming utility
- **Arduino IDE** - Select "USBasp" as programmer
- **Zadig** - USB driver installer for Windows

## Driver Installation (Windows)

1. Download [Zadig](https://zadig.akeo.ie/)
2. Connect USBasp
3. In Zadig: Options → List All Devices
4. Select "USBasp" from dropdown
5. Install libusb-win32 or libusbK driver

## Basic AVRDUDE Commands

```bash
# Read fuses
avrdude -c usbasp -p m328p -v

# Write flash
avrdude -c usbasp -p m328p -U flash:w:firmware.hex:i

# Write fuses (CAREFUL!)
avrdude -c usbasp -p m328p -U lfuse:w:0xFF:m -U hfuse:w:0xDE:m
```

## Notes

- Clone board with no identifying markings
- If "cannot set sck period" warning appears, firmware may need update
- Some clones have issues with slow clock targets - use `-B` flag in AVRDUDE

## Local Files

*USBasp is open-source - see [fischl.de](https://www.fischl.de/usbasp/) for schematics and firmware.*
