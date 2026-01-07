# ATtiny2313 LED Clock

LED clock project using ATtiny2313 microcontroller - learning ISP programming and timekeeping.

## Overview

This project builds a semi-useful LED clock using an ATtiny2313 microcontroller. The primary learning goals are:
- Building practical circuits with ATtiny microcontrollers
- Implementing ISP (In-circuit Serial Programmer) interface
- Exploring accurate timekeeping with basic hardware
- Designing LED display drivers

The clock features a new LED screen that needs to be soldered and assembled. The counter code needs tuning to improve timekeeping accuracy.

## Project Status

**Status:** In Progress

**Completed:**
- Initial clock circuit design
- ATtiny2313 firmware (needs tuning)
- ISP programming interface

**Materials Acquired:**
- New LED screen module (ready to solder)

**Next Steps:**
1. Solder LED screen module
2. Tune counter code for better timekeeping accuracy
3. Test timekeeping drift over 24-48 hours
4. Consider external crystal oscillator if accuracy insufficient
5. Design and build enclosure

## Equipment Used

- ATtiny2313 microcontroller
- LED display module (new, to be soldered)
- [ISP programmer](../../Test%20Equipment/) - For programming ATtiny2313
- Soldering equipment - [KSGER T12](../../Test%20Equipment/)

## Materials

See [tools-and-components.md](../../tools-and-components.md) for component inventory.

**Key Components:**
- ATtiny2313 microcontroller
- LED display module
- Crystal oscillator (if needed for accuracy)
- Resistors, capacitors, power supply

## Learning Goals

- Master ISP programming interface
- Understand AVR microcontroller architecture
- Learn low-power timekeeping techniques
- Practice PCB assembly and soldering

## References

- ATtiny2313 datasheet
- AVR ISP programming guides
- [project-ideas.md](../../project-ideas.md) - Original project concept

---

*Last updated: 2026-01-07*
