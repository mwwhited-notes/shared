# THAT Hybrid Controller (THAThc)

Arduino Mega 2560 hybrid-computing interface for Anabrid's "The Analog Thing" (THAT), using the
open-source THAThc library to drive and read the analog computer's HYBRID port.

## Overview

THAT provides five integrators, four summers, four inverters, two multipliers, two comparators,
and eight coefficient potentiometers — everything needed for classic analog computing — but on
its own it only runs in front-panel/manual mode. The HYBRID port exposes three digital control
lines (enable hybrid mode, Mode IC, Mode OP) and four analog monitor outputs (X, Y, Z, U), which
is exactly what a microcontroller needs to drive IC/OP cycling programmatically and log the
analog outputs as data instead of just watching them on a scope.

[THAThc](https://github.com/anabrid/THAThc) is Anabrid's own open-source Arduino library for this:
it wraps the HYBRID port in a singleton object with both an interactive serial shell (`enable`,
`ic`, `op`, `halt`, `run`, `rep`, `sample`, `read`, `arm`) and direct method calls for scripted,
repeatable runs — turning THAT from a manually-operated bench instrument into something that can
run automated sweeps, log ADC data, and be driven from a larger test setup.

This is the concrete implementation of the "Hybrid Computing" step already planned in
[analog-computer-experiments](../analog-computer-experiments/) — that project targeted an STM32
interface generically; THAThc is the ready-made Arduino equivalent and a faster path to the same
goal (digital control of analog parameters, data logging, real-time coefficient adjustment).

## Materials

| Material | Purpose | Source | Notes |
|----------|---------|--------|-------|
| Arduino Mega 2560 | Hybrid controller host | Already owned ([programmable devices inventory](../../.personal/incoming/programmable-devices.md)) | Chosen by THAThc for its extra digital/analog pin count |
| Anabrid THAT | Analog computer under control | Already owned ([test equipment inventory](../../.personal/incoming/test-equipment.md)) | Must be powered from its own USB-C supply, not the Arduino — draws ~300mA |
| 2x8 IDC cable | HYBRID port connection | To source | Connects HYBRID port to a breakout/piggyback board |
| Piggyback/breakout board | Signal breakout to Arduino headers | To build/source | Referenced by THAThc repo photos but not fully detailed there |
| Jumper wires | 8 signal connections (X, Y, Z, U, GND x2, enable, MOP, MIC) | On hand | See pinout below |

## HYBRID Port Pinout

Per [the-analog-thing.org's Hybrid Computer wiki page](https://the-analog-thing.org/wiki/Hybrid_Computer):

| HYBRID Pin | Signal | Arduino Mega Pin |
|------------|--------|-------------------|
| 2 | Analog X output | A0 |
| 4 | Analog Y output | A1 |
| 6 | Analog Z output | A2 |
| 8 | Analog U output | A3 |
| 9-10 | Ground | GND |
| 13 | Enable hybrid mode | D2 |
| 14 | Mode OP (MOP) | D3 |
| 16 | Mode IC (MIC) | D4 |

Logic levels are CMOS, compatible with the Mega, ESP32/8266, Teensy, and Raspberry Pi without
level shifting. The analog lines already include level shifting on THAT's side for direct
microcontroller compatibility.

**Safety note:** THAT must be powered from its own dedicated USB-C supply — never from the
Arduino's 5V rail. THAT draws roughly 300mA, enough to cause an excessive voltage drop if powered
through the microcontroller.

## Construction Method / Build Steps

1. Build or source a piggyback/breakout board to fan out the HYBRID port's 2x8 IDC connector to
   discrete jumper-friendly pins
2. Wire the 8 connections per the pinout table above (4 analog inputs, 2 ground, 3 digital control)
3. Install the THAThc Arduino library ([github.com/anabrid/THAThc](https://github.com/anabrid/THAThc))
4. Flash the Mega 2560 and bring up the interactive serial shell to verify `enable`/`ic`/`op` cycle
   control and `read`/`sample` ADC access before scripting anything
5. Move from shell commands to the direct API for automated, repeatable problem runs (`rep` for
   repetitive runs, configurable ADC sample interval down to 110µs across up to 4 channels,
   2048-entry data buffer)
6. Log captured data and compare against expected analog-computing solutions (start with the
   simple ODEs already documented in [analog-computer-experiments/notes/](../analog-computer-experiments/notes/))

## Key Features

- Turns THAT's manual IC/OP front-panel cycling into a programmable, repeatable operation
- Up to 4 simultaneous ADC channels (X, Y, Z, U) at a minimum 110µs sample interval
- 2048-entry onboard data buffer with automatic sampling-interval management
- Both an interactive shell (for manual/exploratory use) and a direct object-oriented API (for
  scripted/automated use) in the same library
- ADC calibration methods to correct conversion scaling

## Advantages Over Manual Operation

| Feature | THAThc | Manual Front-Panel Operation |
|---------|--------|-------------------------------|
| Repeatability | Scripted `rep` cycles, identical every run | Manual switch/dial operation, run-to-run variance |
| Data capture | Logged to Arduino buffer, exportable | Read off scope/panel meters by hand |
| Coefficient sweeps | Can be automated in code | Manual potentiometer adjustment per run |
| Integration | Can be driven from a larger test/automation setup | Standalone bench use only |

## Use Cases

- Automated coefficient sweeps for a given differential equation (e.g. varying damping ratio in a
  mass-spring-damper run and logging each result)
- Repeatable demonstration runs (Lorenz attractor, predator-prey) with captured data instead of
  scope photos
- A stepping stone toward the STM32/Zynq hybrid-computing goals already listed in
  [analog-computer-experiments](../analog-computer-experiments/) and
  [Zynq SoC Exploration](../zynq-soc-exploration/)

## Project Status

**Status:** Planning

**Next Steps:**
1. Source or build the HYBRID port piggyback/breakout board
2. Wire the Arduino Mega 2560 per the pinout table
3. Install THAThc library and verify shell commands (`enable`, `ic`, `op`) against a known-simple
   circuit already patched on THAT
4. Script a first automated `rep` run and confirm captured ADC data matches expected output
5. Fold results back into [analog-computer-experiments](../analog-computer-experiments/)'s planned
   experiments (Lorenz attractor, predator-prey, PID tuning) using THAThc for data capture

## References

- [THAThc GitHub repository](https://github.com/anabrid/THAThc) - Arduino library and shell/API reference
- [THE ANALOG THING Hybrid Computer wiki](https://the-analog-thing.org/wiki/Hybrid_Computer) - HYBRID port pinout and logic-level specification
- [Analog/Hybrid Computing with The Analog Thing Computer - Servo Magazine](https://www.servomagazine.com/magazine/article/analog-hybrid-computing-with-the-analog-thing-computer) - companion write-up covering the same IDC-cable + Arduino Mega breakout approach and control code
- Cross-reference: [analog-computer-experiments/](../analog-computer-experiments/) - originating project, general THAT experiments
- Cross-reference: [AnalogComputers/analog-computing-repository/10-application-notes/03-anabrid-that.md](../../AnalogComputers/analog-computing-repository/10-application-notes/03-anabrid-that.md) - Anabrid THAT application notes

---

*Last updated: 2026-07-24*
