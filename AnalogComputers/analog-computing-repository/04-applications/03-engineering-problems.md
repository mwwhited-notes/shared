# Engineering Problems

## Overview

Analog computers have been extensively used in engineering for design analysis, prototype simulation, and real-time computation. This document covers classic and modern engineering applications[^1].

## Structural Engineering

### Beam Deflection

Euler-Bernoulli beam equation:
```
EI·d⁴y/dx⁴ = w(x)
```

Where:
- E = Young's modulus
- I = moment of inertia
- y = deflection
- w(x) = distributed load

**Solution approach:**
```
d²M/dx² = w(x)      (load to moment)
M = EI·d²y/dx²      (moment-curvature)
```

Four integrations with appropriate boundary conditions.

### Vibration Analysis

Multi-story building vibration:
```
[M]·{ẍ} + [C]·{ẋ} + [K]·{x} = {F(t)}
```

Each floor is a degree of freedom:
- Mass matrix [M]: diagonal for lumped mass
- Stiffness matrix [K]: story stiffnesses
- Damping matrix [C]: structural damping

**Analog implementation:** n integrator pairs for n stories

### Structural Dynamics

Response to earthquake excitation:
```
ẍ + 2ζωₙẋ + ωₙ²x = -ẍ_ground(t)
```

Ground acceleration as forcing function.

## Aerospace Engineering

### Aircraft Longitudinal Dynamics

```
Short period approximation:
α̇ = q - (1/mU₀)(L_α·α + L_δ·δ_e)
q̇ = (1/I_y)(M_α·α + M_q·q + M_δ·δ_e)
```

**State variables:**
- α: angle of attack
- q: pitch rate
- δ_e: elevator deflection (input)

### Rocket Trajectory

```
m·dv/dt = T - D - mg·sin(γ)
m·v·dγ/dt = L - mg·cos(γ)
dh/dt = v·sin(γ)
dx/dt = v·cos(γ)
dm/dt = -ṁ_fuel
```

**Nonlinearities:**
- Mass changes with time
- Drag varies with velocity squared
- Atmosphere varies with altitude

### Orbital Mechanics

Two-body problem:
```
r̈ = -μ/r³·r⃗

In components:
ẍ = -μx/r³
ÿ = -μy/r³
r = √(x² + y²)
```

Historical use: NASA trajectory calculations pre-Apollo[^2]

## Automotive Engineering

### Vehicle Dynamics

Quarter-car suspension model:
```
m_s·ẍ_s = -k_s(x_s - x_u) - c_s(ẋ_s - ẋ_u)
m_u·ẍ_u = k_s(x_s - x_u) + c_s(ẋ_s - ẋ_u) - k_t(x_u - x_r)
```

Where:
- m_s: sprung mass (body)
- m_u: unsprung mass (wheel)
- k_s, c_s: suspension spring and damper
- k_t: tire stiffness
- x_r: road input

### Engine Dynamics

Crankshaft torsional vibration:
```
I_i·θ̈_i + k_i(θ_i - θ_{i-1}) + k_{i+1}(θ_i - θ_{i+1}) = T_i(t)
```

Multiple coupled oscillators for each cylinder.

### Anti-lock Braking System (ABS)

Wheel slip dynamics:
```
λ = (V_vehicle - ω·r_wheel)/(V_vehicle)

I·ω̇ = r·F_brake - r·F_traction(λ)
```

Nonlinear tire-road friction characteristic.

## Chemical Engineering

### Reactor Dynamics

Continuous stirred-tank reactor (CSTR):
```
V·dC_A/dt = F(C_{A,in} - C_A) - V·k(T)·C_A
V·ρ·c_p·dT/dt = F·ρ·c_p(T_in - T) + (-ΔH_r)·V·k(T)·C_A - Q_cool
```

**Nonlinearities:**
- Arrhenius temperature dependence: k(T) = k_0·exp(-E_a/RT)
- Potential for runaway reactions

### Distillation Column

Multi-stage equilibrium:
```
For each stage i:
L_{i-1}·x_{i-1} + V_{i+1}·y_{i+1} = L_i·x_i + V_i·y_i

Energy balance:
V_i·H_V,i + L_{i-1}·H_L,i-1 = V_{i+1}·H_V,i+1 + L_i·H_L,i ± Q_i
```

Implemented as network of coupled equations.

### Process Control

Typical control loops:
- Temperature control (PID with lag)
- Pressure control (fast dynamics)
- Level control (integrating process)
- Flow control (cascade master)

## Electrical Engineering

### Power System Stability

Swing equation for generator:
```
M·dδ/dt = P_m - P_e·sin(δ)
```

Where:
- M: inertia constant
- δ: rotor angle
- P_m: mechanical power
- P_e: electrical power

**Multi-machine systems:** Coupled swing equations

### Motor Drive Dynamics

DC motor:
```
L_a·di_a/dt + R_a·i_a + K_e·ω = V_a
J·dω/dt + B·ω = K_t·i_a - T_load
```

Field-oriented control of AC motors requires coordinate transformations.

### Filter Design

Prototype Butterworth/Chebyshev filters:
- Design normalized prototype
- Simulate frequency response
- Verify transient response
- Scale to final implementation

## Nuclear Engineering

### Reactor Kinetics

Point kinetics equations:
```
dn/dt = (ρ - β)/Λ·n + Σλ_i·C_i
dC_i/dt = β_i/Λ·n - λ_i·C_i
```

Where:
- n: neutron density
- C_i: precursor concentrations
- ρ: reactivity
- β: delayed neutron fraction
- Λ: generation time

**Control rod dynamics:** ρ as function of rod position

### Heat Transfer in Fuel Elements

```
ρ·c_p·∂T/∂t = (1/r)·∂/∂r(k·r·∂T/∂r) + q'''
```

Radial discretization for fuel rod temperature profile.

## Biomedical Engineering

### Cardiovascular System

Windkessel model:
```
P_aorta = R·Q + C·dP_aorta/dt
```

Multi-compartment model:
```
C_1·dP_1/dt = Q_in - (P_1 - P_2)/R_1
C_2·dP_2/dt = (P_1 - P_2)/R_1 - (P_2 - P_3)/R_2
...
```

### Pharmacokinetics

Drug distribution:
```
dC_1/dt = -(k_12 + k_10)·C_1 + k_21·C_2 + D(t)/V_1
dC_2/dt = k_12·C_1 - k_21·C_2
```

Two-compartment model with drug input D(t).

### Neural Dynamics

Hodgkin-Huxley model (simplified):
```
C_m·dV/dt = -g_Na·m³·h·(V - E_Na) - g_K·n⁴·(V - E_K) - g_L·(V - E_L) + I_ext
```

Highly nonlinear gating variables m, h, n.

## Economic Modeling

### Supply-Demand Dynamics

```
dP/dt = k(D(P) - S(P))

Where:
D(P) = a - b·P    (demand)
S(P) = c + d·P    (supply)
```

### Business Cycle Model

Samuelson-Hicks accelerator:
```
Y_t = C_t + I_t + G_t
C_t = c·Y_{t-1}
I_t = v·(Y_{t-1} - Y_{t-2})
```

Can generate oscillatory behavior.

## Real-Time Applications

### Hardware-in-the-Loop Testing

```
┌─────────────────┐     ┌─────────────────┐
│  Real ECU       │     │  Plant Model    │
│  (Controller)   │◄───►│  (Analog)       │
└─────────────────┘     └─────────────────┘
       │                        │
       └────────────────────────┘
              (closed loop)
```

**Applications:**
- Automotive ECU testing
- Avionics systems
- Industrial controllers

### Flight Simulation

Full flight simulators used analog computers through 1980s:
- 6-DOF motion equations
- Aerodynamic models
- Engine models
- Control system

## Design Optimization

### Parameter Variation

Analog advantage: Continuous parameter variation while observing response

**Process:**
1. Build analog model
2. Vary parameter (pot adjustment)
3. Observe response on scope
4. Find optimal setting
5. Record parameter value

### Sensitivity Analysis

```
∂y/∂p ≈ Δy/Δp
```

Small parameter changes produce observable output changes.

## References

[^1]: [Engineering LibreTexts - Analog Computer](https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Operational_Amplifiers_and_Linear_Integrated_Circuits_-_Theory_and_Application_(Fiore)/10:_Integrators_and_Differentiators/10.04:_Section_4-)
[^2]: [Computer History Museum - Analog Computers](https://www.computerhistory.org/revolution/analog-computers/3/141)

## Further Reading

- [Control Systems](01-control-systems.md)
- [Physics Simulations](02-physics-simulations.md)
- [Mass-Spring-Damper Tutorial](../07-tutorials/03-mass-spring-damper.md)
