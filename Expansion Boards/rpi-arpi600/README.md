# Waveshare ARPI600

**Raspberry Pi Expansion - Arduino Shield & XBee Adapter**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | Waveshare |
| Board | ARPI600 |
| Platform | Raspberry Pi |
| Form Factor | HAT-style expansion |
| Primary Function | Arduino shield adapter + XBee socket |
| Main IC | PCF8563 (RTC) |
| Quantity | 1 |

## Compatibility

| Compatible With | Notes |
|-----------------|-------|
| Raspberry Pi 3 Model B+ | 40-pin GPIO |
| Raspberry Pi 3 Model B | 40-pin GPIO |
| Raspberry Pi 4 Model B | 40-pin GPIO |
| Raspberry Pi 2 Model B | 40-pin GPIO |
| Raspberry Pi Model B+ | 40-pin GPIO |
| Jetson Nano | 40-pin GPIO |
| Arduino UNO Shields | **3.3V ONLY - No level shifting!** |

## Specifications

| Specification | Value |
|--------------|-------|
| GPIO Header | 40-pin Raspberry Pi standard |
| Arduino Headers | UNO R3 footprint |
| XBee Socket | 2mm pitch, 20-pin |
| RTC Chip | PCF8563 |
| RTC I2C Address | 0x51 |
| ADC | Via analog pins (optional) |
| USB-UART | CP2102 or similar |
| Level Shifting | **NONE** - 3.3V direct connection |

## Pin Mapping

### Raspberry Pi to Arduino Pin Mapping

| Arduino Pin | RPi BCM GPIO | RPi Physical | Notes |
|-------------|--------------|--------------|-------|
| D0 (RX) | GPIO 15 | Pin 10 | UART RX |
| D1 (TX) | GPIO 14 | Pin 8 | UART TX |
| D2 | GPIO 18 | Pin 12 | |
| D3 | GPIO 27 | Pin 13 | |
| D4 | GPIO 22 | Pin 15 | |
| D5 | GPIO 23 | Pin 16 | |
| D6 | GPIO 24 | Pin 18 | |
| D7 | GPIO 25 | Pin 22 | |
| D8 | GPIO 4 | Pin 7 | |
| D9 | GPIO 5 | Pin 29 | |
| D10 | GPIO 6 | Pin 31 | SPI CE0 |
| D11 | GPIO 10 | Pin 19 | SPI MOSI |
| D12 | GPIO 9 | Pin 21 | SPI MISO |
| D13 | GPIO 11 | Pin 23 | SPI CLK |
| SDA | GPIO 2 | Pin 3 | I2C |
| SCL | GPIO 3 | Pin 5 | I2C |

### Analog Pins (A0-A5)

Configurable via jumpers:
- **Position 1**: GPIO/IO pins
- **Position 3**: ADC input (if ADC chip populated)

### XBee Serial Configuration

Use jumpers to route serial connections:

| Jumper Setting | Connection |
|----------------|------------|
| P_RX ↔ CP_TX, P_TX ↔ CP_RX | USB-UART to RPi serial |
| XB_RX ↔ CP_TX, XB_TX ↔ CP_RX | USB-UART to XBee |
| XB_RX ↔ P_TX, XB_TX ↔ P_RX | RPi serial to XBee |

### Pins Used

- **Power:** 3.3V, 5V, GND
- **I2C:** GPIO 2 (SDA), GPIO 3 (SCL)
- **SPI:** GPIO 9, 10, 11
- **UART:** GPIO 14, 15
- **General GPIO:** Multiple

### Stacking Compatibility

- [x] Passes through 40-pin GPIO
- [ ] Can stack with: **3.3V Arduino shields ONLY**
- [x] Conflicts with: 5V Arduino shields (NO LEVEL SHIFTING)

## Features

- Run Arduino shields on Raspberry Pi
- XBee module socket for wireless communication
- USB to UART converter for debugging
- PCF8563 RTC with battery backup (CR2032)
- Multiple serial routing options via jumpers
- 40-pin GPIO passthrough
- Arduino UNO R3 form factor

## Important Warnings

### Voltage Level Warning

> **CRITICAL**: The ARPI600 has **NO LEVEL SHIFTING** between the Raspberry Pi (3.3V) and Arduino shield connectors.
>
> **DO NOT use standard 5V Arduino shields!** This will damage your Raspberry Pi.
>
> Only use shields that are:
> - Designed for 3.3V operation
> - Have their own level shifting
> - Are specifically marked as 3.3V/5V compatible

### Compatible Shield Types

| Shield Type | Compatible | Notes |
|-------------|------------|-------|
| 3.3V shields | Yes | Safe to use directly |
| 5V shields | **NO** | Will damage RPi! |
| Level-shifted shields | Yes | Has built-in protection |
| I2C shields (3.3V) | Yes | Most I2C is 3.3V compatible |

## RTC Usage

The PCF8563 RTC is at I2C address 0x51.

### Verify RTC Detection
```bash
sudo i2cdetect -y 1
# Should show 51 in the grid
```

### Enable RTC in Raspberry Pi
```bash
# Add to /boot/config.txt
dtoverlay=i2c-rtc,pcf8563

# Remove fake-hwclock
sudo apt-get remove fake-hwclock
sudo update-rc.d -f fake-hwclock remove
```

### Set RTC Time
```bash
# Write system time to RTC
sudo hwclock -w

# Read RTC time
sudo hwclock -r
```

## Documentation

### Board Documentation
- [Waveshare Product Page](https://www.waveshare.com/arpi600.htm)
- [Waveshare Wiki](https://www.waveshare.com/wiki/ARPI600)

### IC Datasheets
- [PCF8563 RTC Datasheet](https://www.nxp.com/docs/en/data-sheet/PCF8563.pdf)

## Software Setup

### Enable I2C and SPI
```bash
sudo raspi-config
# Interface Options > I2C > Enable
# Interface Options > SPI > Enable
```

### GPIO Access (Python)
```python
import RPi.GPIO as GPIO

# Use BCM numbering (matches Arduino pin mapping above)
GPIO.setmode(GPIO.BCM)

# Example: Arduino D2 = BCM GPIO 18
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.HIGH)
```

### I2C Access (Python)
```python
import smbus

bus = smbus.SMBus(1)

# Read from RTC (address 0x51)
data = bus.read_byte_data(0x51, 0x02)
```

## Example: Using with 3.3V Shield

```python
#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

# Arduino pin to BCM mapping
ARDUINO_D13 = 11  # BCM GPIO 11

GPIO.setmode(GPIO.BCM)
GPIO.setup(ARDUINO_D13, GPIO.OUT)

try:
    while True:
        GPIO.output(ARDUINO_D13, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(ARDUINO_D13, GPIO.LOW)
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
```

## Notes

- **NO 5V TOLERANCE** - This is the most critical limitation
- RTC needs CR2032 battery (not included, not common in stores)
- XBee modules operate at 3.3V - compatible
- USB-UART useful for debugging or XBee configuration
- Consider Waveshare's other boards if you need 5V shield support
- Jetson Nano compatible via 40-pin header

## Local Files

*To be downloaded*

- `PCF8563_Datasheet.pdf` - RTC chip datasheet
- `ARPI600_Schematic.pdf` - Board schematic
