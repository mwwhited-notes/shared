# Potentiometers and Coefficient Units

## Overview

Potentiometers (pots) are the primary means of setting coefficients and scaling factors in analog computers. They allow precise control over gains, time constants, and equation parameters.

## Potentiometer Fundamentals

### Basic Operation

A potentiometer is a three-terminal variable resistor[^1]:

```
    Terminal A ──┬──
                 │
                ┌┴┐
                │ │ ← Resistance element
                │ │
                │●│ ← Wiper (movable contact)
                │ │
                └┬┘
                 │
    Terminal B ──┴──

    Wiper ──────────── Variable output
```

### Voltage Divider Configuration

Most common in analog computing:

```
Vin ────┬────
        │
       ┌┴┐
       │ │
       │●├──── Vout = k × Vin
       │ │
       └┬┘
        │
       ─┴─
       GND

Where: k = position (0 to 1)
```

### Rheostat Configuration

Used for current control:

```
Vin ────┬────
        │
       ┌┴┐
       │ │
       │●├──── Vout
       │ │
       └─┘
        (B terminal unused or connected to wiper)

Resistance = R × k
```

## Potentiometer Types for Analog Computing

### Single-Turn Potentiometers

| Parameter | Specification |
|-----------|---------------|
| Rotation | 270° - 300° |
| Resolution | ~5% |
| Linearity | 1-5% |
| Use | Coarse adjustment, teaching |

### Multi-Turn Potentiometers

| Turns | Resolution | Linearity | Use |
|-------|------------|-----------|-----|
| 3-turn | ~0.5% | 0.25% | General purpose |
| 10-turn | ~0.1% | 0.1% | Precision computing |
| 15-turn | ~0.05% | 0.05% | High precision |

**10-Turn with Dial Counter:**
```
    ┌─────────────┐
    │  ╔═══════╗  │
    │  ║ 0.347 ║  │ ← Digital readout
    │  ╚═══════╝  │
    │     ◎       │ ← 10-turn shaft
    │   COEFF    │
    └─────────────┘
```

### Precision Characteristics

| Type | Resolution | Linearity | Temp Coeff |
|------|------------|-----------|------------|
| Wirewound | 0.01% | 0.02% | 20-50 ppm/°C |
| Cermet | 0.1% | 0.1% | 100 ppm/°C |
| Conductive Plastic | 0.5% | 0.1% | 500 ppm/°C |
| Carbon | 1% | 2% | 1000 ppm/°C |

## Coefficient Setting Units

### Basic Coefficient Pot

```
+10V Reference ──┬────
                 │
                ┌┴┐
                │ │
                │●├──── Coefficient × 10V
                │ │
                └┬┘
                 │
                ─┴─
                GND
```

Output = k × 10V, where k is pot setting (0.000 to 1.000)

### Signed Coefficient Unit

For negative coefficients:

```
+10V ──┬────                    -10V ──┬────
       │                               │
      ┌┴┐                             ┌┴┐
      │ │                             │ │
      │●├──┐                      ┌───┤●│
      │ │  │                      │   │ │
      └┬┘  │                      │   └┬┘
       │   │                      │    │
      ─┴─  │    ┌────────┐       │   ─┴─
      GND  └────┤ Switch ├───────┘   GND
                │ +/-    │
                └───┬────┘
                    │
                    └──── Signed coefficient output
```

### Buffered Coefficient Unit

Prevents loading effects:

```
Reference ──┬────
            │
           ┌┴┐
           │ │
           │●├────(+)──┐
           │ │         │
           └┬┘    OP   ├── Buffered output
            │          │
           ─┴─   (-)───┴── (unity gain buffer)
           GND    │
                  ▼
                 GND
```

## Loading Effects

### Problem

When a pot feeds a load, the output is affected:

```
Ideal: Vout = k × Vin

With load RL: Vout = k × Vin × RL / (RL + k(1-k)×Rpot)
```

### Maximum Error

Loading error is worst at k = 0.5:
```
Error(max) ≈ Rpot / (4 × RL)

For Rpot = 10kΩ, RL = 100kΩ:
Error ≈ 10k / 400k = 2.5%
```

### Solutions

1. **Use buffered pots** (op-amp follower)
2. **Choose Rpot << RL** (e.g., 1kΩ pot with 100kΩ input)
3. **Calibrate at operating point**

## Setting Coefficients Accurately

### Using Digital Voltmeter

1. Apply reference voltage to pot
2. Measure output with DVM
3. Adjust until Vout = k × Vref

```
Example: Set k = 0.347 with +10V reference
Target: Vout = 3.470V ± 1mV
```

### Using Null Method

For higher precision:

```
                    ┌─────────┐
Pot output ─────────┤-        │
                    │  NULL   ├── Null detector
Reference (scaled) ─┤+  DET   │   (galvanometer/scope)
                    └─────────┘
```

Adjust pot until null detector shows zero.

### Calibration Curve

For precision work, create calibration table:

| Dial Reading | Actual k | Error |
|--------------|----------|-------|
| 0.100 | 0.1003 | +0.03% |
| 0.200 | 0.2001 | +0.01% |
| 0.500 | 0.5002 | +0.02% |
| 0.800 | 0.7998 | -0.02% |
| 1.000 | 1.0001 | +0.01% |

## Special Coefficient Configurations

### Coefficient Greater Than 1

When k > 1 is needed, combine pot with amplifier gain:

```
For k = 3.47:
  Use k = 0.347 with gain of 10
  Or k = 0.694 with gain of 5
```

### Variable Time Constant

Using pot in integrator:

```
Reference ──┬────            C
            │           ┌───||───┐
           ┌┴┐          │        │
           │ │          │        │
           │●├───/\/\/──┴───────(-)──┐
           │ │     Rf              │
           └┬┘               OP    ├── Integrator output
            │                      │
           ─┴─            ┌───(+)──┘
           GND            │
                          ▼
                         GND
```

Time constant τ varies with pot setting.

### Coefficient Servo

For remote or automatic coefficient setting:

```
            ┌───────────┐
Command ────┤   Servo   ├───┬── Pot shaft
            │  Motor    │   │
            └───────────┘   │
                            │
                           ┌┴┐
                           │●│ ← Pot follows command
                           └─┘
```

## Digital Potentiometers

### Overview

Replace mechanical pots with electronic control[^2]:

```
                ┌─────────────────┐
Reference ──────┤ A               │
                │    Digital      │
    GND ────────┤ B     Pot       ├── Wiper output
                │                 │
                │   SPI/I2C Bus   │
                └────────┬────────┘
                         │
                    To controller
```

### Comparison

| Parameter | Mechanical | Digital |
|-----------|------------|---------|
| Resolution | 0.01% (10T) | 8-12 bit (0.4%-0.02%) |
| Setting Speed | Manual | Microseconds |
| Repeatability | Wear dependent | Perfect |
| Temperature | 20-50 ppm/°C | 1-100 ppm/°C |
| Wiper current | High | Limited (1-5 mA) |
| Power consumption | Zero | Few mW |
| Cost | Low | Medium |

### Common Digital Pot ICs

| Device | Resolution | Interface | Resistance |
|--------|------------|-----------|------------|
| MCP4131 | 7-bit | SPI | 5k-100k |
| AD5290 | 8-bit | SPI | 10k-50k |
| AD5241 | 8-bit | I2C | 10k-1M |
| AD5270 | 10-bit | SPI | 20k-50k |
| AD5293 | 10-bit | SPI | 20k-100k |

## Practical Considerations

### Warm-Up Time

Allow potentiometers to stabilize:
- Wirewound: 15-30 minutes
- Cermet: 5-10 minutes
- Digital: Immediate

### Mechanical Considerations

- Avoid mechanical shock after setting
- Lock adjustment screws
- Use shaft locks for critical settings
- Consider sealed pots for long-term stability

### Environmental Effects

| Factor | Effect | Mitigation |
|--------|--------|------------|
| Temperature | Resistance drift | Use low TC pots, temperature control |
| Humidity | Resistance change | Sealed/conformal coated units |
| Vibration | Setting shifts | Locking mechanisms |
| Age | Wear, oxidation | Regular recalibration |

### Noise

Potentiometers can introduce noise:
- Wiper noise (especially carbon)
- Thermal noise
- Contact resistance variations

**Solutions:**
- Use wirewound or cermet
- Add filtering on output
- Avoid frequent adjustment during operation

## Documentation Format

Standard coefficient documentation:

```
COEFFICIENT TABLE
═══════════════════════════════════════════════════════
Pot # | Parameter    | Value | Dial   | Notes
═══════════════════════════════════════════════════════
P1    | Damping (b)  | 0.250 | 2.500  | Fixed for all runs
P2    | Stiffness(k) | 0.800 | 8.000  | Vary 0.4-1.0
P3    | Force scale  | 0.100 | 1.000  | Fixed
P4    | Time scale   | 1.000 | 10.00  | Real time
═══════════════════════════════════════════════════════
```

## References

[^1]: [Potentiometer - Wikipedia](https://en.wikipedia.org/wiki/Potentiometer)
[^2]: [Digital Potentiometer - Wikipedia](https://en.wikipedia.org/wiki/Digital_potentiometer)

## Further Reading

- [Scaling and Normalization](../01-fundamentals/05-scaling.md)
- [Programming and Patching](../01-fundamentals/04-programming-patching.md)
