# Signal Processing

## Overview

Analog signal processing predates digital techniques and remains relevant for real-time, low-power, and high-frequency applications. Analog computers naturally perform many signal processing operations through their basic computing elements.

## Filtering

### Low-Pass Filter

First-order low-pass (integrator with feedback):
```
              Rf
         ┌────/\/\/────┐
         │      │      │
         │      │      │
         │     ═╪═ Cf  │
         │      │      │
Vin ─────/\/\/──┴─────(-)──┐
          Rin              │
                     OP    ├── Vout (filtered)
                           │
                ┌─────(+)──┘
                │
                ▼
               GND
```

**Transfer function:**
```
H(s) = -Rf/Rin · 1/(1 + sRfCf)
Cutoff: fc = 1/(2πRfCf)
```

### High-Pass Filter

```
          Cf      Rf
Vin ──────||────/\/\/──┬─────(-)──┐
                       │          │
                       │    OP    ├── Vout
                       │          │
                  ┌───(+)─────────┘
                  │
                  ▼
                 GND
```

**Transfer function:**
```
H(s) = -sRfCf/(1 + sRfCf)
```

### Band-Pass Filter

Cascade low-pass and high-pass, or use state-variable filter:

```
      ┌──────[HP]──[LP]──────┐
      │                      │
Vin ──┴──────────────────────┴── Vout (band-pass)
```

### State-Variable Filter

Simultaneously produces LP, HP, BP outputs:
```
Vin ──[SUM]──[INT]──[INT]──┬── LP output
        ↑      │     │     │
        │      │     │     │
        │      └─────┼─────┤
        │            │     │
        └────[−Q]────┤     ├── BP output
                     │     │
                     │     │
                     ├─────┴── HP output
                     │
```

**Design equations:**
```
Center frequency: f0 = 1/(2πRC)
Q factor: Set by feedback resistor ratio
```

### Notch (Band-Stop) Filter

Twin-T network or subtract BP from input:
```
Vout = Vin - K·BP
```

Removes specific frequency while passing others.

### Higher-Order Filters

**Sallen-Key (second-order):**
```
Each stage: 2 poles
Cascade for 4th, 6th order
```

**Butterworth:** Maximally flat passband
**Chebyshev:** Sharper rolloff, passband ripple
**Bessel:** Maximally flat delay (linear phase)

## Amplification

### Instrumentation Amplifier

High-precision differential amplification:
```
     ┌─────────────────────────────────────┐
     │            OP1                       │
V1 ──┤(+)──────────┬─────────┐             │
     │             │         │             │
     │            Rg         │             │
     │             │         │     ┌───────┼── Vout
     │             │         │     │       │
     │            Rg    OP3 ─┼─────┤       │
     │             │         │     │       │
V2 ──┤(+)──────────┴─────────┘     │       │
     │            OP2              │       │
     └─────────────────────────────┘       │
                                           │
Gain = 1 + 2Rf/Rg                          │
                                           │
```

**Features:**
- High CMRR
- High input impedance
- Adjustable gain with single resistor

### Programmable Gain Amplifier (PGA)

Switch between gain settings:
```
        R1   R2   R3   R4
       ─┬───┬───┬───┬───┐
        SW1 SW2 SW3 SW4 │
        └───┴───┴───┴───┘
                        │
Vin ─────/\/\/──────────┴────(-)──
          Rin
```

Digital control of gain via analog switches.

## Modulation and Demodulation

### Amplitude Modulation (AM)

```
s(t) = [1 + m·x(t)]·cos(ωc·t)
```

**Implementation:**
```
Carrier ──┬──[MULT]── AM output
          │    ↑
          │    │
x(t) ──[×m]──[+1]──
```

### Frequency Modulation (FM)

```
s(t) = cos(ωc·t + β·∫x(τ)dτ)
```

Requires VCO (voltage-controlled oscillator).

### Phase Modulation (PM)

```
s(t) = cos(ωc·t + k·x(t))
```

### Demodulation

**Envelope detection:** Rectifier + low-pass filter
**Synchronous detection:** Multiply by carrier, low-pass filter
**FM detection:** Differentiator + envelope detector, or PLL

## Waveform Generation

### Sine Wave Oscillator

Wien bridge oscillator:
```
        C
   ┌────||────┐
   │          │
   │    R     │
   ├───/\/\/──┤
   │          │
Vout ─────────┴────(+)──┐
                        │
              OP        ├─┬── Vout
                        │ │
            ┌──────(-)──┘ │
            │             │
           /\/\/ Rf       │
            │             │
            └─────────────┘
```

**Frequency:** f = 1/(2πRC)

### Triangle/Square Wave Generator

Integrator + Schmitt trigger:
```
         ┌───────────────────────────┐
         │                           │
         ↓                           │
─────[INT]──┬──[Schmitt]─────────────┘
            │      │
            │      └── Square wave
            │
            └── Triangle wave
```

### Sawtooth Generator

Integrator with reset:
```
Constant ──[INT]──[Comparator/Reset]── Sawtooth
```

### Function Generator Architecture

```
                ┌────────────────────┐
                │                    ↓
Square ◄────────┤◄──[Schmitt]◄──[INT]──► Triangle
                │                    │
                │                    │
                │               [Shaper]
                │                    │
                └────────────────────┴──► Sine
```

## Spectrum Analysis

### Analog Spectrum Analyzer

Swept superheterodyne architecture:
```
Input ──[Mixer]──[IF Filter]──[Detector]──[Display]
           ↑
      [Local Osc]
           ↑
      [Sweep Gen]
```

### Real-Time Spectrum Analysis

Bank of band-pass filters:
```
Input ──┬──[BP f1]──[Detector]── Amplitude at f1
        │
        ├──[BP f2]──[Detector]── Amplitude at f2
        │
        ├──[BP f3]──[Detector]── Amplitude at f3
        │
        └── ...
```

### Harmonic Analysis

Extract specific harmonic components:
```
For fundamental: f0
For nth harmonic: n·f0

Input ──[BP at nf0]──[RMS]── nth harmonic amplitude
```

## Correlation and Convolution

### Cross-Correlation

```
Rxy(τ) = ∫x(t)·y(t+τ)dt
```

**Implementation:**
- Delay line for time shift
- Multiplier
- Integrator (or low-pass filter)

### Auto-Correlation

```
Rxx(τ) = ∫x(t)·x(t+τ)dt
```

Same signal to both inputs of correlator.

### Convolution

```
(f * g)(t) = ∫f(τ)·g(t-τ)dτ
```

Complex, requires programmable delay.

## Phase-Locked Loop (PLL)

### Basic PLL Architecture

```
Input ──[Phase Det]──[Loop Filter]──[VCO]──┬── Output
           ↑                               │
           │                               │
           └───────────────────────────────┘
```

**Applications:**
- Frequency synthesis
- FM demodulation
- Clock recovery
- Carrier recovery

### PLL Components

**Phase Detector:** Multiplier or XOR gate
**Loop Filter:** Low-pass, determines bandwidth and stability
**VCO:** Voltage-to-frequency converter

## Analog Signal Processing ICs

### Common Devices

| Function | Example ICs |
|----------|-------------|
| Op-amp | TL074, LM324, OP07 |
| Multiplier | AD633, MPY634 |
| Filter (switched-cap) | MAX291, LTC1068 |
| PLL | CD4046, LM565 |
| VCA | SSM2164, THAT2180 |
| Function generator | XR2206, MAX038 |

## Modern Applications

### Audio Processing

- Equalization (parametric, graphic)
- Compression/limiting
- Effects (chorus, flanger, phaser)
- Crossovers

### RF/Microwave

- Mixers
- Filters (SAW, ceramic)
- Amplifiers (LNA, PA)
- AGC circuits

### Instrumentation

- Signal conditioning
- Anti-aliasing filters
- Sample-and-hold
- Isolation amplifiers

### Neural Networks (Analog Implementation)

```
Neuron: y = σ(Σwᵢxᵢ + b)

Analog: Weighted summer + sigmoid function generator
```

## Advantages of Analog Signal Processing

1. **Real-time operation**: No sampling delay
2. **Power efficiency**: Often lower than digital
3. **Continuous time**: No aliasing
4. **High bandwidth**: Limited only by components
5. **No quantization noise**: Continuous amplitude

## Limitations

1. **Accuracy**: Component tolerances
2. **Drift**: Temperature, aging
3. **Flexibility**: Hardware changes needed
4. **Repeatability**: Unit-to-unit variation
5. **Complexity**: Difficult for adaptive algorithms

## References

[^1]: [Active Filter - Wikipedia](https://en.wikipedia.org/wiki/Active_filter)
[^2]: [State Variable Filter - Wikipedia](https://en.wikipedia.org/wiki/State_variable_filter)
[^3]: [Phase-Locked Loop - Wikipedia](https://en.wikipedia.org/wiki/Phase-locked_loop)
[^4]: [Analog Filter Design - Texas Instruments](https://www.ti.com/lit/an/sloa049d/sloa049d.pdf)
[^5]: [Active Filter Design Techniques - TI SLOA096](https://www.ti.com/lit/an/sloa096/sloa096.pdf)

## Further Reading

- [Op-Amp Basics](../01-fundamentals/02-op-amp-basics.md)
- [Function Generators](../02-components/05-function-generators.md)
- [Control Systems](01-control-systems.md)
