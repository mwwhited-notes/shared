# ST-Link V2

**STM32/STM8 Programmer and Debugger**

## Unit Information

| Field | Value |
|-------|-------|
| Manufacturer | HiLetgo (clone) |
| Model | ST-Link V2 |
| Hardware Revision | V2 |
| Case | Small aluminum enclosure |
| Status | Working |
| Date Ordered | 2023-04-02 |
| Purchase Price | $10.49 |
| Source | Amazon (HiLetgo) |

## Specifications

| Specification | Value |
|--------------|-------|
| Target MCUs | STM32 (Cortex-M), STM8 |
| Interface | USB 2.0 Full Speed |
| Debug Protocols | SWD, SWIM (STM8) |
| Connector | 10-pin IDC (0.1" pitch) |
| Voltage | 3.0V to 3.6V target |
| Max SWD Clock | 4 MHz |

## Supported Protocols

| Protocol | Target | Pins Used |
|----------|--------|-----------|
| SWD | STM32 (Cortex-M) | SWDIO, SWCLK |
| SWIM | STM8 | SWIM, RESET |

*Note: 10-pin version does not support full JTAG (20-pin version required for JTAG).*

## Pinout (10-pin IDC)

```
        ┌─────────────┐
   RST  │ 1        2  │  SWDIO
        │             │
   GND  │ 3        4  │  GND
        │             │
  SWIM  │ 5        6  │  SWCLK
        │             │
  3.3V  │ 7        8  │  3.3V
        │             │
  5.0V  │ 9       10  │  5.0V
        └─────────────┘
```

## SWD Connection (STM32)

| ST-Link Pin | Target | Function |
|-------------|--------|----------|
| 2 | SWDIO | Data I/O |
| 6 | SWCLK | Clock |
| 1 | NRST | Reset (optional) |
| 3 or 4 | GND | Ground |
| 7 or 8 | 3.3V | Power (optional, if powering target) |

## SWIM Connection (STM8)

| ST-Link Pin | Target | Function |
|-------------|--------|----------|
| 5 | SWIM | Single-wire debug |
| 1 | NRST | Reset |
| 3 or 4 | GND | Ground |

## Documentation

- [ST-Link V2 User Manual (UM1075)](https://www.st.com/resource/en/user_manual/um1075-stlinkv2-incircuit-debuggerprogrammer-for-stm8-and-stm32-stmicroelectronics.pdf)
- [STM32 Programming Manual](https://www.st.com/resource/en/programming_manual/pm0075-stm32f10xxx-flash-memory-microcontrollers-stmicroelectronics.pdf)

## Software

### Official Tools
- **STM32CubeProgrammer** - ST's unified programming tool
  - [Download](https://www.st.com/en/development-tools/stm32cubeprog.html)
- **STM32CubeIDE** - Full development environment with debugging
- **STVP** - ST Visual Programmer (for STM8)

### Open Source Tools
- **OpenOCD** - Open On-Chip Debugger
- **stlink** - Open source ST-Link tools
  - [GitHub](https://github.com/stlink-org/stlink)
- **PlatformIO** - Development platform with ST-Link support

## Driver Installation (Windows)

Drivers included with STM32CubeProgrammer or STM32CubeIDE.

Manual installation:
1. Download [STSW-LINK009](https://www.st.com/en/development-tools/stsw-link009.html)
2. Run installer
3. Connect ST-Link

## Basic OpenOCD Usage

```bash
# Connect to STM32F103
openocd -f interface/stlink.cfg -f target/stm32f1x.cfg

# In another terminal, connect with GDB
arm-none-eabi-gdb firmware.elf
(gdb) target remote localhost:3333
(gdb) load
(gdb) continue
```

## Basic stlink Usage

```bash
# Probe connected device
st-info --probe

# Flash firmware
st-flash write firmware.bin 0x8000000

# Erase chip
st-flash erase

# Read flash to file
st-flash read dump.bin 0x8000000 0x10000
```

## Firmware Update

ST-Link firmware can be updated using:
1. STM32CubeProgrammer → ST-Link → Firmware Update
2. Or standalone [STSW-LINK007](https://www.st.com/en/development-tools/stsw-link007.html)

## Notes

- Small aluminum case with 10-pin connector
- 10-pin version supports SWD and SWIM only (no full JTAG)
- Supports both STM32 (ARM Cortex-M) and STM8 (proprietary core)
- SWD is standard for STM32 debugging (JTAG rarely needed)

## Local Files

*Note: ST website blocks automated downloads. Download manually from the documentation links above.*
