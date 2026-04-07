# 6-DOF Simulator Patching Guide for Analog Computers (Systron Donner SD-80)

## Six Degrees of Freedom Overview

A 6-DOF (six degrees of freedom) simulator models the complete motion of a vehicle or spacecraft:

**Translational Motions (Position):**
- X: Forward/Backward (surge)
- Y: Left/Right (sway)  
- Z: Up/Down (heave)

**Rotational Motions (Attitude):**
- Roll (φ): Rotation about X-axis
- Pitch (θ): Rotation about Y-axis
- Yaw (ψ): Rotation about Z-axis

---

## Core 6-DOF Equations of Motion

### Translational Equations (Newton's Second Law)

```
m·aX = ΣFX (all forces in X-direction)
m·aY = ΣFY (all forces in Y-direction)
m·aZ = ΣFZ (all forces in Z-direction)
```

Expressed as first-order derivatives for integration:

```
dVx/dt = (FX_aero + FX_thrust + FX_gravity) / m
dVy/dt = (FY_aero + FY_thrust + FY_gravity) / m
dVz/dt = (FZ_aero + FZ_thrust + FZ_gravity) / m

dX/dt = Vx
dY/dt = Vy
dZ/dt = Vz
```

### Rotational Equations (Euler's Rotational Equations)

```
Ixx·dP/dt = Mx - Iyy·P·R + (Iyy - Izz)·Q·R
Iyy·dQ/dt = My - Izz·Q·P + (Izz - Ixx)·R·P
Izz·dR/dt = Mz - Ixx·R·Q + (Ixx - Iyy)·P·Q
```

Where:
- P, Q, R = roll rate, pitch rate, yaw rate (rad/sec)
- Mx, My, Mz = moments/torques about X, Y, Z axes
- Ixx, Iyy, Izz = moments of inertia

Simplified (assuming small angles and moment coupling negligible):

```
dP/dt = Mx / Ixx
dQ/dt = My / Iyy
dR/dt = Mz / Izz

dφ/dt = P
dθ/dt = Q
dψ/dt = R
```

### Attitude Propagation (Euler Angle Kinematics)

```
dφ/dt = P + tan(θ)·(Q·sin(φ) + R·cos(φ))
dθ/dt = Q·cos(φ) - R·sin(φ)
dψ/dt = (Q·sin(φ) + R·cos(φ)) / cos(θ)
```

**Note:** Euler angles have singularity at θ = ±90°. For high-angle maneuvers, quaternion propagation is preferred.

---

## Analog Computer Block Diagram Architecture

### Basic 6-DOF Computational Structure

```
┌─────────────────────────────────────────────────────────────┐
│           FORCES & MOMENTS SUMMER                           │
│  (Sums all aerodynamic, gravitational, and thrust effects)  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  FX_INPUT ──┐     MY_INPUT ──┐                            │
│  FY_INPUT ──├─> SUMMER ──┐   ├─> SUMMER ──┐             │
│  FZ_INPUT ──┘     BLOCK   │   ├─> MOMENT   │             │
│                           │   │  DIVIDER   │             │
│                           │   └──────┬──────┘             │
│  GRAVITY ─────────────────┤          │                   │
│  (G-VECTOR) ──────────────┤    ┌─────▼──────┐            │
│                           │    │  MZ_INPUT  │            │
│                           └─>  │   MOMENT   │            │
│                                │  DIVIDERS  │            │
│                                │ (÷Ixx, ÷Iyy│            │
│                                │  ÷Izz)     │            │
│                                └─────┬──────┘            │
├─────────────────────────────────────────────────────────────┤
│                      INTEGRATORS (CASCADE)                  │
│                                                              │
│  ACCELERATION ─┐                  ANGLE RATE ─┐           │
│  FORCE/MASS    │   1ST INT         (P,Q,R)     │   2ND     │
│  ──────────┬─> INTEGRATOR ──┬────> INTEGRATOR ┼──>ANGLE  │
│            │   (dt)         │      (dt)        │  (φ,θ,ψ) │
│            │                │                  │           │
│            └────────────────┴──────────────────┘           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Detailed Patching Configuration for SD-80

### Module Count Requirements for 6-DOF Flight Simulator

**Minimum Configuration (Basic 6-DOF):**

| Component | Count | Module Type | Notes |
|-----------|-------|-------------|-------|
| Integrators | 12-18 | Dual Integrator (Model 3320) | 6-9 modules (2 integrators each) |
| Summers | 8-12 | Dual Summer (Model 3321) | 4-6 modules for force/moment summation & cascading |
| Multipliers | 6-8 | Multiplier/Comparator (3323) | For nonlinear aerodynamic terms |
| Inverters | 4-6 | Inverter Amplifiers (Model 3322) | Sign changes as needed |
| Function Generators | 2-3 | VDFG Cards | Trigonometric, aerodynamic tables |
| Potentiometers | 30-60 | Coefficient Pots | Vehicle parameters, scale factors, aerodynamic coefficients |

**Full Configuration (6-DOF with Atmosphere & Atmosphere):**
- 18-22 integrators
- 12-16 summers
- 8-12 multipliers
- 6-8 inverters
- 3-4 function generators
- 60-100+ potentiometers

**SD-80 Capacity:** 42 computing modules + 125 potentiometers = adequate for full 6-DOF simulator

---

## Patch Panel Wiring Schematic for 6-DOF Flight Simulator

### Section 1: Force Summation (Translational Dynamics)

```
AERODYNAMIC FORCES (from function generators or lookup tables):
┌─────────────────┬─────────────────┬──────────────────┐
│   Fx_aero       │   Fy_aero       │   Fz_aero        │
│   (1 module)    │   (1 module)    │   (1 module)     │
└────────┬────────┴────────┬────────┴──────────┬───────┘
         │                 │                   │
         ▼                 ▼                   ▼
    ┌──────────────────────────────────────────────┐
    │  SUMMER 1: ΣFx = Fx_aero + Fx_thrust + Fx_g  │
    │  SUMMER 2: ΣFy = Fy_aero + Fy_thrust + Fy_g  │
    │  SUMMER 3: ΣFz = Fz_aero + Fz_thrust - m·g   │
    │  (Model 3321: Dual Summer Amplifiers)        │
    │  Input Potentiometers: Mass (m) for scaling  │
    └──────────────┬───────────────────────────────┘
                   │
                   ▼ (to Integrators)
```

### Section 2: Acceleration to Velocity Integration

```
    ΣFx ─┐
    ΣFy ──┼──> DIVIDER/SCALER ──> a_x = Fx/m
    ΣFz ─┘    (Potentiometer)     a_y = Fy/m
                                   a_z = Fz/m
                                   │
                                   ▼
         ┌────────────────────────────────────────┐
         │  INTEGRATOR 1: dVx/dt = ax             │
         │  INTEGRATOR 2: dVy/dt = ay             │
         │  INTEGRATOR 3: dVz/dt = az             │
         │  (Model 3320: Dual Integrator Modules) │
         │  (3 modules required)                  │
         └────────────────┬───────────────────────┘
                          │
                          ▼
         ┌────────────────────────────────────────┐
         │  OUTPUT: Velocities Vx, Vy, Vz        │
         │  Available for feedback/display        │
         └────────────────┬───────────────────────┘
                          │
                          ▼
         ┌────────────────────────────────────────┐
         │  INTEGRATOR 4: dX/dt = Vx              │
         │  INTEGRATOR 5: dY/dt = Vy              │
         │  INTEGRATOR 6: dZ/dt = Vz              │
         │  (Model 3320: Dual Integrator)         │
         │  (3 modules required)                  │
         └────────────────┬───────────────────────┘
                          │
                          ▼
         ┌────────────────────────────────────────┐
         │  OUTPUT: Positions X, Y, Z             │
         │  (Used for display/navigation)         │
         └────────────────────────────────────────┘
```

### Section 3: Moment Summation (Rotational Dynamics)

```
AERODYNAMIC MOMENTS (Rolling, Pitching, Yawing):
┌─────────────────┬─────────────────┬──────────────────┐
│   Mx_aero       │   My_aero       │   Mz_aero        │
│   (roll moment) │   (pitch moment)│   (yaw moment)   │
│   (1 module)    │   (1 module)    │   (1 module)     │
└────────┬────────┴────────┬────────┴──────────┬───────┘
         │                 │                   │
         ▼                 ▼                   ▼
    ┌──────────────────────────────────────────────┐
    │ SUMMER 4: ΣMx = Mx_aero + Mx_control        │
    │ SUMMER 5: ΣMy = My_aero + My_control        │
    │ SUMMER 6: ΣMz = Mz_aero + Mz_control        │
    │ (Model 3321: Dual Summer Amplifiers)        │
    │ Additional terms: Moment coupling products  │
    └──────────────┬───────────────────────────────┘
                   │
                   ▼ (Moment coupling terms)
    ┌──────────────────────────────────────────────┐
    │ MOMENT COUPLING MULTIPLIERS:                 │
    │ Mx_coupling = (Iyy - Izz) × Q × R           │
    │ My_coupling = (Izz - Ixx) × R × P           │
    │ Mz_coupling = (Ixx - Iyy) × P × Q           │
    │ (Model 3323: Multiplier modules)            │
    │ (Requires 2-3 modules for coupling)         │
    └──────────────┬───────────────────────────────┘
                   │
                   ▼ (back to summers)
```

### Section 4: Angular Acceleration to Rate Integration

```
    ΣMx ─┐
    ΣMy ──┼──> DIVIDER ──> α_p = Mx/Ixx
    ΣMz ─┘    (Potentiometers) α_q = My/Iyy
              Ixx, Iyy, Izz     α_r = Mz/Izz
                                   │
                                   ▼
         ┌────────────────────────────────────────┐
         │  INTEGRATOR 7: dP/dt = α_p (roll rate)│
         │  INTEGRATOR 8: dQ/dt = α_q (pitch)    │
         │  INTEGRATOR 9: dR/dt = α_r (yaw rate)│
         │  (Model 3320: Dual Integrator)        │
         │  (3 modules + 1 for odd one)          │
         │  OUTPUT: P, Q, R (angular rates)      │
         └────────────────┬───────────────────────┘
                          │
                          ▼
         ┌────────────────────────────────────────┐
         │ ATTITUDE PROPAGATION (via Function Gen)│
         │  Using Euler Angle Kinematics:        │
         │  dφ/dt = P + TAN(θ)×(Q·SIN(φ)+R·COS)│
         │  dθ/dt = Q·COS(φ) - R·SIN(φ)          │
         │  dψ/dt = (Q·SIN(φ)+R·COS(φ))/COS(θ)  │
         │                                        │
         │  Implemented via:                     │
         │  - Function generators (trig funcs)   │
         │  - Multipliers (products)             │
         │  - Summers (combinations)             │
         └────────────────┬───────────────────────┘
                          │
                          ▼
         ┌────────────────────────────────────────┐
         │  INTEGRATOR 10: dφ/dt (from above)     │
         │  INTEGRATOR 11: dθ/dt (from above)     │
         │  INTEGRATOR 12: dψ/dt (from above)     │
         │  (Model 3320: Dual Integrator)         │
         │  (3 modules)                           │
         │  OUTPUT: φ, θ, ψ (Euler Angles)       │
         └────────────────┬───────────────────────┘
                          │
                          ▼
         ┌────────────────────────────────────────┐
         │  OUTPUTS: Roll, Pitch, Yaw             │
         │  (Used for attitude display)           │
         └────────────────────────────────────────┘
```

---

## Detailed Patch Connections (6-DOF Configuration)

### Input Stage (Aerodynamic Forces & Control)

**Patch Cord Routing:**

```
Angle of Attack (α) ────────┐
Sideslip Angle (β) ─────────┼──> FUNCTION GENERATOR 1
Mach Number (M) ────────────┤    (Aerodynamic Lookup)
                            │
Dynamic Pressure (q) ───────┤
Reference Area (S) ─────────┤
Aerodynamic Coeff Table ────┘

OUTPUT: Fx_aero, Fy_aero, Fz_aero
        Mx_aero, My_aero, Mz_aero
        (patch to summers via multipliers)
        
Control Inputs:
Elevator Deflection (δe) ──────┬──> POTENTIOMETER (scaled)
Aileron Deflection (δa) ────────┼──> POTENTIOMETER
Rudder Deflection (δr) ─────────┤
Thrust Command (Thr) ──────────┘

OUTPUT: Fx_control, Fy_control, Fz_control
        Mx_control, My_control, Mz_control
        (patch to summers)
```

### Core Computation (Cascading Integrators)

**Integrator Module Arrangement (9 modules minimum for cascaded integration):**

```
Module 1 (Dual INT):    Fx/m → Vx    |    Fy/m → Vy
Module 2 (Dual INT):    Fz/m → Vz    |    Mx/Ixx → P
Module 3 (Dual INT):    My/Iyy → Q   |    Mz/Izz → R
Module 4 (Dual INT):    Vx → X       |    Vy → Y
Module 5 (Dual INT):    Vz → Z       |    dφ/dt → φ
Module 6 (Dual INT):    dθ/dt → θ    |    dψ/dt → ψ

Total: 12 integrators across 6 modules (2 per module)
```

### Potentiometer Settings (Coefficient Pots)

**Required Vehicle/Simulation Parameters:**

```
1. MASS SCALING:
   k_mass_x = 1/m  (scale factor for Fx/m)
   k_mass_y = 1/m  (scale factor for Fy/m)
   k_mass_z = 1/m  (scale factor for Fz/m)
   Range: 0-100% of 10-turn pot, set to match vehicle

2. MOMENT OF INERTIA SCALING:
   k_ixx = 1/Ixx   (scale factor for Mx/Ixx)
   k_iyy = 1/Iyy   (scale factor for My/Iyy)
   k_izz = 1/Izz   (scale factor for Mz/Izz)
   Range: 0-100% of 10-turn pot

3. TIME SCALING (if real-time ≠ sim time):
   k_time = t_real / t_sim
   Range: 0.1 to 10× (nominal = 1.0)

4. COORDINATE TRANSFORMATION:
   k_grav_x = gravity component in body X (0 to -9.81 m/s²)
   k_grav_y = gravity component in body Y (0 to -9.81 m/s²)
   k_grav_z = gravity component in body Z (0 to -9.81 m/s²)
   Range: 0-100% scaled to ±10V range

5. AERODYNAMIC COEFFICIENTS (lookup tables):
   CL (lift coefficient)
   CD (drag coefficient)
   Cm (pitch moment coefficient)
   Cn (yaw moment coefficient)
   Cl (roll moment coefficient)
   (Set via function generator cards if using tables)

6. CONTROL SURFACE EFFECTIVENESS:
   k_elev (elevator effectiveness, rad/volt)
   k_aileron (aileron effectiveness, rad/volt)
   k_rudder (rudder effectiveness, rad/volt)
   k_thrust (thrust scaling, N/volt)
   Range: 0-100% of 10-turn pot

7. VISCOUS DAMPING:
   k_damp_p = damping/Ixx for roll
   k_damp_q = damping/Iyy for pitch
   k_damp_r = damping/Izz for yaw
   (optional, set to zero for rigid body model)
```

---

## Function Generator Configuration (Aerodynamic Tables)

### Variable Diode Function Generator (VDFG) Setup

**For lookup table of CL vs α (angle of attack):**

```
Input Voltage: -10V to +10V representing -90° to +90° angle of attack
Output Voltage: -10V to +10V representing CL = -1 to +1

Breakpoint Setup (12 segments, 6 adjustable positive, 6 negative):
┌─────────────────────────────────────────────────────────────┐
│ Segment │  α Range   │   CL Target  │  Output Voltage     │
├─────────────────────────────────────────────────────────────┤
│ 1       │  -90° to  │ -0.5 to 0.0  │  -5V to 0V         │
│ 2       │  -45°     │ 0.0 to -0.3  │  0V to -3V         │
│ 3       │  -20° to  │ -0.3 to 0.3  │  -3V to 3V         │
│ 4       │   0°      │  0.3 to 0.8  │  3V to 8V          │
│ 5       │   10°     │  0.8 to 1.2  │  8V to 10V         │
│ 6       │   20° to  │  1.2 to 0.8  │  10V to 8V         │
│         │   45°     │ (stall region)│                     │
│ 7-12    │ Negative  │ (mirror of    │ (mirror of         │
│         │   side    │  positive)    │  positive)         │
└─────────────────────────────────────────────────────────────┘

Setup Process:
1. Set VDFG card in function generator receptacle
2. Adjust breakpoint potentiometers for segment endpoints
3. Adjust slope potentiometers for line segment slopes
4. Test with input sweeps: apply ±10V ramp, observe linearity
5. Patch output to SUMMER inputs via multiplier (scale by dynamic pressure)
```

### Multiple Function Generators (Complete Aerodynamic Model)

```
FUNCTION GENERATOR CARD 1: CL vs α
Input: α (angle of attack)
Output: CL (lift coefficient) × qbar × S

FUNCTION GENERATOR CARD 2: CD vs α  
Input: α (angle of attack)
Output: CD (drag coefficient) × qbar × S

FUNCTION GENERATOR CARD 3: Cm vs α
Input: α (angle of attack)
Output: Cm (pitch moment coefficient) × qbar × S × cbar

FUNCTION GENERATOR CARD 4: Control Surface Effects
Input: δe (elevator), δa (aileron), δr (rudder)
Output: ΔCL, ΔCm, ΔCn as functions of control deflections
```

---

## Patch Cord Color-Coding Convention (Recommended)

| Signal Type | Color | Example |
|------------|-------|---------|
| **Forces (F)** | RED | Fx, Fy, Fz |
| **Moments (M)** | BLUE | Mx, My, Mz |
| **Velocities (V)** | GREEN | Vx, Vy, Vz |
| **Positions (X)** | YELLOW | X, Y, Z |
| **Angles (rad)** | ORANGE | φ, θ, ψ |
| **Angular Rates** | PURPLE | P, Q, R |
| **Control Input** | WHITE | δe, δa, δr |
| **Aerodynamic** | BROWN | CL, CD, Cm |
| **Potentiometer** | BLACK | Coefficient pots |
| **Ground/Reference** | GRAY | Reference voltage |

---

## Example Patch Diagram: Pitch Axis Only (Simplified 1-DOF)

```
SIMPLIFIED PITCH AXIS SIMULATION:

Input:
┌──────────────────┐
│ Elevator (δe)    │────> POTENTIOMETER (k_elev)
│ vs table lookup  │      │
└──────────────────┘      ▼
                    ┌─────────────────────────┐
                    │ SUMMER: My = My_aero +  │
                    │         My_control     │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ POTENTIOMETER: My/Iyy   │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ INTEGRATOR 1: dQ/dt     │
                    │ INPUT: My/Iyy           │
                    │ OUTPUT: Q (pitch rate)  │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ INTEGRATOR 2: dθ/dt     │
                    │ INPUT: Q                │
                    │ OUTPUT: θ (pitch angle) │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ DISPLAY: Pitch Angle    │
                    │ and Pitch Rate          │
                    └─────────────────────────┘
```

---

## Time Constant & Real-Time Considerations

### Time-Scale Factor

**Problem:** Analog computer solutions are fast (real-time integration)

**Solution:** Scale differential equations by time constant τ

```
Replace: dx/dt = f(x)
With:    d(x)/d(τ) = (dt/dτ) × f(x)

where τ = time_scaling × t_real

Example for 10× slower than real-time:
- Integrator input: F/m multiplied by 0.1
- Integrator output appears 10× slower
- Observe 1° per second pitch as 0.1° per second on meter
```

### Practical Configuration:

```
TIME SCALING POTENTIOMETER (all integrators):
Set k_time = (100 sec / real_sim_time_sec) × (time_scale_factor)

Example: To run 10× slower than real-time with 100V reference:
k_time = 0.1 (patch as 0.1 × reference voltage to all integrator inputs)

Adjustment procedure:
1. Set elevator to hold pitch at 5°
2. Adjust k_time until pitch rate appears reasonable
3. Cross-check against expected aircraft dynamics
```

---

## Problem Board Layout (Physical Organization)

### Recommended Module Arrangement on SD-80

**Front Row (Left to Right):**
```
┌──────┬──────┬──────┬──────┬──────┬──────┐
│SUMMER│SUMMER│SUMMER│SUMMER│INT   │INT   │
│ 1-2  │ 3-4  │ 5-6  │ 7-8  │ 1-2  │ 3-4  │
│ (Fx) │ (My) │ (Mz) │(Fz)  │ Vx   │ Vy   │
└──────┴──────┴──────┴──────┴──────┴──────┘
```

**Center Row:**
```
┌──────┬──────┬──────┬──────┬──────┬──────┐
│INT   │INT   │INT   │INT   │MULT  │MULT  │
│ 5-6  │ 7-8  │ 9-10 │11-12 │ 1-2  │ 3-4  │
│ Vz   │  X   │  Q   │  θ   │ Coupling│ α-trig│
│      │      │      │      │ terms │ functions│
└──────┴──────┴──────┴──────┴──────┴──────┘
```

**Right Side (Potentiometers above):**
```
POT PANELS:
┌─────────────────────────────────────┐
│ Mass scaling (3 pots)              │
│ Inertia scaling (3 pots)           │
│ Time scaling (1 pot)               │
│ Control gains (3 pots)             │
│ Gravity vector (3 pots)            │
│ Aero coefficients (12+ pots)       │
│ TOTAL: 25-30 potentiometers        │
└─────────────────────────────────────┘
```

---

## Operational Procedure for 6-DOF Flight Simulator

### Setup Phase (1-2 hours typical)

1. **Mount modules in receptacles**
   - Place integrators in predictable locations
   - Group summers and multipliers near inputs
   - Arrange for minimum patch cord runs

2. **Install potentiometers and set initial values**
   - Mass: typically 0.5-10× (for variable aircraft)
   - Inertias: 1-10 Ixx/Iyy/Izz ratios
   - Time scaling: 1.0 for real-time, 0.1-10 for variable speed

3. **Route major patch cords**
   - Force pathway: Input → Summer → Integrator → (Velocity out)
   - Moment pathway: Input → Summer → Integrator → (Rate out)
   - Feedback loops: Rate → Attitude propagation → next integration stage

4. **Install function generator cards**
   - Verify card orientation and seating
   - Check breakpoint and slope pot ranges
   - Test with oscilloscope before final patching

5. **Power-up and Balance Phase (20-30 min)**
   - Set all modes to BALANCE
   - Adjust amplifier null potentiometers
   - Verify zero-signal outputs are ±0 volts
   - Check overload indicators (none should light)

### Trim & Calibration Phase (1-2 hours)

6. **Set initial conditions**
   - Level flight: φ = 0°, θ = 0°, P = Q = R = 0
   - Cruise altitude and velocity
   - Initial control surface positions (δe = 0, etc.)

7. **Compute trim condition**
   - Hold elevator neutral (δe = 0)
   - Adjust throttle for level flight
   - Verify: dθ/dt = 0 (no pitch acceleration)
   - Adjust differential aileron for balanced roll: dφ/dt = 0

8. **Verify aircraft response characteristics**
   - Small pitch input: expect rising pitch, then damping
   - Check phugoid oscillation period (15-25 sec typical)
   - Verify short-period pitch oscillation (2-3 sec typical)

### Testing Phase

9. **Run step responses**
   - Elevator input: 1° step, observe pitch rate & acceleration
   - Cross-check against aircraft performance data
   - Adjust aerodynamic coefficients if needed

10. **Record trim settings and potentiometer values**
    - Document all 30+ pot positions
    - Note time-scale factor used
    - Photograph problem board patch configuration

---

## Troubleshooting Common 6-DOF Simulation Problems

| Symptom | Likely Cause | Solution |
|---------|--------------|----------|
| Pitch diverges immediately | Negative feedback inverted | Check My/Iyy sign, flip integrator input |
| Pitch oscillation grows without bound (instability) | Time scaling too fast or pitch damping missing | Reduce k_time or add damping term to summer |
| Pitch rate never settles (runaway integral) | Bias current drift in integrator | Shorten integrator RC time constant or add reset |
| Elevator input has no effect | Control potentiometer set to zero | Verify k_elev is non-zero and patched |
| Asymmetric response to roll left vs right | Moment coupling term has wrong sign | Check (Ixx - Iyy) term in roll equation |
| Solution goes to limit (±10V) immediately | Initialization condition drives system to limit | Check initial condition settings (should be zero) |
| Attitude angles grow indefinitely | Angular rate integration not reset | Verify integrator reset switch in BALANCE mode |
| Jerky, non-smooth motion | Overload light flickering | Reduce input amplitude or adjust time scaling |

---

## Advanced Features: Enhanced 6-DOF Configurations

### Wind/Atmosphere Model

```
Add 3 function generators:
- Wind_x(altitude) 
- Wind_y(altitude)
- Wind_z(altitude) [updrafts]

Patch to velocity summer:
V_inertial_x = V_body_x + Wind_x(Z)
V_inertial_y = V_body_y + Wind_y(Z)
V_inertial_z = V_body_z + Wind_z(Z)
```

### Ground Effect Modeling

```
Add height-dependent aerodynamic coefficient variation:
CL_ground_effect = CL + f(h/wing_span) × ΔCL
where f(h) = function from ground effect VDFG card
Typical range: correction = 0 (no effect) at h > 100 ft
             = -0.2 to +0.3 near ground
```

### Damage/Degradation Simulation

```
Add damage factor (0-1) to aerodynamic coefficients:
CL_damaged = CL × (1 - damage_factor)
CD_damaged = CD × (1 + 2×damage_factor)

Patch damage_factor potentiometer to multiplier inputs
for all three lift/drag/moment coefficients
```

### Thrust Vector Control (TVC)

```
Add 2 additional control inputs:
- Thrust_pitch_angle (δt_pitch)
- Thrust_yaw_angle (δt_yaw)

Patch to moment summers:
My += Thrust_mag × sin(δt_pitch) × x_cg_offset
Mz += Thrust_mag × sin(δt_yaw) × x_cg_offset
```

---

## Documentation Checklist for 6-DOF Simulator

Before running extended testing sessions, record:

- [ ] **Patch diagram:** Photograph all connections, label major pathways
- [ ] **Potentiometer log:** Document all 30-50+ pot settings (photograph with values)
- [ ] **Time scaling:** Note k_time value and corresponding real/sim time ratio
- [ ] **Module inventory:** List all 18-22 modules installed, locations
- [ ] **Function generator:** Note each VDFG card breakpoints and slopes
- [ ] **Trim data:** Record trim conditions (altitude, V, θ, P, Q, R)
- [ ] **Performance data:** Cross-check against manufacturer's flight test data
- [ ] **Calibration notes:** Any offset adjustments or balance trimming performed
- [ ] **Problem board state:** Save photographs from multiple angles
- [ ] **Operating limits:** Maximum/minimum safe input voltages, scaling factors

---

## References & Further Reading

**Analog Computing References:**
- Korn, G.A., "Continuous-System Simulation and Analog Computers," IEEE Control Systems Magazine, June 2005
- Systron-Donner SD 40-80 Maintenance Manual (bitsavers archive)
- Systron-Donner Handbook of Analog Computation (Jun67)

**6-DOF Flight Dynamics:**
- Stevens, Lewis, and Johnson, "Aircraft Control and Simulation: Dynamics, Controls Design, and Autonomous Systems," 3rd Edition, Wiley, 2013
- Beard, R.W. and McLain, T.W., "Small Unmanned Aircraft: Theory and Practice," Princeton University Press, 2012
- Etkin, B., "Dynamics of Atmospheric Flight," Dover Publications, 2005

**NASA Simulator References:**
- NASA SP-2000-4224: "Computers Take Flight: A History of NASA's Pioneering Digital Fly-By-Wire Project"
- VisSim Tutorial Series: "Introduction to 6-DOF Simulation of Air Vehicles"

