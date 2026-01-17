# SainSmart Sensor Shield V4.0

**Arduino Shield - Sensor/Servo Breakout**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | SainSmart |
| Board | Sensor Shield V4.0 |
| Platform | Arduino |
| Form Factor | Shield |
| Primary Function | Sensor and servo breakout |
| Status | Discontinued |
| Quantity | 2 |

## Compatibility

| Compatible With | Notes |
|-----------------|-------|
| Arduino UNO | Primary target |
| Arduino Duemilanove | Compatible |
| Arduino Leonardo | Compatible |
| Arduino Mega | Compatible (I2C on different pins) |

## Specifications

| Specification | Value |
|--------------|-------|
| Analog Connectors | 6 (A0-A5) |
| Digital/Servo Headers | 14 (D0-D13) |
| I2C/UART Interface | 1 (4-pin, jumper selectable) |
| Communication | I2C or UART (jumper select) |
| Voltage Output | 5V and GND on all connectors |
| Reset Button | Yes |

## Pin Mapping

All Arduino pins are broken out to 3-pin headers (Signal, VCC, GND):

| Connector | Arduino Pin | Type | Notes |
|-----------|-------------|------|-------|
| A0-A5 | A0-A5 | Analog | 3-pin (S, V, G) |
| D0-D13 | D0-D13 | Digital/Servo | 3-pin (S, V, G) |
| I2C/UART | A4/A5 or D0/D1 | Serial | 4-pin, jumper select |
| AUX | A0-A5 | Auxiliary | Additional analog access |

### Header Pinout

Each 3-pin header:
```
[S] - Signal (to Arduino pin)
[V] - VCC (5V)
[G] - GND
```

### I2C/UART Jumper Settings

| Jumper | Connection | Use |
|--------|------------|-----|
| I2C | SDA=A4, SCL=A5 | I2C devices (sensors, displays) |
| UART | RX=D0, TX=D1 | Serial devices |

### Pins Used

- **Power:** 5V, GND (distributed to all headers)
- **Passthrough:** All digital and analog pins

### Stacking Compatibility

- [x] Passes through all pins
- [x] Can stack with: Most shields
- [ ] Conflicts with: None directly (just provides breakout)

## Features

- Easy plug-and-play sensor connections
- 3-pin servo-style headers on all I/O
- No soldering required for most sensors
- I2C and UART interface options
- Clearly labeled pin headers
- Reset button accessible on shield
- Compatible with common sensor modules

## Common Sensor Connections

| Sensor Type | Recommended Pins |
|-------------|------------------|
| Analog sensors | A0-A5 |
| Digital sensors | D2-D13 |
| Servos | D2-D13 (PWM: D3,5,6,9,10,11) |
| I2C devices | A4 (SDA), A5 (SCL) |
| Serial devices | D0 (RX), D1 (TX) |

## Documentation

### Board Documentation
- [SainSmart Product Page](https://www.sainsmart.com/products/sensor-shield-v4-module) (Discontinued)

## Software & Libraries

No special library required - this is a breakout shield. Use standard Arduino functions and sensor-specific libraries.

## Example Code

```cpp
// Example: Reading analog sensor on A0
// Connect sensor to A0 3-pin header

void setup() {
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(A0);
  Serial.print("Sensor: ");
  Serial.println(sensorValue);
  delay(100);
}
```

## Notes

- This shield is a passive breakout - no active components
- Power for sensors comes from Arduino 5V rail
- When using multiple servos, consider external power supply
- I2C interface only works properly with UNO (A4/A5 are I2C)
- Product has been discontinued by SainSmart
- Many clone versions available from other manufacturers

## Local Files

*No datasheets required - this is a passive breakout board with no active ICs.*
