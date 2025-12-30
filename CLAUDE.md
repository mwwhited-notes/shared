# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is Matt's personal notebook - a collection of notes, project ideas, scripts, and technical documentation covering embedded systems, electronics, retro computing, and software development.

## Owner Information

**GitHub:** [mwwhited](https://github.com/mwwhited)

**Organizations:**
- [OutOfBandDevelopment](https://github.com/OutOfBandDevelopment) - 1099 consulting organization (.NET libraries, build tools)
- [mwwhited-archives](https://github.com/mwwhited-archives) - Archived projects
- [mwwhited-notes](https://github.com/mwwhited-notes) - Documentation and notes (includes this repo)

**Key Repositories by Domain:**

*Embedded & Hardware:*
- [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery) - Arduino, AVR, ESP8266, STM32, FPGA (Arty A7/Z7, Cyclone II), CPLD, PAL, analog circuits
- [DeviceBridge](https://github.com/mwwhited/DeviceBridge) / [PrinterEmulator](https://github.com/mwwhited/PrinterEmulator) - TDS2024 IEEE-1284 parallel-to-USB capture
- [MM8000](https://github.com/mwwhited-archives/MM8000) - Intel 8085 trainer emulator (CLI + ANTLR assembler)
- [MyMashedDuet](https://github.com/mwwhited/MyMashedDuet) - Velleman K8200 3D printer Duet 3 config

*.NET Libraries & Tools (Out-of-Band Development):*
- [dotex](https://github.com/OutOfBandDevelopment/dotex) - .NET extensions framework
- [oobtainium](https://github.com/OutOfBandDevelopment/oobtainium) - Mocking framework
- [BuildFirstOnce](https://github.com/OutOfBandDevelopment/BuildFirstOnce) - MSBuild orchestration
- [RunScripts](https://github.com/OutOfBandDevelopment/RunScripts) - Docker wrapper scripts for dev tools

*Data & Encoding:*
- [BinaryDataDecoders](https://github.com/mwwhited/BinaryDataDecoders) - Encoding/decoding libraries (.NET)

**Skills/Experience:** FPGA (Xilinx, Intel/Altera), embedded systems (12+ platforms), protocol engineering (IEEE-1284, LANC, LXI, RS485, SCPI), .NET architecture, DevOps/build tooling, vintage computing (8085, Apple II, TI-99/4A), 3D printing

## Key Directories

- **Programmable Devices/** - Inventory of FPGA, CPLD, MCU, and development boards with specifications and archived documentation
- **Expansion Boards/** - Inventory of Arduino shields, Raspberry Pi HATs, BeagleBone capes, and other dev board accessories
- **Test Equipment/** - Lab equipment documentation (oscilloscopes, DMMs, power supplies, programmers, 3D printer)
- **Vintage Computers/** - Apple IIc, Apple IIgs, TI-99/4A with peripherals (Floppy Emu, VGA adapters, RAM expansions)
- **Camera Collection/** - Photography equipment inventory (Nikon D800, film cameras, lenses, M42 vintage glass)
- **Notes/** - Technical notes on various topics (Kubernetes, dotnet, FPGA, vintage computing, etc.)
- **Scripts/** - Utility scripts (JavaScript, T-SQL, dotnet, Vivado TCL, WSL configuration)
- **HammingDistances/** - Precomputed Hamming distance lookup tables (CSV format)
- **AnalogComputers/** - Analog computing research repository (~232 PDFs, 660MB) covering fundamentals, aerospace simulation, vintage computer manuals, and application notes
- **workshop-capabilities.md** - Workshop equipment summary, project ideas by difficulty/category, troubleshooting guides, wishlist

## Documentation Protocols

All protocols are located in `.claude/protocols/`.

### Programmable Devices
Follow `.claude/protocols/PROGRAMMABLE_DEVICES_DOCUMENTATION_PROTOCOL.md` when:
- Adding new development boards or microcontrollers
- Creating device README files with specifications
- Downloading and verifying datasheets/schematics
- Creating PlantUML block diagrams for device architecture

Key requirements:
- Each device gets its own directory with standardized README.md
- Download PDFs locally (datasheets, schematics, pinouts)
- Verify downloaded files are valid PDFs, not HTML error pages
- Include pinout images and text-based pinout tables
- Document both official tools and open-source alternatives (Arduino IDE, PlatformIO)

### Expansion Boards
Follow `.claude/protocols/EXPANSION_BOARDS_DOCUMENTATION_PROTOCOL.md` when:
- Adding shields, HATs, capes, or other expansion modules
- Documenting pin mappings and compatibility with parent boards
- Cross-referencing with boards in `Programmable Devices/`

### Test Equipment
Follow `.claude/protocols/EQUIPMENT_DOCUMENTATION_PROTOCOL.md` for lab equipment entries.

### Vintage Computers
Follow `.claude/protocols/VINTAGE_COMPUTERS_DOCUMENTATION_PROTOCOL.md` when:
- Adding vintage computer systems or peripherals
- Documenting accessories (Floppy Emu, RAM expansions, video adapters)
- Cross-referencing with related FPGA soft cores or emulation projects

### Online Shopping
Follow `.claude/protocols/ONLINE_SHOPPING_PROTOCOL.md` when:
- User mentions purchases from online sellers
- Documenting seller experiences (good or bad)
- Tracking pricing and shipping quality

### Camera Collection
Follow `.claude/protocols/CAMERA_COLLECTION_PROTOCOL.md` when:
- Adding camera bodies (digital or film)
- Documenting lenses, teleconverters, and accessories
- Tracking lens mount compatibility
- Cross-referencing with purchase info in ShoppingOnline.md

### Analog Computers
Reference `AnalogComputers/analog-computing-repository/CLAUDE.md` for the analog computing research collection.

Repository structure:
- `01-fundamentals/` through `08-references/` - Organized learning materials
- `09-datasheets/pdfs/` - Component datasheets
- `10-application-notes/pdfs/` - 159 PDFs (ADI, TI, ALPACA, biomedical, etc.)
- `11-aerospace-simulation/pdfs/` - 53 PDFs (Apollo, fire control, hybrid computing)
- `12-analog-computer-docs/` - 21 vintage computer manuals (EAI, Heathkit, Comdyna)

Key files:
- `download-sources.md` - Registry of all download sources (NASA NTRS, Bitsavers, Archive.org, etc.)
- `research-protocol.md` - Search strategies by topic

File naming: lowercase with hyphens, source prefix (`ntrs-`, `dtic-`, `adi-`, `ti-`, etc.)

Quality checks:
```bash
file *.pdf          # Verify actual PDF format
ls -lh *.pdf        # Files > 1KB (tiny = failed download)
```

## File Naming Conventions

- Device directories: lowercase with hyphens (`arduino-uno`, `digilent-arty-a7-100`)
- Expansion board directories: platform prefix + name (`arduino-motor-shield`, `rpi-sense-hat`, `bbb-relay-cape`)
- Datasheets: `<Chip>_Datasheet.pdf`
- Schematics: `<Board>_Schematic.pdf`
- Pinouts: `<Board>_Pinout.png`

## Common Tasks

### Verify Downloaded PDFs
```bash
file *.pdf  # Should show "PDF document", not "HTML"
ls -lh *.pdf  # Datasheets typically > 100KB
```

### Check for Missing README Files
```bash
for dir in */; do
  if [ ! -f "$dir/README.md" ]; then
    echo "No README: $dir"
  fi
done
```

## Cross-References

- `workshop-capabilities.md` - **Main workshop reference** with equipment summary, project ideas, troubleshooting guides
- `Programmable Devices/readme.md` - Device index with programmer compatibility
- `Expansion Boards/readme.md` - Shields, HATs, capes index with compatibility info
- `Test Equipment/readme.md` - Equipment index (oscilloscopes, DMMs, programmers, 3D printer)
- `Vintage Computers/readme.md` - Apple IIc, Apple IIgs, TI-99/4A inventory
- `Camera Collection/readme.md` - Cameras, lenses, and photography accessories
- `AnalogComputers/analog-computing-repository/README.md` - Analog computing collection overview
- `AnalogComputers/analog-computing-repository/research-protocol.md` - Search strategies and download sources by topic
- `AnalogComputers/analog-computing-repository/download-sources.md` - PDF source registry
- `links.md` - Curated reference links (AI/ML, dotnet, electronics, retro computing)
- `project-ideas.md` - Ongoing project list

## Notable Hardware

Key equipment that connects to GitHub projects:
- **TDS2024 Oscilloscope** - Target hardware for [DeviceBridge](https://github.com/mwwhited/DeviceBridge) IEEE-1284 capture project
- **MM-8000K Trainer** - Physical Intel 8085 trainer with [MM8000 emulator](https://github.com/mwwhited-archives/MM8000)
- **Velleman K8200** - 3D printer with Duet 3 upgrade, config at [MyMashedDuet](https://github.com/mwwhited/MyMashedDuet)
- **Arty A7-100 / Arty Z7-20** - FPGA boards used in [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery) projects
- **Gigatron TTL** - TTL computer kit (7400-series, no microprocessor)
- **Multicomp EP2C5-DB** - FPGA retro computing kit (Z80/6502/6809)
