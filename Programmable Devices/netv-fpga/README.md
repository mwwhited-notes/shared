# NeTV - FPGA Video Overlay Device

Open-source FPGA-based video overlay device for real-time video processing and manipulation.

## Device Information

| Field | Value |
|-------|-------|
| Manufacturer | bunnie (Andrew "bunnie" Huang) / Chumby |
| Model | NeTV |
| Type | FPGA Video Processor |
| FPGA | Xilinx Spartan-6 LX45 |
| Year | ~2012 |
| Status | TBD |
| Open Source | Yes |

## Overview

NeTV is an open-hardware FPGA-based device that sits between a video source (cable box, game console, etc.) and a display, allowing real-time video overlay and processing. Created by Andrew "bunnie" Huang (known for Xbox hacking and open hardware advocacy).

**Key Capability:** Insert graphics, text, or manipulated video into live HDMI streams without modifying the source device.

## Technical Specifications

### FPGA

| Component | Specification |
|-----------|--------------|
| **FPGA** | Xilinx Spartan-6 LX45 |
| **Logic Cells** | ~43,000 |
| **Block RAM** | 2,088 Kb |
| **DSP Slices** | 58 |
| **I/O** | Up to 358 user I/O pins |

### Video Capabilities

| Feature | Details |
|---------|---------|
| **Input** | HDMI 1.3 (up to 1080p) |
| **Output** | HDMI 1.3 (up to 1080p) |
| **Processing** | Real-time video overlay, alpha blending |
| **Latency** | Low-latency passthrough |
| **Color Depth** | 24-bit color |

### System

| Component | Specification |
|-----------|--------------|
| **CPU** | ARM (embedded in system) |
| **OS** | Linux (embedded) |
| **Storage** | SD card |
| **Network** | Ethernet |
| **Power** | 12V DC |

## Features

### Video Processing

- **Real-time HDMI overlay** - Insert graphics over live video
- **Alpha blending** - Transparent overlays
- **Video passthrough** - Zero-latency mode when overlay disabled
- **Resolution support** - 480p, 720p, 1080i, 1080p

### Programmability

- **FPGA gateware** - Verilog/VHDL customization
- **Linux userspace** - C/Python applications
- **Web interface** - Browser-based control
- **API** - HTTP REST API for automation

### Use Cases

1. **Live video annotations** - Add graphics, scoreboards, timers to broadcasts
2. **Augmented reality overlays** - Real-time information overlay on video
3. **Video effects** - Filters, transformations, mixing
4. **Subtitles/captions** - Real-time text overlay
5. **Gaming overlays** - Twitch-style overlays for streaming
6. **Video hacking/research** - HDMI protocol analysis and experimentation

## Architecture

```
HDMI Input → HDMI Decoder → FPGA Processing → HDMI Encoder → HDMI Output
                                  ↑
                             ARM CPU + Linux
                             (Control, Overlay Data)
```

**Processing Flow:**
1. HDMI input decoded to video stream
2. FPGA processes video (overlay, effects)
3. ARM CPU provides overlay content and control
4. Processed video encoded to HDMI output

## Hardware Design

**Open Hardware:**
- Schematics available
- PCB layout available
- Bill of materials (BOM) published
- Licensed under open-source hardware license

**Components:**
- Xilinx Spartan-6 FPGA (video processing)
- HDMI transceivers (input/output)
- ARM CPU (control system)
- DDR2 memory (frame buffering)
- Ethernet PHY
- SD card slot

## Software & Gateware

### FPGA Gateware

**Repository:** [bunnie/netv-fpga](https://github.com/bunnie/netv-fpga)

**Language:** Verilog

**Components:**
- HDMI input decoder
- Video processing pipeline
- Overlay engine with alpha blending
- HDMI output encoder
- Memory controller

### Linux System

**Userspace Applications:**
- Web server for control interface
- Overlay rendering
- Network configuration
- API server

### Development

**FPGA Tools:**
- Xilinx ISE (legacy)
- Xilinx Vivado (if porting to newer devices)

**Software Development:**
- Cross-compile for ARM
- Python/C for userspace apps
- HTML/JavaScript for web UI

## Programming & Configuration

### FPGA Configuration

**Loading Custom Gateware:**
```bash
# Flash FPGA bitstream to device
# (Specific commands depend on NeTV boot loader)
```

### API Examples

**HTTP API for overlay control:**
```bash
# Set URL for overlay content
http://10.0.88.1/bridge?cmd=seturl&value=http://example.com

# Load content in tab
http://10.0.88.1/bridge?cmd=multitab&tab=0&options=load&param=http://server:5000
```

## Projects & Applications

### Potential Projects

1. **Live Streaming Overlay**
   - Display chat, alerts, stats on game/video stream
   - Twitch/YouTube streaming graphics

2. **Home Automation Display**
   - Overlay home automation status on TV
   - Display sensor data, cameras, notifications

3. **Security Camera Overlay**
   - Add timestamp, camera ID, motion alerts
   - Multi-camera split-screen

4. **Educational Content**
   - Real-time annotations for teaching
   - Interactive video overlays

5. **Video Research**
   - HDMI protocol analysis
   - Video format conversion experiments
   - Custom video processing algorithms

## Resources

### Official Documentation

- **Main Wiki:** [NeTV Main Page](https://www.kosagi.com/w/index.php?title=NeTV_Main_Page)
- **FPGA Repository:** [bunnie/netv-fpga](https://github.com/bunnie/netv-fpga)
- **Local UI Documentation:** [NeTV_local_UI](https://www.kosagi.com/w/index.php?title=NeTV_local_UI)
- **Web Services:** [NeTV_web_services](https://www.kosagi.com/w/index.php?title=NeTV_web_services)
- **App Development:** [NeTV App Development](https://www.kosagi.com/w/index.php?title=%22App%22_development)
- **Tricks & Tips:** [NeTV_tricks](https://www.kosagi.com/w/index.php?title=NeTV_tricks)
- **Android App:** [netv-android](https://github.com/sutajiokousagi/netv-android)

### Community & Forums

- **Kosagi Forums:** [https://www.kosagi.com/forums/](https://www.kosagi.com/forums/)
- bunnie's blog: [bunniestudios.com](https://www.bunniestudios.com/)

### Reference Links

Saved in `notes.md` (this directory):
```
https://github.com/bunnie/netv-fpga
https://github.com/sutajiokousagi/netv-android
https://www.kosagi.com/forums/index.php
https://www.kosagi.com/w/index.php?title=NeTV_local_UI
https://www.kosagi.com/w/index.php?title=NeTV_web_services
https://www.kosagi.com/w/index.php?title=%22App%22_development
https://www.kosagi.com/w/index.php?title=NeTV_tricks

http://10.0.88.1/bridge?cmd=multitab&tab=0&options=load&param=http://10.0.88.4:5000
http://10.0.88.1/bridge?cmd=seturl&value=http://www.abc.com
http://10.0.88.1/bridge?cmd=seturl&value=http://10.0.88.4:5000
```

## Comparison to Other FPGA Boards

| Feature | NeTV | Arty A7 | DE10-Nano |
|---------|------|---------|-----------|
| **Primary Use** | Video overlay | General FPGA dev | SoC development |
| **FPGA** | Spartan-6 LX45 | Artix-7 100T | Cyclone V |
| **Video I/O** | HDMI in/out | None (add-on) | None (add-on) |
| **CPU** | ARM (embedded) | None | ARM Cortex-A9 |
| **OS** | Linux | None | Linux |
| **Application** | Specialized | General purpose | SoC development |

**NeTV Advantage:** Ready-made video processing platform with HDMI built-in.

## Related Projects

- [FPGA CPU Design](../../projects/fpga-cpu-design/) - Custom CPU in SystemVerilog
- [Zynq SoC Exploration](../../projects/zynq-soc-exploration/) - ARM+FPGA SoC
- [Arty A7-100](../digilent-arty-a7-100/) - Xilinx Artix-7 FPGA board
- [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery) - FPGA and embedded projects

## Documentation

**Local Files:**
- `notes.md` - URL references and API examples

## Notes

- Created by Andrew "bunnie" Huang (famous for Xbox hacking, Chumby)
- Open-source hardware and software
- Designed for video overlay applications
- FPGA customization allows arbitrary video processing
- Good example of FPGA applied to real-world video problems
- Older Spartan-6 FPGA (ISE toolchain, not Vivado)
- Could be integrated with home automation for TV overlays

## Hackability: ★★★★★

- **Fully open source** hardware and software
- **FPGA gateware customizable** in Verilog
- **Linux userspace** programmable in C/Python
- **Active community** (though older device)
- **Well documented** with wiki and GitHub repos

---

*Last updated: 2026-01-07*
