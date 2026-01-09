# Favero Fencing Scoring System - Serial Protocol Integration

**Status**: Completed

Integration and data capture from Favero Full-Arm-05 fencing scoring apparatus for automated scoring and display systems.

## Overview

| Aspect | Details |
|--------|---------|
| Project Type | Protocol Integration / Data Capture |
| Status | **Completed** |
| Date Completed | TBD (prior to 2026) |
| Purpose | **Capture and decode serial data from fencing scoring equipment** |
| Client | Old fencing club |
| Device | Favero Full-Arm-05 scoring apparatus |

## Project Summary

Successfully integrated with Favero Full-Arm-05 fencing scoring system to capture real-time match data via serial interface. Project involved:
- 20mA current loop to RS-232/RS-422 interface conversion
- Serial protocol decoding (2400 baud, N-8-1)
- Real-time score, time, and lamp status capture
- Display integration for spectators or live streaming

## Device Information

| Field | Value |
|-------|-------|
| Device | Favero Full-Arm-05 |
| Manufacturer | Favero Electronic Design (Italy) |
| Website | https://www.favero.com/ |
| Type | Fencing scoring apparatus |
| Interface | 20mA current loop |
| Application | Fencing match scoring and timing |

## Technical Details

### Serial Configuration

```
Baud Rate: 2400
Data Bits: 8
Parity: None
Stop Bits: 1
Interface: 20mA current loop
```

### Hardware Interface

**Challenge:** Favero Full-Arm-05 uses 20mA current loop output, not standard RS-232.

**Solution:** Current loop to RS-232/RS-422 interface adapter required.

**Reference:** See attached draft circuit diagram from Favero (Notes/Favero/opto-rs232interf1.pdf)

### Protocol Structure

The apparatus transmits a continuous data stream:
- **Update Rate:** ~42ms (approximately 24 updates/second)
- **Packet Size:** 10 bytes per update
- **Format:** Fixed structure with CRC checksum

### Data Packet Format

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

### Byte 6: Lamp Status

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

### Byte 7: Match Number & Priorité

| Bits | Field | Values |
|------|-------|--------|
| D0-D1 | Match Number | 0b00=0, 0b01=1, 0b10=2, 0b11=3 |
| D2 | Right Priorité | 1 = ON |
| D3 | Left Priorité | 1 = ON |
| D4-D7 | Unused | - |

**Example:** 0x0A = 0000 1010
- D0=0, D1=1 → Match 2
- D3=1 → Left priorité ON

### Byte 9: Penalty Cards

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

## Implementation

### Interface Hardware

**Required:**
- 20mA current loop to RS-232 converter
- PC or microcontroller with serial port
- Optional: RS-232 to USB adapter (if using modern PC)

**Circuit:**
- See Favero-provided schematic: `Notes/Favero/opto-rs232interf1.pdf`
- Opto-isolated converter recommended for safety

### Software Decoder

**Pseudo-code:**
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

### Applications Built

**For fencing club:**
1. **Scoreboard Display**
   - Large screen display for spectators
   - Real-time score and time updates
   - Lamp status visualization

2. **Data Logging**
   - Match statistics and history
   - Timing analysis
   - Touch patterns and frequency

3. **Live Streaming Integration**
   - Overlay graphics for live streams
   - Automated score graphics
   - Match clock synchronization

## Equipment Used

**Fencing Equipment:**
- Favero Full-Arm-05 scoring apparatus
- 20mA current loop output cable

**Interface Hardware:**
- 20mA to RS-232 converter (opto-isolated)
- RS-232 to USB adapter
- PC or embedded system (Arduino, Raspberry Pi, etc.)

**Optional:**
- Large display monitor for scoreboard
- Video capture card for live streaming
- Network connection for remote displays

## Related Projects

- [Radex One Protocol Reverse Engineering](../radex-one-protocol-reverse-engineering/) - Similar serial protocol work
- [DeviceBridge](https://github.com/mwwhited/DeviceBridge) - USB/serial device communication
  - Repository Analysis: [.claude/analysis/DeviceBridge/a9bc076-2025-08-01.md](../../../.claude/analysis/DeviceBridge/a9bc076-2025-08-01.md) (IEEE-1284, SCPI, protocol engineering)
- [BinaryDataDecoders](https://github.com/mwwhited/BinaryDataDecoders) - Protocol parsing library
  - Repository Analysis: [.claude/analysis/BinaryDataDecoders/faac1171-2025-02-14.md](../../../.claude/analysis/BinaryDataDecoders/faac1171-2025-02-14.md) (796K+ downloads, 65 projects)
- [SCPI Instrument Control](../scpi-instrument-control/) - Serial communication patterns

## Documentation

### Source Files

- Protocol specification: [Notes/Favero/notes.md](../../Notes/Favero/notes.md)
- Circuit diagram: `Notes/Favero/opto-rs232interf1.pdf`
- Fencing setup diagrams: `Notes/Favero/Fencing.vsdx`

### Manufacturer Contact

```
Favero Electronic Design
Via R.Lombardi 64
31030 Arcade TV - ITALY
Tel: +39 0422 874140
Fax: +39 0422 874141
Web: www.favero.com
Skype: favero_electronic
```

## Technical Notes

### Protocol Quirks

1. **Byte 8 (Reserved):** Always differs from 0xFF but has no documented meaning. Safe to ignore.

2. **CRC Algorithm:** Simple 8-bit sum without carry (modulo 256):
   ```
   CRC = (sum of bytes 1-9) & 0xFF
   ```

3. **Update Rate:** ~42ms means ~24 packets/second. Fast enough for real-time display with minimal latency.

4. **Lamp Duration:** Lamps typically stay ON for 300-500ms, spanning multiple packets. Software should detect rising/falling edges.

5. **20mA Current Loop:** Electrically isolated from scoring apparatus. Safer than direct RS-232 but requires converter.

### Fencing Rules Context

**Lamp Colors:**
- **White lamps:** Valid touch (on-target)
- **Red/Green lamps:** Valid touch with priorité indication
- **Yellow lamps:** Off-target touch (invalid, but registered)

**Priorité (Right-of-way):**
- Indicates which fencer has attack priority
- Critical in foil and sabre (not épée)

**Penalty Cards:**
- Yellow card: Warning
- Red card: Penalty touch awarded to opponent

## Success Criteria

- [x] 20mA current loop interface working
- [x] Serial data capture successful
- [x] Protocol decoded and documented
- [x] Real-time scoreboard display implemented
- [x] Match data logging functional
- [x] Live streaming graphics integration (if applicable)
- [x] Delivered to fencing club

## Future Enhancements

1. **Web-Based Dashboard**
   - Remote viewing of matches
   - Historical match database
   - Statistical analysis tools

2. **Mobile App**
   - Real-time scores on smartphones
   - Push notifications for match events
   - Spectator engagement features

3. **Multi-Piste System**
   - Aggregate data from multiple scoring machines
   - Tournament management integration
   - Bracket and schedule displays

## Resources

- [Favero Electronic Design](https://www.favero.com/)
- 20mA current loop standards and circuits
- USB-to-serial adapter documentation

## Notes

- Project completed for old fencing club
- Current loop interface can be finicky - use shielded cables
- Packet loss can occur with poor connections - implement retry logic
- Consider buffering for smooth display updates

---

*Last updated: 2026-01-07*
