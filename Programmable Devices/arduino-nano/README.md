# Arduino Nano

**Compact AVR Microcontroller Board**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | Arduino (and clones) |
| Board | Nano V3 |
| MCU | ATmega328P |
| Date Acquired | |
| Quantity | |

## Specifications

| Specification | Value |
|--------------|-------|
| Architecture | AVR 8-bit |
| Clock Speed | 16 MHz |
| Flash | 32 KB (2 KB bootloader) |
| SRAM | 2 KB |
| EEPROM | 1 KB |
| Digital I/O | 14 (6 PWM) |
| Analog Inputs | 8 (10-bit ADC) |
| Operating Voltage | 5V |
| Input Voltage | 7-12V |
| DC Current per I/O | 40 mA |

## Interfaces

| Interface | Pins |
|-----------|------|
| UART | 1 (pins 0, 1) |
| SPI | 1 (pins 10-13) |
| I2C | 1 (A4-SDA, A5-SCL) |
| USB | Mini-USB (FTDI or CH340) |

## Features

- Breadboard-friendly form factor
- Same capabilities as UNO
- 2 extra analog inputs (A6, A7)
- Mini-USB connector
- Small footprint (18 x 45 mm)
- Built-in LED on pin 13

## Programming

| Method | Tools |
|--------|-------|
| USB (Bootloader) | Arduino IDE, avrdude |
| ICSP | USBasp, AVR ISP |

## Documentation

- [Arduino Nano Product Page](https://store.arduino.cc/products/arduino-nano)
- [ATmega328P Datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7810-Automotive-Microcontrollers-ATmega328P_Datasheet.pdf)
- [Arduino Nano Pinout](https://docs.arduino.cc/hardware/nano)

## Software & Tools

- **Arduino IDE** - Select "Arduino Nano" board
- **PlatformIO** - Alternative IDE
- [Arduino IDE Download](https://www.arduino.cc/en/software)

## Clone Notes

- Most clones use CH340 USB chip (need driver)
- Select "ATmega328P (Old Bootloader)" if upload fails
- Some clones have Mini-USB, some have Micro-USB

## Notes

- Perfect for breadboard prototyping
- A6, A7 are analog input only (not digital)
- Newer official Nano has Micro-USB
- Clone pricing makes them ideal for permanent installations

## Local Files

*Documentation to be downloaded*
