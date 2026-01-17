# Raspberry Pi 40-pin GPIO 1 to 2 Expansion Board

**Compatibility:** Raspberry Pi 2, Pi 3, Pi 4, Pi Zero (with adapter)
**Model:** RAS-GP02 (or similar GPIO doubler)
**Function:** GPIO Pin Multiplier / Extension Board
**Purchased:** 2020-04-28
**Source:** Amazon
**Price:** $8.99

---

## Overview

This GPIO expansion board allows you to connect two GPIO-dependent devices or shields simultaneously to a single Raspberry Pi 40-pin GPIO header. It uses ribbon cable connections to split the GPIO pins, enabling parallel access for multiple expansion boards.

---

## Specifications

| Parameter | Value |
|-----------|-------|
| **Connector Type** | 40-pin GPIO header (standard Raspberry Pi) |
| **Output Connectors** | 2x 40-pin GPIO headers (via ribbon cables) |
| **Function** | GPIO pin multiplier / doubler |
| **Ribbon Cable Length** | Typically 20-30cm |
| **Compatible Models** | Pi 2, Pi 3, Pi 3B+, Pi 4, Pi Zero (with adapter) |
| **Power Distribution** | 5V and 3.3V available at both outputs |

---

## Pin Mapping

### Input (Pi GPIO)
- Standard 40-pin GPIO header for Raspberry Pi

### Outputs (via ribbons)
- **Board A:** 40-pin GPIO header
- **Board B:** 40-pin GPIO header

Both output headers provide identical pin access, allowing simultaneous connection of two separate GPIO-dependent devices or shields.

---

## Primary Applications

- **Multiple Shield Support:** Running two GPIO shields simultaneously
- **HAT Expansion:** Connecting multiple HATs without a stackable hub
- **Sensor Arrays:** Connecting multiple GPIO-based sensors in parallel
- **Development Flexibility:** Swapping between different expansion configurations

---

## Compatible Expansion Boards

Works with any Raspberry Pi HAT or GPIO-dependent shield, including:
- [ARPI600](../rpi-arpi600/) - Arduino shield adapter
- [PoE HAT (2018)](../rpi-poe-hat-2018/) - Power over Ethernet (if cable allows)
- Custom GPIO-based sensors and devices

---

## Limitations

- **Not stackable:** Cannot be directly stacked on other HATs
- **Cable routing:** Requires proper cable management for clarity
- **No address conflicts:** User must ensure GPIO address conflicts don't occur when using two devices simultaneously
- **Power distribution:** Total power consumption must stay within Raspberry Pi limits

---

## Related Equipment

- **Raspberry Pi boards:** Pi 2, Pi 3, Pi 4 (in Programmable Devices/)
- **Expansion boards:** [ARPI600](../rpi-arpi600/), [PoE HAT](../rpi-poe-hat-2018/)

---

## Compatibility Notes

- Works with all 40-pin Raspberry Pi models
- Pi Zero requires GPIO header soldering or adapter
- Compatible with both official and third-party HATs

---

## Notes

- Purchased as standalone expansion solution for multiple GPIO devices
- Provides flexibility for projects requiring multiple concurrent expansions
- Simple passive design with no active components

---

*Last updated: 2026-01-17*
