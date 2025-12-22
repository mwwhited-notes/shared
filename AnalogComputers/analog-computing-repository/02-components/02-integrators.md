# Integrators

## Overview

The integrator is the most important computing element in an analog computer. It performs mathematical integration, which is essential for solving differential equations—the primary application of analog computers.

## The Miller Integrator

### Basic Circuit

```
              C
         ┌────||────┐
         │          │
         │    Rf    │ (optional, for DC stability)
         ├───/\/\/──┤
         │          │
Vin ─────/\/\/─────(-)──┐
          R             │
                  OP    ├── Vout
                        │
             ┌─────(+)──┘
             │
             ▼
            GND
```

### Transfer Function

**Time Domain:**
```
Vout(t) = -(1/RC) ∫ Vin(t) dt + Vout(0)
```

**Frequency Domain (Laplace):**
```
Vout(s)/Vin(s) = -1/(sRC)
```

**Frequency Domain (jω):**
```
H(jω) = -1/(jωRC) = 1/(ωRC) ∠ +90°
```

### Time Constant

The integrator time constant τ determines the integration rate:
```
τ = RC

Vout = -(1/τ) ∫ Vin dt
```

| R | C | τ | Integration Speed |
|---|---|---|-------------------|
| 100kΩ | 1μF | 0.1s | Fast |
| 1MΩ | 1μF | 1s | Standard |
| 1MΩ | 10μF | 10s | Slow |

## Circuit Analysis

### Using Virtual Ground Principle

```
At inverting input: V(-) = 0 (virtual ground)

Current through R: I = Vin/R

This current charges C: I = -C × dVout/dt

Therefore: Vin/R = -C × dVout/dt

Solving: Vout = -(1/RC) ∫ Vin dt
```

### Response to Constant Input

For Vin = V0 (constant):
```
Vout(t) = -(V0/RC) × t + Vout(0)
```

This is a **ramp** with slope = -V0/RC

```
Vout
 │
 │  Vout(0)
 ├────○
 │     ╲
 │      ╲  slope = -V0/RC
 │       ╲
 │        ╲
 │         ╲
 └──────────────── t
```

### Response to Step Input

For step from 0 to V0 at t=0:
```
Vout(t) = -(V0/RC) × t

Rate: 10V input with RC=1s gives -10V/s output slope
```

## Initial Conditions

### Setting Initial Conditions

The integrator must be initialized before computation:

```
              C
         ┌────||────┐
         │          │
         │    SW1   │ ← Reset switch
         ├────○─────┤
         │    │     │
         │   Vic    │ ← IC voltage source
         │          │
Vin ─────/\/\/─────(-)──┐
          R             │
                  OP    ├── Vout
                        │
             ┌─────(+)──┘
             │
             ▼
            GND
```

**Operation Modes:**

| Mode | SW1 | Action |
|------|-----|--------|
| IC (Reset) | Closed | Vout = -Vic |
| Operate | Open | Normal integration |
| Hold | Open | Holds current value |

### Electronic Mode Switching

```
                    C
               ┌────||────┐
               │          │
               │   S1a    │
    Vic ───────┼───○      │
               │   │      │
               │   S1b    │
               ├────○─────┤
               │          │
    Vin ───────/\/\/─────(-)──┐
                R             │
                        OP    ├── Vout
                              │
                   ┌─────(+)──┘
                   │
                   ▼
                  GND

Mode Control:
- IC: S1a closed, S1b open → Vout = -Vic
- OP: S1a open, S1b closed → Integrating
- HOLD: Both open → Output frozen
```

### FET Switch Implementation

```
              C
         ┌────||────┐
         │          │
         │    │     │
    Vic ─┤◁───┤ Q1  │  ← JFET or MOSFET
         │    │     │
         │    │     │
         ├────┤     │
         │    │     │
Vin ─────/\/\/─┤◁───┤ Q2
          R   │     │
              │     │
             (-)────┤
                    │
              OP    ├── Vout
                    │
         ┌─────(+)──┘
         │
         ▼
        GND
```

## Summing Integrator

Multiple inputs can be integrated simultaneously:

```
              C
         ┌────||────┐
         │          │
V1 ──────/\/\/──┬──(-)──┐
          R1    │       │
                │ OP    ├── Vout
V2 ──────/\/\/──┤       │
          R2    │       │
                │       │
V3 ──────/\/\/──┘  ┌───(+)─┘
          R3       │
                   ▼
                  GND
```

**Transfer Function:**
```
Vout = -(1/C) ∫ (V1/R1 + V2/R2 + V3/R3) dt
```

For equal resistors R:
```
Vout = -(1/RC) ∫ (V1 + V2 + V3) dt
```

## Practical Considerations

### Capacitor Selection

| Type | Advantages | Disadvantages | Use For |
|------|------------|---------------|---------|
| Polypropylene | Low leakage, stable | Large size | Precision |
| Polystyrene | Very low DA | Temperature sensitive | Precision |
| Ceramic (NP0) | Small, cheap | Limited values | General |
| Electrolytic | High values | Leakage, polarized | Long time constants |
| Teflon | Excellent stability | Expensive | Highest precision |

**DA = Dielectric Absorption**: Causes "memory" effect

### Dealing with Drift

Real integrators drift due to:
1. Op-amp input offset voltage
2. Input bias current
3. Capacitor leakage

**Solutions:**

1. **Parallel Resistor** (limits DC gain):
```
              C
         ┌────||────┐
         │          │
         │    Rf    │  Rf >> R (typically 100× to 1000×)
         ├───/\/\/──┤
         │          │
Vin ─────/\/\/─────(-)──
          R
```

2. **Chopper-Stabilized Op-Amp**
3. **Periodic Reset**
4. **Sample-and-Hold Output**

### Frequency Response

**Ideal Integrator:**
```
|H(jω)| = 1/(ωRC)
Phase = +90°
```

**With Parallel Resistor Rf:**
```
Low frequency: Gain limited to Rf/R
High frequency: Normal integration
Corner frequency: fc = 1/(2πRfC)
```

```
Gain
(dB)
  │
  │────────────○
  │            │╲
  │            │ ╲ -20dB/decade
  │            │  ╲
  │            │   ╲
  └────────────┼────╲───── f
              fc
```

### Output Limiting

Prevent capacitor overcharge with diode limiters:

```
              C
         ┌────||────┬────┐
         │          │    │
         │         ─┴─   │
         │          ▲ D1 │
         │          │    │
         │    ┌─────┼────┤
         │    │     │    │
         │    │    ─┴─   │
         │    │     ▲ D2 │
         │    │     │    │
         │    │     │    │
    ─────/\/\/┴────(-)───┤
          R              │
                   OP    ├── Vout
                         │
              ┌─────(+)──┘
              │
              ▼
             GND
```

## Track Mode (for Initial Conditions)

**Track Mode**: Integrator follows input (like amplifier)
**Hold Mode**: Integrator holds value
**Integrate Mode**: Normal integration

```
Track: Connect output to IC input through resistor
       Vout follows Vic × (Rf/Rin)
```

## Multi-Rate Integration

For problems with multiple time scales:

**Method 1: Different RC values**
```
Fast integrator: τ = 0.01s
Slow integrator: τ = 1s
```

**Method 2: Time scaling**
```
Run slow subsystem faster
Run fast subsystem slower
```

## Integrator Specifications (Typical)

| Parameter | Value |
|-----------|-------|
| Time constant | 0.1s, 1s, 10s (selectable) |
| Input resistance | 100kΩ |
| Number of inputs | 4-8 |
| IC range | ±10V |
| Drift rate | < 1mV/s |
| Accuracy | 0.01% |
| Output range | ±10V |

## Common Applications

### Velocity from Acceleration

```
a(t) ──[INT]── v(t) = ∫a dt + v₀
```

### Position from Velocity

```
v(t) ──[INT]── x(t) = ∫v dt + x₀
```

### Charge from Current

```
i(t) ──[INT]── q(t) = ∫i dt + q₀
```

### Low-Pass Filter

An integrator with feedback creates a first-order low-pass:
```
              C
         ┌────||────┐
         │          │
         │    Rf    │
         ├───/\/\/──┤
         │          │
Vin ─────/\/\/─────(-)── Vout (low-pass filtered)
          R

Cutoff: fc = 1/(2πRfC)
```

## Testing an Integrator

### Step Response Test

1. Apply constant voltage (e.g., +1V)
2. Observe linear ramp at output
3. Measure slope = -Vin/(RC)
4. Verify time constant

### Triangle Wave Test

1. Apply square wave input
2. Observe triangle wave output
3. Slope should be consistent
4. Peaks should not saturate

### Drift Test

1. Set IC to 0V
2. Ground all inputs
3. Switch to OPERATE
4. Monitor output over time
5. Drift should be < 1mV/s

## Summary

| Parameter | Formula | Notes |
|-----------|---------|-------|
| Time constant | τ = RC | Larger = slower integration |
| Output (DC input) | -Vin×t/τ | Ramp |
| Initial condition | Vout(0) = -Vic | Inverted |
| Summing | Σ(Vi/Ri)/C | Weighted integration |

## Further Reading

- [Differentiators](03-differentiators.md)
- [Solving ODEs](../03-mathematics/03-ode-solving.md)
- [Scaling](../01-fundamentals/05-scaling.md)
