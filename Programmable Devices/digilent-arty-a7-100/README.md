# Digilent Arty A7-100

**Artix-7 FPGA Development Board**

## Board Information

| Field | Value |
|-------|-------|
| Manufacturer | Digilent |
| Board | Arty A7-100T |
| FPGA | Xilinx Artix-7 XC7A100T-1CSG324C |
| Date Acquired | |
| Quantity | 1 |

## Specifications

| Specification | Value |
|--------------|-------|
| Logic Cells | 101,440 |
| Slices | 15,850 |
| CLB Flip-Flops | 126,800 |
| Block RAM | 4,860 Kb (135 x 36Kb blocks) |
| DSP Slices | 240 |
| Clock Management | 6 CMTs (12 PLLs) |
| On-chip ADC | 1 XADC |

## Board Features

| Feature | Details |
|---------|---------|
| DDR3L | 256 MB (16-bit, 667 MHz) |
| Flash | 16 MB Quad-SPI |
| Ethernet | 10/100 Mbps |
| USB-UART | FTDI FT2232HQ |
| USB-JTAG | Integrated (Digilent) |
| Switches | 4 slide switches |
| Buttons | 4 push buttons + reset |
| LEDs | 4 RGB LEDs, 4 green LEDs |
| Pmod Ports | 4 standard Pmod |
| Arduino Headers | Yes (shield compatible) |
| ChipKit Headers | Yes |

## Interfaces

- 4x Pmod ports (32 I/O)
- Arduino/ChipKit shield connector
- USB-JTAG programming
- USB-UART bridge
- 10/100 Ethernet
- Micro SD card slot (directly to FPGA pins, directly addressable)

## Programming

| Method | Tools |
|--------|-------|
| JTAG | Vivado Hardware Manager |
| Quad-SPI Flash | Vivado (persistent config) |

## Documentation

- [Arty A7 Reference Manual](https://digilent.com/reference/programmable-logic/arty-a7/reference-manual)
- [Arty A7 Schematic](https://digilent.com/reference/_media/programmable-logic/arty-a7/arty-a7-e2-sch.pdf)
- [XC7A100T Datasheet](https://docs.amd.com/v/u/en-US/ds181_Artix_7_Data_Sheet)
- [Artix-7 Configuration Guide](https://docs.amd.com/v/u/en-US/ug470_7Series_Config)

## Software & Tools

- **Vivado Design Suite** - FPGA development (free WebPACK license)
- **Vitis** - Software development for MicroBlaze
- [Vivado Download](https://www.xilinx.com/support/download.html)
- [Digilent Board Files](https://github.com/Digilent/vivado-boards)

## Notes

- Supports Vivado WebPACK (free license, no size restrictions for Artix-7)
- Can run MicroBlaze soft processor
- Arduino headers allow use of many shields
- 100T variant has more resources than the A7-35T

## Local Files

*Documentation to be downloaded*
