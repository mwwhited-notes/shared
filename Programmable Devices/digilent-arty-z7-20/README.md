# Digilent Arty Z7-20

**Zynq-7000 SoC Development Board**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | Digilent |
| Board | Arty Z7-20 |
| SoC | Xilinx Zynq-7000 XC7Z020-1CLG400C |
| Status | Working |
| Date Ordered | 2021-11-22 |
| Purchase Price | $209.00 |
| Source | Digilent |
| Quantity | 1 |

## Specifications

### Processing System (PS)

| Specification | Value |
|--------------|-------|
| Processor | Dual-core ARM Cortex-A9 |
| Clock Speed | Up to 866 MHz |
| L1 Cache | 32 KB I-cache, 32 KB D-cache per core |
| L2 Cache | 512 KB shared |
| On-chip Memory | 256 KB |

### Programmable Logic (PL)

| Specification | Value |
|--------------|-------|
| Logic Cells | 85,000 |
| Slices | 13,300 |
| CLB Flip-Flops | 106,400 |
| Block RAM | 4.9 Mb (140 x 36Kb blocks) |
| DSP Slices | 220 |

## Board Features

| Feature | Details |
|---------|---------|
| DDR3 | 512 MB (16-bit) |
| Flash | 16 MB Quad-SPI |
| USB-UART | FTDI FT2232HQ |
| USB-JTAG | Integrated (Digilent) |
| USB OTG | USB 2.0 host/device |
| HDMI | TX and RX |
| Audio | Line in, line out, mic, headphone |
| Switches | 2 slide switches |
| Buttons | 4 push buttons + reset |
| LEDs | 2 RGB LEDs, 4 green LEDs |
| Pmod Ports | 2 standard Pmod |
| Arduino Headers | Yes (shield compatible) |
| ChipKit Headers | Yes |

## Interfaces

- 2x Pmod ports (directly addressable, directly to PL pins)
- Arduino/ChipKit shield connector
- HDMI input and output
- Audio codec (ADAU1761)
- USB OTG (host/device/OTG)
- USB-JTAG programming
- USB-UART bridge
- MicroSD card slot

## Programming

| Method | Tools |
|--------|-------|
| JTAG | Vivado Hardware Manager, Vitis |
| Quad-SPI Flash | Vivado/Vitis (persistent config) |
| SD Card Boot | Copy BOOT.bin to SD |

## Documentation

- [Arty Z7 Reference Manual](https://digilent.com/reference/programmable-logic/arty-z7/reference-manual)
- [Arty Z7 Schematic](https://digilent.com/reference/_media/programmable-logic/arty-z7/arty-z7-sch.pdf)
- [Zynq-7000 Technical Reference Manual](https://docs.amd.com/v/u/en-US/ug585-Zynq-7000-TRM)
- [Zynq-7000 Datasheet](https://docs.amd.com/v/u/en-US/ds190-Zynq-7000-Overview)

## Software & Tools

- **Vivado Design Suite** - PL development
- **Vitis** - PS software development
- **PetaLinux** - Embedded Linux
- [Vivado Download](https://www.xilinx.com/support/download.html)
- [Digilent Board Files](https://github.com/Digilent/vivado-boards)

## Notes

- Combines ARM processing with FPGA fabric
- Can run Linux (PetaLinux, Ubuntu, etc.)
- HDMI TX/RX enables video processing projects
- Z7-20 has more PL resources than Z7-10

## Local Files

*Documentation to be downloaded*
