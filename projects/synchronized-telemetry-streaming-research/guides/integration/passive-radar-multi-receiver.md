# Passive Radar Multi-Receiver Synchronization Guide

## Overview
Coordinate multiple geographically distributed SDR receivers for passive radar, radio direction finding, or seismic monitoring using synchronized timestamps and TDOA (Time Difference of Arrival) analysis.

## Architecture
```
Receivers (GPS-synchronized clocks)
    ↓
Sample streams with precise timestamps
    ↓
Time Correlation Engine
    ↓
TDOA Analysis
    ↓
Source localization
```

## Synchronization Methods

### 1. GPS 1PPS (Best: <10µs)
- Connect GPS receiver to all SDRs
- 1 pulse per second with <100ns jitter
- Most accurate for distributed systems

### 2. NTP (Good: <1ms over LAN)
- Network Time Protocol
- Easy to deploy, no special hardware
- Sufficient for most applications

### 3. PTP (Excellent: <1µs)
- IEEE 1588v2 Precision Time Protocol
- Hardware-assisted synchronization
- Enterprise-grade deployment

## Implementation
```python
# Python SDR + LSL multi-stream
from pylsl import StreamInfo, StreamOutlet

# Each receiver outputs:
# - I/Q samples at precise timestamp
# - GPS coordinates
# - Antenna orientation

# LabRecorder captures all streams
# Post-processing computes TDOA
```

## TDOA Localization
- Cross-correlation between receivers
- Hyperbolic position fix
- Accuracy: wavelength/2 phase resolution

## References
- Architecture: `diagrams/synchronization/multi-stream-correlation.puml`
- Passive radar guide: `guides/deployment/`

---
Created: 2026-01-16
