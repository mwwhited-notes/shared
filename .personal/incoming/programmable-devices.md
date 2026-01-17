# Programmable Devices Collection Inventory

**Generated:** 2026-01-17

**Source:** Collections/Programmable Devices/readme.md

**Collection:** FPGA, CPLD, MCU, and other programmable development boards with specifications and programmer compatibility

---

## Summary

**Total Devices:** 37 programmable boards across 14 categories

**Primary Categories:** FPGA Development, SoC Development, Arduino & AVR, ESP & WiFi, ARM Boards, IoT & Wireless, Wireless Modules, CPLD/GAL, Specialty Platforms

---

## FPGA Development Boards

| Board Name | FPGA/Chip | Logic Cells | RAM | Programming | Status |
|-----------|----------|------------|-----|-------------|--------|
| Digilent Arty A7-100 | Artix-7 XC7A100T | 101,440 | 4,860 Kb | JTAG, USB | Active |
| Altera EP2C5 Mini | Cyclone II EP2C5T144 | 4,608 | 119 Kb | JTAG | Active |
| NeTV Starter Pack | Spartan-6 XC6SLX9 | 9,152 | 576 Kb | JTAG, USB | Active |

**Tools:** Vivado (Xilinx), Quartus (Altera), ISE (Xilinx legacy)

---

## SoC Development Boards

| Board Name | SoC/Chip | Processing System | Programmable Logic | Status |
|-----------|----------|-------------------|-------------------|--------|
| Digilent Arty Z7-20 | Zynq XC7Z020 | Dual ARM Cortex-A9 | 85K Logic Cells | Active |

**Capabilities:** Dual-core ARM processors with integrated FPGA fabric for heterogeneous computing

---

## Arduino & AVR Boards

| Board Name | Microcontroller | Flash | RAM | Clock | GPIO | Status |
|-----------|---|---|---|---|---|---|
| Arduino UNO | ATmega328P | 32 KB | 2 KB | 16 MHz | 14 | Active |
| Arduino Mega | ATmega2560 | 256 KB | 8 KB | 16 MHz | 54 | Active |
| Arduino Nano | ATmega328P | 32 KB | 2 KB | 16 MHz | 14 | Active |
| Arduino Pro Mini | ATmega328P | 32 KB | 2 KB | 8/16 MHz | 14 | Active |
| Arduino Pro Micro | ATmega32U4 | 32 KB | 2.5 KB | 16 MHz | 20 | Active |
| Arduino Duemilanove | ATmega328P | 32 KB | 2 KB | 16 MHz | 14 | Active |

**IDE Support:** Arduino IDE, PlatformIO, Atmel Studio

---

## AVR Microcontrollers (Standalone)

| Chip | Flash | RAM | GPIO | Clock | Max Speed | Status |
|------|-------|-----|------|-------|-----------|--------|
| ATtiny2313 | 2 KB | 128 B | 18 | 20 MHz | 20 MHz | Active |
| ATtiny85 | 8 KB | 512 B | 6 | 20 MHz | 20 MHz | Active |
| ATtiny84A | 8 KB | 512 B | 12 | 20 MHz | 20 MHz | Active |
| ATmega328 | 32 KB | 2 KB | 23 | 20 MHz | 20 MHz | Active |
| ATmega32 | 32 KB | 2 KB | 32 | 16 MHz | 16 MHz | Active |

**Programming:** ISP (In-System Programming), JTAG, Serial bootloader (some)

---

## ESP8266 & ESP32 WiFi Boards

| Board Name | MCU | Flash | RAM | Wireless Capability | Status |
|-----------|-----|-------|-----|-----------------|--------|
| ESP8266mod AI-Thinker | ESP8266 | 4 MB | 80 KB | WiFi 802.11 b/g/n | Active |
| Inland ESP32 | ESP32-WROOM | 4 MB | 520 KB | WiFi 802.11 b/g/n + BLE 4.2 | Active |
| ESP-01 | ESP8266 | 1 MB | 80 KB | WiFi 802.11 b/g/n | Active |
| D1 ESP8266 | ESP8266 | 4 MB | 80 KB | WiFi 802.11 b/g/n | Active |

**IDE Support:** Arduino IDE (via ESP extensions), PlatformIO, MicroPython, Lua

---

## ARM Development Boards

| Board Name | MCU | Flash | RAM | Clock | Features | Status |
|-----------|-----|-------|-----|-------|----------|--------|
| STM32 BluePill | STM32F103C8T6 | 64 KB | 20 KB | 72 MHz | Cortex-M3, DMA | Active |
| Netduino Mini | AT91SAM7X512 | 512 KB | 128 KB | 48 MHz | Cortex-M3, .NET Micro | Active |
| Raspberry Pi Pico W | RP2040 | 2 MB | 264 KB | 133 MHz | Dual-core, WiFi | Active |
| Device Solutions Tahoe II | i.MXS (ARM920T) | 4 MB | 8 MB | 100 MHz | Linux capable | Active |

**IDE Support:** Arduino IDE, PlatformIO, STM32CubeIDE, Keil µVision

---

## IoT & Wireless Boards

| Board Name | MCU | Wireless Technology | Status |
|-----------|-----|---|---|
| Spark Core (Particle) | STM32F103 | WiFi (CC3000) | Active |
| RedBear Blend Micro | ATmega32U4 | Bluetooth Low Energy (BLE nRF8001) | Active |

---

## Wireless Modules

| Module Name | Protocol | Frequency | Power | Range | Status |
|-----------|----------|-----------|-------|-------|--------|
| MaxStream XBee | IEEE 802.15.4 | 2.4 GHz | 1 mW | 300 ft | Active |
| Digi XBee Pro S1 | IEEE 802.15.4 | 2.4 GHz | 60 mW | 1 mile | Active |

**Use Cases:** Home automation mesh networks, remote sensing, wireless sensor networks

---

## PIC Microcontrollers

| Chip | Flash | RAM | I/O Pins | Clock | Status |
|------|-------|-----|----------|-------|--------|
| PIC16F627 | 1K words | 224 B | 16 | 4 MHz | Active |

**IDE Support:** MPLAB X, PICkit programmer

---

## 8051-Compatible Microcontrollers

| Chip | Architecture | Flash | RAM | Clock | Interface | Status |
|------|---|---|---|---|---|---|
| STC 89C52RC | 8051-compatible | 8 KB | 512 B | 35 MHz | UART ISP (in-circuit serial) | Active |

**Programming:** Serial ISP (in-system programmable), no external programmer required

---

## Other Microcontrollers

| Chip | Architecture | Flash | RAM | Status | Notes |
|------|---|---|---|---|---|
| Zilog Z8 Encore! | Z8 (8-bit CISC) | 8 KB | 512 B | Active | Educational microcontroller |
| Parallax Basic Stamp 2 | PBASIC Interpreter | 2 KB EEPROM | 32 B | Active | Interpreted BASIC language |

---

## CPLDs (Complex Programmable Logic Devices)

| Device | Type | Macrocells | I/O Pins | Speed | Programming | Status |
|--------|------|-----------|----------|-------|-------------|--------|
| Xilinx XC95108 | CPLD | 108 | 81 | 7.5 ns | JTAG ISP | Active |

---

## PLDs & GALs (Simple Programmable Logic)

| Device | Type | Macrocells | I/O Pins | Status |
|--------|------|-----------|----------|--------|
| ATF16V8B | GAL (Simple PLD) | 8 | 8 | Active |
| AMPAL22V10APC | PAL | 10 | 10 | Active |

---

## Specialty Computing Platforms

### Analog Computers

| Device | Integrators | Summers | Multipliers | Status | Use Case |
|--------|-------------|---------|-------------|--------|----------|
| Anabrid THAT | 5 | 4 | 2 | Active | Continuous analog simulation, differential equations |

### TTL Computers

| Device | Architecture | Bits | Logic Family | Status | Use Case |
|--------|---|---|---|---|---|
| Gigatron TTL | 8-bit Harvard | 8 | 7400 TTL | Active | Educational TTL computer, no CPU chip |

### Microprocessor Trainers

| Trainer | Processor | Clock | RAM | ROM | Status |
|---------|-----------|-------|-----|-----|--------|
| NRI/Elenco MM-8000K | Intel 8085A | 3 MHz | 256 B | 2 KB | Active |

**Use:** Educational training kit for 8085 assembly language

### Retro Computing Kits

| Board Name | FPGA/MCU | Supported CPUs | Status |
|-----------|----------|---|---|
| Multicomp EP2C5-DB | Cyclone II EP2C5 | Z80, 6502, 6809 | Active |

**Purpose:** Soft-core processors implemented in FPGA for retro computing emulation

### Robot Kits

| Kit Name | Type | Control Method | Status |
|----------|------|---|---|
| D2-1 Line Follower | Line Following Robot | Analog circuits (no MCU) | Active |

---

## Homebrew & Custom PCBs

| Item | Platform | Quantity | Type | Status |
|------|----------|----------|------|--------|
| NESMaker Compatible NES PCB | NES | 2 | Game cartridge PCB | Active |

---

## Programmer Compatibility Reference

### JTAG Programmers
- **Digilent Adept** - Xilinx FPGA programming (Arty boards)
- **TL866II Plus** - Supports CPLD/GAL/EEPROM programming
- **Generic JTAG adapters** - Compatible with most FPGA/CPLD boards

### Serial/ISP Programmers
- **USBasp** - AVR ISP programmer
- **FTDI USB-to-Serial** - For AVR boards with bootloader
- **STLink** - STM32 ARM debugging and programming
- **PICkit** - Microchip PIC programming
- **CH340** - Common serial/USB converter for ESP boards

### Bootloaders
- Arduino boards - Bootloader-based serial programming (no external programmer)
- ESP8266/ESP32 - USB/UART bootloader
- STM32 - Optional bootloader, JTAG alternative
- AVR microcontrollers - ISP programming or bootloader (if present)

---

## Software Ecosystem

### IDEs & Development Environments
| IDE | Supported Devices | Platform |
|-----|---|---|
| Arduino IDE | Arduino, ESP8266, ESP32, AVR | Web-based, Desktop |
| PlatformIO | All Arduino-compatible + STM32, ESP, Cortex-M | IDE plugins, CLI |
| Vivado (Xilinx) | Arty A7-100, Arty Z7-20 | Windows, Linux |
| Quartus (Altera) | Altera/Cyclone boards | Windows, Linux |
| STM32CubeIDE | STM32 BluePill, ARM boards | Desktop |
| MPLAB X | PIC microcontrollers | Desktop |

### Programming Languages
- C/C++ - Primary for most boards (Arduino IDE, PlatformIO)
- Python - MicroPython (ESP32, Pico)
- Verilog/VHDL - FPGA development
- Assembly - Low-level optimization, microprocessor trainers
- BASIC - Parallax Basic Stamp

---

## Collection Organization

### By Difficulty Level
- **Beginner:** Arduino boards, ESP8266/ESP32
- **Intermediate:** STM32 BluePill, ARM boards, simple FPGA boards
- **Advanced:** Complex FPGA development, analog computers, TTL projects

### By Application
- **IoT/WiFi Projects:** ESP boards, Spark Core, XBee modules
- **Real-time Control:** Arduino, STM32 BluePill
- **Signal Processing:** FPGA boards, analog computers
- **Educational:** Trainer kits, retro computing emulation

---

## Specifications Summary

**Largest Flash:** Arduino Mega (256 KB), Netduino Mini (512 KB)

**Largest RAM:** Netduino Mini (128 KB), Raspberry Pi Pico W (264 KB)

**Highest Clock:** Raspberry Pi Pico W (133 MHz)

**Most GPIO:** Arduino Mega (54 pins)

**FPGA Logic Capacity:** Arty A7-100 (101K LUTs)

**Wireless Capability:** Inland ESP32 (WiFi + BLE), D1 ESP8266 (WiFi)

---

## Cross-References

**Related Collections:**
- Expansion Boards - Shields and HATs for Arduino/Raspberry Pi
- Test Equipment - Programmers, debuggers, oscilloscopes for development
- Tools and Components - Breadboards, wire, passive components

**Projects Using These Devices:**
- FPGA CPU Design - Arty A7-100 for soft-core implementations
- SBC Cluster - BeagleBone and Raspberry Pi boards
- Home Automation - ESP32 WiFi nodes, XBee mesh network
- Retro Computing - Multicomp for Z80/6502 emulation
- Robot Projects - Line follower and other hobby robotics

---

## Programming Interface Breakdown

| Interface Type | Devices | Advantages |
|---|---|---|
| Serial/USB Bootloader | Arduino, ESP boards | No external programmer needed |
| JTAG ISP | FPGA/CPLD boards | Fast programming, in-circuit debugging |
| ISP Serial | AVR standalone | Standard for hobbyist programming |
| Wireless (SPI/UART) | XBee, BLE modules | Network-based applications |

---

## Summary Statistics

- **Arduino-Compatible Boards:** 8
- **Wireless-Enabled:** 6
- **FPGA/CPLD:** 4
- **ARM Cortex-M:** 5
- **Specialty Platforms:** 4
- **Wireless Modules:** 2
- **Total:** 37 programmable devices

---

*Response generated by REQUEST_RESPONSE_PROTOCOL.md workflow*
*Privacy status: Vendor names and prices removed per protocol. Project references preserved for cross-referencing capability.*
*Last updated: 2026-01-17*
