# Maxstream XBIB-U-DEV

**XBee USB Development Interface Board**

## Unit Information

| Field | Value |
|-------|-------|
| Manufacturer | Digi International (formerly MaxStream) |
| Model | XBIB-U-DEV |
| Hardware Revision | Rev 3 |
| Condition | Working |

## Specifications

| Specification | Value |
|--------------|-------|
| Interface | USB (FTDI-based) |
| Socket | 20-pin XBee through-hole |
| Power | USB powered or external |
| Indicators | Power LED, RSSI LED, Associate LED |
| I/O Access | Breakout headers for XBee I/O pins |

## Compatible XBee Modules

- XBee 802.15.4 (Series 1)
- XBee ZB (Series 2/2B/2C)
- XBee DigiMesh
- XBee 868/900
- XBee-PRO variants
- XBee3 modules

## Features

- USB to serial interface for XBee configuration
- RSSI and Associate status LEDs
- Reset button
- Commissioning button
- Breakout access to all XBee pins
- Loopback jumper for testing

## Documentation

- [XBIB-U-DEV User Guide (Digi)](https://www.digi.com/resources/documentation/digidocs/pdfs/90001457-13.pdf)
- [XBee/XBee-PRO RF Modules Documentation](https://www.digi.com/products/embedded-systems/digi-xbee/rf-modules/2-4-ghz-rf-modules/xbee-zigbee)
- [XCTU Software Guide](https://www.digi.com/resources/documentation/digidocs/90001458-13/default.htm)

## Software

- **XCTU** - Digi's XBee configuration and testing utility
  - [Download XCTU](https://www.digi.com/products/embedded-systems/digi-xbee/digi-xbee-tools/xctu)
- **Digi XBee Python Library** - For programmatic access
- **Serial Terminal** - Any terminal at 9600-115200 baud

## XBee Modules in Collection

*Document your XBee modules here:*

| Module Type | Frequency | Protocol | Firmware | Notes |
|-------------|-----------|----------|----------|-------|
| | | | | |
| | | | | |
| | | | | |

## Pinout Reference

Standard XBee 20-pin layout:
```
          ┌───────────┐
     VCC  │ 1      20 │  GND
          │           │
    DOUT  │ 2      19 │  RESET
          │           │
     DIN  │ 3      18 │  RSSI PWM
          │           │
   DIO12  │ 4      17 │  ASSOC
          │           │
   RESET  │ 5      16 │  RTS
          │           │
   DIO10  │ 6      15 │  DIO5
          │           │
    DIO11 │ 7      14 │  VREF
          │           │
     N/C  │ 8      13 │  CTS
          │           │
     DTR  │ 9      12 │  ON/SLEEP
          │           │
     GND  │ 10     11 │  DIO4
          └───────────┘
```

## Basic XCTU Usage

1. Install XCTU and connect XBIB-U-DEV with XBee module
2. Click "Discover devices" (magnifying glass icon)
3. Select correct COM port and baud rates to scan
4. Module appears in device list when found
5. Click module to view/edit configuration

## Common Configuration Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| ID | PAN ID | 3332 |
| CH | Channel | C |
| MY | 16-bit address | 0 |
| DH/DL | Destination address | 0 |
| BD | Baud rate | 3 (9600) |
| AP | API mode | 0 (transparent) |

## Notes

- Board is Rev 3 of the XBIB-U-DEV
- Multiple XBee modules of different types in collection
- Use XCTU to identify module type and update firmware

## Local Files

- `XBIB-U-DEV_UserGuide.pdf` - Development board user guide
