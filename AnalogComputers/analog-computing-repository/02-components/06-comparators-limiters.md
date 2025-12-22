# Comparators and Limiters

## Overview

Comparators and limiters are essential for implementing conditional logic, bounds checking, and protection in analog computers. They bridge the gap between continuous analog signals and discrete decision-making.

## Comparators

### Basic Comparator Operation

A comparator outputs one of two voltage levels depending on which input is larger[^1]:

```
         ┌───────┐
V+ ──────┤+      │
         │ COMP  ├── Vout = { +Vsat if V+ > V-
V- ──────┤-      │            { -Vsat if V+ < V-
         └───────┘
```

### Op-Amp as Comparator

Any op-amp used open-loop acts as a comparator:

```
                ┌───────┐
Vin ────────────┤+      │
                │  OP   ├── Vout
Vref ───────────┤-      │
                └───────┘

Vout = +Vsat when Vin > Vref
Vout = -Vsat when Vin < Vref
```

**Transition Region:**
- Input difference for full swing: ΔV ≈ Vsat/Aol
- For 741 (Aol = 200,000): ΔV ≈ 50μV

### Dedicated Comparator ICs

| Device | Features | Propagation Delay |
|--------|----------|-------------------|
| LM311 | Open collector output | 200 ns |
| LM339 | Quad, open collector | 1.3 μs |
| MAX961 | High speed | 4.5 ns |
| LT1016 | Ultra-fast | 10 ns |
| TLV3501 | Rail-to-rail, low power | 4.5 ns |

### Zero-Crossing Detector

```
                ┌───────┐
Vin ────────────┤+      │
                │ COMP  ├── Vout
GND ────────────┤-      │
                └───────┘

Output changes state when Vin crosses zero
```

**Application:** Detecting zero crossings in oscillatory solutions.

### Window Comparator

Detects when signal is within a defined range:

```
                ┌───────┐
Vin ────────────┤+      │
                │ COMP1 ├───┐
V_high ─────────┤-      │   │
                └───────┘   │
                            ├── AND ── "In Window"
                ┌───────┐   │
V_low ──────────┤+      │   │
                │ COMP2 ├───┘
Vin ────────────┤-      │
                └───────┘

Output high when: V_low < Vin < V_high
```

## Schmitt Trigger (Comparator with Hysteresis)

### Purpose

Prevents oscillation at switching point when input has noise[^2].

### Circuit

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
              ├───────────┘
              │
             /\/\/ R2
              │
              ▼
             Vref
```

### Threshold Voltages

```
V_TH (positive-going) = Vref × (Rf/(R1+Rf)) + Vsat × (R1/(R1+Rf))
V_TL (negative-going) = Vref × (Rf/(R1+Rf)) - Vsat × (R1/(R1+Rf))

Hysteresis = V_TH - V_TL = 2 × Vsat × R1/(R1+Rf)
```

### Hysteresis Diagram

```
Vout
  │
  │   +Vsat ─────────────────────●←──
  │                              │
  │                              │
  │                        ──●   │
  │                       │  │   │
  └───────────────────────┼──┼───┼──── Vin
                V_TL     V_TH
                          │  │
  │                       ●──→   │
  │                              │
  │   -Vsat ─────●───────────────
  │              →
```

## Limiters (Clippers)

### Diode Limiters

**Basic Clipper:**
```
           D
Vin ───────►|──┬── Vout
               │
               │
              ─┴─ V_limit
```

When Vin > V_limit + 0.6V, diode conducts and limits output.

### Precision Limiter (Active Clipper)

Uses op-amp to eliminate diode drop error[^3]:

```
              Rf
         ┌────/\/\/────┐
         │      │      │
         │      │      │
         │     ─►|─────┤ D1
         │      │      │
         │     ─►|─────┤ D2
         │      │      │
         │      │      │
Vin ─────/\/\/──┴─────(-)──┐
          Rin              │
                     OP    ├── Vout
                           │
                ┌─────(+)──┘
                │
                ▼
               GND
```

### Symmetrical Limiter (Clipper)

Limits both positive and negative excursions:

```
                    R
Vin ────────/\/\/────┬── Vout
                     │
                    ─┴─
                     ▲ Z1 (Zener)
                     │
                     │
                    ─▼─
                     ▲ Z2 (Zener)
                     │
                    ─┴─
                    GND

Vout limited to ±(Vz + 0.6V)
```

### Soft Limiting

Gradual limiting rather than sharp cutoff:

```
Vout
  │
  │        ___________
  │      /
  │    /
  │  /
  │/
  ├────────────────── Vin
  │\
  │  \
  │    \
  │      \___________
  │
```

Implemented with multiple diode stages or transistor saturation.

## Dead Zone Circuit

Creates region of zero output around zero input:

```
Vout
  │
  │        /
  │       /
  │      /
  │     │  Dead zone
  ├─────┼─────────── Vin
  │     │
  │      \
  │       \
  │        \
  │
```

**Circuit:**
```
                D1        R
Vin ────────────►|────/\/\/──┐
                             │
                             ├── Vout
                             │
Vin ────────────►|────/\/\/──┘
                D2        R
        (biased for dead zone)
```

## Absolute Value Circuit

### Precision Full-Wave Rectifier

```
              R
         ┌────/\/\/────┐
         │      │      │
         │     D1      │
         │    ─►|──────┤
         │      │      │
         │    D2 │     │
         │    |◄─      │
         │      │      │
Vin ─────/\/\/──┴─────(-)──┐     R        R
          R                │    ┌─/\/\/───/\/\/──┐
                     OP1   ├────┤                 │
                           │    │          R     │
                ┌─────(+)──┘    │    ┌────/\/\/──┼──(-)──┐
                │               │    │           │       │
                ▼               │    │     OP2   │       ├── |Vin|
               GND          Vin─┴────┤           │       │
                                     │      ┌───(+)──────┘
                                     │      │
                                     │      ▼
                                     │     GND
                                     │
                                     R
                                     │
                                     ▼
                                    GND
```

## Applications in Analog Computing

### 1. Bouncing Ball Simulation

When ball hits floor (y = 0):
```
y ──[COMP: y < 0]── Control bounce
```

### 2. Coulomb Friction

Sign-dependent friction force:
```
v ──[SGN]──[×|F_friction|]── Friction force opposing motion
```

### 3. Relay Hysteresis

Simulating systems with on/off control:
```
Temperature ──[Schmitt Trigger]── Heater on/off
```

### 4. Protection Circuits

Prevent integrator saturation:
```
[Integrator output] ──[Limiter: ±9V]── Protected output
```

### 5. Peak Detection

```
           D
Vin ────────►|──┬── Vpeak
               │
              ═╪═ C (hold)
               │
               ▼
              GND
```

## Practical Considerations

### Comparator Speed

For fast comparisons in analog computing:
- Use dedicated comparators (not general-purpose op-amps)
- Consider propagation delay in timing
- Watch for metastability near threshold

### Noise Immunity

Without hysteresis, noise causes multiple transitions:
```
Vin with noise:  ∼∼∼∼∼∼∼∼∼∼  crossing threshold
Output:          ▄▀▄▀▄▀▄▀▄▀  chattering
```

Always use hysteresis when input may be noisy.

### Power Dissipation

During transitions, comparators may draw high current. Use decoupling:
```
+V ──┬── to comparator
     │
    ═╧═ 0.1μF
     │
    ─┴─ GND
```

## Summary Table

| Element | Function | Key Application |
|---------|----------|-----------------|
| Comparator | Two-level output | Threshold detection |
| Schmitt Trigger | Comparator + hysteresis | Noise immunity |
| Limiter | Bound output voltage | Saturation modeling |
| Dead Zone | Zero output near zero input | Backlash, deadband |
| Absolute Value | |Vin| | Magnitude extraction |
| Window Comparator | In-range detection | Bounds checking |

## References

[^1]: [Op-Amp Comparator - Electronics Tutorials](https://www.electronics-tutorials.ws/opamp/op-amp-comparator.html)
[^2]: [Schmitt Trigger - Wikipedia](https://en.wikipedia.org/wiki/Schmitt_trigger)
[^3]: [Precision Rectifier - Wikipedia](https://en.wikipedia.org/wiki/Precision_rectifier)

## Further Reading

- [Function Generators](05-function-generators.md)
- [Control Systems](../04-applications/01-control-systems.md)
