# Chaos and Strange Attractors

## Overview

Chaotic systems exhibit sensitive dependence on initial conditions—small differences grow exponentially, making long-term prediction impossible despite deterministic equations. Analog computers are excellent tools for visualizing chaos.

## What is Chaos?

### Characteristics

1. **Deterministic:** Same equations, same results (in theory)
2. **Sensitive to ICs:** Tiny changes → completely different trajectories
3. **Bounded:** Solutions stay within finite region
4. **Aperiodic:** Never exactly repeats
5. **Strange attractors:** Complex geometric structure

### Famous Quote

> "Does the flap of a butterfly's wings in Brazil set off a tornado in Texas?" — Edward Lorenz

## The Lorenz System

### The Equations

```
dx/dt = σ(y - x)
dy/dt = x(ρ - z) - y
dz/dt = xy - βz
```

### Parameters

Standard chaotic values:
- σ (sigma) = 10
- ρ (rho) = 28
- β (beta) = 8/3 ≈ 2.67

### Physical Origin

Simplified model of atmospheric convection:
- x: Convection intensity
- y: Temperature difference (horizontal)
- z: Temperature difference (vertical)

### The Strange Attractor

```
        z
        │     ╭──────╮     ╭──────╮
        │    ╱        ╲   ╱        ╲
        │   │          ╲ ╱          │
        │   │           ╳           │
        │    ╲        ╱   ╲        ╱
        │     ╰──────╯     ╰──────╯
        │
        └────────────────────────────── y
       ╱
      ╱ x
     ╱
```

The "butterfly" or "owl mask" shape.

## Analog Implementation of Lorenz

### Block Diagram

```
Equation 1: dx/dt = σ(y - x)
┌────────────────────────────────────────┐
│                                        │
y ───┬───┐                               │
     │   ├──[−σ×y + σ×x]──[INT]──┬── x   │
x ───┴───┘                       │       │
     ↑                           │       │
     └───────────────────────────┘       │
                                         │
Equation 2: dy/dt = x(ρ - z) - y         │
┌────────────────────────────────────────┤
│                                        │
x ────[×(ρ-z)]──┐                        │
      MULT      │                        │
z ──[−1]────────┤                        │
      ↓         ├──[−y]──[INT]──┬── y    │
ρ ──[REF]───────┘               │        │
                                │        │
y ──────────────────────────────┘        │
                                         │
Equation 3: dz/dt = xy - βz              │
┌────────────────────────────────────────┘
│
x ────[MULT]──┐
      ×y      │
y ────────────┤
              ├──[−βz]──[INT]──┬── z
z ─────[×β]───┘                │
                               │
              ┌────────────────┘
              └── (z fed back)
```

### Components Required

| Element | Quantity | Function |
|---------|----------|----------|
| Integrators | 3 | One per state variable |
| Multipliers | 2 | xy and x(ρ-z) terms |
| Summers | 3 | Combining terms |
| Inverters | As needed | Sign inversions |
| Pots | 3+ | σ, ρ, β coefficients |

### Scaling

For ±10V operation:
- x, y: typically range ±20 → scale by 0.5
- z: typically ranges 0-50 → scale by 0.2 and offset

Adjust coefficients accordingly.

## Observing the Attractor

### X-Y Display

Connect oscilloscope:
- X channel: x output
- Y channel: y output (or z)

**Settings:**
- X-Y mode (not timebase)
- DC coupling
- Adjust scales for full view

### 3D Visualization

To see the 3D structure:
1. Display x vs. y
2. Display x vs. z
3. Display y vs. z
4. Rotate mentally (or use three scopes)

### Time Traces

Individual x(t), y(t), z(t) show aperiodic oscillation.

## The Van der Pol Oscillator

### Equation

```
d²x/dt² - μ(1 - x²)·dx/dt + x = 0
```

### Behavior

- μ = 0: Simple harmonic oscillator
- μ > 0: Limit cycle (self-sustained oscillation)
- Large μ: Relaxation oscillations

### Analog Implementation

```
              ┌────────────────────────────────────────────┐
              │                                            │
              │     ┌─────────────────────────────────────────┐
              │     │                                      │  │
        ┌─────┴─────┴────────────────────────────────────┐ │  │
        │                                                │ │  │
────────┤───[SUM]──[INT]──┬──[INT]──┬── x                │ │  │
        │     ↑           │         │                    │ │  │
        │     │          x'         │                    │ │  │
        │     │           │         │                    │ │  │
        │     │    ┌──────┘         │                    │ │  │
        │     │    │                │                    │ │  │
        │     │    ├──[MULT]──(1-x²)│                    │ │  │
        │     │    │    ↑           │                    │ │  │
        │     │    │ (1-x²)         │                    │ │  │
        │     │    │    │           │                    │ │  │
1 ──────┼─────┼────┼────┤           │                    │ │  │
        │     │    │    │           │                    │ │  │
x ──────┼─────┼────┼──[MULT]──[×−1]─┤                    │ │  │
        │     │    │    ↑           │                    │ │  │
x ──────┼─────┼────┴────┘           │                    │ │  │
        │     │                     │                    │ │  │
        │     └───[−1]◄─────────────┘────────────────────┘ │  │
        │                                                  │  │
        └───[×μ]───(multiplied by μ)───────────────────────┘  │
                                                              │
                   └──────────────────────────────────────────┘
```

### X-Y Display (Phase Portrait)

- X: position x
- Y: velocity x'

Shows limit cycle as closed curve.

## The Rössler System

### Equations

```
dx/dt = -y - z
dy/dt = x + ay
dz/dt = b + z(x - c)
```

### Parameters for Chaos

- a = 0.2
- b = 0.2
- c = 5.7

### Advantages for Analog

- Only ONE multiplication (xz)
- Simpler than Lorenz
- Good first chaotic system to build

### Attractor Shape

Single-scroll attractor, simpler than Lorenz butterfly.

## Chua's Circuit

### The Simplest Chaotic Circuit

```
        C₁              L
   ┌────||────┬────────────┬────────┐
   │          │            │        │
   │    ┌─────┴─────┐      │       ═╪═ C₂
   │    │   Chua's  │     /\/\/     │
   │    │   Diode   │      R        │
   │    │   (NR)    │      │        │
   │    └───────────┘      │        │
   │          │            │        │
   └──────────┴────────────┴────────┘
```

### Chua's Diode

Piecewise-linear negative resistance:
```
i = G_b × v + 0.5(G_a - G_b)(|v + B_p| - |v - B_p|)
```

Built from op-amps and resistors.

### Why Famous

- Proven chaotic
- Easy to build
- Well-studied mathematically
- Demonstrates route to chaos

## Exploring Parameter Space

### Bifurcation

As parameters change, system behavior changes:

```
ρ in Lorenz system:
ρ < 1:     Stable fixed point
1 < ρ < 24.74: Stable periodic orbits
ρ > 24.74: Chaos (with periodic windows)
```

### Route to Chaos

1. **Period doubling:** Oscillation period keeps doubling
2. **Intermittency:** Occasional bursts of chaos
3. **Crisis:** Sudden appearance of chaos

### Analog Exploration

Vary pot slowly while watching X-Y display:
- See fixed points collapse
- Watch limit cycles form
- Observe period doubling
- Transition to chaos

## Practical Tips

### Numerical Stability

Unlike digital simulations, analog computers:
- Don't have numerical instability
- Don't require small time steps
- Naturally handle stiff equations

### Amplitude Limiting

Add limiters to prevent runaway:
- Zener diodes in feedback
- Soft limiters

### Noise

Some noise is OK—actually makes chaos more "realistic."
Too much noise obscures structure.

### Time Scaling

Slow down for visual observation:
- Lorenz naturally around 1Hz range
- Scale to ~0.1-1 Hz for comfortable viewing

## Measurement

### Largest Lyapunov Exponent

Measures rate of divergence:
- λ > 0: Chaotic
- λ = 0: Periodic
- λ < 0: Stable

Difficult to measure accurately with analog, but can estimate.

### Power Spectrum

Chaotic systems have broadband spectrum (not just harmonics).
Use spectrum analyzer or FFT.

### Fractal Dimension

Strange attractors have non-integer dimension.
Requires digitizing and analysis.

## Educational Value

### What Students Learn

1. **Determinism ≠ predictability**
2. **Nonlinearity creates complexity**
3. **Sensitivity to initial conditions**
4. **Geometry of phase space**
5. **Bifurcations and routes to chaos**

### Comparison with Digital

Run same system on analog and digital:
- Trajectories diverge (both are correct!)
- Demonstrates sensitivity
- Analog shows continuous evolution

## Further Projects

### Double Scroll (Chua)

Build Chua's circuit and observe double-scroll attractor.

### Coupled Oscillators

Two Van der Pol oscillators with coupling:
- Synchronization
- Chaos
- Quasiperiodicity

### Driven Duffing

```
d²x/dt² + δ·dx/dt + αx + βx³ = γcos(ωt)
```

Shows chaos in driven system.

## Resources

- [Analog Computer Chaos - Bernd Ulmann](https://analogparadigm.com/)
- Edward Lorenz, "Deterministic Nonperiodic Flow" (1963)
- [Chua's Circuit - Scholarpedia](http://scholarpedia.org/article/Chua_circuit)

## Further Reading

- [Nonlinear Equations](../03-mathematics/06-nonlinear-equations.md)
- [Physics Simulations](../04-applications/02-physics-simulations.md)
- [THE Analog Thing](../06-modern-systems/01-the-analog-thing.md)
