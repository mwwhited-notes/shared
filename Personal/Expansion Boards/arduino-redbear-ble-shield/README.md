# RedBear BLE Shield v2.1

**Arduino Shield - Bluetooth Low Energy (BLE 4.0)**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | RedBear Lab |
| Board | BLE Shield v2.1 |
| Platform | Arduino |
| Form Factor | Shield |
| Primary Function | Bluetooth Low Energy communication |
| Main IC | Nordic nRF8001 |
| Quantity | 1 |

## Compatibility

| Compatible With | Notes |
|-----------------|-------|
| Arduino UNO | Primary target |
| Arduino Mega 2560 | Compatible |
| Arduino Leonardo | Compatible |
| Arduino Due | Compatible (3.3V native) |
| RedBoard, FRDM-KL05 | Via SPI pin jumpers |

## Specifications

| Specification | Value |
|--------------|-------|
| BLE Chip | Nordic nRF8001 |
| BLE Version | Bluetooth 4.0 Low Energy |
| Role | Peripheral (Slave) only |
| Operating Voltage | 3.3V or 5V |
| Interface | ACI (SPI-like) |
| Antenna | PCB antenna (onboard) |
| External Antenna | Optional SMA (solder pads) |
| Max TX Power | 0 dBm |
| Data Rate | Up to 20 bytes/packet |

## Pin Mapping

| Shield Pin | Arduino Pin | Function | Notes |
|------------|-------------|----------|-------|
| MOSI | D11 / ICSP | SPI Data Out | Selectable via jumper |
| MISO | D12 / ICSP | SPI Data In | Selectable via jumper |
| SCK | D13 / ICSP | SPI Clock | Selectable via jumper |
| REQN | D9 | ACI Request | Directly connected |
| RDYN | D8 | ACI Ready | Directly connected |
| RESET | D4 or D7 | BLE Reset | Jumper selectable |
| VCC | 3.3V/5V | Power | Auto voltage selection |
| GND | GND | Ground | Common ground |

### ACI Interface (SPI-like)

| Signal | Description |
|--------|-------------|
| MOSI | Master Out Slave In |
| MISO | Master In Slave Out |
| SCK | Serial Clock |
| REQN | Request (like CS) |
| RDYN | Ready (interrupt) |

### Pins Used

- **Power:** 3.3V or 5V, GND
- **SPI:** D11, D12, D13 (or ICSP)
- **Control:** D8 (RDYN), D9 (REQN), D4 or D7 (Reset)

### Stacking Compatibility

- [x] Passes through unused pins
- [x] Can stack with: Non-SPI shields
- [x] Conflicts with: Shields using D8, D9, or SPI pins

## Features

- Bluetooth 4.0 Low Energy support
- Works with iOS, Android, and other BLE Central devices
- PCB antenna for compact design
- Optional external SMA antenna support
- Flexible SPI pin configuration (D11-13 or ICSP)
- Selectable REQN/RDYN pins (D2-D10)
- 3.3V and 5V compatible
- Reset button for both Arduino and BLE chip
- Test points for power measurement

## v2.1 Improvements Over v2.0

- SPI pins selectable between D11-13 or ICSP header
- Shorter PCB fits Arduino Yun
- More flexible REQN/RDYN pin selection
- ICSP header passes through for stacking
- SMA antenna option added

## Limitations

- **Peripheral role only** - Cannot act as Central (nRF8001 limitation)
- **Two BLE Shields cannot communicate directly** - Both are peripherals
- **No RSSI reading** - nRF8001 doesn't provide RSSI function
- **20 bytes max per packet** - BLE specification limit

## Documentation

### Board Documentation
- [GitHub Repository](https://github.com/RedBearLab/BLEShield)
- [nRF8001 Library](https://github.com/RedBearLab/nRF8001)

### IC Datasheets
- [Nordic nRF8001 Product Page](https://www.nordicsemi.com/Products/nRF8001)

## Software & Libraries

### RedBear BLE Library
```
# Manual installation from GitHub
git clone https://github.com/RedBearLab/nRF8001.git
# Copy to Arduino/libraries folder
```

### Nordic BLE SDK for Arduino
- [Nordic BLE SDK](https://github.com/NordicSemiconductor/ble-sdk-arduino)

## Example Code

```cpp
#include <SPI.h>
#include <boards.h>
#include <ble_shield.h>

void setup() {
  Serial.begin(57600);

  // Initialize BLE Shield
  ble_begin();

  Serial.println("BLE Shield Ready");
}

void loop() {
  // Check for incoming BLE data
  while (ble_available()) {
    Serial.write(ble_read());
  }

  // Send data from Serial to BLE
  while (Serial.available()) {
    ble_write(Serial.read());
  }

  // Process BLE events
  ble_do_events();
}
```

## Mobile Apps

- **BLE Controller** - RedBear iOS/Android app for testing
- **nRF Connect** - Nordic's BLE debugging app
- **LightBlue** - iOS BLE explorer

## Notes

- RedBear Lab was acquired; support may be limited
- Library may require updates for newer Arduino IDE versions
- The nRF8001 is an older BLE chip; consider newer options for new designs
- BLE Shield uses simple TX/RX service profile by default
- Custom GATT profiles require modifying nRFgo Studio configuration

## Local Files

### Pending (Manual Download Required)
- `nRF8001_ProductSpecification.pdf` - see [MISSING_DOCUMENTATION.md](../MISSING_DOCUMENTATION.md)
