# Scaling and Normalization

## Why Scaling Matters

Analog computers operate within fixed voltage limits, typically ±10V or ±100V. Scaling ensures that:

1. **Variables stay within range**: Prevents op-amp saturation
2. **Accuracy is maximized**: Uses full voltage range
3. **Coefficients are realizable**: Values between 0 and 1 for pots
4. **Time scales are practical**: Matches observation requirements

## Types of Scaling

### 1. Magnitude Scaling (Amplitude Scaling)

Relates physical variables to computer voltage:

```
x_computer = a × x_physical

where: a = scale factor (V per physical unit)
```

**Example:**
- Physical displacement: 0 to 2 meters
- Computer voltage: 0 to 10V
- Scale factor: a = 5 V/m
- Computer variable: [x] = 5x meters → volts

### 2. Time Scaling

Relates computer time to physical time:

```
τ_computer = β × t_physical

where: β = time scale factor
```

**Examples:**
- β = 1: Real time
- β = 10: Computer runs 10× faster
- β = 0.1: Computer runs 10× slower

### 3. Coefficient Scaling

Adjusts equation coefficients to be within potentiometer range (0 to 1):

```
If coefficient k > 1:
    Split into: k = n × k'
    where n = gain (integer), k' = pot setting < 1
```

## The Scaling Procedure

### Step 1: Identify Variable Ranges

For each variable in your equation, determine:
- Maximum expected value
- Minimum expected value
- Typical operating range

**Example: Damped Oscillator**
```
m·x'' + b·x' + k·x = F(t)

Variables:
- x: position, range ±2 m
- x': velocity, range ±10 m/s
- x'': acceleration, range ±50 m/s²
- F: force, range 0-20 N
```

### Step 2: Define Scale Factors

Choose scale factors so maximum values approach (but don't exceed) computer limits:

```
Machine unit (MU) = typically 10V

Scale factor = MU / |max physical value|
```

**Example (continued):**
```
[x] = 10V / 2m = 5 V/m
[x'] = 10V / 10(m/s) = 1 V/(m/s)
[x''] = 10V / 50(m/s²) = 0.2 V/(m/s²)
[F] = 10V / 20N = 0.5 V/N
```

### Step 3: Substitute Scaled Variables

Replace physical variables with computer variables:

```
Let: X = [x]·x, X' = [x']·x', etc.

Original: m·x'' + b·x' + k·x = F
Scaled:   m·(X''/[x'']) + b·(X'/[x']) + k·(X/[x]) = F/[F]·[F]
```

### Step 4: Rearrange and Simplify

```
X'' = [x'']/m · {[F]·F_computer - b·[x']/[x'']·X' - k·[x]/[x'']·X}
```

### Step 5: Calculate Coefficient Values

Substitute numerical values and compute pot settings:

```
Given: m=1, b=0.5, k=4

Coefficient for F: [x'']/m·[F] = 0.2/1·0.5 = 0.1
Coefficient for X': [x'']/m·b·[x']/[x''] = 0.2·0.5·1/0.2 = 0.5
Coefficient for X: [x'']/m·k·[x]/[x''] = 0.2·4·5/0.2 = 20 → needs gain!
```

### Step 6: Handle Out-of-Range Coefficients

When coefficients exceed 1.0:

**Method 1: Use Amplifier Gain**
```
20 = 10 × 2.0 → Gain of 10, pot = 0.200
   or
20 = 20 × 1.0 → Gain of 20, pot = 1.000
```

**Method 2: Rescale Variables**
```
Choose larger [x] to reduce coefficient
```

**Method 3: Use Multiple Pots in Series**
```
20 = 5 × 4 × 1.0 → Two stages
```

## Time Scaling Details

### Computing with Time Scaling

Integrator time constant: τ = RC

```
Without time scaling: dx/dt → X/τ
With time scaling β:   dx/dt → β·X/τ
```

To run faster (β > 1): Decrease RC
To run slower (β < 1): Increase RC

### Standard Time Constants

| RC Value | Time Constant | Typical Use |
|----------|---------------|-------------|
| 0.1 s | Fast | Quick transients |
| 1.0 s | Standard | Normal operation |
| 10 s | Slow | Slow processes |
| 100 s | Very slow | Long-term dynamics |

### Time Scaling Example

**Problem:** Simulate thermal process with time constant of 1 hour
**Computer:** Needs result in 10 seconds

```
β = computer_time / real_time = 10s / 3600s = 1/360

Time scale factor: 360:1 (360× faster)

Integrator RC = (1 second) / 360 = 2.78 ms
```

## Practical Scaling Worksheet

### Scaling Template

```
VARIABLE SCALING TABLE
═══════════════════════════════════════════════════
Variable    | Physical Max | Scale Factor | Computer Max
═══════════════════════════════════════════════════
x           |              | [x] =        | = 10V (check)
x'          |              | [x'] =       | = 10V (check)
x''         |              | [x''] =      | = 10V (check)
...         |              |              |
═══════════════════════════════════════════════════

COEFFICIENT TABLE
═══════════════════════════════════════════════════
Term        | Raw Coeff    | Scaled Coeff | Pot Setting | Gain
═══════════════════════════════════════════════════
            |              |              |             |
═══════════════════════════════════════════════════

TIME SCALING
═══════════════════════════════════════════════════
Physical time span:
Desired computer time:
Time scale factor β:
Standard RC:
Scaled RC:
═══════════════════════════════════════════════════
```

## Common Scaling Strategies

### Strategy 1: Normalized Variables

Divide all variables by their maximum expected values:

```
x_norm = x / x_max   (dimensionless, range ±1)
Computer: X = 10V × x_norm  (range ±10V)
```

**Advantage:** Simple, intuitive
**Disadvantage:** May not use full dynamic range

### Strategy 2: Ratio of Scale Factors

Express all coefficients as ratios:

```
If equation has: a·x + b·y + c·z = 0

Scale factors: [x], [y], [z]

Coefficients become: a·[x]/[y], b, c·[z]/[y]
(normalizing to coefficient of y)
```

### Strategy 3: Energy Scaling

For physical systems, scale by energy relationships:

```
Kinetic energy: (1/2)mv²
Potential energy: (1/2)kx²

Scale so: [v]² = (k/m)·[x]²
```

## Checking Your Scaling

### Verification Checklist

1. **Dimensional Analysis**
   - All terms in equation have same scaled units
   - Scale factors cancel correctly

2. **Range Check**
   - All variables stay within ±1 MU (10V) for expected inputs
   - Allow 20% margin for unexpected excursions

3. **Coefficient Check**
   - All pot settings between 0.001 and 0.999
   - Gains are realizable (1, 2, 4, 5, 10 typical)

4. **Time Check**
   - Fastest dynamics visible on output device
   - Slowest dynamics complete in reasonable time

### Overload Detection

Signs of poor scaling:
- Output "clipping" at ±10V
- Flat tops on waveforms
- Overload indicators lit
- Distorted or asymmetric response

**Solution:** Reduce scale factor for overloaded variable

### Underutilization

Signs of poor scaling:
- Very small signals (< 1V peak)
- Poor signal-to-noise ratio
- Difficulty reading values

**Solution:** Increase scale factor

## Scaling Example: Van der Pol Oscillator

**Equation:**
```
x'' - μ(1 - x²)x' + x = 0
```

**Parameter:** μ = 1

**Step 1: Estimate ranges**
- Limit cycle amplitude: |x| ≤ 2
- Velocity: |x'| ≤ 3
- Acceleration: |x''| ≤ 6

**Step 2: Scale factors (for ±10V)**
```
[x] = 10/2 = 5 V/unit
[x'] = 10/3 ≈ 3 V/unit
[x''] = 10/6 ≈ 1.5 V/unit
```

**Step 3: Scaled equation**
```
X''/[x''] - μ(1 - (X/[x])²)·X'/[x'] + X/[x] = 0

X'' = [x'']{μ(1 - X²/[x]²)·X'/[x'] - X/[x]}
```

**Step 4: Coefficients**
```
For x' term: μ·[x'']/[x'] = 1·1.5/3 = 0.5 ✓
For x term: [x'']/[x] = 1.5/5 = 0.3 ✓
For x² term: 1/[x]² = 1/25 = 0.04 ✓
```

All coefficients are in range!

## References

[^1]: Korn, Granino A. and Korn, Theresa M. *Electronic Analog and Hybrid Computers*. McGraw-Hill, 1972.
[^2]: [Scaling in Analog Computing - THE Analog Thing Wiki](https://the-analog-thing.org/wiki/index.php?title=Scaling)
[^3]: Ulmann, Bernd. *Analog Computing*. Oldenbourg Wissenschaftsverlag, 2013.
[^4]: [Dynamic Range - Wikipedia](https://en.wikipedia.org/wiki/Dynamic_range)

## Further Reading

- [Programming and Patching](04-programming-patching.md)
- [Solving ODEs](../03-mathematics/03-ode-solving.md)
- [Mass-Spring-Damper Tutorial](../07-tutorials/03-mass-spring-damper.md)
