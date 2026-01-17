# ESP8266MOD AI-Thinker (ESP-12F)

**WiFi Microcontroller Module**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | AI-Thinker |
| Module | ESP-12F (ESP8266MOD) |
| SoC | ESP8266EX |
| Date Acquired | |
| Quantity | |

## Specifications

| Specification | Value |
|--------------|-------|
| Processor | Tensilica L106 32-bit |
| Clock Speed | 80 MHz (160 MHz boost) |
| Flash | 4 MB (external SPI) |
| RAM | 80 KB user available |
| Instruction RAM | 32 KB |
| WiFi | 802.11 b/g/n (2.4 GHz) |
| GPIO | 11 usable |
| ADC | 1 (10-bit, 0-1V) |
| Operating Voltage | 3.3V |

## WiFi Specifications

| Feature | Value |
|---------|-------|
| Standards | 802.11 b/g/n |
| Frequency | 2.4 GHz |
| Security | WEP, WPA, WPA2 |
| Modes | Station, SoftAP, Station+SoftAP |
| Protocols | TCP/IP, HTTP, MQTT, etc. |

## Pinout

| Pin | Function | Notes |
|-----|----------|-------|
| GPIO0 | Boot mode / General | LOW = flash mode |
| GPIO1 | TX0 | UART0 TX |
| GPIO2 | General | Must be HIGH at boot |
| GPIO3 | RX0 | UART0 RX |
| GPIO4 | SDA | I2C data |
| GPIO5 | SCL | I2C clock |
| GPIO12 | MISO | SPI / General |
| GPIO13 | MOSI | SPI / General |
| GPIO14 | SCLK | SPI / General |
| GPIO15 | CS | Must be LOW at boot |
| GPIO16 | Wake | Deep sleep wake |
| ADC | A0 | 0-1V input only |

## Boot Mode Pins

| GPIO0 | GPIO2 | GPIO15 | Mode |
|-------|-------|--------|------|
| LOW | HIGH | LOW | Flash/Programming |
| HIGH | HIGH | LOW | Normal Boot |

## Features

- Full TCP/IP stack
- WiFi Direct (P2P)
- Integrated antenna (PCB trace)
- Metal shield for RF
- FCC/CE certified
- Low power modes

## Programming

| Method | Tools |
|--------|-------|
| USB-Serial | FTDI, CP2102 (3.3V only!) |
| OTA | Arduino OTA, espota |

### Programming Wiring

| Adapter | ESP-12F |
|---------|---------|
| TX | RX (GPIO3) |
| RX | TX (GPIO1) |
| GND | GND |
| 3.3V | VCC, CH_PD/EN |
| DTR (via cap) | GPIO0 |
| RTS (via cap) | RST |

**Pull-ups needed:** CH_PD/EN to VCC, GPIO0 to VCC, GPIO2 to VCC
**Pull-down needed:** GPIO15 to GND

## Documentation

- [ESP8266EX Datasheet](https://www.espressif.com/sites/default/files/documentation/0a-esp8266ex_datasheet_en.pdf)
- [ESP8266 Technical Reference](https://www.espressif.com/sites/default/files/documentation/esp8266-technical_reference_en.pdf)
- [ESP-12F Specifications](https://docs.ai-thinker.com/en/esp8266/spec/esp_12f)
- [ESP8266 Arduino Core](https://arduino-esp8266.readthedocs.io/)

## Software & Tools

- **Arduino IDE** - With ESP8266 board package
- **PlatformIO** - Alternative IDE
- **esptool.py** - Flashing utility
- **ESP8266 Arduino Core** - [Install URL](http://arduino.esp8266.com/stable/package_esp8266com_index.json)

### Arduino IDE Setup

1. File > Preferences > Additional Board URLs
2. Add: `http://arduino.esp8266.com/stable/package_esp8266com_index.json`
3. Tools > Board > Boards Manager > Install ESP8266
4. Select "Generic ESP8266 Module"

## Power Considerations

- Peak current draw: ~400mA during WiFi TX
- Requires stable 3.3V supply
- NOT 5V tolerant on any pin
- Add 100uF+ capacitor near VCC
- Deep sleep: ~20uA

## Notes

- **3.3V ONLY** - 5V will damage the chip
- Must have correct boot pin states
- GPIO0 LOW at power-on enters flash mode
- Limited GPIO compared to ESP32
- ADC limited to 0-1V (use voltage divider)
- ESP-12F is most common variant

## Local Files

*Documentation to be downloaded*
