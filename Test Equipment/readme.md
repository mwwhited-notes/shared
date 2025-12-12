# Test Equipment Inventory

Personal electronics lab equipment reference with specifications, documentation links, and software resources.

Each device has its own directory with detailed specifications and locally archived documentation.

**[Equipment Documentation Protocol](EQUIPMENT_DOCUMENTATION_PROTOCOL.md)** - Guide for adding new equipment and maintaining this inventory.

**[Missing Documentation Tracker](MISSING_DOCUMENTATION.md)** - Documents that require manual download (check off when obtained).

---

## Equipment Index

### Oscilloscopes

| Model | Type | Bandwidth | Channels | Directory |
|-------|------|-----------|----------|-----------|
| [Rigol DS1102E](rigol-ds1102e/) | DSO | 100 MHz | 2 | `rigol-ds1102e/` |
| [Tektronix TDS2024](tektronix-tds2024/) | DSO | 200 MHz | 4 | `tektronix-tds2024/` |
| [Hitachi V-1150](hitachi-v1150/) | Analog | 150 MHz | 4 | `hitachi-v1150/` |
| [DSO201 (DSO Nano)](dso201/) | Pocket DSO | 1 MHz | 1 | `dso201/` |
| [Digilent Analog Discovery 2](digilent-ad2/) | USB | 30 MHz | 2 | `digilent-ad2/` |

### Signal Generators

| Model | Channels | Max Frequency | Directory |
|-------|----------|---------------|-----------|
| [Rigol DG1022](rigol-dg1022/) | 2 | 20 MHz | `rigol-dg1022/` |
| [Analog Discovery 2 (AWG)](digilent-ad2/) | 2 | 12 MHz | `digilent-ad2/` |

### Multimeters

| Model | Type | Resolution | Directory |
|-------|------|------------|-----------|
| [HP/Agilent/Keysight 34401A](hp-34401a/) | Bench | 6½ digit | `hp-34401a/` |
| [Rigol DM3058E](rigol-dm3058e/) | Bench | 5½ digit | `rigol-dm3058e/` |
| [Tenma 72-2055](tenma-72-2055/) | Handheld | 3½ digit | `tenma-72-2055/` |

### LCR Meters

| Model | Type | Max Test Freq | Directory |
|-------|------|---------------|-----------|
| [DER EE DE-5000](deree-de5000/) | Handheld | 100 kHz | `deree-de5000/` |
| [Holdpeak HP-4070L](holdpeak-hp4070l/) | Handheld | 100 Hz | `holdpeak-hp4070l/` |

### Power Supplies

| Model | Output | Programmable | Directory |
|-------|--------|--------------|-----------|
| [Korad KA3005P](korad-ka3005p/) | 30V/5A | Yes (USB/RS-232) | `korad-ka3005p/` |
| [QE-MS305D](qe-ms305d/) | 30V/5A | No | `qe-ms305d/` |

### Logic Analyzers

| Model | Channels | Max Sample Rate | Directory |
|-------|----------|-----------------|-----------|
| [Saleae Logic Original](saleae-logic/) | 8 digital | 24 MSa/s | `saleae-logic/` |
| [Analog Discovery 2](digilent-ad2/) | 16 digital | 100 MSa/s | `digilent-ad2/` |

### Programmers

| Model | Type | Targets | Directory |
|-------|------|---------|-----------|
| [XGecu TL866II Plus](xgecu-tl866ii-plus/) | Universal | EEPROM, Flash, MCU, GAL | `xgecu-tl866ii-plus/` |
| [USBasp](usbasp/) | AVR ISP | ATmega, ATtiny, AT90 | `usbasp/` |
| [Altera USB Blaster](altera-usb-blaster/) | FPGA/CPLD | Altera/Intel FPGAs, CPLDs | `altera-usb-blaster/` |
| [ST-Link V2](st-link-v2/) | ARM/STM8 | STM32, STM8 | `st-link-v2/` |
| [USB to ESP-01 Adapter](usb-esp01-adapter/) | ESP8266 | ESP-01 module | `usb-esp01-adapter/` |
| [Velleman K8048RS](velleman-k8048rs/) | PIC ISP | PIC 8/14/18/28-pin | `velleman-k8048rs/` |

### Protocol Tools

| Model | Protocols | Directory |
|-------|-----------|-----------|
| [SparkFun Bus Pirate v3.6a](sparkfun-bus-pirate/) | SPI, I2C, UART, 1-Wire, JTAG | `sparkfun-bus-pirate/` |
| [FT232H Breakout](ft232h-breakout/) | SPI, I2C, JTAG, UART, GPIO | `ft232h-breakout/` |

### Development Boards

| Model | Purpose | Directory |
|-------|---------|-----------|
| [Maxstream XBIB-U-DEV](maxstream-xbib-u-dev/) | XBee development/programming | `maxstream-xbib-u-dev/` |

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
└── maxstream-xbib-u-dev/
    ├── README.md
    └── XBIB-U-DEV_UserGuide.pdf
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

## Notes

- **TDS2024** has TDS2CMA module (GPIB, RS-232, Centronics, FFT) but NO USB and NO CompactFlash
- **Saleae Logic** is the original 8-channel digital-only version (not Logic 8 with analog)
- **HP 34401A** provides highest precision (6½ digit) for calibration reference work
- **Bus Pirate** is SparkFun v3.6a version

---

*Last updated: December 2024*
