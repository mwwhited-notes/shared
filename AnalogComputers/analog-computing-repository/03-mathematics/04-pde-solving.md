# Solving Partial Differential Equations (PDEs)

## Overview

Analog computers can solve partial differential equations by discretizing the spatial dimensions and converting the PDE into a system of ordinary differential equations. This approach leverages the natural time-integration capability of analog hardware[^1].

## Method of Lines

### Basic Concept

The Method of Lines converts a PDE to a system of ODEs:
1. Discretize spatial dimensions into grid points
2. Approximate spatial derivatives with finite differences
3. Leave time continuous
4. Solve resulting ODE system with analog integrators

### Spatial Discretization

```
u(x,t) → uᵢ(t) at x = i·Δx

∂u/∂x ≈ (uᵢ₊₁ - uᵢ₋₁)/(2Δx)        [central difference]
∂²u/∂x² ≈ (uᵢ₊₁ - 2uᵢ + uᵢ₋₁)/(Δx)² [second derivative]
```

## Heat Equation (Diffusion)

### One-Dimensional Heat Equation

```
∂u/∂t = α·∂²u/∂x²
```

**Discretized form:**
```
duᵢ/dt = α/(Δx)²·(uᵢ₊₁ - 2uᵢ + uᵢ₋₁)
```

**For n interior points:** n coupled ODEs

### Analog Implementation

Each grid point requires one integrator:

```
For point i:

uᵢ₋₁ ──[×1]──┐
             │
uᵢ ───[×−2]──┼──[SUM]──[×α/(Δx)²]──[INT]──┬── uᵢ
             │                             │
uᵢ₊₁ ──[×1]──┘                             │
                                           │
                    ┌──────────────────────┘
                    │
                    └─→ (connects to neighboring integrators)
```

### Five-Point Network Example

```
     ┌───[INT]───┐     ┌───[INT]───┐     ┌───[INT]───┐
     │    u₁     │     │    u₂     │     │    u₃     │
u₀ ──┴───────────┴─────┴───────────┴─────┴───────────┴── u₄
(BC)      ↑                  ↑                  ↑      (BC)
          │                  │                  │
         [R]                [R]                [R]
          │                  │                  │
          └──────────────────┴──────────────────┘
                    (diffusion network)
```

### RC Ladder Network (Direct Analog)

The RC ladder directly models heat diffusion:

```
        R         R         R         R
u₀ ────/\/\/──┬──/\/\/──┬──/\/\/──┬──/\/\/── u₄
              │         │         │
             ═╪═       ═╪═       ═╪═
              │ C       │ C       │ C
              │         │         │
             ─┴─       ─┴─       ─┴─
             GND       GND       GND
```

Time constant: τ = RC corresponds to α/(Δx)²

## Wave Equation

### One-Dimensional Wave Equation

```
∂²u/∂t² = c²·∂²u/∂x²
```

**Discretized form:**
```
d²uᵢ/dt² = c²/(Δx)²·(uᵢ₊₁ - 2uᵢ + uᵢ₋₁)
```

### State-Space Form

Introduce velocity: vᵢ = duᵢ/dt

```
duᵢ/dt = vᵢ
dvᵢ/dt = c²/(Δx)²·(uᵢ₊₁ - 2uᵢ + uᵢ₋₁)
```

**For n points:** 2n integrators needed

### Analog Implementation

Each point requires two integrators (position and velocity):

```
           ┌────────────────────────────────────────┐
           │                                        │
           ↓                                        │
uᵢ₋₁ ─┬───[SUM]──[×c²/(Δx)²]──[INT]──┬──[INT]──┬── uᵢ
      │    ↑                         │ vᵢ      │
      │    │                         │         │
uᵢ ──[×−2]─┤                         └─────────┼─→ (feedback)
      │    │                                   │
      │    │                                   │
uᵢ₊₁ ─┴───┘                                   │
                                               │
           ┌───────────────────────────────────┘
           │
           └─→ (to neighboring points)
```

## Laplace's Equation (Steady-State)

### Two-Dimensional Laplace

```
∂²u/∂x² + ∂²u/∂y² = 0
```

### Resistive Network Solution

A 2D resistive network naturally solves Laplace's equation:

```
             R
      u(i,j+1)
         │
         /\/\/
         │
R        │        R
u(i-1,j)─/\/\/─ u(i,j) ─/\/\/─ u(i+1,j)
         │
         /\/\/
         │
      u(i,j-1)
```

**At each node:** Σ(currents) = 0

```
(u(i+1,j) - u(i,j))/R + (u(i-1,j) - u(i,j))/R +
(u(i,j+1) - u(i,j))/R + (u(i,j-1) - u(i,j))/R = 0
```

Simplifies to: u(i,j) = (1/4)[u(i+1,j) + u(i-1,j) + u(i,j+1) + u(i,j-1)]

### Boundary Conditions

- **Dirichlet** (fixed value): Apply voltage at boundary nodes
- **Neumann** (flux): Use high resistance to boundary
- **Mixed**: Combination of above

## Poisson's Equation

### Equation

```
∂²u/∂x² + ∂²u/∂y² = f(x,y)
```

### Implementation

Same resistive network, but inject current at each node:

```
       R              R
u(i-1,j)─/\/\/─ ● ─/\/\/─ u(i+1,j)
               │
              ─┴─ I(i,j) = f(x,y)·Δx²/R
               ↑
          (current source)
```

## Convection-Diffusion Equation

### Equation

```
∂u/∂t + v·∂u/∂x = D·∂²u/∂x²
```

**Discretized:**
```
duᵢ/dt = -v·(uᵢ₊₁ - uᵢ₋₁)/(2Δx) + D·(uᵢ₊₁ - 2uᵢ + uᵢ₋₁)/(Δx)²
```

### Stability Consideration

The Peclet number Pe = vΔx/(2D) must be small enough to avoid oscillations.

## Nonlinear PDEs

### Burgers' Equation

```
∂u/∂t + u·∂u/∂x = ν·∂²u/∂x²
```

Requires multiplier at each grid point (u·∂u/∂x term).

### Implementation Complexity

| Term | Components per Point |
|------|---------------------|
| ∂u/∂t | 1 integrator |
| ∂u/∂x | 2 coefficients |
| ∂²u/∂x² | 3 coefficients |
| u·∂u/∂x | 1 multiplier + coefficients |

## Practical Considerations

### Grid Size Limitations

Number of components grows with grid points:
- 1D: n integrators for n points
- 2D: n² integrators for n×n grid
- 3D: n³ integrators (usually impractical)

**Practical limits:**
- 1D: 10-100 points
- 2D: 5×5 to 20×20 grid
- 3D: Rarely attempted with traditional analog

### Boundary Condition Implementation

| Type | Implementation |
|------|----------------|
| Dirichlet | Fixed voltage source |
| Neumann | High resistance + current source |
| Periodic | Connect ends together |
| Radiation | Resistance to "ambient" voltage |

### Time Scaling

Physical diffusion may be too slow or fast:
```
Physical time t → Computer time τ = βt
Adjust α/(Δx)² by factor β
```

### Accuracy

Limited by:
- Number of grid points (spatial resolution)
- Component accuracy (temporal accuracy)
- Cumulative errors at many nodes

Typical: 1-5% error for practical implementations

## Modern Approaches

### Ultrasonic Metasurfaces

Recent research uses acoustic wave interactions with metasurfaces to solve PDEs[^2]:
- Wave-based computation
- Natural parallel processing
- Potential for integration

### Optical Computing

Optical systems can solve PDEs:
- Light propagation as diffusion analog
- Fourier optics for spatial derivatives
- Very high speed

### Memristor Crossbars

Emerging technology for PDE solving:
- Nanoscale components
- High density
- Programmable coefficients

## Example: 1D Heat Equation Simulation

**Setup for 5 interior points:**

```
Parameters:
- α = 0.1 m²/s (thermal diffusivity)
- L = 1 m (rod length)
- Δx = 0.2 m (spacing)
- n = 4 interior points

Coefficient: α/(Δx)² = 0.1/(0.04) = 2.5 s⁻¹

Boundary conditions:
- u₀ = 0°C (fixed)
- u₅ = 100°C (fixed)

Initial condition:
- All interior points at 20°C
```

**Circuit requires:**
- 4 integrators
- 4 summing networks
- 12 coefficient pots
- 2 reference sources (boundaries)

## References

[^1]: [Analog Computing of Partial Differential Equations - HAL Science](https://hal.science/hal-00957602/document)
[^2]: [Solving ODEs and PDEs Using Ultrasonic Metasurfaces - Nature Scientific Reports](https://www.nature.com/articles/s41598-023-38718-1)

## Further Reading

- [ODE Solving](03-ode-solving.md)
- [Physics Simulations](../04-applications/02-physics-simulations.md)
- [Engineering Problems](../04-applications/03-engineering-problems.md)
