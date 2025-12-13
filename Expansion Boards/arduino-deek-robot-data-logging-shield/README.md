# Deek-Robot Data Logging Shield V1.0

**Arduino Shield - SD Card and RTC Data Logger**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | Deek-Robot |
| Board | Data Logging Shield V1.0 |
| Platform | Arduino |
| Form Factor | Shield |
| Primary Function | SD card logging with RTC |
| Main ICs | DS1307 (RTC), SD card slot |
| Quantity | 3 |

## Compatibility

| Compatible With | Notes |
|-----------------|-------|
| Arduino UNO | Primary target |
| Arduino Duemilanove | Compatible |
| Arduino Mega | Compatible (different SPI pins) |
| Arduino Leonardo | Compatible |

## Specifications

| Specification | Value |
|--------------|-------|
| RTC Chip | DS1307 |
| RTC I2C Address | 0x68 |
| RTC Battery | CR1220 (3V coin cell) |
| SD Card Slot | Standard SD / microSD (adapter) |
| SD Interface | SPI |
| SD Card Format | FAT16/FAT32 |
| Prototyping Area | Yes |

## Pin Mapping

| Shield Function | Arduino Pin | Notes |
|-----------------|-------------|-------|
| SD Card CS | D10 | Directly connected |
| SD Card MOSI | D11 | SPI |
| SD Card MISO | D12 | SPI |
| SD Card SCK | D13 | SPI |
| RTC SDA | A4 | I2C |
| RTC SCL | A5 | I2C |

### On Mega 2560

| Shield Function | Mega Pin | Notes |
|-----------------|----------|-------|
| SD Card CS | D10 or D53 | Check shield version |
| SD Card MOSI | D51 | SPI (via ICSP) |
| SD Card MISO | D50 | SPI (via ICSP) |
| SD Card SCK | D52 | SPI (via ICSP) |
| RTC SDA | D20 | I2C |
| RTC SCL | D21 | I2C |

### Pins Used

- **Power:** 5V, 3.3V, GND
- **SPI:** D10 (CS), D11 (MOSI), D12 (MISO), D13 (SCK)
- **I2C:** A4 (SDA), A5 (SCL)

### Stacking Compatibility

- [x] Passes through most unused pins
- [ ] Can stack with: Non-SPI shields, or shields with different CS
- [x] Conflicts with: Other SPI shields using D10 as CS

## Features

- SD card slot for data storage
- DS1307 RTC for timestamping
- Battery backup for RTC
- Prototyping area for custom circuits
- Standard SPI interface for SD card
- I2C interface for RTC
- Compatible with Arduino SD library

## SD Card Information

| Specification | Value |
|---------------|-------|
| Card Types | SD, SDHC (up to 32GB typical) |
| File System | FAT16, FAT32 |
| Max File Size | 4GB (FAT32 limit) |
| SPI Speed | Up to ~8 MHz |

### SD Card Formatting

- Format as FAT32 for cards > 2GB
- Use SD Card Association formatter for best results
- 8.3 filename format recommended for compatibility

## Documentation

### Reference Documentation
- [Arduino SD Library Reference](https://www.arduino.cc/reference/en/libraries/sd/)
- [DS1307 Datasheet](https://datasheets.maximintegrated.com/en/ds/DS1307.pdf)

## Software & Libraries

### SD Card Library (Built-in)
```cpp
#include <SD.h>
#include <SPI.h>
```

### RTC Library
```
# Arduino Library Manager
Search for: "RTClib" by Adafruit
```

## Example Code

### Basic Data Logging

```cpp
#include <SD.h>
#include <SPI.h>
#include <Wire.h>
#include <RTClib.h>

#define SD_CS 10

RTC_DS1307 rtc;
File logFile;

void setup() {
  Serial.begin(9600);

  // Initialize RTC
  if (!rtc.begin()) {
    Serial.println("Couldn't find RTC");
    while (1);
  }

  if (!rtc.isrunning()) {
    Serial.println("RTC is NOT running, setting time...");
    rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
  }

  // Initialize SD card
  if (!SD.begin(SD_CS)) {
    Serial.println("SD card initialization failed!");
    while (1);
  }
  Serial.println("SD card initialized.");
}

void loop() {
  DateTime now = rtc.now();

  // Create filename based on date
  String filename = String(now.month()) + String(now.day()) + ".csv";

  // Open file for writing
  logFile = SD.open(filename, FILE_WRITE);

  if (logFile) {
    // Log timestamp and sensor value
    logFile.print(now.year());
    logFile.print("-");
    logFile.print(now.month());
    logFile.print("-");
    logFile.print(now.day());
    logFile.print(" ");
    logFile.print(now.hour());
    logFile.print(":");
    logFile.print(now.minute());
    logFile.print(":");
    logFile.print(now.second());
    logFile.print(",");

    // Log analog reading
    int sensorValue = analogRead(A0);
    logFile.println(sensorValue);

    logFile.close();

    Serial.print("Logged: ");
    Serial.println(sensorValue);
  } else {
    Serial.println("Error opening file");
  }

  delay(1000);  // Log every second
}
```

### Set RTC Time

```cpp
#include <Wire.h>
#include <RTClib.h>

RTC_DS1307 rtc;

void setup() {
  Serial.begin(9600);
  rtc.begin();

  // Set to compile time (run once, then comment out)
  rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));

  // Or set manually:
  // rtc.adjust(DateTime(2024, 12, 15, 14, 30, 0));

  Serial.println("RTC time set!");
}

void loop() {
  DateTime now = rtc.now();
  Serial.print(now.year());
  Serial.print('/');
  Serial.print(now.month());
  Serial.print('/');
  Serial.print(now.day());
  Serial.print(' ');
  Serial.print(now.hour());
  Serial.print(':');
  Serial.print(now.minute());
  Serial.print(':');
  Serial.println(now.second());

  delay(1000);
}
```

## Notes

- Insert battery with correct polarity before first use
- RTC keeps time even when Arduino is off (battery backup)
- Use short filenames (8.3 format) for best compatibility
- SD card must be formatted FAT16/FAT32
- Remove SD card before uploading new sketches if using D10
- The Deek-Robot version is a clone of the Adafruit Data Logger Shield
- Prototyping area useful for adding sensors

## Local Files

### Pending (Manual Download Required)
- `DS1307_Datasheet.pdf` - see [MISSING_DOCUMENTATION.md](../MISSING_DOCUMENTATION.md)
