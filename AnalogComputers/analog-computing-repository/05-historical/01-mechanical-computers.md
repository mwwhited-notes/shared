# Mechanical Analog Computers

## Overview

Before electronic analog computers, mechanical devices performed analog computations using gears, cams, levers, and other mechanisms. These devices laid the groundwork for understanding analog computation and solving complex mathematical problems[^1].

## Ancient and Medieval Devices

### Antikythera Mechanism (~100 BCE)

The oldest known analog computer:
- Discovered in 1901 from Greek shipwreck
- Predicted astronomical positions
- 30+ bronze gears
- Computed: Sun, Moon positions, eclipses, Olympic games
- Differential gear mechanism

**Significance:** Demonstrates sophisticated mechanical computing over 2000 years ago.

### Astrolabe (Medieval)

```
┌───────────────────────────┐
│       ╭───────╮           │
│      ╱  ╭───╮  ╲          │
│     │  │ ★  │  │          │
│     │  │    │  │          │
│      ╲  ╰───╯  ╱          │
│       ╰───────╯           │
│    [Rete - star map]      │
│                           │
│    [Mater - coordinate    │
│     plate]                │
└───────────────────────────┘
```

**Functions:**
- Finding time from star positions
- Determining sunrise/sunset
- Navigation
- Surveying

### Sectors and Proportional Compasses (1600s)

Galileo's sector:
- Two hinged rulers with scales
- Solved proportion problems
- Artillery calculations
- Surveying

## The Slide Rule

### Development

- **1620:** Edmund Gunter - logarithmic scale
- **1622:** William Oughtred - combined two scales
- **1859:** Amédée Mannheim - modern form

### Operating Principle

Multiplication via addition of logarithms:
```
log(A × B) = log(A) + log(B)

Slide scale B along scale A
Read product where scales align
```

### Scales

| Scale | Function |
|-------|----------|
| C, D | Basic multiplication/division |
| A, B | Squares |
| K | Cubes |
| L | Logarithms |
| S | Sines |
| T | Tangents |
| CI | Reciprocals |

### Accuracy

- 3 significant figures (typical)
- 4 figures (precision rules)
- Speed: ~4 seconds per operation (practiced user)

### Legacy

Used until 1970s:
- Engineers
- Scientists
- Students
- Apollo astronauts carried backup slide rules

## Planimeters

### Function

Measure area of irregular closed curves by tracing the boundary.

### Types

**Polar Planimeter (Amsler, 1854):**
```
        Pole (fixed)
            │
            ╲
             ╲ Arm 1
              ╲
               ○─────────────○ Tracer
              ╱     Arm 2
             ╱
            ╱
     Measuring wheel
```

**Operation:**
1. Fix pole outside figure
2. Trace boundary with tracer point
3. Measuring wheel records area

**Mathematics:** Green's theorem relates line integral to area

**Accuracy:** 0.1% to 1%

### Applications

- Map areas (geography, surveying)
- Engineering drawings
- Ship hull cross-sections
- Steam engine indicator diagrams

## Integrators

### Wheel-and-Disk Integrator (James Thomson, 1876)

```
           Disk (rotates)
              ╱│
             ╱ │
            ╱  │ ← Wheel position (input y)
           ╱   ●────────────────────
          ╱    │    Wheel (friction drive)
         ╱     │
        ╱      │
       ╱       │
      ╱        │
Input x ───────┼───────► Output: ∫y dx
               │
```

**Principle:**
- Disk rotates proportional to x
- Wheel position set by y
- Wheel rotation = ∫y dx

**Limitation:** Low torque output, required torque amplification

### Ball-and-Disk Integrator

Improved version using ball between two disks for better torque transfer.

## Differential Analyzers

### Vannevar Bush's Differential Analyzer (1931)

The first practical large-scale mechanical analog computer[^2].

**Components:**
- Wheel-and-disk integrators (6)
- Torque amplifiers
- Adders (differential gears)
- Input/output tables
- Interconnection shafts

**Architecture:**
```
┌─────────────────────────────────────────────────┐
│                                                 │
│  [Input Table] → [Integrator] → [Output Table] │
│       ↑              ↑              ↓          │
│       │         [Adder]             │          │
│       │              ↑              │          │
│       └──────────────┴──────────────┘          │
│                                                 │
│         (Mechanical shaft connections)          │
└─────────────────────────────────────────────────┘
```

**Capabilities:**
- 6th-order differential equations
- Accuracy: ~0.1%
- Setup time: hours to days

### Torque Amplifier

Critical invention enabling practical differential analyzers:
```
    Input shaft (low torque)
           │
           ▼
    ┌──────────────┐
    │   Friction   │
    │   drum 1     │───┐
    └──────────────┘   │
           ↑           │
    ┌──────────────┐   │
    │   Friction   │───┤
    │   drum 2     │   │
    └──────────────┘   │
           │           │
           ▼           │
    High-torque motor ─┘
           │
           ▼
    Output shaft (high torque)
```

**Gain:** ~10,000× torque amplification

### Famous Differential Analyzers

| Machine | Location | Year | Integrators |
|---------|----------|------|-------------|
| Bush's original | MIT | 1931 | 6 |
| Moore School | Penn | 1935 | 14 |
| Manchester | UK | 1935 | 8 |
| MADDIDA | Northrop | 1949 | Digital hybrid |

## Mechanical Fire Control

### Naval Fire Control Computers

**Ford Mk 37 (WWII):**
- Computed gun aiming solutions
- Inputs: ship motion, target motion, ballistics
- Mechanical cams and gears
- Real-time operation

**Norden Bombsight:**
- Computed bomb release point
- Accounted for altitude, speed, wind
- Automatic level stabilization

### Components

**Cams:** Generated nonlinear functions
```
    Cam profile defines f(θ)
         ╭───╮
        ╱     ╲
       │       │
       │   ●   │ ← Follower
        ╲     ╱
         ╰───╯
```

**Differentials:** Added or subtracted rotations
**Ball resolvers:** Computed sine/cosine
**Mechanical multipliers:** Product of two inputs

## Tide Predictors

### Lord Kelvin's Tide Predictor (1872)

```
     Multiple pulleys with different ratios
            │   │   │   │
            ●   ●   ●   ●  ← Harmonic components
            │   │   │   │
            └───┴───┴───┘
                  │
                  ▼
              [Summer]
                  │
                  ▼
            Tide prediction
```

**Function:** h(t) = Σ Aₙ cos(ωₙt + φₙ)

**Components:** Up to 40 harmonic constituents

### Operation

- Each pulley rotates at constituent frequency
- Amplitude set by pulley size/position
- Cord sums all components
- Output: predicted tide height

**Accuracy:** Predicted tides months/years in advance

## Legacy

Mechanical analog computers established:
1. **Physical representation of mathematics**
2. **Integration as fundamental operation**
3. **Feedback and control concepts**
4. **Real-time computation**
5. **System simulation principles**

These concepts transferred directly to electronic analog computers.

## References

[^1]: [Analog Computer - Wikipedia: Mechanical Computers](https://en.wikipedia.org/wiki/Analog_computer)
[^2]: [Computer History Museum - Differential Analyzer](https://www.computerhistory.org/revolution/analog-computers/3/143)

## Further Reading

- [Early Electronic Computers](02-early-electronic.md)
- [Famous Analog Machines](04-famous-machines.md)
