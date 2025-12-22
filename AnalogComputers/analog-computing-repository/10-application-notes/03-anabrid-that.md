# Anabrid THE ANALOG THING (THAT) Documentation

## Overview

THE ANALOG THING (THAT) is a high-quality, low-cost, open-source analog computer developed by anabrid GmbH in Germany. It is designed for education, experimentation, and demonstrating analog computing principles.

**Official Resources:**
- Main Website: [https://the-analog-thing.org/](https://the-analog-thing.org/)
- Documentation: [https://the-analog-thing.org/docs/dirhtml/](https://the-analog-thing.org/docs/dirhtml/)
- First Steps Guide: [https://the-analog-thing.org/THAT_First_Steps.pdf](https://the-analog-thing.org/THAT_First_Steps.pdf)
- Wiki: [https://the-analog-thing.org/wiki/](https://the-analog-thing.org/wiki/)
- GitHub: [https://github.com/anabrid/the-analog-thing](https://github.com/anabrid/the-analog-thing)

## THAT Specifications

| Feature | Specification |
|---------|---------------|
| Integrators | 5 |
| Summers | 4 (8 inputs total) |
| Multipliers | 2 |
| Inverters | 4 |
| Comparators | 2 |
| Coefficient Potentiometers | 10 |
| Power Supply | USB or external ±15V |
| Reference Voltage | ±1 (machine unit) |
| Form Factor | Compact desktop |
| Design | Open source hardware |

## Computing Elements

### Integrators

THAT includes 5 integrators with:
- Selectable time constants
- Initial condition setting
- Mode control (IC/OP/HALT)

```
      [τ selector]
           │
Input ────[∫]──── Output
           │
      [IC setting]
```

### Summers

4 summing amplifiers, each with 2 inputs:
- Unity gain summing
- Can cascade for more inputs

```
In1 ──┐
      ├──[Σ]──── -(In1 + In2)
In2 ──┘
```

### Multipliers

2 four-quadrant multipliers:
- Based on AD633 or equivalent
- Scale factor of 1 (machine unit based)

```
X ──┐
    ├──[×]──── X × Y
Y ──┘
```

### Coefficient Potentiometers

10 precision potentiometers for setting coefficients:
- Range: 0 to 1
- Used for equation constants
- Dial markings for approximate setting

### Comparators

2 comparators for:
- Zero-crossing detection
- Logic-level signals
- Triggering events

## Getting Started with THAT

### Step 1: Power Connection

Connect via USB or external power supply:
- USB provides both power and ground
- External supply: ±15V DC

### Step 2: Understand the Panel

```
┌─────────────────────────────────────────────────────────────┐
│  THE ANALOG THING                                           │
│                                                             │
│  [INT1] [INT2] [INT3] [INT4] [INT5]     INTEGRATORS        │
│                                                             │
│  [SUM1] [SUM2] [SUM3] [SUM4]            SUMMERS            │
│                                                             │
│  [MLT1] [MLT2]                          MULTIPLIERS        │
│                                                             │
│  [P1] [P2] [P3] [P4] [P5]               COEFFICIENT POTS   │
│  [P6] [P7] [P8] [P9] [P10]                                 │
│                                                             │
│  [INV1] [INV2] [INV3] [INV4]            INVERTERS          │
│                                                             │
│  [COMP1] [COMP2]                        COMPARATORS        │
│                                                             │
│  MODE: [IC] [OP] [HALT]                 CONTROL            │
│                                                             │
│  ●●●●●●●●●●●●●●●●●●●●●●●●●●●●           PATCH FIELD        │
└─────────────────────────────────────────────────────────────┘
```

### Step 3: Patching Basics

Use patch cables to connect:
- Computing element outputs to inputs
- Potentiometer outputs to element inputs
- Reference voltages as needed

## Example: Simple Harmonic Oscillator

Implement: d²x/dt² + ω²x = 0

### Block Diagram

```
      ┌─────────────────────────────────────┐
      │                                     │
      ↓                                     │
  ┌──[−ω²]──[INT1]────[INT2]────┬───────────┘
  │                             │
  └───────── x output ──────────┘
```

### THAT Implementation

1. **Set coefficient** P1 to ω² value
2. **Connect** INT2 output → P1 → INT1 input
3. **Connect** INT1 output → INT2 input
4. **Set initial conditions:**
   - INT1: 0 (zero velocity)
   - INT2: desired amplitude (initial displacement)
5. **Connect oscilloscope** to INT2 output
6. **Switch to OP mode** and observe sinusoidal oscillation

### Frequency Adjustment

- Frequency depends on ω² (P1 setting) and time constants
- Adjust P1 to change frequency
- Real-time tuning while observing output

## Example: Lorenz Attractor

The Lorenz system:
```
dx/dt = σ(y - x)
dy/dt = x(ρ - z) - y
dz/dt = xy - βz
```

### Using THAT's Resources

- 3 integrators (INT1, INT2, INT3) for x, y, z
- 2 multipliers for xz and xy terms
- Coefficient pots for σ, ρ, β
- Summers to combine terms

### Detailed Patching

See the official THAT documentation for complete patching diagrams:
[THAT Lorenz Example](https://the-analog-thing.org/wiki/Lorenz)

## Visualization

### Oscilloscope Connection

Connect THAT outputs to oscilloscope:
- X-Y mode for phase portraits
- Time mode for waveforms
- Use multiple channels for different variables

### Recommended Settings

- DC coupling
- Appropriate voltage scale (typically 1-5 V/div)
- Triggering on one channel for stable display

## THAT vs. Traditional Analog Computers

| Feature | THAT | Traditional |
|---------|------|-------------|
| Size | Desktop | Room-sized |
| Cost | ~$350 | $10,000+ |
| Integrators | 5 | 20-100+ |
| Precision | Educational | Professional |
| Power | USB/±15V | Dedicated supply |
| Patching | Compact | Full patch panel |

## Additional Resources

### Analog Paradigm Application Notes

The Analog Paradigm Model-1 application notes are also applicable:
[https://analogparadigm.com/documentation.html](https://analogparadigm.com/documentation.html)

Topics include:
- Solving differential equations
- Chaos and attractors
- Physical simulations
- Mathematical operations

### GitHub Repositories

- **THAT Hardware**: [https://github.com/anabrid/the-analog-thing](https://github.com/anabrid/the-analog-thing)
- **THAT Documentation**: [https://github.com/anabrid/the-analog-thing-docs](https://github.com/anabrid/the-analog-thing-docs)
- **Model-1 App Notes**: [https://github.com/anabrid/Model-1/tree/main/application_notes](https://github.com/anabrid/Model-1/tree/main/application_notes)

### Community

- Contact: hello@anabrid.com
- Help Desk: [https://helpdesk.anabrid.com/](https://helpdesk.anabrid.com/)

## Tips for Using THAT

1. **Start simple**: Begin with first-order equations before attempting chaos
2. **Check signs**: Most errors come from wrong sign in feedback
3. **Observe scaling**: Keep signals within ±1 machine unit
4. **Use the wiki**: Many example circuits available
5. **Document your patches**: Take photos of successful setups

## Comparison with DIY Approaches

| Aspect | THAT | DIY |
|--------|------|-----|
| Ready to use | Yes | No |
| Calibration | Factory | Required |
| Documentation | Extensive | Self-made |
| Support | Available | Community |
| Expandability | Limited | Unlimited |
| Learning depth | Good | Excellent |

THAT is ideal for learning and demonstration, while DIY projects offer deeper understanding of circuit design.

## References

1. anabrid GmbH, "THE ANALOG THING First Steps Guide," 2023.
2. anabrid GmbH, "THAT Online Documentation."
3. Ulmann, Bernd, "Analog Computing," Oldenbourg Wissenschaftsverlag, 2013.

