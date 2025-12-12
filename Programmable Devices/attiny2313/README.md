# ATtiny2313

**Minimal AVR Microcontroller**

## Device Information

| Field | Value |
|-------|-------|
| Manufacturer | Microchip (Atmel) |
| Part Number | ATtiny2313 / ATtiny2313A |
| Package | DIP-20, SOIC-20 |
| Date Acquired | |
| Quantity | |

## Specifications

| Specification | Value |
|--------------|-------|
| Architecture | AVR 8-bit |
| Clock Speed | Up to 20 MHz |
| Flash | 2 KB |
| SRAM | 128 bytes |
| EEPROM | 128 bytes |
| I/O Pins | 18 |
| Operating Voltage | 2.7-5.5V (ATtiny2313A: 1.8-5.5V) |

## Peripherals

| Peripheral | Details |
|-----------|---------|
| Timers | 1x 8-bit, 1x 16-bit |
| PWM | 4 channels |
| UART | 1 (full duplex) |
| USI | 1 (SPI/I2C capable) |
| Analog Comparator | 1 |
| External Interrupts | 2 + pin change |

## Pinout (DIP-20)

```
                 ATtiny2313
                 +----U----+
    (RESET) PA2 -|1      20|- VCC
       (D0) PD0 -|2      19|- PB7 (D17/SCK)
       (D1) PD1 -|3      18|- PB6 (D16/MISO)
       (D2) PA1 -|4      17|- PB5 (D15/MOSI)
       (D3) PA0 -|5      16|- PB4 (D14)
  (D4/INT0) PD2 -|6      15|- PB3 (D13/OC1A)
  (D5/INT1) PD3 -|7      14|- PB2 (D12/OC0A)
       (D6) PD4 -|8      13|- PB1 (D11/AIN1)
       (D7) PD5 -|9      12|- PB0 (D10/AIN0)
            GND -|10     11|- PD6 (D8)
                 +---------+
```

## Features

- UART for serial communication
- USI for SPI/TWI (I2C)
- In-System Programming (ISP)
- debugWIRE on-chip debug
- Low power modes
- Internal RC oscillator (8 MHz, 4 MHz, 128 kHz)

## Programming

| Method | Tools |
|--------|-------|
| ISP | USBasp, AVR ISP, Arduino as ISP |
| debugWIRE | Atmel-ICE, AVR Dragon |
| High-Voltage | STK500, HV programmer |

### Arduino as ISP Wiring

| Arduino | ATtiny2313 |
|---------|-----------|
| Pin 10 | RESET (pin 1) |
| Pin 11 | MOSI (pin 17) |
| Pin 12 | MISO (pin 18) |
| Pin 13 | SCK (pin 19) |
| 5V | VCC (pin 20) |
| GND | GND (pin 10) |

## Documentation

- [ATtiny2313 Datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-2543-AVR-ATtiny2313_Datasheet.pdf)
- [ATtiny2313A Datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/doc8246.pdf)
- [AVR Instruction Set](https://ww1.microchip.com/downloads/en/devicedoc/atmel-0856-avr-instruction-set-manual.pdf)

## Software & Tools

- **Arduino IDE** - With ATTinyCore board package
- **AVRDUDE** - Command-line programming
- **Atmel Studio / Microchip Studio** - Full IDE
- [ATTinyCore](https://github.com/SpenceKonde/ATTinyCore)

## Fuse Settings

| Fuse | Default | Description |
|------|---------|-------------|
| LOW | 0x64 | 8MHz internal, CKDIV8 enabled (1MHz) |
| HIGH | 0xDF | SPIEN enabled, others default |
| EXTENDED | 0xFF | Self-program disabled |

### Common Configurations

```bash
# 8 MHz internal oscillator (disable CKDIV8)
avrdude -p attiny2313 -c usbasp -U lfuse:w:0xe4:m

# External crystal
avrdude -p attiny2313 -c usbasp -U lfuse:w:0xff:m
```

## Notes

- No ADC - use ATtiny2313A or ATtiny4313 if analog needed
- Very limited RAM (128 bytes) - careful with buffers
- UART makes debugging easier than many tiny AVRs
- Great for simple serial-controlled projects
- ATtiny4313 is pin-compatible with more memory

## Local Files

*Documentation to be downloaded*
