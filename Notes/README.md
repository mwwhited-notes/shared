# Notes Directory

Technical notes, research, and reference materials organized by topic.

## Directory Structure

### Hardware Notes (`hardware/`)

Electronics, FPGA, and digital design notes:

- **74-181/** - 74181 ALU chip research and Digital simulator files
  - `74-181.dig`, `ALU181.dig` - Digital logic simulations
  - Related to [SAP-1 Computer project](../projects/sap-1-computer/)

- **74f181.md** - Link to 74181 ALU notes (https://tomnisbet.github.io/nqsap/docs/74181-alu-notes/)

- **3D Printer/** - Velleman K8200 3D printer technical notes
  - `3d printer pinout.xlsx` - Connector pinouts
  - `3dprinter power.xlsx` - Power distribution
  - See [Test Equipment/](../Test%20Equipment/) for full K8200 documentation

- **Field Programmable Analog Array/** - FPAA research notes
  - Anadigm/Lattice FPAA technology

- **Logic Tables/** - Digital logic reference tables

- **Xilinx Native FIFO.md** - Xilinx FPGA FIFO implementation notes

### Software Notes (`software/`)

Software development, architecture, and DevOps notes:

- **AI ML Stuff/** - Machine learning and AI resources
  - `AI ML Papers.md` - Research papers
  - `ai notes.md` - ML concepts and notes
  - `Anti-AI.md` - AI skepticism and limitations
  - `LocalitySensitiveHashing.md` - LSH algorithms
  - `vectorsearch.md` - Vector search techniques

- **App Ideas/** - Software project ideas and concepts
  - `New dotnet IOC Wrapper.md` - Dependency injection wrapper concept
  - `Road Trip App.md` - Road trip planning application
  - `Project Definition/` - Project definition tooling concepts

- **Build your own OCR/** - OCR implementation research
  - `design.md` - OCR system design notes

- **DiagramsAndPatterns/** - Software architecture patterns and templates
  - `ArchitecturePatterns/` - Data access, presentation, service patterns
  - `DesignPatterns/` - Behavioral, creational, structural patterns
  - `Designs/` - OAuth2, web search engine designs
  - `Examples/` - PlantUML diagrams, OCL examples
  - `Templates/` - Architecture docs, test strategies, deployment plans
  - `README.md` - Pattern library overview

- **dotnet/** - .NET development notes
  - ASP.NET Core, Entity Framework, Azure DevOps
  - Git tips, NuGet packaging, MSBuild

- **Kubernetes/** - Kubernetes and container orchestration notes

### Other Directories

- **Favero/** - Fencing timing equipment documentation
  - `notes.md` - Favero timing system notes
  - `opto-rs232interf1.pdf` - RS-232 interface documentation
  - `Fencing.vsdx` - Fencing setup diagrams

- **Hobbies/** - Non-technical hobby notes
  - `Homebrew Beer.md` - Homebrewing notes
  - `Leather working.md` - Leathercraft notes

- **gadgets and gizmos/** - Miscellaneous gadget notes
  - `Automatic pet feeder.md`
  - `Duet3 - 3D Printer.md` - Duet 3 control board notes
  - `E6B - Flight Computer.md`
  - `KL-1 (Circular Slide Rule).md`
  - `NeTV.md` - NeTV FPGA video board
  - `RadexOneReverseEngineerNotes.md` - Geiger counter reverse engineering

## Root Level Files

- **Design.vsdx** - Visio design diagrams
- **DocConversion.md** - Document conversion notes
- **Gadgets.md** - Gadget links and ideas
- **Home Network.md** - Home network configuration notes
- **HomeSeer-pi Backup.md** - HomeSeer backup procedures (now using Home Assistant)
- **Linux Serial.md** - Linux serial port configuration
- **Stream.md** - Streaming notes
- **UsbDevices.reg** - Windows USB device registry exports
- **UsbHidDecode.md** - USB HID protocol decoding
- **WSL Repair.md** - WSL troubleshooting notes
- **sqlclr notes.md** - SQL CLR integration notes

## Related Documentation

### Equipment & Projects

Equipment-specific notes have been moved to their respective directories:

- **TI-99/4A notes** → [Vintage Computers/ti-99-4a/notes/](../Vintage%20Computers/ti-99-4a/notes/)
- **Analog Computing notes** → [projects/analog-computer-experiments/notes/](../projects/analog-computer-experiments/notes/)
- **SAP-1 Computer** → [projects/sap-1-computer/](../projects/sap-1-computer/)

### Link Collections

- [links.md](../links.md) - Curated technical links (AI/ML, dotnet, electronics, retro computing, etc.)
  - Consolidated from `good reads.md`, `Vintage Stuff.md`, and `nerdy.md`

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
- It's component inventory → Use [tools-and-components.md](../tools-and-components.md)

## Cross-References

- [projects/](../projects/) - Active project documentation
- [Test Equipment/](../Test%20Equipment/) - Lab equipment documentation
- [Programmable Devices/](../Programmable%20Devices/) - FPGA, MCU, dev boards
- [Vintage Computers/](../Vintage%20Computers/) - Retro computing hardware
- [tools-and-components.md](../tools-and-components.md) - Component inventory
- [links.md](../links.md) - Curated technical links

---

*Last updated: January 2026*
