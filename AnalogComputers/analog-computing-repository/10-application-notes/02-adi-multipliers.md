# Analog Devices Multiplier Applications

## Overview

Analog multipliers are essential for solving nonlinear differential equations and implementing mathematical operations beyond addition and integration. This summary covers applications of the AD633 and related Analog Devices multipliers.

**Related Documents:**
- [AD633 Datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/ad633.pdf)
- [AN-106: A Collection of Amp Applications](https://www.analog.com/media/en/technical-documentation/application-notes/28080533an106.pdf)

## AD633 Transfer Function

```
W = (X1 - X2)(Y1 - Y2) / 10V + Z
```

The built-in 10V scale factor means:
- Full-scale inputs (±10V on X and Y) produce ±10V output
- No external scaling resistors needed
- Direct interface to ±10V analog computer signals

## Four-Quadrant Multiplication

The AD633 performs four-quadrant multiplication:

| X | Y | Output (XY/10) |
|---|---|----------------|
| + | + | + |
| + | - | - |
| - | + | - |
| - | - | + |

This is essential for analog computing where variables can be positive or negative.

## Basic Multiplication Circuit

```
X input ──── X1 ─┐
                 │
     GND ──── X2 ┤
                 │      ┌─── W = XY/10
Y input ──── Y1 ─┤ AD633│
                 │      │
     GND ──── Y2 ┤      │
                 │      │
     GND ──── Z ─┘      │
                        │
         +15V ─── V+ ───┘
         -15V ─── V-
```

## Squaring Circuit

Used for computing x² terms in differential equations.

```
Input X ──┬── X1 ─┐
          │       │
   GND ── │  X2 ──┤
          │       │      ┌─── W = X²/10
          └── Y1 ─┤ AD633│
                  │      │
       GND ── Y2 ─┤      │
                  │      │
       GND ── Z ──┘      │
```

**Output:** W = X²/10

**Example:** For X = 5V:
- W = (5)²/10 = 2.5V

## Division Circuit

Division uses feedback around the multiplier.

```
                      ┌────────────────────┐
                      │                    │
Numerator N ──── X1 ──┤                    │
                      │                    │
         GND ──── X2 ─┤       AD633        ├─── W = 10N/D
                      │                    │
              ┌── Y1 ─┤                    │
              │       │                    │
         GND ─│  Y2 ──┤                    │
              │       │                    │
         GND ─│  Z ───┘                    │
              │                            │
              └────────────────────────────┘
                   (feedback to Y1)

Denominator D connected through feedback:
Y1 = W, so W × D = 10N
Therefore: W = 10N/D
```

**Constraints:**
- Denominator D must be positive
- Valid for D > 0.5V (for reasonable accuracy)
- Output limited to ±10V

## Square Root Circuit

```
              ┌────────────────────────────┐
              │                            │
Input V ─────X1 ─┐                         │
                 │                         │
      GND ── X2 ─┤                         │
                 │                         │
          ┌─ Y1 ─┤       AD633       ├─────┴── W = √(10V)
          │      │                   │
      GND │  Y2 ─┤                   │
          │      │                   │
      GND │  Z ──┘                   │
          │                          │
          └──────────────────────────┘
              (feedback to Y1)

W² = V × 10
W = √(10V)
```

**For V = 4V:** W = √(40) = 6.32V

## Applications in Analog Computing

### 1. Lorenz System xy Term

The Lorenz equations include the term xy:
```
dz/dt = xy - βz
```

```
x ──── X1 ─┐
           │
GND ── X2 ─┤
           │      ┌─── xy/10
y ──── Y1 ─┤ AD633│
           │      │
GND ── Y2 ─┤      │
           │      │
GND ── Z ──┘      │
```

Scale by 10 in subsequent summer if needed.

### 2. Van der Pol x²x' Term

The Van der Pol equation: x'' - μ(1-x²)x' + x = 0

Requires computing x² and then multiplying by x':

```
Stage 1: Square x
x ──┬── X1 ─┐
    │       │        ┌─── x²/10
    └── Y1 ─┤ AD633 ─┤
            │        │
    GND ────┘        │

Stage 2: Compute (1 - x²/10)
1V ──┐
     ├── Summer ── (1 - x²/10)
x²/10┘

Stage 3: Multiply by x'
(1-x²/10) ── X1 ─┐
                 │      ┌─── (1-x²)x'/10
x' ───────── Y1 ─┤ AD633│
                 │      │
        GND ─────┘      │
```

### 3. Modulation / Demodulation

**Amplitude Modulation:**
```
Carrier ──── X1 ─┐
                 │      ┌─── AM signal
Signal ───── Y1 ─┤ AD633│
(+ DC offset)    │      │
         GND ────┘      │

Output = Carrier × (DC + Signal)/10
```

### 4. Phase-Sensitive Detection

```
Signal ──────── X1 ─┐
                    │      ┌─── DC output
Reference ───── Y1 ─┤ AD633│    (proportional to
                    │      │     signal amplitude
            GND ────┘      │     at reference freq)
                           │
                    ┌──────┘
                    │
                  [LPF]
                    │
              DC out
```

### 5. RMS-to-DC Conversion

```
             ┌────────────────────────────┐
             │                            │
Input ───────X1 ─┐                        │
                 │                        │
Input ────┬─ Y1 ─┤                        │
          │      │       AD633            │
      GND │  X2 ─┤                        ├──── RMS
          │      │                        │
      GND │  Y2 ─┤                        │
          │      │                        │
Filtered─│── Z ──┘                        │
          │                               │
          │    ┌──────────────────────────┘
          │    │
          │  [LPF]
          │    │
          └────┴──(feedback)

Computes: √(mean(V²))
```

## Error Sources and Compensation

### Scale Factor Error

Typical ±1% scale factor error can be trimmed:

```
               Rscale (trim)
                 ┌───┐
X ──┬───────────┤   ├─── X1
    │           └─┬─┘
    │             │
    └─────────────┘

Adjust Rscale to calibrate 10V scale factor
```

### Offset Compensation

Use Z input for output offset trim:

```
             Offset
              Trim
               │
       ±100mV ─┴─ Z
```

### Feedthrough Nulling

For minimum X and Y feedthrough:
- Balance X1/X2 and Y1/Y2 inputs
- Add small trim voltage to unused input

## Specifications Summary

| Parameter | AD633 | AD534 | AD734 |
|-----------|-------|-------|-------|
| Total Error | ±1% | ±0.25% | ±0.1% |
| Bandwidth | 1 MHz | 1 MHz | 10 MHz |
| Slew Rate | 20 V/μs | 20 V/μs | 450 V/μs |
| Supply | ±8V to ±18V | ±8V to ±18V | ±4V to ±18V |

## When to Use Different Multipliers

| Application | Recommended |
|-------------|-------------|
| General analog computing | AD633 |
| High precision | AD534 |
| High frequency | AD734 |
| Low cost, moderate precision | AD633 |
| True RMS measurement | AD534 or AD734 |

## References

1. Analog Devices, "AD633 Datasheet," Rev. K.
2. Analog Devices, "AN-106: A Collection of Amp Applications."
3. Analog Devices, "Nonlinear Circuits Handbook."

