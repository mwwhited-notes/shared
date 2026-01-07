# Passive Radar SDR - Conversation Context

This file contains context for continuing technical discussions about this project with AI assistants or in new chat sessions.

## Prompt for Continuing Conversation

---

I'm working on building a passive radar receiver system using multiple SDR receivers. I want to detect aircraft and vehicles by exploiting existing RF illuminators like FM radio, TV broadcast, or cellular towers.

**My background:**
- Software developer with experience in C#, .NET
- Ham radio operator with RF/electronics knowledge
- Have worked with Raspberry Pi projects and home automation
- Comfortable with technical projects and troubleshooting

**What we've covered so far:**
- Basic passive radar architecture (reference + surveillance channels)
- Need for synchronized SDR receivers sharing clock source
- Signal processing chain: capture, direct signal cancellation, cross-correlation, range-Doppler mapping
- Hardware options like KrakenSDR, modified RTL-SDRs, or HackRF
- FM radio as recommended starting illuminator source
- Key challenges: clock sync, dynamic range, multipath, processing power

**Project documentation location:**
This project is documented at `/projects/passive-radar-sdr/` in my technical notebook repository.

**What I want to explore:**
- Detailed synchronization techniques for RTL-SDR receivers
- Signal processing algorithms and implementation approaches
- Antenna configuration and isolation strategies
- Software tools (GNU Radio, Python/NumPy, existing passive radar toolkits)
- Practical first steps for a working proof-of-concept system

Please help me design a practical implementation plan for building this passive radar system, focusing on the technical details of clock synchronization and the signal processing pipeline.

---

## Quick Technical Reference

### Current Phase
Planning and hardware selection

### Key Technical Areas to Explore

1. **Clock Synchronization**
   - GPS disciplined oscillator (GPSDO) integration
   - RTL-SDR clock modification (external clock input)
   - Phase coherence measurement and verification
   - KrakenSDR synchronization architecture

2. **Signal Processing Pipeline**
   - GNU Radio flowgraph design
   - Adaptive filtering for direct signal cancellation (LMS, RLS algorithms)
   - Fast cross-correlation implementation (FFT-based)
   - Range-Doppler map generation
   - CFAR (Constant False Alarm Rate) detection

3. **Antenna System**
   - Reference antenna (high-gain directional toward illuminator)
   - Surveillance antenna (omnidirectional or sector)
   - Isolation requirements (>60 dB typical)
   - Antenna placement and orientation

4. **Software Architecture**
   - Real-time vs. batch processing trade-offs
   - Data buffering and memory management
   - GPU acceleration options (CUDA, OpenCL)
   - Visualization and tracking display

### Hardware Decisions to Make

- [ ] KrakenSDR ($350, integrated sync) vs. modified RTL-SDR (~$100-150, DIY sync)
- [ ] GPSDO source (Leo Bodnar, Trimble, rubidium standard)
- [ ] Antenna types and mounting
- [ ] Processing computer specs (CPU cores, RAM, GPU)

### Software Stack Candidates

- **Signal Acquisition:** GNU Radio, SDR++, CubicSDR
- **Processing:** Python (NumPy, SciPy, PyTorch), MATLAB/Octave, C++
- **Existing Tools:** KrakenSDR passive radar app, pyPassiveRadar, gr-radar
- **Visualization:** Matplotlib, Qt/PyQt, web-based (WebGL)

### Illuminator Strategy

Start with FM radio (88-108 MHz):
- Strong, stable signal
- Wide coverage area
- Well-documented for passive radar
- Simple antenna design
- Proven detection range: 50-150 km for aircraft

Later expansion:
- Digital TV (DVB-T) for higher resolution
- Cellular (LTE) for local area coverage
- DAB (Digital Audio Broadcasting)

### Learning Resources Needed

- Academic papers on bistatic radar geometry
- GNU Radio tutorials for SDR signal processing
- KrakenSDR documentation and examples
- Cross-correlation and matched filter theory
- CLEAN algorithm for multipath mitigation

---

## Session Notes

Use this section to track progress from different work sessions or conversations.

### Session 1: Initial Planning (2026-01-07)
- Created project documentation structure
- Identified key technical challenges
- Listed hardware and software options
- Established learning goals and milestones

### Session 2: [Date]
*Add notes here*

---

*Last updated: 2026-01-07*
