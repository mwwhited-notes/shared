# Linear Algebra Operations

## Overview

Analog computers can perform various linear algebra operations, though they are traditionally optimized for differential equations rather than matrix operations. Modern analog approaches, particularly for neural network acceleration, have renewed interest in analog linear algebra[^1].

## Vector Operations

### Vector Addition

Adding two vectors element-wise:

```
A = [a₁, a₂, a₃]
B = [b₁, b₂, b₃]
C = A + B = [a₁+b₁, a₂+b₂, a₃+b₃]
```

**Implementation:** Parallel summers for each element:

```
a₁ ──┬──[SUM]── c₁ = a₁ + b₁
b₁ ──┘

a₂ ──┬──[SUM]── c₂ = a₂ + b₂
b₂ ──┘

a₃ ──┬──[SUM]── c₃ = a₃ + b₃
b₃ ──┘
```

### Scalar Multiplication

Multiplying a vector by a constant:

```
k × A = [k×a₁, k×a₂, k×a₃]
```

**Implementation:** Potentiometers or gain stages:

```
a₁ ──[×k]── k×a₁
a₂ ──[×k]── k×a₂
a₃ ──[×k]── k×a₃
```

### Dot Product (Inner Product)

```
A · B = a₁b₁ + a₂b₂ + a₃b₃
```

**Implementation:** Multipliers followed by summer:

```
a₁ ──┬──[MULT]──┐
b₁ ──┘          │
                │
a₂ ──┬──[MULT]──┼──[SUM]── A · B
b₂ ──┘          │
                │
a₃ ──┬──[MULT]──┘
b₃ ──┘
```

### Vector Norm (Magnitude)

```
|A| = √(a₁² + a₂² + a₃²)
```

**Implementation:** Squarers, summer, and square root:

```
a₁ ──[SQR]──┐
            │
a₂ ──[SQR]──┼──[SUM]──[SQRT]── |A|
            │
a₃ ──[SQR]──┘
```

## Matrix-Vector Multiplication

### Basic Operation

For matrix A and vector x:
```
y = Ax

where: yᵢ = Σⱼ aᵢⱼ × xⱼ
```

### 2×2 Example

```
[y₁]   [a₁₁  a₁₂] [x₁]   [a₁₁x₁ + a₁₂x₂]
[y₂] = [a₂₁  a₂₂] [x₂] = [a₂₁x₁ + a₂₂x₂]
```

**Circuit Implementation:**

```
x₁ ──┬──[×a₁₁]──┐
     │          ├──[SUM]── y₁
     │  [×a₁₂]──┘
x₂ ──┼────┘
     │
     ├──[×a₂₁]──┐
     │          ├──[SUM]── y₂
x₂ ──┴──[×a₂₂]──┘
```

### General n×m Matrix

For y = Ax where A is n×m:
- Need: n×m coefficient multipliers
- Need: n summers (one per output)
- Parallelism: All n outputs computed simultaneously

## Matrix Operations

### Matrix Addition

C = A + B (element-wise)

Simply add corresponding elements with summers.

### Matrix Multiplication

For C = A × B:
```
cᵢⱼ = Σₖ aᵢₖ × bₖⱼ
```

**Complexity:**
- n×n matrices require n³ multiplications
- Analog: n² parallel dot products
- Advantage: All computed simultaneously

### Transpose

For transposing, simply reroute connections:
- No active components needed
- Just rewiring of signal paths

## Solving Linear Systems

### Direct Method (Impractical)

For Ax = b, computing x = A⁻¹b directly is impractical in analog due to:
- Difficulty implementing matrix inversion
- Accumulation of errors

### Iterative Methods

More suitable for analog implementation:

#### Jacobi Iteration

For Ax = b:
```
xᵢ^(k+1) = (bᵢ - Σⱼ≠ᵢ aᵢⱼxⱼ^(k)) / aᵢᵢ
```

**Analog Implementation:**

```
       ┌──────────────────────────────────┐
       │                                  │
       ↓                                  │
bᵢ ────[SUM]────[÷aᵢᵢ]────[INT]────┬─── xᵢ
         ↑                         │
         │                         │
    (weighted sum of other xⱼ)─────┘
```

The integrator provides the iteration dynamics, with the system relaxing to the solution.

#### Gauss-Seidel Iteration

Similar to Jacobi but uses updated values immediately:
- Faster convergence
- Natural in analog (continuous update)

### Eigenvalue Problems

For eigenvalue λ and eigenvector v: Av = λv

**Power Iteration Method:**

```
       ┌──────────────────────────┐
       │                          │
       ↓                          │
v ────[A×]────[normalize]─────────┘

Converges to dominant eigenvector
Corresponding eigenvalue from Rayleigh quotient: λ = vᵀAv/vᵀv
```

## Applications

### 1. Resistive Networks

A network of resistors naturally solves Kirchhoff's equations:

```
     R₁       R₂       R₃
V₁ ─/\/\/─┬─/\/\/─┬─/\/\/─ V₂
          │       │
         /\/\    /\/\
          R₄      R₅
          │       │
         ─┴─     ─┴─
         GND     GND

Node voltages satisfy: GV = I
where G is conductance matrix
```

### 2. Spring Network Simulation

Mass-spring network dynamics:
```
M·ẍ + D·ẋ + K·x = F

Where K is stiffness matrix, D is damping matrix
```

### 3. Neural Network Forward Pass

Modern analog AI accelerators compute[^2]:
```
y = σ(Wx + b)

W: weight matrix
x: input vector
b: bias
σ: activation function
```

**Advantages:**
- O(1) time complexity (parallel)
- Very low energy
- Suitable for inference

## Modern Analog Linear Algebra

### Crossbar Arrays

Matrix-vector multiplication using resistor crossbar[^3]:

```
x₁ ────┬─────┬─────┬────
       │     │     │
       G₁₁   G₁₂   G₁₃
       │     │     │
x₂ ────┼─────┼─────┼────
       │     │     │
       G₂₁   G₂₂   G₂₃
       │     │     │
x₃ ────┼─────┼─────┼────
       │     │     │
       ↓     ↓     ↓
      y₁    y₂    y₃

yⱼ = Σᵢ Gᵢⱼ × xᵢ
```

- Each conductance Gᵢⱼ represents matrix element
- Input voltages represent vector x
- Output currents represent product y
- Single time step for any matrix size

### Memristor-Based Computing

Memristors enable programmable crossbar arrays:
- Conductance set by programming voltage
- Non-volatile (retains weight)
- Very compact (nanoscale possible)
- Basis for neuromorphic computing

## Limitations

### Accuracy

- Component tolerances: 0.1-1%
- Typical overall: 2-4 significant digits
- Not suitable for high-precision linear algebra

### Dynamic Range

- Limited to ±10V or similar
- Need careful scaling for large matrices
- Overflow possible with large products

### Scalability

- Wiring complexity grows as O(n²) for n×n matrix
- Practical limit: ~100×100 in traditional analog
- Modern IC: 1000×1000+ crossbars

## Summary

| Operation | Components Needed | Parallelism |
|-----------|-------------------|-------------|
| Vector add | n summers | Full |
| Dot product | n multipliers + 1 summer | Full |
| Matrix-vector | n×m pots + n summers | Full |
| Matrix multiply | Complex, many multipliers | Partial |
| Linear system (iterative) | Matrix multiply + integrators | Full |

## References

[^1]: [Analog Computing for Molecular Dynamics - arXiv](https://arxiv.org/pdf/2107.06283)
[^2]: [New analog quantum computers to solve previously unsolvable problems - Phys.org](https://phys.org/news/2023-01-analog-quantum-previously-unsolvable-problems.html)
[^3]: [Analog Computing - ScienceDirect Topics](https://www.sciencedirect.com/topics/engineering/analog-computer)

## Further Reading

- [Solving ODEs](03-ode-solving.md)
- [Applications: Engineering Problems](../04-applications/03-engineering-problems.md)
