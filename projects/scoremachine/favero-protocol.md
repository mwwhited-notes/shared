# Favero Fencing Scoring System - Serial Protocol Specification

**Protocol Version:** Full-Arm-05
**Last Updated:** 2026-01-12

---

## Overview

This document specifies the RS-485 serial protocol used by Favero Full-Arm-05 fencing scoring apparatus. This protocol is used by the ScoreMachine project (both Phase 1 and Phase 2) to capture real-time match data for scoring displays and live streaming overlays.

**Protocol Implementation:**
- **BinaryDataDecoders:** [Favero protocol parser](https://github.com/mwwhited/BinaryDataDecoders) (796K+ NuGet downloads)
- **Production System:** [FencingScoreBoard](https://github.com/mwwhited/FencingScoreBoard) - ASP.NET Core + SignalR service

---

## Device Information

| Field | Value |
|-------|-------|
| Device | Favero Full-Arm-05 |
| Manufacturer | Favero Electronic Design (Italy) |
| Website | https://www.favero.com/ |
| Type | Fencing scoring apparatus |
| Interface | 20mA current loop |
| Application | Fencing match scoring and timing |

**Manufacturer Contact:**
```
Favero Electronic Design
Via R.Lombardi 64
31030 Arcade TV - ITALY
Tel: +39 0422 874140
Fax: +39 0422 874141
Web: www.favero.com
Skype: favero_electronic
```

---

## Serial Configuration

```
Baud Rate: 2400
Data Bits: 8
Parity: None
Stop Bits: 1
Interface: 20mA current loop
```

**Hardware Interface:**

The Favero Full-Arm-05 uses a **20mA current loop** output, not standard RS-232. A current loop to RS-232/RS-485 converter is required.

**Circuit Reference:** See [reference/favero/opto-rs232interf1.pdf](reference/favero/opto-rs232interf1.pdf) for Favero-provided schematic.

**Recommended:** Opto-isolated converter for electrical safety.

---

## Protocol Structure

The apparatus transmits a continuous data stream:
- **Update Rate:** ~42ms (approximately 24 updates/second)
- **Packet Size:** 10 bytes per update
- **Format:** Fixed structure with CRC checksum
- **Start Marker:** 0xFF (byte 1)

---

## Data Packet Format

| Byte | Field | Description | Example |
|------|-------|-------------|---------|
| 1 | Start | Packet start marker (0xFF) | 0xFF |
| 2 | Right Score | Right fencer score (0x00-0x0F) | 0x06 = 6 points |
| 3 | Left Score | Left fencer score (0x00-0x0F) | 0x12 = 12 points |
| 4 | Seconds | Time seconds (0x00-0x59) | 0x56 = 56 seconds |
| 5 | Minutes | Time minutes, units only (0x00-0x09) | 0x02 = 2 minutes |
| 6 | Lamp Status | Lamp state bitfield (8 bits) | See below |
| 7 | Match/Priorité | Match number and priorité flags | See below |
| 8 | Reserved | Internal use (not 0xFF) | Varies |
| 9 | Penalty Cards | Red/yellow card bitfield | See below |
| 10 | CRC | Sum of bytes 1-9 (no carry) | Checksum |

---

## Byte 6: Lamp Status

Bitfield showing which lamps are ON (1) or OFF (0):

| Bit | Lamp | Color | Side |
|-----|------|-------|------|
| D0 | Left white | White | Left |
| D1 | Right white | White | Right |
| D2 | Red | Red | Left |
| D3 | Green | Green | Right |
| D4 | Right yellow | Yellow | Right |
| D5 | Left yellow | Yellow | Left |
| D6-D7 | Unused | - | - |

**Example:** 0x14 = 0001 0100
- Bit D2 = 1 (Red lamp ON - left touch)
- Bit D4 = 1 (Right yellow lamp ON - off-target right)

**Fencing Context:**
- **White lamps:** Valid touch (on-target)
- **Red/Green lamps:** Valid touch with priorité indication
- **Yellow lamps:** Off-target touch (invalid, but registered)

---

## Byte 7: Match Number & Priorité

| Bits | Field | Values |
|------|-------|--------|
| D0-D1 | Match Number | 0b00=0, 0b01=1, 0b10=2, 0b11=3 |
| D2 | Right Priorité | 1 = ON |
| D3 | Left Priorité | 1 = ON |
| D4-D7 | Unused | - |

**Example:** 0x0A = 0000 1010
- D0=0, D1=1 → Match 2
- D3=1 → Left priorité ON

**Priorité (Right-of-way):**
- Indicates which fencer has attack priority
- Critical in foil and sabre (not épée)

---

## Byte 9: Penalty Cards

| Bit | Card | Side |
|-----|------|------|
| D0 | Red card | Right |
| D1 | Red card | Left |
| D2 | Yellow card | Right |
| D3 | Yellow card | Left |
| D4-D5 | Variable | (ignore) |
| D6-D7 | Always 0 | - |

**Example:** 0x38 = 0011 1000
- D3=1 → Left yellow card

**Penalty Context:**
- **Yellow card:** Warning
- **Red card:** Penalty touch awarded to opponent

---

## Example Data Stream

### Complete Packet

```
Bytes: FF 06 12 56 02 14 0A 00 38 56

Decoded:
- Start: 0xFF
- Right Score: 6
- Left Score: 12
- Time: 2:56
- Lamps: Red (left), Yellow right (off-target)
- Match: 2
- Priorité: Left
- Penalty: Left yellow card
- CRC: 0x56 (sum of bytes 1-9)
```

**Original Example from Manufacturer:**
```
FFh, 06h, 12h, 56h, 02h, 14h, 0Ah, 00h, 38h, 56h

Which displays:
- Right score = 6
- Left score = 12
- Time = 2:56
- Lamps ON: Red, Yellow right, Left priorité
- Number of Matches = 2
- Left yellow penalty lamp = ON
```

Source: [reference/favero/notes.md](reference/favero/notes.md) (email from Gino Favero, manufacturer)

---

## Technical Notes

### CRC Algorithm

Simple 8-bit sum without carry (modulo 256):

```
CRC = (sum of bytes 1-9) & 0xFF
```

### Protocol Quirks

1. **Byte 8 (Reserved):** Always differs from 0xFF but has no documented meaning. Safe to ignore per manufacturer documentation.

2. **Update Rate:** ~42ms means ~24 packets/second. Fast enough for real-time display with minimal latency.

3. **Lamp Duration:** Lamps typically stay ON for 300-500ms, spanning multiple packets. Software should detect rising/falling edges for accurate touch detection.

4. **20mA Current Loop:** Electrically isolated from scoring apparatus. Safer than direct RS-232 but requires converter circuit.

5. **Time Format:** Byte 5 contains ONLY units of minutes (0-9), not tens. Maximum time display is 9:59.

---

## Implementation Reference

### Software Decoder (Pseudo-code)

```python
import serial

def decode_favero_packet(packet):
    if len(packet) != 10 or packet[0] != 0xFF:
        return None

    # Verify CRC
    crc = sum(packet[:9]) & 0xFF
    if crc != packet[9]:
        return None

    return {
        'right_score': packet[1],
        'left_score': packet[2],
        'time': f"{packet[4]}:{packet[3]:02d}",
        'lamps': {
            'left_white': bool(packet[5] & 0x01),
            'right_white': bool(packet[5] & 0x02),
            'red': bool(packet[5] & 0x04),
            'green': bool(packet[5] & 0x08),
            'right_yellow': bool(packet[5] & 0x10),
            'left_yellow': bool(packet[5] & 0x20),
        },
        'match_number': packet[6] & 0x03,
        'priorite': {
            'right': bool(packet[6] & 0x04),
            'left': bool(packet[6] & 0x08),
        },
        'penalties': {
            'right_red': bool(packet[8] & 0x01),
            'left_red': bool(packet[8] & 0x02),
            'right_yellow': bool(packet[8] & 0x04),
            'left_yellow': bool(packet[8] & 0x08),
        }
    }

# Main loop
ser = serial.Serial('/dev/ttyUSB0', 2400, timeout=1)
while True:
    packet = ser.read(10)
    data = decode_favero_packet(packet)
    if data:
        print(f"Score: {data['left_score']}-{data['right_score']}")
        print(f"Time: {data['time']}")
```

### Production Implementation

**BinaryDataDecoders Library:**
- NuGet Package: [BinaryDataDecoders.ElectronicScoringMachines.Fencing](https://www.nuget.org/packages/BinaryDataDecoders.ElectronicScoringMachines.Fencing/)
- Repository: [BinaryDataDecoders/Favero](https://github.com/mwwhited/BinaryDataDecoders/tree/master/src/BinaryDataDecoders.ElectronicScoringMachines.Fencing/Favero)
- Downloads: 796K+ (as of 2026)

**FencingScoreBoard Service:**
- Uses System.IO.Pipelines for high-performance async stream parsing
- SignalR for real-time push to overlay clients
- Supports both Favero and Saint George protocols

---

## ScoreMachine Integration

### Phase 1: Raspberry Pi + NeTV (2017-2019)

**Hardware:**
- Ebyte E810-DTU serial-to-TCP/IP converter
- Network connection to .NET service on Raspberry Pi
- See [phase1-raspberry-pi-netv.md](phase1-raspberry-pi-netv.md) for complete setup

**Configuration:**
```bash
# E810-DTU #1: Favero Scoring Machine
IP: 10.0.88.11
Port: 4001
Protocol: RS-485
Baud: 2400-N-8-1
```

### Phase 2: Windows + OBS (2019-Present)

**Hardware:**
- Direct RS-485-to-USB adapter
- Windows 10+ PC
- See [phase2-windows-obs.md](phase2-windows-obs.md) for complete setup

**Configuration:**
```bash
# Typical USB serial device
Device: /dev/ttyUSB0 (Linux) or COM3 (Windows)
Baud: 2400-N-8-1
```

**Environment Variables (Phase 1 Raspberry Pi):**

See [reference/favero/linux-serial-setup.md](reference/favero/linux-serial-setup.md) for USB device auto-detection scripts.

---

## Equipment Required

### Fencing Equipment
- Favero Full-Arm-05 scoring apparatus
- 20mA current loop output cable

### Interface Hardware

**Phase 1 (Distributed):**
- 20mA to RS-485 converter (opto-isolated)
- Ebyte E810-DTU serial-to-TCP/IP converter
- Ethernet network infrastructure
- Raspberry Pi 2 (ARM host)

**Phase 2 (Simplified):**
- 20mA to RS-485 converter (opto-isolated)
- RS-485 to USB adapter
- Windows 10+ PC

---

## Reference Files

| File | Description | Location |
|:-----|:------------|:---------|
| **Protocol Email** | Original specification from Gino Favero (manufacturer) | [reference/favero/notes.md](reference/favero/notes.md) |
| **Circuit Diagram** | 20mA to RS-232 opto-isolated converter schematic | [reference/favero/opto-rs232interf1.pdf](reference/favero/opto-rs232interf1.pdf) |
| **Linux Setup** | Raspberry Pi USB serial detection and environment variables | [reference/favero/linux-serial-setup.md](reference/favero/linux-serial-setup.md) |
| **System Diagrams** | Visio diagrams of fencing equipment setup | [reference/favero/Fencing.vsdx](reference/favero/Fencing.vsdx) |
| **Data Analysis** | Excel workbook (protocol capture/analysis) | [reference/favero/Book11.xlsx](reference/favero/Book11.xlsx) |

---

## Related Protocols

### Saint George Protocol

The ScoreMachine project also supports Saint George scoring machines (UK manufacturer):

- **BinaryDataDecoders:** [Saint George protocol parser](https://github.com/mwwhited/BinaryDataDecoders/tree/master/src/BinaryDataDecoders.ElectronicScoringMachines.Fencing/SaintGeorge)
- **Protocol:** Similar RS-485 serial, different packet structure
- **Compatibility:** Both protocols supported in FencingScoreBoard service

---

## Troubleshooting

### Common Issues

**1. No Data Received:**
- Verify 20mA to RS-485 converter wiring (see circuit diagram)
- Check serial port configuration (2400-N-8-1)
- Confirm scoring machine is powered and operational
- Test with oscilloscope on converter output (expect ~2.5V idle, transitions 0-5V)

**2. CRC Errors:**
- Check for electrical noise (use shielded cables)
- Verify ground connections on converters
- Increase serial read buffer size
- Consider opto-isolation if not already present

**3. Packet Loss:**
- Monitor serial port buffer overruns
- Ensure software can process 24 packets/second minimum
- Check CPU load on receiving system
- Consider increasing serial port buffer size in OS

**4. Incorrect Decoding:**
- Verify byte order (MSB/LSB)
- Check for off-by-one errors in byte indexing
- Compare with manufacturer example packet
- Use BinaryDataDecoders library (tested in production)

---

## Resources

- **Manufacturer:** [Favero Electronic Design](https://www.favero.com/)
- **Production Code:** [FencingScoreBoard](https://github.com/mwwhited/FencingScoreBoard)
- **Protocol Library:** [BinaryDataDecoders](https://github.com/mwwhited/BinaryDataDecoders)
- **ScoreMachine Documentation:** [README.md](README.md)
- **Phase 1 Setup:** [phase1-raspberry-pi-netv.md](phase1-raspberry-pi-netv.md)
- **Phase 2 Setup:** [phase2-windows-obs.md](phase2-windows-obs.md)

---

*Protocol specification based on manufacturer documentation from Gino Favero, Favero Electronic Design*
*Implemented in production at Arnold Fencing Classic (2018-2020) and Royal Arts Fencing Academy (2020-present)*
*Last updated: 2026-01-12*
