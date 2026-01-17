# Arduino Pro Mini

**Minimal AVR Microcontroller Board**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | SparkFun / Clones |
| Board | Pro Mini |
| MCU | ATmega328P |
| Date Acquired | |
| Quantity | |

## Specifications

| Specification | Value |
|--------------|-------|
| Architecture | AVR 8-bit |
| Clock Speed | 8 MHz (3.3V) or 16 MHz (5V) |
| Flash | 32 KB (2 KB bootloader) |
| SRAM | 2 KB |
| EEPROM | 1 KB |
| Digital I/O | 14 (6 PWM) |
| Analog Inputs | 8 (10-bit ADC) |
| Operating Voltage | 3.3V or 5V (variant dependent) |
| DC Current per I/O | 40 mA |

## Variants

| Variant | Voltage | Clock | Use Case |
|---------|---------|-------|----------|
| 5V/16MHz | 5V | 16 MHz | General use |
| 3.3V/8MHz | 3.3V | 8 MHz | Battery, 3.3V sensors |

## Interfaces

| Interface | Pins |
|-----------|------|
| UART | 1 (pins 0, 1) |
| SPI | 1 (pins 10-13) |
| I2C | 1 (A4-SDA, A5-SCL) |

## Features

- No USB - minimal design for low power/cost
- Small footprint (18 x 33 mm)
- Low quiescent current (~4mA active)
- Breadboard compatible
- Raw pin for unregulated power input
- A4-A7 on edge (not standard header)

## Programming

| Method | Tools |
|--------|-------|
| USB-Serial Adapter | FTDI, CP2102, CH340 adapter |
| ICSP | USBasp, AVR ISP |

### USB-Serial Programming Wiring

| Adapter | Pro Mini |
|---------|----------|
| DTR | DTR (via 0.1uF cap) |
| RX | TXO |
| TX | RXI |
| VCC | VCC |
| GND | GND |

## Documentation

- [SparkFun Pro Mini Guide](https://learn.sparkfun.com/tutorials/using-the-arduino-pro-mini-3-3v)
- [ATmega328P Datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7810-Automotive-Microcontrollers-ATmega328P_Datasheet.pdf)
- [Pro Mini Schematic](https://www.sparkfun.com/products/11114)

## Software & Tools

- **Arduino IDE** - Select "Arduino Pro or Pro Mini"
- **Select correct processor** - "ATmega328P (3.3V, 8MHz)" or "(5V, 16MHz)"
- [Arduino IDE Download](https://www.arduino.cc/en/software)

## Notes

- **IMPORTANT**: Check voltage variant before connecting!
- 3.3V version can be damaged by 5V power
- No onboard USB - need FTDI/serial adapter
- DTR pin provides auto-reset for programming
- Great for battery-powered projects
- A6, A7 are analog input only

## Local Files

*Documentation to be downloaded*
