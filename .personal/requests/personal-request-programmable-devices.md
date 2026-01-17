# Personal Request: Programmable Devices Inventory

## What We Need

Current inventory of development boards, microcontrollers, and FPGA boards from Personal/Programmable Devices collection.

## Use Case

`workshop-capabilities.md` and multiple projects reference specific programmable devices. This information is essential for:
- Device inventory and specification summary
- Project compatibility verification (which boards can run which projects)
- Programmer compatibility tracking
- Tool chain documentation (Arduino IDE, PlatformIO, Vivado, etc.)
- Cross-referencing equipment with active projects
- Planning new projects based on available hardware

## Information to Extract From Personal/Programmable Devices/

For each device, provide:

### Device Information
- Device name and model number
- Device type (FPGA, microcontroller, SoC, Arduino variant, retro board, etc.)
- Key specifications (logic cells/gates, memory, CPU speed, GPIO pins)
- Available programming interfaces (ISP, JTAG, USB, serial, etc.)
- Supported toolchains (Vivado, Arduino IDE, PlatformIO, ARM Keil, etc.)
- Current status (Active/Shelved/Project/Experimental)
- Related active projects using this device

### Categories Needed

1. **FPGA Boards** - Xilinx/Intel/Lattice boards with logic capacity and memory
2. **Microcontroller Boards** - Arduino, STM32, AVR, ESP8266/ESP32, PIC, etc.
3. **ARM SoC Boards** - Raspberry Pi, Zynq, BeagleBone, etc.
4. **CPLD/GAL Boards** - Complex programmable logic, simple programmable logic
5. **Retro/TTL Boards** - Gigatron, Multicomp, other discrete logic systems
6. **Wireless Modules** - XBee, BLE, WiFi modules, radio boards
7. **8-bit Trainers** - Educational trainer kits (8085, etc.)
8. **Robot/Hobbyist Kits** - Line followers, robot platforms, etc.

## Format Requested

Markdown table by category with status tracking:

**FPGA Boards**
| Model | Logic Cells | Memory | JTAG Support | Vivado | Status | Projects |
|---|---|---|---|---|---|---|
| | | | | | | |

**Microcontroller Boards**
| Model | CPU | RAM | Flash | GPIO | Arduino IDE | PlatformIO | Status | Projects |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

**ARM SoC Boards**
| Model | CPU | RAM | Specs | Status | Projects |
|---|---|---|---|---|---|
| | | | | | |

**CPLD/GAL Boards**
| Model | Type | Capacity | Programmer | Status | Projects |
|---|---|---|---|---|---|
| | | | | | |

**Retro/TTL Boards**
| Model | Type | Processor | Memory | Status | Projects |
|---|---|---|---|---|---|
| | | | | | |

**Wireless Modules**
| Model | Type | Frequency | Interface | Status | Projects |
|---|---|---|---|---|---|
| | | | | | |

## Cross-Reference Notes

- Programmer compatibility (TL866II Plus, USBasp, ST-Link, etc.)
- Which devices are actively used in projects vs. archived/experimental
- Toolchain and IDE requirements for each device
- Any custom bootloaders or firmware pre-loaded on devices
- Training/reference materials available for each device

## Response File Location

Place completed inventory at: `.personal/incoming/programmable-devices.md`
