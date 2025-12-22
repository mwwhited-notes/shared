# Control Systems

## Overview

Control systems are one of the most important application areas for analog computers. The real-time nature of analog computation makes it ideal for implementing and simulating feedback control systems[^1].

## PID Control

### Basic PID Controller

The Proportional-Integral-Derivative controller is the most common control algorithm:

```
u(t) = Kp·e(t) + Ki·∫e(t)dt + Kd·de(t)/dt
```

Where:
- e(t) = setpoint - measured value (error)
- u(t) = control output
- Kp, Ki, Kd = tuning parameters

### Analog PID Implementation

```
                    ┌────[Kp]────────────────┐
                    │                        │
error ──────────────┼────[INT]───[Ki]────────┼───[SUM]─── control output
                    │                        │
                    └────[DIFF]──[Kd]────────┘
```

**Detailed Circuit:**
```
                       R_p
              ┌────────/\/\/─────────────┐
              │                          │
              │         C_i              │
              │    ┌────||────┐          │
              │    │          │          │
              ├────┤   R_i    ├──────────┤
              │    │──/\/\/───│          │
              │    │          │          │
error ────────┤    └──────────┘          ├──(-)──┐
              │                          │       │
              │    R_d     C_d           │  OP   ├── output
              └────/\/\/───||────────────┘       │
                                         │       │
                                  ┌─────(+)──────┘
                                  │
                                  ▼
                                 GND
```

### PID Tuning via Analog

Advantages of analog PID for tuning:
- Adjust Kp, Ki, Kd with potentiometers
- See response instantly
- Find optimal values interactively

## Feedback Control Simulation

### Block Diagram Components

| Block | Function | Implementation |
|-------|----------|----------------|
| G(s) | Plant transfer function | RC networks, op-amps |
| H(s) | Feedback transfer function | Similar |
| Σ | Summing junction | Summer |
| × | Gain | Potentiometer/amplifier |

### Closed-Loop System

```
         ┌───────────────────────────────────────┐
         │                                       │
r(t) ────┼──[Σ]────[Controller]────[Plant]────┬──┴── y(t)
         │   ↑                                │
         │   │       ┌────────────────────────┘
         │   │       │
         │   └───[−]─┴──[Sensor/H(s)]
         │
         └───────────────────────────────────────
```

### Transfer Functions

Common transfer functions implemented with op-amps:

**First-Order System (Low-pass):**
```
G(s) = K/(τs + 1)

Implementation: Integrator with feedback resistor
```

**Second-Order System:**
```
G(s) = ωₙ²/(s² + 2ζωₙs + ωₙ²)

Implementation: Two integrators with feedback
```

**Time Delay:**
```
G(s) = e^(-sT)

Implementation: All-pass filters in cascade, or digital delay
```

## Servo Systems

### Position Servo

Controls position using position feedback:

```
Command ──[Σ]────[Amp]────[Motor]────[Position]──┬── Output
position   ↑                                      │
           │                                      │
           └───────[−]────[Position sensor]───────┘
```

**Analog Simulation:**
```
Motor: Torque = K_t · i
       J·dω/dt + b·ω = Torque
       dθ/dt = ω

Three integrators simulate motor dynamics
```

### Velocity Servo

```
Command ──[Σ]────[Amp]────[Motor]────┬── Velocity
velocity   ↑                         │
           │                         │
           └───────[−]───[Tachometer]┘
```

## Process Control

### Temperature Control

```
Setpoint ──[Σ]────[PID]────[Heater]────[Thermal]────┬── Temperature
             ↑              (power)      (mass)     │
             │                                      │
             └──────[−]─────[Temperature sensor]────┘

Thermal system: C·dT/dt = P - k(T - T_ambient)
```

### Level Control

```
Level      ┌──[Valve]──┐
setpoint ──[Σ]──[PID]──┴──[Tank]────┬── Level
            ↑                       │
            │                       │
            └───[−]──[Level sensor]─┘

Tank: A·dh/dt = Q_in - Q_out
```

### Flow Control

Fast dynamics, may need derivative action or cascade control.

## Stability Analysis

### Root Locus

Analog computers can trace root locus by:
1. Slowly varying loop gain K
2. Observing system response
3. Noting oscillation frequency at stability boundary

### Bode Analysis

Using sinusoidal input:
1. Apply sine wave at various frequencies
2. Measure amplitude ratio and phase shift
3. Plot Bode diagram point by point

### Nyquist Plot

X-Y display showing:
- X = Real part of G(jω)·H(jω)
- Y = Imaginary part
- As ω varies from 0 to ∞

## Advanced Control

### State-Space Control

For system: ẋ = Ax + Bu, y = Cx

**State Feedback:**
```
u = -Kx + r

Implementation: Matrix K as coefficient network
```

### Optimal Control (LQR)

Minimize: J = ∫(xᵀQx + uᵀRu)dt

The optimal gain K can be implemented with potentiometer network once computed.

### Adaptive Control

Parameter adjustment based on performance:
```
                   ┌──────────────────────────┐
                   │                          │
r ──[Σ]────[Controller]────[Plant]────┬──── y
     ↑         ↑                      │
     │         │                      │
     │    [Adaptation]◄───────────────┤
     │         │                      │
     └───[−]───┘                      │
                                      │
               └──────────────────────┘
```

## Flight Control Example

### Pitch Attitude Control

```
Aircraft pitch dynamics (simplified):
θ̈ = (M_α·α + M_δ·δ + M_q·q) / I_y

Where:
θ = pitch angle
α = angle of attack
δ = elevator deflection
q = pitch rate
```

**Analog Implementation:**
- Multiple integrators for dynamics
- Feedback paths for stability augmentation
- Input from pilot commands

### Autopilot Modes

| Mode | Control Variable | Feedback |
|------|-----------------|----------|
| Attitude hold | Pitch angle θ | Gyro |
| Altitude hold | Altitude h | Altimeter |
| Speed hold | Airspeed V | Pitot tube |
| Heading hold | Heading ψ | Compass |

## Industrial Applications

### Chemical Process Control

```
Multi-loop control:
- Temperature control (slow)
- Pressure control (medium)
- Flow control (fast)

Cascade and feedforward strategies
```

### Power Systems

```
Generator governor:
P_ref ──[Σ]──[Governor]──[Turbine]──[Generator]──┬── P_out
         ↑                                        │
         │                                        │
         └─────────[−]────[Power meter]───────────┘

Frequency regulation: f = f_nom + K(P_ref - P_out)
```

## Real-Time Simulation

### Hardware-in-the-Loop (HIL)

```
┌─────────────────┐     ┌─────────────────┐
│  Real           │     │  Simulated      │
│  Controller     │◄───►│  Plant          │
│  (hardware)     │     │  (analog comp.) │
└─────────────────┘     └─────────────────┘
```

**Advantages:**
- Test real controller
- Safe environment
- Repeatable conditions

### Operator Training Simulators

Analog computers historically used for:
- Flight simulators
- Power plant simulators
- Ship handling trainers

## Design Example: Motor Speed Control

**Specifications:**
- DC motor, J = 0.01 kg·m², b = 0.1 N·m·s
- Speed range: 0-3000 RPM
- Settling time < 0.5s
- Overshoot < 10%

**Motor Model:**
```
J·dω/dt + b·ω = K_t·i
```

**PI Controller Design:**
```
u = Kp(ω_ref - ω) + Ki∫(ω_ref - ω)dt

Choose: Kp = 1, Ki = 10 (tune interactively)
```

**Analog Circuit:**
- One integrator for motor dynamics
- One integrator for PI integral term
- Two potentiometers for Kp, Ki

## References

[^1]: [Control Systems Engineering - Engineering LibreTexts](https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Operational_Amplifiers_and_Linear_Integrated_Circuits_-_Theory_and_Application_(Fiore)/10:_Integrators_and_Differentiators/10.04:_Section_4-)

## Further Reading

- [ODE Solving](../03-mathematics/03-ode-solving.md)
- [Mass-Spring-Damper Tutorial](../07-tutorials/03-mass-spring-damper.md)
- [Signal Processing](04-signal-processing.md)
