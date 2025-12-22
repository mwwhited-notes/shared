# Glossary of Terms

## A

**Accuracy**
: The degree to which a computed result matches the true mathematical result. Analog computers typically achieve 0.01-0.1% accuracy.

**ADC (Analog-to-Digital Converter)**
: Device that converts continuous analog voltages to discrete digital values.

**Amplitude Scaling**
: Adjusting variable ranges to fit within computer voltage limits (typically ±10V).

**Analog Computer**
: A computing device that uses continuously variable physical quantities (usually voltages) to model mathematical relationships.

**Attractor**
: A set of states toward which a dynamical system evolves over time.

## B

**Bandwidth**
: The range of frequencies over which a circuit operates correctly. Limited by op-amp GBW product.

**Bias Current**
: Small current flowing into op-amp inputs due to transistor base/gate currents.

**Block Diagram**
: Graphical representation of system interconnections using functional blocks.

**Boundary Value Problem (BVP)**
: Differential equation with conditions specified at multiple points (e.g., both ends of an interval).

## C

**Chaos**
: Deterministic behavior that appears random due to extreme sensitivity to initial conditions.

**Chopper Stabilization**
: Technique to eliminate op-amp offset drift using modulation and demodulation.

**Closed-Loop Gain**
: Gain of amplifier circuit with feedback connected.

**Coefficient**
: A constant multiplier in an equation, set using potentiometers in analog computers.

**CMRR (Common Mode Rejection Ratio)**
: Ability of differential amplifier to reject signals common to both inputs.

**Comparator**
: Circuit that outputs one of two levels depending on which input is larger.

## D

**DAC (Digital-to-Analog Converter)**
: Device that converts discrete digital values to continuous analog voltages.

**Damping Ratio (ζ)**
: Parameter describing oscillation decay rate. ζ < 1 underdamped, ζ = 1 critical, ζ > 1 overdamped.

**Dead Zone**
: Region around zero where output remains zero regardless of input.

**Decoupling Capacitor**
: Capacitor near IC power pins to filter noise and prevent oscillation.

**Differential Analyzer**
: Mechanical analog computer using wheel-and-disk integrators.

**Differential Equation**
: Equation involving derivatives of unknown functions.

**Differentiator**
: Circuit whose output is proportional to the derivative of its input.

**Drift**
: Slow change in output due to temperature, aging, or component imperfections.

**Dynamic Range**
: Ratio of largest to smallest signal a system can handle (typically 60-80 dB for analog computers).

## E

**Error**
: Difference between computed and true result.

**Exponential Decay**
: Solution form y = y₀e^(-t/τ), characteristic of first-order systems.

## F

**Feedback**
: Returning part of output to input to control system behavior.

**First-Order System**
: System described by first-order differential equation (one integrator).

**Forcing Function**
: External input driving a differential equation.

**Frequency Response**
: System behavior as function of input frequency.

**Function Generator**
: Circuit that produces a nonlinear input-output relationship.

## G

**Gain**
: Ratio of output to input amplitude.

**GBW (Gain-Bandwidth Product)**
: Product of gain and bandwidth, constant for a given op-amp.

**Ground**
: Reference voltage (0V) for all measurements.

## H

**HALT Mode**
: Operating state where integrators hold their current values.

**Harmonic Oscillator**
: System described by d²x/dt² + ω²x = 0.

**Hybrid Computer**
: System combining analog and digital computing elements.

**Hysteresis**
: Different switching thresholds depending on direction of change.

## I

**IC (Initial Condition)**
: Starting value of a variable at t = 0.

**Ideal Op-Amp**
: Theoretical op-amp with infinite gain, infinite input impedance, zero output impedance.

**Impedance**
: Generalization of resistance including capacitive and inductive effects.

**Initial Value Problem (IVP)**
: Differential equation with conditions specified at starting point only.

**Integrator**
: Circuit whose output is proportional to the time integral of its input.

**Inverter**
: Circuit that outputs the negative of its input.

## J-K

**Kelvin Feedback Technique**
: Method of converting differential equations to analog computer block diagrams.

## L

**Laplace Transform**
: Mathematical technique for converting differential equations to algebraic equations.

**Limit Cycle**
: Isolated periodic orbit in phase space.

**Limiter**
: Circuit that constrains output to specified voltage range.

**Loading**
: Effect of connecting a load that draws current and affects voltage.

**Loop**
: Closed path in a block diagram or circuit.

**Lyapunov Exponent**
: Measure of rate of divergence of nearby trajectories; positive indicates chaos.

## M

**Machine Unit (MU)**
: Standard voltage unit of analog computer, typically 10V.

**Magnitude Scaling**
: See Amplitude Scaling.

**Method of Lines**
: Technique for solving PDEs by discretizing space and leaving time continuous.

**Multiplier**
: Circuit that outputs the product of two input voltages.

## N

**Natural Frequency (ωₙ)**
: Oscillation frequency of undamped second-order system.

**Negative Feedback**
: Feedback that opposes changes in output, stabilizing the system.

**Noise**
: Unwanted random variations in signals.

**Nonlinear**
: Relationship that is not proportional (e.g., includes products, powers, or other nonlinear functions).

**Normalization**
: Scaling variables to dimensionless form, typically range ±1.

## O

**Offset Voltage**
: Small voltage difference required at op-amp inputs for zero output.

**Op-Amp (Operational Amplifier)**
: High-gain differential amplifier, the fundamental building block of electronic analog computers.

**Open-Loop Gain**
: Gain of op-amp without feedback (typically 10⁵ to 10⁶).

**OPERATE Mode**
: Operating state where integrators are computing (integrating).

**ODE (Ordinary Differential Equation)**
: Differential equation with one independent variable.

## P

**Parallel Operation**
: All computations occurring simultaneously, fundamental advantage of analog.

**Patch Panel**
: Array of connectors for interconnecting computing elements.

**Patch Cord**
: Cable with plugs for connecting elements on patch panel.

**PDE (Partial Differential Equation)**
: Differential equation with multiple independent variables.

**Phase Portrait**
: Plot of system trajectory in state space (e.g., position vs. velocity).

**Phase Shift**
: Time delay expressed as angle (degrees or radians).

**Potentiometer**
: Variable resistor used to set coefficient values.

**Precision**
: Consistency of repeated measurements; different from accuracy.

## Q-R

**Rail**
: Power supply voltage limit (positive or negative rail).

**Real-Time**
: Computation at same rate as physical process being modeled.

**Reference Voltage**
: Stable voltage source used for scaling and coefficients.

**Relaxation Oscillator**
: Oscillator producing square or triangle waves through switching.

**RESET Mode**
: See IC Mode.

**Resonance**
: Maximum response when forcing frequency equals natural frequency.

## S

**Saturation**
: Output reaching rail voltage and unable to go higher/lower.

**Scale Factor**
: Ratio relating physical variable to computer voltage.

**Schmitt Trigger**
: Comparator with hysteresis.

**Second-Order System**
: System described by second-order differential equation (two integrators).

**Sensitivity**
: Change in output for given change in parameter.

**Servo**
: Feedback control system for position or velocity.

**Slew Rate**
: Maximum rate of change of op-amp output voltage.

**State Variable**
: Variable appearing as derivative in state-space formulation.

**Strange Attractor**
: Attractor with fractal structure, characteristic of chaotic systems.

**Summer**
: Circuit that outputs the (inverted) sum of multiple inputs.

## T

**Time Constant (τ)**
: Characteristic time of first-order system; time to reach 63.2% of final value.

**Time Scaling**
: Running computation faster or slower than real time.

**Transfer Function**
: Ratio of output to input in frequency domain.

**Transient**
: Response that dies out over time, as opposed to steady-state.

## U-V

**Virtual Ground**
: Point held at ground potential by op-amp feedback, though not directly connected to ground.

**Virtual Short**
: The two inputs of an ideal op-amp with negative feedback are at the same voltage.

## W-Z

**Weighted Sum**
: Sum where inputs are multiplied by different coefficients.

**Zero-Drift**
: Op-amp design achieving extremely low offset and drift through chopper stabilization.
