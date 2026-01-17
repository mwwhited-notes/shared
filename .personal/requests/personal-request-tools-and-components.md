# Personal Request: Tools and Components Inventory

## What We Need

Current inventory of hand tools, consumables, and components stock from Personal/tools-and-components.md.

## Use Case

`workshop-capabilities.md` documents available tools and component stock. This information is essential for:
- Component stock summary in Equipment Summary section
- Project planning - verify what components are available before specifying parts
- Workshop capabilities - what's available for immediate use vs. what needs ordering
- Troubleshooting guides - identify what tools are available for repairs
- Building confidence in what projects are feasible

## Information to Extract From Personal/tools-and-components.md

### Tool Categories

1. **Hand Tools** - Precision tools, wrenches, pliers, screwdrivers, etc.
   - Tool name
   - Specifications/size
   - Quantity
   - Condition/status

2. **Soldering & Rework Equipment** - Irons, stations, hot air, desoldering
   - Equipment name and model
   - Capabilities
   - Tip/nozzle options available
   - Status

3. **ESD & Safety** - Straps, mats, gloves, dissipators
   - Item name
   - Specifications
   - Quantity
   - Status

4. **Consumables** - Solder, flux, solder wick, tips, nozzles
   - Item name
   - Type/specification
   - Stock level
   - Notes on quality/supplier

### Component Inventory

Organize by category with quantities:

1. **Passive Components**
   - Resistors (value ranges, quantities per value)
   - Capacitors (ceramic, electrolytic, film types)
   - Inductors
   - Other passive components

2. **Active Components**
   - Op-amps (part numbers, quantities)
   - Logic ICs (types available, quantities)
   - Transistors/MOSFETs
   - Diodes/Optocouplers
   - Other ICs

3. **Power Components**
   - Voltage regulators (types, quantities)
   - DC-DC converters
   - Linear regulators

4. **Discrete Components**
   - LEDs (colors, quantities)
   - Displays
   - Switches
   - Connectors

5. **Prototyping Materials**
   - Breadboards
   - Perfboards
   - Project enclosures
   - Headers/sockets

6. **Wire & Cable Stock**
   - Wire gauges available
   - Cable types (USB, network, audio, etc.)
   - Quantities

7. **Tools** (if also tracked in components)
   - Specialty tools
   - Measurement tools
   - Assembly tools

## Format Requested

**Hand Tools**
| Tool Name | Specification | Qty | Condition |
|---|---|---|---|
| | | | |

**Consumables Stock**
| Item | Type/Spec | Qty | Supplier Notes |
|---|---|---|---|
| | | | |

**Component Inventory**
| Component | Type/Value | Quantity | Notes |
|---|---|---|---|
| | | | |

(Organized by category)

## Cross-Reference Notes

- Which components are used in active projects
- Component stock levels (low? adequate? well-stocked?)
- Supplier information for common reorders
- Component organization system/location
- Any special storage requirements

## Response File Location

Place completed inventory at: `personal/incoming/tools-and-components.md`
