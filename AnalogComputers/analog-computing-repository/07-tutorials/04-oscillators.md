# Oscillator Circuits

## Overview

Oscillators are self-sustaining systems that produce periodic outputs without external periodic input. In analog computing, oscillators generate sine waves, test signals, and simulate periodic phenomena.

## The Harmonic Oscillator

### Differential Equation

```
d²x/dt² + ω₀²x = 0
```

**Solution:** x(t) = A·cos(ω₀t + φ)

### Why It Oscillates

Energy continuously converts between two forms:
- Kinetic (∝ velocity²)
- Potential (∝ position²)

Without damping, total energy is conserved → perpetual oscillation.

## Basic Sine Wave Oscillator

### Block Diagram

```
         ┌────────────────────────────────┐
         │                                │
         ↓                                │
─────[−ω₀²]────[INT]────[INT]────┬────────┘
                 │        │      │
                x'        x      └─── output
```

### Circuit Implementation

```
              C₁                    C₂
         ┌────||────┐          ┌────||────┐
         │          │          │          │
         │          │          │          │
x ───────/\/\/──────┼──────────/\/\/──────┼─┬── x
     R_ω            │      R             │ │
                    │                    │ │
    ┌───────────(-)─┤              ┌────(-)┤
    │               │              │      │
    │         OP1   ├──────────────│  OP2 ├──── x
    │               │     x'       │      │
    │          ┌───(+)             │ ┌───(+)
    │          │                   │ │
    │         ─┴─                  │─┴─
    │         GND                  GND
    │                              │
    └──────────────────────────────┘
        (feedback through R_ω)
```

### Setting Frequency

```
ω₀ = 1/(R_ω · C₁) assuming τ₁ = τ₂

For f₀ = 1 Hz:
  ω₀ = 2π
  R_ω · C = 1/(2π) ≈ 0.159

With C = 1μF: R_ω = 159kΩ
```

### Initial Conditions

To start oscillation, need non-zero energy:
- Set x(0) ≠ 0 (initial displacement), or
- Set x'(0) ≠ 0 (initial velocity)

If both ICs are zero, output stays at zero!

## Wien Bridge Oscillator

### Circuit

```
                Rf
           ┌────/\/\/────┐
           │             │
           │    Lamp     │ (AGC element)
           ├────────────────┐
           │                │
           │         ┌─────(-)──┐
           │         │          │
     ┌─────┴─────────┤    OP    ├───┬── Vout
     │               │          │   │
     │          ┌───(+)─────────┘   │
     │          │                   │
     │         ═╪═ C                │
     │          │                   │
     │         /\/\/ R               │
     │          │                   │
     │          ├───────────────────┘
     │          │
     │         /\/\/ R
     │          │
     │         ═╪═ C
     │          │
     │         ─┴─ GND
     └────────────────────────────────
```

### How It Works

- RC network provides frequency-selective feedback
- Positive feedback at one frequency (f = 1/(2πRC))
- AGC (lamp) limits amplitude to prevent clipping

### Frequency

```
f₀ = 1/(2πRC)

For f = 1kHz with C = 10nF:
R = 1/(2π × 1000 × 10×10⁻⁹) = 15.9kΩ
```

## Phase-Shift Oscillator

### Circuit

```
           Rf
      ┌────/\/\/────┐
      │             │
      ├─────────────┤
      │             │
      │      ┌─────(-)──┐
      │      │          │
      └──────┤    OP    ├───┬── Vout
             │          │   │
        ┌───(+)─────────┘   │
        │                   │
       ─┴─ GND              │
                            │
   ┌────────────────────────┘
   │
   ├──||──/\/\/──┬──||──/\/\/──┬──||──/\/\/──┐
   │   C    R    │   C    R    │   C    R    │
   │             │             │             │
  ─┴─           ─┴─           ─┴─           ─┴─
  GND           GND           GND           GND
```

### Design

Three RC sections, each provides 60° phase shift at oscillation frequency.

```
f₀ = 1/(2π√6·RC)

Gain required: |Av| ≥ 29
```

## Quadrature Oscillator

### Special Feature

Produces both sine AND cosine outputs (90° apart).

### Circuit

```
              C                    C
         ┌────||────┐         ┌────||────┐
         │          │         │          │
         │          │         │          │
────/\/\/┴─────(-)──┤         │     ┌────┴─────(-)──┐
    R               │         │     │               │
              OP1   ├─────────/\/\/─┤         OP2   ├──── cos
                    │    R    │                     │
         ┌─────(+)──┘         └─────────────────────┼──── sin
         │                                          │
        ─┴─ GND                                     │
                                                    │
         ┌──────────────────────────────────────────┘
         │
         └── (feedback to first integrator input)
```

### Outputs

- OP1 output: cos(ω₀t)
- OP2 output: sin(ω₀t)

Useful for coordinate transformations, modulation.

## Voltage-Controlled Oscillator (VCO)

### Concept

Frequency varies with control voltage.

### Implementation

Replace fixed frequency-setting resistor with voltage-controlled element:
- FET as variable resistor
- OTA (operational transconductance amplifier)
- Multiplying DAC

### Applications

- FM modulation
- Phase-locked loops
- Frequency sweeping
- Voltage-to-frequency conversion

## Relaxation Oscillators

### Triangle/Square Generator

```
         ┌───────────────────────────────────────┐
         │                                       │
         │    ┌─────────────────────────────────────┐
         │    │                                  │  │
         ↓    │                                  │  │
────[Schmitt]─┴──[INT]──┬────────────────────────┘  │
        │               │                           │
        │               └── Triangle out            │
        │                                           │
        └── Square out                              │
                                                    │
           ┌────────────────────────────────────────┘
           │
           └── (Square feeds back to integrator)
```

### Operation

1. Schmitt trigger outputs +V or -V
2. Integrator ramps up or down
3. When integrator output reaches threshold, Schmitt flips
4. Cycle repeats

### Frequency Control

```
f = 1/(4RC) × (V_threshold/V_saturation)
```

## Amplitude Stability

### The Problem

Ideal oscillators have constant amplitude, but:
- Component tolerances cause slight gain errors
- Gain > 1: amplitude grows until clipping
- Gain < 1: amplitude decays to zero

### Solutions

#### 1. Limiting (Clipping)
Add diode limiters in feedback:
```
           Rf
      ┌────/\/\/──┬───┐
      │          ─┴─  │
      │           ▲   │
      │          ─┴─  │
      │           ▲   │
      │           │   │
     (-)──────────┴───┴── Vout
```

Simple but adds distortion.

#### 2. AGC (Automatic Gain Control)
Vary gain element based on output amplitude:
```
Vout ──[Rectifier]──[LPF]──[Gain Control]
                              │
                              ▼
                     (varies Rf or lamp resistance)
```

Cleaner sine wave, more complex.

#### 3. Lamp Stabilization
Incandescent lamp in feedback (Wien bridge):
- Lamp resistance increases with temperature
- As amplitude increases, lamp heats, R increases, gain decreases
- Natural AGC with thermal time constant

## Practical Considerations

### Starting Oscillation

If oscillation doesn't start:
- Apply initial condition
- Momentarily disturb a node
- Ensure gain slightly > 1 at startup

### Frequency Accuracy

Depends on:
- Component tolerances (R, C)
- Temperature coefficients
- Op-amp frequency response

For precision: Use crystal oscillator or PLL.

### Distortion

Sources:
- Op-amp nonlinearity
- Amplitude limiting
- Component saturation

Minimize by:
- Operating at low amplitude
- Using quality op-amps
- Soft limiting (AGC)

## Applications in Analog Computing

### Test Signal Generation

- Sine waves for frequency response
- Square waves for step response
- Triangle waves for linearity testing

### Function Generation

- Quadrature outputs for resolvers
- Sweep for spectral analysis

### Simulation

- Model periodic forcing functions
- Generate carrier for modulation
- Timing signals

## Example: Build a 1Hz Sine Oscillator

### Components

| Part | Value |
|------|-------|
| Op-amps | 2× OP07 or OPA2277 |
| Resistors | 2× 100kΩ |
| Capacitors | 2× 1.6μF (or 1μF + 0.56μF) |
| Trim pot | 1× 50kΩ |

### Time Constant

```
ω₀ = 2π for 1 Hz
τ = 1/ω₀ = 0.159s
RC = 0.159s

With R = 100kΩ: C = 1.59μF
```

### Procedure

1. Build two integrators
2. Connect output of INT2 to input of INT1 (with sign inversion)
3. Connect output of INT1 to input of INT2
4. Set ICs: INT1 = 0V, INT2 = 5V
5. Observe sine wave on oscilloscope

## References

[^1]: [Electronic Oscillator - Wikipedia](https://en.wikipedia.org/wiki/Electronic_oscillator)
[^2]: [Wien Bridge Oscillator - Wikipedia](https://en.wikipedia.org/wiki/Wien_bridge_oscillator)
[^3]: [Phase-Shift Oscillator - Wikipedia](https://en.wikipedia.org/wiki/Phase-shift_oscillator)
[^4]: [Relaxation Oscillator - Electronics Tutorials](https://www.electronics-tutorials.ws/waveforms/generators.html)

## Further Reading

- [Mass-Spring-Damper](03-mass-spring-damper.md)
- [Chaos and Attractors](05-chaos-attractors.md)
- [Signal Processing](../04-applications/04-signal-processing.md)
