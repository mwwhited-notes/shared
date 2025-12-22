# Mass-Spring-Damper Simulation

## Overview

The mass-spring-damper system is the classic second-order ODE that demonstrates oscillation, damping, and transient response. This tutorial shows how to implement it on an analog computer.

## The Physical System

```
    Fixed wall
        ║
        ║
        ╠═══╗ Spring (k)
        ║   ║
        ║   ╠═══════╗
        ║   ║       ║
        ║   ║   ┌───╨───┐
        ║   ║   │       │
        ╠═══╝   │   m   │──── x (displacement)
        ║       │       │
        ║  ┌────┴───────┤
        ║  │ Damper (b) │
        ╠══╧════════════╝
        ║
       ─┴─ (ground)
```

## The Equation

### Newton's Second Law

```
m·(d²x/dt²) = -k·x - b·(dx/dt) + F(t)
```

Where:
- m = mass (kg)
- k = spring constant (N/m)
- b = damping coefficient (N·s/m)
- x = displacement (m)
- F(t) = external force (N)

### Standard Form

```
d²x/dt² + (b/m)·(dx/dt) + (k/m)·x = F(t)/m
```

Define:
- ωₙ = √(k/m) = natural frequency
- ζ = b/(2√(km)) = damping ratio

Then:
```
d²x/dt² + 2ζωₙ·(dx/dt) + ωₙ²·x = F(t)/m
```

## System Behavior

### Damping Cases

| Damping Ratio | Behavior | Physical Meaning |
|---------------|----------|------------------|
| ζ = 0 | Undamped | Perpetual oscillation |
| 0 < ζ < 1 | Underdamped | Decaying oscillation |
| ζ = 1 | Critically damped | Fastest non-oscillatory |
| ζ > 1 | Overdamped | Slow exponential decay |

### Natural Frequency

Undamped oscillation frequency: fₙ = ωₙ/(2π) Hz

Damped oscillation frequency: ωd = ωₙ√(1-ζ²)

## Analog Implementation

### Block Diagram

```
           ┌──────────────────────────────────────────────┐
           │                                              │
           │     ┌────────────────────────────────────────┼───┐
           │     │                                        │   │
F(t) ──────┼─────┤                                        │   │
   /m      │     │                                        │   │
           │     ↓                                        │   │
      ┌────┴───[SUM]─────[INT]──────[INT]─────┬─── x     │   │
      │          ↑          │          │      │           │   │
      │          │         x'          │      │           │   │
      │          │          │          │      │           │   │
      │          │          │          └──────┘           │   │
      │          │          │                             │   │
      │    ┌─────┴──────────┼─────────────────────────────┘   │
      │    │                │                                 │
      │   [-ωₙ²]           [-2ζωₙ]                            │
      │    │                │                                 │
      └────┴────────────────┴─────────────────────────────────┘
```

### Detailed Circuit

```
                 C₁                     C₂
            ┌────||────┐           ┌────||────┐
            │          │           │          │
F/m ────────┤          │           │          │
    R_F     │    OP1   │     R₃    │    OP2   │
    ────/\/\/┤         ├───/\/\/───┤          ├───┬─── x
            │          │           │          │   │
x' ─────────┼───(-)────┤           │          │   │
    R_b     │          │      ┌───(-)─────────┤   │
    ────/\/\/┤         │      │               │   │
            │          │      │          ┌───(+)──┘
x ──────────┤          │      │          │
    R_k     │     ┌───(+)     │         ─┴─ GND
    ────/\/\/┘    │           │
                 ─┴─ GND      │
                              │
              ┌───────────────┘
              │
       (x fed back through R_k)
```

## Component Selection

### Example Parameters

Choose physical values:
- m = 1 kg
- k = 100 N/m (ωₙ = 10 rad/s, fₙ = 1.59 Hz)
- b = 4 N·s/m (ζ = 0.2, underdamped)

### Coefficient Calculation

```
ωₙ² = k/m = 100
2ζωₙ = b/m = 4
```

### Scaling for ±10V Operation

Assume maximum displacement x_max = 0.1 m
Scale factor: [x] = 10V / 0.1m = 100 V/m

Machine variables:
- X = 100·x (in volts)
- X' = 100·x' = 100·(dx/dt)

### Time Constant Selection

For τ = 0.01s (fast for visualization):
- R = 100kΩ
- C = 100nF
- Time scale factor: β = 100 (runs 100× faster)

Adjusted coefficients:
- ωₙ²/β² = 100/10000 = 0.01 → pot setting
- 2ζωₙ/β = 4/100 = 0.04 → pot setting

### Component Values

| Component | Value | Function |
|-----------|-------|----------|
| R (all) | 100kΩ | Standard input resistance |
| C₁, C₂ | 100nF | Integration capacitor |
| R_k pot | 0.01 of full scale | ωₙ² coefficient |
| R_b pot | 0.04 of full scale | 2ζωₙ coefficient |
| R_F pot | Adjustable | Force amplitude |

## Step-by-Step Build

### Step 1: Build Two Integrators

Following the [Simple ODE Tutorial](02-simple-ode.md):
- INT1: Output is x' (velocity)
- INT2: Input from INT1, output is x (position)

### Step 2: Build Summer

At input of INT1:
- Input 1: F(t)/m (forcing)
- Input 2: -2ζωₙ × x' (damping)
- Input 3: -ωₙ² × x (spring)

### Step 3: Set Coefficients

Using precision potentiometers:
1. Set damping coefficient (2ζωₙ)
2. Set spring coefficient (ωₙ²)
3. Set force scaling

### Step 4: Connect Feedback

- x' → damping pot → summer
- x → spring pot → summer

### Step 5: Set Initial Conditions

For step response from rest:
- IC for x: set to x₀ (initial displacement)
- IC for x': set to 0 (starting from rest)

For impulse response:
- IC for x: 0
- IC for x': v₀ (initial velocity)

## Running the Simulation

### Step Response

1. Set IC: x = x₀, x' = 0
2. Set F(t) = 0 (free response)
3. Switch to OPERATE mode
4. Observe oscillation on scope

**Expected (underdamped, ζ = 0.2):**
- Oscillatory decay
- Frequency ≈ fₙ (slightly less)
- Amplitude envelope: e^(-ζωₙt)

### Forced Response

1. Apply sinusoidal F(t) from function generator
2. Vary frequency from 0.1fₙ to 10fₙ
3. Observe amplitude and phase

**At resonance (ω = ωₙ):**
- Maximum amplitude
- Phase = -90°

## Measurements

### From Oscilloscope

| Parameter | How to Measure |
|-----------|----------------|
| Natural frequency | Peak-to-peak time in free response |
| Damping ratio | Logarithmic decrement of peaks |
| Steady-state amplitude | Amplitude after transient dies |
| Phase | Time delay × frequency × 360° |

### Logarithmic Decrement

```
δ = ln(x₁/x₂) = ln(peak₁/peak₂)

ζ = δ / √(4π² + δ²)
```

## Exploring Parameter Effects

### Varying Damping (ζ)

| Setting | Behavior |
|---------|----------|
| ζ = 0 | Continuous oscillation |
| ζ = 0.1 | Lightly damped, many cycles |
| ζ = 0.5 | Moderate damping, few cycles |
| ζ = 1.0 | Critical, no oscillation |
| ζ = 2.0 | Overdamped, slow return |

### Varying Stiffness (k)

Higher k:
- Higher natural frequency
- Faster oscillation
- Quick response

Lower k:
- Lower natural frequency
- Slower oscillation
- Sluggish response

## Extensions

### Adding Coulomb Friction

```
F_friction = -μ·sign(x')
```

Requires comparator for sign detection.

### Nonlinear Spring

```
F_spring = -k₁·x - k₃·x³
```

Requires multiplier for x³ term.

### Multiple Masses

Coupled oscillators:
- Two masses, two springs
- Four integrators
- Mode coupling visible

## Troubleshooting

### System Doesn't Oscillate

- Check damping isn't too high (ζ > 1)
- Verify spring coefficient is non-zero
- Check feedback polarity (must be negative)

### Amplitude Grows Without Bound

- Positive feedback somewhere (check signs)
- Damping coefficient is negative

### Wrong Frequency

- Check time constant (RC product)
- Verify coefficient pot settings
- Confirm time scaling factor

## Key Learnings

1. **Two integrators needed for 2nd-order ODE**
2. **Damping determines oscillation decay**
3. **Natural frequency set by m and k**
4. **Resonance occurs when forcing frequency = natural frequency**
5. **Parameter changes have immediate, visible effect**

## Further Reading

- [ODE Solving](../03-mathematics/03-ode-solving.md)
- [Oscillators](04-oscillators.md)
- [Physics Simulations](../04-applications/02-physics-simulations.md)
