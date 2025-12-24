# Workshop Capabilities & Project Ideas

Quick reference for what this workshop can do and project suggestions when you need inspiration.

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

| Category | Devices | Best For |
|----------|---------|----------|
| **FPGA** | Artix-7 (100K LCs), Cyclone II | Custom logic, retro clones, DSP |
| **SoC** | Zynq (ARM + FPGA) | Linux + hardware acceleration |
| **Arduino/AVR** | UNO, Mega, Nano, ATtiny, ATmega | Prototyping, sensors, simple control |
| **ESP WiFi** | ESP8266, ESP32 | IoT, home automation, wireless |
| **ARM** | STM32 BluePill | USB devices, RTOS, performance |
| **Wireless** | XBee, BLE modules | Mesh networks, remote sensors |
| **Analog** | The Analog Thing | ODEs, control systems, simulation |
| **Legacy** | PIC, 8051, Z8, Basic Stamp | Specific applications, learning |
| **CPLD/GAL** | XC95108, ATF16V8B | Glue logic, vintage chip replacement |

### Vintage Computers

| System | Projects |
|--------|----------|
| Apple IIc | Software, peripherals, restoration |
| Apple IIgs | 16-bit dev, sound/graphics, GS/OS |
| TI-99/4A | Cartridges, speech, expansion |

### Test & Measurement

| Category | Equipment | Capability |
|----------|-----------|------------|
| **Oscilloscope** | 200 MHz DSO, 150 MHz analog | Debug signals to ~50 MHz |
| **Multimeter** | 6½ digit HP 34401A | Precision measurements |
| **LCR Meter** | 100 kHz DE-5000 | Component characterization |
| **Logic Analyzer** | 16 ch @ 100 MSa/s | Digital protocol debug |
| **Power Supply** | 30V/5A, 60V/3A | Most bench projects |
| **Thermal** | FLIR TG130 (80x60) | Hot spot detection |
| **Microscope** | 3.5X-90X stereo + 5MP camera, 40X-2000X compound | SMD work, inspection, imaging |
| **Document Camera** | Kitchbar KB-700 (8MP) | PCB photos, documentation |

### Assembly & Rework

| Tool | Use |
|------|-----|
| KSGER T12 | Soldering (10 tip shapes) |
| YaeCCC 858D | Hot air SMD rework |
| Hakko FR-301 | Through-hole desoldering |
| Stereo microscope | SMD inspection/placement |
| Microscope camera | Capture images/video of work |
| Document camera | PCB overview photos, tutorials |

### Programmers

| Programmer | Targets |
|------------|---------|
| TL866II Plus | EEPROM, Flash, AVR, PIC, GAL |
| USBasp | AVR (Arduino, ATtiny, ATmega) |
| ST-Link V2 | STM32, STM8 |
| Altera USB Blaster | Intel/Altera FPGA, CPLD |
| FT232H | Xilinx CPLD (via xc3sprog) |

---

## What Can I Build?

### Electronics & Embedded

- [ ] Custom Arduino shields
- [ ] ESP8266/ESP32 IoT devices
- [ ] Wireless sensor networks (XBee mesh)
- [ ] USB HID devices (STM32)
- [ ] Motor controllers
- [ ] LED matrix displays
- [ ] Audio synthesizers
- [ ] Data loggers
- [ ] Environmental monitors

### FPGA Projects

- [ ] Soft CPU cores (RISC-V, 6502, Z80)
- [ ] Retro computer clones
- [ ] Video signal generators
- [ ] DSP filters
- [ ] Logic analyzers
- [ ] Custom peripherals
- [ ] Hardware accelerators

### Analog Computing

- [ ] Lorenz attractor (chaos)
- [ ] Predator-prey simulation
- [ ] Mechanical oscillator models
- [ ] Control system simulation
- [ ] RC circuit analysis
- [ ] Hybrid analog-digital systems

### Vintage Computing

- [ ] Apple II software development
- [ ] TI-99/4A cartridge creation
- [ ] Custom expansion cards
- [ ] GAL replacements for failed chips
- [ ] Composite video mods
- [ ] Floppy emulators (Gotek/FlashFloppy)

---

## What Can I Fix?

### With Current Equipment

| Problem | Tools Needed | Can Do? |
|---------|--------------|---------|
| Dead power supply | DMM, scope, thermal | ✓ |
| Bad capacitors | Soldering, ESR meter | ✓ |
| Failed through-hole IC | Desoldering gun | ✓ |
| Failed SMD IC | Hot air, microscope | ✓ |
| Bad solder joints | Microscope, soldering | ✓ |
| Intermittent connection | Scope, thermal | ✓ |
| Logic IC failure | Logic analyzer, TL866 | ✓ |
| EEPROM/Flash corruption | TL866II Plus | ✓ |
| GAL/PAL failure | TL866II Plus + new GAL | ✓ |
| Vintage computer repair | All of the above | ✓ |
| Serial/I2C/SPI debug | Bus Pirate, logic analyzer | ✓ |
| USB device issues | Scope, protocol analyzer | ✓ |

### Repair Workflow

1. **Visual inspection** - Microscope for damaged components
2. **Thermal scan** - FLIR for hot spots
3. **Power check** - DMM for voltages
4. **Signal trace** - Scope for waveforms
5. **Protocol debug** - Logic analyzer for digital
6. **Component test** - LCR meter, TL866
7. **Rework** - Solder/hot air/desolder as needed

---

## Project Ideas by Difficulty

### Beginner (Hours to Days)

| Project | Platform | Skills |
|---------|----------|--------|
| Blink LED | Arduino | Basic |
| Temperature logger | ESP8266 + DHT22 | WiFi, sensors |
| USB volume knob | Arduino Pro Micro | USB HID |
| IR remote decoder | Arduino + IR sensor | Protocols |
| EEPROM reader/writer | Arduino + I2C EEPROM | I2C |
| Logic probe | ATtiny85 | Simple circuits |
| Persistence of vision | Arduino + LEDs | Timing |

### Intermediate (Days to Weeks)

| Project | Platform | Skills |
|---------|----------|--------|
| Wireless sensor node | ESP32 + sensors | WiFi, MQTT |
| MIDI controller | Arduino Pro Micro | USB MIDI |
| Frequency counter | Arduino + prescaler | Timing, display |
| CNC pendant | STM32 + encoder | USB, interrupts |
| Analog synth module | Op-amps + Arduino | Analog + digital |
| XBee mesh network | XBee + Arduino | Wireless protocols |
| SD card oscilloscope | STM32 + ADC | High-speed sampling |
| GPS tracker | ESP32 + GPS | Location, cellular |

### Advanced (Weeks to Months)

| Project | Platform | Skills |
|---------|----------|--------|
| 6502 on FPGA | Arty A7 | Verilog, CPU design |
| TI-99/4A cartridge | CPLD + Flash | Vintage, CPLD |
| Apple II clone core | Arty A7 | FPGA, retro |
| Hybrid analog-digital | THAT + MCU | Analog computing |
| USB protocol analyzer | Zynq | High-speed, USB |
| SDR receiver | Zynq + ADC | RF, DSP |
| Ben Eater CPU in HDL | Arty A7 | CPU architecture |
| Video game console | Arty A7 | Graphics, audio |
| Analog computer sim | THAT | Differential equations |
| Custom logic analyzer | FPGA + SRAM | High-speed capture |

---

## Project Ideas by Category

### Home Automation

- [ ] ESP8266 smart outlet
- [ ] Temperature/humidity monitor
- [ ] Garage door controller
- [ ] Plant watering system
- [ ] Motion-activated lighting
- [ ] Energy monitor (CT clamp)
- [ ] HVAC zone controller

### Audio/Music

- [ ] MIDI controller
- [ ] Analog synthesizer module
- [ ] Audio spectrum analyzer
- [ ] Guitar effects pedal
- [ ] Chiptune player (SID, AY-3-8910)
- [ ] Apple IIgs Ensoniq projects

### Retro Computing

- [ ] Floppy drive emulator
- [ ] Composite to HDMI converter
- [ ] PS/2 to vintage keyboard adapter
- [ ] ROM cartridge with flash
- [ ] Reproduction PCBs
- [ ] Failed chip replacement (GAL)
- [ ] Memory expansion

### Test Equipment

- [ ] Curve tracer
- [ ] Component tester
- [ ] Logic analyzer (FPGA-based)
- [ ] Frequency counter
- [ ] Signal generator
- [ ] ESR meter
- [ ] Cable tester

### Learning Projects

- [ ] 555 timer circuits
- [ ] Op-amp experiments
- [ ] Analog computing basics (THAT)
- [ ] 8-bit CPU (Ben Eater style in HDL)
- [ ] FPGA basics (blinky to UART)
- [ ] Bare metal ARM programming
- [ ] Assembly language (6502, Z80, ARM)

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
