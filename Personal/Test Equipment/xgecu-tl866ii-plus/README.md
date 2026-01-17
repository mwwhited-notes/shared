# XGecu TL866II Plus

**Universal USB Programmer**

## Unit Information

| Field | Value |
|-------|-------|
| Manufacturer | XGecu |
| Model | TL866II Plus |
| Type | Universal Programmer |
| Status | Working |
| Date Ordered | 2020-01-21 |
| Purchase Price | $59.99 |
| Source | Amazon (LAQIYA) |

## Specifications

| Specification | Value |
|--------------|-------|
| MCU | PIC24 |
| Interface | USB 1.1 |
| ZIF Socket | 40-pin |
| Supported ICs | 15,000+ |
| Max VPP | 18V |
| Operating Systems | Windows XP/7/8/10/11 |

## Supported Device Types

- **EEPROM/Flash:** 24/25/26/27/28/29/37/39/49/50 series (serial & parallel)
- **Microcontrollers:** 8051, Atmel AVR (ATmega, ATtiny, AT90), Microchip PIC (PIC10/12/16/18)
- **Programmable Logic:** GAL devices
- **Logic IC Testing:** 54/74 series, CD4000 CMOS

## Features

- ICSP interface
- Logic IC testing
- SRAM testing
- Project file support

## Documentation

- [User Manual (PDF)](https://www.obdii365.com/upload/pro/tl866ii_plus_usb_programmer_user_manual.pdf)
- [User Manual (Alternative)](https://www.hadex.cz/spec/m545b.pdf)
- [T56/TL866II User Guide (PDF)](http://xgecu.com/MiniPro/T56_TL866II%20USER%20GUIDE.pdf)

## Software - Windows (Official)

- [XGPro Download (Official)](http://www.xgecu.com/en)
- [Software Archive (GitHub Mirror)](https://github.com/Kreeblah/XGecu_Software)

## Software - Linux/macOS (Open Source)

- [minipro (GitLab)](https://gitlab.com/DavidGriffith/minipro) - Command-line programmer
- [TL866 Utilities (GitHub)](https://github.com/radiomanV/TL866) - Firmware tools & Wine wrapper

## Linux Installation (minipro)

```bash
sudo apt-get install build-essential pkg-config git libusb-1.0-0-dev
git clone https://gitlab.com/DavidGriffith/minipro.git
cd minipro
make
sudo make install
sudo cp udev/*.rules /etc/udev/rules.d/
sudo udevadm trigger
```

## Basic minipro Commands

```bash
minipro -L "CHIP"              # Search for chip
minipro -p "CHIP" -r out.bin   # Read chip to file
minipro -p "CHIP" -w in.bin    # Write file to chip
minipro -p "CHIP" -e           # Erase chip
minipro -p "CHIP" -c out.bin   # Verify chip against file
```

## Local Files

- `TL866II_UserManual.pdf` - User manual
