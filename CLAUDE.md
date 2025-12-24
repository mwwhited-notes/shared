# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is Matt's personal notebook - a collection of notes, project ideas, scripts, and technical documentation covering embedded systems, electronics, retro computing, and software development.

## Key Directories

- **Programmable Devices/** - Inventory of FPGA, CPLD, MCU, and development boards with specifications and archived documentation
- **Expansion Boards/** - Inventory of Arduino shields, Raspberry Pi HATs, BeagleBone capes, and other dev board accessories
- **Test Equipment/** - Lab equipment documentation (oscilloscopes, DMMs, power supplies, programmers)
- **Notes/** - Technical notes on various topics (Kubernetes, dotnet, FPGA, vintage computing, etc.)
- **Scripts/** - Utility scripts (JavaScript, T-SQL, dotnet, Vivado TCL, WSL configuration)
- **HammingDistances/** - Precomputed Hamming distance lookup tables (CSV format)
- **AnalogComputers/** - Analog computing research repository (~232 PDFs, 660MB) covering fundamentals, aerospace simulation, vintage computer manuals, and application notes

## Documentation Protocols

### Programmable Devices
Follow `Programmable Devices/PROGRAMMABLE_DEVICES_DOCUMENTATION_PROTOCOL.md` when:
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
Follow `Expansion Boards/EXPANSION_BOARDS_DOCUMENTATION_PROTOCOL.md` when:
- Adding shields, HATs, capes, or other expansion modules
- Documenting pin mappings and compatibility with parent boards
- Cross-referencing with boards in `Programmable Devices/`

### Test Equipment
Follow `Test Equipment/EQUIPMENT_DOCUMENTATION_PROTOCOL.md` for lab equipment entries.

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

- `Programmable Devices/readme.md` - Device index with programmer compatibility
- `Expansion Boards/readme.md` - Shields, HATs, capes index with compatibility info
- `Test Equipment/readme.md` - Equipment index
- `AnalogComputers/analog-computing-repository/README.md` - Analog computing collection overview
- `AnalogComputers/analog-computing-repository/download-sources.md` - PDF source registry
- `links.md` - Curated reference links (AI/ML, dotnet, electronics, retro computing)
- `project-ideas.md` - Ongoing project list
