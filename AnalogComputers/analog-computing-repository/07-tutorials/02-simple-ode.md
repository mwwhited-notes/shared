# Solving a Simple ODE

## Overview

This tutorial demonstrates solving a first-order ordinary differential equation using an analog computer circuit: the classic RC discharge problem.

## The Problem

### Differential Equation

```
dy/dt + y/τ = 0
```

With initial condition: y(0) = y₀

### Physical Interpretation

This represents:
- Capacitor discharge through resistor
- Radioactive decay
- Cooling (Newton's law)
- Many exponential decay processes

### Analytical Solution

```
y(t) = y₀ × e^(-t/τ)
```

Where τ = time constant

## Method 1: Direct RC Circuit (Passive)

### Circuit

The simplest analog solution—the equation IS the circuit:

```
         R
Vc(0) ──/\/\/──┬──── Vc(t)
               │
              ═╪═ C
               │
              ─┴─ GND
```

### How It Works

Kirchhoff's voltage law:
```
Vc = V_R = i × R
i = C × dVc/dt

Therefore: Vc = RC × dVc/dt
Rearranged: dVc/dt = -Vc/(RC)
```

This is exactly our equation with τ = RC!

### Building It

**Components:**
- 1× 100kΩ resistor
- 1× 10μF capacitor
- Voltage source for initial condition

**Time constant:** τ = RC = 100kΩ × 10μF = 1 second

**Procedure:**
1. Charge capacitor to y₀ (e.g., 10V)
2. Disconnect voltage source
3. Measure voltage decay with oscilloscope or voltmeter

**Expected Results:**
| Time (s) | Voltage (V) |
|----------|-------------|
| 0 | 10.0 |
| 1 (= τ) | 3.68 |
| 2 | 1.35 |
| 3 | 0.50 |
| 5 | 0.07 |

## Method 2: Op-Amp Integrator (Active)

### Why Use an Op-Amp?

- Precise control of time constant
- Ability to set initial conditions
- Can drive loads without affecting solution
- Extendable to more complex problems

### Reformulating the Equation

Rearrange: dy/dt = -y/τ

Block diagram:
```
         ┌───────────────────────┐
         │                       │
y ───────┤───[×(-1/τ)]───[∫dt]───┴─── y
         │                       ↑
         │                       │
         └───────────────────────┘
```

### Circuit Implementation

```
              C
         ┌────||────┐
         │          │
         │    ┌─────┤
         │    │     │
y ───────/\/\/┴────(-)──┐
          R             │
                  OP    ├── (-1/τ)∫y dt
                        │
           ┌───────(+)──┘
           │
          ─┴─ GND
```

**Wait—this produces the integral of y, not y itself!**

### Complete Circuit

We need to close the loop. The integrator output (-∫y/τ dt) becomes the new y:

```
              C
         ┌────||────┐
         │          │
         │   ┌──────┴───────────────────┐
         │   │                          │
──────/\/\/──┴────(-)──┐                │
    R                  │                │
                 OP    ├────────────────┴─── y
                       │
          ┌───────(+)──┘
          │
         ─┴─ GND

Note: Input and output are the same point!
```

**This is a single-integrator feedback loop.**

### With Initial Condition

```
              C
         ┌────||────┐
         │          │
         │ ┌────────┴──────────────────────┐
         │ │   S1 (IC/OP switch)           │
         │ │   ○                           │
         │ └───┤                           │
         │     │                           │
y₀ ──────┬─────●                           │
         │     (IC position)               │
         │                                 │
         ├───/\/\/──────(-)──┐             │
         │    R              │             │
         │             OP    ├─────────────┴─── y
         │                   │
         │      ┌───────(+)──┘
         │      │
         │     ─┴─ GND
         │
         └────────────────────────────────────
```

**Operation:**
1. **IC Mode:** S1 in IC position, capacitor charges to -y₀
2. **OP Mode:** S1 opens, system evolves, y decays exponentially

## Step-by-Step Build

### Components Needed

| Component | Value | Purpose |
|-----------|-------|---------|
| OP07 or OPA277 | - | Precision op-amp |
| Resistor R | 1MΩ | Sets time constant |
| Capacitor C | 1μF | Integration element |
| Switch | SPDT | Mode control |
| Pot | 10kΩ | IC voltage setting |
| Resistors | Various | IC voltage divider |

### Time Constant

τ = RC = 1MΩ × 1μF = 1 second

### Wiring Procedure

1. **Power the op-amp** (±12V, with decoupling)

2. **Build IC circuit:**
   - Connect pot between +10V and -10V
   - Pot wiper provides adjustable IC voltage

3. **Wire the integrator:**
   - R from summing junction to switch
   - C from summing junction to output
   - Summing junction to pin 2 (inverting input)
   - Pin 3 (non-inverting) to GND

4. **Connect switch:**
   - Center: summing junction
   - IC position: to pot wiper (through R)
   - OP position: open (or to y output for feedback)

5. **Close the loop:**
   - Connect output (pin 6) back through R to summing junction

### Testing

1. Set IC to +5V (pot adjustment)
2. Put switch in IC position
3. Wait for capacitor to charge
4. Flip to OP mode
5. Observe exponential decay on oscilloscope

### Expected Waveform

```
y(V)
  │
10├──●
  │   ╲
  │    ╲
  │     ╲
 5├──────●
  │       ╲
  │        ╲
  │         ╲__________
  │
  └────┬────┬────┬────── t(s)
       1    2    3

At t = τ = 1s: y = y₀/e ≈ 0.368 × y₀
```

## Extending to Forced Equations

### Adding Forcing Function

For: dy/dt + y/τ = f(t)

Add input to summer:
```
              C
         ┌────||────┐
         │          │
f(t) ────/\/\/──┬───┴────────┐
         Rf     │            │
                │            │
y ───────/\/\/──┴───(-)──┐   │
          R              │   │
                   OP    ├───┴─── y
                         │
            ┌───────(+)──┘
            │
           ─┴─ GND
```

### Step Response

If f(t) = step function:
- Solution approaches f×τ at steady state
- Time constant τ governs approach rate

## Common Issues

### Drift

**Symptom:** Output slowly drifts even with zero input
**Causes:** Op-amp offset, bias current
**Solutions:**
- Use precision op-amp (OP07)
- Add offset trim
- Use FET-input op-amp for low bias current

### Wrong Time Constant

**Symptom:** Decay too fast or slow
**Check:**
- Resistor value with multimeter
- Capacitor value (often off by 20%)
- Time scale on oscilloscope

### Oscillation

**Symptom:** Output oscillates instead of smooth decay
**Causes:** Poor layout, no decoupling, parasitic feedback
**Solutions:**
- Add decoupling capacitors
- Shorten wires
- Keep input/output separated

## Key Learnings

1. **Analog computers solve ODEs naturally** - physics does the math
2. **Initial conditions matter** - set before starting
3. **Time constant = RC** - easily adjustable
4. **Feedback creates the equation** - loop implements dy/dt = f(y)
5. **Precision requires care** - component selection matters

## Next Steps

- [Mass-Spring-Damper](03-mass-spring-damper.md) - Second-order ODE
- [Oscillators](04-oscillators.md) - Harmonic motion
- [Chaos and Attractors](05-chaos-attractors.md) - Nonlinear systems

## References

[^1]: [RC Time Constant - Wikipedia](https://en.wikipedia.org/wiki/RC_time_constant)
[^2]: [First-Order ODE - Wolfram MathWorld](https://mathworld.wolfram.com/OrdinaryDifferentialEquationFirstOrder.html)
[^3]: [Op-Amp Integrator - Electronics Tutorials](https://www.electronics-tutorials.ws/opamp/opamp_6.html)

## Further Reading

- [Integrators](../02-components/02-integrators.md)
- [ODE Solving](../03-mathematics/03-ode-solving.md)
- [Scaling](../01-fundamentals/05-scaling.md)
