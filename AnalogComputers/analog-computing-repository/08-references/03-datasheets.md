# Component Datasheets

## Overview

This reference provides key specifications and links to datasheets for components commonly used in analog computing.

## Operational Amplifiers

### General Purpose

#### TL071/TL074 (JFET Input)

| Parameter | TL071 | TL074 |
|-----------|-------|-------|
| Type | Single | Quad |
| Vos (typ) | 3 mV | 3 mV |
| Ib (typ) | 30 pA | 30 pA |
| GBW | 3 MHz | 3 MHz |
| Slew Rate | 13 V/μs | 13 V/μs |
| Supply | ±15V | ±15V |

**Datasheet:** Texas Instruments - search "TL074 datasheet"

**Use:** General purpose, low bias current applications

#### LM741

| Parameter | Value |
|-----------|-------|
| Type | Single |
| Vos (typ) | 2 mV |
| Ib (typ) | 80 nA |
| GBW | 1 MHz |
| Slew Rate | 0.5 V/μs |
| Supply | ±15V |

**Datasheet:** Multiple manufacturers

**Use:** Historic reference, educational (not for precision)

#### LM324/LM358

| Parameter | LM324 | LM358 |
|-----------|-------|-------|
| Type | Quad | Dual |
| Vos (typ) | 2 mV | 3 mV |
| Ib (typ) | 45 nA | 45 nA |
| GBW | 1 MHz | 1 MHz |
| Supply | Single or dual | Single or dual |

**Use:** Low cost, single-supply capable

### Precision Op-Amps

#### OP07

| Parameter | Value |
|-----------|-------|
| Type | Single |
| Vos (typ) | 60 μV |
| Vos drift | 0.6 μV/°C |
| Ib (typ) | 3 nA |
| GBW | 600 kHz |
| Supply | ±15V |

**Datasheet:** Analog Devices

**Use:** Precision integrators, low-offset applications

#### OPA277/OPA2277

| Parameter | OPA277 | OPA2277 |
|-----------|--------|---------|
| Type | Single | Dual |
| Vos (typ) | 20 μV | 20 μV |
| Vos drift | 0.1 μV/°C | 0.1 μV/°C |
| Ib (typ) | 1 nA | 1 nA |
| GBW | 1 MHz | 1 MHz |

**Datasheet:** Texas Instruments

**Use:** High precision, low drift

#### AD8676

| Parameter | Value |
|-----------|-------|
| Type | Dual |
| Vos (typ) | 12 μV |
| Vos drift | 0.1 μV/°C |
| Noise | 2.8 nV/√Hz |
| GBW | 10 MHz |

**Datasheet:** Analog Devices

**Use:** Highest precision applications

### Zero-Drift (Chopper) Op-Amps

#### OPA2188

| Parameter | Value |
|-----------|-------|
| Type | Dual |
| Vos (max) | 25 μV |
| Vos drift | 0.085 μV/°C |
| Ib (typ) | 250 pA |
| GBW | 2 MHz |

**Datasheet:** Texas Instruments

**Use:** Precision integrators with minimal drift

#### LTC2057

| Parameter | Value |
|-----------|-------|
| Type | Single |
| Vos (max) | 4 μV |
| Vos drift | 0.015 μV/°C |
| GBW | 1.5 MHz |

**Datasheet:** Analog Devices (Linear Technology)

**Use:** Highest precision, long-term integration

## Analog Multipliers

### AD633

| Parameter | Value |
|-----------|-------|
| Configuration | 4-quadrant |
| Scale factor | 10V |
| Accuracy | 2% |
| Bandwidth | 1 MHz |
| Supply | ±15V |

**Transfer function:** W = (X1-X2)(Y1-Y2)/10V + Z

**Datasheet:** Analog Devices

**Use:** General multiplication, squaring, division

### AD534

| Parameter | Value |
|-----------|-------|
| Configuration | 4-quadrant |
| Scale factor | 10V |
| Accuracy | 0.1% (trimmed) |
| Bandwidth | 1 MHz |
| Supply | ±15V |

**Datasheet:** Analog Devices

**Use:** Precision multiplication

### MPY634

| Parameter | Value |
|-----------|-------|
| Configuration | 4-quadrant |
| Scale factor | 10V |
| Accuracy | 0.5% |
| Bandwidth | 10 MHz |
| Supply | ±15V |

**Datasheet:** Texas Instruments

**Use:** Wideband multiplication

## Comparators

### LM311

| Parameter | Value |
|-----------|-------|
| Response time | 200 ns |
| Output type | Open collector |
| Supply | ±15V or single |

**Datasheet:** Texas Instruments

**Use:** General purpose comparison, Schmitt triggers

### LM339

| Parameter | Value |
|-----------|-------|
| Type | Quad |
| Response time | 1.3 μs |
| Output type | Open collector |

**Datasheet:** Multiple manufacturers

**Use:** Multiple comparators, window comparators

## Voltage References

### REF02/REF5050 (5V)

| Parameter | REF02 | REF5050 |
|-----------|-------|---------|
| Output | 5.000V | 5.000V |
| Initial accuracy | 0.3% | 0.05% |
| Temp coefficient | 8.5 ppm/°C | 3 ppm/°C |

**Use:** Precision reference for coefficients

### REF5010 (10V)

| Parameter | Value |
|-----------|-------|
| Output | 10.000V |
| Initial accuracy | 0.05% |
| Temp coefficient | 3 ppm/°C |
| Noise | 3 μVpp |

**Datasheet:** Texas Instruments

**Use:** ±10V reference for analog computers

### LT1021

| Parameter | Value |
|-----------|-------|
| Output | 10.000V |
| Initial accuracy | 0.05% |
| Temp coefficient | 5 ppm/°C |

**Datasheet:** Analog Devices

**Use:** Precision 10V reference

## Passive Components

### Precision Resistors

| Type | Tolerance | Temp Coefficient |
|------|-----------|------------------|
| Metal Film | 1% | 50-100 ppm/°C |
| Precision Metal Film | 0.1% | 15-25 ppm/°C |
| Wirewound | 0.01% | 5-20 ppm/°C |
| Bulk Metal Foil | 0.005% | 0.2-2 ppm/°C |

**Recommended for analog computing:** 1% or 0.1% metal film

### Precision Capacitors

| Type | Tolerance | Temp Coeff | Use |
|------|-----------|------------|-----|
| Polypropylene | 1-5% | ±200 ppm/°C | Integrators |
| Polystyrene | 0.5-2% | -120 ppm/°C | Precision |
| NP0/C0G Ceramic | 1-5% | ±30 ppm/°C | Decoupling, filters |
| Teflon (PTFE) | 0.5-2% | -170 ppm/°C | Highest precision |

### Precision Potentiometers

| Type | Turns | Resolution | Linearity |
|------|-------|------------|-----------|
| Standard wirewound | 10 | 0.03% | 0.25% |
| Precision wirewound | 10 | 0.01% | 0.1% |
| Cermet | 10-15 | 0.05% | 0.15% |
| Conductive plastic | 1-10 | 0.1% | 0.1% |

**Recommended:** 10-turn wirewound with dial counter

## Digital Potentiometers

### AD5293

| Parameter | Value |
|-----------|-------|
| Resolution | 10-bit (1024 steps) |
| End-to-end resistance | 20k, 50k, 100k |
| Wiper resistance | 35Ω typ |
| Interface | SPI |

**Datasheet:** Analog Devices

**Use:** Digitally controlled coefficients

### MCP4131

| Parameter | Value |
|-----------|-------|
| Resolution | 7-bit (128 steps) |
| Resistance | 5k-100k options |
| Interface | SPI |

**Datasheet:** Microchip

**Use:** Low-cost digital coefficient setting

## Analog Switches

### DG411

| Parameter | Value |
|-----------|-------|
| Type | Quad SPST |
| Ron | 25Ω |
| Leakage | 0.5 nA |
| Supply | ±15V |

**Datasheet:** Vishay

**Use:** Mode switching, sample-and-hold

### ADG1234

| Parameter | Value |
|-----------|-------|
| Type | Quad SPDT |
| Ron | 4Ω |
| Leakage | 1.5 nA |
| Bandwidth | 400 MHz |

**Datasheet:** Analog Devices

**Use:** High-speed switching

## Data Converters

### ADC (for hybrid systems)

| Device | Resolution | Sample Rate |
|--------|------------|-------------|
| ADS8688 | 16-bit | 500 kSPS |
| AD7606 | 16-bit | 200 kSPS |
| MCP3208 | 12-bit | 100 kSPS |

### DAC (for coefficient setting)

| Device | Resolution | Settling |
|--------|------------|----------|
| AD5764 | 16-bit | 10 μs |
| DAC8568 | 16-bit | 1 μs |
| MCP4728 | 12-bit | 6 μs |

## Supplier Part Numbers

### Digi-Key Suggested Cart (Basic Kit)

| Description | Part Number | Qty |
|-------------|-------------|-----|
| TL074CN | 296-1780-5-ND | 2 |
| OP07CP | OP07CPZ-ND | 2 |
| AD633JNZ | AD633JNZ-ND | 1 |
| REF5050 | 296-25771-5-ND | 1 |
| 10k 1% resistor | 13-MFR-25FRF52-10KCT-ND | 20 |
| 100k 1% resistor | 13-MFR-25FRF52-100KCT-ND | 20 |
| 1μF polypropylene | 338-1115-ND | 10 |
| 0.1μF ceramic | 399-C0805C104K5RACTU-ND | 20 |

## Further Reading

- [Modern Op-Amps](../06-modern-systems/02-modern-op-amps.md)
- [DIY Projects](../06-modern-systems/03-diy-projects.md)
