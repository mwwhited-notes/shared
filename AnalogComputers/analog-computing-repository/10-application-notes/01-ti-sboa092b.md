# TI Handbook of Operational Amplifier Applications (SBOA092B)

## Overview

Texas Instruments Application Report SBOA092B is one of the most comprehensive and valuable resources for understanding operational amplifier circuits. Originally written in the 1960s for analog computing applications, it remains highly relevant today.

**Full Document**: [https://www.ti.com/lit/an/sboa092b/sboa092b.pdf](https://www.ti.com/lit/an/sboa092b/sboa092b.pdf)

## Table of Contents Summary

1. Basic Operational Amplifier Circuits
2. Summing Point Restraints
3. Impedance Levels
4. Integrators and Differentiators
5. Voltage-to-Current Converters
6. Current-to-Voltage Converters
7. Active Filters
8. Comparators
9. Voltage References
10. Oscillators
11. Peak Detectors
12. Sample-and-Hold Circuits

## Key Circuits for Analog Computing

### 1. Inverting Amplifier (Basic Building Block)

The inverting amplifier configuration forms the basis of almost all analog computing circuits.

```
           Rf
      ┌────/\/\/────┐
      │             │
Vin ──/\/\/────────(-)──┐
      Rin              │
                 OP    ├── Vout = -(Rf/Rin)·Vin
                       │
         ┌─────────(+)─┘
         │
        ─┴─ GND
```

**Key Points:**
- Gain determined by resistor ratio
- Input impedance equals Rin
- Virtual ground at summing junction
- Phase inversion (180°)

### 2. Summing Amplifier

```
              Rf
         ┌────/\/\/────┐
         │             │
V1 ──────/\/\/──┬─────(-)──┐
         R1     │          │
                │    OP    ├── Vout = -Rf(V1/R1 + V2/R2 + V3/R3)
V2 ──────/\/\/──┤          │
         R2     │          │
                │     ┌───(+)
V3 ──────/\/\/──┘     │
         R3          ─┴─ GND
```

**For equal resistors (R1 = R2 = R3 = R = Rf):**
```
Vout = -(V1 + V2 + V3)
```

**Applications:**
- Combining signals in differential equations
- Weighted summation
- Audio mixing

### 3. Integrator

The integrator is THE most important circuit for analog computing.

```
              C
         ┌────||────┐
         │          │
Vin ─────/\/\/─────(-)──┐
         R              │
                  OP    ├── Vout = -(1/RC)∫Vin dt
                        │
          ┌─────────(+)─┘
          │
         ─┴─ GND
```

**Time Constant:** τ = RC

**Design Considerations from SBOA092B:**
1. Use low-offset op-amps to minimize drift
2. Add reset switch for initial conditions
3. Consider dielectric absorption in capacitors
4. Parallel resistor limits DC gain (prevents saturation)

**Practical Integrator with DC Stability:**
```
              C
         ┌────||────┐
         │          │
         │    Rf    │  (Rf >> R, typically 100x)
         ├──/\/\/───┤
         │          │
Vin ─────/\/\/─────(-)──┐
         R              │
                  OP    ├── Vout
                        │
          ┌─────────(+)─┘
          │
         ─┴─ GND

DC gain limited to Rf/R
Integration valid for f > 1/(2πRfC)
```

### 4. Differentiator

```
              R
         ┌────/\/\/────┐
         │             │
Vin ─────||───────────(-)──┐
          C                │
                     OP    ├── Vout = -RC·(dVin/dt)
                           │
            ┌──────────(+)─┘
            │
           ─┴─ GND
```

**Problems with Basic Differentiator:**
- Gain increases with frequency (noise amplification)
- Potentially unstable
- Rarely used in practice

**Practical Differentiator (from SBOA092B):**
```
              R1
         ┌────/\/\/────┐
         │             │
         │      C1     │
         ├─────||──────┤
         │             │
Vin ─────/\/\/───||───(-)──┐
         Rs     C          │
                     OP    ├── Vout
                           │
            ┌──────────(+)─┘
            │
           ─┴─ GND
```

**Design for limited bandwidth:**
- Rs limits high-frequency input current
- C1 rolls off gain at high frequencies
- Maximum gain = R1/Rs

### 5. Voltage-to-Current Converter

```
           R
      ┌────/\/\/────┐
      │             │
      │      ┌─────(-)──┐
      │      │          │
Vin ──┴──────┴──────(+)─┤ OP ├──┬── Vout
                        │    │  │
                        └────┘  │
                                │
                               ─┴─
                               Load
                                │
                               ─┴─ GND

I_load = Vin/R (independent of load)
```

### 6. Current-to-Voltage Converter (Transimpedance)

```
              Rf
         ┌────/\/\/────┐
         │             │
Iin ─────┼────────────(-)──┐
         │                 │
         │           OP    ├── Vout = -Iin × Rf
         │                 │
         │    ┌────────(+)─┘
         │    │
         │   ─┴─ GND
```

## Analog Computing Specific Sections

### Summing Point Restraints

The document explains the "virtual ground" concept:
- The summing junction stays at virtual ground
- No current flows into the op-amp inputs
- All input currents flow through the feedback element

This is fundamental to understanding how analog computers work.

### Sign Inversion and Why It Matters

All basic op-amp circuits invert:
- Need two inversions to get back to original sign
- Important for feedback loops in differential equations
- Can combine inversion with other operations

### Combining Operations

**Summing Integrator:**
```
                C
         ┌────||────┐
         │          │
V1 ──────/\/\/──┬──(-)──┐
         R1     │       │
                │  OP   ├── Vout = -(1/C)∫(V1/R1 + V2/R2)dt
V2 ──────/\/\/──┤       │
         R2     │       │
                │  ┌───(+)
                │  │
                │ ─┴─ GND
```

**Weighted Summing Integrator:**
Different input resistors provide different weights for each input.

## Important Design Notes from SBOA092B

### 1. Component Selection

**Resistors:**
- Use 1% metal film for accuracy
- Match resistor pairs to 0.1% for best performance
- Temperature coefficients should match

**Capacitors:**
- Polypropylene or polystyrene for integrators
- Low dielectric absorption is critical
- Avoid ceramic for precision applications

### 2. Power Supply Considerations

- Always bypass with 0.1μF ceramic close to IC
- Add 10μF electrolytic on power rails
- Use regulated supplies for precision work

### 3. Bandwidth Limitations

- Op-amp gain decreases with frequency
- Integration accuracy limited by GBW product
- Allow 10x margin between signal frequency and GBW

### 4. Noise Considerations

- Input-referred noise multiplied by gain
- Use low-noise op-amps for high-gain stages
- Bandwidth limiting reduces noise

## Recommended Reading Sequence

1. **Start with Section 1**: Basic circuits and virtual ground concept
2. **Study Section 4**: Integrators and differentiators (core of analog computing)
3. **Review Section 2**: Summing point restraints for deeper understanding
4. **Explore Section 7**: Active filters build on these concepts

## Related TI Documents

- **SNOA621C**: More application examples
- **SNLA140D**: Circuit collection
- **SBOA275**: Detailed integrator design
- **SLOA049D**: Filter design techniques

## Citation

Texas Instruments, "Handbook of Operational Amplifier Applications," Application Report SBOA092B, October 2001 (Revised).

