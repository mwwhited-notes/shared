# Inland ESP32

**WiFi + Bluetooth Development Board**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | Inland (Micro Center) |
| Model | KS0413 |
| Module | ESP32-WROOM-32D |
| SoC | ESP32-D0WDQ6 |
| Date Acquired | |
| Quantity | |

## Specifications

| Specification | Value |
|--------------|-------|
| Processor | Dual-core Xtensa LX6 |
| Clock Speed | Up to 240 MHz |
| Flash | 4 MB |
| SRAM | 520 KB |
| RTC SRAM | 16 KB |
| WiFi | 802.11 b/g/n (2.4 GHz) |
| Bluetooth | Classic + BLE 4.2 |
| GPIO | 34 |
| ADC | 18 channels (12-bit) |
| DAC | 2 channels (8-bit) |
| Operating Voltage | 3.3V |
| Input Voltage | 5V via USB |

## Wireless Specifications

| Feature | Value |
|---------|-------|
| WiFi Standards | 802.11 b/g/n |
| WiFi Frequency | 2.4 GHz |
| Bluetooth | v4.2 BR/EDR + BLE |
| Modes | Station, SoftAP, Station+SoftAP |

## Peripherals

| Peripheral | Quantity |
|-----------|----------|
| SPI | 4 |
| I2C | 2 |
| I2S | 2 |
| UART | 3 |
| PWM | 16 channels |
| Touch Sensors | 10 |
| ADC | 18 (12-bit) |
| DAC | 2 (8-bit) |
| Hall Sensor | 1 |
| Temperature Sensor | 1 |

## Board Features

- USB-Serial (CP2102 or CH340)
- Micro-USB connector
- Boot and Reset buttons
- Onboard LED (GPIO2)
- 30-pin variant (fits breadboard with 1 row each side)
- 3.3V regulator

## GPIO Notes

| GPIO | Notes |
|------|-------|
| GPIO0 | Boot mode (has pull-up) |
| GPIO1 | TX0 |
| GPIO2 | Onboard LED |
| GPIO3 | RX0 |
| GPIO6-11 | Connected to flash (don't use) |
| GPIO34-39 | Input only, no pull-up/down |

## Programming

| Method | Tools |
|--------|-------|
| USB (Bootloader) | Arduino IDE, PlatformIO |
| OTA | Arduino OTA, ESP-IDF OTA |
| UART | esptool.py |

## Documentation

- [ESP32 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf)
- [ESP32 Technical Reference](https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_en.pdf)
- [ESP32-WROOM-32 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32_datasheet_en.pdf)
- [ESP32 Arduino Core](https://docs.espressif.com/projects/arduino-esp32/)

## Software & Tools

- **Arduino IDE** - With ESP32 board package
- **PlatformIO** - Alternative IDE
- **ESP-IDF** - Official Espressif framework
- **esptool.py** - Flashing utility
- [ESP32 Arduino Core](https://github.com/espressif/arduino-esp32)

### Arduino IDE Setup

1. File > Preferences > Additional Board URLs
2. Add: `https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json`
3. Tools > Board > Boards Manager > Install ESP32
4. Select "ESP32 Dev Module" or "Inland ESP32"

## Power Modes

| Mode | Current |
|------|---------|
| Active (WiFi TX) | ~240 mA |
| Active (CPU only) | ~30 mA |
| Modem Sleep | ~20 mA |
| Light Sleep | ~0.8 mA |
| Deep Sleep | ~10 uA |

## Notes

### Inland-Specific Quirks
- **Pin labels on bottom** - Silkscreen is on underside to keep board compact for breadboard use
- **BOOT button must be held throughout programming** - Unlike other ESP32 boards that only need BOOT held at power-up
- **Pinout differs from generic ESP32-WROOM-32** - See [natedogg2020/Inland_ESP32-Supplements](https://github.com/natedogg2020/Inland_ESP32-Supplements) for detailed mapping

### General ESP32 Notes
- GPIO6-11 are used for internal flash - avoid using
- GPIO34-39 are input only
- More capable than ESP8266 (dual-core, BLE, more GPIO)
- 3.3V logic but 5V tolerant on some pins (check datasheet)
- Touch pins can wake from deep sleep

## Local Files

### Pinout
**Note:** Pin labels are on the BOTTOM of the board. See both images:

![Inland ESP32 Top View](Inland_ESP32_Pinout_Top.jpg)
![Inland ESP32 Bottom View (Pin Labels)](Inland_ESP32_Pinout_Bottom.jpg)

### Documentation
- `ESP32_Datasheet.pdf` - ESP32 SoC datasheet
- `Inland_ESP32_Pinout_Top.jpg` - Board top view
- `Inland_ESP32_Pinout_Bottom.jpg` - Board bottom view with pin labels
