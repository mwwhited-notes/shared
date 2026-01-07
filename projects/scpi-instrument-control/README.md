# SCPI Instrument Control System

Network control system for SCPI-compatible test equipment with custom .NET Core VISA driver.

## Overview

This project develops a comprehensive control system for bench test equipment using SCPI (Standard Commands for Programmable Instruments). Goals include:
- Implementing SCPI communication with multiple instruments
- Writing a custom VISA driver for .NET Core
- Building an RS-232/Ethernet gateway or USB-to-network bridge
- Creating automated test and measurement workflows

The system will control existing bench equipment: HP 34401A DMM, Rigol DM3058E DMM, Rigol DG1022 function generator, and Korad power supplies.

## Project Status

**Status:** In Progress - Planning/Research Phase

**Next Steps:**
1. Research SCPI command set for each instrument
2. Test SCPI communication via direct serial/USB connection
3. Design .NET Core VISA driver architecture
4. Implement basic SCPI commands (IDN, measure, output control)
5. Build RS-232/Ethernet gateway (Raspberry Pi or BeagleBone Black)
6. Develop instrument abstraction layer
7. Create sample automation scripts

## Equipment Used

### Test Instruments
- [HP 34401A DMM](../../Test%20Equipment/) - 6.5-digit multimeter, GPIB/RS-232
- [Rigol DM3058E](../../Test%20Equipment/rigol-dm3058e/) - 5.5-digit DMM, USB/LAN/RS-232
- [Rigol DG1022](../../Test%20Equipment/rigol-dg1022/) - Function generator, USB/LAN
- Korad power supplies - Programmable bench supplies

### Gateway/Interface Options
- [Raspberry Pi](../../Programmable%20Devices/) - USB-to-network bridge
- [BeagleBone Black](../../Programmable%20Devices/beaglebone-black-rev-c/) - Alternative gateway platform
- RS-232/Ethernet adapter modules

## Architecture

```
[Test Instruments] <--SCPI/RS-232/USB--> [Gateway Device] <--Ethernet--> [.NET Core VISA Driver] <---> [Automation Scripts]
```

## Related Projects

- [DeviceBridge](https://github.com/mwwhited/DeviceBridge) - IEEE-1284 parallel port capture (related protocol work)
- [LXI Bridge for Test Equipment](../../project-ideas.md) - Potential future expansion with web interface

## Learning Goals

- Master SCPI protocol and instrument communication
- Build production-quality VISA driver for .NET Core
- Learn instrument automation patterns
- Practice network protocol design (RS-232/Ethernet gateway)

## References

- SCPI specification (IEEE 488.2)
- HP 34401A programming manual
- Rigol programming guides
- [project-ideas.md](../project-ideas.md) - Original project concept

---

*Last updated: 2026-01-07*
