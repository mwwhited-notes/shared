# Vintage Computers Inventory

Personal collection of vintage and retro computers with specifications, documentation links, and restoration notes.

Each system has its own directory with detailed specifications and locally archived documentation.

---

## Table of Contents

- [Vintage Computers Inventory](#vintage-computers-inventory)
  - [Table of Contents](#table-of-contents)
  - [Computer Index](#computer-index)
    - [Apple II Family](#apple-ii-family)
    - [Texas Instruments](#texas-instruments)
    - [Homebrew / Project PCBs](#homebrew--project-pcbs)
  - [Directory Structure](#directory-structure)
  - [Software Resources](#software-resources)
    - [Emulators](#emulators)
    - [Disk/Tape Images](#disktape-images)
    - [Development Tools](#development-tools)
  - [Notes](#notes)

---

## Computer Index

### Apple II Family

| System | Year | CPU | RAM | Storage | Directory |
|--------|------|-----|-----|---------|-----------|
| [Apple IIc](apple-iic/) | 1984 | 65C02 @ 1.023 MHz | 128 KB | 5.25" floppy | `apple-iic/` |
| [Apple IIgs](apple-iigs/) | 1986 | 65C816 @ 2.8 MHz | 256 KB-8 MB | 3.5"/5.25" floppy | `apple-iigs/` |

### Texas Instruments

| System | Year | CPU | RAM | Storage | Directory |
|--------|------|-----|-----|---------|-----------|
| [TI-99/4A](ti-99-4a/) | 1981 | TMS9900 @ 3.0 MHz | 16 KB | Cassette/Floppy | `ti-99-4a/` |

### Homebrew / Project PCBs

| Item | Platform | Purpose | Directory |
|------|----------|---------|-----------|
| [NESMaker PCB](nesmaker-pcb/) | NES | Homebrew cartridge | `nesmaker-pcb/` |

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

---

*Last updated: December 2025*
