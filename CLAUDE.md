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

- **Personal/** - Personal equipment collections and purchase history (moved to standalone structure)
  - **Personal/Programmable Devices/** - FPGA, CPLD, MCU, development boards
  - **Personal/Expansion Boards/** - Arduino shields, Pi HATs, BeagleBone capes
  - **Personal/Test Equipment/** - Lab equipment (oscilloscopes, DMMs, power supplies, programmers)
  - **Personal/Vintage Computers/** - Apple IIc, IIgs, TI-99/4A with peripherals
  - **Personal/Camera Collection/** - Photography equipment (cameras, lenses, M42 vintage glass)
  - **Personal/Device Lab/** - Computing devices for hacking (tablets, phones, gaming, NAS)
  - **Personal/Hobby Collection/** - Hobby and craft equipment (leathercraft, sewing, jewelry)
  - **Personal/Sports Collection/** - Sports and outdoor recreation equipment
  - **Personal/.invoices/** - Purchase invoices from Amazon and AliExpress (2017-2026)
- **projects/** - Active project documentation and build logs
  - `fpga-cpu-design/` - Custom CPU in SystemVerilog
  - `attiny2313-clock/` - ATtiny LED clock
  - `scpi-instrument-control/` - Test equipment automation
  - `analog-computer-experiments/` - Anabrid THAT projects
  - `mm8000-trainer-ui/` - Intel 8085 trainer interface
  - `zynq-soc-exploration/` - Xilinx Zynq ARM+FPGA SoC
  - `sap-1-computer/` - SAP-1/Ben Eater 8-bit breadboard computer
  - `diy-trekpak-dividers/` - Workshop organization
  - `home-automation/` - Home Assistant migration
  - `synchronized-telemetry-streaming-research/` - **Research:** RFCs, standards, protocols for synchronized telemetry and blob transfer (40+ standards documented)
- **network-diagram.md** - Home network topology, IP assignments, VLAN planning, and security notes
- **projects/project-ideas.md** - Project backlog and ideas (references detailed docs in `projects/`)
- **DiagramsAndPatterns/** - Software architecture patterns and templates library
  - Design patterns (behavioral, creational, structural, etc.)
  - Architecture patterns (data access, presentation, service)
  - Example designs (OAuth2, web search engine)
  - Templates (architecture docs, test strategies, deployment plans)
- **Notes/** - Technical notes organized by topic (see Notes/README.md)
  - `hardware/` - Logic tables, reference materials
  - `software/` - AI/ML, dotnet, app ideas
- **Scripts/** - Utility scripts (JavaScript, T-SQL, dotnet, Vivado TCL, WSL configuration)
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

### Online Shopping & Invoice Processing
Invoice processing and purchase history tracking now happens in **Personal/** folder.

See `Personal/CLAUDE.md` and `Personal/.claude/protocols/ONLINE_SHOPPING_PROTOCOL.md` when:
- Processing purchases from online retailers
- Documenting seller experiences and reliability
- Tracking pricing, shipping quality, and purchase history
- Adding items to Personal/.invoices/ archives

### Camera Collection
For camera collections documentation, see Personal folder:
- Personal/Camera Collection/ - Photography equipment inventory
- Personal/ShoppingOnline.md - Seller notes and purchase history
- Personal/.invoices/ - Purchase invoices

### Personal Collections
Follow appropriate protocol when adding items to Personal/ folder collections:

#### Device Lab
Follow `.claude/protocols/DEVICE_LAB_PROTOCOL.md` when:
- Adding computing devices (tablets, phones, gaming handhelds, NAS, desktops)
- Documenting hackability (root, jailbreak, custom firmware options)
- Tracking devices for tinkering and repurposing projects
- Cross-referencing with home-automation and other projects

#### Hobby Collection
Follow `.claude/protocols/HOBBY_COLLECTION_PROTOCOL.md` when:
- Adding hobby and craft equipment (leathercraft, sewing, jewelry making)
- Documenting materials and supplies inventory
- Tracking project ideas and inspiration
- Cross-referencing with related creative projects

#### Sports Collection
Follow `.claude/protocols/SPORTS_COLLECTION_PROTOCOL.md` when:
- Adding sports and outdoor recreation equipment (water sports, biking, camping, fitness)
- Documenting maintenance and service history
- Planning trips and adventures
- Cross-referencing with outdoor projects

### Projects
Follow `.claude/protocols/PROJECTS_PROTOCOL.md` when:
- Creating documentation for a new project build
- Documenting an active project that spans multiple sessions
- Moving a project idea from `project-ideas.md` to active implementation
- Creating build logs, parts lists, or progress tracking
- **For research projects:** Follow research protocol below

Key requirements:
- Each project gets its own directory in `projects/`
- README.md with overview, materials, build steps, and status
- Optional build-log.md for session-by-session progress
- Optional parts-list.md for detailed BOM
- Cross-reference to/from project-ideas.md and equipment inventories

### Research Projects (New Protocol)
Follow this when creating comprehensive research/standards documentation:
- Document RFCs, IEEE standards, and CNCF specifications
- Create comparison matrices (technology selection guides)
- Build comprehensive bibliography with 100+ resources
- Cross-reference to related projects in repository
- Include practical implementation guides and use case scenarios
- Download primary standards documents (PDF) to `documents/` folder
- Create index/navigation document for easy access
- Include academic papers and foundational research citations

**Recent example:** `projects/synchronized-telemetry-streaming-research/`
- 5 documentation files (3000+ lines)
- 40+ standards catalogued with RFCs and links
- 8 repository projects cross-referenced
- 100+ implementation resources indexed
- Quick-start guides for 4 common scenarios

### Tools and Components (In Personal Folder)
See `Personal/.claude/protocols/TOOLS_AND_COMPONENTS_PROTOCOL.md` when:
- Adding components or tools from invoices
- Processing Amazon/AliExpress orders for tools, wire, components
- Organizing component stock in Personal collections
- Cross-referencing with Personal equipment inventories

**Note:** Tools and components processing is now part of Personal/ invoice workflow. See `Personal/CLAUDE.md` for details.

### Project Review
Follow `.claude/protocols/PROJECT_REVIEW_PROTOCOL.md` when:
- Reviewing repository inventory for consistency
- Updating `workshop-capabilities.md` with new equipment or projects
- Updating `project-ideas.md` with new project ideas
- Performing periodic maintenance on project documentation
- Syncing project files after adding new equipment

Key features:
- Full review workflow for quarterly maintenance
- Quick sync workflow after adding equipment
- Cross-reference verification between inventory and project files
- Project idea generation based on equipment combinations

### Maintenance & Performance
Follow `.claude/protocols/CLAUDE_MD_MAINTENANCE_PROTOCOL.md` to keep this file concise.
Follow `.claude/protocols/TODO_MD_ARCHIVAL_PROTOCOL.md` to archive completed tasks from TODO.md.

**Current status:**
- CLAUDE.md: Root file (target <500 lines, warning at 600)
- TODO.md: Root file with repository-wide tasks
- Personal/: Standalone folder with all collections and protocols
  - Personal/CLAUDE.md - Personal repository configuration
  - Personal/TODO.md - Personal collection task tracking
  - Personal/README.md - Personal collections main index
  - Personal/.claude/protocols/ - 10 documentation protocols for collections
- All equipment collections moved to Personal/ (ready for separate repository)
- See `changes/` directory for archived work

### Directory Indexes for Performance & Token Usage

Each major directory has a focused README.md index following `.claude/protocols/INDEX_PROTOCOL.md`. These serve dual purposes:

**Performance Benefits:**
- Indexes provide a quick reference without loading entire directory contents into context
- Each index includes git hashes enabling targeted `git diff` review (avoids reviewing unrelated changes)
- Structured table format with quick-reference summaries reduces context bloat

**Index Organization:**
- `projects/README.md` - Master index of 21+ projects (status, categories, cross-references)
- `.claude/protocols/README.md` - Master index of 19 documentation protocols (versions, purposes, decision tree)
- `Personal/README.md` - Main index for all personal equipment collections
- `Personal/Programmable Devices/README.md` - Dev boards inventory
- `Personal/Expansion Boards/README.md` - Shields, HATs, capes
- `Personal/Test Equipment/README.md` - Lab equipment inventory
- `Personal/Vintage Computers/README.md` - Vintage systems
- `Personal/Camera Collection/README.md` - Photography equipment
- `Personal/Device Lab/README.md` - Computing devices for hacking
- `Personal/Hobby Collection/README.md` - Hobby and craft equipment
- `Personal/Sports Collection/README.md` - Sports and recreation equipment
- `Notes/README.md` - Technical notes directory guide
- `AnalogComputers/README.md` - Analog computing research collection overview

**Key Principle:** When needing information about items in a collection, read the focused index first before drilling into individual item documentation.

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

### Main Reference Files
- `workshop-capabilities.md` - **Main workshop reference** with equipment summary, project ideas, troubleshooting guides
- `projects/project-ideas.md` - Ongoing project backlog with cross-references to active projects
- `links.md` - Curated reference links (AI/ML, dotnet, electronics, retro computing, vintage electronics)

### Personal Equipment & Purchase Collections

All personal equipment collections and purchase history have been moved to `Personal/` folder for standalone repository:

**Personal Collections:**
- `Personal/readme.md` - Main index for Personal collections
- `Personal/CLAUDE.md` - Configuration for Personal repository
- `Personal/TODO.md` - Task tracking for Personal collections
- `Personal/Programmable Devices/readme.md` - Dev boards (FPGA, CPLD, MCU)
- `Personal/Expansion Boards/readme.md` - Shields, HATs, capes
- `Personal/Test Equipment/readme.md` - Lab equipment
- `Personal/Vintage Computers/readme.md` - Vintage computer systems
- `Personal/Camera Collection/readme.md` - Photography equipment
- `Personal/Device Lab/readme.md` - Computing devices for hacking
- `Personal/Hobby Collection/readme.md` - Hobby and craft equipment
- `Personal/Sports Collection/readme.md` - Sports and recreation equipment

**Personal Purchase & Inventory Records:**
- `Personal/.invoices/` - Purchase history archives (Amazon, AliExpress)
- `Personal/tools-and-components.md` - Hand tools, wire, consumables, component stock
- `Personal/ShoppingOnline.md` - Seller notes and online shopping experience tracking
- `Personal/Restaurants.md` - Personal restaurant and local dining recommendations

### Projects
- `projects/` - Active project directories with READMEs (see projects/project-ideas.md for complete list)
- `home-automation/CLAUDE.md` - Home automation project (HomeSeer to Home Assistant migration)
- `network-diagram.md` - Network topology and IP assignments

### Research Collections
- `AnalogComputers/analog-computing-repository/README.md` - Analog computing collection overview
- `AnalogComputers/analog-computing-repository/research-protocol.md` - Search strategies and download sources by topic
- `AnalogComputers/analog-computing-repository/download-sources.md` - PDF source registry
- `projects/synchronized-telemetry-streaming-research/` - RFC and standards research (40+ standards, 100+ implementation resources)
  - `RESEARCH_BIBLIOGRAPHY.md` - Comprehensive RFC/standard catalog with cross-references
  - `event-streaming-and-blob-transfer.md` - CloudEvents, Kafka, S3, BitTorrent, IPFS standards
  - `out-of-order-blob-transfer.md` - RaptorQ (RFC 6330), FECFRAME, QUIC, SCTP protocols
  - `documents/` - Downloaded RFC and standards PDFs (8 files, 1.1 MB)
- `Notes/README.md` - Technical notes directory guide

## Notable Hardware

Key equipment that connects to GitHub projects:
- **TDS2024 Oscilloscope** - Target hardware for [DeviceBridge](https://github.com/mwwhited/DeviceBridge) IEEE-1284 capture project
- **MM-8000K Trainer** - Physical Intel 8085 trainer with [MM8000 emulator](https://github.com/mwwhited-archives/MM8000)
- **Velleman K8200** - 3D printer with Duet 3 upgrade, config at [MyMashedDuet](https://github.com/mwwhited/MyMashedDuet)
- **Arty A7-100 / Arty Z7-20** - FPGA boards used in [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery) projects
- **Gigatron TTL** - TTL computer kit (7400-series, no microprocessor)
- **Multicomp EP2C5-DB** - FPGA retro computing kit (Z80/6502/6809)
