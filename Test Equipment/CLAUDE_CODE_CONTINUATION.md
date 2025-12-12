# Test Equipment Inventory Project - Continuation Document

## Project Summary

This document provides context for continuing work on Matt's test equipment inventory documentation in Claude Code.

## What Was Done

Created a comprehensive markdown report (`test-equipment-inventory.md`) documenting Matt's personal electronics lab equipment with:

1. **Detailed specifications** for each instrument
2. **Links to user manuals, service manuals, and programming guides** (PDFs where available)
3. **Software resources** including manufacturer utilities and open-source alternatives
4. **Summary tables** organized by equipment category

## Equipment Inventory (16 Instruments)

### Oscilloscopes (5)
| Model | Type | Bandwidth | Channels |
|-------|------|-----------|----------|
| Rigol DS1102E | DSO | 100 MHz | 2 |
| Tektronix TDS2024 + TDS2CMA | DSO | 200 MHz | 4 |
| Hitachi V-1150 | Analog | 150 MHz | 4 |
| DSO201 (DSO Nano) | Pocket DSO | 1 MHz | 1 |
| Digilent Analog Discovery 2 | USB Multi-instrument | 30 MHz | 2 |

### Signal Generators (2)
| Model | Channels | Max Frequency |
|-------|----------|---------------|
| Rigol DG1022 | 2 | 20 MHz |
| Analog Discovery 2 (AWG) | 2 | 12 MHz |

### Multimeters (3)
| Model | Type | Resolution |
|-------|------|------------|
| HP/Agilent/Keysight 34401A | Bench | 6½ digit |
| Rigol DM3058E | Bench | 5½ digit |
| Tenma 72-2055 | Handheld | 3½ digit |

### LCR Meters (2)
| Model | Type | Max Test Freq |
|-------|------|---------------|
| DER EE DE-5000 | Handheld | 100 kHz |
| Holdpeak HP-4070L | Handheld | 100 Hz |

### Power Supplies (2)
| Model | Output | Programmable |
|-------|--------|--------------|
| Korad KA3005P | 30V/5A | Yes (USB/RS-232) |
| QE-MS305D | 30V/5A | No |

### Logic Analyzers (2)
| Model | Channels | Max Sample Rate |
|-------|----------|-----------------|
| Saleae Logic Original | 8 digital | 24 MSa/s |
| Analog Discovery 2 | 16 digital | 100 MSa/s |

### Protocol Tools (1)
| Model | Protocols |
|-------|-----------|
| SparkFun Bus Pirate v3.6a | SPI, I2C, UART, 1-Wire, JTAG |

### Programmers (1)
| Model | Type | Supported ICs |
|-------|------|---------------|
| XGecu TL866II Plus | Universal | 15,000+ |

## User Context

**Name:** Matt

**Background:** Software developer with experience in:
- Database applications (SQLite, SQL Server)
- .NET development (.NET 4.8 and .NET Core/8.0+)
- WCF services
- Transactional messaging systems

**Electronics Interests:**
- Test equipment automation and instrument interfacing
- LXI protocol bridges and VISA instrument interfaces
- Arduino/microcontroller projects (timing control, port manipulation)
- Analog circuit design (op-amp function generators, piecewise diode circuits)
- Mathematical visualization (Mandelbrot set on analog computers)

**Preferences:**
- C#, SQLite, SQL Server
- Markdown documentation
- PlantUML diagrams, C4 architecture patterns
- BDD, UI diagrams in PlantUML+salt

## Files Created

1. **`test-equipment-inventory.md`** - Main equipment inventory with full documentation links
   - Located in `/mnt/user-data/outputs/`
   - ~600 lines, comprehensive markdown report

## Potential Next Steps

Ideas for extending this project:

1. **Add more equipment** - User may have additional instruments to document
2. **Create instrument automation scripts** - Python/C# code for controlling programmable instruments (Korad KA3005P, HP 34401A, Rigol instruments via USB/GPIB)
3. **Build LXI/VISA interface library** - Aligns with Matt's interest in centralizing bench instruments over network
4. **Create calibration tracking database** - SQLite schema to track calibration dates and results
5. **Generate PlantUML equipment diagrams** - Visual representation of bench setup and connections
6. **Add adapter/accessory inventory** - Document probe adapters, BNC cables, test leads, etc.

## Key Documentation URLs (Quick Reference)

### Rigol
- DS1102E Manual: https://cdn-shop.adafruit.com/datasheets/Users+Guide+DS1000E.pdf
- DG1022 Manual: http://pmaweb.caltech.edu/~phy003/DG1022_UserGuide_EN.pdf
- DM3058E Manual: https://www.batronix.com/files/Rigol/Multimeter/DM3058/DM3058_UserGuide_EN.pdf

### Tektronix
- TDS2024 Manual: https://neurophysics.ucsd.edu/Manuals/Tektronix/TDS%201000B%20and%20TDS%202000B%20Manual.pdf
- TDS2024 Service: https://download.tek.com/manual/071107602.pdf

### HP/Keysight
- 34401A User Guide: http://instructor.physics.lsa.umich.edu/adv-labs/Tools_Resources/HP%2034401A%20user's%20guide.pdf
- 34401A Service: https://www.keysight.com/us/en/assets/9018-05613/service-manuals/9018-05613.pdf

### Digilent
- Analog Discovery 2: https://cdn-shop.adafruit.com/product-files/4652/4652_manual.pdf
- WaveForms Software: https://digilent.com/reference/software/waveforms/waveforms-3/start

### Saleae
- Logic 2 Download: https://saleae.com/downloads
- User Guide: https://www.batronix.com/files/Saleae/Saleae+Users+Guide.pdf

### TL866II Plus
- Official Software: http://www.xgecu.com/en
- minipro (Linux): https://gitlab.com/DavidGriffith/minipro

### Bus Pirate
- SparkFun Guide: https://learn.sparkfun.com/tutorials/bus-pirate-v36a-hookup-guide/all
- Dangerous Prototypes Docs: http://dangerousprototypes.com/docs/Bus_Pirate

## Notes

- TDS2024 has TDS2CMA module (GPIB, RS-232, Centronics, FFT) but NO USB and NO CompactFlash
- Saleae is the original 8-channel digital-only version (not Logic 8 with analog)
- Bus Pirate is SparkFun v3.6a version
- HP 34401A provides highest precision (6½ digit) for calibration reference work
