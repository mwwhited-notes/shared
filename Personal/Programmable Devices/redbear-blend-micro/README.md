# RedBear Blend Micro

**Arduino-Compatible BLE Development Board**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | RedBear Lab |
| Board | Blend Micro |
| MCU | ATmega32U4 |
| BLE Module | Nordic nRF8001 |
| Date Acquired | |
| Quantity | |

## Specifications

### MCU (ATmega32U4)

| Specification | Value |
|--------------|-------|
| Architecture | AVR 8-bit |
| Clock Speed | 16 MHz |
| Flash | 32 KB (4 KB bootloader) |
| SRAM | 2.5 KB |
| EEPROM | 1 KB |
| Operating Voltage | 3.3V |

### BLE Module (nRF8001)

| Specification | Value |
|--------------|-------|
| Bluetooth | BLE 4.0 |
| TX Power | -18 to +4 dBm |
| Range | ~30m (typical) |
| Profiles | GATT, GAP |
| Interface | SPI + ACI |

## Block Diagram

```plantuml
@startuml
skinparam backgroundColor #FEFEFE
skinparam componentStyle rectangle

package "Blend Micro" {
    [ATmega32U4\n16MHz\n32KB Flash] as MCU
    [nRF8001\nBLE 4.0] as BLE
    [3.3V LDO] as REG
    [Chip Antenna] as ANT
    [USB\nMicro-B] as USB
}

' Internal connections
MCU <--> BLE : SPI + ACI
MCU <--> USB : Native USB
BLE --> ANT
REG --> MCU : 3.3V
REG --> BLE : 3.3V

' External interfaces
package "External Pins" {
    [D0-D17] as DIGITAL
    [A0-A5] as ANALOG
    [I2C\nSDA/SCL] as I2C
    [SPI\nMOSI/MISO/SCK] as SPI
}

MCU --> DIGITAL
MCU --> ANALOG
MCU --> I2C
MCU --> SPI

' Wireless
BLE <.r.> [BLE Central\n(Phone/PC)] : BLE 4.0

@enduml
```

## Pinout

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

map "Blend Micro Pinout" as pinout {
    Digital =>
    D0 => RX (UART)
    D1 => TX (UART)
    D2 => SDA (I2C)
    D3 => SCL (I2C) / PWM
    D4 => GPIO
    D5 => PWM
    D6 => PWM
    D7 => GPIO
    D8 => GPIO
    D9 => PWM
    D10 => PWM
    D11 => GPIO
    D12 => GPIO
    D13 => LED / PWM

    Analog =>
    A0 => ADC
    A1 => ADC
    A2 => ADC
    A3 => ADC
    A4 => ADC
    A5 => ADC

    Power =>
    VIN => 3.5-16V Input
    3V3 => 3.3V Output
    GND => Ground
    RAW => Unregulated Input
}

note right of pinout
  * D2/D3 also used for I2C
  * D13 has onboard LED
  * All pins are 3.3V logic
end note

@enduml
```

## nRF8001 Connection

| nRF8001 | ATmega32U4 | Function |
|---------|-----------|----------|
| MOSI | PB2 | SPI Data In |
| MISO | PB3 | SPI Data Out |
| SCK | PB1 | SPI Clock |
| REQN | PD4 | Request (to nRF8001) |
| RDYN | PD7 | Ready (from nRF8001) |
| RST | - | Connected to MCU reset |

## Features

- Arduino Leonardo compatible
- Bluetooth Low Energy 4.0
- Native USB (HID, Serial, MIDI)
- Chip antenna (no external antenna needed)
- Breadboard compatible
- Small footprint

## Programming

| Method | Tools |
|--------|-------|
| USB (Bootloader) | Arduino IDE |
| ICSP | AVR programmer |

## BLE Development

The nRF8001 uses Nordic's ACI (Application Controller Interface):

```cpp
#include <SPI.h>
#include <BLEPeripheral.h>

BLEPeripheral ble;
BLEService ledService("19B10000-E8F2-537E-4F6C-D104768A1214");
BLECharCharacteristic ledChar("19B10001-E8F2-537E-4F6C-D104768A1214",
                               BLERead | BLEWrite);

void setup() {
    ble.setLocalName("BlendMicro");
    ble.setAdvertisedServiceUuid(ledService.uuid());
    ble.addAttribute(ledService);
    ble.addAttribute(ledChar);
    ble.begin();
}
```

## Documentation

- [Blend Micro Product Page](https://redbear.cc/product/blend-micro.html)
- [ATmega32U4 Datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7766-8-bit-AVR-ATmega16U4-32U4_Datasheet.pdf)
- [nRF8001 Datasheet](https://infocenter.nordicsemi.com/pdf/nRF8001_PS_v1.3.pdf)
- [nRF8001 Product Spec](https://infocenter.nordicsemi.com/index.jsp?topic=%2Fcom.nordic.infocenter.nrf8001.v1.3%2Fnrf8001.html)
- [BLE Peripheral Library](https://github.com/sandeepmistry/arduino-BLEPeripheral)

## Software & Tools

- **Arduino IDE** - Select "Arduino Leonardo"
- **BLEPeripheral Library** - BLE stack for nRF8001
- **nRF Connect** - Mobile app for BLE testing
- [RedBear Library](https://github.com/RedBearLab/nRF8001)

### Arduino IDE Setup

1. Install Arduino IDE
2. Select Board: "Arduino Leonardo"
3. Install BLEPeripheral library via Library Manager
4. Or use RedBear's RBL_nRF8001 library

## Common Uses

- BLE beacons
- Wireless sensors
- Phone-controlled projects
- BLE HID devices
- Fitness/health devices
- Smart home sensors

## Notes

- **3.3V logic** - Not 5V tolerant
- BLE only (not Bluetooth Classic)
- nRF8001 is BLE peripheral only (can't scan/connect to other devices)
- Limited to 6 characteristics per service
- RedBear Lab discontinued - libraries community maintained
- Compatible with iOS, Android, Windows, macOS BLE

## Alternatives

For newer BLE projects:
- **nRF52840 boards** - More capable BLE 5.0
- **ESP32** - WiFi + BLE combo
- **Arduino Nano 33 BLE** - Official Arduino BLE board

## Local Files

*Documentation to be downloaded*
