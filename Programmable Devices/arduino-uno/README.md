# Arduino UNO

**AVR Microcontroller Development Board**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | Arduino (and clones) |
| Board | UNO R3 |
| MCU | ATmega328P |
| Date Acquired | |
| Quantity | |

## Specifications

| Specification | Value |
|--------------|-------|
| Architecture | AVR 8-bit |
| Clock Speed | 16 MHz |
| Flash | 32 KB (0.5 KB bootloader) |
| SRAM | 2 KB |
| EEPROM | 1 KB |
| Digital I/O | 14 (6 PWM) |
| Analog Inputs | 6 (10-bit ADC) |
| Operating Voltage | 5V |
| Input Voltage | 7-12V (6-20V limits) |
| DC Current per I/O | 20 mA |

## Interfaces

| Interface | Pins |
|-----------|------|
| UART | 1 (pins 0, 1) |
| SPI | 1 (pins 10-13) |
| I2C | 1 (A4-SDA, A5-SCL) |
| USB | USB-B (ATmega16U2 or CH340) |

## Features

- Standard Arduino form factor
- Extensive shield ecosystem
- USB programming (no external programmer needed)
- Auto-reset for programming
- Power jack and USB power options
- ICSP header for bootloader programming

## Programming

| Method | Tools |
|--------|-------|
| USB (Bootloader) | Arduino IDE, avrdude |
| ICSP | USBasp, AVR ISP, Arduino as ISP |

## Documentation

- [Arduino UNO Product Page](https://store.arduino.cc/products/arduino-uno-rev3)
- [ATmega328P Datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7810-Automotive-Microcontrollers-ATmega328P_Datasheet.pdf)
- [Arduino UNO Schematic](https://www.arduino.cc/en/uploads/Main/Arduino_Uno_Rev3-schematic.pdf)
- [Arduino UNO Pinout](https://docs.arduino.cc/hardware/uno-rev3)

## Software & Tools

- **Arduino IDE** - Primary development environment
- **PlatformIO** - Alternative IDE with better tooling
- **AVRDUDE** - Command-line programming
- [Arduino IDE Download](https://www.arduino.cc/en/software)

## Clone Notes

Common clone variations:
- **CH340/CH341 USB chip** - Requires CH340 driver instead of FTDI/ATmega16U2
- **LGT8F328P clones** - Different MCU, mostly compatible
- Check USB chip if upload fails (driver issue)

## Notes

- Most common Arduino board, huge community support
- Clone boards work identically (may need CH340 driver)
- 5V logic level (not directly 3.3V compatible)
- Limited RAM for complex programs

## Local Files

*Documentation to be downloaded*
