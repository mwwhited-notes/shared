# Projects Index

Active project documentation and build logs organized by category.

## Quick Reference

| Project | Category | Status | Equipment |
|---------|----------|--------|-----------|
| [FPGA CPU Design](#fpga-cpu-design) | Digital Logic | In Progress | Arty A7-100 |
| [SAP-1 Computer](#sap-1-computer) | Digital Logic | In Progress | 74-series, breadboards |
| [Zynq SoC Exploration](#zynq-soc-exploration) | SoC/Embedded | In Progress | Arty Z7-20 |
| [Analog Computer Experiments](#analog-computer-experiments) | Analog Computing | In Progress | THAT |
| [ATtiny2313 LED Clock](#attiny2313-led-clock) | Microcontrollers | In Progress | ATtiny2313 |
| [MM-8000K Trainer UI](#mm-8000k-intel-8085-trainer-ui) | Retro Computing | In Progress | MM-8000K |
| [SCPI Instrument Control](#scpi-instrument-control) | Test Automation | Planning | Lab equipment |
| [Home Automation](#home-automation) | Smart Home | In Progress | Pi 3, Z-Wave |
| [DIY TrekPak Dividers](#diy-trekpak-dividers) | Workshop | Materials Ready | Foam, pins |

## Projects by Category

### Digital Logic & FPGA

#### FPGA CPU Design
**Status:** In Progress
**Directory:** [fpga-cpu-design/](fpga-cpu-design/)

Custom CPU architecture designed from scratch in SystemVerilog for FPGA implementation on the Digilent Arty A7-100. Learning computer architecture fundamentals, SystemVerilog HDL, and FPGA resource optimization.

**Equipment:** Arty A7-100, Vivado
**Related:** [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery)

---

#### SAP-1 Computer
**Status:** In Progress
**Directory:** [sap-1-computer/](sap-1-computer/)

Building the SAP-1 (Simple As Possible) 8-bit breadboard computer based on Ben Eater's design. Uses discrete 74-series TTL logic chips, AT28C16 EEPROMs for microcode, and ATF16v8b GAL chips for memory control.

**Equipment:** 74-series logic, breadboards, EEPROM/GAL programmers
**Related:** Digital Computer Electronics (Malvino), [Ben Eater's videos](https://www.youtube.com/playlist?list=PLowKtXNTBypGqImE405J2565dvjafglHU)

---

### System-on-Chip & Embedded

#### Zynq SoC Exploration
**Status:** In Progress - Initial Learning
**Directory:** [zynq-soc-exploration/](zynq-soc-exploration/)

Exploring Xilinx Zynq architecture combining ARM Cortex-A9 processors with FPGA fabric. Learning AXI bus interfacing, custom hardware accelerators, embedded Linux, and hardware-software co-design.

**Equipment:** Arty Z7-20, Vivado + Vitis
**Related:** FPGA CPU Design project

---

#### ATtiny2313 LED Clock
**Status:** In Progress
**Directory:** [attiny2313-clock/](attiny2313-clock/)

LED clock using ATtiny2313 microcontroller. Learning ISP programming, AVR architecture, and timekeeping techniques. New LED screen module ready for soldering, counter code needs tuning for accuracy.

**Equipment:** ATtiny2313, LED display, ISP programmer, KSGER T12 soldering station

---

### Analog Computing

#### Analog Computer Experiments
**Status:** In Progress - Learning Phase
**Directory:** [analog-computer-experiments/](analog-computer-experiments/)

Exploring analog computing fundamentals with Anabrid's "The Analog Thing" (THAT). Planned experiments include Lorenz attractor visualization, predator-prey modeling, and hybrid analog-digital systems with STM32.

**Equipment:** THAT analog computer, oscilloscope, STM32 boards
**Research:** [AnalogComputers/analog-computing-repository/](../AnalogComputers/analog-computing-repository/) - 232 PDFs, 660MB collection

---

### Retro Computing

#### MM-8000K Intel 8085 Trainer UI
**Status:** In Progress
**Directory:** [mm8000-trainer-ui/](mm8000-trainer-ui/)

Modern user interface for the MM-8000K Intel 8085 trainer. Combines physical hardware with software emulation for convenient development and debugging. Features memory viewer, register display, and assembler with syntax highlighting.

**Equipment:** MM-8000K trainer, development workstation
**Related:** [MM8000 Emulator](https://github.com/mwwhited-archives/MM8000) (.NET Core + ANTLR)

---

### Test & Measurement Automation

#### SCPI Instrument Control
**Status:** Planning/Research
**Directory:** [scpi-instrument-control/](scpi-instrument-control/)

Network control system for SCPI-compatible test equipment with custom .NET Core VISA driver. Building RS-232/Ethernet gateway for lab equipment automation (HP 34401A, Rigol DM3058E, DG1022, Korad supplies).

**Equipment:** HP 34401A DMM, Rigol DM3058E, DG1022, Raspberry Pi/BeagleBone
**Related:** [DeviceBridge](https://github.com/mwwhited/DeviceBridge)

---

### Smart Home & IoT

#### Home Automation
**Status:** In Progress
**Directory:** [home-automation/](home-automation/)

Migrating from HomeSeer HS4 to Home Assistant for home automation. Z-Wave focus with multi-protocol support (Zigbee, Matter, Thread). 100% local control with self-hosted remote access via WireGuard VPN.

**Equipment:** Raspberry Pi 3 (×2), Z-Wave hats, Z-Net bridge, Galaxy Tab4 Nook (dashboard)
**Platform:** Home Assistant (open source, no subscriptions)

---

### Workshop Organization

#### DIY TrekPak Dividers
**Status:** Materials Ready
**Directory:** [diy-trekpak-dividers/](diy-trekpak-dividers/)

Custom drawer and parts case dividers using corrugated plastic, EVA foam, and hair pins. DIY alternative to Pelican TrekPak system at ~$60-70 vs $80-150+ commercial cost. Works with any drawer/case size.

**Materials:** Hair pins, EVA foam, felt tape, corrugated plastic
**Use Cases:** Component storage, tool organization, camera cases

---

## Project Status Summary

- **Active Development:** 7 projects (FPGA CPU, SAP-1, Zynq, Analog Computer, ATtiny Clock, MM8000 UI, Home Automation)
- **Planning/Research:** 1 project (SCPI Control)
- **Materials Ready:** 1 project (TrekPak Dividers)

## Cross-References

### Equipment Inventories
- [Programmable Devices/](../Programmable%20Devices/) - FPGA, MCU, dev boards
- [Test Equipment/](../Test%20Equipment/) - Oscilloscopes, DMMs, programmers
- [Vintage Computers/](../Vintage%20Computers/) - Apple II, TI-99/4A, MM-8000K
- [Device Lab/](../Device%20Lab/) - Tablets, Pi devices, hackable hardware
- [Expansion Boards/](../Expansion%20Boards/) - Arduino shields, Pi HATs

### Planning & Documentation
- [project-ideas.md](../project-ideas.md) - Project backlog and future ideas
- [workshop-capabilities.md](../workshop-capabilities.md) - Equipment summary and project ideas by difficulty
- [tools-and-components.md](../tools-and-components.md) - Hand tools, wire, consumables, component stock

### Research Collections
- [AnalogComputers/analog-computing-repository/](../AnalogComputers/analog-computing-repository/) - Analog computing research (232 PDFs)
- [Notes/](../Notes/) - Technical notes by topic (hardware, software, FPGA, AI/ML)

### Related Repositories
- [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery) - Arduino, AVR, ESP8266, STM32, FPGA projects
- [MM8000](https://github.com/mwwhited-archives/MM8000) - Intel 8085 trainer emulator
- [DeviceBridge](https://github.com/mwwhited/DeviceBridge) - IEEE-1284 parallel port capture
- [MyMashedDuet](https://github.com/mwwhited/MyMashedDuet) - Velleman K8200 3D printer config

## Adding New Projects

Follow [.claude/protocols/PROJECTS_PROTOCOL.md](../.claude/protocols/PROJECTS_PROTOCOL.md) when creating new project documentation.

**Standard structure:**
```
projects/
└── new-project-name/
    ├── README.md           # Required - overview, status, equipment, references
    ├── build-log.md        # Optional - session-by-session progress
    ├── parts-list.md       # Optional - detailed BOM
    └── [project files]     # Code, schematics, notes, etc.
```

---

*Last updated: 2026-01-07*
