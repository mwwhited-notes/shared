# Altera USB Blaster

**FPGA/CPLD Programmer**

## Unit Information

| Field | Value |
|-------|-------|
| Manufacturer | Unknown (clone) |
| Model | USB-Blaster |
| Hardware Revision | Rev C (per label) |
| PCB Color | Green |
| Status | Working |
| Date Ordered | 2014-01-28 |
| Purchase Price | $14.50 |
| Source | Amazon (get005) |

## Specifications

| Specification | Value |
|--------------|-------|
| Target Devices | Altera/Intel FPGAs and CPLDs |
| Interface | USB 2.0 (Full Speed) |
| Programming Modes | JTAG, Active Serial (AS), Passive Serial (PS) |
| Connector | 10-pin JTAG header (2x5, 0.1" pitch) |
| Voltage | 1.5V to 5V target support |
| Max JTAG Clock | 24 MHz |

## Supported Device Families

- **CPLDs:** MAX II, MAX V, MAX 7000, MAX 3000
- **FPGAs:** Cyclone series, Stratix series, Arria series
- **Configuration Devices:** EPCS, EPCQ serial flash

## Pinout (10-pin JTAG)

```
        ┌─────────┐
   TCK  │ 1     2 │  GND
        │         │
   TDO  │ 3     4 │  VCC
        │         │
   TMS  │ 5     6 │  N/C
        │         │
   N/C  │ 7     8 │  N/C
        │         │
   TDI  │ 9    10 │  GND
        └─────────┘
```

## Documentation

- [USB-Blaster Download Cable User Guide (Intel)](https://www.intel.com/content/dam/www/programmable/us/en/pdfs/literature/ug/ug_usb_blstr.pdf)
- [Intel FPGA Download Cables](https://www.intel.com/content/www/us/en/support/programmable/support-resources/download-cable.html)

## Software

- **Quartus Prime** (current) - Intel FPGA development suite
- **Quartus II** (legacy) - For older device families
- **OpenOCD** - Open-source alternative (limited support)
- **UrJTAG** - Open-source JTAG tools

## Driver Installation (Windows)

Drivers are installed automatically with Quartus software:
1. Install Quartus Prime or Quartus II
2. Connect USB-Blaster
3. Drivers should install automatically from `<quartus_install>\drivers\usb-blaster`

Manual driver installation:
1. Device Manager → Unknown Device
2. Update Driver → Browse → `<quartus_install>\drivers\usb-blaster`

## Usage with Quartus

1. Open Quartus Programmer (Tools → Programmer)
2. Click "Hardware Setup"
3. Select "USB-Blaster" from dropdown
4. Add programming file (.sof, .pof, .jic)
5. Click "Start"

## Notes

- Green PCB labeled "USB-Blaster"
- Works with older Quartus II software for CPLD programming
- Unknown if genuine Terasic/Altera or clone
- Clone USB-Blasters generally work identically to genuine ones

## Local Files

- `USB-Blaster_UserGuide.pdf` - Intel user guide
