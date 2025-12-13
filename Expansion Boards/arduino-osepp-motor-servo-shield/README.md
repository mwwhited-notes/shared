# OSEPP Motor & Servo Shield v1.0

**Arduino Shield - DC Motor and Servo Control**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | OSEPP |
| Board | Motor & Servo Shield (SCSHD-01) |
| Version | v1.0 |
| Platform | Arduino |
| Form Factor | Shield |
| Primary Function | Motor and servo control |
| Main IC | 2x L293D |
| Quantity | 1 |

## Compatibility

| Compatible With | Notes |
|-----------------|-------|
| Arduino UNO | Primary target |
| Arduino Duemilanove | Compatible |
| Arduino Diecimila | Compatible |
| Arduino Mega | Compatible |

## Specifications

| Specification | Value |
|--------------|-------|
| Motor Driver IC | 2x L293D (Quad H-Bridge) |
| DC Motors | Up to 4 bi-directional |
| Stepper Motors | Up to 2 (unipolar/bipolar) |
| Servo Motors | 2 |
| Motor Voltage | 4.5V - 25V DC |
| Output Current | 0.6A per channel (1.2A peak) |
| PWM Speed Control | 8-bit resolution |
| Protection | Thermal shutdown, kickback diodes |

## Pin Mapping

| Shield Function | Arduino Pin | Notes |
|-----------------|-------------|-------|
| Motor 1 PWM | D11 | Speed control |
| Motor 2 PWM | D3 | Speed control |
| Motor 3 PWM | D6 | Speed control |
| Motor 4 PWM | D5 | Speed control |
| Shift Register | D4, D7, D8, D12 | Motor direction |
| Servo 1 | D9 | PWM servo control |
| Servo 2 | D10 | PWM servo control |

### Motor Channel Mapping

| Motor | PWM Pin | Direction Control |
|-------|---------|-------------------|
| M1 | D11 | Shift register |
| M2 | D3 | Shift register |
| M3 | D6 | Shift register |
| M4 | D5 | Shift register |

### Pins Used

- **Power:** VIN or external motor power, 5V for servos
- **PWM:** D3, D5, D6, D11 (motor speed)
- **Digital:** D4, D7, D8, D12 (shift register)
- **Servo:** D9, D10

### Stacking Compatibility

- [ ] Passes through unused pins - Limited
- [ ] Can stack with: Shields not using motor pins
- [x] Conflicts with: Most PWM-using shields

## Features

- 4 DC motors with individual speed control
- 2 stepper motors (single/double coil/interleaved)
- 2 servo motor connections
- Separate motor and servo power inputs
- Terminal blocks for easy motor connection
- 3-pin servo headers
- Pull-down resistors prevent motor spin on startup
- Power indicator LEDs
- Reset button passthrough
- DIP sockets for easy IC replacement

## Power Configuration

### Motor Power

| Setting | Source | Notes |
|---------|--------|-------|
| M+ Terminal | External 4.5-25V | Recommended for motors |
| VIN Jumper | Arduino VIN | Limited current |

### Servo Power

| Setting | Source | Notes |
|---------|--------|-------|
| Servo Terminal | External 5-6V | Recommended for servos |
| 5V Jumper | Arduino 5V | Limited to ~500mA |

## Documentation

### Board Documentation
- [OSEPP Product Page](https://osepp.com/electronic-modules/shields/49-motor-servo-shield)
- [RadioShack Product Page](https://www.radioshack.com/products/scshd-01-osepp-motor-and-servo-shield)

### IC Datasheets
- [L293D Datasheet](https://www.ti.com/lit/ds/symlink/l293d.pdf)

## Software & Libraries

### Adafruit Motor Shield Library (Compatible)
```
# Arduino Library Manager
Search for: "Adafruit Motor Shield Library"
```

The OSEPP shield is compatible with the Adafruit Motor Shield library (AFMotor).

## Example Code

```cpp
#include <AFMotor.h>

AF_DCMotor motor1(1);  // Motor on M1
AF_DCMotor motor2(2);  // Motor on M2
Servo servo1;

void setup() {
  motor1.setSpeed(200);  // 0-255
  motor2.setSpeed(200);

  servo1.attach(9);  // Servo on pin 9
}

void loop() {
  // Run motor forward
  motor1.run(FORWARD);
  motor2.run(FORWARD);
  delay(1000);

  // Run motor backward
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
  delay(1000);

  // Stop motors
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  delay(500);

  // Sweep servo
  for (int pos = 0; pos <= 180; pos++) {
    servo1.write(pos);
    delay(15);
  }
}
```

### Stepper Motor Example

```cpp
#include <AFMotor.h>

AF_Stepper stepper(200, 1);  // 200 steps/rev, port 1

void setup() {
  stepper.setSpeed(30);  // 30 RPM
}

void loop() {
  stepper.step(100, FORWARD, SINGLE);
  stepper.step(100, BACKWARD, SINGLE);

  stepper.step(100, FORWARD, DOUBLE);
  stepper.step(100, BACKWARD, DOUBLE);

  stepper.step(100, FORWARD, INTERLEAVE);
  stepper.step(100, BACKWARD, INTERLEAVE);
}
```

## Notes

- Use external power for motors - Arduino power is insufficient
- L293D chips can be replaced if damaged (DIP socket)
- Thermal shutdown protects against overheating
- Internal kickback diodes protect against motor noise
- Motors disabled during Arduino startup (pull-down resistors)
- Compatible with AFMotor library from Adafruit

## Local Files

*To be downloaded*

- `L293D_Datasheet.pdf` - Motor driver IC datasheet
- `OSEPP_Motor_Shield_Schematic.pdf` - Board schematic
