# Notes Directory

Complete index of technical notes, research materials, and reference documentation organized by topic including hardware electronics, software development, and miscellaneous reference.

**Quick Reference:** Hardware, Software, Hobbies | [Documentation Protocol](../.claude/protocols/INDEX_PROTOCOL.md)

## Table of Contents

- [Directory Structure](#directory-structure)
  - [Hardware Notes](#hardware-notes-hardware)
  - [Software Notes](#software-notes-software)
  - [Other Directories](#other-directories)
  - [Root Level Files](#root-level-files)
- [Related Documentation](#related-documentation)
- [When to Use Notes/](#when-to-use-notes)
- [Cross-References](#cross-references)

---

## Directory Structure

### Hardware Notes (`hardware/`)

Electronics, FPGA, and digital design notes:

- **Logic Tables/** - Digital logic reference tables (7-segment display, etc.)

**Moved to Projects:**
- **74-181/** → [SAP-1 Computer](../projects/sap-1-computer/reference-74181-alu/) - 74181 ALU chip research and Digital simulator files
- **74f181.md** → [SAP-1 Computer](../projects/sap-1-computer/reference-74181-alu/) - Link to 74181 ALU notes
- **3D Printer/** → K8200 pinout and power notes now live with the equipment itself in the
  Personal repository ([Test Equipment inventory](../.personal/incoming/test-equipment.md))
- **Field Programmable Analog Array/** → [Analog Computer Experiments](../projects/analog-computer-experiments/fpaa-research/) - FPAA research notes
- **Xilinx Native FIFO.md** → [FPGA CPU Design](../projects/fpga-cpu-design/xilinx-fifo-reference.md) - Xilinx FPGA FIFO implementation notes

### Software Notes (`software/`)

Software development, architecture, and DevOps notes:

- **App Ideas/** - Software project ideas and concepts
  - `New dotnet IOC Wrapper.md` - Dependency injection wrapper concept
  - `Road Trip App.md` - Road trip planning application
  - `Project Definition/` - Project definition tooling concepts

- **Build your own OCR/** - OCR implementation research
  - `design.md` - OCR system design notes

- **dotnet/** - .NET development notes
  - ASP.NET Core, Entity Framework, Azure DevOps
  - Git tips, NuGet packaging, MSBuild

**Moved to Top Level:**
- **DiagramsAndPatterns/** → [diagrams-and-patterns/](../diagrams-and-patterns/) - Software architecture patterns and templates library

**Moved to Projects:**
- **AI ML Stuff/** → [AI/ML Research](../projects/ai-ml-research/) - AI/ML research papers and notes (vector search files moved to [Vector Search SQL Server](../projects/vector-search-sqlserver/))
- **Kubernetes/** → [DevOps Playground Cluster](../projects/devops-playground-cluster/kubernetes-notes/) - Kubernetes and container orchestration notes

### Other Directories

- **Hobbies/** - Non-technical hobby notes
  - `Homebrew Beer.md` - Homebrewing notes
  - `Leather working.md` - Leathercraft notes

- **gadgets and gizmos/** - Miscellaneous gadget notes
  - `Automatic pet feeder.md` - Pet feeder operating instructions
  - `E6B - Flight Computer.md` - Flight computer notes
  - `KL-1 (Circular Slide Rule).md` - Circular slide rule notes

**Moved to Projects:**
- **Favero/** → [ScoreMachine - Favero protocol](../projects/scoremachine/favero-protocol.md) - Fencing timing equipment documentation
- **Duet3 - 3D Printer.md** → Duet 3 control board notes now live with the equipment itself in
  the Personal repository ([Test Equipment inventory](../.personal/incoming/test-equipment.md))
- **RadexOneReverseEngineerNotes.md** → [Radex One Protocol](../projects/radex-one-protocol-reverse-engineering/protocol-notes.md) - Geiger counter reverse engineering
- **NeTV.md** → NeTV FPGA video overlay device notes now live with the hardware itself in the
  Personal repository ([Programmable Devices inventory](../.personal/incoming/programmable-devices.md))

## Root Level Files

- **Design.vsdx** - Visio design diagrams
- **DocConversion.md** - Document conversion notes
- **Home Network.md** - Home network configuration notes
- **UsbDevices.reg** - Windows USB device registry exports
- **WSL Repair.md** - WSL troubleshooting notes
- **sqlclr notes.md** - SQL CLR integration notes

**Moved to Projects:**
- **Gadgets.md** → [projects/gadget-kit-ideas.md](../projects/gadget-kit-ideas.md) - Computer kits, test equipment builds, circuit ideas
- **Stream.md** → [projects/streaming-channel-planning.md](../projects/streaming-channel-planning.md) - YouTube/Twitch electronics/computer channel planning
- **HomeSeer-pi Backup.md** → [Home Automation](../projects/home-automation/homeseer-backup-notes.md) - HomeSeer backup procedures
- **Linux Serial.md** → [ScoreMachine](../projects/scoremachine/reference/favero/linux-serial-setup.md) - Linux serial port setup for scoring machine
- **UsbHidDecode.md** → [Radex One Protocol](../projects/radex-one-protocol-reverse-engineering/usb-hid-notes.md) - USB HID protocol decoding for Radex One

## Related Documentation

### Equipment & Projects

Equipment-specific notes have been moved to their respective directories:

- **TI-99/4A notes** → [Vintage Computers inventory](../.personal/incoming/vintage-computers.md)
- **Analog Computing notes** → [projects/analog-computer-experiments/notes/](../projects/analog-computer-experiments/notes/)
- **SAP-1 Computer** → [projects/sap-1-computer/](../projects/sap-1-computer/)

### Link Collections

- [links.md](../links.md) - Curated technical links (AI/ML, dotnet, electronics, retro computing, etc.)
  - Consolidated from `good reads.md`, `Vintage Stuff.md`, and `nerdy.md` (originals removed)

## When to Use Notes/

Add content to Notes/ when:
- Taking research notes on software or hardware topics
- Documenting technical concepts or learning
- Collecting reference materials not tied to specific equipment
- Storing miscellaneous technical documentation

**Don't add to Notes/ if:**
- It's equipment documentation → Use appropriate equipment directory (Test Equipment/, Programmable Devices/, etc.)
- It's an active project → Use projects/ directory
- It's just links → Add to [links.md](../links.md)
- It's component inventory → Use [tools-and-components.md](../.personal/incoming/tools-and-components.md)

## Cross-References

- [projects/](../projects/) - Active project documentation
- [diagrams-and-patterns/](../diagrams-and-patterns/) - Software architecture patterns and templates library
- [Test Equipment inventory](../.personal/incoming/test-equipment.md) - Lab equipment documentation
- [Programmable Devices inventory](../.personal/incoming/programmable-devices.md) - FPGA, MCU, dev boards
- [Vintage Computers inventory](../.personal/incoming/vintage-computers.md) - Retro computing hardware
- [tools-and-components.md](../.personal/incoming/tools-and-components.md) - Component inventory
- [links.md](../links.md) - Curated technical links

---

## Recent Reorganization

Many project-specific notes have been moved from Notes/ to their respective project directories for better organization:

- **SAP-1 Computer:** 74-181 ALU reference files
- **FPGA CPU Design:** Xilinx FIFO implementation notes
- **Analog Computer Experiments:** FPAA research
- **DevOps Playground Cluster:** Kubernetes notes
- **Home Automation:** HomeSeer backup procedures
- **Favero Fencing System:** Fencing equipment documentation
- **Radex One Protocol:** Geiger counter reverse engineering
- **Test Equipment (K8200):** 3D printer technical notes and Duet3 configuration

General reference notes (AI/ML research, dotnet development, app ideas) remain in Notes/ as they apply across multiple projects.

**DiagramsAndPatterns** has been promoted to a top-level directory as it's a comprehensive design patterns and architecture reference library.

---

*Index Version: 1.0*
*Last Updated: 2026-01-16*
*Scope: Technical notes and reference materials for hardware electronics, software development, architecture patterns, and miscellaneous technical documentation*
