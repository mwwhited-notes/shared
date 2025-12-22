# Operational Amplifier Basics

## What is an Operational Amplifier?

An operational amplifier (op-amp) is a DC-coupled, high-gain electronic voltage amplifier with differential inputs and typically a single-ended output. The name comes from its original use: performing mathematical **operations** in analog computers.

## Ideal Op-Amp Characteristics

For analog computing analysis, we often assume an "ideal" op-amp:

| Parameter | Ideal Value | Typical Real Value |
|-----------|-------------|-------------------|
| Open-loop gain (A) | ∞ | 10⁵ to 10⁹ |
| Input impedance (Zᵢ) | ∞ | > 1 MΩ (BJT), > 10¹² Ω (FET) |
| Output impedance (Zₒ) | 0 | < 100 Ω |
| Bandwidth | ∞ | Limited (GBW product) |
| Input offset voltage | 0 | 1-10 mV |
| Input bias current | 0 | pA to μA |

## Op-Amp Symbol and Terminals

```
        V+
        │
    ┌───┴───┐
    │       │
(-)─┤-      ├─── Vout
    │   A   │
(+)─┤+      │
    │       │
    └───┬───┘
        │
        V-
```

- **(+) Non-inverting input**: Positive voltage here increases output
- **(-) Inverting input**: Positive voltage here decreases output
- **Vout**: Output voltage
- **V+, V-**: Power supply rails (typically ±15V or ±12V)

## The Golden Rules (Ideal Op-Amp with Negative Feedback)

When an op-amp operates with negative feedback:

### Rule 1: No Current into Inputs
The input impedance is so high that no current flows into either input terminal:
```
I(+) = I(-) = 0
```

### Rule 2: Virtual Short
The infinite gain forces the two input terminals to the same voltage:
```
V(+) = V(-)
```

These two rules are the foundation of all op-amp circuit analysis.

## Basic Op-Amp Configurations

### 1. Inverting Amplifier

```
         Rf
    ┌────/\/\/────┐
    │             │      ┌──────┐
Vin ─/\/\/─┬─────(-)─────┤+     │
     Rin   │             │  op  ├── Vout
           │    ┌───(+)──┤-     │
           │    │        └──────┘
           ▼    ▼
          GND  GND
```

**Transfer Function:**
```
Vout = -(Rf/Rin) × Vin
```

**Gain:**
```
Av = -Rf/Rin
```

The negative sign indicates phase inversion (180°).

### 2. Non-Inverting Amplifier

```
              Rf
         ┌────/\/\/────┐
         │             │   ┌──────┐
         │    ┌───────(-)──┤      │
         │    │            │      │
Vin ─────┼────┴───────(+)──┤ op   ├── Vout
         │                 └──────┘
         │
        /\/\/ R1
         │
         ▼
        GND
```

**Transfer Function:**
```
Vout = (1 + Rf/R1) × Vin
```

**Gain:**
```
Av = 1 + Rf/R1
```

Always positive gain ≥ 1.

### 3. Voltage Follower (Buffer)

```
           ┌────────────────┐
           │        ┌─────┐ │
Vin ───────┴──(+)───┤ op  ├─┴── Vout
                    │     │
          ┌───(-)───┤     │
          │         └─────┘ 
          └───────────── Vout
```

**Transfer Function:**
```
Vout = Vin
```

Unity gain buffer with high input impedance, low output impedance.

## Op-Amp Computing Circuits

### Summing Amplifier (Adder)

```
                            Rf
                     ┌────/\/\/────┐
                     │   ┌──────┐  │
V1 ─/\/\/─┬──────(-)─┴───┤      │  │
     R1   │              │  op  ├──┴─── Vout
V2 ─/\/\/─┤     ┌───(+)──┤      │
     R2   │     │        └──────┘
V3 ─/\/\/─┘     ▼
     R3        GND
```

**Transfer Function (with equal resistors R):**
```
Vout = -(Rf/R)(V1 + V2 + V3)
```

If Rf = R:
```
Vout = -(V1 + V2 + V3)
```

### Integrator

```
                        C
                   ┌────||───────┐
                   │   ┌──────┐  │
Vin ─/\/\/─┬──(-)──┴───┤      │  │
     R     │           │  op  ├──┴─── Vout
           │  ┌───(+)──┤      │
           │  │        └──────┘
           ▼  ▼
          GND GND
```

**Transfer Function:**
```
Vout = -(1/RC) ∫ Vin dt
```

Time constant: τ = RC

### Differentiator

```
           R
                     ┌────/\/\/────┐
                     │   ┌──────┐  │
Vin ──||──┬─────(-)──┴───┤      │  │
      C   │              │  op  ├──┴─── Vout
          │     ┌───(+)──┤      │
          │     │        └──────┘
          ▼     ▼
         GND   GND
```

**Transfer Function:**
```
Vout = -RC × (dVin/dt)
```

Note: Differentiators are noise-sensitive and less commonly used.

## Real Op-Amp Considerations

### Gain-Bandwidth Product (GBW)

Real op-amps have limited bandwidth. The gain-bandwidth product is constant:
```
GBW = Gain × Bandwidth
```

For a 741 op-amp: GBW ≈ 1 MHz
- At gain of 10: BW ≈ 100 kHz
- At gain of 100: BW ≈ 10 kHz

### Slew Rate

Maximum rate of output voltage change:
```
Slew Rate = dVout/dt (max)
```

Typical: 0.5 V/μs (741) to 1000+ V/μs (high-speed)

### Offset Voltage

Input offset voltage causes output error:
```
Vout(error) = Vos × (1 + Rf/Rin)
```

For precision computing, use:
- Low-offset op-amps
- Offset trim potentiometer
- Chopper-stabilized op-amps

### Common Mode Rejection Ratio (CMRR)

Ability to reject signals common to both inputs:
```
CMRR = 20 log₁₀(Ad/Acm) dB
```

Typical: 80-120 dB

## Op-Amp Selection for Analog Computing

### Key Parameters to Consider

| Parameter | Importance | Typical Requirement |
|-----------|------------|---------------------|
| Input offset voltage | Critical | < 1 mV |
| Input bias current | High | < 100 nA |
| Open-loop gain | High | > 100,000 |
| GBW product | Medium | > 1 MHz |
| Slew rate | Medium | > 1 V/μs |
| Power supply range | Medium | ±12V to ±18V |

### Recommended Op-Amps for Analog Computing

| Op-Amp | Type | Notable Features |
|--------|------|------------------|
| LM741 | General purpose | Classic, inexpensive |
| TL071/TL074 | JFET input | Low bias current |
| OP07 | Precision | Very low offset |
| OPA2134 | Audio | Low noise, high speed |
| AD744 | Precision | Fast, accurate |
| LT1013 | Precision | Dual, low power |

## Power Supply Considerations

### Bipolar Supply
Most analog computing uses bipolar (split) supplies:
- Typical: ±12V, ±15V
- Allows positive and negative signal voltages
- Output swings nearly rail-to-rail

### Decoupling
Always use decoupling capacitors:
```
        +V
        │
       === 0.1μF (close to IC)
        │
       === 10μF (near supply)
        │
       ─┴─ GND
```

## Practical Tips

1. **Keep leads short** to minimize noise pickup
2. **Use ground planes** for stable reference
3. **Match resistor values** for accurate ratios
4. **Use 1% or better** tolerance resistors
5. **Temperature stability** matters for precision
6. **Allow warm-up time** (10-30 minutes) for best accuracy
7. **Check for oscillation** - unwanted high-frequency oscillation is common

## References

[^1]: [Operational Amplifier - Wikipedia](https://en.wikipedia.org/wiki/Operational_amplifier)
[^2]: [Op-Amp Basics - Analog Devices](https://www.analog.com/en/education/landing-pages/003/beginners-guide-to-op-amps.html)
[^3]: [Op-Amp History - Computer History Museum](https://www.computerhistory.org/revolution/analog-computers/3/156)
[^4]: Jung, Walter G. *Op Amp Applications Handbook*. Analog Devices, 2005.
[^5]: [TL07x Datasheet - Texas Instruments](https://www.ti.com/lit/ds/symlink/tl071.pdf)

## Further Reading

- [Summers and Inverters](../02-components/01-summers-inverters.md)
- [Integrators](../02-components/02-integrators.md)
- [Scaling and Normalization](05-scaling.md)
