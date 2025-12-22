# DIY Analog Computer Projects

## Overview

Building your own analog computer is an excellent way to learn about analog computing, electronics, and differential equations. This guide provides projects ranging from simple circuits to complete systems.

## Basic Building Blocks

### Project 1: Op-Amp Inverter

**Difficulty:** Beginner
**Components:**
- 1× TL071 or 741 op-amp
- 2× 10kΩ resistors (1%)
- ±12V power supply
- Breadboard

**Circuit:**
```
           10kΩ
      ┌────/\/\/────┐
      │             │
Vin ──/\/\/────────(-)──┐
       10kΩ             │
                  TL071 ├── Vout = -Vin
                        │
           ┌───────(+)──┘
           │
          ─┴─ GND
```

**Test:** Apply +5V, measure -5V output

### Project 2: Summing Amplifier

**Difficulty:** Beginner
**Components:**
- 1× TL074 (quad op-amp)
- 4× 10kΩ resistors

**Circuit:**
```
             10kΩ
        ┌────/\/\/────┐
        │             │
V1 ─────/\/\/────┬───(-)──┐
        10kΩ     │        │
                 │  TL074 ├── Vout = -(V1 + V2 + V3)
V2 ─────/\/\/────┤        │
        10kΩ     │        │
                 │   ┌───(+)
V3 ─────/\/\/────┘   │
        10kΩ        ─┴─ GND
```

### Project 3: Basic Integrator

**Difficulty:** Beginner-Intermediate
**Components:**
- 1× OP07 (precision op-amp)
- 1× 100kΩ resistor
- 1× 1μF film capacitor
- 1× 10MΩ resistor (for DC stability)
- 1× SPDT switch (for reset)

**Circuit:**
```
                    1μF
               ┌────||────┐
               │          │
               │   10MΩ   │
               ├──/\/\/───┤
               │          │
Vin ───/\/\/───┼─────────(-)──┐
       100kΩ   │              │
               │        OP07  ├── Vout
               │              │
               │    ┌─────(+)─┘
               │    │
        Reset ─┴────┴─ GND (connect to IC voltage for reset)
```

**Time constant:** τ = RC = 100kΩ × 1μF = 0.1s

## Intermediate Projects

### Project 4: Simple Harmonic Oscillator

**Difficulty:** Intermediate
**Goal:** Implement d²x/dt² + ω²x = 0

**Components:**
- 2× OP07 or OPA277 (precision op-amps)
- 4× 100kΩ resistors
- 2× 1μF film capacitors
- 1× 10kΩ pot (for ω² adjustment)
- 2× momentary switches (reset)

**Block Diagram:**
```
         ┌─────────────────────────────────┐
         │                                 │
         ↓                                 │
    ┌────[−ω²]────[INT1]────[INT2]────┬────┘
    │                                 │
    └────────(output x)───────────────┘
```

**Expected Output:** Sinusoidal oscillation

### Project 5: Damped Oscillator

**Difficulty:** Intermediate
**Equation:** d²x/dt² + 2ζω·dx/dt + ω²x = 0

**Additional Components:**
- 1× additional pot (for damping ζ)
- 1× additional summer input

**Modification:** Add feedback from INT1 output (velocity) with damping coefficient.

**Behavior:**
- ζ < 1: Underdamped (oscillates and decays)
- ζ = 1: Critically damped
- ζ > 1: Overdamped

### Project 6: Function Generator

**Difficulty:** Intermediate

**Produces:** Triangle and square waves

**Components:**
- 2× op-amps (1 integrator, 1 Schmitt trigger)
- Resistors, capacitors

**Circuit Concept:**
```
         ┌────────────────────────┐
         │                        │
    ┌────[INT]────[Schmitt]───────┘
    │                │
    │                └── Square wave out
    │
    └── Triangle wave out
```

## Advanced Projects

### Project 7: Complete Analog Computer Module

**Difficulty:** Advanced

**Specifications:**
- 4 integrators with IC setting
- 2 summers (4 inputs each)
- 2 inverters
- 8 coefficient pots
- Mode control (IC/OP/HALT)

**Suggested Layout:**
```
┌─────────────────────────────────────────────────────────┐
│   INTEGRATORS                    SUMMERS                │
│   [INT1] [INT2] [INT3] [INT4]   [SUM1] [SUM2]          │
│                                                         │
│   INVERTERS          COEFFICIENT POTS                   │
│   [INV1] [INV2]     [P1][P2][P3][P4][P5][P6][P7][P8]   │
│                                                         │
│   MODE: [IC] [OP] [HALT]     REFERENCES: [+10V] [-10V] │
│                                                         │
│   ●●●●●●●●●●●●●●●●●●●● PATCH PANEL ●●●●●●●●●●●●●●●●●●● │
└─────────────────────────────────────────────────────────┘
```

### Project 8: Multiplier Circuit

**Difficulty:** Advanced

**Option A: Using AD633 IC**
```
                ┌────────────────────┐
                │                    │
   X1 ──────────┤ X1            OUT ├──┬── W = (X1-X2)(Y1-Y2)/10 + Z
                │              (+V) ├──│
   X2 ──────────┤ X2      AD633     │  │
                │                   │  │
   Y1 ──────────┤ Y1           (-V)├──┘
                │                   │
   Y2 ──────────┤ Y2             Z ├─── GND
                │                   │
                └───────────────────┘
```

**Option B: Discrete log-antilog multiplier** (more complex)

### Project 9: Lorenz Attractor

**Difficulty:** Advanced

**Equations:**
```
dx/dt = σ(y - x)
dy/dt = x(ρ - z) - y
dz/dt = xy - βz
```

**Requirements:**
- 3 integrators
- 2 multipliers
- Multiple summers
- 4+ coefficient pots

**Parameters:** σ = 10, ρ = 28, β = 8/3

**Output:** Connect x, y, z to oscilloscope in X-Y mode for strange attractor visualization.

## PCB-Based Projects

### Project 10: Modular Analog Computer PCB

**Design a PCB with:**
- Standard module format
- Stackable/chainable design
- Edge connectors for patching
- Precision components

**Suggested Module Types:**
1. Integrator module (2 integrators)
2. Summer module (2 summers)
3. Multiplier module (1 multiplier)
4. Coefficient module (4 pots)
5. Control module (mode switching)

### Using KiCad or EasyEDA

**Design tips:**
- Ground plane for noise reduction
- Separate analog and digital grounds
- Low-impedance power distribution
- Test points for debugging

## Software Simulation First

### SPICE Simulation

Before building, simulate with:
- LTspice (free, excellent)
- TINA-TI (free, TI parts)
- Multisim (educational licenses)

**Benefits:**
- Verify circuit before building
- Test scaling
- Identify problems early

### Online Simulators

- Falstad Circuit Simulator (falstad.com/circuit)
- EveryCircuit (mobile app)
- CircuitLab (web-based)

## Component Sources

### Recommended Suppliers

| Supplier | Specialty |
|----------|-----------|
| Digi-Key | Wide selection, specs |
| Mouser | Professional parts |
| Newark | Industrial components |
| Amazon/eBay | Budget options |
| Tayda Electronics | Low-cost passives |

### Essential Components List

**Op-Amps:**
- TL074 (general, quad)
- OP07 (precision, single)
- OPA2277 (precision, dual)

**Resistors:**
- 1% metal film, 1/4W
- Values: 1kΩ, 10kΩ, 100kΩ, 1MΩ

**Capacitors:**
- Film/polypropylene (integrators)
- Ceramic (decoupling)
- Values: 100nF, 1μF, 10μF

**Potentiometers:**
- 10-turn, 10kΩ (precision coefficients)
- Single-turn, 10kΩ (adjustments)

**Connectors:**
- 2mm banana jacks
- Pin headers
- BNC connectors

## Testing and Calibration

### Basic Tests

1. **Power supply check:** Verify ±12V (or ±15V)
2. **Offset trim:** Adjust for zero output with zero input
3. **Gain verification:** Apply known input, verify output
4. **Frequency response:** Check bandwidth with function generator

### Calibration Procedure

1. Apply precision reference voltage
2. Adjust offset trimmers to minimize error
3. Verify integrator time constant
4. Check coefficient pot linearity
5. Document any deviations

## Safety Considerations

- Low voltages (±15V max) - generally safe
- Capacitors can hold charge - discharge before working
- Use power supply current limiting
- Don't exceed op-amp ratings

## References

[^1]: [LTspice - Analog Devices](https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html)
[^2]: [Falstad Circuit Simulator](https://www.falstad.com/circuit/)
[^3]: Ulmann, Bernd. *Analog Computing*. Oldenbourg Wissenschaftsverlag, 2013.
[^4]: Horowitz, Paul and Hill, Winfield. *The Art of Electronics*. 3rd Edition, Cambridge University Press, 2015.
[^5]: [AD633 Analog Multiplier Datasheet - Analog Devices](https://www.analog.com/media/en/technical-documentation/data-sheets/AD633.pdf)
[^6]: [Op-Amp Applications Handbook - Analog Devices](https://www.analog.com/en/education/education-library/op-amp-applications-handbook.html)

## Resources

### Online Communities

- r/electronics (Reddit)
- r/AskElectronics (Reddit)
- EEVblog Forum
- Analog computing enthusiast groups

### Books

- "Analog and Hybrid Computing" by Bernd Ulmann[^3]
- "Op-Amp Applications Handbook" by Analog Devices[^6]
- "The Art of Electronics" by Horowitz & Hill[^4]

## Further Reading

- [THE Analog Thing](01-the-analog-thing.md)
- [Modern Op-Amps](02-modern-op-amps.md)
- [First Circuit Tutorial](../07-tutorials/01-first-circuit.md)
