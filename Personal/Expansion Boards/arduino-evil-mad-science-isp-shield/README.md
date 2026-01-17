# Evil Mad Science ISP Shield 2.0

**Arduino Shield - AVR In-System Programmer**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | Evil Mad Science |
| Board | ISP Shield 2.0 |
| Platform | Arduino |
| Form Factor | Shield |
| Primary Function | AVR ISP Programmer |
| Main IC | None (uses Arduino as programmer) |
| Certification | OSHW (Open Source Hardware) |
| Quantity | 1 |

## Compatibility

| Compatible With | Notes |
|-----------------|-------|
| Arduino UNO | Primary target |
| Arduino Duemilanove | Compatible |
| Arduino Diecimila | Compatible |
| Diavolino | Compatible |

## Specifications

| Specification | Value |
|--------------|-------|
| ZIF Socket | 28-pin DIP |
| Crystal | 16 MHz (for ATmega168/328) |
| Target Power | 5V (jumper selectable) |
| Auto-Reset Override | Yes (jumper selectable) |
| Programming Header | 6-pin AVR ISP |
| Target Chips | ATmega168, ATmega328, other AVRs |

## Pin Mapping

| Shield Pin | Arduino Pin | Function | Notes |
|------------|-------------|----------|-------|
| MOSI | D11 | SPI Data Out | To target MOSI |
| MISO | D12 | SPI Data In | From target MISO |
| SCK | D13 | SPI Clock | To target SCK |
| RESET | D10 | Target Reset | To target RESET |
| LED (Heartbeat) | D9 | Status LED | Programming indicator |
| LED (Error) | D8 | Error LED | Error indicator |
| LED (Programming) | D7 | Activity LED | Activity indicator |

### Pins Used

- **Power:** 5V, GND
- **SPI:** D11 (MOSI), D12 (MISO), D13 (SCK)
- **Control:** D10 (Reset), D7-D9 (LEDs)

### Stacking Compatibility

- [ ] Passes through unused pins - Limited, uses SPI
- [ ] Can stack with: Non-SPI shields only
- [x] Conflicts with: Any shield using SPI or pins 7-13

## Features

- 28-pin ZIF socket for easy chip insertion/removal
- Programs ATmega168/ATmega328 directly in socket
- 6-pin ISP header for external target boards
- Auto-reset override jumper (fixes Arduino compatibility issues)
- Target power jumper (5V to target via ISP)
- Status LEDs for heartbeat, error, and programming activity
- 16 MHz crystal for on-board chip programming
- OSHW certified design

## Jumper Settings

### Auto-Reset Override (J1)
| Setting | Function |
|---------|----------|
| Open | Normal operation (auto-reset enabled) |
| Closed | Auto-reset disabled (required for programming) |

### Target Power (J2)
| Setting | Function |
|---------|----------|
| Open | No power to target via ISP header |
| Closed | 5V supplied to target via ISP header |

## Documentation

### Board Documentation
- [Product Page](https://shop.evilmadscientist.com/productsmenu/253)
- [Wiki Documentation](https://wiki.evilmadscientist.com/ISP_Shield)
- [Usage Guide](https://wiki.evilmadscientist.com/Using_The_ISP_Shield_2)
- [Announcement Blog Post](https://www.evilmadscientist.com/2011/isp-shield-kit-version-2-0/)

## Software & Libraries

### Arduino IDE Setup
The ArduinoISP sketch is built into the Arduino IDE:
1. File > Examples > 11.ArduinoISP > ArduinoISP
2. Upload to Arduino with shield attached
3. Use Tools > Programmer > "Arduino as ISP"

### avrdude Usage
```bash
avrdude -c avrisp -p m328p -P /dev/ttyUSB0 -b 19200 -U flash:w:firmware.hex
```

## Usage Instructions

### Programming Chips in ZIF Socket
1. Load ArduinoISP sketch to Arduino
2. Close auto-reset override jumper
3. Insert target chip in ZIF socket (pin 1 aligned)
4. Select target board in Arduino IDE
5. Select "Arduino as ISP" as programmer
6. Use "Burn Bootloader" or "Upload Using Programmer"

### Programming External Targets
1. Connect 6-pin ISP cable to target board
2. Set target power jumper as needed
3. Follow same programming procedure

## Kit Contents

- ISP Shield 2.0 PCB
- Stacking header set
- 28-pin DIP ZIF socket
- 16 MHz crystal
- 6-pin header (for external targets)
- LEDs (3x)
- Resistors
- Reset button

## Notes

- The ArduinoISP sketch mimics the Atmel AVRISP programmer
- Can program any AVR with ISP interface, not just ATmega
- Close auto-reset jumper BEFORE uploading ArduinoISP sketch, then open it
- v2.0 fixes auto-reset compatibility issues from v1.0
- Works with avrdude programmer type "avrisp"

## Local Files

*No IC datasheets required - this shield uses the Arduino as the programmer.*

For board schematic and design files, see the [Evil Mad Science Wiki](https://wiki.evilmadscientist.com/ISP_Shield).
