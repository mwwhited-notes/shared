# Circuit Symbols and Conventions

## Standard Computing Element Symbols

### Integrator

```
     ┌───────────┐
     │    ∫      │
─────┤           ├─────
     │    τ      │
     └───────────┘

Input left, output right
τ = time constant (optional label)
```

**Function:** Vout = -(1/τ)∫Vin dt

### Summer (Adder)

```
     ┌───────────┐
─────┤           │
     │    Σ      ├─────
─────┤           │
     │           │
─────┤           │
     └───────────┘

Multiple inputs left, one output right
```

**Function:** Vout = -(V1 + V2 + V3)

### Inverter

```
     ┌───────────┐
     │           │
─────┤    -1     ├─────
     │           │
     └───────────┘
```

**Function:** Vout = -Vin

### Amplifier (with gain)

```
     ┌───────────┐
     │           │
─────┤    -k     ├─────
     │           │
     └───────────┘

k = gain factor (may be >1 or <1)
```

**Function:** Vout = -k × Vin

### Potentiometer (Coefficient)

```
         ↓ (reference)
         │
        ┌┴┐
        │k│
        └┬┘
         │
         └─────→ output = k × reference
```

Or as block:
```
     ┌───────────┐
     │           │
─────┤    ×k     ├─────
     │           │
     └───────────┘

k = 0 to 1 (typical)
```

### Multiplier

```
     ┌───────────┐
─────┤     ×     ├─────
     │           │
─────┤           │
     └───────────┘

Two inputs left, one output right
```

**Function:** Vout = (V1 × V2)/10

### Divider

```
     ┌───────────┐
─────┤     ÷     ├─────
     │           │
─────┤           │
     └───────────┘

Numerator and denominator inputs
```

### Comparator

```
     ┌───────────┐
─────┤     >     ├─────
     │           │
─────┤           │
     └───────────┘

Outputs high if top input > bottom input
```

### Function Generator

```
     ┌───────────┐
     │   f(x)    │
─────┤           ├─────
     │           │
     └───────────┘

f(x) labels the specific function
```

## Block Diagram Conventions

### Signal Flow

```
─────────→
Signals flow left to right (generally)
Arrow indicates direction
```

### Summing Junction

```
        V1
         │
         ↓
    ───→ ⊕ ───→ output
         ↑
         │
        V2

Circle with + or − at each input
```

### Feedback Path

```
    ┌──────────────────────────────┐
    │                              │
    │   ┌───────┐    ┌───────┐    │
    └──→│       │───→│       │───┬┘
        │   A   │    │   B   │   │
    ───→│       │    │       │   └───→ output
        └───────┘    └───────┘
            ↑
            │
         feedback
```

### Takoff Point

```
                    ┌───→ (to another input)
                    │
─────────────┬──────┴───→ (continues)
             │
             └───→ (to another input)

Signal branches at junction point
```

## Electrical Schematic Symbols

### Operational Amplifier

```
         ┌─────────
    (-)──┤−
         │    ▷────── output
    (+)──┤+
         └─────────
```

Or detailed:
```
              V+
              │
         ┌────┴────┐
    (-)──┤−        ├──── output
         │    A    │
    (+)──┤+        │
         └────┬────┘
              │
              V-
```

### Resistor

```
    ────/\/\/──── (zigzag style)
    ────████───── (rectangle style)
```

### Capacitor

```
    ────||────  (non-polarized)
    ───||+──── (polarized, electrolytic)
         │
```

### Potentiometer

```
        ↓ wiper
    ────┤├────
        │ (arrow indicates wiper)
```

Or:
```
    A ───┬───
        ┌┴┐
        │ │
        │●│← wiper
        │ │
        └┬┘
    B ───┴───
```

### Diode

```
    ────►|────  (standard)
    ────|◄────  (reverse)
```

### Ground

```
    ─┴─  (earth ground)
    ─▽─  (chassis ground)
    ─○─  (signal common)
```

### Power Supply

```
    +V ────
    -V ────
    GND ───┴───
```

## Analog Computer Panel Symbols

### Mode Control

```
    [IC]  Initial Condition (Reset)
    [OP]  Operate (Compute)
    [HD]  Hold (Freeze)
```

### Time Scale

```
    [SLOW]  Longer time constant
    [FAST]  Shorter time constant
```

### Reference Voltages

```
    [+REF]  Positive reference (+10V typical)
    [-REF]  Negative reference (-10V typical)
    [GND]   Ground reference (0V)
```

## Common Abbreviations

| Abbreviation | Meaning |
|--------------|---------|
| INT | Integrator |
| SUM | Summer |
| INV | Inverter |
| MULT | Multiplier |
| DIV | Divider |
| POT | Potentiometer |
| COMP | Comparator |
| FG | Function Generator |
| IC | Initial Condition |
| OP | Operate |
| REF | Reference |

## Color Coding (Typical)

| Color | Meaning |
|-------|---------|
| Red | Positive voltage, V+ |
| Blue/Black | Negative voltage, V- |
| Green | Ground |
| Yellow | Signal paths |
| White | Output signals |

## Mathematical Notation

### Derivatives

```
x' or ẋ = dx/dt (first derivative)
x'' or ẍ = d²x/dt² (second derivative)
```

### Integration

```
∫x dt = integral of x with respect to time
```

### Transfer Function

```
H(s) = Output(s)/Input(s) in Laplace domain
H(jω) = Frequency response
```

## Pin Numbering (8-pin DIP Op-Amp)

```
        ┌───────┐
    NC ─┤ 1   8 ├─ NC
     - ─┤ 2   7 ├─ V+
     + ─┤ 3   6 ├─ Output
    V- ─┤ 4   5 ├─ Offset null
        └───────┘

(Standard pinout: 741, TL071, OP07, etc.)
```

## Further Reading

- [Op-Amp Basics](../01-fundamentals/02-op-amp-basics.md)
- [Components Section](../02-components/)
