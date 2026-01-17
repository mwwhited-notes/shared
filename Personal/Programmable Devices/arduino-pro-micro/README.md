# Arduino Pro Micro

**ATmega32U4 Development Board with Native USB**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | SparkFun / Clones |
| Board | Pro Micro |
| MCU | ATmega32U4 |
| Date Acquired | April 23, 2023 |
| Quantity | 3 |
| Source | Amazon (Hosyond) |
| Price | $18.99 |
| Variant | 5V/16MHz |

## Specifications

| Specification | Value |
|--------------|-------|
| Architecture | AVR 8-bit |
| Clock Speed | 8 MHz (3.3V) or 16 MHz (5V) |
| Flash | 32 KB (4 KB bootloader) |
| SRAM | 2.5 KB |
| EEPROM | 1 KB |
| Digital I/O | 18 (7 PWM) |
| Analog Inputs | 9 (10-bit ADC) |
| Operating Voltage | 3.3V or 5V |
| USB | Native USB (HID, MIDI, Serial) |

## Variants

| Variant | Voltage | Clock |
|---------|---------|-------|
| 5V/16MHz | 5V | 16 MHz |
| 3.3V/8MHz | 3.3V | 8 MHz |

## Interfaces

| Interface | Pins |
|-----------|------|
| UART | 1 (pins 0, 1) |
| SPI | 1 (pins 14-16) |
| I2C | 1 (pins 2-SDA, 3-SCL) |
| USB | Native Micro-USB |

## Features

- **Native USB** - Acts as HID keyboard/mouse, MIDI device
- Same chip as Arduino Leonardo
- Small footprint (18 x 33 mm)
- Breadboard compatible
- Micro-USB connector
- TX/RX LEDs

## USB Capabilities

- USB HID (keyboard, mouse, gamepad)
- USB MIDI device
- USB Serial (CDC)
- Multiple USB endpoints
- No separate USB chip needed

## Programming

| Method | Tools |
|--------|-------|
| USB (Bootloader) | Arduino IDE |
| ICSP | USBasp, AVR ISP |

### Bootloader Reset

If the Pro Micro stops responding:
1. Short RST to GND twice quickly
2. Upload within 8 seconds
3. Or hold RST, release, upload immediately

## Documentation

- [SparkFun Pro Micro Guide](https://learn.sparkfun.com/tutorials/pro-micro--fio-v3-hookup-guide)
- [ATmega32U4 Datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7766-8-bit-AVR-ATmega16U4-32U4_Datasheet.pdf)
- [Pro Micro Schematic](https://cdn.sparkfun.com/datasheets/Dev/Arduino/Boards/Pro_Micro_v13b.pdf)

## Software & Tools

- **Arduino IDE** - Select "SparkFun Pro Micro" or "Arduino Leonardo"
- **Select correct processor** - 3.3V/8MHz or 5V/16MHz
- [SparkFun Board Package](https://github.com/sparkfun/Arduino_Boards)

## Common Uses

- Custom keyboards (QMK firmware)
- Game controllers
- MIDI controllers
- USB dongles
- HID automation

## Notes

- **IMPORTANT**: Check voltage variant!
- Different from Pro Mini (has USB, different chip)
- Serial on pins 0,1 is separate from USB Serial
- Popular for mechanical keyboard projects
- If bricked, use bootloader reset method above

## Local Files

*Documentation to be downloaded*
