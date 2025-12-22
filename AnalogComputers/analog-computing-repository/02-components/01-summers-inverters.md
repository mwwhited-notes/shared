# Summers and Inverters

## Overview

Summers (adders) and inverters are the most fundamental building blocks of analog computers. They perform the basic operations of signal combination and sign inversion.

## The Inverting Amplifier (Inverter)

### Circuit

```
            Rf
       ┌────/\/\/────┐
       │             │
       │      ┌─────(-)──┐
Vin ───/\/\/──┤          │
        Rin   │    OP    ├── Vout = -(Rf/Rin)·Vin
              │          │
         ┌───(+)─────────┘
         │
         ▼
        GND
```

### Transfer Function

```
Vout = -(Rf/Rin) × Vin
```

For unity gain inverter (Rf = Rin):
```
Vout = -Vin
```

### Analysis Using Golden Rules

1. Virtual ground at (-) input: V(-) = V(+) = 0
2. No current into inputs: All current through Rin flows through Rf

```
Current: I = Vin/Rin = -Vout/Rf
Therefore: Vout = -(Rf/Rin)·Vin
```

### Standard Configurations

| Configuration | Rf/Rin | Gain | Use |
|---------------|--------|------|-----|
| Unity inverter | 1 | -1 | Sign change |
| Gain of 2 | 2 | -2 | Amplification |
| Gain of 10 | 10 | -10 | Large amplification |
| Attenuator | 0.5 | -0.5 | Reduce signal |

### Practical Circuit (Unity Inverter)

```
        10kΩ
   ┌────/\/\/────┐
   │             │
   │      ┌─────(-)──┐
Vin─/\/\/─┤    741   ├── Vout = -Vin
   10kΩ   │          │
          │          │
     ┌───(+)─────────┘
     │
    ═╧═
    GND
```

**Component Values:**
- Rin = Rf = 10kΩ (standard)
- Use 1% metal film resistors for accuracy
- Add compensation capacitor if needed (10-100pF across Rf)

## The Summing Amplifier (Summer)

### Circuit

```
             Rf
        ┌────/\/\/────┐
        │             │
V1 ─────/\/\/──┬─────(-)──┐
         R1    │          │
               │    OP    ├── Vout
V2 ─────/\/\/──┤          │
         R2    │          │
               │          │
V3 ─────/\/\/──┘     ┌───(+)─┘
         R3          │
                     ▼
                    GND
```

### Transfer Function

```
Vout = -Rf × (V1/R1 + V2/R2 + V3/R3)
```

For equal resistors (R1 = R2 = R3 = R):
```
Vout = -(Rf/R) × (V1 + V2 + V3)
```

For unity-gain summing (Rf = R):
```
Vout = -(V1 + V2 + V3)
```

### Weighted Summer

Different input resistors give weighted sums:

```
Vout = -(a·V1 + b·V2 + c·V3)

where: a = Rf/R1, b = Rf/R2, c = Rf/R3
```

**Example: Vout = -(2V1 + 0.5V2 + V3)**
```
With Rf = 10kΩ:
- R1 = 5kΩ (gain = 2)
- R2 = 20kΩ (gain = 0.5)
- R3 = 10kΩ (gain = 1)
```

### Standard Summer Configurations

| Inputs | Equal Resistors | Total Gain | Output |
|--------|-----------------|------------|--------|
| 2 | R | -1 | -(V1 + V2) |
| 3 | R | -1 | -(V1 + V2 + V3) |
| 4 | R | -1 | -(V1 + V2 + V3 + V4) |
| 2 | R | -10 | -10(V1 + V2) |

### Practical 4-Input Summer

```
              20kΩ
         ┌────/\/\/────┐
         │             │
V1 ──────/\/\/──┬─────(-)──┐
          20kΩ  │          │
                │          │
V2 ──────/\/\/──┤   TL074  ├── Vout = -(V1+V2+V3+V4)
          20kΩ  │          │
                │          │
V3 ──────/\/\/──┤          │
          20kΩ  │          │
                │     ┌───(+)─┘
V4 ──────/\/\/──┘     │
          20kΩ        ▼
                     GND
```

## Combining Summers and Inverters

### Subtraction

To compute V1 - V2:
```
              ┌───────┐     ┌───────┐
V2 ──────────>│  -1   ├────>│       │
              │ (INV) │     │  SUM  ├──> -(V1 + (-V2)) = -(V1 - V2)
              └───────┘ ┌──>│       │
                        │   └───────┘
V1 ─────────────────────┘

Need another inverter for V1 - V2 (positive result)
```

### Differential Amplifier (Direct Subtraction)

```
             R2
        ┌────/\/\/────┐
        │             │
V1 ─────/\/\/────────(-)──┐
         R1               │
                    OP    ├── Vout = (R2/R1)(V2 - V1)
                          │
V2 ─────/\/\/────────(+)──┘
         R1    │
               │
              /\/\/ R2
               │
               ▼
              GND
```

When R1 = R2:
```
Vout = V2 - V1
```

## Input Considerations

### Input Impedance

The input impedance of each input is simply the input resistor:
```
Zin = Rin
```

This means the source must be able to drive this load.

### Loading Effects

When connecting multiple modules:
```
Source ──┬── Input 1 (10kΩ)
         │
         ├── Input 2 (10kΩ)
         │
         └── Input 3 (10kΩ)

Total load = 10kΩ || 10kΩ || 10kΩ = 3.3kΩ
```

Source op-amp must handle this current.

### Input Current

```
Iin = Vin / Rin

For Vin = 10V, Rin = 10kΩ:
Iin = 1 mA per input
```

## Offset and Error Considerations

### Offset Voltage

Op-amp input offset voltage appears amplified at output:
```
Vout(offset) = Vos × (1 + Rf/Rin)
```

For precision work:
- Use low-offset op-amps (OP07, LT1013)
- Add offset trim potentiometer
- Use chopper-stabilized op-amps

### Bias Current Compensation

To minimize bias current errors, add compensation resistor:

```
             Rf
        ┌────/\/\/────┐
        │             │
Vin ────/\/\/────────(-)──┐
         Rin              │
                    OP    ├── Vout
                          │
               ┌─────(+)──┘
               │
              /\/\/ Rcomp = Rin || Rf
               │
               ▼
              GND
```

## Frequency Response

### Bandwidth Limitation

For inverting amplifier with gain G:
```
Bandwidth = GBW / |G|

Example: 741 with GBW = 1MHz, G = -10
BW = 1MHz / 10 = 100kHz
```

### Compensation for Stability

For high-frequency stability, add feedback capacitor:
```
            Cf (10-100pF)
        ┌────||────┐
        │          │
        │    Rf    │
        ├───/\/\/──┤
        │          │
Vin ────/\/\/─────(-)──┐
         Rin           │
                 OP    ├── Vout
                       │
              ┌───(+)──┘
              │
              ▼
             GND
```

## Typical Specifications for Analog Computing

### Summer Module

| Parameter | Specification |
|-----------|---------------|
| Inputs | 4-8 |
| Input impedance | 10kΩ - 100kΩ |
| Output impedance | < 100Ω |
| Gain accuracy | 0.01% |
| Bandwidth | > 100kHz |
| Output range | ±10V |

### Inverter Module

| Parameter | Specification |
|-----------|---------------|
| Gain | -1.000 ±0.01% |
| Input impedance | 10kΩ |
| Bandwidth | > 1MHz |
| Offset | < 1mV |

## Applications in Analog Computing

### Sign Inversion in Feedback Loops

```
┌───────────────────────────────────┐
│                                   │
│    ┌───────┐     ┌───────┐       │
│───>│  -1   ├────>│       │       │
│    │       │     │  INT  ├───┬───┘
│    └───────┘ ┌──>│       │   │
│              │   └───────┘   │
│              │               │
└──────────────┴───────────────┘
```

### Combining Equation Terms

For: `y = a·x1 + b·x2 - c·x3`

```
x1 ──[pot:a]──┐
              │
x2 ──[pot:b]──┼──[SUM]──[INV]── y
              │
x3 ──[pot:c]──[INV]─┘
```

## Summary

| Element | Symbol | Function | Key Formula |
|---------|--------|----------|-------------|
| Inverter | -1 | Negate | Vout = -Vin |
| Amplifier | -k | Scale & negate | Vout = -k·Vin |
| Summer | Σ | Add (inverted) | Vout = -(V1+V2+...) |
| Weighted Sum | Σ | Weighted add | Vout = -(a·V1+b·V2+...) |

## Further Reading

- [Integrators](02-integrators.md)
- [Op-Amp Basics](../01-fundamentals/02-op-amp-basics.md)
