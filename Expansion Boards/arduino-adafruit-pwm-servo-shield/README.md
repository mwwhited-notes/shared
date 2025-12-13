# Adafruit 16-Channel 12-bit PWM/Servo Shield

**Arduino Shield - PWM/Servo Motor Control**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | Adafruit |
| Board | 16-Channel 12-bit PWM/Servo Shield |
| Product ID | 1411 |
| Platform | Arduino |
| Form Factor | Shield (UNO R3 footprint) |
| Primary Function | PWM/Servo control via I2C |
| Main IC | PCA9685 |
| Quantity | 1 |

## Compatibility

| Compatible With | Notes |
|-----------------|-------|
| Arduino UNO | Primary target |
| Arduino Mega | Compatible |
| Arduino Leonardo | Compatible |
| Any I2C-capable board | Uses only I2C (SDA/SCL) |

## Specifications

| Specification | Value |
|--------------|-------|
| PWM Channels | 16 |
| PWM Resolution | 12-bit (4096 steps) |
| PWM Frequency | 40 Hz - 1000 Hz (adjustable) |
| Interface | I2C |
| I2C Address | 0x40 (default), 0x40-0x7F (configurable) |
| Logic Voltage | 3.3V - 5V |
| Servo Voltage | Up to 6V (separate V+ input) |
| Output Current | 25mA per channel (sink), 10mA (source) |
| Series Resistors | 220 ohm on each output |
| Chainable | Yes, up to 62 boards (992 outputs) |
| Dimensions | 54mm x 70mm x 3mm |

## Pin Mapping

| Shield Pin | Arduino Pin | Function | Notes |
|------------|-------------|----------|-------|
| SDA | A4 (UNO) / 20 (Mega) | I2C Data | Directly connected |
| SCL | A5 (UNO) / 21 (Mega) | I2C Clock | Directly connected |
| V+ | - | Servo Power | External 5-6V via terminal |
| VCC | 5V | Logic Power | From Arduino |
| GND | GND | Ground | Common ground |

### Pins Used

- **Power:** VCC (5V), GND, V+ (external servo power)
- **Communication:** SDA, SCL (I2C)

### Stacking Compatibility

- [x] Passes through unused pins
- [x] Can stack with: Most shields (only uses I2C)
- [ ] Conflicts with: Other I2C devices at address 0x40 (change address via solder jumpers)

## Features

- 16 independent PWM channels
- 12-bit resolution (4096 steps per cycle)
- Built-in PWM oscillator - no continuous signal needed from MCU
- Adjustable frequency for servos or LEDs
- Chainable design for massive expansion
- Separate logic and servo power supplies
- 3-pin servo headers for easy connection
- Address jumpers for multi-board setups

## I2C Address Configuration

| A0 | A1 | A2 | A3 | A4 | A5 | Address |
|----|----|----|----|----|----| --------|
| 0 | 0 | 0 | 0 | 0 | 0 | 0x40 |
| 1 | 0 | 0 | 0 | 0 | 0 | 0x41 |
| 0 | 1 | 0 | 0 | 0 | 0 | 0x42 |
| ... | ... | ... | ... | ... | ... | ... |

Bridge solder jumpers to change address bits.

## Documentation

### Board Documentation
- [Product Page](https://www.adafruit.com/product/1411)
- [Learning Guide](https://learn.adafruit.com/16-channel-pwm-servo-driver)
- [Schematic (PDF)](https://learn.adafruit.com/assets/40728)

### IC Datasheets
- [PCA9685 Datasheet (NXP)](https://www.nxp.com/docs/en/data-sheet/PCA9685.pdf)

## Software & Libraries

### Official Libraries
- **Adafruit PWM Servo Driver Library** - Arduino library for PCA9685
- [GitHub Repository](https://github.com/adafruit/Adafruit-PWM-Servo-Driver-Library)

### Installation
```
# Arduino Library Manager
Search for: "Adafruit PWM Servo Driver Library"
```

### PlatformIO
```ini
lib_deps = adafruit/Adafruit PWM Servo Driver Library
```

## Example Code

```cpp
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

#define SERVOMIN  150  // Minimum pulse length count (out of 4096)
#define SERVOMAX  600  // Maximum pulse length count (out of 4096)

void setup() {
  Serial.begin(9600);
  pwm.begin();
  pwm.setPWMFreq(60);  // Analog servos run at ~60 Hz
}

void loop() {
  // Sweep servo on channel 0
  for (uint16_t pulselen = SERVOMIN; pulselen < SERVOMAX; pulselen++) {
    pwm.setPWM(0, 0, pulselen);
  }
  delay(500);
  for (uint16_t pulselen = SERVOMAX; pulselen > SERVOMIN; pulselen--) {
    pwm.setPWM(0, 0, pulselen);
  }
  delay(500);
}
```

## Notes

- Use separate power supply for servos (V+ terminal) when driving multiple servos
- Do NOT exceed 6V on V+ terminal
- The 220 ohm series resistors allow direct LED connection
- PWM frequency affects all 16 channels simultaneously
- For LEDs, use higher frequencies (1000+ Hz) to avoid flicker

## Local Files

*To be downloaded*

- `PCA9685_Datasheet.pdf` - PWM controller IC datasheet
- `Adafruit_PWM_Servo_Shield_Schematic.pdf` - Board schematic
