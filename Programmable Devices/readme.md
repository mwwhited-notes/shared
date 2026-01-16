# Programmable Devices Inventory

Complete collection of FPGA, CPLD, MCU, and other programmable development boards with specifications, programmer compatibility, and organized by device type. Each device has its own directory with detailed specifications and locally archived documentation.

**Quick Reference:** 37 devices across 14 categories | [Documentation Protocol](../.claude/protocols/PROGRAMMABLE_DEVICES_DOCUMENTATION_PROTOCOL.md)

## Table of Contents

- [Quick Reference Summary](#quick-reference-summary)
- [FPGA Development Boards](#fpga-development-boards)
- [SoC Development Boards](#soc-development-boards)
- [Arduino & AVR Boards](#arduino--avr-boards)
- [AVR Microcontrollers](#avr-microcontrollers-standalone)
- [ESP & WiFi Boards](#esp--wifi-boards)
- [ARM Development Boards](#arm-development-boards)
- [IoT & Wireless Boards](#iot--wireless-boards)
- [Wireless Modules](#wireless-modules)
- [PIC Microcontrollers](#pic-microcontrollers)
- [8051-Compatible Microcontrollers](#8051-compatible-microcontrollers)
- [Other Microcontrollers](#other-microcontrollers)
- [CPLDs](#cplds)
- [PLDs & GALs](#plds--gals)
- [Specialty Platforms](#specialty-platforms)
- [Software Resources](#software-resources)
- [Programmer Compatibility](#programmer-compatibility)
- [Collection Value Summary](#collection-value-summary)
- [Cross-References](#cross-references)

---

## Quick Reference Summary

| Category | Device Count | Status | Key Example |
|----------|--------------|--------|------------|
| Arduino & Clones | 6 | Active | Arduino UNO (ATmega328P) |
| AVR Standalone | 5 | Active | ATmega328, ATtiny85 |
| FPGA Development | 3 | Active | Arty A7-100 (Artix-7 101K LUTs) |
| SoC Boards | 1 | Active | Arty Z7-20 (Zynq Dual ARM + FPGA) |
| ESP/WiFi | 4 | Active | Inland ESP32 (Dual-core + BLE) |
| ARM Boards | 3 | Active | STM32 BluePill (Cortex-M3) |
| Wireless Modules | 4 | Active | XBee Pro S1 (1 mile range) |
| PIC & 8051 | 2 | Active | STC 89C52RC (in-circuit ISP) |
| CPLDs/PLDs | 3 | Active | Xilinx XC95108 (108 macrocells) |
| Specialty Platforms | 4 | Active | Gigatron TTL, Anabrid THAT |
| **TOTAL** | **37** | **Active** | - |

---

## Device Index

### FPGA Development Boards

| Board | FPGA/Chip | Logic Cells | RAM | Git Hash | Directory |
|-------|-----------|-------------|-----|----------|-----------|
| [Digilent Arty A7-100](digilent-arty-a7-100/) | Artix-7 XC7A100T | 101,440 | 4,860 Kb | xxxxxxx | `digilent-arty-a7-100/` |
| [Altera EP2C5 Mini](altera-ep2c5-mini/) | Cyclone II EP2C5T144 | 4,608 | 119 Kb | xxxxxxx | `altera-ep2c5-mini/` |
| [NeTV Starter Pack](netv-fpga/) | Spartan-6 XC6SLX9 | 9,152 | 576 Kb | xxxxxxx | `netv-fpga/` |

### SoC Development Boards

| Board | SoC/Chip | Processing System | Programmable Logic | Git Hash | Directory |
|-------|----------|-------------------|-------------------|----------|-----------|
| [Digilent Arty Z7-20](digilent-arty-z7-20/) | Zynq XC7Z020 | Dual Cortex-A9 | 85K Logic Cells | xxxxxxx | `digilent-arty-z7-20/` |

### Arduino / AVR Boards

| Board | MCU | Flash | RAM | Clock | Git Hash | Directory |
|-------|-----|-------|-----|-------|----------|-----------|
| [Arduino UNO](arduino-uno/) | ATmega328P | 32 KB | 2 KB | 16 MHz | xxxxxxx | `arduino-uno/` |
| [Arduino Mega](arduino-mega/) | ATmega2560 | 256 KB | 8 KB | 16 MHz | xxxxxxx | `arduino-mega/` |
| [Arduino Nano](arduino-nano/) | ATmega328P | 32 KB | 2 KB | 16 MHz | xxxxxxx | `arduino-nano/` |
| [Arduino Pro Mini](arduino-pro-mini/) | ATmega328P | 32 KB | 2 KB | 8/16 MHz | xxxxxxx | `arduino-pro-mini/` |
| [Arduino Pro Micro](arduino-pro-micro/) | ATmega32U4 | 32 KB | 2.5 KB | 16 MHz | xxxxxxx | `arduino-pro-micro/` |
| [Arduino Duemilanove](arduino-duemilanove/) | ATmega328P | 32 KB | 2 KB | 16 MHz | xxxxxxx | `arduino-duemilanove/` |

### AVR Microcontrollers (Standalone)

| Chip | Flash | RAM | GPIO | Clock | Git Hash | Directory |
|------|-------|-----|------|-------|----------|-----------|
| [ATtiny2313](attiny2313/) | 2 KB | 128 B | 18 | 20 MHz | xxxxxxx | `attiny2313/` |
| [ATtiny85](attiny85/) | 8 KB | 512 B | 6 | 20 MHz | xxxxxxx | `attiny85/` |
| [ATtiny84A](attiny84a/) | 8 KB | 512 B | 12 | 20 MHz | xxxxxxx | `attiny84a/` |
| [ATmega328](atmega328/) | 32 KB | 2 KB | 23 | 20 MHz | xxxxxxx | `atmega328/` |
| [ATmega32](atmega32/) | 32 KB | 2 KB | 32 | 16 MHz | xxxxxxx | `atmega32/` |

### ESP / WiFi Boards

| Board | MCU | Flash | RAM | Wireless | Git Hash | Directory |
|-------|-----|-------|-----|----------|----------|-----------|
| [ESP8266mod AI-Thinker](esp8266mod-ai-thinker/) | ESP8266 | 4 MB | 80 KB | WiFi 802.11 b/g/n | xxxxxxx | `esp8266mod-ai-thinker/` |
| [Inland ESP32](inland-esp32/) | ESP32-WROOM | 4 MB | 520 KB | WiFi + BLE 4.2 | xxxxxxx | `inland-esp32/` |
| [ESP-01](esp-01/) | ESP8266 | 1 MB | 80 KB | WiFi 802.11 b/g/n | xxxxxxx | `esp-01/` |
| [D1 ESP8266](d1-esp8266/) | ESP8266 | 4 MB | 80 KB | WiFi 802.11 b/g/n | xxxxxxx | `d1-esp8266/` |

### ARM Development Boards

| Board | MCU | Flash | RAM | Clock | Git Hash | Directory |
|-------|-----|-------|-----|-------|----------|-----------|
| [STM32 BluePill](stm32-bluepill/) | STM32F103C8T6 | 64 KB | 20 KB | 72 MHz | xxxxxxx | `stm32-bluepill/` |
| [Netduino Mini](netduino-mini/) | AT91SAM7X512 | 512 KB | 128 KB | 48 MHz | xxxxxxx | `netduino-mini/` |
| [Device Solutions Tahoe II](devicesolutions-tahoe-ii/) | i.MXS (ARM920T) | 4 MB | 8 MB | 100 MHz | xxxxxxx | `devicesolutions-tahoe-ii/` |

### IoT / Wireless Boards

| Board | MCU | Connectivity | Git Hash | Directory |
|-------|-----|--------------|----------|-----------|
| [Spark Core (Particle)](spark-core/) | STM32F103 | WiFi (CC3000) | xxxxxxx | `spark-core/` |
| [RedBear Blend Micro](redbear-blend-micro/) | ATmega32U4 | BLE (nRF8001) | xxxxxxx | `redbear-blend-micro/` |

### Wireless Modules

| Module | Protocol | Frequency | Power | Range | Git Hash | Directory |
|--------|----------|-----------|-------|-------|----------|-----------|
| [MaxStream XBee](maxstream-xbee/) | 802.15.4 | 2.4 GHz | 1 mW | 300 ft | xxxxxxx | `maxstream-xbee/` |
| [Digi XBee Pro S1](digi-xbee-pro-s1/) | 802.15.4 | 2.4 GHz | 60 mW | 1 mile | xxxxxxx | `digi-xbee-pro-s1/` |

### PIC Microcontrollers

| Chip | Flash | RAM | I/O | Clock | Git Hash | Directory |
|------|-------|-----|-----|-------|----------|-----------|
| [PIC16F627](pic16f627/) | 1K words | 224 B | 16 | 4 MHz | xxxxxxx | `pic16f627/` |

### 8051-Compatible Microcontrollers

| Chip | Flash | RAM | Clock | Interface | Git Hash | Directory |
|------|-------|-----|-------|-----------|----------|-----------|
| [STC 89C52RC](stc-89c52rc/) | 8 KB | 512 B | 35 MHz | UART ISP | xxxxxxx | `stc-89c52rc/` |

### Other Microcontrollers

| Chip | Architecture | Flash | RAM | Git Hash | Directory |
|------|--------------|-------|-----|----------|-----------|
| [Zilog Z8 Encore!](zilog-z8/) | Z8 (8-bit CISC) | 8 KB | 512 B | xxxxxxx | `zilog-z8/` |
| [Basic Stamp 2](parallax-basic-stamp-2/) | PBASIC Interpreter | 2 KB EEPROM | 32 B | xxxxxxx | `parallax-basic-stamp-2/` |

### CPLDs

| Device | Macrocells | I/O | Speed | Git Hash | Directory |
|--------|------------|-----|-------|----------|-----------|
| [Xilinx XC95108](xilinx-xc95108/) | 108 | 81 | 7.5 ns | xxxxxxx | `xilinx-xc95108/` |

### PLDs / GALs

| Device | Type | Macrocells | I/O | Git Hash | Directory |
|--------|------|------------|-----|----------|-----------|
| [ATF16V8B](atf16v8b/) | GAL/SPLD | 8 | 8 | xxxxxxx | `atf16v8b/` |
| [AMPAL22V10APC](ampal22v10/) | PAL | 10 | 10 | xxxxxxx | `ampal22v10/` |

### Analog Computers

| Device | Integrators | Summers | Multipliers | Git Hash | Directory |
|--------|-------------|---------|-------------|----------|-----------|
| [Anabrid THAT](anabrid-that/) | 5 | 4 | 2 | xxxxxxx | `anabrid-that/` |

### TTL Computers

| Device | Architecture | Logic Family | Git Hash | Directory |
|--------|--------------|--------------|----------|-----------|
| [Gigatron TTL](gigatron-ttl/) | 8-bit Harvard | 7400 TTL | xxxxxxx | `gigatron-ttl/` |

### Microprocessor Trainers

| Trainer | CPU | RAM | ROM | Directory |
|---------|-----|-----|-----|-----------|
| [NRI/Elenco MM-8000K](mm-8000k/) | Intel 8085A (3 MHz) | 256 B | 2 KB | `mm-8000k/` |

### Retro Computing Kits

| Board | FPGA/MCU | Supported CPUs | Directory |
|-------|----------|----------------|-----------|
| [Multicomp EP2C5-DB](multicomp-ep2c5/) | Cyclone II EP2C5 | Z80, 6502, 6809 | `multicomp-ep2c5/` |

### Robot Kits

| Kit | Type | Control | Directory |
|-----|------|---------|-----------|
| [D2-1 Line Follower](d2-1-line-follower/) | Line Following Robot | Analog (no MCU) | `d2-1-line-follower/` |

### Homebrew Cartridge PCBs

| Item | Platform | Qty | Price | Source | Date |
|------|----------|-----|-------|--------|------|
| NESMaker Compatible NES PCB | NES | 2 | $11.80 | Tindie (mrTentacle) | 2021-02-05 |

---

## Directory Structure

```
├── readme.md                              # This file
├── PROGRAMMABLE_DEVICES_DOCUMENTATION_PROTOCOL.md
├── MISSING_DOCUMENTATION.md               # Tracks failed downloads
│
├── digilent-arty-a7-100/                  # FPGA
├── altera-ep2c5-mini/
├── digilent-arty-z7-20/                   # SoC (Zynq)
│
├── arduino-uno/                           # Arduino/AVR Boards
├── arduino-mega/
├── arduino-nano/
├── arduino-pro-mini/
├── arduino-pro-micro/
├── arduino-duemilanove/
│
├── attiny2313/                            # AVR Standalone
├── attiny85/
├── attiny84a/
├── atmega328/
├── atmega32/
│
├── esp8266mod-ai-thinker/                 # ESP/WiFi
├── inland-esp32/
├── esp-01/
├── d1-esp8266/
│
├── stm32-bluepill/                        # ARM
├── netduino-mini/
├── devicesolutions-tahoe-ii/
│
├── spark-core/                            # IoT/Wireless
├── redbear-blend-micro/
│
├── maxstream-xbee/                        # Wireless Modules
├── digi-xbee-pro-s1/
│
├── pic16f627/                             # PIC
│
├── stc-89c52rc/                           # 8051
│
├── zilog-z8/                              # Other MCUs
├── parallax-basic-stamp-2/
│
├── xilinx-xc95108/                        # CPLD
│
├── atf16v8b/                              # PLD/GAL
├── ampal22v10/
│
├── anabrid-that/                          # Analog Computer
│
├── gigatron-ttl/                          # TTL Computer
│   ├── README.md
│   └── Gigatron_Manual.pdf
│
├── mm-8000k/                              # Microprocessor Trainer
│   └── README.md
│
└── multicomp-ep2c5/                       # Retro Computing Kit
    └── README.md
```

---

## Software Resources

### IDEs & Development Environments

- **Arduino IDE** - Arduino and compatible boards
- **PlatformIO** - Multi-platform embedded development
- **Vivado** - Xilinx FPGA development
- **Vitis** - Xilinx software development (Zynq)
- **STM32CubeIDE** - STM32 development
- **Visual Studio + .NET Micro Framework** - Netduino development
- **Particle CLI / Web IDE** - Particle/Spark development

### Programming Tools

- **AVRDUDE** - AVR programming (Arduino, ATtiny)
- **esptool** - ESP8266/ESP32 flashing
- **stlink** - ST-Link programming tools
- **OpenOCD** - Open On-Chip Debugger
- **dfu-util** - USB DFU programming

### Useful Libraries

- **Arduino Core** - Arduino framework
- **ESP-IDF** - Espressif IoT Development Framework
- **STM32 HAL** - Hardware Abstraction Layer
- **FreeRTOS** - Real-time operating system

---

## Programmer Compatibility

Cross-reference with programmers in `../Test Equipment/`:

### USBasp (AVR ISP)
- Arduino UNO, Mega, Nano, Pro Mini, Pro Micro, Duemilanove (via ICSP)
- ATtiny2313, ATtiny85, ATtiny84A
- ATmega328, ATmega32

### TL866II Plus (Universal)
- ATtiny2313, ATtiny85, ATtiny84A, ATmega328, ATmega32 (socket)
- ATF16V8B, AMPAL22V10APC (GAL/PAL)
- PIC16F627
- STC 89C52RC

### ST-Link V2 (ARM)
- STM32 BluePill

### Altera USB Blaster (FPGA/CPLD)
- Altera EP2C5 Mini (Cyclone II)

### FT232H + xc3sprog (Xilinx CPLD)
- Xilinx XC95108

### Velleman K8048RS (PIC)
- PIC16F627 (requires RS-232 serial port)

### USB-Serial / Built-in USB
- Arduino boards (USB bootloader)
- ESP8266/ESP32 boards (esptool via USB)
- D1 ESP8266 (CH340 USB)
- ESP-01 (requires USB-ESP01 Adapter)

### No Compatible Programmer (Need Additional Hardware)
- Zilog Z8 Encore (requires Zilog USB Smart Cable)
- Digilent Arty A7/Z7 (requires Xilinx Platform Cable or built-in JTAG via USB)
- XBee modules (use XBIB-U-DEV or XBee Explorer via USB)
- Netduino Mini, Tahoe II (USB deployment via .NET MF)

---

## Collection Value Summary

### Documented Purchases

| Item | Category | Price | Source | Date |
|------|----------|-------|--------|------|
| Anabrid THAT | Analog Computer | $529.70 | the-analog-thing.org | 2024-02-24 |
| Digilent Arty A7-100 | FPGA | $0.00 | Gift (Christmas) | 2020-12-25 |
| Digilent Arty Z7-20 | SoC FPGA | $209.00 | Digilent | 2021-11-22 |
| Altera EP2C5 Mini | FPGA | $22.80 | Amazon (get005) | 2014-01-28 |
| Raspberry Pi 3 B+ | SBC | $38.30 | Amazon | 2019-01-28 |
| ATmega328P-PU (×3) | AVR | $12.99 | Amazon | 2019-01-28 |
| NESMaker NES PCB (×2) | Homebrew PCB | $11.80 | Tindie (mrTentacle) | 2021-02-05 |
| Gigatron TTL | TTL Computer | $0.00 | Gift (birthday) | 2020-03-16 |
| MM-8000K | Trainer | $129.00 | Amazon (Zack's Edu Castle) | 2012-12-04 |
| Xilinx XC95108 | CPLD | $0.00 | College | - |
| STM32 BluePill (×5) | ARM | $15.88 | Amazon (Teyleten Robot) | 2023-04-02 |
| Device Solutions Tahoe II | ARM | $0.00 | MS .NET MF competition | - |
| Multicomp EP2C5-DB | Retro FPGA Kit | $16.00 | Tindie (Land Boards) | 2021-02-05 |
| STC 89C52RC (DIY kit) | 8051 | $7.41 | AliExpress (cuiisw) | 2024-03-10 |
| D1 ESP8266 | ESP | $0.36 | AliExpress (diymore) | 2022-12-14 |
| **Documented Total** | | **$993.24** | | |

### Undocumented Equipment

The following items need purchase information added:

| Item | Category |
|------|----------|
| Arduino UNO | Arduino |
| Arduino Mega | Arduino |
| Arduino Nano | Arduino |
| Arduino Pro Mini | Arduino |
| Arduino Pro Micro | Arduino |
| Arduino Duemilanove | Arduino |
| ATtiny2313 | AVR |
| ATtiny85 | AVR |
| ATtiny84A | AVR |
| ATmega32 | AVR |
| ESP8266mod AI-Thinker | ESP |
| Inland ESP32 | ESP |
| ESP-01 | ESP |
| Netduino Mini | ARM |
| Spark Core | IoT |
| RedBear Blend Micro | IoT |
| MaxStream XBee | Wireless |
| Digi XBee Pro S1 | Wireless |
| PIC16F627 | PIC |
| Zilog Z8 Encore | Other MCU |
| Basic Stamp 2 | Other MCU |
| ATF16V8B | PLD |
| AMPAL22V10 | PLD |
| D2-1 Line Follower | Robot Kit |

---

## Notes

- **Arduino UNO/Mega** entries cover both official boards and common clones (CH340/CH341 USB)
- **STM32 BluePill** - Some have 128KB flash despite being marked as 64KB; may have fake STM32 chips
- **ESP-01** requires external USB-serial adapter for programming
- **Netduino Mini** runs .NET Micro Framework (deprecated)
- **Inland ESP32** has unique pinout - labels on bottom of board
- **STC 89C52RC** programs via UART (power cycle to enter ISP mode)
- **ATF16V8B** programmable with TL866II Plus universal programmer
- **AMPAL22V10** is OTP (one-time programmable); use GAL22V10 for development, then program PAL
- **XC95108** can be programmed with FT232H + xc3sprog (not compatible with Altera USB Blaster)
- **Basic Stamp 2** uses PBASIC interpreted language

---

## Cross-References

- [Expansion Boards/](../Expansion%20Boards/) - Arduino shields, Raspberry Pi HATs, BeagleBone capes for these devices
- [Test Equipment/](../Test%20Equipment/) - Programmers, debuggers, oscilloscopes for device development
- [Projects](../projects/) - Active projects using these devices:
  - [fpga-cpu-design/](../projects/fpga-cpu-design/) - Arty A7-100 custom CPU
  - [zynq-soc-exploration/](../projects/zynq-soc-exploration/) - Arty Z7-20 ARM+FPGA
  - [attiny2313-clock/](../projects/attiny2313-clock/) - ATtiny2313 LED clock
  - [analog-computer-experiments/](../projects/analog-computer-experiments/) - Anabrid THAT

---

*Index Version: 1.0*
*Last Updated: 2026-01-16*
*Total Devices: 37 across 14 categories*
*Scope: Complete inventory of microcontrollers, FPGA/CPLD boards, wireless modules, development platforms, and specialty computing hardware*
