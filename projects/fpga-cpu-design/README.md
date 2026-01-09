# FPGA CPU Design

Custom CPU and computer system designed in SystemVerilog for FPGA implementation.

## Overview

This project involves designing a custom CPU architecture from scratch, implementing it in SystemVerilog, and deploying it to an FPGA. The project builds on existing ALU and text graphics engine work from previous explorations. Goals include deepening understanding of computer architecture, learning SystemVerilog, and creating a working computer system.

The CPU will be implemented on the Digilent Arty A7-100 FPGA development board.

## Project Status

**Status:** In Progress

**Completed:**
- ALU design (from previous work)
- Text graphics engine (from previous work)

**Next Steps:**
1. Review and refactor existing ALU and graphics engine code
2. Design CPU control unit and instruction set architecture (ISA)
3. Implement register file and program counter
4. Develop memory controller
5. Integrate components and test on Arty A7-100
6. Write sample programs to test functionality

## Equipment Used

- [Digilent Arty A7-100](../../Programmable%20Devices/digilent-arty-a7-100/) - FPGA development board (XC7A100T)
  - Artix-7 XC7A100T FPGA (15,850 slices, 4,860 Kbit Block RAM, 240 DSP slices)
  - 256MB DDR3L, 16MB Quad-SPI Flash
  - 4 Pmod connectors, Arduino/ChipKit shield connector
- [AMD/Xilinx Vivado](../../Programmable%20Devices/digilent-arty-a7-100/README.md#development-tools) - FPGA synthesis and implementation
- [Test Equipment/](../../Test%20Equipment/) - Logic analyzer for debugging

## Code Repository

**Repository:** [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery)

**Location:** FPGA projects and SystemVerilog designs

**Repository Analysis:** [.claude/analysis/EmbeddedBakery/4caaa60-2025-03-14.md](../../../.claude/analysis/EmbeddedBakery/4caaa60-2025-03-14.md)
- 28 FPGA projects identified
- 484 Arduino sketches
- 6,586 total files
- Target platforms: Arty A7-100, Arty Z7-20, Cyclone II, and others

## Related Projects

- [SAP-1 Computer](../sap-1-computer/) - Breadboard 8-bit computer (learning progression: TTL breadboard → FPGA)
- [Zynq SoC Exploration](../zynq-soc-exploration/) - ARM+FPGA SoC on Arty Z7-20
- [MM-8000K Trainer UI](../mm8000-trainer-ui/) - Intel 8085 architecture reference
  - Repository: [MM8000](https://github.com/mwwhited-archives/MM8000) (Archived)
  - Analysis: [.claude/analysis/MM8000/7fbbdec-2026-01-08.md](../../../.claude/analysis/MM8000/7fbbdec-2026-01-08.md)

## Learning Goals

- Master SystemVerilog for RTL design
- Understand CPU microarchitecture deeply (pipelining, hazards, control flow)
- Learn FPGA resource optimization
- Practice verification and debugging of digital designs

## References

- Existing ALU and graphics engine code (to be migrated)
- [project-ideas.md](../project-ideas.md) - Original project concept

---

*Last updated: 2026-01-07*
