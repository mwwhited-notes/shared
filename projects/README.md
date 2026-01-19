# Projects Index

Active project documentation and build logs organized by category.

**See also:** [project-ideas.md](project-ideas.md) - Project backlog and future ideas

## Quick Reference

| Project | Category | Status | Equipment |
|---------|----------|--------|-----------|
| [FPGA CPU Design](#fpga-cpu-design) | Digital Logic | In Progress | [Arty A7-100](../.personal/incoming/programmable-devices.md) |
| [SAP-1 Computer](#sap-1-computer) | Digital Logic | In Progress | [74-series, breadboards](../.personal/incoming/tools-and-components.md) |
| [DRL/DTL Logic Boards](#drldtl-logic-boards) | Digital Logic | Reference | [Diodes, transistors](../.personal/incoming/tools-and-components.md) |
| [Zynq SoC Exploration](#zynq-soc-exploration) | SoC/Embedded | In Progress | [Arty Z7-20](../.personal/incoming/programmable-devices.md) |
| [Analog Computer Experiments](#analog-computer-experiments) | Analog Computing | In Progress | [THAT](../.personal/incoming/test-equipment.md) |
| [ATtiny2313 LED Clock](#attiny2313-led-clock) | Microcontrollers | Completed | [ATtiny2313](../.personal/incoming/programmable-devices.md) |
| [MM-8000K Trainer UI](#mm-8000k-intel-8085-trainer-ui) | Retro Computing | On Hold | [MM-8000K](../.personal/incoming/vintage-computers.md) |
| [Apple II Disk Archival](#apple-ii-disk-archival) | Retro Computing | Active | [Greaseweazle V4.1](../.personal/incoming/test-equipment.md), Epson SD-800 |
| [Passive Radar SDR](#passive-radar-sdr-system) | RF/SDR | Planning | [KrakenSDR/RTL-SDR](../.personal/incoming/programmable-devices.md) |
| [Radex One Protocol](#radex-one-geiger-counter-protocol) | Protocol Reverse Eng | Completed | [Radex One](../.personal/incoming/device-lab.md) |
| [Favero Fencing System](#favero-fencing-scoring-system) | Protocol Integration | Completed | Favero Full-Arm-05 |
| [ImageWriter II Emulator](#imagewriter-ii-emulator) | Protocol Integration | Planning | Serial cable, [Apple IIc](../.personal/incoming/vintage-computers.md) |
| [SCPI Instrument Control](#scpi-instrument-control) | Test Automation | Planning | [Lab equipment](../.personal/incoming/test-equipment.md) |
| [Vector Search SQL Server](#vector-search-in-sql-server) | Database/ML | Completed | SQL Server, .NET |
| [AI/ML Research](#aiml-research--reference) | Research/Reference | Reference | [Technical books](../.personal/incoming/books.md) |
| [Self-Hosted Git Server](#self-hosted-git-server) | DevOps/Infrastructure | Planning | [PR4100 NAS](../.personal/incoming/device-lab.md) |
| [SBC Cluster](#sbc-cluster-arm) | DevOps/Infrastructure | Planning | [ARM SBCs](../.personal/incoming/device-lab.md) |
| [DevOps Playground Cluster](#devops-playground-cluster) | DevOps/HPC | In Progress | [FX-9590, FX-8350](../.personal/incoming/device-lab.md) |
| [Home Automation](#home-automation) | Smart Home | In Progress | [Pi 3, Z-Wave](../.personal/incoming/device-lab.md) |
| [DIY TrekPak Dividers](#diy-trekpak-dividers) | Workshop | Reference | Foam, pins |
| [Cline with Local LLM](#cline-with-local-llm) | AI / Dev Tools | Planning | [RTX 4070 Ti](../.personal/incoming/device-lab.md) |
| [HuggingFace .NET Native](#huggingface-dotnet-native-execution) | AI/ML Research | Research | .NET workstation |
| [Local Docker Registry](#local-docker-registry) | DevOps / Infrastructure | Planning | [NAS/Cluster](../.personal/incoming/device-lab.md) |

## Projects by Category

### Digital Logic & FPGA

#### FPGA CPU Design
**Status:** In Progress
**Directory:** [fpga-cpu-design/](fpga-cpu-design/)

Custom CPU architecture designed from scratch in SystemVerilog for FPGA implementation on the Digilent Arty A7-100. Learning computer architecture fundamentals, SystemVerilog HDL, and FPGA resource optimization.

**Equipment:** Arty A7-100, Vivado
**Related:** [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery)

---

#### SAP-1 Computer
**Status:** In Progress
**Directory:** [sap-1-computer/](sap-1-computer/)

Building the SAP-1 (Simple As Possible) 8-bit breadboard computer based on Ben Eater's design. Uses discrete 74-series TTL logic chips, AT28C16 EEPROMs for microcode, and ATF16v8b GAL chips for memory control.

**Equipment:** 74-series logic, breadboards, EEPROM/GAL programmers
**Related:** Digital Computer Electronics (Malvino), [Ben Eater's videos](https://www.youtube.com/playlist?list=PLowKtXNTBypGqImE405J2565dvjafglHU)

---

#### DRL/DTL Logic Boards
**Status:** Reference/As Needed
**Directory:** [drl-dtl-logic-boards/](drl-dtl-logic-boards/)

Educational logic boards demonstrating digital gates using discrete components (Diode-Resistor Logic and Diode-Transistor Logic) rather than integrated circuits. Shows fundamental gate operation before 74-series TTL chips. Useful reference for understanding logic family evolution and teaching digital fundamentals.

**Equipment:** Diodes, resistors, transistors (2N2222/2N3904), breadboards
**Related:** SAP-1 Computer, [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery) (may contain additional notes)
**Educational Value:** Understanding what's inside TTL ICs, logic family history (DRL→DTL→TTL→CMOS)

---

### System-on-Chip & Embedded

#### Zynq SoC Exploration
**Status:** In Progress - Initial Learning
**Directory:** [zynq-soc-exploration/](zynq-soc-exploration/)

Exploring Xilinx Zynq architecture combining ARM Cortex-A9 processors with FPGA fabric. Learning AXI bus interfacing, custom hardware accelerators, embedded Linux, and hardware-software co-design.

**Equipment:** Arty Z7-20, Vivado + Vitis
**Related:** FPGA CPU Design project

---

#### ATtiny2313 LED Clock
**Status:** Completed
**Directory:** [attiny2313-clock/](attiny2313-clock/)

Functional LED clock using ATtiny2313 microcontroller. Successfully implemented ISP programming, timekeeping firmware, and LED display driving. Future enhancement opportunity: implement CPU sleep modes for improved battery life.

**Equipment:** ATtiny2313, LED display, ISP programmer, KSGER T12 soldering station
**Outcome:** Working clock with accurate timekeeping

---

### Analog Computing

#### Analog Computer Experiments
**Status:** In Progress - Learning Phase
**Directory:** [analog-computer-experiments/](analog-computer-experiments/)

Exploring analog computing fundamentals with Anabrid's "The Analog Thing" (THAT). Planned experiments include Lorenz attractor visualization, predator-prey modeling, and hybrid analog-digital systems with STM32.

**Equipment:** THAT analog computer, oscilloscope, STM32 boards
**Research:** [AnalogComputers/analog-computing-repository/](../AnalogComputers/analog-computing-repository/) - 232 PDFs, 660MB collection

---

### Retro Computing

#### MM-8000K Intel 8085 Trainer UI
**Status:** On Hold
**Directory:** [mm8000-trainer-ui/](mm8000-trainer-ui/)

Physical MM-8000K Intel 8085 trainer hardware available and functional. CLI emulator exists on GitHub. UI development not currently planned. Hardware primarily serves as reference for SAP-1 computer project and 8085 architecture experimentation.

**Equipment:** MM-8000K trainer (built and working), development workstation
**Related:** [MM8000 Emulator](https://github.com/mwwhited-archives/MM8000) (.NET Core + ANTLR)
**Cross-reference:** Used as reference for [SAP-1 Computer](../sap-1-computer/) project

---

#### Apple II Disk Archival
**Status:** Active Development
**Directory:** [apple-ii-disk-archival/](apple-ii-disk-archival/)

Comprehensive archival and preservation of Apple II 5.25" and 3.5" floppy disk collection using flux-level imaging with Greaseweazle V4.1 and Epson SD-800 dual-drive unit. Creating preservation masters (.SCP flux images), emulator-ready formats (.WOZ), and working backups (.DSK) of legally owned software.

**Priority Disks:** The Print Shop, The Toy Shop (Broderbund)

**Equipment:** Greaseweazle V4.1, Epson SD-800 (5.25" + 3.5" drives), Apple IIc, Apple IIgs

**Workflow:**
1. Flux imaging → .SCP preservation masters
2. Convert to .WOZ for emulators (preserves copy protection)
3. Optional: Create .DSK unprotected backups for real hardware

**Documentation:**
- [hardware-setup.md](apple-ii-disk-archival/hardware-setup.md) - Greaseweazle + SD-800 configuration
- [Notes/hardware/apple-ii-disk-copy-protection-archival.md](../Notes/hardware/apple-ii-disk-copy-protection-archival.md) - Copy protection schemes and removal techniques
- [Notes/hardware/apple-ii-printshop-toyshop-guide.md](../Notes/hardware/apple-ii-printshop-toyshop-guide.md) - Print Shop/Toy Shop specific guide

**Related:** [ImageWriter II Emulator](imagewriter-ii-emulator/) (print archived programs), [PrinterEmulator](https://github.com/mwwhited/PrinterEmulator)

---

### RF & Software-Defined Radio

#### Passive Radar SDR System
**Status:** Planning
**Directory:** [passive-radar-sdr/](passive-radar-sdr/)

Multi-channel SDR receiver system for passive radar detection of aircraft and vehicles using existing RF illuminators (FM radio, TV broadcast, cellular towers). Exploits bistatic radar principles to detect targets without transmitting, using synchronized SDR receivers for reference and surveillance channels.

**Equipment:** KrakenSDR or synchronized RTL-SDR array, GPSDO, directional antennas
**Software:** GNU Radio, Python/NumPy, KrakenSDR passive radar toolkit
**Related:** Ham radio operations, [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery)

**Key challenges:** Clock synchronization, dynamic range (60-100 dB), multipath, real-time signal processing

---

### Protocol Reverse Engineering & Integration

#### Radex One Geiger Counter Protocol
**Status:** Completed
**Directory:** [radex-one-protocol-reverse-engineering/](radex-one-protocol-reverse-engineering/)

Successfully reverse-engineered the complete USB serial protocol for the Radex One portable geiger counter from Quarta. Documented packet structure, checksum algorithm, data reading (ambient/accumulated/CPM), settings management, and device identification. Protocol uses 2400 baud with little-endian checksums.

**Equipment:** Radex One USB geiger counter, serial capture tools
**Outcome:** Full protocol specification with example code snippets (Python, C#)
**Applications:** Data logging, home automation integration, radiation mapping

---

#### Favero Fencing Scoring System
**Status:** Completed
**Directory:** [favero-fencing-scoring-system/](favero-fencing-scoring-system/)

Serial protocol integration for Favero Full-Arm-05 fencing scoring apparatus. Built for old fencing club to capture real-time match data (scores, time, lamp status, penalties). Implemented 20mA current loop to RS-232 interface conversion and real-time data decoding.

**Equipment:** Favero Full-Arm-05, 20mA to RS-232 converter, display system
**Protocol:** 2400 baud, 10-byte packets @ 42ms update rate
**Applications:** Scoreboard displays, match logging, live streaming graphics

---

#### ImageWriter II Emulator
**Status:** Planning
**Directory:** [imagewriter-ii-emulator/](imagewriter-ii-emulator/)

PC-based printer emulator that captures output from Apple II programs (The Print Shop, The Toy Shop, AppleWorks) and converts to modern formats (PDF, PNG) or routes to contemporary printers. Emulates an ImageWriter II dot-matrix printer over serial connection, enabling digital preservation of printed output and use of vintage software with modern printers.

**Architecture:** `[Apple II] --Serial--> [PC] --Software--> [PDF/PNG/Modern Printer]`

**Key Features:**
- Serial capture via USB-to-Serial adapter
- ImageWriter II protocol decoder (ESC commands, graphics mode)
- Text and graphics rendering engine (144 DPI, 9×9 dot matrix)
- Multi-format output (PDF, PNG, direct printing)
- Special handling for Print Shop banners

**Technology Stack:** .NET Core/8, System.IO.Ports, PdfSharp, ImageSharp

**Implementation Plan:** 12-week phased development
1. Serial capture (Week 1-2)
2. Command parser (Week 3-4)
3. Text rendering (Week 5-6)
4. Graphics rendering (Week 7-8)
5. PDF export (Week 9)
6. Modern printer output (Week 10)
7. Print Shop integration (Week 11-12)

**Equipment:** Apple IIc/IIgs, USB-to-Serial adapter, serial cable

**Related:** [Apple II Disk Archival](apple-ii-disk-archival/) (preserve disks first), [PrinterEmulator](https://github.com/mwwhited/PrinterEmulator), [DeviceBridge](https://github.com/mwwhited/DeviceBridge)

---

### Database & Machine Learning

#### Vector Search in SQL Server
**Status:** Completed
**Directory:** [vector-search-sqlserver/](vector-search-sqlserver/)

Vector search capabilities in SQL Server using Locality-Sensitive Hashing (LSH) with precomputed Hamming distance lookup tables. Enables semantic search, image similarity, and ML/AI applications directly in SQL Server without external vector databases. Part of [dotex](https://github.com/OutOfBandDevelopment/dotex) framework (`OoBDev.Data.Vectors`).

**Source Code:** [OutOfBandDevelopment/dotex](https://github.com/OutOfBandDevelopment/dotex) → `/src/Extensions/OoBDev.Data.Vectors`
**Technology:** LSH indexing, Hamming distances, SQL CLR, .NET
**Data:** Precomputed lookup tables (5/8/10/12/16-bit, ~1.9MB total) in `HammingDistances/`
**Applications:** Semantic search, recommendation engines, anomaly detection, k-NN classification

---

#### AI/ML Research & Reference
**Status:** Reference
**Directory:** [ai-ml-research/](ai-ml-research/)

Collection of AI/ML research papers, implementation notes, and critical perspectives on artificial intelligence. Includes paper summaries, ML concept notes, and thoughtful skepticism about AI limitations. Serves as a reference library for understanding current AI/ML techniques and their practical boundaries.

**Contents:**
- Research paper summaries and notes
- ML implementation concepts (neural networks, training techniques)
- Critical analysis of AI hype and limitations
- Related: Vector search research moved to [Vector Search SQL Server](vector-search-sqlserver/) project

**Resources:** Papers from arXiv, Fast.ai courses, AI Snake Oil blog

---

#### HuggingFace .NET Native Execution
**Status:** Research - Comprehensive Documentation
**Directory:** [huggingface-dotnet-native-execution/](huggingface-dotnet-native-execution/)

Research project documenting approaches for running HuggingFace transformer models (BERT, GPT-2, T5, etc.) natively in .NET applications without calling out-of-process to Python. Covers ONNX conversion workflows, native .NET inference engines, tokenizer implementations, and code generation approaches.

**Key Approaches:**
1. **ONNX Runtime + ML.NET** - Production-ready, 130,000+ model support
2. **TorchSharp** - Native PyTorch in .NET with training support
3. **Transformers.NET** - Community library with HuggingFace Hub integration
4. **Code Generation** - Experimental compile-time model embedding
5. **Semantic Kernel** - AI orchestration framework

**Documentation:**
- [README.md](huggingface-dotnet-native-execution/README.md) - Project overview and quick start
- [TECHNOLOGY_COMPARISON.md](huggingface-dotnet-native-execution/TECHNOLOGY_COMPARISON.md) - Detailed comparison matrix
- [ONNX_CONVERSION_WORKFLOW.md](huggingface-dotnet-native-execution/ONNX_CONVERSION_WORKFLOW.md) - Export and deployment guide
- [IMPLEMENTATION_GUIDES.md](huggingface-dotnet-native-execution/IMPLEMENTATION_GUIDES.md) - 6 practical scenarios
- [RESEARCH_BIBLIOGRAPHY.md](huggingface-dotnet-native-execution/RESEARCH_BIBLIOGRAPHY.md) - 104+ resources

**Technology Stack:** .NET 8, ONNX Runtime, TorchSharp, HuggingFace Optimum, ML.NET

**Use Cases:** Sentiment analysis, question answering, NER, semantic search, text generation

**Related:** [dotex](https://github.com/OutOfBandDevelopment/dotex) (.NET libraries), Vector Search SQL Server project

---

### Test & Measurement Automation

#### SCPI Instrument Control
**Status:** Planning/Research
**Directory:** [scpi-instrument-control/](scpi-instrument-control/)

Network control system for SCPI-compatible test equipment with custom .NET Core VISA driver. Building RS-232/Ethernet gateway for lab equipment automation (HP 34401A, Rigol DM3058E, DG1022, Korad supplies).

**Equipment:** HP 34401A DMM, Rigol DM3058E, DG1022, Raspberry Pi/BeagleBone
**Related:** [DeviceBridge](https://github.com/mwwhited/DeviceBridge)

---

### DevOps & Infrastructure

#### Self-Hosted Git Server
**Status:** Planning
**Directory:** [self-hosted-git-server/](self-hosted-git-server/)

Local Git hosting for personal repositories and backup of public projects. Deploying Gitea on WD My Cloud PR4100 for self-hosted development workflow with web UI, issue tracking, and repository mirroring. Focus on data sovereignty and backup redundancy.

**Hardware:** WD My Cloud PR4100 (Docker host, always-on NAS)
**Platform Options:** Gitea (recommended), bare Git repos, or GitLab CE
**Use Cases:** Private repo hosting, GitHub backup/mirrors, local development

**Migration strategy:** New repos → migrate private repos → mirror public repos (EmbeddedBakery, BinaryDataDecoders, etc.)

---

#### SBC Cluster (ARM)
**Status:** Planning
**Directory:** [sbc-cluster/](sbc-cluster/)

Low-power ARM cluster for learning container orchestration, distributed computing, and network device filtering. 8 single-board computers (4× BeagleBone Black, 2× Raspberry Pi 2, 2× Raspberry Pi Model A) with custom power controller. Focus on ARM Docker/k3s deployment, device filtering experiments, and always-on lightweight services.

**Hardware:** 8× ARM SBCs (~12 cores, 4.5GB RAM total), custom power controller
**Use Cases:** ARM container testing, network filtering, low-power services (Pi-hole)
**Comparison:** Complements DevOps Playground Cluster - ARM vs x86, always-on vs on-demand

---

#### DevOps Playground Cluster
**Status:** In Progress
**Directory:** [devops-playground-cluster/](devops-playground-cluster/)

Multi-node home lab cluster built from Reduced BigRig (FX-9590) and Server (FX-8350) for learning container orchestration, HPC workloads, and DevOps tooling. Experimenting with Docker, Kubernetes (k3s), Slurm, Docker Swarm, Ansible, Terraform, and GitOps workflows.

**Hardware:** Reduced BigRig (FX-9590, 32GB RAM, 2x R9 290), Server (FX-8350, 32GB RAM, 3TB storage)
**Combined Resources:** 16 CPU cores, 64GB RAM, 3TB+ storage
**Technologies:** Docker, Kubernetes, Slurm, Ansible, Prometheus/Grafana

**Key learning areas:** Container orchestration, HPC job scheduling, infrastructure as code, monitoring

---

### Smart Home & IoT

#### Home Automation
**Status:** In Progress
**Directory:** [home-automation/](home-automation/)

Migrating from HomeSeer HS4 to Home Assistant for home automation. Z-Wave focus with multi-protocol support (Zigbee, Matter, Thread). 100% local control with self-hosted remote access via WireGuard VPN.

**Equipment:** Raspberry Pi 3 (×2), Z-Wave hats, Z-Net bridge, Galaxy Tab4 Nook (dashboard)
**Platform:** Home Assistant (open source, no subscriptions)

---

### AI & Development Tools

#### Cline with Local LLM (Qwen3 Coder)
**Status:** Planning - Setup Pending
**Directory:** [cline-qwen3-coder-30b/](cline-qwen3-coder-30b/)

Local LLM-powered Cline CLI integration for private code generation and assistance. Testing Qwen3 Coder 30b 4-bit and Qwen2 variants served via Ollama on RTX 4070 Ti (12GB VRAM). Includes Docker containerization with working directory mapping, similar to Claude Code CLI.

**Hardware:** Nvidia RTX 4070 Ti (12GB VRAM), 32GB+ System RAM
**Key Advantage:** Code stays private (no cloud uploads), zero API costs, instant availability
**Setup:** Docker containers with Ollama + Cline CLI, working directory mapped via `-v %CD%:/workspace`
**Tools:** Ollama (model server), Cline CLI, Qwen3 Coder 30b + Qwen2 variants, Docker

**Documentation:**
- [README.md](cline-qwen3-coder-30b/README.md) - Project overview and specifications
- [DOCKER_SETUP.md](cline-qwen3-coder-30b/DOCKER_SETUP.md) - Complete Docker integration guide
- [Dockerfile](cline-qwen3-coder-30b/Dockerfile) - Container configuration
- [cline-launch.bat](cline-qwen3-coder-30b/cline-launch.bat) / [cline-launch.sh](cline-qwen3-coder-30b/cline-launch.sh) - Launch scripts

**Cross-references:** [ai-ml-research/](ai-ml-research/), [devops-playground-cluster/](devops-playground-cluster/) (GPU hardware), [local-docker-registry/](local-docker-registry/)

---

#### Local Docker Registry
**Status:** Planning - Hardware Allocation Pending
**Directory:** [local-docker-registry/](local-docker-registry/)

Private, self-hosted Docker image registry for caching, offline deployment, and fast local image pulls. Reduces bandwidth costs and Docker Hub rate limiting. Integrates with DevOps Playground Cluster, SBC Cluster, Cline, and CI/CD pipelines.

**Primary Use Cases:**
- **Development:** Local image caching for faster builds
- **CI/CD:** Private registry for internal image builds
- **Cluster Deployments:** Central image source for DevOps and k3s clusters
- **Air-gapped Systems:** Offline deployment support

**Recommended Host:** WD My Cloud PR4100 NAS (always-on, centralized, persistent)
**Alternative Hosts:** DevOps Playground Cluster machines, dedicated SBC, development workstation

**Components:**
- Docker Registry (v2) - REST API on port 5000
- Optional: Registry UI (web browser at port 8080)
- Image storage: Persistent volume with garbage collection

**Documentation:**
- [README.md](local-docker-registry/README.md) - Complete architecture and configuration
- [QUICKSTART.md](local-docker-registry/QUICKSTART.md) - 5-minute setup guide
- [docker-compose.yml](local-docker-registry/docker-compose.yml) - Full service definitions

**Key Integration Points:**
- DevOps Playground Cluster: Pull images from `localhost:5000`
- SBC Cluster: k3s registries.yaml configuration
- Cline Docker setup: Base images from local registry
- CI/CD pipelines: Push to local registry instead of Docker Hub

**Cross-references:** [devops-playground-cluster/](devops-playground-cluster/), [sbc-cluster/](sbc-cluster/), [cline-qwen3-coder-30b/](cline-qwen3-coder-30b/), [self-hosted-git-server/](self-hosted-git-server/)

---

### Workshop Organization

#### DIY TrekPak Dividers
**Status:** Reference/As Needed
**Directory:** [diy-trekpak-dividers/](diy-trekpak-dividers/)

Reference documentation and materials inventory for custom drawer dividers. Uses corrugated plastic, EVA foam, and hair pins as DIY alternative to Pelican TrekPak (~$60-70 vs $80-150+ commercial). Materials acquired and available for use when organization projects arise.

**Materials:** Hair pins, EVA foam, felt tape, corrugated plastic (on hand)
**Use Cases:** Component storage, tool organization, camera cases - build as needed

---

## Project Status Summary

- **Completed:** 4 projects (ATtiny2313 LED Clock, Radex One Protocol, Favero Fencing System, Vector Search SQL Server)
- **Active Development:** 7 projects (FPGA CPU, SAP-1, Zynq, Analog Computer, DevOps Cluster, Home Automation, Apple II Disk Archival)
- **Planning/Research:** 8 projects (Passive Radar SDR, SCPI Control, Self-Hosted Git Server, SBC Cluster, Cline with Local LLM, Local Docker Registry, ImageWriter II Emulator)
- **Research Documentation:** 1 project (HuggingFace .NET Native Execution - comprehensive research complete)
- **On Hold:** 1 project (MM-8000K Trainer UI - hardware functional, used as reference)
- **Reference/As Needed:** 3 projects (DIY TrekPak Dividers, DRL/DTL Logic Boards, AI/ML Research)

**Total: 24 projects** (4 completed, 7 active, 8 planning, 1 research, 1 on hold, 3 reference)

## Cross-References

### Equipment Inventories
- [Programmable Devices/](../Programmable%20Devices/) - FPGA, MCU, dev boards
- [Test Equipment/](../Test%20Equipment/) - Oscilloscopes, DMMs, programmers
- [Vintage Computers/](../Vintage%20Computers/) - Apple II, TI-99/4A, MM-8000K
- [Device Lab/](../Device%20Lab/) - Tablets, Pi devices, hackable hardware
- [Expansion Boards/](../Expansion%20Boards/) - Arduino shields, Pi HATs

### Planning & Documentation
- [project-ideas.md](project-ideas.md) - Project backlog and future ideas
- [workshop-capabilities.md](../workshop-capabilities.md) - Equipment summary and project ideas by difficulty
- [tools-and-components.md](../tools-and-components.md) - Hand tools, wire, consumables, component stock

### Research Collections
- [AnalogComputers/analog-computing-repository/](../AnalogComputers/analog-computing-repository/) - Analog computing research (232 PDFs)
- [ai-ml-research/](ai-ml-research/) - AI/ML research papers and notes
- [Notes/](../Notes/) - Technical notes by topic (hardware, software, FPGA)

### Related Repositories
- [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery) - Arduino, AVR, ESP8266, STM32, FPGA projects
- [MM8000](https://github.com/mwwhited-archives/MM8000) - Intel 8085 trainer emulator
- [DeviceBridge](https://github.com/mwwhited/DeviceBridge) - IEEE-1284 parallel port capture
- [MyMashedDuet](https://github.com/mwwhited/MyMashedDuet) - Velleman K8200 3D printer config

## Adding New Projects

Follow [.claude/protocols/PROJECTS_PROTOCOL.md](../.claude/protocols/PROJECTS_PROTOCOL.md) when creating new project documentation.

**Standard structure:**
```
projects/
└── new-project-name/
    ├── README.md           # Required - overview, status, equipment, references
    ├── build-log.md        # Optional - session-by-session progress
    ├── parts-list.md       # Optional - detailed BOM
    └── [project files]     # Code, schematics, notes, etc.
```

---

*Last updated: 2026-01-19*
*Total projects: 24*
