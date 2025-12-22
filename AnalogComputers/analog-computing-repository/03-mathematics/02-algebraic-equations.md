# Solving Algebraic Equations

## Overview

While analog computers are primarily designed for differential equations, they can solve certain algebraic equations by converting them to dynamic systems that converge to the solution.

## Basic Approach

### Converting Algebra to Dynamics

The key insight: An algebraic equation f(x) = 0 can be solved by creating a dynamic system that converges to the root.

**Method 1: Gradient Descent**
```
dx/dt = -f(x)

As t → ∞, if stable: x → root of f(x) = 0
```

**Method 2: Newton-Raphson Dynamics**
```
dx/dt = -f(x)/f'(x)

Faster convergence but requires computing derivative
```

## Polynomial Equations

### Linear Equation: ax + b = 0

Solution: x = -b/a

**Dynamic Implementation:**
```
dx/dt = -(ax + b)
```

**Circuit:**
```
              ┌────────────────────────────────────┐
              │                                    │
              ↓                                    │
b ──[pot:1]──[SUM]──[-1]──[INT]──┬── x (converges to -b/a)
              ↑                  │
              │                  │
x ──[pot:a]──┘                   │
              │                  │
              └──────────────────┘
```

### Quadratic Equation: ax² + bx + c = 0

**Dynamic system:**
```
dx/dt = -(ax² + bx + c)
```

**Circuit:**
```
x ──┬──[MULT]──[pot:a]──┐
    │          (x²)     │
    │                   │
    ├──[pot:b]──────────┼──[SUM]──[-1]──[INT]─┬── x
    │                   │                     │
c ──┴───────────────────┘                     │
                                              │
                   ┌──────────────────────────┘
                   │
                   └─→ (feedback to x)
```

**Notes:**
- Converges to one root (depending on initial condition)
- Different ICs may find different roots
- May not find complex roots

### Higher-Order Polynomials

For p(x) = aₙxⁿ + aₙ₋₁xⁿ⁻¹ + ... + a₁x + a₀ = 0

**Implementation:**
1. Build polynomial using multipliers and summers
2. Use gradient descent: dx/dt = -p(x)
3. Vary initial conditions to find different roots

## Simultaneous Linear Equations

### Two Equations, Two Unknowns

```
a₁₁x + a₁₂y = b₁
a₂₁x + a₂₂y = b₂
```

**Dynamic system (relaxation method):**
```
dx/dt = -(a₁₁x + a₁₂y - b₁)
dy/dt = -(a₂₁x + a₂₂y - b₂)
```

**Circuit Diagram:**
```
        ┌──────────────────────────────────────┐
        │                                      │
        ↓                                      │
b₁ ────[SUM]────[-1]────[INT]────┬──── x      │
        ↑                        │             │
        │                        │             │
x ─[a₁₁]┤                        └─────────────┤
        │                                      │
y ─[a₁₂]┘                                      │
                                               │
        ┌──────────────────────────────────────┼──┐
        │                                      │  │
        ↓                                      │  │
b₂ ────[SUM]────[-1]────[INT]────┬──── y      │  │
        ↑                        │             │  │
        │                        │             │  │
x ─[a₂₁]┤                        └─────────────┘  │
        │                                         │
y ─[a₂₂]┘─────────────────────────────────────────┘
```

### Convergence Conditions

The system converges if the matrix A is:
- Diagonally dominant: |aᵢᵢ| > Σⱼ≠ᵢ |aᵢⱼ|
- Or: All eigenvalues have positive real parts

### n Linear Equations

Generalization for Ax = b:
```
dx/dt = -(Ax - b) = -Ax + b
```

Implemented with n integrators and coefficient network.

## Nonlinear Algebraic Equations

### Single Equation f(x) = 0

**Newton-Raphson in analog:**
```
dx/dt = -f(x)/f'(x)
```

Requires:
- Computing f(x)
- Computing f'(x) (may use differentiator or explicit formula)
- Division circuit

### System of Nonlinear Equations

For F(x) = 0 where x is a vector:
```
dx/dt = -F(x)
```

Or with Jacobian J(x):
```
dx/dt = -J⁻¹(x)F(x)  (Newton-Raphson)
```

**Example: Two nonlinear equations**
```
f(x,y) = x² + y² - 4 = 0    (circle)
g(x,y) = x - y = 0          (line)
```

**Dynamic system:**
```
dx/dt = -(x² + y² - 4)
dy/dt = -(x - y)
```

Intersection points are equilibria.

## Special Cases

### Square Root: x = √a

Solve: x² - a = 0

**Circuit:**
```
x ──[MULT]──┐
            ├──[SUM]──[-1]──[INT]─┬── x → √a
a ─[−1]─────┘                     │
                                  │
            ┌─────────────────────┘
            │
            └─→ (feedback)
```

Initial condition must be positive for positive root.

### Reciprocal: x = 1/a

Solve: ax - 1 = 0

**Circuit:**
```
x ──[MULT]──┐
            ├──[SUM]──[-1]──[INT]─┬── x → 1/a
a ──────────┘                     │
                                  │
1 ─[−1]─────┘                     │
                                  │
            ┌─────────────────────┘
            └─→ (feedback)
```

### Division: x = b/a

Solve: ax - b = 0

Implemented similarly to reciprocal with b instead of 1.

## Implicit Functions

### Finding y given f(x,y) = 0

For fixed x, find y such that f(x,y) = 0:

```
dy/dt = -f(x,y)

With x held constant, y converges to solution
```

**Example: y³ + xy - 1 = 0**
```
dy/dt = -(y³ + xy - 1)
```

For each x value, system finds corresponding y.

## Optimization: Finding Extrema

### Minimizing f(x)

Find x where df/dx = 0:

**Gradient descent:**
```
dx/dt = -df/dx = -f'(x)
```

Converges to local minimum (if starting in basin of attraction).

### Multivariable Optimization

For f(x,y):
```
dx/dt = -∂f/∂x
dy/dt = -∂f/∂y
```

Converges to local minimum (gradient descent).

### Constrained Optimization

Using penalty methods:
```
Minimize f(x) subject to g(x) = 0

Augmented objective: L(x) = f(x) + λ·g(x)²
```

## Practical Considerations

### Convergence Speed

- Depends on equation structure
- May need time scaling for fast convergence
- Trade-off: speed vs. accuracy

### Multiple Solutions

- Different initial conditions find different roots
- May need to run multiple times
- No guarantee of finding all roots

### Stability

Not all formulations are stable:
```
dx/dt = -f(x)  is stable if f'(x) > 0 at root
dx/dt = +f(x)  is unstable at same root
```

### Accuracy

Limited by:
- Component tolerances
- Noise
- Settling time
- Dynamic range

Typical: 1-3 significant figures

## Summary

| Problem | Dynamic System | Components |
|---------|---------------|------------|
| Linear: ax + b = 0 | dx/dt = -(ax+b) | 1 INT, pots |
| Quadratic | dx/dt = -(ax²+bx+c) | 1 INT, 1 MULT, pots |
| Linear system Ax=b | dx/dt = -(Ax-b) | n INT, coefficient matrix |
| √a | dx/dt = -(x²-a) | 1 INT, 1 MULT |
| General f(x)=0 | dx/dt = -f(x) | Depends on f |

## Further Reading

- [Ordinary Differential Equations](03-ode-solving.md)
- [Nonlinear Equations](06-nonlinear-equations.md)
- [Chaos and Attractors](../07-tutorials/05-chaos-attractors.md)
