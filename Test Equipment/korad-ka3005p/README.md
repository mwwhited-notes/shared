# Korad KA3005P

**Programmable DC Power Supply**

## Specifications

| Specification | Value |
|--------------|-------|
| Type | Linear regulated |
| Output | 0-30 V, 0-5 A, 150 W max |
| Display | Dual 4-digit LED |
| Resolution | 0.001 V / 0.001 A |
| Voltage Accuracy | ±0.5% + 20 mV |
| Current Accuracy | ±0.5% + 10 mA |
| Ripple | <2 mVrms voltage, <3 mArms current |
| Interfaces | USB, RS-232 |

## Features

- CV/CC modes
- 4 programmable memory presets
- OCP/OVP protection

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

- [User Manual (PDF)](https://static.eleshop.nl/mage/media/downloads/KA3005P_user_manual.pdf)
- [User Manual (Digikey)](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/4151/KA3000_6000_Series_Man.pdf)
- [Programming Reference](https://www.sra-shops.com/pub/media/docs/srasolder/instructions/kd3005p-user-manual.pdf)

## Software

- **KORAD PC software** - Official control software
- **sigrok** - Open source, cross-platform support

## Local Files

- `KA3005P_UserManual.pdf` - User manual
