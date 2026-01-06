# Workshop Capabilities & Project Ideas

Quick reference for what this workshop can do and project suggestions when you need inspiration.

**GitHub Profile:** [mwwhited](https://github.com/mwwhited) | **Organizations:** [OutOfBandDevelopment](https://github.com/OutOfBandDevelopment) | [mwwhited-archives](https://github.com/mwwhited-archives) | [mwwhited-notes](https://github.com/mwwhited-notes)

**Key Repositories:**

*Embedded & Hardware:*
- [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery) - Arduino, AVR, ESP8266, STM32, FPGA (Arty A7/Z7, Cyclone II), CPLD, analog circuits
- [DeviceBridge](https://github.com/mwwhited/DeviceBridge) / [PrinterEmulator](https://github.com/mwwhited/PrinterEmulator) - TDS2024 IEEE-1284 parallel-to-USB capture (Arduino Mega)
- [MM8000](https://github.com/mwwhited-archives/MM8000) - Intel 8085 Microprocessor Trainer emulator (CLI + ANTLR assembler)
- [MyMashedDuet](https://github.com/mwwhited/MyMashedDuet) - Velleman K8200 Duet 3 multi-tool configuration

*.NET Libraries & Tools (Out-of-Band Development):*
- [dotex](https://github.com/OutOfBandDevelopment/dotex) - .NET extensions framework (shared libraries)
- [oobtainium](https://github.com/OutOfBandDevelopment/oobtainium) - Method interception mocking framework
- [BuildFirstOnce](https://github.com/OutOfBandDevelopment/BuildFirstOnce) - MSBuild orchestration (run tasks once per solution)
- [RunScripts](https://github.com/OutOfBandDevelopment/RunScripts) - Docker wrapper scripts for dev tools (Python, Node, Rust, TensorFlow, etc.)
- [AllMiniLML6v2Sharp](https://github.com/OutOfBandDevelopment/AllMiniLML6v2Sharp) - Fork: sentence embeddings for C#
- [MSBuild.Sdk.SqlProj](https://github.com/OutOfBandDevelopment/MSBuild.Sdk.SqlProj) - Fork: SDK-style .dacpac builds

*Data & Encoding:*
- [BinaryDataDecoders](https://github.com/mwwhited/BinaryDataDecoders) - Encoding/decoding libraries (.NET)

---

## Table of Contents

- [Equipment Summary](#equipment-summary)
- [What Can I Build?](#what-can-i-build)
- [What Can I Fix?](#what-can-i-fix)
- [Project Ideas by Difficulty](#project-ideas-by-difficulty)
- [Project Ideas by Category](#project-ideas-by-category)
- [Troubleshooting Guide](#troubleshooting-guide)

---

## Equipment Summary

### Compute Platforms

| Category         | Devices                         | Best For                                |
|------------------|---------------------------------|-----------------------------------------|
| **FPGA**         | Artix-7 (100K LCs), Cyclone II  | Custom logic, retro clones, DSP         |
| **SoC**          | Zynq (ARM + FPGA)               | Linux + hardware acceleration           |
| **Arduino/AVR**  | UNO, Mega, Nano, ATtiny, ATmega | Prototyping, sensors, simple control    |
| **ESP WiFi**     | ESP8266, ESP32                  | IoT, home automation, wireless          |
| **ARM**          | STM32 BluePill                  | USB devices, RTOS, performance          |
| **Wireless**     | XBee, BLE modules               | Mesh networks, remote sensors           |
| **Analog**       | The Analog Thing                | ODEs, control systems, simulation       |
| **Legacy**       | PIC, 8051, Z8, Basic Stamp      | Specific applications, learning         |
| **CPLD/GAL**     | XC95108, ATF16V8B               | Glue logic, vintage chip replacement    |
| **TTL Computer** | Gigatron                        | CPU architecture learning, retro gaming |
| **Retro Kits**   | Multicomp (Z80/6502/6809)       | CP/M, vintage OS emulation              |
| **8-bit Trainers** | MM-8000K (8085A) + [emulator](https://github.com/mwwhited-archives/MM8000) | Vintage CPU learning, assembler dev |
| **Robot Kits**     | D2-1 Line Follower               | Sensor integration, motor control   |

### Vintage Computers

| System     | Projects                           |
|------------|------------------------------------|
| Apple IIc  | Software, peripherals, restoration |
| Apple IIgs | 16-bit dev, sound/graphics, GS/OS  |
| TI-99/4A   | Cartridges, speech, expansion      |

**Shared Accessories:**
- Floppy Emu (Big Mess O' Wires) - SD-based floppy/HD emulator for Apple II systems
- Greaseweazle V4.1 - USB floppy controller for disk imaging/writing (3" to 8")

### Device Lab (Modern Computing)

*See [Device Lab/](Device%20Lab/) for full inventory.*

#### Workstations & Servers

| System | Specs | Use |
|--------|-------|-----|
| PowerSpec G474 | i9-14900KF, 160GB DDR5, RTX 4070 Ti, 2TB NVMe | Primary workstation, dev, photo editing |
| Reduced BigRig | FX-9590, 32GB DDR3, 2x R9 290 | DevOps Playground node |
| Server | FX-8350, 32GB DDR3, 3TB storage | DevOps Playground node |
| Surface Book 2 15" | Intel i7, 2-in-1 | Portable dev |

#### DevOps Playground Cluster

Two-node home lab for container orchestration and DevOps learning:
- **Total resources**: 16 cores, 64GB RAM, 3TB+ storage
- **Target technologies**: Docker, Kubernetes (k3s), Slurm, Docker Swarm, Ansible, Terraform
- **GPU compute**: 2x R9 290 available for OpenCL workloads

#### Network Storage

| Device | Capacity | Use |
|--------|----------|-----|
| WD My Cloud PR4100 | 4-bay, Intel N3710 | Media server, Docker host, backups |
| WD MyBookLive | Single drive | Offline archive only (security issues) |

#### Mobile Devices (Hackable)

| Device | Status | Project Potential |
|--------|--------|-------------------|
| Samsung Galaxy Tab4 Nook | LineageOS candidate | Home automation dashboard |
| Amazon Fire HD | Google Play hackable | Kiosk, smart display |
| Apple iPad Mini | Jailbreak candidate | Media, HomeKit |
| Apple iPhone 2G | Fully jailbreakable | Collectible, retro iOS |
| Sony PSVita | CFW available | Emulation, homebrew gaming |

### Test & Measurement

| Category            | Equipment                                        | Capability                    |
|---------------------|--------------------------------------------------|-------------------------------|
| **Oscilloscope**    | 200 MHz DSO, 150 MHz analog                      | Debug signals to ~50 MHz      |
| **Multimeter**      | 6½ digit HP 34401A                               | Precision measurements        |
| **LCR Meter**       | 100 kHz DE-5000                                  | Component characterization    |
| **Logic Analyzer**  | 16 ch @ 100 MSa/s                                | Digital protocol debug        |
| **Power Supply**    | 30V/5A, 60V/3A                                   | Most bench projects           |
| **Thermal**         | FLIR TG130 (80x60)                               | Hot spot detection            |
| **Microscope**      | 3.5X-90X stereo + 5MP camera, 40X-2000X compound | SMD work, inspection, imaging |
| **Document Camera** | Kitchbar KB-700 (8MP)                            | PCB photos, documentation     |
| **Webcam**          | Lenovo 510 FHD (1080p, 95° wide)                 | Video tutorials, streaming    |

### Assembly & Rework

| Tool              | Use                            |
|-------------------|--------------------------------|
| KSGER T12         | Soldering (10 tip shapes)      |
| YaeCCC 858D       | Hot air SMD rework             |
| Hakko FR-301      | Through-hole desoldering       |
| Stereo microscope | SMD inspection/placement       |
| Microscope camera | Capture images/video of work   |
| Document camera   | PCB overview photos, tutorials |

### Lab Equipment

| Tool                        | Use                                          |
|-----------------------------|----------------------------------------------|
| CREWORKS Ultrasonic Cleaner | PCB cleaning, parts degreasing, flux removal |
| Magnetic Stirrer Hot Plate  | Solution prep, chemical mixing               |

### Fabrication

| Tool | Specs | Use |
|------|-------|-----|
| [Velleman K8200](https://github.com/mwwhited/MyMashedDuet) | 200x200x200mm, Duet 3, multi-tool, multi-filament | Enclosures, brackets, fixtures, replacement parts |

### Audio Equipment

| Tool       | Specs                | Use                                           |
|------------|----------------------|-----------------------------------------------|
| Pyle PTAU45| 2×120W, USB/RCA/AUX  | Audio circuit testing, speaker testing, signal amplification |

### Automation & Input

| Tool                   | Use                                               |
|------------------------|---------------------------------------------------|
| Fifine D6 Macro Keypad | 15-key programmable shortcuts, instrument control |

### Protocol Tools

| Tool                | Protocols                        | Use                                    |
|---------------------|----------------------------------|----------------------------------------|
| Bus Pirate v3.6a    | SPI, I2C, UART, 1-Wire, JTAG     | Interactive protocol debugging         |
| FT232H Breakout     | SPI, I2C, JTAG, UART, GPIO       | High-speed protocol interface, bitbang |
| Analog Discovery 2  | SPI, I2C, UART, CAN, etc.        | Protocol analysis with scope/logic     |

### Programmers

| Programmer         | Targets                       |
|--------------------|-------------------------------|
| TL866II Plus       | EEPROM, Flash, AVR, PIC, GAL  |
| USBasp             | AVR (Arduino, ATtiny, ATmega) |
| ST-Link V2         | STM32, STM8                   |
| Altera USB Blaster | Intel/Altera FPGA, CPLD       |
| FT232H             | Xilinx CPLD (via xc3sprog)    |
| Velleman K8048RS   | PIC 8/14/18/28-pin (RS-232)   |
| Greaseweazle V4.1  | Floppy disk read/write (3"-8")|

### Data Acquisition

| Tool           | Inputs      | Outputs   | Interface |
|----------------|-------------|-----------|-----------|
| Velleman K8055 | 5 DI, 2 AI  | 8 DO, 2 AO| USB       |

### Expansion Boards

| Type | Count | Examples |
|------|-------|----------|
| Arduino Shields | 12 | Motor/Servo, LCD Keypad, XBee, RS232/RS485, ISP, Sensor |
| Raspberry Pi HATs | 2 | PoE HAT, ARPI600 |

*See `Expansion Boards/` for full inventory.*

### Components & Consumables Stock

*See [tools-and-components.md](tools-and-components.md) for complete inventory.*

| Category | Stock Summary |
|----------|---------------|
| **Passive Components** | 30-value resistor kit (1Ω-1MΩ), 300x 10KΩ, 10x 100Ω 5W, ceramic/electrolytic cap kits |
| **Potentiometers** | 50x 10K trimpots, 20x 10K with knobs, slide pots, 4-axis joystick |
| **Voltage Regulators** | LM317T (25), LM337T (10), LM2596 buck (20), DC-DC boost converters |
| **Op-amps/Comparators** | TL074CN (20), LM324N (25), LM339 (30) |
| **Logic ICs** | 74HC14 Schmitt (20), 74HCT138 (10), 74LS83 adders (10), CD4070 XOR (10), NE555D (50) |
| **Transistors/MOSFETs** | IRF4905 P-ch (10), optocouplers PC817C (50) |
| **LEDs** | 5mm assorted colors (400+), RGB common cathode (100), 5mm holders (600) |
| **Displays** | Panel voltmeters (15), 7-segment clock displays |
| **Connectors** | DIP sockets (110), spring terminals, aviation plugs, IDC headers/sockets |
| **Switches** | Toggle (8), momentary pushbuttons (29), slide switches (100), membrane keypads |
| **Prototyping** | Perfboard, breadboard, project enclosures (12+), stackable headers |
| **Wire/Cable** | 30AWG wire wrap, ribbon cable, USB/BNC/HDMI cables |
| **Soldering** | T12 tips, desoldering nozzles, tip tinner, flux |
| **Battery Holders** | AA (10), CR123 (10), CR2032 (30) |
| **Fasteners** | M2 screws/nuts, M4 threaded rods, reusable cable ties |
| **Hand Tools** | Precision crimper, chip lifter, wire stripper, ESD wrist straps |

---

## What Can I Build?

*Based on equipment inventory and your demonstrated skills from [GitHub](https://github.com/mwwhited).*

### Protocol Bridges & Interfaces

*Extends your [DeviceBridge](https://github.com/mwwhited/DeviceBridge) and [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery) expertise.*

- [ ] GPIB/IEEE-488 to USB (like DeviceBridge for GPIB instruments)
- [ ] LXI/SCPI instrument automation
- [ ] LANC camera control systems
- [ ] RS485/Modbus gateways
- [ ] Parallel-to-WiFi bridges
- [ ] Protocol analyzers and sniffers

### FPGA & Custom Logic

*Building on your Arty A7/Z7 and Cyclone II work.*

- [ ] Soft CPU cores (6502, Z80, 8080/8085, TMS9900, custom ISA)
- [ ] Retro computer clones (Apple II, TI-99/4A, 8085 trainer)
- [ ] Video controllers (VGA, HDMI encoder)
- [ ] High-speed logic analyzers
- [ ] DSP pipelines and filters
- [ ] Hardware accelerators (Zynq HLS)

### Analog Computing

*Using The Analog Thing.*

- [ ] Chaotic systems (Lorenz, Rössler)
- [ ] Ecosystem simulations
- [ ] Control system modeling
- [ ] Hybrid analog-digital with MCU interface
- [ ] Real-time differential equation solving

### Vintage Computer Hardware

*For Apple IIc, IIgs, and TI-99/4A.*

- [ ] Custom expansion cards
- [ ] SmartPort/floppy alternatives
- [ ] Speech synthesizer clones
- [ ] Memory expansions
- [ ] GAL replacements for customs
- [ ] Video output adapters

### Floppy Disk Archival & Preservation

*Using Greaseweazle V4.1 and vintage computers.*

- [ ] Apple II disk imaging (5.25" DOS 3.3, ProDOS)
- [ ] Apple IIgs disk imaging (3.5" ProDOS, GS/OS)
- [ ] TI-99/4A disk imaging (5.25" TI format)
- [ ] Flux-level preservation (Kryoflux-compatible)
- [ ] Disk repair and recovery
- [ ] Write-back to original media

### Mesh & Wireless Networks

*Using XBee modules and XBIB-U-DEV board.*

- [ ] XBee mesh sensor networks
- [ ] Wireless data logging
- [ ] Remote monitoring systems
- [ ] Point-to-multipoint communication
- [ ] Coordinator/router/end device topologies

### DevOps & Infrastructure

*Using DevOps Playground cluster (Reduced BigRig + Server).*

- [ ] Kubernetes (k3s) cluster deployment
- [ ] Docker Swarm orchestration
- [ ] Slurm HPC job scheduler
- [ ] CI/CD pipelines (Jenkins, GitLab Runner, Drone)
- [ ] GitOps workflows (ArgoCD, Flux)
- [ ] Infrastructure as Code (Ansible, Terraform)
- [ ] Monitoring stack (Prometheus, Grafana)
- [ ] GPU compute workloads (OpenCL on R9 290s)

### Home Automation

*Using home-automation project, Galaxy Tab4 Nook, and cluster.*

- [ ] Home Assistant deployment
- [ ] Z-Wave device migration
- [ ] Tablet dashboard (LineageOS + Fully Kiosk/WallPanel)
- [ ] Multi-protocol hub (Z-Wave, Zigbee, Matter)
- [ ] Self-hosted remote access (no cloud)

### Mobile Device Repurposing

*Using Device Lab mobile devices.*

- [ ] Kiosk mode displays (Fire HD, iPad)
- [ ] Digital photo frames
- [ ] Dedicated media players
- [ ] Home automation control panels
- [ ] Retro gaming handhelds (PSVita CFW)
- [ ] Security cameras / baby monitors

---

## What Can I Fix?

### With Current Equipment

| Problem                 | Tools Needed               | Can Do? |
|-------------------------|----------------------------|---------|
| Dead power supply       | DMM, scope, thermal        | [x]     |
| Bad capacitors          | Soldering, ESR meter       | [x]     |
| Failed through-hole IC  | Desoldering gun            | [x]     |
| Failed SMD IC           | Hot air, microscope        | [x]     |
| Bad solder joints       | Microscope, soldering      | [x]     |
| Intermittent connection | Scope, thermal             | [x]     |
| Logic IC failure        | Logic analyzer, TL866      | [x]     |
| EEPROM/Flash corruption | TL866II Plus               | [x]     |
| GAL/PAL failure         | TL866II Plus + new GAL     | [x]     |
| Vintage computer repair | All of the above           | [x]     |
| Serial/I2C/SPI debug    | Bus Pirate, logic analyzer | [x]     |
| USB device issues       | Scope, protocol analyzer   | [x]     |
| Dirty/contaminated PCB  | Ultrasonic cleaner         | [x]     |
| Old flux residue        | Ultrasonic cleaner + IPA   | [x]     |
| Audio circuit debug     | Scope, DG1022, PTAU45      | [x]     |
| Speaker/amp testing     | DG1022 + PTAU45            | [x]     |

### Repair Workflow

1. **Visual inspection** - Microscope for damaged components
2. **Cleaning** - Ultrasonic cleaner for dirty/corroded boards
3. **Thermal scan** - FLIR for hot spots
4. **Power check** - DMM for voltages
5. **Signal trace** - Scope for waveforms
6. **Protocol debug** - Logic analyzer for digital
7. **Component test** - LCR meter, TL866
8. **Rework** - Solder/hot air/desolder as needed
9. **Post-rework cleaning** - Ultrasonic to remove flux residue

---

## Project Ideas by Difficulty

*Calibrated to your skill level based on EmbeddedBakery, DeviceBridge, and related work.*

### Quick Builds (Hours to Days)

| Project                     | Platform           | Prior Work                                                           |
|-----------------------------|--------------------|----------------------------------------------------------------------|
| SCPI instrument controller  | ESP8266 + LXI      | [EmbeddedBakery ESP8266](https://github.com/mwwhited/EmbeddedBakery) |
| Macro keypad firmware       | ATmega32U4         | USB HID experience |
| GAL replacement for vintage | ATF16V8B + TL866   | [PAL projects](https://github.com/mwwhited/EmbeddedBakery)           |
| RS485 sniffer               | STM32 + UART       | [RS485 work](https://github.com/mwwhited/EmbeddedBakery)             |
| I2C bus scanner/debugger    | Arduino + OLED     | Sensor interfaces                                                    |
| ROM dumper utility          | Arduino Mega       | [DeviceBridge parallel](https://github.com/mwwhited/DeviceBridge)    |
| MM-8000K serial terminal    | USB-TTL + terminal | [MM8000 tools](https://github.com/mwwhited-archives/MM8000)          |
| Floppy disk imaging setup   | Greaseweazle + PC  | Vintage computer collection                                          |
| D2-1 robot MCU upgrade      | ATtiny85 + D2-1    | Line follower analog base                                            |
| K8055 automation script     | K8055 + Python     | USB I/O experience                                                   |

### Medium Projects (Days to Weeks)

| Project                      | Platform              | Prior Work                                                           |
|------------------------------|-----------------------|----------------------------------------------------------------------|
| GPIB/IEEE-488 adapter        | STM32 + level shift   | [DeviceBridge](https://github.com/mwwhited/DeviceBridge) (IEEE-1284) |
| LANC controller expansion    | Arduino + protocol    | [LANC projects](https://github.com/mwwhited/EmbeddedBakery)          |
| LXI-to-serial gateway        | ESP32 + SCPI          | [LXI Serial Bridge](https://github.com/mwwhited/EmbeddedBakery)      |
| 8085 FPGA soft core          | Arty A7 + VHDL        | MM-8000K hardware + [emulator](https://github.com/mwwhited-archives/MM8000) |
| Apple II SmartPort device    | ATmega + CPLD         | [CPLD work](https://github.com/mwwhited/EmbeddedBakery)              |
| TI-99/4A speech synth clone  | FPGA + DAC            | FPGA experience                                                      |
| Ensoniq DOC experiments      | Apple IIgs + code     | Audio/synthesis interest                                             |
| H4n remote interface         | ESP8266 + protocol    | [H4n protocol](https://github.com/mwwhited/EmbeddedBakery)           |
| XBee sensor mesh + dashboard | XBee + ESP32 + web    | ESP + wireless experience                                            |
| Analog + digital hybrid      | THAT + STM32          | [Analog circuits](https://github.com/mwwhited/EmbeddedBakery)        |
| Multicomp Z80 CP/M system    | Multicomp EP2C5       | Retro FPGA kit + [Grant Searle designs](http://searle.wales/)        |
| Multicomp 6502 system        | Multicomp EP2C5       | Apple II experience, 6502 assembly                                   |
| Vintage disk archival system | Greaseweazle + scripts| Apple II/TI-99 disk preservation                                     |
| XBee remote sensor station   | XBee + ATtiny + sensors| XBIB-U-DEV board                                                    |

### Major Projects (Weeks to Months)

| Project                       | Platform            | Prior Work                                                        |
|-------------------------------|---------------------|-------------------------------------------------------------------|
| Custom CPU with unique ISA    | Arty A7             | [MicroBlaze/CPU work](https://github.com/mwwhited/EmbeddedBakery) |
| 65C816 core (IIgs compatible) | Arty A7             | 6502 FPGA experience                                              |
| TMS9900 core (TI-99 compat)   | Arty A7             | CPU design skills                                                 |
| VGA/HDMI framebuffer          | Arty A7             | [Arty A7 projects](https://github.com/mwwhited/EmbeddedBakery)    |
| Apple II expansion card       | KiCad + CPLD        | CPLD + vintage computing                                          |
| USB protocol analyzer         | Zynq                | [Arty Z7 HLS](https://github.com/mwwhited/EmbeddedBakery)         |
| Zynq accelerator (HLS)        | Arty Z7             | [HLS tutorials](https://github.com/mwwhited/EmbeddedBakery)       |
| SDR receiver frontend         | Zynq + ADC          | DSP + Zynq skills                                                 |
| Centronics-to-WiFi bridge     | ESP32 + parallel    | [DeviceBridge](https://github.com/mwwhited/DeviceBridge)          |
| Multi-protocol test instrument| Zynq + analog       | Full-stack embedded                                               |
| Gigatron expansion module     | TTL + interface     | TTL computer ownership                                            |
| USB floppy emulator           | STM32 + Greaseweazle| Floppy imaging experience                                         |
| Complete vintage disk archive | Greaseweazle + DB   | Full Apple II/TI-99 disk collection                               |
| Multicomp 6809 Flex/OS-9      | Multicomp EP2C5     | 6809 soft core experience                                         |

### DevOps & Home Lab (Quick to Major)

| Project | Platform | Difficulty | Notes |
|---------|----------|------------|-------|
| Docker Compose services | Any Linux | Quick | Start with Portainer + Traefik |
| Docker Swarm cluster | BigRig + Server | Quick | Built-in Docker orchestration |
| k3s Kubernetes cluster | BigRig + Server | Medium | Lightweight K8s for home lab |
| Slurm job scheduler | BigRig + Server | Medium | HPC batch job management |
| GitOps with ArgoCD | k3s cluster | Medium | Declarative deployments |
| Full monitoring stack | Cluster | Medium | Prometheus + Grafana + alerts |
| GPU compute on R9 290 | BigRig | Medium | OpenCL workloads, ML experiments |
| Chaos engineering | k3s cluster | Major | Litmus, resilience testing |
| Multi-cluster federation | Cluster + cloud | Major | Hybrid cloud learning |

### Home Automation (Quick to Major)

| Project | Platform | Difficulty | Notes |
|---------|----------|------------|-------|
| Home Assistant install | Pi / Docker / VM | Quick | Basic platform setup |
| Z-Wave device migration | HA + Z-Stick | Quick | Move from HomeSeer |
| Galaxy Tab4 LineageOS flash | Tab4 Nook | Quick | TWRP + ROM flash |
| Tablet dashboard setup | Tab4 + HA | Medium | Fully Kiosk or WallPanel |
| Multi-protocol hub | HA + radios | Medium | Z-Wave + Zigbee + Matter |
| Self-hosted remote access | VPN / Tailscale | Medium | No cloud dependency |
| Voice control integration | HA + local STT | Major | Privacy-focused voice |
| Complete home automation | All devices | Major | Full house integration |

---

## Project Ideas by Category

### Protocol Bridges & Instrument Control

*Building on [DeviceBridge](https://github.com/mwwhited/DeviceBridge) and [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery) work.*

- [ ] GPIB/IEEE-488 USB adapter (extend DeviceBridge parallel expertise)
- [ ] LXI instrument gateway (extend your ESP8266 LXI bridge)
- [ ] LANC camera controller (expand existing LANC work)
- [ ] H4n recorder interface (build on H4n protocol work)
- [ ] RS485 protocol analyzer
- [ ] SCPI command library for test equipment
- [ ] Centronics-to-WiFi print server

### FPGA & CPU Design

*Building on your [Arty A7 MicroBlaze and custom CPU work](https://github.com/mwwhited/EmbeddedBakery) and [MM8000 emulator](https://github.com/mwwhited-archives/MM8000).*

- [ ] Custom ISA CPU (beyond MicroBlaze)
- [ ] 8085 soft core (FPGA version of MM-8000K trainer)
- [ ] 65C816 soft core (Apple IIgs compatible)
- [ ] TMS9900 soft core (TI-99/4A compatible)
- [ ] VGA framebuffer controller
- [ ] HDMI/DVI output encoder
- [ ] Hardware JSON/binary decoder (complement [BinaryDataDecoders](https://github.com/mwwhited/BinaryDataDecoders))
- [ ] Multi-channel logic analyzer
- [ ] DSP filter pipeline

### Vintage Computing

*For your Apple IIc, Apple IIgs, and TI-99/4A.*

- [ ] Apple II expansion card (custom peripheral)
- [ ] SmartPort SD card interface
- [ ] TI-99/4A cartridge with banked ROM
- [ ] TMS5220 speech synthesizer clone
- [ ] Composite to VGA/HDMI scan converter
- [ ] GAL replacements for failed customs
- [ ] Apple IIgs Ensoniq DOC experiments
- [ ] Memory expansion cards

### Zynq / SoC Projects

*Building on your [Arty Z7 HLS tutorials](https://github.com/mwwhited/EmbeddedBakery).*

- [ ] Linux + PL hardware accelerator
- [ ] USB protocol analyzer (high-speed capture)
- [ ] SDR receiver with DSP
- [ ] Multi-protocol test instrument
- [ ] Video processing pipeline
- [ ] Network-attached instrument server

### Analog Computing

*Using The Analog Thing.*

- [ ] Lorenz attractor (chaos visualization)
- [ ] Predator-prey ecosystem simulation
- [ ] Control system modeling
- [ ] Hybrid analog-digital with STM32 interface
- [ ] Mechanical system simulation
- [ ] Real-time ODE solving with digital readout

### Audio & Sound

*Using DG1022 signal generator and PTAU45 amplifier.*

- [ ] Audio spectrum analyzer (FPGA + ADC)
- [ ] Vintage computer sound card testing
- [ ] Speaker impedance measurement jig
- [ ] Audio signal tracer/injector
- [ ] Synthesizer/effects pedal projects
- [ ] Ensoniq DOC experiments (Apple IIgs)

### Floppy Disk Archival & Preservation

*Using Greaseweazle V4.1 with Apple II, Apple IIgs, and TI-99/4A.*

- [ ] Complete Apple II disk imaging workflow
- [ ] Apple IIgs 3.5" disk preservation
- [ ] TI-99/4A disk format imaging
- [ ] Flux-level preservation (raw captures)
- [ ] Damaged disk recovery and repair
- [ ] Disk image database and catalog system
- [ ] Write-back verification tools

### Mesh & Wireless Networks

*Using XBee modules, XBee Pro S1, and XBIB-U-DEV.*

- [ ] Multi-node sensor mesh network
- [ ] Wireless environmental monitoring
- [ ] Remote equipment status dashboard
- [ ] XBee-to-MQTT gateway (ESP32)
- [ ] Battery-powered sensor nodes (ATtiny + XBee)
- [ ] Long-range outdoor sensor deployment

### Retro Computing FPGA

*Using Multicomp EP2C5-DB and Altera EP2C5 Mini.*

- [ ] Z80 CP/M system (Grant Searle design)
- [ ] 6502 system with BASIC
- [ ] 6809 Flex or OS-9 system
- [ ] Custom peripheral interfaces
- [ ] VGA text/graphics output
- [ ] SD card mass storage interface

### DevOps & Infrastructure

*Using DevOps Playground cluster and NAS devices.*

- [ ] Kubernetes (k3s) multi-node cluster
- [ ] Docker Swarm deployment
- [ ] Slurm HPC workload manager
- [ ] CI/CD pipeline (Jenkins, GitLab Runner, Drone)
- [ ] GitOps with ArgoCD or Flux
- [ ] Ansible playbooks for cluster management
- [ ] Terraform for infrastructure as code
- [ ] Prometheus + Grafana monitoring
- [ ] GPU compute experiments (R9 290 OpenCL)
- [ ] Chaos engineering (Litmus, Chaos Monkey)

### Home Automation

*Using home-automation project and Device Lab tablets.*

- [ ] Home Assistant on cluster or dedicated Pi
- [ ] Z-Wave network migration from HomeSeer
- [ ] Galaxy Tab4 dashboard (LineageOS + WallPanel)
- [ ] Fire HD as secondary display
- [ ] Self-hosted remote access (VPN/Tailscale)
- [ ] Local voice control (no cloud)
- [ ] Multi-protocol support (Z-Wave, Zigbee, Matter, Thread)

### Mobile Device Repurposing

*Using Device Lab mobile devices and gaming handhelds.*

- [ ] Tablet kiosk displays (Fire HD, iPad)
- [ ] Digital signage / photo frames
- [ ] Dedicated streaming clients
- [ ] PSVita CFW + emulation station
- [ ] Retro iOS exploration (iPhone 2G)

### Test Equipment DIY

- [ ] FPGA-based logic analyzer (> 100 MSa/s)
- [ ] Curve tracer (transistor/diode characterization)
- [ ] ESR meter for capacitor testing
- [ ] Frequency counter (reciprocal counting)
- [ ] Protocol-aware cable tester
- [ ] Programmable load (for PSU testing)

---

## Troubleshooting Guide

### "Board is Dead"

```
1. Check power supply voltage (DMM)
2. Check for shorts (DMM continuity)
3. Thermal scan for hot components (FLIR)
4. Check regulator output
5. Check clock signal (scope)
6. Check reset circuit
```

### "Intermittent Behavior"

```
1. Thermal scan during operation
2. Flex test while monitoring
3. Reflow suspect joints
4. Check power rail ripple (scope)
5. Check decoupling caps (ESR)
```

### "Communication Not Working"

```
1. Verify voltage levels (DMM/scope)
2. Check signal integrity (scope)
3. Decode protocol (logic analyzer)
4. Verify timing (logic analyzer)
5. Check pull-ups/termination
```

### "Analog Circuit Issues"

```
1. Check DC operating points (DMM)
2. Measure signal path (scope)
3. Check for oscillation
4. Verify component values (LCR)
5. Thermal check for failing parts
```

### "Vintage Computer Won't Boot"

```
1. Check power supply voltages
2. Thermal scan for hot chips
3. Check clock and reset
4. Test ROM with TL866
5. Test RAM with diagnostic
6. Check custom chips (logic analyzer)
7. Recap if electrolytics are old
```

### "Audio Circuit Not Working"

```
1. Check power supply rails (DMM)
2. Inject test signal (DG1022 sine wave)
3. Trace signal path (scope)
4. Check for DC offset at output
5. Test output with known-good amp (PTAU45)
6. Verify component values (LCR for caps)
7. Check for oscillation/noise (scope)
```

---

## Wishlist (Would Expand Capabilities)

- [ ] **Spectrum analyzer** - RF debugging, EMI troubleshooting, SDR projects
  - Budget/Used:
    - [tinySA Ultra](https://www.tinysa.org/wiki/pmwiki.php?n=Main.Buying) (~$120)
    - Used HP 8590A
  - New:
    - [Rigol DSA815](https://www.rigolna.com/products/spectrum-analyzers/dsa800/)
    - [Siglent SSA3021X](https://siglentna.com/spectrum-analyzers/ssa3000x-series/)

- [ ] **Isolation transformer** - Safe work on line-connected equipment
  - Budget/Used:
    - Used Topaz or Tripp Lite (eBay)
    - Surplus hospital-grade
  - New:
    - [Triad N-68X](https://www.amazon.com/dp/B00BXMBOTG) (500VA)
    - [Hammond 171E](https://www.hammfg.com/electronics/transformers/isolation/171)

- [ ] **Bench LCR meter** - In-circuit SMD testing, better accuracy than DE-5000
  - Budget/Used:
    - Used HP 4263A/4263B
    - BK Precision 879B
  - New:
    - [Keysight U1731C](https://www.keysight.com/us/en/product/U1731C/handheld-lcr-meter.html)
    - [GW Instek LCR-6100](https://www.gwinstek.com/en-global/products/detail/LCR-6000)

- [ ] **Reflow oven** - Batch SMD assembly, consistent results
  - Budget/Used:
    - DIY toaster oven + [Controleo3 kit](https://www.whizoo.com/c3)
    - Used T-962
  - New:
    - [Miniware MHP50](https://www.amazon.com/dp/B0C7KXQQ8X) (hot plate)
    - [Puhui T-937](https://www.amazon.com/dp/B07VR3Q3ZK)

- [ ] **Current probe** - Non-contact current measurement on scope
  - Budget/Used:
    - Used Tektronix A621/A622
    - [Micsig CP2100A](https://www.amazon.com/dp/B07WNLQVZJ)
  - New:
    - [Tektronix A622](https://www.tek.com/en/products/probes/current-probes)
    - [Keysight N2783B](https://www.keysight.com/us/en/product/N2783B/current-probe-100-mhz.html)

- [ ] **Higher res thermal camera** - Better hotspot detection than TG130
  - Budget/Used:
    - [Uni-T UTi260B](https://www.amazon.com/dp/B08R6NK44L)
    - Used FLIR E4/E5
  - New:
    - [FLIR C5](https://www.flir.com/products/c5/)
    - [FLIR ONE Pro](https://www.flir.com/products/flir-one-pro/)

- [ ] **Variac** - Motor testing, slow power-up for vintage gear
  - Budget/Used:
    - Used Powerstat/Superior Electric (eBay)
    - Surplus lab units
  - New:
    - [Variac TDGC2-2KVA](https://www.amazon.com/dp/B09WDHM6NV)
    - [Staco 3PN1010B](https://www.staco-energy.com/variable-transformers/)

- [ ] **PCB mill/router** - Prototype PCBs without waiting for fab (3D printer can't do this)
  - Budget/Used:
    - [Genmitsu 3018-PROVer](https://www.amazon.com/dp/B07P6J9VB4) + PCB kit
    - Used Roland Modela MDX-20
  - New:
    - [BobsCNC E4](https://www.amazon.com/dp/B07GJBTBB9) + spindle upgrade
    - [Bantam Tools Desktop PCB Milling Machine](https://www.bantamtools.com/)

- [ ] **Logic analyzer upgrade** - More channels, higher speed than current setup
  - Budget/Used:
    - [DSLogic Plus](https://www.dreamsourcelab.com/product/dslogic-plus/) (16ch 400MHz)
    - Used Agilent 16700
  - New:
    - [Saleae Logic Pro 16](https://www.saleae.com/products/saleae-logic-pro-16)
    - [Analog Discovery 3](https://digilent.com/shop/analog-discovery-3/)

- [ ] **RF signal generator** - Clean LO/IF source for RF work, mixer testing, receiver alignment
  - Budget/Used:
    - Used HP 8648A/B (100 kHz - 1 GHz / 2 GHz)
    - Used HP 8656B (100 kHz - 990 MHz)
    - Used Marconi 2024 (9 kHz - 2.4 GHz)
  - New:
    - [Siglent SSG3021X](https://siglentna.com/rf-signal-generators/ssg3000x-series/) (9 kHz - 2.1 GHz)
    - [Rigol DSG815](https://www.rigolna.com/products/rf-signal-generators/dsg800/) (9 kHz - 1.5 GHz)
    - [Windfreak SynthHD](https://windfreaktech.com/product/microwave-signal-generator-synthhd/) (10 MHz - 15 GHz, USB)

- [ ] **SDR transceiver** - TX/RX capable for RF experimentation, ham radio, Zynq projects
  - Budget/Used:
    - [RTL-SDR Blog V4](https://www.rtl-sdr.com/rtl-sdr-blog-v4-dongle-initial-release/) (RX only, ~$30)
    - Used USRP B200mini
  - New:
    - [HackRF One](https://greatscottgadgets.com/hackrf/one/) (1 MHz - 6 GHz, half-duplex TX/RX)
    - [LimeSDR Mini 2.0](https://limemicro.com/products/boards/limesdr-mini-2-0/) (10 MHz - 3.5 GHz, full-duplex)
    - [ADALM-PLUTO](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/adalm-pluto.html) (325 MHz - 3.8 GHz, full-duplex, hackable to 70 MHz - 6 GHz)

---

*Last updated: January 2026 (Device Lab integration)*
