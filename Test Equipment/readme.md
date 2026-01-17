# Test Equipment Inventory

Complete electronics lab equipment reference with specifications, programming tools, and instrument control documentation. Each device has its own directory with detailed specifications and locally archived documentation.

**Quick Reference:** 41 pieces of lab equipment | $6,015+ total value | [Documentation Protocol](../.claude/protocols/EQUIPMENT_DOCUMENTATION_PROTOCOL.md) | [Missing Documentation](MISSING_DOCUMENTATION.md)

**For consumables, accessories, hand tools, and components, see [tools-and-components.md](../tools-and-components.md)**

## Table of Contents

- [Quick Reference Summary](#quick-reference-summary)

- [Equipment Index](#equipment-index)
  - [Oscilloscopes](#oscilloscopes)
  - [Signal Generators](#signal-generators)
  - [Multimeters](#multimeters)
  - [LCR Meters](#lcr-meters)
  - [Power Supplies](#power-supplies)
  - [Logic Analyzers](#logic-analyzers)
  - [Programmers](#programmers)
  - [Protocol Tools](#protocol-tools)
  - [Data Acquisition / I/O](#data-acquisition--io)
  - [Development Boards](#development-boards)
  - [Microscopes](#microscopes)
  - [Soldering & Rework](#soldering--rework)
  - [Thermal Imaging](#thermal-imaging)
  - [Imaging & Documentation](#imaging--documentation)
  - [Input Devices](#input-devices)
  - [Audio](#audio)
  - [Lab Equipment](#lab-equipment)
  - [Fabrication](#fabrication)
  - [Safety & Monitoring](#safety--monitoring)
- [Directory Structure](#directory-structure)
- [Software Resources](#software-resources)
  - [Instrument Control](#instrument-control)
  - [Protocol Analysis & Debugging](#protocol-analysis--debugging)
  - [Cross-Platform Tools](#cross-platform-tools)
- [Notes](#notes)

---

## Quick Reference Summary

| Category | Item Count | Status | Key Example |
|----------|-----------|--------|------------|
| Oscilloscopes | 5 | Active | Rigol DS1102E (100 MHz, 2 CH) |
| Signal Generators | 2 | Active | Rigol DG1022 (20 MHz, 2 CH) |
| Multimeters | 7 | Active | HP 34401A (6½ digit) |
| LCR Meters | 2 | Active | DER EE DE-5000 (100 kHz) |
| Power Supplies | 3 | Active | Korad KA3005P (30V/5A programmable) |
| Logic Analyzers | 2 | Active | Saleae Logic (8 CH, 24 MSa/s) |
| Programmers | 8 | Active | XGecu TL866II Plus (universal) |
| Protocol Tools | 2 | Active | Bus Pirate, FT232H Breakout |
| Data Acquisition | 1 | Active | Digilent Analog Discovery 2 |
| Microscopes | 2 | Active | AmScope SM-3 & T490 |
| Soldering & Rework | 3 | Active | KSGER T12, YaeCCC 858D |
| Thermal Imaging | 1 | Active | FLIR TG130 |
| Imaging | 2 | Active | Lenovo 510 FHD, Kitchbar KB-700 |
| Audio | 1 | Active | Pyle PTAU45 |
| Lab Equipment | 3 | Active | Velleman K8200 3D Printer |
| Safety & Monitoring | 1 | Active | RADEX ONE Geiger Counter |
| **TOTAL** | **41** | **Active** | - |

---

## Equipment Index

### Oscilloscopes

| Model | Type | Bandwidth | Channels | Git Hash | Directory |
|-------|------|-----------|----------|----------|-----------|
| [Rigol DS1102E](rigol-ds1102e/) | DSO | 100 MHz | 2 | xxxxxxx | `rigol-ds1102e/` |
| [Tektronix TDS2024](tektronix-tds2024/) | DSO | 200 MHz | 4 | xxxxxxx | `tektronix-tds2024/` |
| [Hitachi V-1150](hitachi-v1150/) | Analog | 150 MHz | 4 | xxxxxxx | `hitachi-v1150/` |
| [DSO201 (DSO Nano)](dso201/) | Pocket DSO | 1 MHz | 1 | xxxxxxx | `dso201/` |
| [Digilent Analog Discovery 2](digilent-ad2/) | USB | 30 MHz | 2 | xxxxxxx | `digilent-ad2/` |

### Signal Generators

| Model | Channels | Max Frequency | Git Hash | Directory |
|-------|----------|---------------|----------|-----------|
| [Rigol DG1022](rigol-dg1022/) | 2 | 20 MHz | xxxxxxx | `rigol-dg1022/` |
| [Analog Discovery 2 (AWG)](digilent-ad2/) | 2 | 12 MHz | xxxxxxx | `digilent-ad2/` |

### Multimeters

| Model | Type | Resolution | Git Hash | Directory |
|-------|------|------------|----------|-----------|
| [HP/Agilent/Keysight 34401A](hp-34401a/) | Bench | 6½ digit | xxxxxxx | `hp-34401a/` |
| [Rigol DM3058E](rigol-dm3058e/) | Bench | 5½ digit | xxxxxxx | `rigol-dm3058e/` |
| [Tenma 72-2055](tenma-72-2055/) | Handheld | 3½ digit | xxxxxxx | `tenma-72-2055/` |
| Eversame USB-C Tester | USB | V/A/W | xxxxxxx | - |
| Nubee IR Thermometer | Handheld | Non-contact | xxxxxxx | - |
| DBPOWER SC-8108 Cable Tester | Network | Cat5/6 Length | xxxxxxx | - |
| Dr.meter LX1010B Lux Meter | Handheld | 0-100k Lux | xxxxxxx | - |

### LCR Meters

| Model | Type | Max Test Freq | Git Hash | Directory |
|-------|------|---------------|----------|-----------|
| [DER EE DE-5000](deree-de5000/) | Handheld | 100 kHz | xxxxxxx | `deree-de5000/` |
| [Holdpeak HP-4070L](holdpeak-hp4070l/) | Handheld | 100 Hz | xxxxxxx | `holdpeak-hp4070l/` |

### Power Supplies

| Model | Output | Programmable | Git Hash | Directory |
|-------|--------|--------------|----------|-----------|
| [Korad KA3005P](korad-ka3005p/) | 30V/5A | Yes (USB/RS-232) | xxxxxxx | `korad-ka3005p/` |
| [Korad KA6003P](korad-ka6003p/) | 60V/3A | Yes (USB/RS-232) | xxxxxxx | `korad-ka6003p/` |
| [QE-MS305D](qe-ms305d/) | 30V/5A | No | xxxxxxx | `qe-ms305d/` |

### Logic Analyzers

| Model | Channels | Max Sample Rate | Git Hash | Directory |
|-------|----------|-----------------|----------|-----------|
| [Saleae Logic Original](saleae-logic/) | 8 digital | 24 MSa/s | xxxxxxx | `saleae-logic/` |
| [Analog Discovery 2](digilent-ad2/) | 16 digital | 100 MSa/s | xxxxxxx | `digilent-ad2/` |

### Programmers

| Model | Type | Targets | Git Hash | Directory |
|-------|------|---------|----------|-----------|
| [XGecu TL866II Plus](xgecu-tl866ii-plus/) | Universal | EEPROM, Flash, MCU, GAL | xxxxxxx | `xgecu-tl866ii-plus/` |
| [USBasp](usbasp/) | AVR ISP | ATmega, ATtiny, AT90 | xxxxxxx | `usbasp/` |
| [Altera USB Blaster](altera-usb-blaster/) | FPGA/CPLD | Altera/Intel FPGAs, CPLDs | xxxxxxx | `altera-usb-blaster/` |
| [ST-Link V2](st-link-v2/) | ARM/STM8 | STM32, STM8 | xxxxxxx | `st-link-v2/` |
| [USB to ESP-01 Adapter](usb-esp01-adapter/) | ESP8266 | ESP-01 module | xxxxxxx | `usb-esp01-adapter/` |
| [Velleman K8048RS](velleman-k8048rs/) | PIC ISP | PIC 8/14/18/28-pin | xxxxxxx | `velleman-k8048rs/` |
| [Greaseweazle V4.1](greaseweazle-v41/) | Floppy Controller | 3", 3.5", 5.25", 8" disks | xxxxxxx | `greaseweazle-v41/` |

### Protocol Tools

| Model | Protocols | Git Hash | Directory |
|-------|-----------|----------|-----------|
| [SparkFun Bus Pirate v3.6a](sparkfun-bus-pirate/) | SPI, I2C, UART, 1-Wire, JTAG | xxxxxxx | `sparkfun-bus-pirate/` |
| [FT232H Breakout](ft232h-breakout/) | SPI, I2C, JTAG, UART, GPIO | xxxxxxx | `ft232h-breakout/` |

### Data Acquisition / I/O

| Model | Inputs | Outputs | Interface | Git Hash | Directory |
|-------|--------|---------|-----------|----------|-----------|
| [Velleman K8055](velleman-k8055/) | 5 DI, 2 AI | 8 DO, 2 AO | USB | xxxxxxx | `velleman-k8055/` |

### Development Boards

| Model | Purpose | Git Hash | Directory |
|-------|---------|----------|-----------|
| [Maxstream XBIB-U-DEV](maxstream-xbib-u-dev/) | XBee development/programming | xxxxxxx | `maxstream-xbib-u-dev/` |

### Microscopes

| Model | Type | Magnification | Git Hash | Directory |
|-------|------|---------------|----------|-----------|
| [AmScope T490-DK](amscope-t490-dk/) | Compound (Darkfield) | 40X-2000X | xxxxxxx | `amscope-t490-dk/` |
| [AmScope SM-3](amscope-sm-3/) | Stereo | 3.5X-90X | xxxxxxx | `amscope-sm-3/` |

### Soldering & Rework

| Model | Type | Power | Git Hash | Directory |
|-------|------|-------|----------|-----------|
| [KSGER T12](ksger-t12/) | Soldering Station | 75W | xxxxxxx | `ksger-t12/` |
| [YaeCCC 858D](yaeccc-858d/) | Hot Air Rework | 700W | xxxxxxx | `yaeccc-858d/` |
| [Hakko FR-301](hakko-fr301/) | Desoldering Gun | 140W | xxxxxxx | `hakko-fr301/` |

### Thermal Imaging

| Model | Type | Resolution | Git Hash | Directory |
|-------|------|------------|----------|-----------|
| [FLIR TG130](flir-tg130/) | Spot Thermal Camera | 80x60 | xxxxxxx | `flir-tg130/` |

### Imaging & Documentation

| Model | Type | Resolution | Git Hash | Directory |
|-------|------|------------|----------|-----------|
| Epson Perfection V850 Pro | Film/Flatbed Scanner | 6400 dpi | xxxxxxx | - |
| [Kitchbar KB-700](kitchbar-kb700/) | Document Camera | 8MP | xxxxxxx | `kitchbar-kb700/` |
| [Lenovo 510 FHD](lenovo-510-fhd/) | Webcam | 1080p | xxxxxxx | `lenovo-510-fhd/` |

### Input Devices

| Model | Type | Keys | Git Hash | Directory |
|-------|------|------|----------|-----------|
| [Fifine AmpliGame D6](fifine-d6/) | Macro Keypad | 15 | xxxxxxx | `fifine-d6/` |

### Audio

| Model | Type | Power | Git Hash | Directory |
|-------|------|-------|----------|-----------|
| [Pyle PTAU45](pyle-ptau45/) | Stereo Amplifier | 2×120W | xxxxxxx | `pyle-ptau45/` |

### Lab Equipment

| Model | Type | Capacity | Git Hash | Directory |
|-------|------|----------|----------|-----------|
| [CREWORKS Ultrasonic Cleaner](creworks-ultrasonic-cleaner/) | Ultrasonic Cleaner | 10L | xxxxxxx | `creworks-ultrasonic-cleaner/` |
| [Magnetic Stirrer Hot Plate](magnetic-stirrer-hotplate/) | Stirrer/Hot Plate | - | xxxxxxx | `magnetic-stirrer-hotplate/` |
| [ExGizmo UV EPROM Eraser](exgizmo-uv-eprom-eraser/) | UV Eraser | Multi-chip | xxxxxxx | `exgizmo-uv-eprom-eraser/` |

### Fabrication

| Model | Type | Build Volume | Git Hash | Directory |
|-------|------|--------------|----------|-----------|
| [Velleman K8200](velleman-k8200/) | 3D Printer (Duet 3) | 200x200x200mm | xxxxxxx | `velleman-k8200/` |

### Safety & Monitoring

| Model | Type | Detection | Git Hash | Directory |
|-------|------|-----------|----------|-----------|
| [RADEX ONE](radex-one/) | Geiger Counter | Gamma, Beta, X-ray | xxxxxxx | `radex-one/` |

---

## Directory Structure

```
├── readme.md                    # This file
├── rigol-ds1102e/
│   ├── README.md
│   └── DS1000E_UserGuide.pdf
├── tektronix-tds2024/
│   ├── README.md
│   ├── TDS2000B_UserManual.pdf
│   └── TDS2000_ServiceManual.pdf
├── hitachi-v1150/
│   └── README.md
├── dso201/
│   └── README.md
├── rigol-dg1022/
│   ├── README.md
│   └── DG1022_UserGuide.pdf
├── hp-34401a/
│   ├── README.md
│   ├── 34401A_UserGuide.pdf
│   └── 34401A_ServiceGuide.pdf
├── rigol-dm3058e/
│   ├── README.md
│   ├── DM3058_UserGuide.pdf
│   └── DM3058_ServiceGuide.pdf
├── tenma-72-2055/
│   ├── README.md
│   └── Tenma_72-2055_Manual.pdf
├── deree-de5000/
│   ├── README.md
│   ├── DE-5000_Manual.pdf
│   └── DE-5000_Datasheet.pdf
├── holdpeak-hp4070l/
│   └── README.md
├── korad-ka3005p/
│   ├── README.md
│   └── KA3005P_UserManual.pdf
├── korad-ka6003p/
│   ├── README.md
│   └── KA6003P_UserManual.pdf
├── qe-ms305d/
│   └── README.md
├── saleae-logic/
│   ├── README.md
│   └── Saleae_UserGuide.pdf
├── digilent-ad2/
│   ├── README.md
│   ├── AD2_ReferenceManual.pdf
│   └── WaveForms_SDK_Reference.pdf
├── xgecu-tl866ii-plus/
│   ├── README.md
│   └── TL866II_UserManual.pdf
├── sparkfun-bus-pirate/
│   └── README.md
├── usbasp/
│   └── README.md
├── altera-usb-blaster/
│   ├── README.md
│   └── USB-Blaster_UserGuide.pdf
├── st-link-v2/
│   └── README.md
├── ft232h-breakout/
│   ├── README.md
│   ├── FT232H_Datasheet.pdf
│   └── AN_108_MPSSE_Commands.pdf
├── usb-esp01-adapter/
│   ├── README.md
│   └── ESP8266_Datasheet.pdf
├── velleman-k8048rs/
│   ├── README.md
│   └── K8048_UserManual.pdf
├── velleman-k8055/
│   ├── README.md
│   └── K8055_UserManual.pdf
├── maxstream-xbib-u-dev/
│   ├── README.md
│   └── XBIB-U-DEV_UserGuide.pdf
├── amscope-t490-dk/
│   ├── README.md
│   └── T490_UserManual.pdf
├── amscope-sm-3/
│   ├── README.md
│   └── SM-3_UserManual.pdf
├── ksger-t12/
│   └── README.md
├── yaeccc-858d/
│   └── README.md
├── hakko-fr301/
│   └── README.md
├── flir-tg130/
│   └── README.md
├── kitchbar-kb700/
│   └── README.md
├── creworks-ultrasonic-cleaner/
│   └── README.md
├── magnetic-stirrer-hotplate/
│   └── README.md
├── lenovo-510-fhd/
│   └── README.md
├── fifine-d6/
│   └── README.md
├── pyle-ptau45/
│   └── README.md
├── greaseweazle-v41/
│   └── README.md
├── velleman-k8200/
│   ├── README.md
│   ├── K8200_Assembly_Manual.pdf
│   ├── K8200_User_Manual.pdf
│   └── Duet3_MB_6HC_Schematic.pdf
└── radex-one/
    └── README.md
```

---

## Software Resources

### Instrument Control
- **Rigol:** UltraScope, UltraSigma, UltraDMM
- **Keysight/Agilent:** BenchVue, IntuiLink
- **Digilent:** WaveForms
- **Saleae:** Logic 2
- **Universal:** sigrok/PulseView, PyVISA, NI-VISA

### Protocol Analysis & Debugging
- **OpenOCD** - JTAG/SWD debugging (ST-Link, FTDI, etc.)
- **AVRDUDE** - AVR programming (USBasp, USBtiny, etc.)
- **flashrom** - Flash chip programming
- **pyBusPirateLite** - Bus Pirate Python library
- **pyftdi** - Python FTDI library for FT232H
- **stlink** - Open source ST-Link tools
- **esptool** - ESP8266/ESP32 flashing tool
- **XCTU** - Digi XBee configuration utility

### Cross-Platform Tools
- **sigrok/PulseView** - Logic analyzer, oscilloscope, DMM support
- **PyVISA** - Python VISA instrument control
- **python-ivi** - IVI instrument drivers

---

## Collection Value Summary

### Documented Purchases

| Item | Category | Price | Source | Date |
|------|----------|-------|--------|------|
| Rigol DS1102E | Oscilloscope | $357.00 | Amazon (super-se11er) | 2017-04-11 |
| Tektronix TDS2024 | Oscilloscope | $411.09 | eBay | - |
| Hitachi V-1150 | Oscilloscope | $187.68 | eBay | - |
| DSO201 (DSO Nano) | Pocket Oscilloscope | $0.00 | Gift (project work) | - |
| Rigol DG1022 | Signal Generator | $200.00 | eBay (darny61) | - |
| HP 34401A | Multimeter | $270.00 | eBay | - |
| Rigol DM3058E | Multimeter | $399.95 | TEquipment.net | 2021-12-30 |
| Tenma 72-2055 | Multimeter | $0.00 | High school | - |
| DER EE DE-5000 | LCR Meter | $139.99 | Amazon | - |
| DER EE DE-5000 Kelvin Clips | LCR Accessory | $34.98 | Amazon | 2025-01 |
| Holdpeak HP-4070L | LCR Meter | $25.99 | Amazon | - |
| Korad KA3005P | Power Supply | $143.99 | Micro Center | 2023-01-15 |
| Korad KA6003P | Power Supply | $101.17 | eBay | - |
| QE-MS305D | Power Supply | $39.99 | eBay | - |
| AmScope T490-DK | Microscope | $341.98 | Amazon | - |
| AmScope T490-DK Accessories | Microscope | $319.56 | Amazon/eBay | 2016-2025 |
| AmScope SM-3 | Microscope | $477.00 | Amazon | - |
| KSGER T12 + Accessories | Soldering | $113.65 | AliExpress | 2022-12-27 |
| YaeCCC 858D + Accessories | Hot Air Rework | $94.47 | Amazon | 2022-04-18 |
| Hakko FR-301 | Desoldering | $0.00 | Gift (birthday) | 2023 |
| FLIR TG130 | Thermal | $199.99 | Amazon | - |
| Lenovo 510 FHD | Webcam | $58.99 | Amazon | 2025-01-30 |
| Fifine AmpliGame D6 | Macro Keypad | $71.09 | Amazon | 2025-01-23 |
| CREWORKS Ultrasonic Cleaner | Lab Equipment | $89.95 | Amazon | 2025-10-29 |
| Velleman K8200 | 3D Printer | $749.45 | Amazon | 2014-03-07 |
| Magnetic Stirrer + Flasks | Lab Equipment | $197.20 | Amazon | 2016-01-31 |
| Kitchbar KB-700 | Document Camera | $47.16 | Amazon | 2022-12-07 |
| Analog Discovery 2 + Accessories | Multi-instrument | $571.88 | Digilent | 2021-11-22 |
| XGecu TL866II Plus | Programmer | $59.99 | Amazon | 2020-01-21 |
| USBasp | Programmer | $8.50 | Amazon | 2019-01-28 |
| USB to ESP-01 Adapter | Programmer | $8.28 | Amazon | 2019-01-28 |
| Greaseweazle V4.1 | Floppy Controller | $39.38 | Tindie | 2023-10-29 |
| Altera USB Blaster | Programmer | $14.50 | Amazon (get005) | 2014-01-28 |
| ST-Link V2 | Programmer | $10.49 | Amazon (HiLetgo) | 2023-04-02 |
| FT232H Breakout | Protocol Tool | $10.99 | Amazon (KOOBOOK) | 2021-03-15 |
| Maxstream XBIB-U-DEV | Development Board | $0.00 | MS .NET MF competition | - |
| Saleae Logic | Logic Analyzer | - | SparkFun (new) | - |
| SparkFun Bus Pirate v3.6a | Protocol Tool | - | SparkFun (new) | - |
| Velleman K8048RS | Programmer | - | Micro Center | - |
| Velleman K8055 (×3) | Data Acquisition | - | Micro Center | - |
| Pyle PTAU45 | Audio Amplifier | $71.99 | Amazon | 2013-10-11 |
| ExGizmo UV EPROM Eraser | Lab Equipment | $19.88 | Amazon (ExGizmo) | 2020-01-30 |
| RADEX ONE | Safety & Monitoring | $127.95 | Amazon (Quarta-Rad) | 2020-09-15 |
| **Documented Total** | | **$6,015.15+** | | |

---

## Notes

- **TDS2024** has TDS2CMA module (GPIB, RS-232, Centronics, FFT) but NO USB and NO CompactFlash
- **Saleae Logic** is the original 8-channel digital-only version (not Logic 8 with analog)
- **HP 34401A** provides highest precision (6½ digit) for calibration reference work
- **Bus Pirate** is SparkFun v3.6a version

---

## Cross-References

- [Programmable Devices/](../Programmable%20Devices/) - Development boards, microcontrollers, FPGA boards that use programmers from this inventory
- [Expansion Boards/](../Expansion%20Boards/) - Shields and adapter boards for equipment development
- [Projects](../projects/) - Active projects utilizing test equipment:
  - FPGA development projects (uses Digilent AD2, Xilinx programmers)
  - Electronics projects requiring oscilloscopes and multimeters
  - Custom interface projects (Bus Pirate, FT232H)
- [tools-and-components.md](../tools-and-components.md) - Consumables and accessories for lab equipment

---

*Index Version: 1.1*
*Last Updated: 2026-01-17*
*Total Equipment: 41 pieces | $6,015.15+ documented*
*Scope: Oscilloscopes, signal generators, multimeters, power supplies, programmers, protocol tools, data acquisition, microscopes, thermal imaging, soldering equipment, safety & monitoring, and specialty lab equipment*
