# Korad KA6003P

**Programmable DC Power Supply**

## Unit Information

| Field | Value |
|-------|-------|
| Manufacturer | Korad |
| Model | KA6003P |
| Type | Linear Regulated DC Power Supply |
| Status | On Order |
| Condition | New |

## Specifications

| Specification | Value |
|--------------|-------|
| Type | Linear regulated |
| Output | 0-60 V, 0-3 A, 180 W max |
| Display | Dual 4-digit LED |
| Resolution | 10 mV / 1 mA |
| Display Resolution | 0.001 V / 0.001 A |
| Voltage Accuracy | ±0.5% + 20 mV |
| Current Accuracy | ±0.5% + 10 mA |
| Ripple | <2 mVrms voltage, <3 mArms current |
| Temperature Coefficient | ≤100 ppm (voltage and current) |
| Reaction Time | ≤100 ms (10% rated load) |
| Interfaces | USB, RS-232 |
| Input Voltage | 110V/220V switchable (±10%) |
| Input Frequency | 50-60 Hz |
| Operating Temp | 0-40°C (32-104°F) |
| Storage Temp | 0-70°C (32-158°F) |

## Features

- CV/CC (Constant Voltage/Constant Current) modes
- 4 programmable memory presets (M1-M4)
- OCP (Overcurrent Protection)
- OVP (Overvoltage Protection)
- Low ripple and noise
- Remote control via USB/RS-232

## SCPI Commands

```
*IDN?          # Identity query
VSET1:<value>  # Set voltage
ISET1:<value>  # Set current
VOUT1?         # Query actual voltage
IOUT1?         # Query actual current
OUT1           # Toggle output
STATUS?        # Query status
RCL1-4         # Recall preset
SAV1-4         # Save preset
```

## Documentation

- [Korad Official Product Page](https://www.koradtechnology.com/product/73.html)
- [User Manual (Digikey)](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/4151/KA3000_6000_Series_Man.pdf)

## Software

- **KORAD PC software** - Official control software (included)
- **sigrok** - Open source, cross-platform support

## Package Contents

- KA6003P Power Supply
- Power cord
- 5A test leads
- User manual

## Notes

Higher voltage version of the KA3005P (60V/3A vs 30V/5A). Same power rating (180W), uses identical SCPI command set and software.

## Local Files

- `KA6003P_UserManual.pdf` - KA Series User Manual (162KB)

## Revision History

| Date | Change |
|------|--------|
| 2024-12-24 | Initial entry (unit on order) |
