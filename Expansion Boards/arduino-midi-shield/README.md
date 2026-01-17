# Arduino MIDI Shield Breakout Board

**Compatibility:** Arduino UNO R3, Leonardo, Mega 2560
**Function:** MIDI Digital Interface Adapter
**Purchased:** 2020-12-03
**Source:** Amazon (XieQianJin)
**Price:** $12.99

---

## Overview

This MIDI Shield provides a breakout interface for connecting MIDI devices (synthesizers, drum machines, keyboard controllers) to Arduino microcontroller boards via the DIN-5 MIDI protocol.

---

## Specifications

| Parameter | Value |
|-----------|-------|
| **Interface** | 5-pin DIN MIDI connector |
| **Protocol** | MIDI (Musical Instrument Digital Interface) |
| **Baud Rate** | 31,250 bps |
| **Compatible Boards** | Arduino UNO R3, Leonardo, Mega 2560 |
| **Power Supply** | 5V from Arduino |
| **UART Connection** | RX/TX pins |

---

## Pin Mapping

### MIDI Connector (5-pin DIN)

| Pin | Signal | Function |
|-----|--------|----------|
| 1 | Shield | Ground |
| 2 | NC | Not Connected |
| 3 | Ground | MIDI Ground |
| 4 | Receive- | MIDI RX data (inverted) |
| 5 | Receive+ | MIDI RX data (normal) |

### Arduino Pinout

- **RX** - Serial UART RX (pin 0 on UNO, pin 19 on Mega)
- **TX** - Serial UART TX (pin 1 on UNO, pin 18 on Mega)
- **5V** - Power supply
- **GND** - Ground

---

## Primary Applications

- **MIDI Controller Input:** Receiving note data from keyboards, controllers, drum machines
- **Sequencer Interface:** Communication with external sequencers
- **Music Performance:** Real-time MIDI data processing for synthesizer control
- **Embedded Music Systems:** Arduino-based MIDI devices and controllers

---

## Related Equipment

- **MIDI Cables:** Standard 5-pin DIN MIDI cables (not included)
- **MIDI Controllers:** Keyboards, drum machines, control surfaces
- **Testing Equipment:** Logic analyzers (Saleae Logic) for MIDI signal verification

---

## Compatibility Notes

- Works with standard MIDI cables and connectors
- Requires 31,250 baud rate configuration in Arduino code
- Compatible with MIDI library implementations (Arduino MIDI Library, etc.)
- RX-only configuration (receives MIDI data)

---

## Documentation

Official MIDI specification: MIDI 1.0 Protocol (5-pin DIN connector)

---

## Notes

- Purchased as part of mixed MIDI audio project order (Order #113-6684790-7490604)
- Enables Arduino boards to receive MIDI performance and control data
- Complements other MIDI components (MIDI cables, USB MIDI interface)

---

*Last updated: 2026-01-17*
