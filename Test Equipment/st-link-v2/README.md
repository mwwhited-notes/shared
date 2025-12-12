# ST-Link V2

**STM32/STM8 Programmer and Debugger**

## Unit Information

| Field | Value |
|-------|-------|
| Manufacturer | STMicroelectronics (possibly genuine) |
| Model | ST-Link V2 |
| Hardware Revision | V2 |
| Case | Small aluminum enclosure |
| Condition | Working |

## Specifications

| Specification | Value |
|--------------|-------|
| Target MCUs | STM32 (Cortex-M), STM8 |
| Interface | USB 2.0 Full Speed |
| Debug Protocols | SWD, JTAG, SWIM (STM8) |
| Connector | 20-pin IDC (0.1" pitch) |
| Voltage | 3.0V to 3.6V target |
| Max SWD Clock | 4 MHz |

## Supported Protocols

| Protocol | Target | Pins Used |
|----------|--------|-----------|
| SWD | STM32 (Cortex-M) | SWDIO, SWCLK |
| JTAG | STM32 (Cortex-M) | TMS, TCK, TDI, TDO, TRST |
| SWIM | STM8 | SWIM, RESET |

## Pinout (20-pin IDC)

```
        ┌─────────────┐
   VCC  │ 1        2  │  N/C
        │             │
  TRST  │ 3        4  │  GND
        │             │
   TDI  │ 5        6  │  GND
        │             │
   TMS  │ 7        8  │  GND
  SWDIO │             │
        │             │
   TCK  │ 9       10  │  GND
 SWCLK  │             │
        │             │
  RTCK  │ 11      12  │  GND
        │             │
   TDO  │ 13      14  │  GND
        │             │
 RESET  │ 15      16  │  GND
        │             │
  N/C   │ 17      18  │  GND
        │             │
  N/C   │ 19      20  │  GND
        └─────────────┘
```

## Minimum SWD Connection

Only 4 wires needed for basic SWD:
- Pin 1: VCC (3.3V reference)
- Pin 7: SWDIO
- Pin 9: SWCLK
- Pin 15: RESET (optional but recommended)
- Pin 4/6/8/etc: GND

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

- Small aluminum case suggests genuine ST unit (clones usually plastic)
- Supports both STM32 (ARM Cortex-M) and STM8 (proprietary core)
- SWD is preferred over JTAG for STM32 (fewer wires, same functionality)

## Local Files

- `ST-Link_V2_UserManual.pdf` - User manual (UM1075)
