# THE Analog Thing (THAT)

## Overview

THE Analog Thing (THAT) is a modern, open-source, educational analog computer designed and manufactured by anabrid GmbH in Germany. It represents a revival of interest in analog computing for education and experimentation[^1][^2].

## Background

### Development

- **2020:** Founded by Dr. Bernd Ulmann and colleagues
- **2021:** Production begins
- **2024:** Received iF Design Award and Red Dot Prize
- **Available worldwide:** ~$300-350 including shipping

### Philosophy

- **Open-source:** Design files publicly available
- **Not-for-profit:** Educational pricing
- **Hands-on:** Learn by doing
- **Accessible:** Low cost, high quality

## Specifications

### Computing Elements

| Component | Quantity | Function |
|-----------|----------|----------|
| Integrators | 5 | Integration with IC setting |
| Summers | 4 | Weighted addition |
| Inverters | 4 | Sign inversion |
| Multipliers | 2 | Analog multiplication |
| Comparators | 2 | Threshold detection |
| Coefficient pots | 8 | 10-turn precision |

### Technical Specifications

```
Power supply: External ±15V DC
Machine unit: ±10V
Accuracy: ~0.1% (1% pots, op-amp limited)
Bandwidth: DC to ~100kHz
Dimensions: 200mm × 140mm × 40mm
Weight: ~500g
```

### Connectors

- **Patch panel:** 2mm banana jacks
- **Hybrid port:** Digital interface (GPIO, SPI)
- **BNC outputs:** For oscilloscope connection
- **Power:** Standard barrel connector

## Block Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                       THAT ANALOG THING                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  INTEGRATORS (5)           SUMMERS (4)         INVERTERS   │
│  ┌───┐ ┌───┐ ┌───┐ ┌───┐  ┌───┐ ┌───┐ ┌───┐   ┌───┐ ┌───┐ │
│  │∫1 │ │∫2 │ │∫3 │ │∫4 │  │Σ1 │ │Σ2 │ │Σ3 │   │-1 │ │-1 │ │
│  └─●─┘ └─●─┘ └─●─┘ └─●─┘  └─●─┘ └─●─┘ └─●─┘   └─●─┘ └─●─┘ │
│    │     │     │     │      │     │     │       │     │   │
│                                                             │
│  MULTIPLIERS (2)        COMPARATORS (2)                     │
│  ┌───┐ ┌───┐           ┌───┐ ┌───┐                         │
│  │×1 │ │×2 │           │CMP│ │CMP│                         │
│  └─●─┘ └─●─┘           └─●─┘ └─●─┘                         │
│                                                             │
│  COEFFICIENT POTS (8)                                       │
│  [0-1] [0-1] [0-1] [0-1] [0-1] [0-1] [0-1] [0-1]           │
│                                                             │
│  MODE CONTROL                                               │
│  [IC/OP/HALT]  [REP]  [SLOW/FAST]                          │
│                                                             │
│  REFERENCES: +1, -1, GND                                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Operating Modes

### IC (Initial Condition)

- Integrators hold at set IC values
- System paused
- Used for setting starting conditions

### OP (Operate)

- Integrators integrate
- System computing
- Observe solution evolution

### HALT

- Integrators hold current values
- System frozen at current state
- Useful for observation/measurement

### REP (Repetitive)

- Automatic IC → OP → IC cycling
- Creates repeating display on oscilloscope
- Adjustable cycle rate

## Integrator Details

### Initial Condition Setting

```
          IC Input
              │
              ▼
    ┌─────────────────┐
    │   S1 (IC/OP)    │
    │       ○         │
    │       │         │
    │      ═╪═ C      │
    │       │         │
SJ  │       │         │ ← Summing junction
────┼───────┤         │
    │       │         │
    │  ┌────┴──(-)──┐ │
    │  │            │ │
    │  │   OP-AMP   ├─┼── Output
    │  │            │ │
    │  └───────(+)──┘ │
    │          │      │
    │          ▼      │
    │         GND     │
    └─────────────────┘
```

### Time Constant

THAT uses τ = 100μs (fast) or 1ms (slow) selectable:
- **SLOW:** 10ms time constant (k₀ = 10⁴)
- **FAST:** 1ms time constant (k₀ = 10³)

## Example Problems

### Harmonic Oscillator

```
d²x/dt² + ω²x = 0
```

**Patching:**
```
1. Connect INT1 output to INT2 input (positive)
2. Connect INT2 output through pot (set to ω²) to summer
3. Connect summer through inverter to INT1 input
4. Set ICs (position, velocity)
5. Run in REP mode
6. Observe sinusoidal output
```

### Van der Pol Oscillator

```
d²x/dt² - μ(1-x²)·dx/dt + x = 0
```

**Requires:** Both multipliers for the x²·dx/dt term

### Lorenz Attractor

```
dx/dt = σ(y - x)
dy/dt = x(ρ - z) - y
dz/dt = xy - βz
```

**Note:** Requires 3 integrators, 2 multipliers - within THAT's capability

## Hybrid Operation

### Digital Interface

THAT includes a hybrid connector for:
- Digital mode control
- Reading comparator outputs
- External timing signals
- Microcontroller integration (Arduino, Raspberry Pi)

### Example: Microcontroller + THAT

```
Arduino              THAT
   │                  │
   │───[Mode Control]─│── IC/OP/HALT
   │                  │
   │◄──[Comparator]───│── Event detection
   │                  │
   │───[DAC (ext)]────│── Coefficient setting
   │                  │
```

## Chaining Multiple THATs

For larger problems:
- Daisy-chain power and control
- Connect outputs to inputs between units
- Expandable computing power

**Example:** 2 THATs = 10 integrators, 4 multipliers

## Educational Applications

### Typical Courses

1. **Differential Equations**
   - Visualize solutions
   - Parameter variation studies

2. **Control Systems**
   - Feedback dynamics
   - Stability analysis

3. **Physics**
   - Oscillations
   - Chaos theory
   - Coupled systems

4. **Electrical Engineering**
   - Circuit analogs
   - Filter design

### Learning Outcomes

- Understand ODEs intuitively
- Experience real-time computation
- Connect math to physical systems
- Hands-on circuit skills

## Resources

### Official Documentation

- [THAT Website](https://the-analog-thing.org/)
- [Online Documentation](https://the-analog-thing.org/docs/)
- [First Steps Guide](https://the-analog-thing.org/THAT_First_Steps.pdf)

### Community

- Forums and discussion groups
- User-contributed examples
- Open-source software tools

### Accessories

- Patch cord sets
- External power supply
- Storage case
- Companion oscilloscope recommendations

## Getting Started Checklist

1. ☐ Obtain THAT and power supply
2. ☐ Read First Steps documentation
3. ☐ Connect oscilloscope or PC interface
4. ☐ Build first circuit (harmonic oscillator)
5. ☐ Experiment with damping, forcing
6. ☐ Try more complex examples
7. ☐ Design your own problems

## References

[^1]: [THE Analog Thing - Official Website](https://the-analog-thing.org/)
[^2]: [IEEE Spectrum - Try This New Analog Computer](https://spectrum.ieee.org/try-this-new-analog-computer)

## Further Reading

- [Modern Op-Amps](02-modern-op-amps.md)
- [DIY Projects](03-diy-projects.md)
- [Tutorials](../07-tutorials/)
