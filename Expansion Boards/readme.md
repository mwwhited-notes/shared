# Expansion Boards Inventory

Personal collection of Arduino shields, Raspberry Pi HATs, BeagleBone capes, and other development board expansion modules with specifications, documentation links, and compatibility information.

Each expansion board has its own directory with detailed specifications and locally archived documentation.

**[Expansion Boards Documentation Protocol](EXPANSION_BOARDS_DOCUMENTATION_PROTOCOL.md)** - Guide for adding new expansion boards and maintaining this inventory.

---

## Board Index

### Arduino Shields - Motor & Servo Control

| Shield | Function | Main IC | Interface | Qty | Directory |
|--------|----------|---------|-----------|-----|-----------|
| [Adafruit 16-Ch PWM/Servo](arduino-adafruit-pwm-servo-shield/) | 16-channel servo/PWM | PCA9685 | I2C | 1 | `arduino-adafruit-pwm-servo-shield/` |
| [OSEPP Motor & Servo](arduino-osepp-motor-servo-shield/) | 4 DC / 2 stepper / 2 servo | 2x L293D | PWM + Shift | 1 | `arduino-osepp-motor-servo-shield/` |

### Arduino Shields - Communication & Wireless

| Shield | Function | Main IC | Interface | Qty | Directory |
|--------|----------|---------|-----------|-----|-----------|
| [XBee Shield](arduino-xbee-shield/) | XBee wireless adapter | - | UART/SoftSerial | 2 | `arduino-xbee-shield/` |
| [RedBear BLE Shield v2.1](arduino-redbear-ble-shield/) | Bluetooth Low Energy | nRF8001 | SPI (ACI) | 1 | `arduino-redbear-ble-shield/` |
| [RS232/RS485 Shield](arduino-rs232-rs485-shield/) | Industrial serial | MAX232/MAX485 | UART | 1 | `arduino-rs232-rs485-shield/` |

### Arduino Shields - Sensors & Data

| Shield | Function | Main IC | Interface | Qty | Directory |
|--------|----------|---------|-----------|-----|-----------|
| [SainSmart Sensor Shield v4.0](arduino-sainsmart-sensor-shield-v4/) | Sensor breakout | - | Passthrough | 2 | `arduino-sainsmart-sensor-shield-v4/` |
| [Mega Sensor Shield v2.0](arduino-mega-sensor-shield-v2/) | Mega sensor breakout | - | Passthrough | 2 | `arduino-mega-sensor-shield-v2/` |
| [Robogaia 6-Axis IMU](arduino-robogaia-6axis-imu/) | Gyro + Accelerometer | MPU-6050 | I2C | 1 | `arduino-robogaia-6axis-imu/` |
| [Deek-Robot Data Logger](arduino-deek-robot-data-logging-shield/) | SD card + RTC | DS1307 | SPI + I2C | 3 | `arduino-deek-robot-data-logging-shield/` |

### Arduino Shields - Display & UI

| Shield | Function | Main IC | Interface | Qty | Directory |
|--------|----------|---------|-----------|-----|-----------|
| [OSEPP LCD Keypad](arduino-osepp-lcd-keypad-shield/) | 16x2 LCD + 5 buttons | HD44780 | 4-bit parallel | 1 | `arduino-osepp-lcd-keypad-shield/` |
| [Multi-Function Shield](arduino-multi-function-shield/) | 7-seg, LEDs, buttons, buzzer | 74HC595 | Shift register | 1 | `arduino-multi-function-shield/` |

### Arduino Shields - Programming & Development

| Shield | Function | Main IC | Interface | Qty | Directory |
|--------|----------|---------|-----------|-----|-----------|
| [Evil Mad Science ISP Shield 2.0](arduino-evil-mad-science-isp-shield/) | AVR ISP programmer | - | SPI | 1 | `arduino-evil-mad-science-isp-shield/` |

### Raspberry Pi HATs

| HAT | Function | Interface | Compatible Models | Qty | Directory |
|-----|----------|-----------|-------------------|-----|-----------|
| [PoE HAT (2018)](rpi-poe-hat-2018/) | Power over Ethernet | 802.3af PoE | Pi 3B+, Pi 4 | 1 | `rpi-poe-hat-2018/` |
| [ARPI600](rpi-arpi600/) | Arduino shield + XBee adapter | GPIO/I2C/SPI | Pi 2/3/4, Jetson | 1 | `rpi-arpi600/` |

### BeagleBone Capes

| Cape | Function | Interface | Compatible Models | Directory |
|------|----------|-----------|-------------------|-----------|
| *None yet* | | | | |

### ESP32/ESP8266 Shields

| Shield | Function | Interface | Compatible Boards | Directory |
|--------|----------|-----------|-------------------|-----------|
| *None yet* | | | | |

---

## Quick Reference by Function

### Motor Control
- [Adafruit 16-Ch PWM/Servo](arduino-adafruit-pwm-servo-shield/) - I2C, 16 channels, stackable
- [OSEPP Motor & Servo](arduino-osepp-motor-servo-shield/) - L293D, 4 DC motors + 2 servos

### Wireless Communication
- [XBee Shield](arduino-xbee-shield/) - ZigBee/802.15.4 via XBee modules
- [RedBear BLE Shield](arduino-redbear-ble-shield/) - Bluetooth 4.0 Low Energy

### Serial Communication
- [RS232/RS485 Shield](arduino-rs232-rs485-shield/) - Industrial serial protocols

### Sensors & IMU
- [Robogaia 6-Axis IMU](arduino-robogaia-6axis-imu/) - MPU-6050 accelerometer + gyroscope
- [SainSmart Sensor Shield](arduino-sainsmart-sensor-shield-v4/) - Breakout for UNO
- [Mega Sensor Shield](arduino-mega-sensor-shield-v2/) - Breakout for Mega

### Data Logging
- [Deek-Robot Data Logger](arduino-deek-robot-data-logging-shield/) - SD card + DS1307 RTC

### Display & User Interface
- [OSEPP LCD Keypad](arduino-osepp-lcd-keypad-shield/) - 16x2 LCD + buttons
- [Multi-Function Shield](arduino-multi-function-shield/) - 7-segment + LEDs + buttons

### Programming Tools
- [Evil Mad Science ISP Shield](arduino-evil-mad-science-isp-shield/) - AVR ISP programmer

### Power
- [Raspberry Pi PoE HAT](rpi-poe-hat-2018/) - 802.3af Power over Ethernet

### Platform Adapters
- [ARPI600](rpi-arpi600/) - Arduino shields on Raspberry Pi (3.3V only!)

---

## Directory Structure

```
├── readme.md                                    # This file
├── EXPANSION_BOARDS_DOCUMENTATION_PROTOCOL.md   # Protocol document
├── MISSING_DOCUMENTATION.md                     # Tracks failed downloads
├── sync-docs.bat                                # OneDrive sync script
│
├── arduino-adafruit-pwm-servo-shield/           # Motor/Servo
├── arduino-osepp-motor-servo-shield/
│
├── arduino-xbee-shield/                         # Communication
├── arduino-redbear-ble-shield/
├── arduino-rs232-rs485-shield/
│
├── arduino-sainsmart-sensor-shield-v4/          # Sensors
├── arduino-mega-sensor-shield-v2/
├── arduino-robogaia-6axis-imu/
├── arduino-deek-robot-data-logging-shield/
│
├── arduino-osepp-lcd-keypad-shield/             # Display/UI
├── arduino-multi-function-shield/
│
├── arduino-evil-mad-science-isp-shield/         # Programming
│
├── rpi-poe-hat-2018/                            # Raspberry Pi
└── rpi-arpi600/
```

---

## Compatibility Cross-Reference

### Arduino Shield Compatibility

| Shield | UNO | Mega | Leonardo | Due | Notes |
|--------|-----|------|----------|-----|-------|
| Adafruit PWM/Servo | ✓ | ✓ | ✓ | ✓ | I2C only |
| OSEPP Motor & Servo | ✓ | ✓ | ✓ | - | Uses many PWM pins |
| XBee Shield | ✓ | ✓ | ✓ | - | Serial switch |
| RedBear BLE | ✓ | ✓ | ✓ | ✓ | SPI pins vary |
| RS232/RS485 | ✓ | ✓ | ~ | - | Serial mode |
| SainSmart Sensor v4 | ✓ | ~ | ✓ | - | I2C UNO only |
| Mega Sensor v2 | - | ✓ | - | - | Mega only |
| Robogaia IMU | ✓ | ✓ | ✓ | ✓ | I2C |
| Deek-Robot Logger | ✓ | ✓ | ✓ | - | SPI + I2C |
| OSEPP LCD Keypad | ✓ | ✓ | ✓ | - | Parallel LCD |
| Multi-Function | ✓ | ✓ | ✓ | - | Many pins |
| ISP Shield | ✓ | - | - | - | UNO/Duemilanove |

### Pin Conflict Quick Reference

| Shield | D0-1 | D2-3 | D4-7 | D8-9 | D10-13 | A0 | A1-3 | A4-5 |
|--------|------|------|------|------|--------|----|----- |------|
| Adafruit PWM | | | | | | | | I2C |
| OSEPP Motor | | | ✓ | | ✓ | | | |
| XBee | ✓/~ | ✓/~ | | | | | | |
| RedBear BLE | | | ✓ | ✓ | ✓ | | | |
| RS232/RS485 | ✓/~ | ✓/~ | | | | | | |
| Sensor v4 | | | | | | | | I2C |
| Robogaia IMU | | | | | | | | I2C |
| Data Logger | | | | | ✓ | | | I2C |
| LCD Keypad | | | ✓ | ✓ | ✓ | ✓ | | |
| Multi-Function | | | ✓ | | ✓ | ✓ | ✓ | ✓ |
| ISP Shield | | | ✓ | ✓ | ✓ | | | |

**Legend:** ✓ = Used, ~ = Optional/Switch selectable, I2C = Uses A4/A5 for I2C

---

## Common Interface Types

| Interface | Description | Typical Use |
|-----------|-------------|-------------|
| I2C | Two-wire serial | Sensors, displays, RTCs |
| SPI | Four-wire serial | SD cards, displays, high-speed |
| UART | Serial communication | GPS, Bluetooth, XBee |
| GPIO | General purpose I/O | Relays, buttons, LEDs |
| PWM | Pulse width modulation | Motor control, servos, LEDs |

---

## Notes

- Shield/HAT form factors may vary - always verify physical compatibility
- Some shields stack; check pin conflicts when using multiple shields
- Power requirements vary - verify total current draw doesn't exceed board limits
- Level shifting may be required between 5V Arduino shields and 3.3V boards
- **ARPI600 Warning:** No level shifting - only use 3.3V shields!

---

*Last updated: December 2024*
