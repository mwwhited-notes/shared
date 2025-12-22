# Modern Op-Amp ICs for Analog Computing

## Overview

Modern integrated circuit operational amplifiers offer performance far exceeding the vacuum tube and early transistor op-amps of classic analog computers. This guide covers selecting and using modern op-amps for analog computing applications.

## Key Parameters for Analog Computing

### Critical Specifications

| Parameter | Importance | Target Value |
|-----------|------------|--------------|
| Input offset voltage | Critical | < 1 mV |
| Input bias current | High | < 100 nA (< 1 pA for FET) |
| Open-loop gain | High | > 100,000 |
| CMRR | High | > 80 dB |
| Slew rate | Medium | > 1 V/μs |
| GBW product | Medium | > 1 MHz |
| Offset drift | High | < 10 μV/°C |

### Why These Matter

**Input offset voltage:** Causes integrator drift
- 1mV offset with gain of 1000 → 1V error

**Input bias current:** Drains integrator capacitor
- 100nA into 1μF → 100mV/s drift

**Open-loop gain:** Affects accuracy of virtual ground
- Higher is better for precision

## Recommended Op-Amps

### General Purpose

| Device | Vos (μV) | Ib (nA) | GBW (MHz) | Notes |
|--------|----------|---------|-----------|-------|
| TL074 | 3000 | 0.03 | 3 | Quad, JFET, low cost |
| TL084 | 3000 | 0.03 | 3 | Quad, JFET |
| LM324 | 2000 | 45 | 1 | Quad, single supply capable |
| LM358 | 3000 | 45 | 1 | Dual |

### Precision

| Device | Vos (μV) | Ib (nA) | GBW (MHz) | Notes |
|--------|----------|---------|-----------|-------|
| OP07 | 75 | 3 | 0.6 | Classic precision |
| OP27 | 100 | 80 | 8 | Fast precision |
| OPA2277 | 50 | 2 | 1 | Dual precision |
| AD8676 | 15 | 2 | 10 | Very low offset |

### Chopper-Stabilized (Zero-Drift)

| Device | Vos (μV) | Drift (μV/°C) | GBW (MHz) | Notes |
|--------|----------|---------------|-----------|-------|
| OPA2188 | 25 | 0.085 | 2 | Dual, excellent |
| LTC2057 | 4 | 0.015 | 1.5 | Single, very precise |
| MAX44250 | 5 | 0.02 | 10 | Fast zero-drift |
| ADA4522 | 5 | 0.022 | 2.7 | Rail-to-rail |

### High Speed

| Device | Vos (mV) | GBW (MHz) | SR (V/μs) | Notes |
|--------|----------|-----------|-----------|-------|
| AD8065 | 1.5 | 145 | 180 | FET input |
| OPA2134 | 0.5 | 8 | 20 | Audio, low noise |
| AD744 | 0.25 | 13 | 75 | Precision, fast |
| LT1363 | 1 | 70 | 1000 | Very fast |

## Op-Amp Selection Guide

### For Integrators

**Primary concerns:** Offset, bias current, low-frequency accuracy

**Best choices:**
1. Chopper (zero-drift) for precision: OPA2188, LTC2057
2. Precision for moderate accuracy: OP07, OPA277
3. JFET input for low bias: TL074 (if offset acceptable)

### For Summers

**Primary concerns:** Offset, gain accuracy

**Best choices:**
1. Precision: OP07, OPA277
2. General: TL074, LM324

### For High-Speed Applications

**Primary concerns:** Bandwidth, slew rate

**Best choices:**
1. AD8065, LT1363, AD744
2. Balance speed vs. precision

### For Low Power

**Primary concerns:** Power consumption, battery operation

**Best choices:**
1. LPV821 (650 nA supply)
2. OPA379 (2.9 μA)
3. MCP6441 (450 nA)

## Practical Circuits

### Precision Integrator

```
                     C = 100nF
                ┌────────||────────┐
                │                  │
                │   Rf = 10MΩ      │ (optional, limits DC gain)
                ├────────/\/\/─────┤
                │                  │
Vin ────/\/\/───┴─────────────(-)──┐
        Rin = 100kΩ                │
                             OPA277├── Vout
                                   │
                    ┌─────────(+)──┘
                    │
                   ─┴─ GND

Time constant: τ = RC = 0.01s
```

### Summing Amplifier

```
                 Rf = 100kΩ
            ┌────────/\/\/────────┐
            │                     │
V1 ──/\/\/──┤                     │
     100kΩ  │                     │
            │                     │
V2 ──/\/\/──┼─────────────────(-)─┤
     100kΩ  │                     │
            │               OP07  ├── Vout = -(V1+V2+V3)
V3 ──/\/\/──┤                     │
     100kΩ  │                     │
            │        ┌────────(+)─┘
            │        │
            │       ─┴─ GND
            │
           ─┴─ GND
```

### Precision Inverter

```
            Rf = 100kΩ (matched)
       ┌────────/\/\/────────┐
       │                     │
Vin ───/\/\/─────────────(-)─┤
       Rin = 100kΩ           │
                       OP07  ├── Vout = -Vin
                             │
            ┌────────────(+)─┘
            │
           /\/\/ Rcomp = 50kΩ (for bias current compensation)
            │
           ─┴─ GND
```

## Power Supply Considerations

### Bipolar Supply

Most analog computing uses bipolar (±) supplies:
- **±12V:** Common, wide device selection
- **±15V:** Traditional, maximum swing
- **±5V:** Modern, lower power

### Decoupling

Critical for stable operation:
```
+V ───┬───────────────────────────┬─── to op-amp V+
      │                           │
     ═╪═ 10μF                    ═╪═ 100nF
      │ (electrolytic)            │ (ceramic)
      │                           │
     ─┴─ GND                     ─┴─ GND

(Same for -V)
```

### Voltage References

For precision coefficients:
- **REF5010:** ±10V, 0.1% initial accuracy
- **LT1021:** ±10V, very low drift
- **AD586:** +5V, precision

## Noise Considerations

### Noise Sources

| Source | Mitigation |
|--------|------------|
| Resistor thermal noise | Use lower values where possible |
| Op-amp voltage noise | Choose low-noise device |
| Op-amp current noise | Use lower source impedance |
| 1/f noise | Affects DC accuracy, use chopper |

### Low-Noise Op-Amps

| Device | Voltage Noise (nV/√Hz) | Notes |
|--------|------------------------|-------|
| OPA211 | 1.1 | Very low noise |
| AD8671 | 2.8 | Precision, low noise |
| OPA2134 | 8 | Good for audio |
| LT1028 | 0.85 | Lowest noise |

## Modern Considerations

### Rail-to-Rail Operation

Modern op-amps with rail-to-rail output:
- Maximize dynamic range
- Work with single supply
- Examples: OPA2340, MCP6022

### Programmable Gain Amplifiers

Digital control of analog gain:
- AD8253 (1, 10, 100, 1000)
- PGA112 (binary gains 1-128)

### Multichannel Devices

For compact systems:
- Quad packages: TL074, LM324, OPA4277
- Octal packages: OPA8171

## Comparison with Classic Op-Amps

| Parameter | 741 (1968) | Modern Precision | Improvement |
|-----------|------------|------------------|-------------|
| Vos | 5 mV | 5 μV | 1000× |
| Ib | 80 nA | 1 pA | 80,000× |
| GBW | 1 MHz | 10 MHz | 10× |
| Slew rate | 0.5 V/μs | 50 V/μs | 100× |
| Power | 50 mW | 1 mW | 50× |

## Recommended Starter Kit

For building analog computers:

1. **TL074** (general purpose, quad)
2. **OP07** (precision, single)
3. **OPA2277** (precision, dual)
4. **AD633** (multiplier)
5. **REF02** (5V reference)
6. **LM311** (comparator)

## References

[^1]: [Operational Amplifier - Wikipedia](https://en.wikipedia.org/wiki/Operational_amplifier)
[^2]: [Op-Amp Selection Guide - Texas Instruments](https://www.ti.com/lit/sg/slyt050/slyt050.pdf)
[^3]: [Zero-Drift Amplifiers - Analog Devices](https://www.analog.com/en/products/amplifiers/operational-amplifiers/zero-drift-amplifiers.html)
[^4]: [TL07x Datasheet - Texas Instruments](https://www.ti.com/lit/ds/symlink/tl071.pdf)
[^5]: [OP07 Datasheet - Analog Devices](https://www.analog.com/media/en/technical-documentation/data-sheets/op07.pdf)

## Further Reading

- [Op-Amp Basics](../01-fundamentals/02-op-amp-basics.md)
- [Integrators](../02-components/02-integrators.md)
- [DIY Projects](03-diy-projects.md)
