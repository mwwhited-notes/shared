# Zynq SoC Exploration

Learning System-on-Chip (SoC) design with Xilinx Zynq Z7-20 - ARM + FPGA integration.

## Overview

This project explores System-on-Chip (SoC) design using the Xilinx Zynq architecture, which combines ARM Cortex-A9 processors with FPGA fabric on a single chip. The Digilent Arty Z7-20 board provides a development platform for learning:
- ARM processor programming (bare metal and Linux)
- Custom FPGA accelerators and peripherals
- AXI bus interfacing between ARM and FPGA
- High-performance embedded system design

## Project Status

**Status:** In Progress - Initial Learning Phase

**Next Steps:**
1. Set up Vivado development environment for Zynq
2. Run "Hello World" on ARM core
3. Build simple FPGA peripheral (LED control, GPIO)
4. Implement AXI bus communication between ARM and FPGA
5. Design custom hardware accelerator (e.g., image processing)
6. Explore Linux on Zynq (PetaLinux or custom Yocto build)
7. Build complete SoC application combining software and hardware

## Equipment Used

- **[Digilent Arty Z7-20](../../.personal/incoming/programmable-devices.md)** - Zynq-7020 SoC development board
- **AMD/Xilinx Vivado + Vitis** - SoC development tools
- MicroSD card for Linux boot
- USB-UART for serial console

## Architecture

```
┌─────────────────────────────────────────────┐
│          Xilinx Zynq Z7-20 SoC              │
│                                             │
│  ┌──────────────────┐   ┌────────────────┐ │
│  │  Processing      │   │  Programmable  │ │
│  │  System (PS)     │   │  Logic (PL)    │ │
│  │                  │   │                │ │
│  │  • ARM Cortex-A9 │   │  • Custom      │ │
│  │    (Dual Core)   │   │    Peripherals │ │
│  │  • DDR3 Memory   │◄──┤  • Accelerators│ │
│  │  • Peripherals   │AXI│  • IP Cores    │ │
│  └──────────────────┘   └────────────────┘ │
└─────────────────────────────────────────────┘
```

## Planned Experiments

### Basic Learning
1. ARM bare-metal programming (no OS)
2. Simple FPGA peripheral (GPIO, LED controller)
3. AXI4-Lite memory-mapped communication
4. Interrupts between PL and PS

### Intermediate Projects
1. Custom DMA engine in FPGA
2. Hardware image processing accelerator
3. High-speed data acquisition system
4. Soft-core processor in FPGA fabric (MicroBlaze)

### Advanced Topics
1. Linux kernel driver development for custom IP
2. High-performance DSP applications
3. Multi-core programming (both ARM cores)
4. Integration with external peripherals (sensors, displays)

## Learning Goals

- Understand SoC architecture and design principles
- Master AXI bus protocols (AXI4, AXI4-Lite, AXI-Stream)
- Learn embedded Linux development and device drivers
- Design hardware accelerators for compute-intensive tasks
- Practice co-design (partitioning between software and hardware)

## Code Repository

**Repository:** [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery)

**Analysis:** [.claude/analysis/EmbeddedBakery/4caaa60-2025-03-14.md](../../../.claude/analysis/EmbeddedBakery/4caaa60-2025-03-14.md)
- 28 FPGA projects (includes Arty Z7-20 work)
- 6,586 files total
- Platforms: Arty A7-100, Arty Z7-20, Cyclone II, PAL/GAL

## Related Projects

- [FPGA CPU Design](../fpga-cpu-design/) - Soft-core CPU experience applies to Zynq PL (custom CPU → SoC integration)
  - Learning progression: Custom FPGA CPU → Commercial SoC (Zynq)
- [SCPI Instrument Control](../scpi-instrument-control/) - Zynq could serve as high-performance instrument controller
- [SAP-1 Computer](../sap-1-computer/) - Architecture fundamentals (breadboard → FPGA → SoC)
- [Analog Computer Experiments](../analog-computer-experiments/) - Hybrid analog-digital using Zynq + THAT

## References

- Digilent Arty Z7 reference manual
- Xilinx Zynq-7000 Technical Reference Manual
- Vivado and Vitis documentation
- [project-ideas.md](../project-ideas.md) - Original project concept

---

*Last updated: 2026-01-07*
