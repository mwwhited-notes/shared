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
6. Explore hybrid computing (THAT + STM32 interface)

## Equipment Used

- [Anabrid THAT (The Analog Thing)](../../Test%20Equipment/) - Educational analog computer
- [Oscilloscope](../../Test%20Equipment/) - For visualizing outputs (Lorenz attractor, waveforms)
- [STM32 boards](../../Programmable%20Devices/) - For hybrid analog-digital experiments
- Function generator, power supplies

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

### Hybrid Computing
1. STM32 ADC reading THAT outputs
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

---

*Last updated: 2026-01-07*
