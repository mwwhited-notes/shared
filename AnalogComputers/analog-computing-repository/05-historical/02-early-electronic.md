# Early Electronic Analog Computers

## Overview

The transition from mechanical to electronic analog computers in the 1940s-1960s revolutionized computation speed, accuracy, and flexibility. The operational amplifier became the central computing element[^1].

## The Birth of the Op-Amp

### Vacuum Tube Origins (1940s)

**1941:** First electronic operational amplifier
- Developed by Karl D. Swartzel Jr. at Bell Labs
- For M-9 gun director (anti-aircraft)
- High-gain DC amplifier with feedback

**1947:** George A. Philbrick
- Recognized commercial potential
- Founded Philbrick Researches
- First commercial op-amps

### Early Op-Amp Characteristics

```
Vacuum Tube Op-Amp (typical):
┌────────────────────────────────────┐
│  Gain: 10,000 - 1,000,000         │
│  Input impedance: ~1 MΩ            │
│  Output: ±50V to ±100V             │
│  Power: 10-50 Watts per channel    │
│  Size: Chassis-mounted module      │
│  Drift: Several mV per hour        │
│  Warm-up: 15-30 minutes            │
└────────────────────────────────────┘
```

### Philbrick K2-W (1952)

First widely-used general-purpose op-amp:
- Plug-in octal module
- ±300V supply
- Open-loop gain: 15,000
- Price: ~$22 (1952 dollars)

## Major Early Electronic Computers

### ENIAC (1945)

While primarily digital, used analog concepts:
- Function tables (diode matrices)
- Inspired by differential analyzer
- Computed artillery firing tables

### Typhoon (1947)

MIT Servomechanisms Lab:
- Real-time flight simulation
- Early aerospace application
- Hybrid analog-servo system

### REAC (1946)

Reeves Electronic Analog Computer:
- First commercially available electronic analog computer
- Developed by Reeves Instrument Company
- Used for aircraft design

### GEDA (1947)

Goodyear Electronic Differential Analyzer:
- General-purpose analog computer
- Educational and research use
- Demonstrated practicality of electronic approach

## The Analog Computer Industry

### Major Manufacturers

**United States:**
| Company | Notable Products | Era |
|---------|------------------|-----|
| Electronic Associates Inc. (EAI) | PACE series, 231R | 1950s-1980s |
| Applied Dynamics | AD-4, AD-256 | 1960s-1980s |
| Beckman/Berkeley | EASE series | 1950s-1970s |
| Philbrick | Op-amps, small computers | 1950s-1970s |
| GPS Instrument | Various | 1960s-1970s |

**Europe:**
| Company | Country | Products |
|---------|---------|----------|
| Telefunken | Germany | RA series |
| EAI Europe | Belgium | PACE/EAI |
| Solartron | UK | Various |
| Hitachi | Japan | Large systems |

### Typical System Architecture

```
┌───────────────────────────────────────────────────────────┐
│                    PATCH PANEL                            │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐                 │
│  │ INT │ │ INT │ │ SUM │ │MULT │ │ POT │ ...              │
│  └──●──┘ └──●──┘ └──●──┘ └──●──┘ └──●──┘                 │
│     │       │       │       │       │                     │
│     └───────┴───────┴───────┴───────┘                     │
│              PATCH CORD CONNECTIONS                       │
├───────────────────────────────────────────────────────────┤
│  COEFFICIENT POTENTIOMETERS                               │
│  [0.000] [0.000] [0.000] [0.000] [0.000] ...             │
├───────────────────────────────────────────────────────────┤
│  MODE CONTROL                                             │
│  [RESET] [OPERATE] [HOLD] [REPOP] [TIME SCALE]           │
├───────────────────────────────────────────────────────────┤
│  OUTPUT DEVICES                                           │
│  [Oscilloscope] [X-Y Plotter] [Meters] [Strip Chart]     │
└───────────────────────────────────────────────────────────┘
```

## EAI (Electronic Associates Inc.)

### PACE (Precision Analog Computing Equipment)

**PACE TR-10 (1961):**
- Desktop unit
- 6 integrators, 4 summers
- ±10V operation
- Solid-state (transistor)
- Educational and small problems

**PACE TR-48 (1963):**
- Medium-scale
- 24 integrators
- Professional research

**EAI 231R (1963):**
- Large-scale scientific
- 120 integrators
- 0.01% accuracy
- Expandable to 500+ amplifiers

### EAI 680 Series (1960s-1970s)

**Features:**
- Modular construction
- Automatic patching available
- Computer-controlled coefficients
- Hybrid capability (digital interface)

## Solid-State Revolution

### Transistor Op-Amps (1960s)

**Advantages over vacuum tubes:**
- Lower power consumption
- No warm-up time
- Smaller size
- Better reliability
- Lower cost

**Notable early transistor op-amps:**
- Philbrick P2, P25
- Burr-Brown 3000 series

### Integrated Circuit Op-Amps (1963+)

**Fairchild μA702 (1963):**
- First monolithic IC op-amp
- Limited performance

**Fairchild μA709 (1965):**
- First widely-used IC op-amp
- Designed by Bob Widlar
- Required external compensation

**Fairchild μA741 (1968):**
- Internally compensated
- Became industry standard
- Still produced today

### Impact on Analog Computers

IC op-amps enabled:
- Much smaller computers
- Desk-top units
- Educational versions
- Lower cost per channel
- Better reliability

## Specialized Analog Computers

### Flight Simulators

**Link Trainers (1930s-1940s):**
- Early flight training
- Electromechanical

**Full Flight Simulators (1950s-1960s):**
- All-analog computers
- Real-time aircraft dynamics
- 6 degrees of freedom
- Motion platforms

### Nuclear Reactor Simulators

**Purpose:**
- Operator training
- Safety analysis
- Design verification

**Complexity:**
- Neutron kinetics
- Thermal hydraulics
- Control systems
- Hundreds of amplifiers

### Process Industry Simulators

- Petrochemical plants
- Power plants
- Paper mills
- Chemical processes

## Decline of Electronic Analog Computers

### Factors (1970s-1980s)

1. **Digital computer advancement**
   - Faster processors
   - Lower cost
   - Greater flexibility

2. **Software development**
   - Numerical methods improved
   - Easier programming
   - Simulation languages

3. **Hybrid transition**
   - Best of both worlds
   - Digital control of analog hardware
   - Gradual shift to all-digital

### Last Major Production

- **1980s:** Most manufacturers exit market
- **1990s:** Specialty/niche only
- **2000s:** Educational/hobbyist revival

## Historical Significance

Electronic analog computers:

1. **Solved previously intractable problems**
   - Aerospace design
   - Nuclear weapons development
   - Process control

2. **Trained engineers**
   - Systems thinking
   - Differential equations
   - Real-time dynamics

3. **Developed key technologies**
   - Operational amplifiers
   - Feedback theory
   - Hybrid computation

4. **Influenced digital design**
   - Simulation concepts
   - Numerical methods
   - Real-time systems

## References

[^1]: [Op-amp Circuit Design - Computer History Museum](https://www.computerhistory.org/revolution/analog-computers/3/156)

## Further Reading

- [Hybrid Analog-Digital Systems](03-hybrid-systems.md)
- [Famous Analog Machines](04-famous-machines.md)
- [Op-Amp Basics](../01-fundamentals/02-op-amp-basics.md)
