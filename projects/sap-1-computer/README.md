# SAP-1 Computer (Ben Eater 8-bit Computer)

Building the SAP-1 (Simple As Possible) computer based on Ben Eater's 8-bit breadboard computer design.

## Overview

The SAP-1 is an educational 8-bit computer designed to teach computer architecture fundamentals. This project follows Ben Eater's design using discrete 74-series logic chips on breadboards. The computer demonstrates fundamental concepts:
- Clock cycles and instruction execution
- Program counter and memory addressing
- ALU operations with the 74181 chip
- Control logic using microcode
- Display and output

The build uses breadboards, 74-series TTL logic ICs, EEPROMs for microcode storage, and discrete components.

## Project Status

**Status:** In Progress

**Next Steps:**
1. Complete breadboard assembly
2. Program microcode EEPROMs
3. Test individual modules (clock, ALU, registers, display)
4. Integrate full system
5. Write test programs
6. Debug and refine microcode

## Architecture

The SAP-1 computer includes:
- **Clock Module** - Adjustable clock with single-step capability
- **Registers** - A, B, instruction, memory address, program counter
- **ALU** - 74181 4-bit ALU chip (arithmetic and logic operations)
- **RAM** - Program and data storage (using AT28C16 EEPROMs)
- **Control Logic** - Microcode-based instruction decoder (ATF16v8 GAL)
- **Output** - 7-segment display for results

## Implementation Notes

### Memory Controller

The original Ben Eater design uses combinational logic for memory control. This implementation replaces that with an ATF16v8b GAL programmed with CUPL.

See [memory-controller-notes.md](memory-controller-notes.md) for detailed memory controller documentation including:
- CUPL source code
- IC pinout diagrams
- Logic diagrams
- Truth tables

## Files in This Directory

### Microcode & Programming
- `MicroCode.xlsx`, `NewMicroCode.xlsx` - Microcode control signal tables
- `MicroCode A.bin`, `MicroCode B.bin`, `MicroCode B2.bin` - EEPROM binary files
- `microCode3.bin` through `microCode5.bin` - Microcode versions
- `AT28C16-DIP24.HEX` - EEPROM programming file
- `org-microcode-withflags.BIN` - Original microcode with flags

### Memory Controller
- `memory-controller-notes.md` - Detailed memory controller documentation
- `Memory Controller.dig` - Digital logic simulation
- `Memory Controller.jed`, `.hex` - GAL programming files
- `Memory Controller.xlsx`, `.csv` - Truth tables and logic
- `Memory Controller.svg`, `.png` - Schematics and diagrams
- `Memory Controller Detailed.csv` - Detailed truth table
- `CUPL_Memory Controller/` - CUPL source files for GAL

### RAM Controller
- `RAM Controller.xlsx`, `RAM Controller - Simple.xlsx` - RAM control logic
- `RAM Controller.csv`, `.tru` - RAM control truth tables
- `RAM Controller.jed` - GAL programming file
- `CUPL_RAM Controller/` - CUPL source files

### Display & Testing
- `Display.bin`, `DisplayV2.bin`, `org-Display.bin` - Display ROM files
- `Demo.csv`, `Demo.tru` - Test programs
- `testdatacomp.csv` - Test data comparison
- `MemoryController.tru` - Memory controller test data

### Documentation
- `logic tables.xlsx`, `.csv` - Complete logic tables
- `Memory Register.csv` - Memory register control

## Equipment Used

- Breadboards and jumper wires
- 74-series TTL logic chips (74181, 74LS04, 74LS86, 74LS245, 74LS173, etc.)
- AT28C16 EEPROMs (CAT28C16A) - For microcode storage
- ATF16v8b GAL chips - For memory controller logic
- [EEPROM programmer](../../Test%20Equipment/) - For programming microcode
- [GAL programmer](../../Test%20Equipment/) - For programming ATF16v8b
- [Logic analyzer](../../Test%20Equipment/) - For debugging
- Power supply (5V regulated)

## Design Tools

- [Digital](https://github.com/hneemann/Digital) - Digital logic simulator
- [WinCUPL](https://www.microchip.com/en-us/development-tool/WinCUPL) - GAL programming
- [Truth Table Maker](https://truthtablemaker.com/) - Logic design
- Excel - Microcode and truth table generation

## Learning Goals

- Understand computer architecture from first principles
- Learn digital logic design and debugging
- Practice microcode programming
- Explore instruction set design
- Understand bus architecture and control signals
- Work with GAL/PAL programmable logic

## References

### Books
- **Digital Computer Electronics** by Albert Paul Malvino (purchased 2020-01-09, $29.44)
  - Original SAP-1 computer design source
  - See [tools-and-components.md](../../tools-and-components.md#books--references) for book inventory

### Online Resources
- [Ben Eater's 8-bit Computer Playlist](https://www.youtube.com/playlist?list=PLowKtXNTBypGqImE405J2565dvjafglHU) - Video tutorial series
- [74181 ALU Notes](https://tomnisbet.github.io/nqsap/docs/74181-alu-notes/) - Also see [Notes/hardware/74f181.md](../../Notes/hardware/74f181.md)
- [SAP-1 Architecture](https://en.wikipedia.org/wiki/Simple-As-Possible_computer) - Wikipedia article
- [project-ideas.md](../project-ideas.md) - Original project concept

## Related Projects

- [FPGA CPU Design](../fpga-cpu-design/) - Different project: custom CPU in SystemVerilog, not SAP-1
- [MM-8000K Trainer UI](../mm8000-trainer-ui/) - Physical Intel 8085 trainer used as reference for 8-bit architecture
- See [Notes/hardware/74-181/](../../Notes/hardware/74-181/) for 74181 ALU chip Digital simulator files

## Cross-References

- [Test Equipment/](../../Test%20Equipment/) - EEPROM and GAL programmers
- [Notes/hardware/74-181/](../../Notes/hardware/74-181/) - 74181 ALU research and simulation files
- [tools-and-components.md](../../tools-and-components.md) - 74-series logic chips inventory

---

*Last updated: 2026-01-07*
