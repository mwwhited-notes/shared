# Robogaia 6-Axis Gyro/Accelerometer

**Arduino Shield - Inertial Measurement Unit (IMU)**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | Robogaia |
| Board | 6-Axis Gyro/Accelerometer |
| Platform | Arduino |
| Form Factor | Shield |
| Primary Function | Motion sensing (IMU) |
| Main IC | MPU-6050 (likely) |
| Quantity | 1 |

## Compatibility

| Compatible With | Notes |
|-----------------|-------|
| Arduino UNO | Primary target |
| Arduino Mega | Compatible (I2C pins differ) |
| Arduino Leonardo | Compatible |
| Arduino Due | 3.3V - check compatibility |

## Specifications

| Specification | Value |
|--------------|-------|
| Sensor Type | MEMS 6-DoF IMU |
| Accelerometer | 3-axis |
| Gyroscope | 3-axis |
| Interface | I2C |
| I2C Address | 0x68 (default) or 0x69 |
| ADC Resolution | 16-bit |
| Accelerometer Range | ±2g, ±4g, ±8g, ±16g |
| Gyroscope Range | ±250, ±500, ±1000, ±2000 °/s |
| Operating Voltage | 3.3V - 5V |

## Pin Mapping

| Shield Pin | Arduino Pin | Function | Notes |
|------------|-------------|----------|-------|
| SDA | A4 (UNO) / 20 (Mega) | I2C Data | |
| SCL | A5 (UNO) / 21 (Mega) | I2C Clock | |
| INT | D2 | Interrupt | Optional, for DMP |
| VCC | 5V | Power | On-board regulator to 3.3V |
| GND | GND | Ground | |

### Pins Used

- **Power:** 5V (or 3.3V), GND
- **I2C:** SDA (A4), SCL (A5)
- **Interrupt:** D2 (optional)

### Stacking Compatibility

- [x] Passes through unused pins
- [x] Can stack with: Most shields (only uses I2C)
- [ ] Conflicts with: Other I2C devices at 0x68

## Features

- 6 degrees of freedom (3-axis accel + 3-axis gyro)
- Built-in Digital Motion Processor (DMP)
- On-board 3.3V regulator (5V tolerant input)
- 16-bit ADC for high-resolution measurements
- Programmable full-scale ranges
- Low power modes available
- I2C fast mode (400kHz) support
- Temperature sensor included

## MPU-6050 Technical Details

### Accelerometer
| Range | Sensitivity |
|-------|-------------|
| ±2g | 16384 LSB/g |
| ±4g | 8192 LSB/g |
| ±8g | 4096 LSB/g |
| ±16g | 2048 LSB/g |

### Gyroscope
| Range | Sensitivity |
|-------|-------------|
| ±250 °/s | 131 LSB/(°/s) |
| ±500 °/s | 65.5 LSB/(°/s) |
| ±1000 °/s | 32.8 LSB/(°/s) |
| ±2000 °/s | 16.4 LSB/(°/s) |

## Documentation

### Reference Documentation
- [MPU-6050 Product Page (InvenSense)](https://invensense.tdk.com/products/motion-tracking/6-axis/mpu-6050/)
- [Arduino MPU6050 Tutorial](https://howtomechatronics.com/tutorials/arduino/arduino-and-mpu6050-accelerometer-and-gyroscope-tutorial/)
- [Adafruit MPU6050 Guide](https://learn.adafruit.com/mpu6050-6-dof-accelerometer-and-gyro)

### IC Datasheets
- [MPU-6050 Datasheet](https://invensense.tdk.com/wp-content/uploads/2015/02/MPU-6000-Datasheet1.pdf)
- [MPU-6050 Register Map](https://invensense.tdk.com/wp-content/uploads/2015/02/MPU-6000-Register-Map1.pdf)

## Software & Libraries

### Adafruit MPU6050 Library (Recommended)
```
# Arduino Library Manager
Search for: "Adafruit MPU6050"

# Also requires:
- Adafruit Unified Sensor
- Adafruit Bus IO
```

### Alternative Libraries
- **I2Cdev + MPU6050** - Jeff Rowberg's library with DMP support
- **MPU6050_light** - Lightweight library

## Example Code

### Basic Reading (Adafruit Library)

```cpp
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

Adafruit_MPU6050 mpu;

void setup() {
  Serial.begin(115200);

  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) delay(10);
  }

  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
}

void loop() {
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  Serial.print("Accel X: "); Serial.print(a.acceleration.x);
  Serial.print(" Y: "); Serial.print(a.acceleration.y);
  Serial.print(" Z: "); Serial.println(a.acceleration.z);

  Serial.print("Gyro X: "); Serial.print(g.gyro.x);
  Serial.print(" Y: "); Serial.print(g.gyro.y);
  Serial.print(" Z: "); Serial.println(g.gyro.z);

  Serial.print("Temp: "); Serial.println(temp.temperature);

  delay(100);
}
```

### Raw Register Reading

```cpp
#include <Wire.h>

const int MPU_ADDR = 0x68;

int16_t accelX, accelY, accelZ;
int16_t gyroX, gyroY, gyroZ;
int16_t temp;

void setup() {
  Serial.begin(115200);
  Wire.begin();

  // Wake up MPU6050
  Wire.beginTransmission(MPU_ADDR);
  Wire.write(0x6B);  // PWR_MGMT_1 register
  Wire.write(0);     // Wake up
  Wire.endTransmission(true);
}

void loop() {
  Wire.beginTransmission(MPU_ADDR);
  Wire.write(0x3B);  // Start at ACCEL_XOUT_H
  Wire.endTransmission(false);
  Wire.requestFrom(MPU_ADDR, 14, true);

  accelX = Wire.read() << 8 | Wire.read();
  accelY = Wire.read() << 8 | Wire.read();
  accelZ = Wire.read() << 8 | Wire.read();
  temp = Wire.read() << 8 | Wire.read();
  gyroX = Wire.read() << 8 | Wire.read();
  gyroY = Wire.read() << 8 | Wire.read();
  gyroZ = Wire.read() << 8 | Wire.read();

  Serial.print("aX="); Serial.print(accelX);
  Serial.print(" aY="); Serial.print(accelY);
  Serial.print(" aZ="); Serial.print(accelZ);
  Serial.print(" gX="); Serial.print(gyroX);
  Serial.print(" gY="); Serial.print(gyroY);
  Serial.print(" gZ="); Serial.println(gyroZ);

  delay(100);
}
```

## Applications

- Quadcopter/drone stabilization
- Robot balance control
- Motion tracking
- Gesture recognition
- Tilt sensing
- Vibration monitoring
- Game controllers

## Notes

- Calibration is important for accurate readings
- Gyroscope drift accumulates over time - use sensor fusion
- The DMP can compute quaternions and Euler angles on-chip
- Keep sensor away from motors and other EMI sources
- Mount rigidly to reduce vibration noise
- I2C address can be changed by connecting AD0 pin to VCC (0x69)

## Local Files

*To be downloaded*

- `MPU-6050_Datasheet.pdf` - IMU sensor datasheet
- `MPU-6050_RegisterMap.pdf` - Register documentation
