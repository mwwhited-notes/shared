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
| [ATtiny2313](attiny2313/) | ATtiny2313 | 2 KB | 128 B | 20 MHz | `attiny2313/` |

### ESP / WiFi Boards

| Board | MCU | Flash | RAM | Wireless | Directory |
|-------|-----|-------|-----|----------|-----------|
| [ESP8266mod AI-Thinker](esp8266mod-ai-thinker/) | ESP8266 | 4 MB | 80 KB | WiFi 802.11 b/g/n | `esp8266mod-ai-thinker/` |
| [Inland ESP32](inland-esp32/) | ESP32-WROOM | 4 MB | 520 KB | WiFi + BLE 4.2 | `inland-esp32/` |
| [ESP-01](esp-01/) | ESP8266 | 1 MB | 80 KB | WiFi 802.11 b/g/n | `esp-01/` |

### ARM Development Boards

| Board | MCU | Flash | RAM | Clock | Directory |
|-------|-----|-------|-----|-------|-----------|
| [STM32 BluePill](stm32-bluepill/) | STM32F103C8T6 | 64 KB | 20 KB | 72 MHz | `stm32-bluepill/` |
| [Netduino Mini](netduino-mini/) | AT91SAM7X512 | 512 KB | 128 KB | 48 MHz | `netduino-mini/` |

### IoT / Wireless Boards

| Board | MCU | Connectivity | Directory |
|-------|-----|--------------|-----------|
| [Spark Core (Particle)](spark-core/) | STM32F103 | WiFi (CC3000) | `spark-core/` |
| [RedBear Blend Micro](redbear-blend-micro/) | ATmega32U4 | BLE (nRF8001) | `redbear-blend-micro/` |

---

## Directory Structure

```
├── readme.md                              # This file
├── PROGRAMMABLE_DEVICES_DOCUMENTATION_PROTOCOL.md
├── digilent-arty-a7-100/
│   └── README.md
├── digilent-arty-z7-20/
│   └── README.md
├── arduino-uno/
│   └── README.md
├── arduino-mega/
│   └── README.md
├── arduino-nano/
│   └── README.md
├── arduino-pro-mini/
│   └── README.md
├── arduino-pro-micro/
│   └── README.md
├── attiny2313/
│   └── README.md
├── esp8266mod-ai-thinker/
│   └── README.md
├── inland-esp32/
│   └── README.md
├── esp-01/
│   └── README.md
├── stm32-bluepill/
│   └── README.md
├── netduino-mini/
│   └── README.md
├── spark-core/
│   └── README.md
└── redbear-blend-micro/
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

## Notes

- **Arduino UNO/Mega** entries cover both official boards and common clones (CH340/CH341 USB)
- **STM32 BluePill** - Some have 128KB flash despite being marked as 64KB
- **ESP-01** requires external USB-serial adapter for programming
- **Netduino Mini** runs .NET Micro Framework

---

*Last updated: December 2024*
