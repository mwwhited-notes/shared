# MM-8000K Intel 8085 Trainer UI

Modern user interface for the MM-8000K Intel 8085 trainer with emulator integration.

## Overview

This project develops a modern user interface for the MM-8000K Intel 8085 microprocessor trainer. The trainer is a vintage educational computer used for learning 8085 assembly programming and hardware interfacing.

The project combines physical hardware (MM-8000K trainer) with software emulation (MM8000 emulator on GitHub) to provide both hands-on learning and convenient development/debugging.

## Project Status

**Status:** On Hold / Reference Hardware

**Completed:**
- MM-8000K hardware trainer acquired and working
- [MM8000 emulator](https://github.com/mwwhited-archives/MM8000) implemented (CLI + ANTLR assembler)

**Current Use:**
- Physical MM-8000K trainer used as reference for SAP-1 computer project
- Hardware available for experimentation with 8085 architecture
- Emulator repository archived and functional as-is

**UI Development:** Not planned at this time - emulator CLI is functional and hardware trainer meets current needs

## Equipment Used

- **[MM-8000K Intel 8085 Trainer](../../.personal/incoming/vintage-computers.md)** - Physical hardware trainer
- Development workstation for UI and emulator work
- **[Logic analyzer](../../.personal/incoming/test-equipment.md)** - For hardware debugging (if needed)

## Architecture

```
┌─────────────────────────────────────┐
│     Modern UI (Desktop/Web)         │
│  - Memory viewer                    │
│  - Register display                 │
│  - Assembler w/ syntax highlighting │
│  - Debugger controls                │
└─────────────────┬───────────────────┘
                  │
    ┌─────────────┴──────────────┐
    │                            │
┌───▼─────────────┐   ┌──────────▼──────────┐
│  MM8000 Emulator│   │ MM-8000K Hardware   │
│  (.NET Core)    │   │ (Optional Interface)│
└─────────────────┘   └─────────────────────┘
```

## Related Projects

- [MM8000 Emulator Repository](https://github.com/mwwhited-archives/MM8000) - Existing CLI emulator
- [8085 soft core on FPGA](../../project-ideas.md) - Future FPGA implementation
- [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery) - Related embedded systems work

## Learning Goals

- Deep understanding of 8085 architecture and instruction set
- Desktop/web application development
- Emulator enhancement and debugging
- Reverse engineering and documentation of vintage hardware

## Technology Stack

- **Emulator:** .NET Core, ANTLR (assembler parser)
- **UI Options:** WPF (desktop), Blazor/ASP.NET Core (web), or Electron
- **Communication:** Serial/parallel (if implementing hardware interface)

## References

- MM-8000K trainer documentation
- Intel 8085 datasheet and programming manual
- [MM8000 GitHub repository](https://github.com/mwwhited-archives/MM8000)
- [project-ideas.md](../project-ideas.md) - Original project concept

---

*Last updated: 2026-01-07*
