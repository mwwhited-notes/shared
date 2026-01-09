# NeTV - FPGA Video Overlay Device

Open-source FPGA-based video overlay device for real-time video processing and manipulation.

## Device Information

| Field | Value |
|-------|-------|
| Manufacturer | bunnie (Andrew "bunnie" Huang) / Chumby |
| Model | NeTV Starter Pack |
| Product ID | Adafruit PID 609 |
| Type | FPGA Video Processor |
| FPGA | Xilinx Spartan-6 XC6SLX9 |
| Year | ~2012 |
| Date Acquired | 2026-01 |
| Price | $150.00 |
| Status | No longer stocked (Adafruit) |
| Open Source | Yes |

## Overview

NeTV is an open-hardware FPGA-based device that sits between a video source (cable box, game console, etc.) and a display, allowing real-time video overlay and processing. Created by Andrew "bunnie" Huang (known for Xbox hacking and open hardware advocacy).

**Key Capability:** Insert graphics, text, or manipulated video into live HDMI streams without modifying the source device.

## Technical Specifications

### FPGA

| Component | Specification |
|-----------|--------------|
| **FPGA** | Xilinx Spartan-6 XC6SLX9 |
| **Logic Cells** | 9,152 |
| **Block RAM** | 576 Kb |
| **DSP Slices** | 16 |
| **I/O** | User-accessible |

### Video Capabilities

| Feature | Details |
|---------|---------|
| **Input** | HDMI 1.3 |
| **Output** | HDMI 1.3 |
| **Resolutions** | 480p, 576p, 720p, 1080p/24, 1080i/60 |
| **Pixel Clock** | Up to 95MHz |
| **Processing** | Chroma-key overlay, alpha blending |
| **HDCP** | Supports overlay on encrypted feeds |
| **Color Depth** | 24-bit color |

### System

| Component | Specification |
|-----------|--------------|
| **CPU** | 800 MHz Marvell PXA168 (ARMv5TE) |
| **Cache** | 32kB/32kB L1, 128kB L2 |
| **RAM** | 128 MB DDR2 DRAM |
| **OS** | Angstrom-derived Linux |
| **Storage** | 1 GB microSD card (included) |
| **Network** | 802.11b/g WiFi |
| **Power** | MicroUSB (5V) |
| **Dimensions** | 94mm x 57mm |

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
- Xilinx Spartan-6 XC6SLX9 FPGA (video processing)
- HDMI transceivers (input/output)
- Marvell PXA168 ARM CPU (control system)
- 128 MB DDR2 memory (frame buffering)
- 802.11b/g WiFi
- MicroSD card slot
- IR receiver and extender port
- Status LEDs (blue and green)
- Injection-molded plastic enclosure

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

## Kit Contents

- NeTV board (ARM + FPGA)
- Injection-molded plastic enclosure with rubber anti-slip bottom
- 1 GB microSD card with Angstrom Linux pre-installed
- HDMI cables
- Power supply / USB cable
- Documentation links

## Comparison to Other FPGA Boards

| Feature | NeTV Starter Pack | Arty A7 | DE10-Nano |
|---------|-------------------|---------|-----------|
| **Primary Use** | Video overlay | General FPGA dev | SoC development |
| **FPGA** | Spartan-6 XC6SLX9 | Artix-7 100T | Cyclone V |
| **Logic Cells** | 9,152 | 101,440 | 110,000 |
| **Video I/O** | HDMI in/out | None (add-on) | None (add-on) |
| **CPU** | ARM PXA168 800MHz | None | ARM Cortex-A9 |
| **OS** | Linux | None | Linux |
| **Application** | Specialized | General purpose | SoC development |
| **Price** | $150 (discontinued) | ~$129 | ~$150 |

**NeTV Advantage:** Ready-made video processing platform with HDMI built-in, complete kit with enclosure.

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
