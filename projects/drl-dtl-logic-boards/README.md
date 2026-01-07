# DRL/DTL Logic Boards

**Status**: Reference/As Needed

Diode-Resistor Logic (DRL) and Diode-Transistor Logic (DTL) educational boards for teaching fundamental digital logic without integrated circuits.

## Overview

| Aspect | Details |
|--------|---------|
| Project Type | Digital Logic / Education |
| Status | **Reference/As Needed** |
| Date Built | TBD |
| Purpose | **Discrete component logic gates for teaching digital fundamentals** |
| Technology | DRL (Diode-Resistor Logic), DTL (Diode-Transistor Logic) |

## Project Summary

Educational logic boards demonstrating how digital logic gates work using discrete components (diodes, resistors, transistors) rather than integrated circuits. Useful reference for understanding the fundamentals of digital logic before moving to 74-series TTL or CMOS chips.

## Technology Background

### Diode-Resistor Logic (DRL)

**Principle:** Uses diodes and resistors to implement basic logic functions.

**Typical Gates:**
- **AND gate:** Diodes in series
- **OR gate:** Diodes in parallel
- **NOT gate:** Cannot be implemented with DRL alone (requires active components)

**Advantages:**
- Simple, minimal components
- Easy to understand and build
- Low cost

**Disadvantages:**
- No signal amplification (passive logic)
- Limited fan-out
- Cannot invert signals
- Slower switching speeds

### Diode-Transistor Logic (DTL)

**Principle:** Adds transistors to DRL for signal amplification and inversion.

**Typical Gates:**
- **NAND gate:** Diode AND + transistor inverter
- **NOR gate:** Diode OR + transistor inverter
- **NOT gate:** Single transistor inverter

**Advantages:**
- Signal restoration and amplification
- Can drive multiple gates (better fan-out)
- Complete logic family (all gates possible)
- Precursor to TTL logic

**Disadvantages:**
- More complex than DRL
- Slower than modern logic families
- Higher power consumption than CMOS

## Boards Description

**Type:** Educational demonstration boards

**Purpose:**
- Teaching digital logic fundamentals
- Understanding gate-level operation
- Comparison to modern integrated logic (74-series, CMOS)
- Historical context for early computer design

**Use Cases:**
- Reference for digital design courses
- Comparison to TTL/CMOS logic
- Understanding logic family evolution
- SAP-1 and other discrete logic projects

## Related Notes

**EmbeddedBakery Project:**
- Additional documentation may exist in [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery)
- Check repository for schematics, build photos, or detailed notes

## Related Projects

- [SAP-1 Computer](../sap-1-computer/) - Uses 74-series TTL, next evolution from DTL
- [Gigatron TTL Computer](../../Programmable%20Devices/gigatron-ttl/) - TTL computer kit (7400-series)
- [FPGA CPU Design](../fpga-cpu-design/) - Modern digital logic implementation

## Comparison to Modern Logic

| Logic Family | Era | Components | Speed | Power | Complexity |
|--------------|-----|------------|-------|-------|------------|
| **DRL** | 1950s | Diodes, resistors | Slow | Low | Simple gates only |
| **DTL** | 1960s | Diodes, transistors, resistors | Moderate | Moderate | Complete logic family |
| **TTL (74-series)** | 1970s-present | Integrated transistors | Fast | Moderate-High | Standardized ICs |
| **CMOS (4000/74HC)** | 1980s-present | MOSFETs | Fast | Very Low | High integration |

## Educational Value

### Learning Objectives

1. **Gate-Level Understanding**
   - How AND/OR gates work with diodes
   - Why NOT gates need active components
   - Signal levels and voltage thresholds

2. **Logic Family Evolution**
   - DRL → DTL → TTL → CMOS progression
   - Trade-offs in speed, power, complexity
   - Historical context for computer development

3. **Discrete vs. Integrated**
   - Compare board-level circuits to 74xx chips
   - Understand abstraction layers
   - Appreciate modern IC integration

### Example Circuits

#### DRL AND Gate (2-input)

```
    +5V
     |
    [R] 10kΩ (pull-up)
     |
     +---- Output
     |
    >|-- Diode 1 ---- Input A
     |
    >|-- Diode 2 ---- Input B
     |
    GND
```

**Truth Table:**
| A | B | Output |
|---|---|--------|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

#### DTL NAND Gate (2-input)

```
Input A ---|>|---+
               |
Input B ---|>|---+---- Base ----[Q1]---- Output
               |              (NPN)
              [R]                |
               |                GND
              GND

    +5V ----[Rc]---- Collector (Q1)
```

**Truth Table:**
| A | B | Output |
|---|---|--------|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

## Equipment Used

**Components:**
- Diodes (1N4148 or similar)
- Resistors (various values: 1kΩ, 10kΩ)
- Transistors (2N2222, 2N3904, or similar NPN)
- Breadboard or perfboard
- Power supply (5V)

**Test Equipment:**
- Logic probe or LED indicators
- DMM for voltage measurements
- Oscilloscope (optional, for timing analysis)

## Documentation To-Do

- [ ] Locate detailed notes/schematics in EmbeddedBakery
- [ ] Document board layout and gate types
- [ ] Add photos of boards
- [ ] Create detailed schematics
- [ ] Add experimental results and measurements
- [ ] Compare timing to 74-series equivalents

## Resources

### DRL/DTL References

- **Digital Computer Electronics** (Malvino) - Chapter on logic families
- **The Art of Electronics** (Horowitz & Hill) - Discrete logic section
- Wikipedia: [Diode logic](https://en.wikipedia.org/wiki/Diode_logic)
- Wikipedia: [Diode–transistor logic](https://en.wikipedia.org/wiki/Diode%E2%80%93transistor_logic)

### Historical Context

- Early computers used discrete component logic
- IBM 7000 series (1950s-60s) used DTL
- First IC logic families evolved from DTL
- TTL (7400 series, 1964) replaced DTL for most applications

## Integration with Other Projects

### SAP-1 Computer
- SAP-1 uses 74-series TTL ICs
- DRL/DTL boards demonstrate what's inside those ICs
- Educational progression: discrete → integrated logic

### FPGA Projects
- Modern equivalent: gates in programmable fabric
- Abstraction: FPGA synthesizes from HDL
- DRL/DTL shows physical gate implementation

## Notes

- Boards available as reference for digital logic education
- Not actively being developed, but useful for teaching
- May reference when working on discrete logic projects
- Good comparison point for understanding logic family evolution
- Additional documentation may exist in [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery) repository

---

*Last updated: 2026-01-07*
