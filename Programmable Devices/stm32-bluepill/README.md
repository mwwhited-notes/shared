# STM32 BluePill

**ARM Cortex-M3 Development Board**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | Teyleten Robot |
| Board | BluePill |
| MCU | STM32F103C8T6 |
| Status | Working |
| Date Ordered | 2023-04-02 |
| Purchase Price | $15.88 (5-pack) |
| Source | Amazon (Teyleten Robot-US) |
| Quantity | 5 |

## Specifications

| Specification | Value |
|--------------|-------|
| Core | ARM Cortex-M3 |
| Clock Speed | 72 MHz |
| Flash | 64 KB (often 128 KB*) |
| SRAM | 20 KB |
| Operating Voltage | 3.3V |
| I/O Voltage | 5V tolerant |
| GPIO | 32 |
| ADC | 2 x 12-bit (10 channels) |
| DAC | None |

*Many STM32F103C8T6 chips have 128KB flash despite being marked 64KB

## Peripherals

| Peripheral | Quantity |
|-----------|----------|
| UART | 3 |
| SPI | 2 |
| I2C | 2 |
| USB | 1 (Full Speed) |
| CAN | 1 |
| Timers | 4 (3x 16-bit, 1x PWM) |
| PWM | 15 channels |
| RTC | 1 |
| DMA | 7 channels |

## Board Features

- Micro-USB connector (USB or power only*)
- SWD header (4-pin)
- Reset button
- Boot jumpers (BOOT0, BOOT1)
- 8 MHz crystal
- 32.768 kHz RTC crystal
- User LED (PC13, active LOW)
- Power LED

*USB requires D+ pull-up resistor fix on many boards

## Pinout Overview

| Pin Group | Functions |
|-----------|-----------|
| PA0-PA15 | GPIO, ADC, UART, SPI, I2C, USB |
| PB0-PB15 | GPIO, ADC, UART, SPI, I2C, CAN |
| PC13 | User LED (active LOW) |
| PC14-PC15 | RTC crystal |

## Boot Modes

| BOOT1 | BOOT0 | Mode |
|-------|-------|------|
| X | 0 | Flash (normal) |
| 0 | 1 | System Memory (bootloader) |
| 1 | 1 | SRAM |

## Programming

| Method | Tools |
|--------|-------|
| SWD | ST-Link V2, J-Link |
| Serial Bootloader | USB-Serial (BOOT0=1) |
| USB DFU | After flashing DFU bootloader |

### ST-Link Wiring

| ST-Link | BluePill |
|---------|----------|
| SWDIO | SWDIO |
| SWCLK | SWCLK |
| GND | GND |
| 3.3V | 3.3V (optional) |

### Serial Bootloader

1. Set BOOT0 = 1
2. Connect USB-Serial (TX->PA10, RX->PA9)
3. Flash using stm32flash or STM32CubeProgrammer
4. Set BOOT0 = 0 and reset

## Documentation

- [STM32F103C8 Datasheet](https://www.st.com/resource/en/datasheet/stm32f103c8.pdf)
- [STM32F103 Reference Manual](https://www.st.com/resource/en/reference_manual/rm0008-stm32f101xx-stm32f102xx-stm32f103xx-stm32f105xx-and-stm32f107xx-advanced-armbased-32bit-mcus-stmicroelectronics.pdf)
- [STM32F103C8 Pinout](https://os.mbed.com/platforms/ST-Nucleo-F103RB/)

## Software & Tools

- **STM32CubeIDE** - Official ST IDE
- **Arduino IDE** - With STM32duino
- **PlatformIO** - Multi-framework support
- **STM32CubeProgrammer** - Flashing utility
- **OpenOCD** - Open source debugger

### Arduino IDE Setup (STM32duino)

1. File > Preferences > Additional Board URLs
2. Add: `https://github.com/stm32duino/BoardManagerFiles/raw/main/package_stmicroelectronics_index.json`
3. Tools > Board > Boards Manager > Install STM32
4. Select "Generic STM32F1 series" > "BluePill F103C8"

## Common Issues

### USB Not Working

Many BluePill clones have wrong USB pull-up resistor (10K instead of 1.5K on D+):

**Fix options:**
1. Replace R10 with 1.5K resistor
2. Add 1.8K resistor from PA12 to 3.3V
3. Use software USB pull-up (if supported)

### Fake STM32 Chips

Some boards have counterfeit chips:
- May have less flash
- May have timing issues
- Check chip markings carefully

## Notes

- Very capable for the price
- 5V tolerant I/O (unlike ESP8266/ESP32)
- Native USB (with fix)
- Large community and library support
- CAN bus support unusual at this price point
- LED on PC13 is active LOW (inverted)

## Local Files

### Pinout
![STM32 BluePill Pinout](STM32_BluePill_Pinout.jpg)

### Documentation
- `STM32F103C8_Datasheet.pdf` - Main MCU datasheet
- `STM32_BluePill_Pinout.jpg` - Board pinout diagram
