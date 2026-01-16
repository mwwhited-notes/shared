# Vintage Computers Inventory

Personal collection of retro computers and systems spanning 1980s technology with documentation, peripherals, and emulation resources for preservation and research.

**Quick Reference:** 4 vintage systems | Apple II & TI-99/4A collections | [Documentation Protocol](../.claude/protocols/VINTAGE_COMPUTERS_DOCUMENTATION_PROTOCOL.md)

## Table of Contents

- [Quick Reference Summary](#quick-reference-summary)
- [Computer Index](#computer-index)
  - [Apple II Family](#apple-ii-family)
  - [Texas Instruments](#texas-instruments)
  - [Homebrew / Project PCBs](#homebrew--project-pcbs)
- [Directory Structure](#directory-structure)
- [Software Resources](#software-resources)
  - [Emulators](#emulators)
  - [Disk/Tape Images](#disktape-images)
  - [Development Tools](#development-tools)
- [Cross-References](#cross-references)
- [Notes](#notes)

---

## Quick Reference Summary

| System | Year | CPU | RAM | Quantity | Key Feature | Status |
|--------|------|-----|-----|----------|------------|--------|
| Apple IIc | 1984 | 65C02 @ 1 MHz | 128 KB | 1 | Compact all-in-one | Operational |
| Apple IIgs | 1986 | 65C816 @ 2.8 MHz | 256K-8MB | 1 | 16-bit with graphics | Operational |
| TI-99/4A | 1981 | TMS9900 @ 3 MHz | 16 KB | 1 | Speech synthesis support | Operational |
| NESMaker PCB | Modern | Custom | Varies | 2 | Homebrew NES cartridges | Blank |
| **TOTAL** | - | - | - | **4** | - | - |

---

## Computer Index

### Apple II Family

| System | Year | CPU | RAM | Storage | Git Hash | Directory |
|--------|------|-----|-----|---------|----------|-----------|
| [Apple IIc](apple-iic/) | 1984 | 65C02 @ 1.023 MHz | 128 KB | 5.25" floppy | xxxxxxx | `apple-iic/` |
| [Apple IIgs](apple-iigs/) | 1986 | 65C816 @ 2.8 MHz | 256 KB-8 MB | 3.5"/5.25" floppy | xxxxxxx | `apple-iigs/` |

### Texas Instruments

| System | Year | CPU | RAM | Storage | Git Hash | Directory |
|--------|------|-----|-----|---------|----------|-----------|
| [TI-99/4A](ti-99-4a/) | 1981 | TMS9900 @ 3.0 MHz | 16 KB | Cassette/Floppy | xxxxxxx | `ti-99-4a/` |

### Homebrew / Project PCBs

| Item | Platform | Purpose | Git Hash | Directory |
|------|----------|---------|----------|-----------|
| [NESMaker PCB](nesmaker-pcb/) | NES | Homebrew cartridge | xxxxxxx | `nesmaker-pcb/` |

---

## Directory Structure

```
├── readme.md                    # This file
├── apple-iic/
│   ├── README.md
│   ├── FloppyEmu_Instructions.pdf
│   └── FloppyEmu_QuickStart.pdf
├── apple-iigs/
│   ├── README.md
│   ├── FloppyEmu_Instructions.pdf
│   └── FloppyEmu_QuickStart.pdf
├── ti-99-4a/
│   └── README.md
└── nesmaker-pcb/
    └── README.md
```

---

## Software Resources

### Emulators

| System     | Emulator     | Platform       |
|------------|--------------|----------------|
| Apple II   | AppleWin     | Windows        |
| Apple II   | MAME         | Cross-platform |
| Apple IIgs | GSplus, KEGS | Cross-platform |
| TI-99/4A   | Classic99    | Windows        |
| TI-99/4A   | MAME         | Cross-platform |
| TI-99/4A   | JS99er       | Browser        |

### Disk/Tape Images

- **Archive.org** - Large collection of vintage software
- **Asimov** - Apple II software archive
- **WHT Tech** - TI-99/4A resources

### Development Tools

- **cc65** - C compiler for 6502 (Apple II)
- **Merlin32** - 65816 assembler (Apple IIgs)
- **xdt99** - TI-99/4A cross-development tools

---

## Notes

- See `Notes/TI-99_4a/` for additional TI-99/4A documentation and projects
- Vintage computer repairs may require period-correct components
- Capacitor replacement often needed on 30+ year old systems
- Use caution with original power supplies (age-related failures)
- Floppy Emu devices preserve 5.25" and 3.5" floppies for Apple II systems

---

## Cross-References

- [Programmable Devices/](../Programmable%20Devices/) - FPGA soft cores for emulating vintage CPUs (Multicomp EP2C5 supports Z80/6502/6809)
- [Test Equipment/](../Test%20Equipment/) - Equipment useful for vintage restoration (logic analyzers, power supplies for repaired systems)
- [Projects](../projects/) - Active vintage computing projects:
  - Apple II peripheral development
  - TI-99/4A speech synthesis experiments
  - NES cartridge development with NESMaker PCBs
- [Notes/](../Notes/) - Technical documentation organized by system

---

*Index Version: 1.0*
*Last Updated: 2026-01-16*
*Total Systems: 4 vintage computers*
*Scope: Apple II family, Texas Instruments computers, and homebrew computing platforms with peripherals and restoration documentation*
