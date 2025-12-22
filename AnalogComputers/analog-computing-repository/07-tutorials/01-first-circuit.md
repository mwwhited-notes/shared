# Building Your First Analog Computer Circuit

## Overview

This tutorial guides you through building a simple analog computing circuit: an inverting amplifier that forms the foundation of all analog computer operations.

## Prerequisites

### Knowledge
- Basic understanding of Ohm's law
- Familiarity with breadboard usage
- Understanding of voltage and current

### Equipment
- Breadboard
- Multimeter (DVM)
- ±12V or ±15V dual power supply
- Oscilloscope (helpful but not required)
- Function generator (for testing)

### Components
- 1× TL071 or TL074 op-amp
- 2× 10kΩ resistors (1% tolerance preferred)
- 0.1μF ceramic capacitors (for decoupling)
- Hook-up wire (22 AWG solid core)
- Banana plug patch cords (optional)

## Step 1: Understanding the Circuit

### The Inverting Amplifier

```
           Rf (10kΩ)
      ┌────/\/\/────┐
      │             │
      │      ┌─────(-)──┐
Vin ──/\/\/──┤          │
       Rin   │   TL071  ├── Vout = -(Rf/Rin)×Vin
      (10kΩ) │          │
             │          │
        ┌───(+)─────────┘
        │
       ─┴─ GND
```

### What It Does

- Multiplies input by -1 (unity gain inverter)
- Output voltage = negative of input voltage
- +5V in → -5V out
- -3V in → +3V out

### Why This Matters

The inverter is the simplest op-amp circuit and demonstrates:
- Negative feedback
- Virtual ground concept
- Gain setting with resistors

## Step 2: Breadboard Layout

### Power Rails

```
+12V ────────────────────────────── (+) rail
GND  ────────────────────────────── GND rail
-12V ────────────────────────────── (-) rail
```

### Op-Amp Pinout (TL071, 8-pin DIP)

```
        ┌───────────┐
    NC ─┤ 1       8 ├─ NC
     - ─┤ 2       7 ├─ V+
     + ─┤ 3       6 ├─ Vout
    V- ─┤ 4       5 ├─ NC
        └───────────┘
```

### Breadboard Wiring

```
Row:  1  2  3  4  5  6  7  8  9  10 11 12 13
      │  │  │  │  │  │  │  │  │  │  │  │  │
+12V ─┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴─
      │  │  │  │  │  │  │  │  │  │  │  │  │
      │  │  │  │  │  │  │  │  │  │  │  │  │
      │  │  │  ●──●──●──●──●  │  │  │  │  │   ← Row E
      │  │  │  │  │  │  │  │  │  │  │  │  │
      │  │  │   [TL071 here]  │  │  │  │  │   ← Rows E-F
      │  │  │  ●──●──●──●──●  │  │  │  │  │   ← Row F
      │  │  │  │  │  │  │  │  │  │  │  │  │
      │  │  │  │  │  │  │  │  │  │  │  │  │
-12V ─┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴─

Connections:
- Pin 7 (V+) → +12V rail
- Pin 4 (V-) → -12V rail
- Pin 3 (+) → GND rail
```

## Step 3: Add Power Supply Decoupling

### Why Decoupling?

Prevents oscillation and noise pickup.

### Placement

```
+12V ──┬──── to pin 7
       │
      ═╪═ 0.1μF (ceramic)
       │
       ├──── GND
       │
      ═╪═ 0.1μF (ceramic)
       │
-12V ──┴──── to pin 4
```

Place capacitors as close to IC as possible.

## Step 4: Add Input and Feedback Resistors

### Resistor Placement

```
         ←──── Rf (10kΩ) ────→
         │                   │
         ├───────────────────┤
         │                   │
Vin ─────/\/\/───────────────┤  (pin 2, inverting input)
         Rin (10kΩ)          │
                             │
                             └── Vout (pin 6)
```

### Wiring Steps

1. Connect one end of Rin to your input terminal
2. Connect other end of Rin to pin 2 (inverting input)
3. Connect one end of Rf to pin 2
4. Connect other end of Rf to pin 6 (output)
5. Verify pin 3 (+) is connected to GND

## Step 5: Power Up and Test

### Initial Power-Up

1. Double-check all connections
2. Set power supply current limit to 100mA
3. Turn on power supply
4. Verify:
   - No excessive current draw (<50mA)
   - No components getting hot
   - Op-amp power pins at correct voltage

### DC Test

1. Connect input (Vin) to GND
2. Measure output voltage
3. Should be very close to 0V (within ±50mV)
4. If large offset, check wiring

### Gain Test

1. Connect input to a known voltage (use voltage divider from power rail)
2. For +2V input, expect -2V output
3. For -3V input, expect +3V output
4. Verify gain is -1.00 (within 1%)

### Signal Test (with function generator)

1. Apply 1kHz sine wave, 2Vpp
2. Observe output on oscilloscope
3. Should see inverted sine wave, same amplitude
4. Check for distortion (should be clean)

## Step 6: Modify for Variable Gain

### Adding Gain Adjustment

Replace Rf with series combination:
```
           Rpot (10kΩ)    Rf2 (10kΩ)
      ┌────────⦿────────/\/\/────┐
      │                          │
     pin 2                      pin 6
```

### Gain Range

- Pot at minimum: Gain = -1 (Rf = 10kΩ)
- Pot at maximum: Gain = -2 (Rf = 20kΩ)

### Using 100kΩ Pot

For wider range:
- Minimum: Gain = -1
- Maximum: Gain = -11

## Troubleshooting

### Output Stuck at +V or -V Rail

| Possible Cause | Solution |
|----------------|----------|
| Positive feedback (wrong input) | Check pin 2 vs pin 3 |
| No negative feedback | Verify Rf connected |
| Input signal too large | Reduce input |
| Power supply problem | Check ±12V |

### Output is Zero Regardless of Input

| Possible Cause | Solution |
|----------------|----------|
| No power to op-amp | Check pins 4, 7 |
| Rin not connected | Verify input resistor |
| Output shorted | Check for short |

### Oscillation

| Possible Cause | Solution |
|----------------|----------|
| No decoupling | Add 0.1μF caps |
| Long feedback path | Shorten wires |
| Breadboard capacitance | Use different rows |

### Large Offset

| Possible Cause | Solution |
|----------------|----------|
| Normal for op-amp | Within spec if <10mV |
| Wrong resistor values | Verify with multimeter |
| Damaged op-amp | Replace IC |

## Next Steps

### Build a Summer

Add more input resistors:
```
V1 ──/\/\/──┬──(-)── OP ── Vout = -(V1 + V2 + V3)
V2 ──/\/\/──┤
V3 ──/\/\/──┘
```

### Build an Integrator

Replace Rf with capacitor:
```
Vin ──/\/\/──┬──||──── Vout = -∫Vin dt / RC
             │    C
            (-)
```

See [Solving a Simple ODE Tutorial](02-simple-ode.md)

## Key Takeaways

1. **Virtual ground:** Pin 2 stays at ~0V due to feedback
2. **Current flows through both resistors:** I = Vin/Rin = -Vout/Rf
3. **Decoupling is essential:** Prevents oscillation
4. **Check before power:** Verify wiring carefully
5. **Precision matters:** Use 1% resistors for accuracy

## Parts List Summary

| Component | Quantity | Value | Notes |
|-----------|----------|-------|-------|
| TL071/TL074 | 1 | - | 8-pin DIP |
| Resistor | 2 | 10kΩ | 1% metal film |
| Capacitor | 2 | 0.1μF | Ceramic, decoupling |
| Breadboard | 1 | - | Half-size OK |
| Wire | - | 22 AWG | Solid core |
| Power supply | 1 | ±12V | Current limited |

## References

[^1]: [Operational Amplifier - Wikipedia](https://en.wikipedia.org/wiki/Operational_amplifier)
[^2]: [Inverting Amplifier Tutorial - Electronics Tutorials](https://www.electronics-tutorials.ws/opamp/opamp_2.html)
[^3]: [TL071 Datasheet - Texas Instruments](https://www.ti.com/lit/ds/symlink/tl071.pdf)
[^4]: [Breadboard Basics - SparkFun](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

## Further Reading

- [Op-Amp Basics](../01-fundamentals/02-op-amp-basics.md)
- [Summers and Inverters](../02-components/01-summers-inverters.md)
- [Solving a Simple ODE](02-simple-ode.md)
