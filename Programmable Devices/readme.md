# Programmable Devices Inventory

Personal collection of FPGA, CPLD, MCU, and other programmable development boards with specifications, documentation links, and software resources.

Each device has its own directory with detailed specifications and locally archived documentation.

**[Programmable Devices Documentation Protocol](PROGRAMMABLE_DEVICES_DOCUMENTATION_PROTOCOL.md)** - Guide for adding new devices and maintaining this inventory.

---

## Device Index

### FPGA Development Boards

| Board | FPGA/Chip | Logic Cells | RAM | Directory |
|-------|-----------|-------------|-----|-----------|
| [Digilent Arty A7-100](digilent-arty-a7-100/) | Artix-7 XC7A100T | 101,440 | 4,860 Kb | `digilent-arty-a7-100/` |
| [Altera EP2C5 Mini](altera-ep2c5-mini/) | Cyclone II EP2C5T144 | 4,608 | 119 Kb | `altera-ep2c5-mini/` |

### SoC Development Boards

| Board | SoC/Chip | Processing System | Programmable Logic | Directory |
|-------|----------|-------------------|-------------------|-----------|
| [Digilent Arty Z7-20](digilent-arty-z7-20/) | Zynq XC7Z020 | Dual Cortex-A9 | 85K Logic Cells | `digilent-arty-z7-20/` |

### Arduino / AVR Boards

| Board | MCU | Flash | RAM | Clock | Directory |
|-------|-----|-------|-----|-------|-----------|
| [Arduino UNO](arduino-uno/) | ATmega328P | 32 KB | 2 KB | 16 MHz | `arduino-uno/` |
| [Arduino Mega](arduino-mega/) | ATmega2560 | 256 KB | 8 KB | 16 MHz | `arduino-mega/` |
| [Arduino Nano](arduino-nano/) | ATmega328P | 32 KB | 2 KB | 16 MHz | `arduino-nano/` |
| [Arduino Pro Mini](arduino-pro-mini/) | ATmega328P | 32 KB | 2 KB | 8/16 MHz | `arduino-pro-mini/` |
| [Arduino Pro Micro](arduino-pro-micro/) | ATmega32U4 | 32 KB | 2.5 KB | 16 MHz | `arduino-pro-micro/` |
| [Arduino Duemilanove](arduino-duemilanove/) | ATmega328P | 32 KB | 2 KB | 16 MHz | `arduino-duemilanove/` |

### AVR Microcontrollers (Standalone)

| Chip | Flash | RAM | GPIO | Clock | Directory |
|------|-------|-----|------|-------|-----------|
| [ATtiny2313](attiny2313/) | 2 KB | 128 B | 18 | 20 MHz | `attiny2313/` |
| [ATtiny85](attiny85/) | 8 KB | 512 B | 6 | 20 MHz | `attiny85/` |
| [ATtiny84A](attiny84a/) | 8 KB | 512 B | 12 | 20 MHz | `attiny84a/` |
| [ATmega328](atmega328/) | 32 KB | 2 KB | 23 | 20 MHz | `atmega328/` |
| [ATmega32](atmega32/) | 32 KB | 2 KB | 32 | 16 MHz | `atmega32/` |

### ESP / WiFi Boards

| Board | MCU | Flash | RAM | Wireless | Directory |
|-------|-----|-------|-----|----------|-----------|
| [ESP8266mod AI-Thinker](esp8266mod-ai-thinker/) | ESP8266 | 4 MB | 80 KB | WiFi 802.11 b/g/n | `esp8266mod-ai-thinker/` |
| [Inland ESP32](inland-esp32/) | ESP32-WROOM | 4 MB | 520 KB | WiFi + BLE 4.2 | `inland-esp32/` |
| [ESP-01](esp-01/) | ESP8266 | 1 MB | 80 KB | WiFi 802.11 b/g/n | `esp-01/` |
| [D1 ESP8266](d1-esp8266/) | ESP8266 | 4 MB | 80 KB | WiFi 802.11 b/g/n | `d1-esp8266/` |

### ARM Development Boards

| Board | MCU | Flash | RAM | Clock | Directory |
|-------|-----|-------|-----|-------|-----------|
| [STM32 BluePill](stm32-bluepill/) | STM32F103C8T6 | 64 KB | 20 KB | 72 MHz | `stm32-bluepill/` |
| [Netduino Mini](netduino-mini/) | AT91SAM7X512 | 512 KB | 128 KB | 48 MHz | `netduino-mini/` |
| [Device Solutions Tahoe II](devicesolutions-tahoe-ii/) | i.MXS (ARM920T) | 4 MB | 8 MB | 100 MHz | `devicesolutions-tahoe-ii/` |

### IoT / Wireless Boards

| Board | MCU | Connectivity | Directory |
|-------|-----|--------------|-----------|
| [Spark Core (Particle)](spark-core/) | STM32F103 | WiFi (CC3000) | `spark-core/` |
| [RedBear Blend Micro](redbear-blend-micro/) | ATmega32U4 | BLE (nRF8001) | `redbear-blend-micro/` |

### Wireless Modules

| Module | Protocol | Frequency | Power | Range | Directory |
|--------|----------|-----------|-------|-------|-----------|
| [MaxStream XBee](maxstream-xbee/) | 802.15.4 | 2.4 GHz | 1 mW | 300 ft | `maxstream-xbee/` |
| [Digi XBee Pro S1](digi-xbee-pro-s1/) | 802.15.4 | 2.4 GHz | 60 mW | 1 mile | `digi-xbee-pro-s1/` |

### PIC Microcontrollers

| Chip | Flash | RAM | I/O | Clock | Directory |
|------|-------|-----|-----|-------|-----------|
| [PIC16F627](pic16f627/) | 1K words | 224 B | 16 | 4 MHz | `pic16f627/` |

### 8051-Compatible Microcontrollers

| Chip | Flash | RAM | Clock | Interface | Directory |
|------|-------|-----|-------|-----------|-----------|
| [STC 89C52RC](stc-89c52rc/) | 8 KB | 512 B | 35 MHz | UART ISP | `stc-89c52rc/` |

### Other Microcontrollers

| Chip | Architecture | Flash | RAM | Directory |
|------|--------------|-------|-----|-----------|
| [Zilog Z8 Encore!](zilog-z8/) | Z8 (8-bit CISC) | 8 KB | 512 B | `zilog-z8/` |
| [Basic Stamp 2](parallax-basic-stamp-2/) | PBASIC Interpreter | 2 KB EEPROM | 32 B | `parallax-basic-stamp-2/` |

### CPLDs

| Device | Macrocells | I/O | Speed | Directory |
|--------|------------|-----|-------|-----------|
| [Xilinx XC95108](xilinx-xc95108/) | 108 | 81 | 7.5 ns | `xilinx-xc95108/` |

### PLDs / GALs

| Device | Type | Macrocells | I/O | Directory |
|--------|------|------------|-----|-----------|
| [ATF16V8B](atf16v8b/) | GAL/SPLD | 8 | 8 | `atf16v8b/` |
| [AMPAL22V10APC](ampal22v10/) | PAL | 10 | 10 | `ampal22v10/` |

### Analog Computers

| Device | Integrators | Summers | Multipliers | Directory |
|--------|-------------|---------|-------------|-----------|
| [Anabrid THAT](anabrid-that/) | 5 | 4 | 2 | `anabrid-that/` |

### TTL Computers

| Device | Architecture | Logic Family | Directory |
|--------|--------------|--------------|-----------|
| [Gigatron TTL](gigatron-ttl/) | 8-bit Harvard | 7400 TTL | `gigatron-ttl/` |

### Retro Computing Kits

| Board | FPGA/MCU | Supported CPUs | Directory |
|-------|----------|----------------|-----------|
| [Multicomp EP2C5-DB](multicomp-ep2c5/) | Cyclone II EP2C5 | Z80, 6502, 6809 | `multicomp-ep2c5/` |

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

*Last updated: December 2024*
