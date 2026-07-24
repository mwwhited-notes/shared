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

### Sigmoid, Tanh, and Neural Network Activation Functions

Generating classic neural-network activation functions (sigmoid, tanh, ReLU, ELU, leaky ReLU) in
analog hardware — relevant both as a modern application of analog computing (analog/neuromorphic
ANN inference) and as a good illustration of piecewise-linear/exponential function-generator
technique applied to a currently-popular function family[^6][^7].

**Key identity linking sigmoid and tanh:**
```
sigmoid(x) = 1/(1 + e⁻ˣ) = 1/2 + 1/2·tanh(x/2)
```
Any tanh-generating circuit becomes a sigmoid generator with a gain-of-½ scale and a +0.5 offset —
the two function families below are really one family.

**1. Anti-parallel diode clamp (simplest tanh approximation):**
```
        D1 (fwd)
Vin ──┬──►|──┬── Vout ≈ tanh-like, clamped near ±0.6V
      └──|◄──┘
        D2 (reversed)
```
Two diodes in anti-parallel clamp the output near 0V with an exponential "twist" as each diode's
knee is approached — a rough tanh shape. Scale to a useful range (e.g. ±1V) with a non-inverting
amplifier stage afterward. For control over the steepness of the central slope, move the diode
pair into the feedback loop of an inverting amplifier, with a resistor ahead of the diodes setting
the initial (undamped) gain before the diodes take over and compress the output — larger resistor
= steeper initial slope before compression kicks in. Scale/shift this tanh-like output (gain ≈
−0.9, offset to center at +0.5V) to approximate a sigmoid directly.

**2. Differential pair (Gilbert-style) — closest to a "native" tanh:**
A BJT differential pair's transfer function *is* a tanh of the differential input voltage (scaled
by VT) — this is the same underlying nonlinearity Barrie Gilbert exploited in the classic
"High-Accuracy Sine-Function Generator" (US Patent 4,475,169) to synthesize trig functions from
diff-pair transfer characteristics. Of the approaches here, this is the method most likely to give
a mathematically "true" tanh rather than a diode-clamp approximation, at the cost of needing
matched transistors and careful biasing (temperature-sensitive, like all transistor-exponential
techniques — see [Logarithmic Function Generators](#3-logarithmic-function-generators) above for
the same underlying issue).

**3. Direct analog-computer decomposition (exponential + log-antilog multiply + feedback divide):**
Build the function literally: an exponential converter for e⁻ˣ, a log-antilog multiplier (two more
exponentiators + an adder + a logger) to form the product term, then a multiplier-in-feedback loop
(see [Dividers](04-multipliers-dividers.md#dividers)) to turn the multiply into a divide, with the
"1 +" handled as a trivial offset. Mathematically the most direct path from the formula to a
circuit, but chains multiple temperature-sensitive exponential stages — compounds error at every
stage and is mostly of theoretical/educational interest rather than a practical build.

**4. Piecewise-linear approximation (cheapest, most practical for coarse accuracy):**
Sigmoid is nearly linear over roughly x ∈ [−0.7, +0.7]. A single-segment linear fit over x ∈ [0,1]:
```
y ≈ 0.25x + 0.5
```
| x | Actual sigmoid(x) | Linear approx | Error |
|---|---|---|---|
| 0.2 | 0.5498 | 0.550 | 0.03% |
| 0.3 | 0.5744 | 0.575 | ~0% |
| 0.5 | 0.6225 | 0.625 | 0.5% |
| 0.6 | 0.6457 | 0.650 | 0.67% |
| 0.7 | 0.6688 | 0.675 | 0.9% |
| 0.8 | 0.6900 | 0.690 | ~0% |
| 1.0 | 0.7311 | 0.750 | 2.6% (max) |

Easiest to implement with a single op-amp gain/offset stage — the hardest part in practice is
generating an accurate 0.5V offset, since it affects overall accuracy directly. For a closer fit
across a wider range, extend to the general [multi-segment diode function generator](#design-procedure-for-diode-function-generators)
technique above rather than a single linear segment.

**5. Multi-segment PWL via DAC array (highest precision, borrowed from LCD gamma correction):**
LCD column drivers have used exactly this problem — mapping an input through an arbitrary smooth
curve — for gamma correction for decades: an array of DACs implements a many-segment
piecewise-linear approximation to whatever transfer curve is needed. The same technique maps
directly onto tanh/sigmoid/ReLU generation and is the most precision-tunable of the approaches
here, at the cost of needing multiple DACs instead of a single diode/transistor stage.

**Important limitation for actual analog neural networks (not just single-function generation):**
Any of the above will produce *a* nonlinearity, and the universal approximation theorem only
requires *some* nonlinearity for a multi-layer network to gain expressive depth over a single
linear stage. But generating the forward function is the easy part — training an analog ANN via
backpropagation also requires computing the activation function's *derivative* in hardware and
using it to update multiplier weights on the fly. None of the circuits above address that; they
only solve feedforward inference. A circuit trained in software with a mathematically pure sigmoid
and then implemented with one of these imperfect analog approximations will also pick up bias from
the mismatch between the trained (pure) and deployed (approximate/asymmetric) activation function.

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
[^6]: [Sigmoid using op-amps - Electronics StackExchange](https://electronics.stackexchange.com/questions/639130/sigmoid-using-op-amps)
[^7]: [What are the activation functions that can be generated using op-amps and filters? - Electronics StackExchange](https://electronics.stackexchange.com/questions/657902/what-are-the-activation-functions-that-can-be-generated-using-op-amps-and-filter)
[^8]: [A method of generating a signal proportional to... (Gilbert) - Semantic Scholar](https://www.semanticscholar.org/paper/A-method-of-generating-a-signal-proportional-to-the-Gilbert/9bd413c5f451fd7c7cbc00bb3774154756057c98) - content could not be retrieved during research (page returned empty on repeated fetch attempts); URL slug suggests a Barrie Gilbert paper closely related to the differential-pair/translinear technique cited above — worth opening directly to confirm before citing further

## Further Reading

- [Comparators and Limiters](06-comparators-limiters.md)
- [Nonlinear Equations](../03-mathematics/06-nonlinear-equations.md)
- [Chaos and Attractors](../07-tutorials/05-chaos-attractors.md)
