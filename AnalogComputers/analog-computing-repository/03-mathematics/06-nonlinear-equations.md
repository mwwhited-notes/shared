# Nonlinear Equations

## Overview

Nonlinear equations introduce complexity but also enable modeling of real-world phenomena that linear systems cannot capture. Analog computers handle nonlinearities through multipliers, function generators, and feedback configurations.

## Types of Nonlinearities

### Polynomial Nonlinearities

```
y = ax² + bx + c
y = x³
y = xⁿ
```

**Implementation:** Multipliers and summers

### Transcendental Functions

```
y = sin(x), cos(x)
y = eˣ, ln(x)
y = tanh(x)
```

**Implementation:** Function generators (diode networks, log-antilog)

### Piecewise Linear

```
y = |x|           (absolute value)
y = max(0, x)     (rectifier/ReLU)
y = sat(x)        (saturation)
```

**Implementation:** Diodes, comparators, limiters

### Product Nonlinearities

```
y = x₁ · x₂
y = x²
y = x · f(x)
```

**Implementation:** Analog multipliers

## Implementing Common Nonlinear Functions

### Square Function: y = x²

```
x ──┬──[MULT]── y = x²/10
    │    ↑
    └────┘
```

Note: Multiplier typically has 1/10 scale factor.

### Cube Function: y = x³

```
x ──┬──[MULT]──┬──[MULT]── y = x³/100
    │    ↑     │    ↑
    └────┘     │    │
               └────┘
                 x
```

### Arbitrary Power: y = xⁿ

**Method 1: Chained multipliers** (integer n)
**Method 2: Log-antilog**
```
y = xⁿ = exp(n·ln(x))

x ──[LOG]──[×n]──[EXP]── xⁿ
```

### Sine and Cosine

**Method 1: Diode function generator** (piecewise approximation)
**Method 2: Polynomial approximation**
```
sin(x) ≈ x - x³/6 + x⁵/120 (for small x)
```
**Method 3: Harmonic oscillator**
```
d²y/dt² + ω²y = 0  generates sin(ωt), cos(ωt)
```

### Exponential: y = eˣ

Using transistor characteristics:
```
                ┌───────────────────┐
                │      Q1           │
        ────────┤──────┤├───────────┤
        x       │      │            │
                │     ─┴─           │
                │      │      OP    ├── y ≈ eˣ
                │      │            │
                │      ├───────(+)──┘
                │      │
                ▼      ▼
               GND    GND
```

### Logarithm: y = ln(x)

Interchange transistor and resistor:
```
x ──[Transistor in feedback]── y ≈ ln(x)
```

### Hyperbolic Tangent: y = tanh(x)

Useful for neural network activation:
**Method 1:** Differential pair saturation characteristic
**Method 2:** From exponentials: tanh(x) = (eˣ - e⁻ˣ)/(eˣ + e⁻ˣ)

## Nonlinear ODEs

### Van der Pol Oscillator

```
d²x/dt² - μ(1 - x²)·dx/dt + x = 0
```

**Key nonlinearity:** (1 - x²)·dx/dt

**Implementation:**
```
1 ──────────────────┐
                    │
x ──[SQR]──[×-1]────┼──[SUM]──[MULT]── (1-x²)·x'
                    │           ↑
                    │           │
               x' ──────────────┘
```

### Duffing Oscillator

```
d²x/dt² + δ·dx/dt + αx + βx³ = γcos(ωt)
```

The x³ term creates stiffness nonlinearity.

**Implementation:** Add cube generator to standard oscillator.

### Lorenz System[^1]

```
dx/dt = σ(y - x)
dy/dt = x(ρ - z) - y
dz/dt = xy - βz
```

**Nonlinearities:** xz and xy terms (products)

**Circuit requires:**
- 3 integrators
- 2 multipliers
- Multiple summers and coefficients

### Rössler System

```
dx/dt = -y - z
dy/dt = x + ay
dz/dt = b + z(x - c)
```

**Nonlinearity:** z·x term

Simpler than Lorenz (only one multiplier needed).

## Predator-Prey Models

### Lotka-Volterra

```
dx/dt = αx - βxy    (prey)
dy/dt = δxy - γy    (predator)
```

**Nonlinearities:** xy product terms

**Block diagram:**
```
Prey equation:
x ──┬──[×α]──────┐
    │            ├──[SUM]──[INT]── x
    └──[MULT]────┘
         ↑
y ───────┘

Predator equation:
x ──[MULT]──[×δ]──┐
     ↑            ├──[SUM]──[INT]── y
y ───┴──[×-γ]─────┘
```

## Fluid Dynamics

### Navier-Stokes (Simplified)

Burgers' equation (1D simplification):
```
∂u/∂t + u·∂u/∂x = ν·∂²u/∂x²
```

**Nonlinearity:** u·∂u/∂x (convective term)

Discretized form at each point requires multiplier for u·(uᵢ₊₁-uᵢ₋₁).

## Chemical Kinetics

### Autocatalytic Reaction

```
A + B → 2B

dB/dt = k·A·B
```

**Nonlinearity:** Product A·B

### Brusselator

```
dx/dt = a - (b+1)x + x²y
dy/dt = bx - x²y
```

**Nonlinearity:** x²y requires squarer and multiplier

## Stability Analysis

### Fixed Points

Nonlinear systems have equilibrium points where dx/dt = 0.

Finding fixed points:
1. Set all derivatives to zero
2. Solve resulting algebraic equations
3. Analyze stability (linearize around fixed points)

### Limit Cycles

Some nonlinear systems exhibit sustained oscillations:
- Van der Pol oscillator
- Biological rhythms
- Chemical oscillations

Analog computers naturally reveal limit cycles as closed loops on X-Y display.

### Chaos

Certain nonlinear systems show sensitive dependence on initial conditions:
- Lorenz system (ρ > 24.74)
- Duffing oscillator (certain parameters)
- Rössler system

Analog computers were historically important in discovering chaos[^2].

## Implementation Challenges

### Multiplier Accuracy

| Error Source | Impact |
|--------------|--------|
| Scale factor error | Shifts equilibrium points |
| Offset | Adds DC bias |
| Nonlinearity | Distorts function shape |
| Temperature drift | Time-varying behavior |

### Dynamic Range

Nonlinear terms can cause signal growth:
- x² can overflow if x is large
- Need careful scaling
- May need limiters for protection

### Stability

Nonlinear systems can be:
- Stable (converge to fixed point)
- Periodic (limit cycle)
- Chaotic (bounded but unpredictable)
- Unstable (diverge to infinity)

Scaling must account for all possible behaviors.

## Practical Tips

### Scaling Nonlinear Terms

For y = x²:
```
If x ranges ±10V, then x² ranges 0-100V²
With 1/10 multiplier scale: output = x²/10, ranges 0-10V
```

### Testing Nonlinear Circuits

1. **DC test:** Apply known DC inputs, verify output
2. **Small signal:** Check linearized behavior
3. **Large signal:** Verify no saturation/clipping
4. **Limit test:** Approach boundaries of operating range

### Common Pitfalls

| Problem | Cause | Solution |
|---------|-------|----------|
| Unexpected saturation | Scaling error | Reduce gains |
| Wrong equilibrium | Multiplier offset | Trim offsets |
| Oscillation | Feedback instability | Check signs, adjust gains |
| Chaos when unexpected | Parameter errors | Verify coefficients |

## Summary of Nonlinear Elements

| Function | Components | Typical Accuracy |
|----------|------------|------------------|
| x² | 1 multiplier | 0.1-1% |
| x³ | 2 multipliers | 0.5-2% |
| xⁿ | Log-antilog | 1-3% |
| sin, cos | Function generator | 0.5-2% |
| exp, log | Transistor circuit | 1-3% |
| |x| | Precision rectifier | 0.1-0.5% |
| xy | 1 multiplier | 0.1-1% |

## References

[^1]: [Analog Computer - Wikipedia: Nonlinear Systems](https://en.wikipedia.org/wiki/Analog_computer)
[^2]: [ARS - Using Analog Computers in Today's Computational Challenges](https://ars.copernicus.org/articles/19/105/2021/)

## Further Reading

- [Multipliers and Dividers](../02-components/04-multipliers-dividers.md)
- [Function Generators](../02-components/05-function-generators.md)
- [Chaos and Strange Attractors](../07-tutorials/05-chaos-attractors.md)
