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

For complete vintage computer inventory with specifications and restoration status, see [`.personal/incoming/vintage-computers.md`](.personal/incoming/vintage-computers.md) (4 systems with peripherals).

| System     | Projects                           |
|------------|------------------------------------|
| Apple IIc  | Software, peripherals, restoration |
| Apple IIgs | 16-bit dev, sound/graphics, GS/OS  |
| TI-99/4A   | Cartridges, speech, expansion      |

**Shared Accessories:**
- Floppy Emu (Big Mess O' Wires) - SD-based floppy/HD emulator for Apple II systems
- Greaseweazle V4.1 - USB floppy controller for disk imaging/writing (3" to 8")

### Device Lab (Modern Computing)

For complete device lab inventory, see [`.personal/incoming/device-lab.md`](.personal/incoming/device-lab.md).

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

For complete test equipment inventory with detailed specifications, see [`.personal/incoming/test-equipment.md`](.personal/incoming/test-equipment.md) (41 units).

Quick Reference:

| Category            | Equipment                                        | Capability                    |
|---------------------|--------------------------------------------------|-------------------------------|
| **Oscilloscope**    | Rigol DS1102E (100MHz), Tektronix TDS2024 (200MHz), Hitachi V-1150 (150MHz analog) | Debug signals to ~50 MHz      |
| **Multimeter**      | HP 34401A (6½ digit), Rigol DM3058E (5½ digit)   | Precision measurements        |
| **LCR Meter**       | DER EE DE-5000 (100kHz)                          | Component characterization    |
| **Logic Analyzer**  | Digilent Analog Discovery 2 (16 digital channels @ 100 MSa/s) | Digital protocol debug        |
| **Power Supply**    | Korad KA3005P (30V/5A), Korad KA6003P (60V/3A)   | Most bench projects           |
| **Thermal**         | FLIR TG130 (80x60)                               | Hot spot detection            |
| **Microscope**      | 3.5X-90X stereo + 5MP camera, 40X-2000X compound | SMD work, inspection, imaging |
| **Document Camera** | Kitchbar KB-700 (8MP)                            | PCB photos, documentation     |
| **Signal Generator**| Rigol DG1022 (2ch, 20MHz)                        | Function generation, testing  |

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

Device programmers for all supported platforms (see [`.personal/incoming/programmable-devices.md`](.personal/incoming/programmable-devices.md) for complete device/programmer matrix):

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

For complete expansion board inventory with pin mappings and compatibility information, see [`.personal/incoming/expansion-boards.md`](.personal/incoming/expansion-boards.md) (30+ boards).

| Type | Count | Examples |
|------|-------|----------|
| Arduino Shields | 12+ | Motor/Servo, LCD Keypad, XBee, RS232/RS485, ISP, Sensor |
| Raspberry Pi HATs | 2+ | PoE HAT, ARPI600 |
| BeagleBone Capes | Several | EEPROM, GPIO expanders |
| Digilent Pmods | Various | Digital I/O, analog, protocols |

### Components & Consumables Stock

For complete inventory of tools, consumables, and component stock with quantities, see [`.personal/incoming/tools-and-components.md`](.personal/incoming/tools-and-components.md) (100+ items).

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

## Reference Collections

### Books & Technical References

For technical book collection by topic (software design, hardware, security, etc.), see [`.personal/incoming/books.md`](.personal/incoming/books.md) (50+ titles).

### Camera Equipment & Lenses

For complete camera collection including bodies, lenses, adapters, and accessories, see [`.personal/incoming/camera-collection.md`](.personal/incoming/camera-collection.md) (100+ items).

### Programmable Devices

For complete inventory of FPGA, MCU, SoC, Arduino boards, and retro platforms with specifications and programmer compatibility, see [`.personal/incoming/programmable-devices.md`](.personal/incoming/programmable-devices.md) (37 boards).

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

*Prices verified via web research on 2026-07-22 — fluctuate over time, especially eBay/grey-market. eBay links are search queries (listings expire), not fixed auctions.*

- [ ] **Spectrum analyzer** - RF debugging, EMI troubleshooting, SDR projects
  - Budget/Used:
    - [tinySA Ultra](https://www.randl.com) - ~$130 new (R&L Electronics; also see [official reseller list](https://www.tinysa.org/wiki/pmwiki.php?n=Main.Buying))
    - Used HP 8590A - [eBay search](https://www.ebay.com/sch/i.html?_nkw=HP+8590A+spectrum+analyzer), ~$130-$300
  - New:
    - [Rigol DSA815](https://www.testequity.com/product/32155-1-DSA815) - $1,319 ($999 for DSA815-TG w/ tracking gen), via TestEquity
    - [Siglent SSA3021X](https://www.saelig.com/product/ssa3021x.htm) - $1,395 base / $1,733 Plus, via Saelig

- [ ] **Isolation transformer** - Safe work on line-connected equipment
  - Budget/Used:
    - Used Tripp Lite - [eBay search](https://www.ebay.com/sch/i.html?_nkw=tripp+lite+isolation+transformer), ~$150 (500W) to ~$450 (larger)
    - Used Topaz Ultra-Isolator - [eBay search](https://www.ebay.com/sch/i.html?_nkw=topaz+ultra-isolator+isolation+transformer), ~$150-$500
  - New:
    - [Hammond 171E](https://www.digikey.com/en/products/detail/hammond-manufacturing/171E/455505) (500VA) - $210.04, via DigiKey
    - *(Correction: the previously-listed Triad N-68X is actually a 50VA unit, not 500VA, and its old Amazon link was dead/mismatched. If a small 50VA isolation tap is ever useful, N-68X is [$30.28 via DigiKey](https://www.digikey.com/en/products/detail/triad-magnetics/N-68X/1887210).)*

- [ ] **Bench LCR meter** - In-circuit SMD testing, better accuracy than DE-5000
  - Budget/Used:
    - Used HP 4263A/4263B - [eBay search](https://www.ebay.com/sch/i.html?_nkw=HP+4263A+LCR+meter), ~$100-$400+
    - [BK Precision 879B](https://www.testequipmentdepot.com/bk-precision-879b-dual-display-handheld-lcr-meter-with-esr-measurement-and-usb-interface.html) - $377.95 new via Test Equipment Depot; used [eBay search](https://www.ebay.com/sch/i.html?_nkw=BK+Precision+879B+LCR+meter) ~$250-$400
  - New:
    - [Keysight U1731C](https://www.keysight.com/us/en/product/U1731C/handheld-lcr-meter-100-hz-120-hz-1-khz.html) - $489 list (buy via Transcat/TEquipment/Newark, not direct from Keysight)
    - [GW Instek LCR-6100](https://www.transcat.com/gw-instek-lcr-6100-lcr-6100-308105) - $2,013, via Transcat

- [ ] **Reflow oven** - Batch SMD assembly, consistent results
  - Budget/Used:
    - DIY toaster oven + [Controleo3 build kit](https://whizoo.com/products/controleo3-reflow-oven-build-kit) - $395 (kit only, toaster oven separate)
    - Used T-962/T-962A - [eBay search](https://www.ebay.com/sch/i.html?_nkw=T-962A+reflow+oven), ~$140-$450
  - New:
    - [Miniware MHP50](https://www.amazon.com/dp/B0CWQVQ96X) (hot plate) - ~$100-$109 (previous ASIN was dead; also ~€109 via welectron.com)
    - Puhui T-937 - original Amazon ASIN dead; closest current match is rebrand [KY HOPE T-937](https://www.amazon.com/KY-HOPE-Desktop-Leadfree-Infrared/dp/B096JFFHNQ), or genuine Puhui via [AliExpress official store](https://www.aliexpress.com/item/32692181439.html) ~$575 (promo pricing, normally higher)

- [ ] **Current probe** - Non-contact current measurement on scope
  - Budget/Used:
    - Used Tektronix A621/A622 - [eBay search](https://www.ebay.com/sch/i.html?_nkw=tektronix+a621+a622+current+probe), ~$450-$1,160
    - [Micsig CP2100A](https://www.amazon.com/CP2100A-DC-800KHzUniversal-Measurement-Bandwidth-Oscilloscope/dp/B0C8DBP28F) - ~$260 (Amazon; previous ASIN was dead), $370 via Saelig
  - New:
    - [Tektronix A622](https://www.tequipment.net/TektronixA622.html) - ~$1,360, via TEquipment (Tek's own site no longer has a working probes page)
    - [Keysight N2783B](https://www.keysight.com/us/en/product/N2783B/ac-dc-current-probe-100-mhz.html) - ~$5,500-$6,000 (RS Online $5,991, Transcat $5,522)

- [ ] **Higher res thermal camera** - Better hotspot detection than TG130
  - Budget/Used:
    - [Uni-T UTi260B](https://www.amazon.com/UNI-T-UTi260B-49152Pixels-Resolution-Rechargeable/dp/B09W16Z18K) - ~$300-$400 (previous ASIN was dead)
    - Used FLIR E4/E5 - [eBay search](https://www.ebay.com/sch/i.html?_nkw=flir+e4+e5+thermal+camera), ~$750-$1,700
  - New:
    - [FLIR C5](https://www.flir.com/products/c5/) - $649.00 (standalone)
    - [FLIR ONE Pro](https://www.flir.com/products/flir-one-pro/) - $429.00 (phone attachment, not standalone)

- [ ] **Variac** - Motor testing, slow power-up for vintage gear
  - Budget/Used:
    - Used Powerstat/Superior Electric - [eBay search](https://www.ebay.com/sch/i.html?_nkw=superior+electric+powerstat+variac), ~$100-$300 depending on amperage
    - Surplus lab units (Staco, General Radio) - typically $75-$400+ on eBay depending on kVA
  - New:
    - Variac TDGC2-2KVA - previous Amazon ASIN unconfirmed/likely delisted; comparable listing via [Circuit Specialists](https://www.circuitspecialists.com/variac-tdgc2-2), ~$60-$100
    - [Staco 3PN1010B](https://www.digikey.com/en/products/detail/staco-energy-products-company/3PN1010B/526078) - $740.00, via DigiKey (old staco-energy.com domain is dead; correct site is [stacoenergy.com](https://www.stacoenergy.com/products-solutions/products/variable-transformers-and-test-sets/variable-transformers.html))

- [ ] **PCB mill/router** - Prototype PCBs without waiting for fab (3D printer can't do this)
  - Budget/Used:
    - [Genmitsu 3018-PROVer](https://www.sainsmart.com/products/sainsmart-genmitsu-cnc-router-3018-prover-kit) - $269.00 direct from SainSmart (was sold out at last check; old Amazon ASIN outdated)
    - Used Roland Modela MDX-20 - [eBay search](https://www.ebay.com/sch/i.html?_nkw=roland+modela+mdx-20), ~$450-$700
  - New:
    - ~~BobsCNC E4~~ - **BobsCNC has ceased operations (~March 2025)**; used units only via [eBay search](https://www.ebay.com/sch/i.html?_nkw=bobscnc+evolution+4), ~$550-$750
    - [Bantam Tools Desktop CNC Milling Machine](https://bantamtools.com/products/bantam-tools-desktop-cnc-milling-machine) - ~$2,499 base / ~$3,299 bundle (old product URL 404s; may be low-stock, confirm with sales@bantamtools.com)

- [ ] **Logic analyzer upgrade** - More channels, higher speed than current setup
  - Budget/Used:
    - [DSLogic Plus](https://www.dreamsourcelab.com/shop/logic-analyzer/dslogic-plus/) (16ch 400MHz) - $149 new (old product URL moved); used [eBay search](https://www.ebay.com/sch/i.html?_nkw=DSLogic+Plus+logic+analyzer), ~$80-$130
    - Used Agilent 16700 (modular mainframe) - [eBay search](https://www.ebay.com/sch/i.html?_nkw=Agilent+16700+logic+analyzer), ~$50-$500 depending on modules included
  - New:
    - [Saleae Logic Pro 16](https://www.mouser.com/ProductDetail/Saleae/Logic-Pro-16-Black) - $1,499 (sold out direct from Saleae; via Mouser); used ~$900-$1,200
    - [Analog Discovery 3](https://www.digikey.com/en/product-highlight/d/digilent/analog-discovery-3) - $379 ($249 academic), Pro Bundle $409

- [ ] **RF signal generator** - Clean LO/IF source for RF work, mixer testing, receiver alignment
  - Budget/Used:
    - Used HP 8648A/B - [eBay search](https://www.ebay.com/sch/i.html?_nkw=HP+8648A+signal+generator), ~$150-$450
    - Used HP 8656B - [eBay search](https://www.ebay.com/sch/i.html?_nkw=HP+8656B+signal+generator), ~$225-$550
    - Used Marconi 2024 - [eBay search](https://www.ebay.com/sch/i.html?_nkw=Marconi+2024+signal+generator), ~$230-$850
  - New:
    - [Siglent SSG3021X](https://siglentna.com/product/ssg3021x/) (9 kHz - 2.1 GHz) - $2,645
    - Rigol DSG815 (9 kHz - 1.5 GHz) - ~$2,099 via TEquipment/Transcat
    - [Windfreak SynthHD v2](https://www.saelig.com/product/synthhd-v2.htm) (10 MHz - 15 GHz, USB) - $2,179 (base SynthHD $1,279); used [eBay search](https://www.ebay.com/sch/i.html?_nkw=Windfreak+SynthHD) ~$700-$1,000 when available

- [ ] **Programmable DC electronic load** - Discharge testing (capacity/IR) for salvaged cells, PD output load-testing
  - Needed for: [Reclaimed-Cell USB-C PD Pack](projects/reclaimed-cell-usbc-pd-pack/)
  - Budget/grey-market:
    - ATORCH DL24P (USB-input, ~150-180W) - ~$27-$46 via [AliExpress official store](https://atorch.aliexpress.com/store/1101249506) (note: atorch.com is a dead/parked domain; real brand site is atorch-electric.com)
    - [MakerHawk 150W/200V/25A Load Tester](https://www.amazon.com/MakerHawk-Battery-Load-Tester-Adjustable/dp/B0DM8Z6D4P) - ~$40-$60
  - New/bench-grade:
    - [Siglent SDL1020X-E](https://www.saelig.com/product/sdl1020x-e.htm) (150V/30A, 200W) - $574.00 (also DigiKey, Circuit Specialists, TestEquity)

- [ ] **Spot welder (18650-capable)** - Nickel strip welding for series/parallel cell packs, safer than soldering cell tops
  - Needed for: [Reclaimed-Cell USB-C PD Pack](projects/reclaimed-cell-usbc-pd-pack/)
  - Budget/grey-market:
    - Generic 18650 spot welder kit, e.g. [Cozyel 5000W Mini Spot Welder](https://www.amazon.com/Cozyel-Battery-Adjustable-Soldering-0-1-0-2mm/dp/B0BMKLJRXT) - ~$40-$90
  - New:
    - [Kweld complete kit](https://www.keenlab.de/index.php/product/kweld-complete-kit/) - €169-177 direct from Keenlab (Germany); US via [Grid Rewired](https://gridrewired.com/en-us/products/kweld-spot-welder-kit) ~$251 (check stock)
    - [Sunkko 709A](https://www.amazon.com/SUNKKO-Battery-Soldering-Welding-Machine/dp/B01JB8VR9E) - $259.99-$279.99 (Banggood/Sunkko MSRP); used [eBay search](https://www.ebay.com/sch/i.html?_nkw=sunkko+709a) ~$200-$340

- [x] **SDR receiver** - RX capable for RF experimentation, spectrum analysis, ADS-B, weather satellites
  - **Acquired:** RTL-SDR Blog V4 (R828D, 500 kHz - 1766 MHz, 1PPM TCXO) — 2026-04-03
- [ ] **SDR transceiver** - TX/RX capable for RF experimentation, ham radio, Zynq projects
  - Budget/Used:
    - [RTL-SDR Blog V4](https://www.rtl-sdr.com/rtl-sdr-blog-v4-dongle-initial-release/) (RX only) — already owned
    - Used USRP B200mini - [eBay search](https://www.ebay.com/sch/i.html?_nkw=usrp+b200mini), ~$800-$1,190 (new starts ~$556)
  - New:
    - [HackRF One](https://www.nooelec.com/store/hackrf.html) (1 MHz - 6 GHz, half-duplex TX/RX) - from $399.95 via Nooelec (greatscottgadgets.com is info-only, not a store)
    - [LimeSDR Mini 2.0](https://www.crowdsupply.com/lime-micro/limesdr-mini-2) (10 MHz - 3.5 GHz, full-duplex) - $399 + $8 shipping, via Crowd Supply
    - [ADALM-PLUTO](https://www.digikey.com/en/products/detail/analog-devices-inc/ADALM-PLUTO/6624230) (325 MHz - 3.8 GHz, full-duplex, hackable to 70 MHz - 6 GHz) - $233.14, via DigiKey

---

*Last updated: 2026-07-22 (Wishlist pricing/links verified against live retailer and eBay data)*
