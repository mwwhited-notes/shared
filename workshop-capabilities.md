# Workshop Capabilities & Project Ideas

Quick reference for what this workshop can do and project suggestions when you need inspiration.

**GitHub Profile:** [mwwhited](https://github.com/mwwhited)

**Key Repositories:**
- [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery) - Arduino, AVR, ESP8266, STM32, FPGA (Arty A7/Z7, Cyclone II), CPLD, analog circuits
- [DeviceBridge](https://github.com/mwwhited/DeviceBridge) - TDS2024 Centronics-to-USB adapter (IEEE-1284, Arduino Mega)
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

### Vintage Computers

| System     | Projects                           |
|------------|------------------------------------|
| Apple IIc  | Software, peripherals, restoration |
| Apple IIgs | 16-bit dev, sound/graphics, GS/OS  |
| TI-99/4A   | Cartridges, speech, expansion      |

**Shared Accessories:**
- Floppy Emu (Big Mess O' Wires) - SD-based floppy/HD emulator for Apple II systems
- Greaseweazle V4.1 - USB floppy controller for disk imaging/writing (3" to 8")

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

### Automation & Input

| Tool | Use |
|------|-----|
| Fifine D6 Macro Keypad | 15-key programmable shortcuts, instrument control |

### Programmers

| Programmer         | Targets                       |
|--------------------|-------------------------------|
| TL866II Plus       | EEPROM, Flash, AVR, PIC, GAL  |
| USBasp             | AVR (Arduino, ATtiny, ATmega) |
| ST-Link V2         | STM32, STM8                   |
| Altera USB Blaster | Intel/Altera FPGA, CPLD       |
| FT232H             | Xilinx CPLD (via xc3sprog)    |

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

- [ ] Soft CPU cores (6502, Z80, TMS9900, custom ISA)
- [ ] Retro computer clones (Apple II, TI-99/4A)
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

### Medium Projects (Days to Weeks)

| Project                      | Platform              | Prior Work                                                           |
|------------------------------|-----------------------|----------------------------------------------------------------------|
| GPIB/IEEE-488 adapter        | STM32 + level shift   | [DeviceBridge](https://github.com/mwwhited/DeviceBridge) (IEEE-1284) |
| LANC controller expansion    | Arduino + protocol    | [LANC projects](https://github.com/mwwhited/EmbeddedBakery)          |
| LXI-to-serial gateway        | ESP32 + SCPI          | [LXI Serial Bridge](https://github.com/mwwhited/EmbeddedBakery)      |
| Apple II SmartPort device    | ATmega + CPLD         | [CPLD work](https://github.com/mwwhited/EmbeddedBakery)              |
| TI-99/4A speech synth clone  | FPGA + DAC            | FPGA experience                                                      |
| Ensoniq DOC experiments      | Apple IIgs + code     | Audio/synthesis interest                                             |
| H4n remote interface         | ESP8266 + protocol    | [H4n protocol](https://github.com/mwwhited/EmbeddedBakery)           |
| XBee sensor mesh + dashboard | XBee + ESP32 + web    | ESP + wireless experience                                            |
| Analog + digital hybrid      | THAT + STM32          | [Analog circuits](https://github.com/mwwhited/EmbeddedBakery)        |

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

*Building on your [Arty A7 MicroBlaze and custom CPU work](https://github.com/mwwhited/EmbeddedBakery).*

- [ ] Custom ISA CPU (beyond MicroBlaze)
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

---

## Wishlist (Would Expand Capabilities)

- [ ] Spectrum analyzer (RF work)
- [ ] Isolation transformer (safety)
- [ ] Bench LCR meter (in-circuit SMD)
- [ ] Reflow oven (batch SMD assembly)
- [ ] Hot air pencil (finer SMD work)
- [ ] Current probe for scope
- [ ] Higher resolution thermal camera
- [ ] Variac (motor testing)

---

*Last updated: December 2025*
