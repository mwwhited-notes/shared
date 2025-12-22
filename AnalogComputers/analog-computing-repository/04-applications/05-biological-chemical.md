# Biological and Chemical Systems

## Overview

Biological and chemical systems often involve complex nonlinear dynamics, multiple interacting species, and varying time scales—characteristics well-suited to analog computer simulation.

## Population Dynamics

### Exponential Growth

```
dN/dt = r·N
```

Solution: N(t) = N₀·e^(rt)

**Analog:**
```
       ┌─────────────────────┐
       │                     │
       ↓                     │
N₀ ──[INT]──[×r]──────┬── N(t)
       ↑              │
       │              │
       └──────────────┘
```

### Logistic Growth

```
dN/dt = r·N·(1 - N/K)
```

Where K = carrying capacity

**Implementation:**
```
N ──┬──[×r]──[MULT]──[INT]── N
    │           ↑
    │           │
    └──[1 - N/K]┘
```

### Lotka-Volterra (Predator-Prey)[^1]

```
dx/dt = αx - βxy     (prey)
dy/dt = δxy - γy     (predator)
```

**Classic analog computer demonstration**

**Block diagram:**
```
PREY (x):
    ┌──────────────────────────────────────┐
    │                                      │
x ──┼──[×α]──┐                             │
    │        ├──[SUM]──[INT]──┬── x        │
    │  ┌──[MULT]──[×−β]───────┘   │        │
    │  │    ↑                     │        │
    │  │    │                     │        │
    │  └────┼─────────────────────┼────────┤
    │       │                     │        │
y ──────────┘                     │        │
                                  │        │
                   ┌──────────────┘        │
                   │                       │
                   └───────────────────────┘

PREDATOR (y):
Similar structure with δxy - γy
```

**Behavior:**
- Periodic oscillations
- Phase-shifted populations
- Displayed on X-Y plotter: closed orbits

### Competition Model

```
dN₁/dt = r₁N₁(1 - N₁/K₁ - α₁₂N₂/K₁)
dN₂/dt = r₂N₂(1 - N₂/K₂ - α₂₁N₁/K₂)
```

Competition coefficients α₁₂, α₂₁ determine outcome.

## Epidemiology

### SIR Model

```
dS/dt = -βSI
dI/dt = βSI - γI
dR/dt = γI
```

Where:
- S = Susceptible
- I = Infected
- R = Recovered
- β = infection rate
- γ = recovery rate

**Implementation:**
```
S ──┬──[MULT]──[×−β]──[INT]── S
    │    ↑
I ──┴────┘
    │
    └──[MULT]──[×β]──┐
         ↑           ├──[SUM]──[INT]── I
I ──────────────────[×−γ]──────┘
         │
         └──────[×γ]──[INT]── R
```

**Basic reproduction number:** R₀ = β/γ

### SIS Model (Endemic)

```
dS/dt = -βSI + γI
dI/dt = βSI - γI
```

No permanent immunity; can reach endemic equilibrium.

### SEIR Model

Adds Exposed (latent) compartment:
```
S → E → I → R
```

Four coupled equations.

## Enzyme Kinetics

### Michaelis-Menten

```
E + S ⇌ ES → E + P
```

Quasi-steady-state:
```
v = Vmax·[S]/(Km + [S])
```

**Full dynamics:**
```
d[S]/dt = -k₁[E][S] + k₋₁[ES]
d[ES]/dt = k₁[E][S] - k₋₁[ES] - k₂[ES]
d[P]/dt = k₂[ES]
[E] + [ES] = [E]₀ (conservation)
```

### Enzyme Inhibition

**Competitive:**
```
v = Vmax·[S]/(Km(1 + [I]/Ki) + [S])
```

**Non-competitive:**
```
v = Vmax·[S]/((Km + [S])(1 + [I]/Ki))
```

## Chemical Reaction Networks

### First-Order Reaction

```
A → B

d[A]/dt = -k[A]
d[B]/dt = k[A]
```

Simple integrator with feedback.

### Second-Order Reaction

```
A + B → C

d[A]/dt = -k[A][B]
d[B]/dt = -k[A][B]
d[C]/dt = k[A][B]
```

Requires multiplier for [A][B] term.

### Reversible Reaction

```
A ⇌ B
    k₁
    k₋₁

d[A]/dt = -k₁[A] + k₋₁[B]
d[B]/dt = k₁[A] - k₋₁[B]
```

Reaches equilibrium: [B]/[A] = k₁/k₋₁

### Oscillating Reactions

**Brusselator:**
```
d[X]/dt = A - (B+1)[X] + [X]²[Y]
d[Y]/dt = B[X] - [X]²[Y]
```

Can exhibit limit cycle oscillations.

**Oregonator (BZ reaction model):**
```
d[X]/dt = k₁[A][Y] - k₂[X][Y] + k₃[A][X] - 2k₄[X]²
d[Y]/dt = -k₁[A][Y] - k₂[X][Y] + f·k₅[B][Z]
d[Z]/dt = k₃[A][X] - k₅[B][Z]
```

Models the famous Belousov-Zhabotinsky reaction.

## Pharmacokinetics

### One-Compartment Model

```
dC/dt = -k·C + D(t)/V

Where:
C = concentration
k = elimination rate
D(t) = dosing function
V = volume of distribution
```

### Two-Compartment Model

```
dC₁/dt = -(k₁₂ + k₁₀)C₁ + k₂₁C₂ + D(t)/V₁
dC₂/dt = k₁₂C₁ - k₂₁C₂
```

Central and peripheral compartments.

### Repeated Dosing

Pulse train input D(t) for multiple doses:
```
D(t) = Σ D₀·δ(t - n·τ)
```

Analog: Periodic reset of initial conditions

## Neuroscience

### Hodgkin-Huxley Model

Action potential generation:
```
C_m·dV/dt = -g_Na·m³h(V - E_Na) - g_K·n⁴(V - E_K) - g_L(V - E_L) + I

dm/dt = α_m(V)(1-m) - β_m(V)m
dh/dt = α_h(V)(1-h) - β_h(V)h
dn/dt = α_n(V)(1-n) - β_n(V)n
```

**Highly nonlinear:** Rate functions α, β are exponentials of voltage.

### FitzHugh-Nagumo (Simplified)

```
dv/dt = v - v³/3 - w + I
dw/dt = ε(v + a - bw)
```

Reduced model capturing essential dynamics.

### Neural Network

Simple neural oscillator:
```
τ·dx_i/dt = -x_i + Σw_ij·σ(x_j) + I_i
```

Where σ is sigmoid activation function.

## Gene Regulation

### Repressilator

Three-gene oscillator:
```
dm_i/dt = -m_i + α/(1 + p_j^n) + α₀
dp_i/dt = -β(p_i - m_i)
```

Where gene i is repressed by protein j (in cycle).

### Toggle Switch

Bistable genetic switch:
```
du/dt = α₁/(1 + v^β) - u
dv/dt = α₂/(1 + u^γ) - v
```

Two stable states (high-u/low-v or low-u/high-v).

## Ecological Models

### Food Chain

```
dx/dt = x(1 - x) - a·xy/(1 + bx)
dy/dt = a·xy/(1 + bx) - c·y - d·yz/(1 + ey)
dz/dt = d·yz/(1 + ey) - f·z
```

Three trophic levels with saturating functional responses.

### Spatial Ecology (Reaction-Diffusion)

```
∂u/∂t = D_u·∇²u + f(u,v)
∂v/∂t = D_v·∇²v + g(u,v)
```

Turing patterns, traveling waves.
Implemented with spatial discretization.

## Practical Considerations

### Time Scaling

| Biological Process | Time Scale | Analog Scaling |
|-------------------|------------|----------------|
| Action potential | 1-10 ms | Real-time or slower |
| Enzyme reaction | ms-s | Real-time |
| Cell cycle | hours | Speed up 1000× |
| Population dynamics | years | Speed up 10⁶× |
| Evolution | millions of years | Impractical |

### Stiffness

Many biological systems are stiff:
- Fast reactions + slow reactions
- May require time-scale separation
- Or variable time scaling

### Parameter Sensitivity

Biological parameters often uncertain:
- Analog allows interactive exploration
- Quick sensitivity analysis
- Find robust regions

## References

[^1]: [Analog Computer - Wikipedia: Biological Models](https://en.wikipedia.org/wiki/Analog_computer)

## Further Reading

- [Nonlinear Equations](../03-mathematics/06-nonlinear-equations.md)
- [ODE Solving](../03-mathematics/03-ode-solving.md)
- [Chaos and Attractors](../07-tutorials/05-chaos-attractors.md)
