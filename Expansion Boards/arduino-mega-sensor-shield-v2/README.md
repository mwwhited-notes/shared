# Arduino Mega Sensor Shield V2.0

**Arduino Mega Shield - Sensor/Servo/Communication Breakout**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | Various |
| Board | Mega Sensor Shield V2.0 |
| Platform | Arduino Mega |
| Form Factor | Shield (Mega footprint) |
| Primary Function | Sensor, servo, and communication breakout |
| Dimensions | 100mm x 55mm |
| Quantity | 2 |

## Compatibility

| Compatible With | Notes |
|-----------------|-------|
| Arduino Mega 2560 | Primary target |
| Arduino Mega 1280 | Compatible |
| Arduino Mega ADK | Compatible |

## Specifications

| Specification | Value |
|--------------|-------|
| Digital I/O Headers | 54 (D0-D53) |
| Analog Headers | 16 (A0-A15) |
| Servo Connectors | 32 |
| I2C Interface | Yes |
| Bluetooth Interface | Yes (module not included) |
| SD Card Interface | Yes (directly accessible) |
| APC220 RF Interface | Yes |
| Ultrasonic Interface | Yes (RB URF v1.1) |
| LCD Interface | Serial and Parallel |
| ICSP Header | Yes |

## Pin Mapping

All pins broken out to 3-pin headers (Signal, VCC, GND):

| Connector Group | Pins | Type |
|-----------------|------|------|
| Digital | D0-D53 | 3-pin (S, V, G) |
| Analog | A0-A15 | 3-pin (S, V, G) |
| I2C | SDA (20), SCL (21) | 4-pin header |
| Serial1 | TX1 (18), RX1 (19) | For Bluetooth |
| Serial2 | TX2 (16), RX2 (17) | For APC220 |
| Serial3 | TX3 (14), RX3 (15) | Available |

### Communication Module Interfaces

| Interface | Pins | Purpose |
|-----------|------|---------|
| Bluetooth | D18 (TX1), D19 (RX1) | HC-05/HC-06 modules |
| APC220 RF | D16 (TX2), D17 (RX2) | Wireless RF module |
| SD Card | D50-D53 (SPI) | SD card access |
| I2C | D20 (SDA), D21 (SCL) | I2C devices |

### Pins Used

- **Power:** 5V, GND (distributed)
- **Passthrough:** All 54 digital, 16 analog pins

### Stacking Compatibility

- [x] Passes through all pins
- [x] Can stack with: Most Mega-compatible shields
- [ ] Conflicts with: Shields using same communication pins

## Features

- All 54 digital pins broken out to 3-pin servo headers
- All 16 analog pins accessible
- 32 dedicated servo motor connections
- Bluetooth module socket (HC-05/HC-06)
- APC220 RF module socket
- SD card interface passthrough
- RB URF ultrasonic sensor interface
- LCD serial and parallel interfaces
- I2C header for easy sensor connection
- External power option for servos
- ICSP header access

## Power Configuration

### Servo Power Jumper

| Setting | Source | Notes |
|---------|--------|-------|
| Jumper ON | Arduino 5V | Limited to ~300mA total |
| Jumper OFF | External | Use terminal block for servo power |

**Important:** When using multiple servos, remove jumper and supply external 5-6V power.

## Documentation

### Board Documentation
- [TwinSchip Guide](https://www.twinschip.com/Arduino_Mega_Sensor_Shield)
- [Cirkit Designer Docs](https://docs.cirkitdesigner.com/component/e70ac574-48f3-e7f8-de8f-2d743bdd7902/arduino-mega-sensor-shield-v2)

## Software & Libraries

No special library required - breakout shield. Use standard Arduino libraries for connected modules.

### Common Libraries
- `SD.h` - SD card access
- `Wire.h` - I2C communication
- `SoftwareSerial.h` - Additional serial ports (not needed on Mega)

## Example Code

```cpp
// Example: Using multiple serial interfaces on Mega

void setup() {
  Serial.begin(9600);   // USB Serial
  Serial1.begin(9600);  // Bluetooth (pins 18/19)
  Serial2.begin(9600);  // APC220 (pins 16/17)

  Serial.println("Mega Sensor Shield Ready");
}

void loop() {
  // Forward Bluetooth data to USB Serial
  if (Serial1.available()) {
    Serial.write(Serial1.read());
  }

  // Forward USB Serial to Bluetooth
  if (Serial.available()) {
    Serial1.write(Serial.read());
  }
}
```

## Notes

- Designed specifically for Arduino Mega (not UNO compatible)
- Multiple hardware serial ports available (Serial1, Serial2, Serial3)
- External power recommended for multiple servos
- SD card uses SPI pins (50-53)
- I2C on pins 20 (SDA) and 21 (SCL)
- All pin labels clearly marked on silkscreen

## Local Files

*To be downloaded*

- `Mega_Sensor_Shield_V2_Schematic.pdf` - Board schematic
