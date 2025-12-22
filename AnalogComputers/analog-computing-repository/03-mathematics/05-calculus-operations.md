# Integration and Differentiation

## Overview

Integration and differentiation are the fundamental calculus operations in analog computing. The integrator is the workhorse of analog computers, while differentiation, though possible, is used more sparingly due to noise sensitivity.

## Mathematical Integration

### Definite Integration

Computing the area under a curve:
```
∫[a to b] f(t) dt
```

**Analog Implementation:**
1. Apply f(t) to integrator input
2. Set initial condition to 0 at t = a
3. Run until t = b
4. Read output = definite integral

### Indefinite Integration

Finding antiderivative F(t) where dF/dt = f(t):
```
F(t) = ∫ f(t) dt + C
```

**Analog Implementation:**
- Integrator with IC = C
- Output continuously represents F(t)

### Multiple Integration

```
∬ f(x,y) dx dy
```

**Implementation:** Chain integrators
```
f(x,y) ──[INT_x]── ∫f dx ──[INT_y]── ∬f dx dy
```

Requires careful management of variables and timing.

## Integration Applications

### Computing Area

```
       y
       │
       │    ┌────┐
       │    │    │
       │ ───┘    └───
       │
       └──────────────── t

y(t) ──[INT]── Area under curve
```

### Averaging

```
Average = (1/T) ∫[0 to T] f(t) dt
```

Use integrator followed by coefficient (1/T).

### Energy Computation

```
Energy = ∫ P(t) dt = ∫ v(t)·i(t) dt

v ──┬──[MULT]──[INT]── Energy
i ──┘
```

### RMS Calculation

```
RMS = √[(1/T) ∫[0 to T] f²(t) dt]

f(t) ──[SQR]──[INT]──[÷T]──[SQRT]── RMS
```

### Convolution

```
(f * g)(t) = ∫ f(τ)·g(t-τ) dτ
```

Complex but possible with time-shifting and multiplication.

## Mathematical Differentiation

### Basic Differentiation

```
df/dt = lim[Δt→0] [f(t+Δt) - f(t)] / Δt
```

**Analog Implementation:** Differentiator circuit
```
f(t) ──[DIFF]── df/dt
```

### Higher-Order Derivatives

```
f(t) ──[DIFF]── f'(t) ──[DIFF]── f''(t)
```

**Warning:** Each differentiation amplifies noise.

## Differentiation Applications

### Velocity from Position

```
x(t) ──[DIFF]── v(t) = dx/dt
```

### Rate of Change Detection

```
Signal ──[DIFF]── Rate of change
                  (detects rapid changes)
```

### Edge Detection

Differentiating a step produces an impulse at the edge.

## Avoiding Differentiation

### Why Avoid?

1. **Noise amplification**: High-frequency noise is amplified
2. **Instability**: Differentiators can oscillate
3. **Limited bandwidth**: Must be bandwidth-limited for stability
4. **Lower accuracy**: Compared to integration

### Alternative: Work Backward from Integral

If you need f'(t), but have f(t):

**Instead of:**
```
f(t) ──[DIFF]── f'(t)
```

**Restructure problem so:**
```
f'(t) ──[INT]── f(t)
```

Then f'(t) is available as an intermediate signal.

### Example: Second-Order System

**Need:** velocity v = dx/dt from position x

**Wrong approach:**
```
x ──[DIFF]── v     (noisy!)
```

**Better approach (restructure):**
```
Formulate as: dv/dt = f(...)
              dx/dt = v

v ──[INT]── x
↑
(v is directly available, no differentiation needed)
```

## Numerical Differentiation Analog

### Backward Difference

```
f'(t) ≈ [f(t) - f(t-Δt)] / Δt
```

**Implementation with delay:**
```
f(t) ────────────┬──[SUM]──[×1/Δt]── f'(t) approx
                 │
f(t) ──[DELAY]───┘
```

Delay can be implemented with:
- Analog delay line
- Sample-and-hold
- Digital delay (hybrid)

### Central Difference

```
f'(t) ≈ [f(t+Δt) - f(t-Δt)] / (2Δt)
```

Requires prediction (not causal) or two delays.

## Integration Techniques

### Track-and-Hold Integration

For repeated measurements:
```
1. Integrate signal
2. Hold result
3. Read value
4. Reset integrator
5. Repeat
```

### Gated Integration

Integrate only during specified window:
```
                 ┌──────────┐
Signal ──────────┤  ×       ├──[INT]── Gated integral
                 │          │
Gate ────────────┤ (switch) │
                 └──────────┘
```

### Charge-Balancing Integration

High-precision integration using feedback:
```
               ┌─────────────────────┐
               │                     │
Signal ────────┼──[INT]──[COMP]──────┤
               │           │         │
               │    ┌──────┘         │
               │    │                │
Pulse out ◄────┼────┤                │
               │    │                │
               │   [±Ref]────────────┘
               │
               └─────────────────────
```

Number of pulses proportional to integral.

## Practical Integrator Accuracy

### Sources of Error

| Error Source | Magnitude | Effect |
|--------------|-----------|--------|
| Input offset | 1-10 mV | Ramp drift |
| Bias current | 1-100 nA | Ramp drift |
| Capacitor leakage | 0.1-1%/min | Discharge |
| Dielectric absorption | 0.01-1% | Memory effect |
| Temperature | 50-500 ppm/°C | Gain change |

### Long-Term Integration

For integration over minutes/hours:
- Use low-leakage capacitors (Teflon, polypropylene)
- Use FET-input op-amps (low bias current)
- Provide periodic reset/recalibration
- Consider digital assist (hybrid)

### Short-Term Integration

For integration over microseconds/milliseconds:
- Standard components adequate
- Watch for bandwidth limitations
- Slew rate may limit high-frequency content

## Summary Table

| Operation | Component | Advantages | Disadvantages |
|-----------|-----------|------------|---------------|
| Integration | Integrator | Low noise, stable | Drift, requires IC |
| Differentiation | Differentiator | Direct | Noisy, unstable |
| Numerical diff | Delay + subtractor | Less noisy | Requires delay element |
| Avoided diff | Restructure | Best accuracy | Requires problem reformulation |

## Best Practices

### For Integration
1. Use quality capacitors (low leakage, low DA)
2. Choose appropriate time constant for signal bandwidth
3. Provide means to set initial conditions
4. Include reset capability for repetitive operation
5. Consider drift compensation for long integrations

### For Differentiation
1. Always include high-frequency roll-off
2. Filter input signal if noisy
3. Limit maximum gain
4. Consider restructuring problem to avoid
5. Use only when absolutely necessary

## References

[^1]: [Integration - Wikipedia](https://en.wikipedia.org/wiki/Integral)
[^2]: [Analog Integration Techniques - Analog Devices](https://www.analog.com/media/en/training-seminars/tutorials/MT-049.pdf)
[^3]: [Op-Amp Integrator - Electronics Tutorials](https://www.electronics-tutorials.ws/opamp/opamp_6.html)
[^4]: Korn, Granino A. and Korn, Theresa M. *Electronic Analog and Hybrid Computers*. McGraw-Hill, 1972.

## Further Reading

- [Integrators](../02-components/02-integrators.md)
- [Differentiators](../02-components/03-differentiators.md)
- [Solving ODEs](03-ode-solving.md)
