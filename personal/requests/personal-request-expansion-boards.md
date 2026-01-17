# Personal Request: Expansion Boards Inventory

## What We Need

Current inventory of expansion boards (shields, HATs, capes, breakouts) from Personal/Expansion Boards collection.

## Use Case

`workshop-capabilities.md` currently shows placeholder counts (12 Arduino Shields, 2 Raspberry Pi HATs). Need actual inventory to:
- Document specific shields, HATs, and capes available
- Track pin mappings and compatibility with parent boards
- Identify which boards support which projects
- Cross-reference with Programmable Devices collection
- Plan integration possibilities for projects

## Information to Extract From Personal/Expansion Boards/

### By Platform

**Arduino Shields:**
- Shield name and model
- Functions/capabilities (motor control, LCD, XBee, RS232/RS485, ISP, sensors, etc.)
- Pin compatibility (which Arduino boards)
- Project use or potential
- Status (Active/Shelved/Project/Parts)

**Raspberry Pi HATs:**
- HAT name and model
- Functions/capabilities
- GPIO/Interface requirements
- Compatibility notes
- Project use or potential
- Status

**BeagleBone Capes:**
- Cape name and model
- Functions/capabilities
- Pin compatibility
- Project use or potential
- Status

**Other Expansion Modules:**
- Any other expansion boards (breakout boards, daughter cards, etc.)
- Platform compatibility
- Functions/capabilities
- Status

## Format Requested

Markdown tables organized by platform:

**Arduino Shields**
| Shield Name | Functions | Compatible With | Status | Projects |
|---|---|---|---|---|
| | | | | |

**Raspberry Pi HATs**
| HAT Name | Functions | GPIO Required | Status | Projects |
|---|---|---|---|---|
| | | | | |

**BeagleBone Capes**
| Cape Name | Functions | Compatibility | Status | Projects |
|---|---|---|---|---|
| | | | | |

**Other Expansion Modules**
| Module Name | Platform | Functions | Status | Projects |
|---|---|---|---|---|
| | | | | |

## Cross-Reference Notes

- Pin mapping details for compatibility verification
- Which Programmable Devices these boards work with
- Any compatibility issues or limitations
- Projects that currently use each board

## Response File Location

Place completed inventory at: `personal/incoming/expansion-boards.md`
