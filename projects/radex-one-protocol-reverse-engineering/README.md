# Radex One Geiger Counter - USB Serial Protocol Reverse Engineering

**Status**: Completed

Reverse engineering the USB serial protocol for the [Radex One](https://quartarad.com/product/radex-one/) geiger counter from Quarta.

## Overview

| Aspect | Details |
|--------|---------|
| Project Type | Reverse Engineering / Protocol Analysis |
| Status | **Completed** |
| Date Completed | TBD (prior to 2026) |
| Purpose | **Decode USB serial protocol for programmatic access to geiger counter data** |
| Device | Radex One portable geiger counter (Quarta) |

## Project Summary

Successfully reverse-engineered the complete USB serial protocol for the Radex One geiger counter, documenting:
- Serial communication parameters (2400-N-8-1)
- Complete packet structure (request/response format)
- Checksum algorithm
- Data reading (ambient, accumulated, CPM)
- Settings management (alarm, threshold)
- Device identification (serial number, version)

## Device Information

| Field | Value |
|-------|-------|
| Device | Radex One |
| Manufacturer | Quarta (https://quartarad.com/) |
| Type | Portable USB geiger counter |
| Interface | USB Serial (virtual COM port) |
| Serial Parameters | 2400 baud, N-8-1 |

## Protocol Details

### Serial Configuration

```
Baud Rate: 2400
Data Bits: 8
Parity: None
Stop Bits: 1
```

### Packet Structure

#### Outbound (PC → Device)

```
Prefix: [0x7b, 0xff]
Request Type: [0x20, 0x00]
Extension Length: [0xLL, 0xHH]
Packet Number: [0xLL, 0xHH]
Zero Reserved: [0x00, 0x00]
CheckSum: FFFF - Sum(Prefix...ZeroReserve) % FFFF
Extensions: (variable, based on Extension Length)
```

#### Inbound (Device → PC)

```
Prefix: [0x7a, 0xff]
Response Type: [0x20, 0x80]
Extension Length: [0xLL, 0xHH]
Packet Number: [0xLL, 0xHH]
Zero Reserved: [0x00, 0x00]
CheckSum: FFFF - Sum(Prefix...ZeroReserve) % FFFF
Extensions: (variable, based on Extension Length)
```

### Command Types

#### 1. Read Data (0x00, 0x08)

**Request:**
```
Request Type: [0x00, 0x08]
Reserved: [0x0c, 0x00]
CheckSum: [calculated]
```

**Response:**
```
Response Type: [0x00, 0x08]
Reserved: [0x00, 0x00]
Reserved: [0x0c, 0x00]
Reserved: [0x00, 0x00]
Ambient: [0xLL, 0xHH]
Reserved: [0x00, 0x00]
Accumulated: [0xLL, 0xHH]
Reserved: [0x00, 0x00]
CPM: [0xLL, 0xHH]
Reserved: [0x00, 0x00]
CheckSum: [calculated]
```

**Example:**
```
>: 7BFF 2000 0600 1800 ____ 4600 0008 0C00 F3F7
<: 7AFF 2080 1600 1800 ____ 3680 0008 ____ 0C00 ____ 1200 ____ 1200 ____ 1500 ____ BAF7
```

#### 2. Read Serial Number/Version (0x01, 0x00)

**Request:**
```
Request Type: [0x01, 0x00]
Reserved: [0x0c, 0x00]
CheckSum: [calculated]
```

**Response:**
```
Response Type: [0x01, 0x00]
Reserved: [0x0c, 0x00]
Serial Number/Version Data: (variable length)
CheckSum: [calculated]
```

**Example:**
```
>: 7BFF 2000 0600 9B0D ____ C2F2 0100 0C00 F2FF
<: 7AFF 2080 1E00 9B0D ____ AB72 0100 ____ 1400 ____ 11A4 ____ 9820 ____ 1400 0612 0108 4803 0800 ____ D61D

Decoded: SN: 180620-0840-008344 v1.8
```

#### 3. Write Settings (0x02, 0x08)

**Request:**
```
Request Type: [0x02, 0x08]
Reserved: [0x0e, 0x00]
Target Value: [0x05, 0x00]
Zero Reserved: [0x00, 0x00]
Alarm Setting: [0x03]  // 0x01 = Vibration, 0x02 = Audio
Threshold: [0xLL, 0xHH]
Zero Reserved: [0x00, 0x00, 0x00]
CheckSum: [calculated]
```

**Response:**
```
Response Type: [0x02, 0x08]
Zero Reserved: [0x00, 0x00]
CheckSum: [calculated]
```

**Example:**
```
>: 7BFF 2000 1000 FA05 ____ 59FA 0208 0E00 0500 ____ 020A ____ ____ E8ED
<: 7AFF 2080 0600 FA05 ____ 647A 0208 ____ FDF7
```

**Note:** Write request must be repeated 3 times for confirmation.

#### 4. Read Settings (0x01, 0x08)

**Request:**
```
Request Type: [0x01, 0x08]
Reserved: [0x0c, 0x00]
CheckSum: [calculated]
```

**Response:**
```
Response Type: [0x01, 0x08]
Zero Reserved: [0x00, 0x00]
Target Value: [0x05, 0x00]
Zero Reserved: [0x00, 0x00]
Alarm Setting: [0x03]
Threshold: [0xLL, 0xHH]
Zero Reserved: [0x00, 0x00, 0x00]
CheckSum: [calculated]
```

**Example:**
```
>: 7BFF 2000 0600 FD05 ____ 60FA 0108 0C00 F2F7
<: 7AFF 2080 1000 FD05 ____ 577A 0108 ____ 0500 ____ 020A ____ ____ F7ED
```

### Checksum Algorithm

```
CheckSum = 0xFFFF - (Sum of all bytes from Prefix to ZeroReserve) % 0xFFFF
```

Little-endian byte order (LSB first).

## Data Fields

### Radiation Measurements

| Field | Description | Units |
|-------|-------------|-------|
| **Ambient** | Current ambient radiation level | μSv/h |
| **Accumulated** | Accumulated dose | μSv |
| **CPM** | Counts per minute | counts/min |

### Alarm Settings

| Alarm Type | Value | Description |
|------------|-------|-------------|
| Vibration | 0x01 | Vibration alarm enabled |
| Audio | 0x02 | Audio alarm enabled |
| Both | 0x03 | Both alarms enabled |

### Threshold

Alarm threshold value for radiation level trigger (little-endian 16-bit).

## Applications

### Potential Use Cases

1. **Data Logging**
   - Automated radiation monitoring
   - Long-term exposure tracking
   - Environmental radiation mapping

2. **Integration**
   - Home automation systems (Home Assistant, etc.)
   - Scientific data collection
   - Real-time web dashboards

3. **Remote Monitoring**
   - Network-connected radiation monitoring
   - Alert systems for high radiation
   - Multi-sensor deployments

## Implementation Notes

### Serial Port Access

**Linux:**
```bash
# Device typically appears as /dev/ttyUSB0 or /dev/ttyACM0
ls -l /dev/tty* | grep USB
```

**Windows:**
```
# Check Device Manager for COM port assignment
# Usually COM3 or higher
```

### Example Code Snippets

#### Python - Read Data

```python
import serial

def read_radiation_data(port='/dev/ttyUSB0'):
    ser = serial.Serial(port, baudrate=2400, bytesize=8, parity='N', stopbits=1)

    # Request data packet
    request = bytearray([0x7b, 0xff, 0x20, 0x00, 0x06, 0x00, 0x18, 0x00,
                         0x00, 0x00, 0x46, 0x00, 0x00, 0x08, 0x0c, 0x00, 0xf3, 0xf7])

    ser.write(request)
    response = ser.read(26)  # Read 26 byte response

    # Parse ambient, accumulated, CPM from response
    ambient = int.from_bytes(response[12:14], byteorder='little')
    accumulated = int.from_bytes(response[16:18], byteorder='little')
    cpm = int.from_bytes(response[20:22], byteorder='little')

    return {
        'ambient': ambient,
        'accumulated': accumulated,
        'cpm': cpm
    }
```

#### C# - Read Settings

```csharp
using System.IO.Ports;

SerialPort port = new SerialPort("COM3", 2400, Parity.None, 8, StopBits.One);
port.Open();

byte[] request = new byte[] {
    0x7B, 0xFF, 0x20, 0x00, 0x06, 0x00, 0xFD, 0x05,
    0x00, 0x00, 0x60, 0xFA, 0x01, 0x08, 0x0C, 0x00, 0xF2, 0xF7
};

port.Write(request, 0, request.Length);
byte[] response = new byte[22];
port.Read(response, 0, 22);

// Parse alarm settings and threshold
byte alarmType = response[14];
ushort threshold = BitConverter.ToUInt16(response, 15);
```

## Related Projects

- [DeviceBridge](https://github.com/mwwhited/DeviceBridge) - USB device communication framework (could be used for Radex One integration)
  - Repository Analysis: [.claude/analysis/DeviceBridge/a9bc076-2025-08-01.md](../../../.claude/analysis/DeviceBridge/a9bc076-2025-08-01.md) (IEEE-1284, SCPI, protocol engineering)
- [BinaryDataDecoders](https://github.com/mwwhited/BinaryDataDecoders) - .NET encoding/decoding library (protocol parsing)
  - Repository Analysis: [.claude/analysis/BinaryDataDecoders/faac1171-2025-02-14.md](../../../.claude/analysis/BinaryDataDecoders/faac1171-2025-02-14.md) (796K+ downloads, 65 projects)
- [Home Automation](../home-automation/) - Could integrate radiation monitoring
- [Favero Fencing System](../favero-fencing-scoring-system/) - Similar serial protocol reverse-engineering work

## Equipment Used

**Device:**
- Radex One USB Geiger Counter (Quarta)

**Tools:**
- USB serial capture/analysis tool
- Serial terminal (PuTTY, screen, minicom, etc.)
- Logic analyzer or software USB sniffer (optional)

## Documentation

### Source Notes

Complete protocol analysis notes: [Notes/gadgets and gizmos/RadexOneReverseEngineerNotes.md](../../Notes/gadgets%20and%20gizmos/RadexOneReverseEngineerNotes.md)

### Example Traces

**Read Data Request:**
```
>: 7BFF 2000 0600 1800 ____ 4600 0008 0C00 F3F7
<: 7AFF 2080 1600 1800 ____ 3680 0008 ____ 0C00 ____ 1200 ____ 1200 ____ 1500 ____ BAF7
```

**Read Serial Number (SN: 180620-0840-008344 v1.8):**
```
>: 7BFF 2000 0600 9B0D ____ C2F2 0100 0C00 F2FF
<: 7AFF 2080 1E00 9B0D ____ AB72 0100 ____ 1400 ____ 11A4 ____ 9820 ____ 1400 0612 0108 4803 0800 ____ D61D
```

**Write Settings (repeat 3x):**
```
>: 7BFF 2000 1000 FA05 ____ 59FA 0208 0E00 0500 ____ 020A ____ ____ E8ED
<: 7AFF 2080 0600 FA05 ____ 647A 0208 ____ FDF7
```

**Read Settings:**
```
>: 7BFF 2000 0600 FD05 ____ 60FA 0108 0C00 F2F7
<: 7AFF 2080 1000 FD05 ____ 577A 0108 ____ 0500 ____ 020A ____ ____ F7ED
```

## Success Criteria

- [x] Serial communication parameters identified
- [x] Packet structure documented
- [x] Checksum algorithm reverse-engineered
- [x] Data reading commands documented
- [x] Settings read/write commands documented
- [x] Device identification commands documented
- [x] Example code snippets created
- [ ] Optional: Full library implementation (C#, Python, or JavaScript)
- [ ] Optional: Integration with home automation system

## Future Enhancements

1. **Library Development**
   - Create .NET library for Radex One communication
   - Publish to NuGet
   - Add to [BinaryDataDecoders](https://github.com/mwwhited/BinaryDataDecoders)

2. **Home Automation Integration**
   - Home Assistant custom component
   - MQTT bridge for radiation data
   - Real-time graphing and alerts

3. **Multi-Device Support**
   - Support multiple Radex One devices
   - Aggregate data from multiple sensors
   - Radiation mapping application

## Resources

- [Radex One Product Page](https://quartarad.com/product/radex-one/)
- [USB Serial Protocol Analysis Tools](https://sigrok.org/)
- Protocol documentation: `Notes/gadgets and gizmos/RadexOneReverseEngineerNotes.md`

## Notes

- Protocol uses little-endian byte order
- Checksum is critical - invalid checksum will result in no response
- Write settings command must be sent 3 times for device to accept changes
- Device responds within ~50ms typically
- USB serial converter chip may vary by production batch

---

*Last updated: 2026-01-07*
