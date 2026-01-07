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
- [AMD/Xilinx Vivado](../../Programmable%20Devices/digilent-arty-a7-100/README.md#development-tools) - FPGA synthesis and implementation

## Related Projects

- [Intel 8085 Trainer UI](#) - CPU design learning complements trainer UI work
- See [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery) repository for previous FPGA work

## Learning Goals

- Master SystemVerilog for RTL design
- Understand CPU microarchitecture deeply (pipelining, hazards, control flow)
- Learn FPGA resource optimization
- Practice verification and debugging of digital designs

## References

- Existing ALU and graphics engine code (to be migrated)
- [project-ideas.md](../../project-ideas.md) - Original project concept

---

*Last updated: 2026-01-07*
