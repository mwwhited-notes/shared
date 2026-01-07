# Repository Restructure: Documentation Organization

Major documentation reorganization and project structure improvements completed in early January 2026.

## Summary

- **Date range:** 2026-01-01 to 2026-01-07
- **Total tasks completed:** 10
- **Key outcomes:**
  - Created project directories for all active projects
  - Reorganized Notes/ directory with hardware/software subdirectories
  - Consolidated scattered link files into unified links.md
  - Established cross-references between project-ideas.md and projects/
  - Improved documentation discoverability

## Completed Tasks

### Project Structure

- [x] Create project folders for all active projects
  - Created 9 project directories: fpga-cpu-design, sap-1-computer, zynq-soc-exploration, analog-computer-experiments, attiny2313-clock, mm8000-trainer-ui, scpi-instrument-control, home-automation, diy-trekpak-dividers
  - Each project has standardized README.md with status, equipment, and cross-references

- [x] Cross-reference project-ideas.md with projects/ directory
  - Added bidirectional links between backlog and active projects
  - Status indicators show which ideas are active vs. pending

### Notes Directory Reorganization

- [x] Reorganize Notes/ directory (hardware/, software/ subdirectories)
  - Created hardware/ subdirectory for FPGA, digital logic, 3D printer, FPAA topics
  - Created software/ subdirectory for AI/ML, dotnet, Kubernetes, diagrams, app ideas
  - Improved topic-based navigation

- [x] Create Notes/README.md
  - Added comprehensive index of all notes with descriptions
  - Organized by category (hardware, software, general)
  - Cross-referenced with related projects and equipment

### Link Consolidation

- [x] Consolidate link files into links.md
  - Merged scattered reference links into single curated file
  - Organized by category: AI/ML, dotnet, electronics, retro computing, vintage electronics
  - Removed duplicate entries

### Content Migration

- [x] Move TI-99/4A notes to Vintage Computers
  - Relocated notes to appropriate equipment inventory location
  - Maintained context with vintage computer collection

- [x] Move Analog Computing notes to projects/analog-computer-experiments
  - Integrated notes with active THAT (The Analog Thing) project
  - Cross-referenced with AnalogComputers/ research collection

- [x] Move SAP-1 notes to projects/sap-1-computer
  - Consolidated breadboard computer notes with project documentation
  - Added memory controller documentation and microcode files

### Documentation Updates

- [x] Update CLAUDE.md with new structure
  - Updated key directories section to reflect reorganization
  - Added references to new Notes/README.md structure
  - Maintained concise high-level overview

- [x] Add Digital Computer Electronics book to inventory
  - Added Malvino's book to tools-and-components.md (purchased 2020-01-09, $29.44)
  - Cross-referenced with SAP-1 computer project
  - Source of original SAP-1 architecture

## Files Changed

### Created
- `projects/fpga-cpu-design/README.md` - FPGA CPU project documentation
- `projects/sap-1-computer/README.md` - SAP-1 breadboard computer project
- `projects/zynq-soc-exploration/README.md` - Zynq SoC learning project
- `projects/analog-computer-experiments/README.md` - Analog computing with THAT
- `projects/attiny2313-clock/README.md` - ATtiny LED clock project
- `projects/mm8000-trainer-ui/README.md` - Intel 8085 trainer UI project
- `projects/scpi-instrument-control/README.md` - Test equipment automation
- `projects/home-automation/README.md` - HomeSeer to Home Assistant migration
- `projects/diy-trekpak-dividers/README.md` - Workshop organization project
- `projects/README.md` - Project index with quick reference table
- `Notes/README.md` - Technical notes index
- `links.md` - Consolidated reference links

### Modified
- `CLAUDE.md` - Updated structure references
- `tools-and-components.md` - Added Digital Computer Electronics book
- `projects/project-ideas.md` - Added cross-references to active projects

### Reorganized
- `Notes/hardware/` - Hardware-related notes (FPGA, digital logic, 3D printing, FPAA)
- `Notes/software/` - Software-related notes (AI/ML, dotnet, Kubernetes)

## Equipment Referenced

No new equipment added, but improved cross-referencing between:
- Projects and equipment inventories (Programmable Devices, Test Equipment, Vintage Computers)
- Active projects and related GitHub repositories
- Documentation and physical hardware

## Impact

### Improved Organization
- Clear separation between active projects and project ideas
- Topic-based notes navigation (hardware vs. software)
- Single source of truth for reference links

### Better Discoverability
- Projects/README.md provides quick overview of all active work
- Notes/README.md indexes all technical notes
- Cross-references enable easy navigation between related content

### Foundation for Future Work
- Standardized project structure enables consistent documentation
- Clear protocols for adding new equipment and projects
- Scalable organization as collection grows

## Next Steps

Moved back to TODO.md:
- [ ] Review and update workshop-capabilities.md with new projects
- [ ] Consider adding project status tracking to project-ideas.md
- [ ] Continue cataloging remaining equipment purchases
- [ ] Review amazon/aliexpress/mouser orders for inventory updates

---

*Archived: 2026-01-07*
