# Multipliers and Dividers

## Overview

Analog multipliers and dividers enable nonlinear operations in analog computers. Unlike the linear operations of summers and integrators, multiplication allows solving nonlinear differential equations and implementing complex mathematical functions.

## Analog Multiplier Fundamentals

An analog multiplier produces an output that is the product of two input signals[^1]:

```
Vout = K × Vx × Vy
```

Where K is a scale factor (typically 0.1 V⁻¹ for ±10V systems).

### Four-Quadrant Operation

A four-quadrant multiplier handles all sign combinations[^2]:

| Quadrant | Vx | Vy | Vout |
|----------|----|----|------|
| I | + | + | + |
| II | - | + | - |
| III | - | - | + |
| IV | + | - | - |

```
        Vy
        ↑
   II   │   I
   (-×+)│(+×+)
────────┼────────→ Vx
   III  │   IV
   (-×-)│(+×-)
        │
```

## Multiplier Techniques

### 1. Log-Antilog Method

The most common IC implementation uses logarithmic properties[^3]:

```
log(X × Y) = log(X) + log(Y)

Therefore: X × Y = antilog(log(X) + log(Y))
```

**Block Diagram:**
```
Vx ──[LOG]──┬──[SUM]──[ANTILOG]── Vx × Vy
            │
Vy ──[LOG]──┘
```

**Transistor Implementation:**

The base-emitter voltage of a transistor is logarithmically related to collector current[^4]:
```
VBE = (kT/q) × ln(IC/IS)
```

This natural logarithmic relationship enables accurate multiplication.

### 2. Gilbert Cell

The Gilbert cell is a popular transconductance multiplier topology[^2]:

```
                    +V
                     │
              ┌──────┼──────┐
              │      │      │
             RL     RL     RL
              │      │      │
    ┌─────────┼──────┼──────┼─────────┐
    │         │      │      │         │
   Q3        Q4     Q5     Q6        (output)
    │         │      │      │
    └────┬────┘      └────┬────┘
         │                │
        Q1               Q2
         │                │
         └───────┬────────┘
                 │
                Iee
                 │
                GND

Vy controls Q1/Q2 pair
Vx controls Q3/Q4 and Q5/Q6 pairs
```

**Advantages:**
- High bandwidth (100+ MHz)
- Good accuracy
- Fully differential

### 3. Quarter-Square Multiplier

Uses the algebraic identity[^5]:
```
X × Y = ¼[(X + Y)² - (X - Y)²]
```

**Block Diagram:**
```
    ┌──[+]──[SQR]──┐
Vx ─┤              ├──[DIFF]── Vout = Vx × Vy
    │              │
Vy ─┤              │
    │              │
    └──[-]──[SQR]──┘
```

### 4. Time-Division Multiplier

Uses pulse-width modulation:
```
Vx controls duty cycle
Vy is gated by PWM
Low-pass filter extracts product
```

High accuracy but limited bandwidth.

## Commercial Multiplier ICs

### Available Devices

| Device | Manufacturer | Accuracy | Bandwidth | Notes |
|--------|--------------|----------|-----------|-------|
| AD534 | Analog Devices | 0.1% | 1 MHz | Precision, externally trimmed |
| AD633 | Analog Devices | 2% | 1 MHz | Low cost, 4-quadrant |
| AD734 | Analog Devices | 0.1% | 10 MHz | High speed |
| MPY634 | Texas Instruments | 0.5% | 10 MHz | Wide bandwidth |
| MLT04 | Analog Devices | 0.1% | 10 MHz | Quad multiplier |

### AD633 Application Circuit

```
         ┌────────────────────┐
         │                    │
   Vx ───┤ X1            OUT ├───┬── Vout = (X1-X2)(Y1-Y2)/10 + Z
         │              (+V) ├───│
   GND ──┤ X2                │   │
         │      AD633        │   │
   Vy ───┤ Y1            (-V)├───┘
         │                    │
   GND ──┤ Y2              Z ├─── GND (or offset)
         │                    │
         └────────────────────┘

Vout = Vx × Vy / 10V
```

For ±10V inputs: Vout ranges ±10V

## Dividers

### Division Using Multiplier in Feedback

A multiplier in the feedback loop of an op-amp performs division[^6]:

```
            ┌─────────────────────────┐
            │                         │
            │   ┌──────┐             │
            │   │      ├─────────────┘
            └───┤ MULT │
                │      ├──┐
    Vy ─────────┤      │  │
                └──────┘  │
                          │
    Vx ────/\/\/──────────┼────(-)──┐
            R             │         │
                          │   OP    ├── Vout = Vx/Vy × 10V
                          │         │
                     ┌────┴───(+)───┘
                     │
                     ▼
                    GND

Feedback forces: Vout × Vy / 10 = Vx
Therefore: Vout = 10 × Vx / Vy
```

**Limitations:**
- Vy must be same polarity (can't divide by zero or negative)
- Limited accuracy near Vy = 0
- Dynamic range limited

### Two-Quadrant Divider

For division where denominator is always positive:
```
Vout = Vx / Vy (Vy > 0)
```

### Ratio Function

```
Vout = Vx / Vy × Vref

When Vref = Vy: Vout = Vx (unity)
When Vref = 10V: Vout = 10 × Vx/Vy
```

## Squaring and Square Roots

### Squarer

Connect both inputs together:
```
Vin ──┬───[X1]──┐
      │         │
      └───[Y1]──┴── Vout = Vin² / 10V
```

### Square Root

Use squarer in feedback loop:
```
            ┌─────────────────────────┐
            │                         │
            │   ┌──────┐             │
            └───┤ MULT ├──┬──────────┘
                │      │  │
            ┌───┤      │  │
            │   └──────┘  │
            │             │
    Vin ────/\/\/─────────┴────(-)──┐
            R                       │
                              OP    ├── Vout = √(10 × Vin)
                                    │
                     ┌─────────(+)──┘
                     │
                     ▼
                    GND

Feedback: Vout² / 10 = Vin
Therefore: Vout = √(10 × Vin)
```

**Note:** Input must be positive (or use absolute value circuit).

## Applications in Analog Computing

### 1. Nonlinear Differential Equations

Van der Pol oscillator: x'' - μ(1 - x²)x' + x = 0

The x² term requires a multiplier:
```
x ──[MULT]── x²
```

### 2. Power Calculations

```
P = V × I

Voltage ──┬──[MULT]── Power
          │
Current ──┘
```

### 3. Trigonometric Functions

Using identities:
```
sin(2θ) = 2sin(θ)cos(θ)   [requires multiplier]
cos²(θ) = ½(1 + cos(2θ))  [requires squarer]
```

### 4. Coordinate Transformations

Polar to Cartesian:
```
x = r × cos(θ)
y = r × sin(θ)
```

### 5. RMS Computation

```
           ┌──[SQR]──[LPF]──[SQRT]── Vrms
Vin ───────┘
```

## Accuracy Considerations

### Error Sources

| Source | Typical Error | Notes |
|--------|---------------|-------|
| Scale factor | 0.1-2% | Can be trimmed |
| Offset | 1-50 mV | Temperature dependent |
| Nonlinearity | 0.1-1% | Inherent in technique |
| Feedthrough | 0.1-1% | X input at Y=0 |
| Temperature | 50-500 ppm/°C | Affects all parameters |

### Improving Accuracy

1. **External trimming**: Use precision resistors
2. **Offset nulling**: Add trim potentiometers
3. **Temperature compensation**: Use matched transistors
4. **Calibration**: Periodic adjustment

## Practical Considerations

### Bandwidth Limits

Multiplier bandwidth decreases with signal amplitude:
```
Small signal: Full bandwidth (1-10 MHz)
Full scale: Reduced bandwidth due to slew rate
```

### Power Supply

Most multipliers require bipolar supplies:
```
Typical: ±15V or ±12V
Power: 50-500 mW
```

### Layout

For high accuracy:
- Short lead lengths
- Ground plane
- Decoupling capacitors
- Avoid temperature gradients

## Summary Table

| Operation | Configuration | Notes |
|-----------|---------------|-------|
| Multiply | X × Y | Direct use |
| Square | X × X | Connect inputs together |
| Divide | X / Y | Multiplier in feedback |
| Square root | √X | Squarer in feedback |
| Power | X^n | Chain multipliers/log-antilog |

## References

[^1]: [Analog Multiplier - Wikipedia](https://en.wikipedia.org/wiki/Analog_multiplier)
[^2]: [Analog Devices MT-079: Analog Multipliers Tutorial](https://www.analog.com/media/en/training-seminars/tutorials/MT-079.pdf)
[^3]: [How to Multiply Currents: Inside a Counterfeit Analog Multiplier](http://www.righto.com/2020/09/how-to-multiply-currents-inside.html)
[^4]: [Analog Multipliers and Dividers in Linear ICs](https://www.origin-ic.com/blog/analog-multipliers-and-dividers-in-linear-ics/40732)
[^5]: [Alternative Computing Models: Electronic Analog Computing - Servo Magazine](https://www.servomagazine.com/magazine/article/alternative-computing-models-part-3-electronic-analog-computing)
[^6]: [Analog Mathematics - Nuts & Volts Magazine](https://www.nutsvolts.com/magazine/article/analog_mathematics)

## Further Reading

- [Function Generators](05-function-generators.md)
- [Nonlinear Equations](../03-mathematics/06-nonlinear-equations.md)
