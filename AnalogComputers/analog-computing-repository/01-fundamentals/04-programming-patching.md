# Programming and Patching Techniques

## Overview

"Programming" an analog computer means configuring the interconnections between computing elements to implement a specific mathematical model. Unlike digital programming with code, analog programming involves physical patch cords and coefficient settings.

## The Analog Programming Process

### Step-by-Step Workflow

```
1. Mathematical Model
        ↓
2. Normalize Equations
        ↓
3. Rearrange for Highest Derivative
        ↓
4. Draw Block Diagram
        ↓
5. Apply Scaling
        ↓
6. Create Patch Diagram
        ↓
7. Wire the Computer
        ↓
8. Set Coefficients
        ↓
9. Set Initial Conditions
        ↓
10. Run and Observe
```

## The Kelvin Feedback Technique

The Kelvin (or Lord Kelvin) technique is the standard method for translating differential equations into analog circuits.

### Basic Principle

1. Isolate the highest-order derivative on one side
2. Generate this derivative using summers
3. Use integrators to obtain lower-order derivatives
4. Feed back the integrated signals with appropriate coefficients

### Example: Second-Order ODE

Given:
```
m·(d²x/dt²) + b·(dx/dt) + k·x = F(t)
```

**Step 1: Isolate highest derivative**
```
d²x/dt² = (1/m)[F(t) - b·(dx/dt) - k·x]
```

**Step 2: Assume we have d²x/dt², then integrate**
```
d²x/dt² → ∫ → dx/dt → ∫ → x
```

**Step 3: Feed back with coefficients**
```
                    ┌────────────────────────────────────┐
                    │                                    │
F(t) ─────┬────────(Σ)─────[∫]─────┬────[∫]─────┬──── x
          │         │              │            │
          │    ┌────┘              │            │
          │    │                   │            │
          │   [-b/m]◄──────────────┘            │
          │                                     │
          └──[-k/m]◄────────────────────────────┘
```

## Patch Diagram Conventions

### Standard Symbols

| Symbol            | Element       | Function       |
|-------------------|---------------|----------------|
| Triangle          | Op-amp        | Amplification  |
| ∫                 | Integrator    | Integration    |
| Σ                 | Summer        | Addition       |
| -1                | Inverter      | Sign change    |
| Circle with arrow | Potentiometer | Coefficient    |
| ×                 | Multiplier    | Multiplication |

### Typical Patch Panel Layout

```
┌─────────────────────────────────────────────────────┐
│  PATCH PANEL                                        │
│                                                     │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐    │
│  │ INT │ │ INT │ │ INT │ │ INT │ │ INT │ │ INT │    │
│  │  1  │ │  2  │ │  3  │ │  4  │ │  5  │ │  6  │    │
│  └──●──┘ └──●──┘ └──●──┘ └──●──┘ └──●──┘ └──●──┘    │
│     │       │       │       │       │       │       │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐    │
│  │ SUM │ │ SUM │ │ SUM │ │ SUM │ │ INV │ │ INV │    │
│  │  1  │ │  2  │ │  3  │ │  4  │ │  1  │ │  2  │    │
│  └──●──┘ └──●──┘ └──●──┘ └──●──┘ └──●──┘ └──●──┘    │
│     │       │       │       │       │       │       │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐    │
│  │ POT │ │ POT │ │ POT │ │ POT │ │ POT │ │ POT │    │
│  │  1  │ │  2  │ │  3  │ │  4  │ │  5  │ │  6  │    │
│  └──●──┘ └──●──┘ └──●──┘ └──●──┘ └──●──┘ └──●──┘    │
│                                                     │
│  [REF+] [REF-] [GND] [IC] [OP] [HALT] [RESET]       │
└─────────────────────────────────────────────────────┘
```

## Operating Modes

### Mode Switch States

| Mode | Description | Integrators | Time |
|------|-------------|-------------|------|
| **RESET (IC)** | Initial Condition | Hold at IC value | Stopped |
| **OPERATE (OP)** | Compute | Integrating | Running |
| **HALT** | Pause | Hold current value | Stopped |

### Typical Timing Sequence

```
Time →
        ┌──────┐         ┌──────┐
RESET ──┘      └─────────┘      └─────
              ┌─────────┐
OPERATE ──────┘         └─────────────
                        ┌─────┐
HALT    ────────────────┘     └───────

        [Set IC] [Compute] [Hold] [Read]
```

## Initial Conditions

### Setting IC on Integrators

Initial conditions are applied to integrator capacitors:

```
                           IC Voltage
                               │
                               ▼
                            ┌──┴──┐
                        ────┤ SW  │
                            └──┬──┘
                               │      C
                      ┌────────┼────||────┐
                      │        │          │
Vin ────/\/\─┬────────────(-)────┤      │
         R   │                   │ OP   ├── Vout
             │    ┌─────────(+)──┤      │
             │    │              └──────┘
             ▼    ▼
            GND  GND
```

When in RESET mode:
- Switch connects IC voltage to capacitor
- Integrator output = -IC (inverted)

### IC Setting Methods

1. **Reference Voltage Divider**: Use precision potentiometer from reference
2. **DAC**: Digital-to-analog converter for programmable IC
3. **Track-Store**: Sample from another computation

## Coefficient Setting

### Precision Potentiometers

Ten-turn precision potentiometers provide coefficient multiplication:

```
Vref (+10V) ───┬───
               │
              ┌┴┐
              │ │ k (0.000 to 1.000)
              │ │
              └┬┘
               │
           Vout = k × Vref
```

### Potentiometer Types

| Type | Turns | Resolution | Linearity |
|------|-------|------------|-----------|
| Single-turn | 1 | ~5% | 1-5% |
| 3-turn | 3 | ~1% | 0.5% |
| 10-turn | 10 | ~0.1% | 0.1% |
| Digital pot | N/A | 8-12 bit | 0.1% |

### Coefficient Accuracy

For accurate coefficient setting:
1. Use 10-turn pots with dial counters
2. Calibrate against known reference
3. Use DVM to verify output voltage
4. Account for loading effects

## Common Patching Patterns

### Generating a Constant

```
+REF ───[pot: k]───[INV]─── -k × REF
```

### Negating a Signal

```
Signal ───[INV]─── -Signal
```

### Weighted Sum

```
V1 ───[pot: a]───┐
                 ├───[SUM]─── -(aV1 + bV2 + cV3)
V2 ───[pot: b]───┤
                 │
V3 ───[pot: c]───┘
```

### Time Scaling

To speed up or slow down time:
```
τ = RC (integrator time constant)

Slow down: Increase R or C
Speed up: Decrease R or C
```

Common time scales:
- 1:1 (real time)
- 1:10 (10× slower)
- 10:1 (10× faster)
- 1000:1 (for very fast phenomena)

## Check-Out Procedures

### Before Running

1. **Visual Inspection**: Check all patch connections
2. **Static Check**: Verify potentiometer settings
3. **IC Check**: Confirm initial conditions
4. **Reference Check**: Verify reference voltages
5. **Mode Test**: Cycle through RESET-OP-HALT

### During Running

1. Monitor key signals on oscilloscope
2. Watch for overloads (limiting)
3. Check for oscillation or instability
4. Verify expected behavior

### Common Problems

| Symptom          | Possible Cause                      |
|------------------|-------------------------------------|
| Output saturated | Scaling error, wrong sign           |
| Oscillation      | Unintended feedback, layout issue   |
| Drift            | Op-amp offset, temperature          |
| Wrong answer     | Patching error, wrong coefficient   |
| No output        | Missing connection, power issue     |

## Documentation Practices

### Patch Sheet Format

```
PROJECT: Mass-Spring-Damper
DATE: 2024-12-22
AUTHOR: [Name]

EQUATIONS:
m·x'' + b·x' + k·x = F(t)
m = 1, b = 0.5, k = 4, F(t) = step

SCALING:
[x] = 5 units, [x'] = 10 units/sec
Time scale: 1:1

COEFFICIENTS:
P1: 0.500 (b/m)
P2: 4.000 (k/m)
P3: 1.000 (F/m)

INITIAL CONDITIONS:
INT1 (x'): 0.000
INT2 (x): 1.000 (initial displacement)

CONNECTIONS:
SUM1 input 1 → P3 (F)
SUM1 input 2 → INV1 output
SUM1 output → INT1 input
INT1 output → P1, INT2 input
INT2 output → P2
P1 output → SUM1 input 3
P2 output → INV1 input

OUTPUTS:
Scope Ch1: INT2 output (x)
Scope Ch2: INT1 output (x')
```

## Tips for Efficient Patching

1. **Plan before patching**: Draw complete diagram first
2. **Use short cables**: Minimize noise pickup
3. **Color code**: Different colors for different signals
4. **Label everything**: Attach tags to patch cords
5. **Start simple**: Test each section before adding more
6. **Document as you go**: Update patch sheet immediately
7. **Save working setups**: Take photos of successful patches

## References

[^1]: [Analog Computer Programming - Wikipedia](https://en.wikipedia.org/wiki/Analog_computer#Programming)
[^2]: Korn, Granino A. and Korn, Theresa M. *Electronic Analog and Hybrid Computers*. McGraw-Hill, 1972.
[^3]: [Patching Analog Computers - anabrid wiki](https://the-analog-thing.org/wiki/)
[^4]: [Kelvin Feedback - Engineering Electromagnetics](https://www.analog.com/en/technical-articles/understand-kelvin-connections.html)

## Further Reading

- [Scaling and Normalization](05-scaling.md)
- [Solving ODEs](../03-mathematics/03-ode-solving.md)
- [Tutorial: Solving a Simple ODE](../07-tutorials/02-simple-ode.md)
