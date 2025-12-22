# Solving Ordinary Differential Equations (ODEs)

## Overview

Solving ordinary differential equations is the primary application of analog computers. The physical integration performed by capacitors directly implements mathematical integration, making analog computers natural ODE solvers[^1].

## First-Order ODEs

### General Form

```
dy/dt = f(t, y)
```

With initial condition: y(0) = y₀

### Linear First-Order: dy/dt + ay = b

**Rearrange:**
```
dy/dt = -ay + b = b - ay
```

**Block Diagram:**
```
         ┌───────────────────────────┐
         │                           │
         ↓                           │
b ───────[SUM]───[INT]────┬───────── y
           ↑              │
           │              │
y ──[×a]───┘              │
           │              │
           └──────────────┘
```

**Implementation:**
```
              C
         ┌────||────┐
         │          │
b ───────┼──────────┼───────────┬──────── y
    R1   │     R2   │           │
    ─────/\/\/──┬──/\/\/────────┤
                │               │
    ┌───────────┴──────────────(-)──┐
    │                               │
    │         OP-AMP                ├── y
    │                               │
    └─────────────────────────(+)───┘
                               │
                               ▼
                              GND
```

### Time Constant

The solution has time constant τ = 1/a:
```
y(t) = (y₀ - b/a)e^(-at) + b/a
```

Steady state: y(∞) = b/a

### RC Circuit Example

```
τ dy/dt + y = Vin

where τ = RC
```

Natural analog implementation—the equation IS the circuit!

## Second-Order ODEs

### General Form

```
d²y/dt² = f(t, y, dy/dt)
```

### Standard Form (Linear, Constant Coefficient)

```
m·d²y/dt² + b·dy/dt + k·y = F(t)
```

**Physical Interpretation:**
- m: mass
- b: damping coefficient
- k: spring constant
- F(t): forcing function

### Solution Method

**Step 1: Isolate highest derivative**
```
d²y/dt² = (1/m)[F(t) - b·dy/dt - k·y]
```

**Step 2: Apply Kelvin feedback technique**

Assume we have d²y/dt², then integrate twice:
```
d²y/dt² → [INT] → dy/dt → [INT] → y
```

**Step 3: Feed back with coefficients**

```
              ┌───────────────────────────────────────────┐
              │                                           │
              │    ┌──────────────────────────────────────┼───┐
              │    │                                      │   │
F(t)──[1/m]──[SUM]─┴──[INT]──┬──[INT]──┬── y             │   │
              ↑              │         │                  │   │
              │         dy/dt          │                  │   │
              │              │         │                  │   │
              └───[−b/m]◄────┘         │                  │   │
              │                        │                  │   │
              └───[−k/m]◄──────────────┘──────────────────┘   │
                                                              │
                                       └──────────────────────┘
```

### Complete Circuit Diagram

```
             C1                    C2
        ┌────||────┐          ┌────||────┐
        │          │          │          │
F(t)────/\/\/──┬───┼──────────/\/\/──┬───┼────── y
   R_F  R1     │   │     R3    R4    │   │
               │   │                 │   │
dy/dt ─/\/\/───┤   │    y ───/\/\/───┤   │
   R_b         │   │         R_k     │   │
               │   │                 │   │
          ┌────┴──(-)──┐        ┌────┴──(-)──┐
          │            │        │            │
          │   OP1      ├────────│   OP2      ├── y
          │            │ dy/dt  │            │
          │       (-)──┘        │       (-)──┘
          └───────────┘         └───────────┘
```

## Higher-Order ODEs

### Third-Order Example

```
d³y/dt³ + a·d²y/dt² + b·dy/dt + c·y = F(t)
```

**Solution:** Use three integrators in cascade

```
d³y/dt³ ──[INT]── d²y/dt² ──[INT]── dy/dt ──[INT]── y
   ↑                 ↑                ↑              |
   │                 │                │              │
   └──[−a]◄──────────┘                │              │
   │                                  │              │
   └──[−b]◄───────────────────────────┘              │
   │                                                 │
   └──[−c]◄──────────────────────────────────────────┘
```

### General n-th Order

For n-th order ODE:
- Need n integrators
- Highest derivative = f(lower derivatives and forcing)
- State variables: y, dy/dt, d²y/dt², ..., d^(n-1)y/dt^(n-1)

## Systems of ODEs

### Coupled Equations

```
dx/dt = f(x, y, t)
dy/dt = g(x, y, t)
```

**Example: Predator-Prey (Lotka-Volterra)**[^2]

```
dx/dt = αx - βxy    (prey)
dy/dt = δxy - γy    (predator)
```

**Block Diagram:**

```
For prey (x):
x ──┬──[×α]──┐
    │        ├──[SUM]──[INT]──┬── x
    │        │                │
    └──[MULT]┼──[×−β]─────────┤
       ↑     │                │
y ─────┘     │                └──→ (feedback)

For predator (y):
x ──┬──[MULT]──[×δ]──┐
    │          ↑     ├──[SUM]──[INT]──┬── y
y ──┴──────────┘     │                │
    │                │                │
    └──[×−γ]─────────┘                │
                                      └──→ (feedback)
```

### State-Space Form

Any system of ODEs can be written:
```
dx/dt = Ax + Bu
y = Cx + Du
```

**Implementation:**
- Matrix A: coefficient network
- Matrix B: input weighting
- n integrators for n state variables

## Nonlinear ODEs

### Van der Pol Oscillator[^3]

```
d²x/dt² - μ(1 - x²)·dx/dt + x = 0
```

**Block Diagram:**

```
         ┌────────────────────────────────────────────┐
         │                                            │
         │    ┌───────────────────────────────────────┼──┐
         │    │                                       │  │
         │    │                                       │  │
─────────[SUM]┴──[INT]──┬──[INT]──┬── x              │  │
         ↑              │         │                   │  │
         │         dx/dt          │                   │  │
         │              │         │                   │  │
         │    ┌─────────┘         │                   │  │
         │    │                   │                   │  │
         │    ├──[MULT]──[×−μ]────┤                   │  │
         │    │    ↑              │                   │  │
         │    │ (1-x²)            │                   │  │
         │    │    │              │                   │  │
1 ───────┼────┼────┤              │                   │  │
         │    │    │              │                   │  │
x ───────┼────┼──[MULT]──[×−1]────┤                   │  │
         │    │    ↑              │                   │  │
x ───────┼────┴────┘              │                   │  │
         │                        │                   │  │
         └────[×−1]◄──────────────┘───────────────────┘  │
                                                         │
                                  └───────────────────────┘
```

### Lorenz System (Chaos)[^4]

```
dx/dt = σ(y - x)
dy/dt = x(ρ - z) - y
dz/dt = xy - βz
```

Requires three integrators and three multipliers.

## Boundary Value Problems

### Shooting Method

For BVP with y(0) = a, y(T) = b:

1. Guess initial slope y'(0)
2. Integrate to t = T
3. Compare y(T) with target b
4. Adjust y'(0) and repeat

Can be automated with feedback control.

### Relaxation Method

For certain problems, use spatial discretization and solve as system of algebraic equations (see PDEs).

## Special Techniques

### Time Scaling

To observe fast or slow dynamics:
```
Physical time t → Computer time τ = βt

New equation: dy/dτ = (1/β)·f(τ/β, y)
```

β > 1: Slow down (observe fast dynamics)
β < 1: Speed up (observe slow dynamics)

### Amplitude Scaling

Prevent overflow:
```
Physical variable x → Computer variable X = αx

Rescale equation coefficients accordingly
```

### Repetitive Operation

For visualization:
1. Integrate from t = 0 to t = T
2. Reset to initial conditions
3. Repeat continuously

Creates steady display on oscilloscope.

## Accuracy Considerations

### Sources of Error

| Source | Typical Magnitude | Mitigation |
|--------|-------------------|------------|
| Component tolerance | 0.1-1% | Precision components |
| Op-amp offset | 1-10 mV | Offset trim |
| Integrator drift | 1-10 mV/s | Reset, high-quality caps |
| Capacitor leakage | 0.1%/s | Low-leakage caps |
| Temperature effects | 50-500 ppm/°C | Temperature control |
| Noise | 1-10 mV RMS | Shielding, filtering |

### Overall Accuracy

Typical analog computer accuracy: 0.01% - 0.1% (3-4 digits)

For comparison:
- 32-bit float: ~7 digits
- 64-bit float: ~16 digits

## Comparison with Digital Methods

| Aspect | Analog | Digital (Runge-Kutta) |
|--------|--------|----------------------|
| Speed | Real-time | Depends on step size |
| Accuracy | 0.01-0.1% | Machine precision |
| Stability | Natural (physical) | May need small steps |
| Setup time | Minutes-hours | Seconds |
| Parameter changes | Instant | Recompute |
| Stiff equations | May struggle | Requires special methods |

## References

[^1]: [Analogue Computing - Using Operational Amplifiers to Solve ODEs](https://www.i4cy.com/analog_computing/)
[^2]: [Analog Computer - Wikipedia](https://en.wikipedia.org/wiki/Analog_computer)
[^3]: [Analogue Computing: Fun with Differential Equations - Chalkdust Magazine](https://chalkdustmagazine.com/features/analogue-computing-fun-differential-equations/)
[^4]: [ARS - Using Analog Computers in Today's Computational Challenges](https://ars.copernicus.org/articles/19/105/2021/)

## Further Reading

- [Partial Differential Equations](04-pde-solving.md)
- [Mass-Spring-Damper Tutorial](../07-tutorials/03-mass-spring-damper.md)
- [Chaos and Strange Attractors](../07-tutorials/05-chaos-attractors.md)
- [Scaling and Normalization](../01-fundamentals/05-scaling.md)
