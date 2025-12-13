# Arduino XBee Shield

**Arduino Shield - XBee Wireless Communication**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | Various (Arduino-compatible) |
| Board | XBee Shield |
| Platform | Arduino |
| Form Factor | Shield |
| Primary Function | XBee wireless module adapter |
| Quantity | 2 |

## Compatibility

| Compatible With | Notes |
|-----------------|-------|
| Arduino UNO | Primary target |
| Arduino Mega | Compatible |
| Arduino Leonardo | Compatible |
| [XBee modules](../../Programmable%20Devices/maxstream-xbee/) | See Programmable Devices |
| [XBee Pro S1](../../Programmable%20Devices/digi-xbee-pro-s1/) | See Programmable Devices |

## Specifications

| Specification | Value |
|--------------|-------|
| XBee Socket | 2mm pitch, 20-pin |
| Voltage Regulator | 3.3V (from 5V Arduino) |
| Level Shifting | Yes (5V to 3.3V) |
| Serial Mode | Hardware UART or Software Serial |
| Frequency | 2.4 GHz (via XBee) |
| Range | 100ft indoor / 300ft outdoor (standard) |

## Pin Mapping

| Shield Pin | Arduino Pin | Function | Notes |
|------------|-------------|----------|-------|
| DIN | D0 (RX) or D2 | XBee Data In | Switch selectable |
| DOUT | D1 (TX) or D3 | XBee Data Out | Switch selectable |
| 3.3V | - | XBee Power | Regulated from 5V |
| GND | GND | Ground | Common ground |
| RESET | RESET | XBee Reset | Connected to Arduino reset |

### Serial Mode Switch

| Position | RX | TX | Notes |
|----------|----|----|-------|
| UART | D0 | D1 | Hardware serial (can't upload while XBee inserted) |
| DLINE | D2 | D3 | Software serial (allows uploading) |

### Pins Used

- **Power:** 3.3V (regulated), 5V, GND
- **Communication:** D0/D1 (UART) or D2/D3 (Software Serial)

### Stacking Compatibility

- [x] Passes through most unused pins
- [x] Can stack with: Shields not using serial pins
- [x] Conflicts with: Other shields using D0/D1 or D2/D3 (depending on switch)

## Features

- Socket for XBee and XBee Pro modules (Series 1 and 2)
- On-board 3.3V regulator for XBee power
- 5V to 3.3V level shifting on data lines
- UART/Software Serial switch for flexibility
- Status LEDs (Power, RSSI, DIN, DOUT)
- Pass-through headers for other shields
- Reset button

## XBee Module Compatibility

| Module Type | Compatible |
|-------------|------------|
| XBee Series 1 | Yes |
| XBee Series 2/2.5 | Yes |
| XBee Pro | Yes |
| XBee 3 | Yes (check footprint) |

## Documentation

### Board Documentation
- [Arduino XBee Shield Page](https://www.arduino.cc/en/Main/ArduinoXbeeShield)
- [SparkFun XBee Shield Guide](https://learn.sparkfun.com/tutorials/xbee-shield-hookup-guide)
- [XBee Shield Schematic](https://www.arduino.cc/en/uploads/Main/XbeeShieldSchematic.pdf)

### XBee Documentation
- See `../Programmable Devices/maxstream-xbee/` for XBee module docs
- See `../Programmable Devices/digi-xbee-pro-s1/` for XBee Pro docs

## Software & Libraries

### Software Serial (Recommended)
```cpp
#include <SoftwareSerial.h>
SoftwareSerial xbee(2, 3); // RX, TX
```

### XCTU Configuration Tool
- [XCTU Download](https://www.digi.com/products/embedded-systems/digi-xbee/digi-xbee-tools/xctu)

## Example Code

```cpp
#include <SoftwareSerial.h>

// XBee shield in DLINE mode (D2=RX, D3=TX)
SoftwareSerial xbee(2, 3);

void setup() {
  Serial.begin(9600);      // USB serial for debugging
  xbee.begin(9600);        // XBee default baud rate
  Serial.println("XBee Ready");
}

void loop() {
  // Forward XBee data to Serial Monitor
  if (xbee.available()) {
    Serial.write(xbee.read());
  }

  // Forward Serial Monitor input to XBee
  if (Serial.available()) {
    xbee.write(Serial.read());
  }
}
```

## Notes

- Remove XBee module before uploading sketches when using UART mode
- Use DLINE (software serial) mode to allow uploads with XBee installed
- XBee modules require configuration via XCTU before use
- Default XBee baud rate is 9600
- Ensure proper antenna orientation for best range
- See Test Equipment for XBIB-U-DEV programming board

## Local Files

*To be downloaded*

- `XBee_Shield_Schematic.pdf` - Board schematic
