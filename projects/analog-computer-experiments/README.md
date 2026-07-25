# Analog Computer Experiments

Exploring analog computing with The Analog Thing (THAT) - integrators, chaos systems, and hybrid computing.

## Overview

This project explores analog computing using Anabrid's "The Analog Thing" (THAT) - a modern educational analog computer. Analog computers solve differential equations in real-time using op-amps, integrators, and function generators.

Goals include learning analog computing fundamentals, implementing classic demonstrations (Lorenz attractor, predator-prey models), and exploring hybrid analog-digital systems.

## Project Status

**Status:** In Progress - Learning Phase

**Completed:**
- Acquired Anabrid THAT analog computer
- Initial familiarization with THAT interface

**Next Steps:**
1. Complete THAT tutorials and example problems
2. Build simple integrator circuits
3. Implement Lorenz attractor (chaos visualization)
4. Model predator-prey ecosystem simulation
5. Experiment with control system modeling (PID loops)
6. Explore hybrid computing — see [that-hybrid-controller](../that-hybrid-controller/) (Arduino Mega 2560 + THAThc library, now the concrete plan for this step)

## Equipment Used

- **[Anabrid THAT (The Analog Thing)](../../.personal/incoming/test-equipment.md)** - Educational analog computer
- **[Oscilloscope](../../.personal/incoming/test-equipment.md)** - For visualizing outputs (Lorenz attractor, waveforms)
- **[STM32 boards](../../.personal/incoming/programmable-devices.md)** - For hybrid analog-digital experiments
- **[Function generator, power supplies](../../.personal/incoming/test-equipment.md)**

## Planned Experiments

### Basic Learning
1. Simple RC integrator circuits
2. Summer and inverter operations
3. Solving first-order differential equations
4. Damped harmonic oscillator

### Classic Demonstrations
1. **Lorenz Attractor** - Chaotic system visualization on oscilloscope
2. **Predator-Prey Model** - Lotka-Volterra equations (population dynamics)
3. **Control Systems** - PID loop modeling and tuning
4. **Ballistic Trajectory** - Projectile motion simulation
5. **Longitudinal Flight Simulator** - Simplified 2D (x,z-plane) aircraft flight dynamics: body-axis
   acceleration from a multiplier/sine/cosine network, pitch-rate integration, and coordinate
   transformation to Earth axes. Modeled on [Analog Museum's lfsim example](https://www.analogmuseum.org/english/examples/lfsim/)
   (built on a Telefunken RA 770, inspired by NASA's X-15 simulator work) — a good target once the
   basic integrator/multiplier/function-generator experiments above are working, since it chains
   several of them together (3 multipliers, 3 sine + 2 cosine function generators, multiple
   integrators). Cross-reference: [11-aerospace-simulation](../../AnalogComputers/analog-computing-repository/11-aerospace-simulation/) collection for the underlying aircraft-simulation theory.
6. **Bouncing Ball in a Box** - Classic demo combining bounded integration (gravity + damped
   rebound, clamped by Zener diodes at ±1 machine unit) with comparator-driven sign flips for wall
   collisions on the X axis, plus a separate high-frequency sine/cosine oscillator superimposed on
   the position signals purely to draw a round "ball" on the scope instead of a dot. Modeled on
   [Analog Museum's bouncing_ball example](https://www.analogmuseum.org/english/examples/bouncing_ball/)
   (Telefunken RA742). Good precursor to the flight simulator above — same sine/cosine function
   generator technique, simpler equations, and a nice concrete demonstration of using comparators
   to handle discontinuities (collisions) without explicit event detection.

### Hybrid Computing
1. **THAThc Arduino interface** - see [that-hybrid-controller](../that-hybrid-controller/) for the
   concrete build (Arduino Mega 2560 + THAT HYBRID port)
2. Digital control of analog parameters
3. Data logging and analysis
4. Real-time coefficient adjustment

## Documentation & Learning Resources

See [AnalogComputers/analog-computing-repository/](../../AnalogComputers/analog-computing-repository/) for extensive PDF library:
- Fundamentals and tutorials
- Application notes (ADI, TI, ALPACA)
- Vintage analog computer manuals (EAI, Heathkit, Comdyna)
- Aerospace simulation papers

## Code Repository

**Hybrid Computing Code:** [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery)

**Repository Analysis:** [.claude/analysis/EmbeddedBakery/4caaa60-2025-03-14.md](../../../.claude/analysis/EmbeddedBakery/4caaa60-2025-03-14.md)
- STM32 projects for hybrid computing
- 484 Arduino sketches (including analog interface work)

## Related Projects

- [THAT Hybrid Controller](../that-hybrid-controller/) - Arduino Mega 2560 + THAThc library for programmatic hybrid computing
- [Zynq SoC Exploration](../zynq-soc-exploration/) - Zynq ARM+FPGA for hybrid analog-digital systems
- [SCPI Instrument Control](../scpi-instrument-control/) - Automated measurement for analog computer outputs
- [Passive Radar SDR](../passive-radar-sdr/) - Analog signal processing concepts

## Learning Goals

- Understand analog computing principles (integrators, summers, function generation)
- Solve differential equations using physical circuits
- Explore chaos theory through analog implementation
- Learn hybrid analog-digital system design

## References

- Anabrid THAT documentation and tutorials
- [AnalogComputers/analog-computing-repository/](../../AnalogComputers/analog-computing-repository/) - 232 PDFs, 660MB research collection
- [project-ideas.md](../project-ideas.md) - Original project concept

### Books (owned, see Personal/Collections/Books/)
- *Applications of Operational Amplifiers: Third-Generation Techniques* - Jerald G. Graeme (Burr-Brown) - op-amp circuit design directly applicable to THAT's integrator/summer/multiplier building blocks
- *Designing with Operational Amplifiers: Applications Alternatives* - Jerald G. Graeme (Burr-Brown) - companion volume, op-amp application circuits

---

*Last updated: 2026-01-07*
