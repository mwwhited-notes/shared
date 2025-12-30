# Project Ideas

Personal project backlog with notes on progress and equipment.

---

## Active / In Progress

* Designing my own CPU/computer (and learn system verilog) [I have most of the ALU and a text graphics engine from a few years ago. Use Arty A7-100.]
* build out that clock (attiny2313) [the new LED screen showed up so I can solder it up now and I need to tweak the counter to see if I can get it to keep time better.] This project was mostly about building something semiuseful with an ATTiny and learning how to built out the ISP (In-circuit Serial Programmer) interface
* play around with SCPI (standard commands for programmable instruments) to control the test equipment on my bench and probably write my own VISA driver for .Net Core (might also build a RS-232/ethernet gateway or USB them into a raspberry pi/beagle bone black) [have HP 34401A, Rigol DM3058E, Rigol DG1022, Korad supplies]
* build out an analog computer/integrator (opamps for math because why not) [Have Anabrid THAT now!]
* build out a UI for an Intel 8085 trainer [MM-8000K hardware + MM8000 emulator on GitHub]
* play around with SoC (system on a chip) based on the Xilinx Zynq Z7 [Have Arty Z7-20]

---

## Backlog

### Vintage Computing & Retro

* write a simple game for the NES and Apple II (program in 6502 assembly) [have NESMaker PCBs, Apple IIc, Apple IIgs]
* archive floppy disk collection with Greaseweazle V4.1 [have Apple II 5.25", Apple IIgs 3.5", TI-99/4A disks]
* build Multicomp Z80 CP/M system on EP2C5-DB [have Multicomp kit, Grant Searle designs available]
* build Multicomp 6502 system with BASIC [good prep for Apple II projects]
* build Multicomp 6809 Flex/OS-9 system [learn another 8-bit architecture]
* Gigatron TTL expansion or game development [have Gigatron TTL computer]
* TI-99/4A cartridge development [have TI-99/4A with speech synthesizer]

### FPGA & CPU Design

* 8085 soft core on FPGA [have MM-8000K as reference, Arty A7]
* 65C816 soft core (Apple IIgs compatible) [would enable IIgs clone]
* TMS9900 soft core (TI-99/4A compatible) [would enable TI-99 clone]
* VGA/HDMI framebuffer controller [needed for retro cores]
* custom ISA CPU design [building on ALU work]

### Protocol Bridges & Interfaces

* GPIB/IEEE-488 USB adapter [for HP 34401A and other GPIB instruments, builds on DeviceBridge work]
* LXI/SCPI instrument automation gateway [ESP32 + instruments]
* Centronics-to-WiFi print server [builds on DeviceBridge parallel port work]
* H4n recorder remote interface [have protocol documented]
* LANC camera controller expansion [have LANC work in EmbeddedBakery]

### Wireless & IoT

* XBee mesh sensor network with dashboard [have XBee modules + XBIB-U-DEV]
* XBee-to-MQTT gateway [ESP32 + XBee]
* battery-powered remote sensor nodes [ATtiny + XBee]
* ESP32 home automation projects [have Inland ESP32, ESP8266 modules]

### Analog & Mixed Signal

* Lorenz attractor on The Analog Thing [chaos visualization]
* predator-prey ecosystem simulation [classic analog computing demo]
* hybrid analog-digital system [THAT + STM32 interface]
* control system modeling [PID loops, feedback systems]

### Learning & Exploration

* play around more with diode logic (working though this in combination with trying to reverse engineer programming some old PAL chips helped me understand how "high voltage" programmers work as well as ROM, SRAM, and more about combinational logic)
* D2-1 line follower robot enhancements [add MCU to analog base]
* Velleman K8055 automation projects [USB I/O board for PC control]
* build out multi-axis hand controller to work with oculus/hololens
* design and build a handheld/bench calculator that will also function as a simple I/O interface for parallel and serial interfaces

---

## Equipment Enabling New Projects

Recent inventory additions that enable new project categories:

| Equipment | Projects Enabled |
|-----------|------------------|
| Greaseweazle V4.1 | Floppy disk archival, vintage disk preservation |
| Multicomp EP2C5-DB | Z80/6502/6809 retro computing, CP/M, BASIC |
| Anabrid THAT | Analog computing, chaos systems, hybrid digital |
| XBee modules + XBIB-U-DEV | Mesh networking, remote sensors |
| Gigatron TTL | TTL computing, expansion modules |
| D2-1 Line Follower | Robot enhancement, sensor fusion |

---

*Last updated: December 2025 (Project Review Protocol sync)*
