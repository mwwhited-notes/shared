# Passive Radar System Using SDR Receivers

Multi-channel SDR receiver system for passive radar detection of aircraft and vehicles using existing RF illuminators.

## Overview

This project develops a passive radar (passive bistatic radar) system using multiple synchronized Software-Defined Radio (SDR) receivers. Unlike conventional radar that transmits its own signal, passive radar exploits existing RF illuminators like FM radio, TV broadcast, or cellular towers to detect and track targets.

The system uses two or more SDR receivers: one pointed at the illuminator (reference channel) to capture the direct signal, and one or more pointed toward the surveillance area to detect reflections from targets. Signal processing techniques extract target information from the difference between direct and reflected signals.

**Key capabilities:**
- Aircraft detection using FM/TV/cellular illuminators
- Vehicle tracking in local area
- Non-cooperative target detection (no transponder required)
- Covert operation (no transmitted signal)

## Project Status

**Status:** Planning Phase

**Background:**
- Software development experience (C#, .NET)
- Ham radio operator with RF/electronics knowledge
- Experience with Raspberry Pi projects and home automation
- Previous conversation covered basic architecture and approaches

**Next Steps:**

1. **Hardware Selection**
   - Evaluate SDR options: **[KrakenSDR](../../.personal/incoming/programmable-devices.md)** vs. synchronized **[RTL-SDR](../../.personal/incoming/programmable-devices.md)** vs. HackRF
   - Source clock synchronization hardware (GPS DO, external oscillator)
   - Select antenna configuration for reference and surveillance channels

2. **Clock Synchronization**
   - Research RTL-SDR clock modification techniques
   - Implement GPS disciplined oscillator (GPSDO) for stable reference
   - Test phase coherence between multiple receivers

3. **Signal Processing Pipeline**
   - Set up GNU Radio for initial signal capture
   - Implement direct signal cancellation algorithm
   - Develop cross-correlation for target detection
   - Create range-Doppler mapping for visualization

4. **Proof-of-Concept System**
   - Start with FM radio illuminator (88-108 MHz)
   - Build simple two-channel system (reference + surveillance)
   - Test aircraft detection in local area
   - Optimize antenna isolation to prevent reference channel saturation

5. **Software Development**
   - Explore Python/NumPy for signal processing
   - Evaluate existing passive radar toolkits
   - Build visualization for range-Doppler maps
   - Create logging and tracking system

## System Architecture

### Basic Passive Radar Configuration

```
                    ┌─────────────┐
                    │ Illuminator │
                    │ (FM/TV/Cell)│
                    └──────┬──────┘
                           │ Direct Signal
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        │                  ▼                  │
    ┌───▼────┐      ┌────────────┐      ┌────▼───┐
    │ Target │      │ Reference  │      │ Target │
    │Aircraft│      │  Antenna   │      │Vehicle │
    └───┬────┘      └──────┬─────┘      └────┬───┘
        │                  │                  │
        │ Reflected        │                  │ Reflected
        │ Signal           │                  │ Signal
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                    ┌──────▼──────┐
                    │ Surveillance│
                    │   Antenna   │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  SDR Array  │
                    │ (Synchronized)
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │   Signal    │
                    │  Processing │
                    │  Computer   │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │ Range-Doppler│
                    │     Map      │
                    └─────────────┘
```

### Signal Processing Pipeline

1. **Capture** - Synchronized SDR receivers sample reference and surveillance channels
2. **Direct Signal Cancellation** - Adaptive filtering removes direct path signal
3. **Cross-Correlation** - Correlate reference with surveillance to find reflections
4. **Range-Doppler Mapping** - Convert correlation to range and velocity
5. **Target Detection** - Threshold detection and tracking of targets

## Technical Challenges

### Clock Synchronization
- **Challenge:** SDR receivers must share stable, phase-coherent clock
- **Solutions:**
  - GPS disciplined oscillator (GPSDO) for all receivers
  - Clock modification for RTL-SDR (external clock input)
  - KrakenSDR (built-in synchronization)

### Dynamic Range
- **Challenge:** Direct signal is very strong, reflections are weak (60-100 dB difference)
- **Solutions:**
  - High-isolation antennas (directional, spatial separation)
  - Adaptive cancellation algorithms
  - High-dynamic-range SDR (>60 dB)

### Multipath
- **Challenge:** Urban environments create multiple reflection paths
- **Solutions:**
  - Sophisticated signal processing (CLEAN algorithm)
  - Multiple surveillance antennas (spatial filtering)
  - Beamforming techniques

### Processing Power
- **Challenge:** Real-time correlation requires significant computation
- **Solutions:**
  - GPU acceleration (CUDA/OpenCL)
  - Dedicated processing computer (multi-core, high RAM)
  - Optimize algorithms for efficiency

## Hardware Options

### SDR Receivers

**KrakenSDR (Recommended for beginners)**
- 5-channel coherent SDR
- Built-in clock synchronization
- Direction finding capability
- USB-powered
- ~$350

**RTL-SDR (Modified for sync)**
- Low cost ($25-35 each)
- Requires clock modification
- Need external GPSDO or rubidium reference
- Good for proof-of-concept

**HackRF One**
- Full duplex, 1 MHz - 6 GHz
- External clock input
- Higher cost (~$300 each)
- Greater flexibility

### Clock References

- GPS disciplined oscillator (GPSDO) - Leo Bodnar, Trimble
- Rubidium frequency standard
- Oven-controlled crystal oscillator (OCXO)

### Computing Platform

- Desktop PC (multi-core CPU, 16+ GB RAM)
- GPU for acceleration (NVIDIA CUDA recommended)
- High-speed storage for signal capture

## Equipment Used

### Current Inventory (to be verified)

Check these inventories for available SDR hardware:
- [Programmable Devices/](../../Programmable%20Devices/) - SDR receivers, RF modules
- [Test Equipment/](../../Test%20Equipment/) - Spectrum analyzers, signal generators
- [Expansion Boards/](../../Expansion%20Boards/) - Raspberry Pi SDR HATs

### To Be Acquired

- KrakenSDR or synchronized RTL-SDR array
- GPS disciplined oscillator
- Directional antennas (Yagi or log-periodic for reference channel)
- Omnidirectional antenna for surveillance
- Computing platform with GPU

## Software Tools

### Signal Acquisition & Processing

- **GNU Radio** - Visual signal processing framework, real-time SDR control
- **Python/NumPy/SciPy** - Signal processing algorithms, correlation, FFT
- **MATLAB/Octave** - Prototyping and analysis

### Existing Passive Radar Projects

- **KrakenSDR Passive Radar** - Official software for KrakenSDR
- **PSCR (Passive Synthetic Coherent Radar)** - Open-source passive radar toolkit
- **pyPassiveRadar** - Python-based passive radar implementation
- **gr-radar** - GNU Radio radar toolkit

### Visualization

- **Matplotlib** - Range-Doppler plots in Python
- **Qt/PyQt** - Real-time display GUI
- **WebGL/Three.js** - 3D visualization of detections

## Learning Goals

- Understand passive radar principles and bistatic geometry
- Master SDR receiver synchronization techniques
- Implement adaptive signal cancellation algorithms
- Learn correlation and range-Doppler processing
- Gain experience with real-time signal processing
- Explore GPU acceleration for DSP
- Understand radar cross-section and detection theory

## Illuminator Options

### FM Radio (Recommended Starting Point)
- **Frequency:** 88-108 MHz
- **Advantages:** Strong signal, wide coverage, well-documented
- **Range:** 50-150 km typical
- **Bandwidth:** ~200 kHz per station

### Digital TV (DVB-T)
- **Frequency:** 470-700 MHz (UHF band)
- **Advantages:** Higher frequency, wider bandwidth
- **Range:** 50-100 km
- **Bandwidth:** 8 MHz channels

### Cellular (LTE/5G)
- **Frequency:** 700-2600 MHz
- **Advantages:** Dense coverage, high power
- **Challenges:** Complex signal structure
- **Range:** 5-20 km

### DAB (Digital Audio Broadcasting)
- **Frequency:** 174-240 MHz
- **Advantages:** Digital, stable signal
- **Range:** 50-100 km

## Safety & Regulatory Notes

- **Passive operation:** No transmission, purely receive-only (legal in most jurisdictions)
- **Privacy considerations:** Can detect objects, not identify specific individuals
- **Airspace awareness:** Be aware of local aviation regulations if tracking aircraft
- **RF exposure:** Standard RF safety practices for antennas

## Related Projects

- [SCPI Instrument Control](../scpi-instrument-control/) - Test equipment automation for calibration
- See [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery) - SDR and RF experimentation

## Resources & References

### Academic Papers
- "Passive Bistatic Radar Systems" - IEEE papers on passive radar theory
- "FM Radio-Based Bistatic Radar" - Detection algorithms and performance

### Online Communities
- r/RTLSDR - RTL-SDR community
- KrakenSDR Discord - Passive radar discussions
- GNU Radio mailing list

### Books
- "Bistatic Radar: Principles and Practice" - Willis & Griffiths
- "Principles of Modern Radar" - Richards, Scheer, Holm

### Websites & Tools
- [KrakenSDR Documentation](https://github.com/krakenrf/krakensdr_docs)
- [RTL-SDR Blog](https://www.rtl-sdr.com/)
- [GNU Radio Tutorials](https://wiki.gnuradio.org/index.php/Tutorials)

## Project Milestones

### Phase 1: Proof-of-Concept (Weeks 1-4)
- Acquire KrakenSDR or 2x synchronized RTL-SDR
- Set up GNU Radio environment
- Capture FM radio reference and surveillance channels
- Verify clock synchronization and phase coherence

### Phase 2: Signal Processing (Weeks 5-8)
- Implement direct signal cancellation
- Develop cross-correlation algorithm
- Create range-Doppler mapping
- Test with stationary targets

### Phase 3: Target Detection (Weeks 9-12)
- Optimize detection algorithms
- Build tracking system
- Test aircraft detection
- Measure detection range and accuracy

### Phase 4: Enhancement (Ongoing)
- Add multiple illuminators
- Implement GPU acceleration
- Develop web-based visualization
- Experiment with other frequencies (TV, cellular)

---

*Last updated: 2026-01-07*
