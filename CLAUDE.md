# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is Matt's personal notebook - a collection of notes, project ideas, scripts, and technical documentation covering embedded systems, electronics, retro computing, and software development.

## Key Directories

- **Programmable Devices/** - Inventory of FPGA, CPLD, MCU, and development boards with specifications and archived documentation
- **Test Equipment/** - Lab equipment documentation (oscilloscopes, DMMs, power supplies, programmers)
- **Notes/** - Technical notes on various topics (Kubernetes, dotnet, FPGA, vintage computing, etc.)
- **Scripts/** - Utility scripts (JavaScript, T-SQL, dotnet, Vivado TCL, WSL configuration)
- **HammingDistances/** - Precomputed Hamming distance lookup tables (CSV format)

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

### Test Equipment
Follow `Test Equipment/EQUIPMENT_DOCUMENTATION_PROTOCOL.md` for lab equipment entries.

## File Naming Conventions

- Device directories: lowercase with hyphens (`arduino-uno`, `digilent-arty-a7-100`)
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
- `Test Equipment/readme.md` - Equipment index
- `links.md` - Curated reference links (AI/ML, dotnet, electronics, retro computing)
- `project-ideas.md` - Ongoing project list
