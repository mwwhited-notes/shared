# Physics Simulations

## Overview

Analog computers excel at simulating physical systems because the mathematical structure of analog circuits mirrors physical laws. The continuous nature of analog computation matches the continuous nature of physical phenomena[^1].

## Mechanical Systems

### Simple Harmonic Oscillator

```
m·d²x/dt² + k·x = 0
```

**Natural frequency:** ω₀ = √(k/m)

**Implementation:**
```
         ┌───────────────────────────────────┐
         │                                   │
         ↓                                   │
───[−k/m]┴──[INT]──┬──[INT]──┬── x          │
                   │         │               │
                  x'         │               │
                             │               │
                   ┌─────────┘               │
                   │                         │
                   └─────────────────────────┘
```

**Output:** x = A·cos(ω₀t + φ)

### Damped Oscillator

```
m·d²x/dt² + b·dx/dt + k·x = 0
```

Add damping feedback:
```
                   ┌─────────────────────────┐
         ┌─────────┼─────────────────────────┼──┐
         │         │                         │  │
         ↓         ↓                         │  │
───[SUM]──┴──[INT]──┬──[INT]──┬── x          │  │
    ↑              │         │               │  │
    │             x'         │               │  │
    │              │         │               │  │
    └───[−b/m]◄────┘         │               │  │
    │                        │               │  │
    └───[−k/m]◄──────────────┘───────────────┘  │
                                                │
                             └──────────────────┘
```

### Forced Oscillations

```
m·d²x/dt² + b·dx/dt + k·x = F₀·cos(ωt)
```

Add forcing function to summer input.

**Demonstrates:**
- Resonance at ω = ω₀
- Phase relationships
- Amplitude response curves

### Coupled Oscillators

Two masses connected by springs:
```
m₁·x₁'' = -k₁·x₁ + k₂(x₂ - x₁)
m₂·x₂'' = -k₂(x₂ - x₁) - k₃·x₂
```

**Shows:** Normal modes, energy transfer between oscillators

## Projectile Motion

### Basic Trajectory

```
d²x/dt² = 0
d²y/dt² = -g
```

**Implementation:**
```
v_x0 ──[INT]── x(t) = v_x0·t

0 ──[INT]── v_y ──[INT]── y(t)
      ↑
    -g (constant input)

Initial: v_y(0) = v_y0, y(0) = y_0
```

### With Air Resistance

```
d²x/dt² = -(b/m)·vₓ·|v|
d²y/dt² = -g - (b/m)·vᵧ·|v|

|v| = √(vₓ² + vᵧ²)
```

Requires:
- Squarers for v²
- Square root
- Multipliers

### Orbital Mechanics

Two-body problem:
```
d²x/dt² = -GM·x/r³
d²y/dt² = -GM·y/r³

r = √(x² + y²)
```

**Implementation challenges:**
- Computing r⁻³ (cube and inverse)
- Maintaining accuracy over orbits
- Time scaling for different orbit periods

## Electrical Circuit Simulation

### RLC Circuit

```
L·dI/dt + R·I + (1/C)·∫I dt = V(t)

Or as second order:
L·C·d²v_c/dt² + R·C·dv_c/dt + v_c = V(t)
```

**Analog of mass-spring-damper:**
| Mechanical | Electrical |
|------------|------------|
| Mass m | Inductance L |
| Damping b | Resistance R |
| Spring k | 1/Capacitance |
| Force F | Voltage V |
| Velocity v | Current I |

### Transmission Line

Distributed LC elements (wave equation):
```
∂V/∂x = -L·∂I/∂t
∂I/∂x = -C·∂V/∂t
```

Simulated with ladder network of integrators.

## Thermal Systems

### Heat Conduction

One-dimensional heat equation:
```
∂T/∂t = α·∂²T/∂x²
```

**RC ladder analog:**
```
        R         R         R
T₀ ────/\/\/──┬──/\/\/──┬──/\/\/── T₃
              │         │
             ═╪═       ═╪═
              │ C       │ C
              │         │
             ─┴─       ─┴─
             GND       GND

R represents thermal resistance
C represents thermal capacitance
```

### Thermal Transients

Heating/cooling of objects:
```
C·dT/dt = P - k(T - T_ambient)

Where:
C = thermal mass
P = power input
k = heat transfer coefficient
```

## Fluid Dynamics

### Tank Draining (Torricelli)

```
A·dh/dt = Q_in - C_d·A_orifice·√(2gh)
```

Nonlinear due to √h term.

**Implementation:**
- Square root function generator
- Or: use h² variable, reformulate

### Hydraulic Systems

```
              ┌──[Pump]──┐
              │          │
   Reservoir ─┤          ├─ Load
              │          │
              └──[Valve]─┘

Flow-pressure relationships:
Q = C_v·√(ΔP)  (valve)
P = ρgh + P₀   (static)
```

## Wave Phenomena

### Standing Waves on a String

```
∂²y/∂t² = c²·∂²y/∂x²
```

Discretize x, implement as coupled oscillator chain.

### Acoustic Resonance

Helmholtz resonator:
```
m·d²x/dt² + R·dx/dt + k·x = F(t)

where m = ρ·L·S/V (acoustic mass)
      k = ρ·c²·S²/V (acoustic stiffness)
```

## Electromagnetic Fields

### LC Oscillator

```
L·dI/dt = V
C·dV/dt = -I

Combined: d²V/dt² = -V/(LC)
```

**Analog:** Two integrators with cross-feedback

### Electromagnetic Induction

Faraday's law simulation:
```
EMF = -N·dΦ/dt
```

Differentiator (or work backward with integration).

## Nuclear Physics

### Radioactive Decay

```
dN/dt = -λN

Solution: N(t) = N₀·e^(-λt)
```

**Analog:** Integrator with positive feedback

```
         ┌──────────────────┐
         │                  │
         ↓                  │
N₀ ──[INT]──[×−λ]─────┬── N(t)
         ↑            │
         │            │
         └────────────┘
```

### Chain Decay

```
A → B → C

dN_A/dt = -λ_A·N_A
dN_B/dt = λ_A·N_A - λ_B·N_B
dN_C/dt = λ_B·N_B
```

Three coupled equations, three integrators.

### Neutron Transport (FERMIAC)

Enrico Fermi's FERMIAC computed neutron random walks[^2]:
- Monte Carlo analog computation
- Mechanical device with random elements
- Used for reactor design

## Quantum Mechanics Analogs

### Schrödinger Equation (Simplified)

Time-independent 1D:
```
-ℏ²/(2m)·d²ψ/dx² + V(x)·ψ = E·ψ
```

Can be simulated for simple potentials using spatial discretization.

### Harmonic Oscillator Potential

```
V(x) = (1/2)·m·ω²·x²
```

Analog of classical oscillator with quantum interpretation.

## Chaos and Nonlinear Dynamics

### Double Pendulum

```
θ₁'' = f₁(θ₁, θ₂, θ₁', θ₂')
θ₂'' = f₂(θ₁, θ₂, θ₁', θ₂')
```

Complex nonlinear functions, demonstrates chaos.

### Lorenz Attractor

```
dx/dt = σ(y - x)
dy/dt = x(ρ - z) - y
dz/dt = xy - βz
```

Classic demonstration of deterministic chaos.
- Standard parameters: σ=10, ρ=28, β=8/3
- Displays butterfly-shaped attractor on X-Y plotter

## Practical Considerations

### Time Scaling

| Physical Process | Time Scale | Computer Scale |
|------------------|------------|----------------|
| Ballistic trajectory | seconds | real-time |
| Orbital motion | hours-days | sped up 1000× |
| Nuclear decay | microseconds-years | adjusted to seconds |
| Thermal transients | minutes-hours | sped up 10-100× |

### Output Display

- **Oscilloscope:** Time traces, X-Y phase plots
- **X-Y Plotter:** Permanent records
- **Panel meters:** Steady-state values
- **Strip chart:** Slow processes

## References

[^1]: [Analog Simulation - ScienceDirect Topics](https://www.sciencedirect.com/topics/engineering/analog-simulation)
[^2]: [FERMIAC - Computer History Museum](https://computerhistory.org/blog/why-analog-computers/)

## Further Reading

- [ODE Solving](../03-mathematics/03-ode-solving.md)
- [PDE Solving](../03-mathematics/04-pde-solving.md)
- [Engineering Problems](03-engineering-problems.md)
- [Chaos and Strange Attractors](../07-tutorials/05-chaos-attractors.md)
