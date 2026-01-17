# Missing Documentation

This file tracks documentation that couldn't be automatically downloaded and requires manual action.

---

## Pending Downloads

### arduino-deek-robot-data-logging-shield
- [ ] **DS1307 RTC Datasheet** - Real-time clock IC
  - Source: https://www.analog.com/media/en/technical-documentation/data-sheets/ds1307.pdf
  - Issue: Analog Devices blocks automated downloads (SSL error)
  - Manual download: Visit URL in browser, save to `arduino-deek-robot-data-logging-shield/DS1307_Datasheet.pdf`

### arduino-redbear-ble-shield
- [ ] **nRF8001 Product Specification** - BLE chip datasheet
  - Source: https://infocenter.nordicsemi.com/pdf/nRF8001_PS_v1.3.pdf
  - Issue: Nordic redirects to documentation portal (requires navigation)
  - Manual download: Visit Nordic DevZone, search for nRF8001, download PS v1.3
  - Alternative: https://www.nordicsemi.com/Products/nRF8001

### arduino-rs232-rs485-shield
- [ ] **MAX485 Datasheet** - RS-485 transceiver IC
  - Source: https://www.analog.com/media/en/technical-documentation/data-sheets/MAX1487-MAX491.pdf
  - Issue: Analog Devices blocks automated downloads (SSL error)
  - Manual download: Visit URL in browser, save to `arduino-rs232-rs485-shield/MAX485_Datasheet.pdf`

### arduino-adafruit-pwm-servo-shield
- [ ] **Board Schematic** - PWM/Servo shield schematic
  - Source: https://learn.adafruit.com/16-channel-pwm-servo-driver (Assets section)
  - Issue: Direct PNG link returned redirect page
  - Manual download: Visit Adafruit Learn page, download schematic image

### rpi-arpi600
- [ ] **ARPI600 Schematic** - Expansion board schematic
  - Source: https://www.waveshare.com/wiki/ARPI600
  - Issue: Waveshare wiki requires navigation to download
  - Manual download: Visit wiki page, find schematic PDF in Resources section

### rpi-poe-hat-2018
- [ ] **PoE HAT Schematic** - Power over Ethernet HAT schematic
  - Source: https://www.raspberrypi.com/documentation/accessories/poe-hat.html
  - Issue: RPi Foundation may not publish full schematic
  - Manual download: Check documentation page for available resources

---

## Not Required (Passive/No Primary IC)

These boards don't require IC datasheets:

- **arduino-sainsmart-sensor-shield-v4** - Passive breakout board (no active ICs)
- **arduino-mega-sensor-shield-v2** - Passive breakout board (no active ICs)
- **arduino-evil-mad-science-isp-shield** - Uses Arduino as programmer (no dedicated IC)

---

## Completed

Documents successfully obtained.

### arduino-adafruit-pwm-servo-shield
- [x] **PCA9685 Datasheet** - Downloaded 2024-12-13
  - File: `PCA9685_Datasheet.pdf` (400 KB)

### arduino-multi-function-shield
- [x] **74HC595 Datasheet** - Downloaded 2024-12-13
  - File: `74HC595_Datasheet.pdf` (2.6 MB)
- [x] **Hackatronics Guide** - Downloaded 2024-12-13
  - File: `Multi_Function_Shield_Guide.pdf` (375 KB)

### arduino-osepp-lcd-keypad-shield
- [x] **HD44780 Datasheet** - Downloaded 2024-12-13
  - File: `HD44780_Datasheet.pdf` (323 KB)

### arduino-osepp-motor-servo-shield
- [x] **L293D Datasheet** - Downloaded 2024-12-13
  - File: `L293D_Datasheet.pdf` (354 KB)

### arduino-robogaia-6axis-imu
- [x] **MPU-6050 Datasheet** - Downloaded 2024-12-13
  - File: `MPU-6050_Datasheet.pdf` (1.6 MB)
- [x] **MPU-6050 Register Map** - Downloaded 2024-12-13
  - File: `MPU-6050_RegisterMap.pdf` (900 KB)

### arduino-rs232-rs485-shield
- [x] **MAX232 Datasheet** - Downloaded 2024-12-13
  - File: `MAX232_Datasheet.pdf` (1.7 MB)

### arduino-xbee-shield
- [x] **XBee Shield Schematic** - Downloaded 2024-12-13
  - File: `XBee_Shield_Schematic.pdf` (141 KB)

### rpi-arpi600
- [x] **PCF8563 RTC Datasheet** - Downloaded 2024-12-13
  - File: `PCF8563_Datasheet.pdf` (484 KB)

---

*Last updated: December 2024*
