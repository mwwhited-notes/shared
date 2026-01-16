# SCPI Instrument Control + LSL Integration Guide

## Overview

Integrate laboratory instruments (oscilloscopes, multimeters, power supplies) with Lab Streaming Layer (LSL) for real-time, synchronized multi-modal data acquisition.

## Architecture

```
Instrument (LXI/VISA)
    ↓ (SCPI Commands)
LSL-SCPI Bridge
    ↓ (LSL Protocol)
Lab Streaming Layer
    ↓ (Multicast Discovery)
Applications (LabRecorder, MATLAB, Python)
```

## Prerequisites

### Hardware
- LXI-compatible instrument with VISA support (Rigol, Keysight, Tektronix, etc.)
- Ethernet connection to instrument
- Host machine with network connectivity

### Software
```bash
# Install PyVISA for SCPI communication
pip install pyvisa pyvisa-py

# Install Lab Streaming Layer
pip install pylsl

# See examples/python/lsl-scpi-bridge/ for complete setup
```

## Setup Steps

### 1. Verify Network Connectivity

```bash
# Test network connection to instrument
ping 192.168.1.100  # Replace with instrument IP

# Verify VISA resource is discoverable
python -c "import pyvisa; rm = pyvisa.ResourceManager(); print(rm.list_resources())"
```

### 2. Configure VISA Resource

Determine the correct VISA resource string:
- **LXI (Ethernet)**: `TCPIP::192.168.1.100::INSTR`
- **GPIB**: `GPIB0::10::INSTR`
- **Serial**: `ASRL3::INSTR`

Test connection:
```python
import pyvisa
rm = pyvisa.ResourceManager()
resource = rm.open_resource('TCPIP::192.168.1.100::INSTR')
print(resource.query('*IDN?'))  # Query instrument identification
resource.close()
```

### 3. Configure LSL Bridge

Edit `examples/python/lsl-scpi-bridge/config.yaml`:

```yaml
instrument:
  visa_resource: "TCPIP::192.168.1.100::INSTR"
  timeout: 5000

measurements:
  type: "voltage"
  channels: [1, 2, 3]
  sample_rate: 10  # Hz

lsl_stream:
  name: "Rigol-DMM-01"
  type: "EEG"
  manufacturer: "Rigol"
  model: "DM3068"
```

### 4. Run the Bridge

```bash
cd examples/python/lsl-scpi-bridge
python lsl_scpi_producer.py -c config.yaml
```

Monitor output:
```
2025-01-16 10:30:45 - __main__ - INFO - LSL-SCPI Bridge initialized
2025-01-16 10:30:45 - __main__ - INFO - Connected to instrument: RIGOL TECHNOLOGIES,DM3068,1234567,v1.0
2025-01-16 10:30:45 - __main__ - INFO - Created 1 LSL outlet(s)
```

## Recording Data

### Using LabRecorder

LabRecorder provides GUI-based recording of all LSL streams:

```bash
# Install LabRecorder
# Download from: https://github.com/labstreaminglayer/App-LabRecorder

# Run and it will discover streams automatically
labrecorder &

# Select streams and click "Start Recording"
# Data saved to XDF format with timestamps
```

### Programmatic Recording

```python
from lsl_inlet import resolve_stream, StreamInlet
import numpy as np

# Resolve the stream by name
streams = resolve_stream('name', 'Rigol-DMM-01')
inlet = StreamInlet(streams[0])

# Receive data
chunk, timestamps = inlet.pull_chunk(timeout=1.0)
print(f"Received {len(chunk)} samples")

# Access individual sample
for sample, ts in zip(chunk, timestamps):
    print(f"Sample: {sample}, Timestamp: {ts}")
```

## Multi-Instrument Synchronization

### Time Sync Challenges

- **Clock Drift**: Each instrument has slightly different clock rate
- **Propagation Delay**: Network latency varies
- **Sampling Rate Mismatch**: Instruments may have slightly different nominal rates

### Solution: NTP-Based Correction

Enable NTP sync in config:

```yaml
time_sync:
  use_ntp: true
  ntp_server: "pool.ntp.org"  # or local NTP server
```

This corrects timestamps against network time reference.

### Alternative: Master Clock

For highest precision, use a disciplined oscillator:
- GPS-Disciplined Oscillator (GPSDO) with 1PPS output
- Connect to trigger input of all instruments
- Use identical trigger source

## Common Measurement Scenarios

### Oscilloscope: Waveform Capture

```python
import lsl_scpi_bridge

config = {
    'instrument': {
        'visa_resource': 'TCPIP::192.168.1.50::INSTR',  # Keysight
    },
    'measurements': {
        'type': 'voltage',
        'channels': [1, 2],
        'sample_rate': 1000,  # 1 kHz
    }
}

bridge = lsl_scpi_bridge.ScpiLslBridge(config)
bridge.start()
bridge.wait()
```

### Power Supply: Current Monitoring

```python
config = {
    'measurements': {
        'type': 'current',
        'channels': [1],
        'sample_rate': 10,  # 10 Hz
        'averaging_count': 5,  # Smooth noise
    }
}
```

### Multi-Channel Temperature

```python
config = {
    'measurements': {
        'type': 'temperature',
        'channels': [1, 2, 3, 4],  # 4-channel thermocouple reader
        'sample_rate': 1,  # 1 Hz
    }
}
```

## Troubleshooting

### Connection Issues

| Error | Cause | Solution |
|-------|-------|----------|
| "VISA resource not found" | Instrument offline or wrong IP | Ping IP, check firewall |
| "Timeout during SCPI query" | Network latency or instrument busy | Increase timeout, reduce sample rate |
| "Connection refused" | Firewall blocking | Check firewall rules on instrument and host |

### Data Quality Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Clock drift over time | No time sync | Enable NTP sync |
| Gaps in timestamps | Measurement slowdown | Reduce sample rate |
| Noisy measurements | Poor electrical ground | Use shielded cables, twisted pairs |

### Performance

If CPU usage is high:
- Reduce `sample_rate`
- Increase `averaging_count` (trades latency for smoothness)
- Use multiple bridges (one per instrument) instead of serial

## Advanced Configuration

### Custom SCPI Commands

Extend `scpi_instrument.py`:

```python
def custom_query(self, command):
    """Send custom SCPI command"""
    return self.query(command)

# Example: Query oscilloscope trigger status
trigger_status = instrument.custom_query(':TRIG:STAT?')
```

### Batch Measurements

For higher efficiency:

```python
# Configure for bulk transfer
config['measurements']['averaging_count'] = 10

# Bridge will automatically average and publish less frequently
```

### Streaming to Multiple Consumers

LSL streams are automatically discovered by all applications on network:
- LabRecorder (GUI recording)
- MATLAB (LSL plugin)
- Python (via liblsl)
- Custom applications

No configuration needed - LSL handles multicast discovery.

## References

- **PyVISA**: https://pyvisa.readthedocs.io/
- **LSL Documentation**: https://labstreaminglayer.readthedocs.io/
- **SCPI Standards**: https://www.ivifoundation.org/scpi/
- **IVI Foundation**: https://www.ivifoundation.org/

## See Also

- Code example: `examples/python/lsl-scpi-bridge/`
- System architecture diagram: `diagrams/architecture/scpi-lsl-integration.puml`
- SCPI+LSL sequence diagram: `diagrams/protocols/lsl-stream-synchronization.puml`

---
**Created**: 2026-01-16
**Last Updated**: 2026-01-16
