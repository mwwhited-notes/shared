# Component Datasheets

This folder contains datasheet summaries and links to official manufacturer datasheets for components commonly used in analog computing.

## Op-Amps

| Component | Manufacturer | Type | Datasheet Link |
|-----------|--------------|------|----------------|
| TL071/TL074 | Texas Instruments | JFET Quad | [TI Datasheet](https://www.ti.com/lit/ds/symlink/tl074.pdf) |
| LM741 | Texas Instruments | General Purpose | [TI Datasheet](https://www.ti.com/lit/ds/symlink/lm741.pdf) |
| LM324 | Texas Instruments | Quad | [TI Datasheet](https://www.ti.com/lit/ds/symlink/lm324.pdf) |
| OP07 | Analog Devices | Precision | [ADI Datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/op07.pdf) |
| OPA277 | Texas Instruments | Precision | [TI Datasheet](https://www.ti.com/lit/ds/symlink/opa277.pdf) |
| AD8676 | Analog Devices | Ultra Precision | [ADI Datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/AD8676.pdf) |

## Multipliers

| Component | Manufacturer | Type | Datasheet Link |
|-----------|--------------|------|----------------|
| AD633 | Analog Devices | 4-Quadrant | [ADI Datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/ad633.pdf) |
| AD534 | Analog Devices | Precision | [ADI Datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/AD534.pdf) |
| MPY634 | Texas Instruments | Wide Bandwidth | [TI Datasheet](https://www.ti.com/lit/ds/symlink/mpy634.pdf) |

## Voltage References

| Component | Manufacturer | Voltage | Datasheet Link |
|-----------|--------------|---------|----------------|
| REF5010 | Texas Instruments | 10V | [TI Datasheet](https://www.ti.com/lit/ds/symlink/ref5010.pdf) |
| LT1021 | Analog Devices | 10V | [ADI Datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/1021fc.pdf) |
| REF02 | Texas Instruments | 5V | [TI Datasheet](https://www.ti.com/lit/ds/symlink/ref02.pdf) |

## Comparators

| Component | Manufacturer | Type | Datasheet Link |
|-----------|--------------|------|----------------|
| LM311 | Texas Instruments | General | [TI Datasheet](https://www.ti.com/lit/ds/symlink/lm311.pdf) |
| LM339 | Texas Instruments | Quad | [TI Datasheet](https://www.ti.com/lit/ds/symlink/lm339.pdf) |

## Datasheet Summaries

Detailed summaries of key components are available in this folder:

- [TL074 JFET Op-Amp](01-tl074.md)
- [OP07 Precision Op-Amp](02-op07.md)
- [AD633 Analog Multiplier](03-ad633.md)
- [LM741 General Purpose Op-Amp](04-lm741.md)

## Notes on Component Selection

### For Integrators
- Use precision op-amps (OP07, OPA277) for low drift
- JFET inputs (TL074) reduce bias current errors
- Zero-drift op-amps (OPA2188) for highest precision

### For Summers
- General purpose (TL074, LM324) usually sufficient
- Match resistors for accurate gain ratios

### For Multipliers
- AD633 is the most common choice for analog computing
- 1% accuracy typical
- Scale factor of 10V denominator

