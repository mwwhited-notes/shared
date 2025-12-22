# Function Generators

## Overview

Function generators in analog computers produce nonlinear relationships between input and output voltages. They implement arbitrary mathematical functions that cannot be achieved with linear elements alone.

## Types of Function Generators

### 1. Diode Function Generators (DFG)

The most common type uses piecewise-linear approximation with diodes and resistors[^1]:

```
Vout
  │
  │         /
  │        /.
  │       / .
  │      /  .
  │     /.  .
  │    / .  .
  │   /  .  .
  │  /.  .  .
  │ / .  .  .
  │/  .  .  .
  └────────────── Vin
    Breakpoints
```

**Basic Segment Circuit:**
```
           D
Vin ───/\/\/───►|────┐
        R            │
                     ├── Contributes to Vout
    Vbreak ──────────┘
```

When Vin exceeds Vbreak, diode conducts and adds a slope change.

### 2. Operational Amplifier Function Generator

Multiple diode-resistor networks with op-amp:

```
             Rf
        ┌────/\/\/────┐
        │             │
        │  D1   R1    │
        ├──►|──/\/\/──┤
        │             │
        │  D2   R2    │
Vin ────┼──►|──/\/\/──┼────(-)──┐
        │             │         │
        │  D3   R3    │   OP    ├── Vout
        ├──►|──/\/\/──┤         │
        │             │         │
        └─────/\/\/───┤    ┌───(+)
               Rin    │    │
                      │    ▼
                      │   GND
                      │
             (bias network for breakpoints)
```

### 3. Logarithmic Function Generators

Use transistor log characteristics[^2]:

```
For y = log(x):
              ┌─────────────────┐
              │      Q1         │
Vin ─────────(-)─┬───┤├─────────┤
                 │    │         │
                 │   ─┴─        │
                 │    ▲         │
                 │    │         │
                 │    │   OP    ├── Vout ≈ log(Vin)
                 │    │         │
                 │    ├────(+)──┘
                 │    │
                 ▼    ▼
                GND  GND
```

### 4. Polynomial Function Generators

Using multipliers to create powers[^3]:

```
For y = ax² + bx + c:

x ──┬─────────────────────[pot:b]──┐
    │                              │
    │   ┌──────┐                   │
    └───┤      ├───[pot:a]─────────┼───[SUM]── y
        │ MULT │                   │
    ┌───┤      │                   │
    │   └──────┘                   │
    │                              │
x ──┘        c ────────────────────┘
```

### 5. Servo-Driven Function Generators

For high-precision arbitrary functions:
- Input voltage drives servo motor
- Motor rotates function cam or potentiometer
- Shaped cam produces arbitrary function
- Used in historical computers for complex functions

## Implementing Common Functions

### Absolute Value

```
        D1
Vin ────►|────┐
              │
    ────►|────┤
        D2    │
              ├── |Vin|
        R     │
Vin ──/\/\/───┘
```

Or with op-amp precision rectifier:
```
              D1
         ┌────►|────┐
         │         │
Vin ─────┤────(-)──┤
         │         │
         │   OP    ├── Vout
         │         │
         ├────(+)──┘
         │    │
         │    ▼
         │   GND
         │
         └────►|────┐
              D2    │
                    ▼
                   GND
```

### Sign Function (Signum)

```
            Vsat
              │
              ▼
Vin ──[COMP]──┬── Vout = +Vref (Vin > 0)
              │         -Vref (Vin < 0)
              ▼
           -Vsat
```

### Limiting (Saturation)

```
Vout
  │
  │    ┌────── +Vmax
  │   /│
  │  / │
  │ /  │
  │/   │
  ├────┼────── Vin
  │    │
  │    │
  │    └────── -Vmax
  │
```

**Circuit with Zener diodes:**
```
              Rf
         ┌────/\/\/────┐
         │      │      │
         │     ─┴─     │
         │      ▲ Z1   │
         │      │      │
         │      │      │
         │     ─┴─     │
         │      ▲ Z2   │
         │      │      │
Vin ─────/\/\/──┴─────(-)──┐
          Rin              │
                     OP    ├── Vout (limited)
                           │
                ┌─────(+)──┘
                │
                ▼
               GND
```

### Dead Zone

```
Vout
  │
  │        /
  │       /
  │      /
  ├──────┼────── Vin
  │      │
  │       \
  │        \
  │
   ←─────→
   Dead zone
```

### Hysteresis (Schmitt Trigger)

```
              Rf
         ┌────/\/\/────┐
         │             │
Vin ─────┴────────(-)──┐
                       │
                 OP    ├──┬── Vout
                       │  │
              ┌───(+)──┘  │
              │           │
             /\/\/ R1     │
              │           │
              └───────────┘
```

Hysteresis width = 2 × Vsat × R1/(R1 + Rf)

### Sine/Cosine Functions

**Method 1: Function Generator with Many Segments**
```
Approximate sine with 8-16 linear segments
Accuracy: 0.1-1% typical
```

**Method 2: Polynomial Approximation**
```
sin(x) ≈ x - x³/6 + x⁵/120 - ...

Requires multipliers for powers
```

**Method 3: Feedback Oscillator**
```
x'' + ω²x = 0 generates sine/cosine

       ┌─────────────────────────────┐
       │                             │
       ↓                             │
    [INT] ─── x' ─── [INT] ─── x ────┤
       ↑                             │
       │                             │
       └──[-ω²]◄─────────────────────┘

Outputs: x = A·sin(ωt), x' = Aω·cos(ωt)
```

### Exponential and Logarithm

Using transistor characteristics[^4]:

**Exponential:**
```
         ┌─────────────────┐
         │      Q1         │
         │      ┤├─────────┤
   Vin ──┤──────│          │
         │     ─┴─         │
         │      │    OP    ├── Vout ≈ exp(Vin)
         │      │          │
         │      ├─────(+)──┘
         │      │
         ▼      ▼
        GND    GND
```

**Logarithm:**
(Interchange transistor and resistor positions)

## Design Procedure for Diode Function Generators

### Step 1: Determine Breakpoints

For function f(x), choose breakpoints where slope changes significantly:
```
x₁, x₂, x₃, ... xₙ
f(x₁), f(x₂), f(x₃), ... f(xₙ)
```

### Step 2: Calculate Slopes

For each segment i:
```
mᵢ = [f(xᵢ₊₁) - f(xᵢ)] / [xᵢ₊₁ - xᵢ]
```

### Step 3: Determine Slope Changes

```
Δmᵢ = mᵢ - mᵢ₋₁
```

### Step 4: Calculate Resistor Values

For feedback resistor Rf:
```
Rᵢ = Rf / |Δmᵢ|
```

### Step 5: Set Breakpoint Voltages

Use voltage dividers from reference to set each breakpoint.

### Example: Approximating x²

For x from 0 to 1 (scaled):

| Segment | x range | Slope | Resistor |
|---------|---------|-------|----------|
| 0 | 0.0-0.2 | 0.2 | 50kΩ |
| 1 | 0.2-0.4 | 0.6 | 25kΩ |
| 2 | 0.4-0.6 | 1.0 | 25kΩ |
| 3 | 0.6-0.8 | 1.4 | 25kΩ |
| 4 | 0.8-1.0 | 1.8 | 25kΩ |

## Inverse Function Generation

To generate f⁻¹(x), place function generator in feedback loop[^5]:

```
            ┌─────────────────┐
            │                 │
            │   ┌────────┐    │
            └───┤  f(x)  ├────┘
                └────────┘
                    │
Vin ─────/\/\/──────┴────(-)──┐
          R                   │
                        OP    ├── Vout = f⁻¹(Vin)
                              │
                   ┌─────(+)──┘
                   │
                   ▼
                  GND

Feedback forces: f(Vout) = Vin
Therefore: Vout = f⁻¹(Vin)
```

## Accuracy and Limitations

### Sources of Error

| Source | Typical Error | Mitigation |
|--------|---------------|------------|
| Diode forward drop | 0.6V | Use precision rectifiers |
| Temperature variation | 2mV/°C | Temperature compensation |
| Resistor tolerance | 0.1-1% | Use precision resistors |
| Breakpoint accuracy | 0.5-2% | Trim potentiometers |
| Slope matching | 0.5-1% | Matched resistors |

### Typical Accuracy

- Simple functions: 0.5-2%
- Complex functions: 1-5%
- With trimming: 0.1-0.5%

## Modern Alternatives

### Digital Function Generation

```
Vin ──[ADC]──[Lookup Table]──[DAC]── Vout

Advantages:
- Any function
- Perfect accuracy
- Easily modified
- Temperature stable

Disadvantages:
- ADC/DAC delay
- Power consumption
- Cost
```

### Hybrid Approaches

Combine analog computing with digital function lookup for complex or arbitrary functions.

## References

[^1]: [Analog Computer - Wikipedia: Function Generators](https://en.wikipedia.org/wiki/Analog_computer)
[^2]: [Logarithms for Analog Circuits - All About Circuits](https://www.allaboutcircuits.com/worksheets/logarithms-for-analog-circuits/)
[^3]: [Analog Mathematics - Nuts & Volts Magazine](https://www.nutsvolts.com/magazine/article/analog_mathematics)
[^4]: [Op-Amp Applications Handbook - Analog Devices](https://www.analog.com/media/en/training-seminars/design-handbooks/Op-Amp-Applications/Op-Amp-Applications-Handbook.pdf)
[^5]: [Engineering LibreTexts - Analog Computer](https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Operational_Amplifiers_and_Linear_Integrated_Circuits_-_Theory_and_Application_(Fiore)/10:_Integrators_and_Differentiators/10.04:_Section_4-)

## Further Reading

- [Comparators and Limiters](06-comparators-limiters.md)
- [Nonlinear Equations](../03-mathematics/06-nonlinear-equations.md)
- [Chaos and Attractors](../07-tutorials/05-chaos-attractors.md)
