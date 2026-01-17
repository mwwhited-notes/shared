# Tools and Components Inventory Protocol

This protocol guides maintenance of `tools-and-components.md` - the inventory of hand tools, consumables, wire/cable, passive components, active components, ICs, and craft supplies.

## Overview

`tools-and-components.md` tracks workshop consumables, tools, and component stock that support the equipment documented in `Test Equipment/`, `Programmable Devices/`, etc.

**Key Principle:** Major equipment goes in dedicated inventories (Test Equipment, Programmable Devices, etc.). Consumables, accessories, and component stock go in tools-and-components.md.

## When to Add Items

Add items to tools-and-components.md when:
1. **Consumables** - Items that get used up (solder, flux, batteries)
2. **Hand tools** - Screwdrivers, pliers, meters that don't warrant their own directory
3. **Component stock** - Resistors, capacitors, ICs, transistors, connectors
4. **Wire & cable** - USB cables, HDMI, BNC, hookup wire
5. **Accessories** - Test leads, adapters, breakout boards
6. **Craft supplies** - Materials for projects (foam, tape, fasteners)

## When NOT to Add Items

Do NOT add to tools-and-components.md if:
1. **Major test equipment** → Use `Test Equipment/` instead
2. **Development boards** → Use `Programmable Devices/` instead
3. **Expansion boards/shields** → Use `Expansion Boards/` instead
4. **Camera equipment** → Use `Camera Collection/` instead
5. **Computing devices** → Use `Device Lab/` instead
6. **Household items** - Food, cleaning supplies, non-technical items

## Section Organization

The file is organized into these major sections:

### 1. Hand Tools
Small tools, measuring devices, soldering accessories
```markdown
| Item | Description | Qty | Purchased | Price |
```

### 2. Network Tools
Cable testers, crimpers, network-specific tools

### 3. Wire & Cable
All cables and wire stock (USB, HDMI, hookup wire, etc.)

### 4. Power Supplies (Bench/Adapter)
Small power adapters, buck/boost converters, wall warts
*Major bench supplies go in Test Equipment/*

### 5. Battery Chargers & Maintainers
Battery charging equipment

### 6. Consumables
Items that get used up: solder, flux, batteries, tips, nozzles

### 7. Test Leads & Probes
Oscilloscope probes, banana plugs, test clips, adapters

### 8. Prototyping
Breadboards, perfboard, headers, sockets, enclosures, development modules

### 9. Connectors & Breakout Boards
All connectors, adapters, switches, buttons, displays

### 10. Fasteners & Hardware
Screws, standoffs, nuts, bolts, zip ties, battery holders

### 11. Components Stock
- Passive Components (resistors, capacitors, potentiometers, diodes)
- Active Components (transistors, relays, motors, displays)
- ICs (logic, microcontrollers, op-amps, voltage regulators)

### 12. Components & Assembly Kits (Invoice-Based)
Pre-assembled and DIY electronics kits imported from invoice processing:
- Breadboards & Prototyping (breadboards, stripboards, proto kits)
- Connectors & Cable Management (BNC, keystone, HDMI, terminal blocks)
- Relays & Control Modules (SainSmart relays, RS-485 modules)
- LED & Optical Components (RGB strips, LED drivers, 7-segment displays)
- Component Assortments (resistor/capacitor/IC kits, potentiometers)
- Switches & Control (toggle switches, DIP switches)
- Serial & Communication (DB connectors, JST connectors)
- Soldering & Rework (T12 tips, soldering stations, stands)
- DIY Educational Kits (SMD practice, function generators, line followers)

### 13. Computer Peripherals
Mice, keyboards, hubs, docks, card readers, adapters

### 14. Raspberry Pi Accessories
Pi-specific accessories that aren't HATs

### 15. Craft & Project Supplies
Materials for projects (foam, tape, fasteners, etc.)

*For technical books, see [books.md](../books.md) - separate inventory maintained by BOOKS_PROTOCOL.md*

## Adding New Items

### Standard Entry Format

```markdown
| Item Name | Brief description with key specs | Qty | YYYY-MM-DD | $XX.XX |
```

### Examples

**Good entries:**
```markdown
| IRFZ44N N-ch MOSFET | 49A/55V TO-220 (Bridgold) | 20 | 2021-01-11 | $9.99 |
| USB 3.0 Extension Cable | 15ft A male to A female (WestCowboy) | 1 | 2023-01-13 | $11.99 |
| Resistors | 10KΩ 1/6W 1% metal film (uxcell) | 300 | 2022-12-30 | $9.59 |
```

**What to include:**
- **Item**: Part type or generic name
- **Description**: Key specs, voltage/current/size, manufacturer/brand in parentheses
- **Qty**: Quantity purchased (not current stock level)
- **Purchased**: Date in YYYY-MM-DD format
- **Price**: Total price for the quantity shown

### Multiple Purchases of Same Item

If you buy the same item multiple times, you can:

**Option 1: Separate entries (preferred for different dates)**
```markdown
| LM324N Op-amps | DIP-14, quad (vendor) | 25 | 2023-03-02 | $6.99 |
| LM324N Op-amps | DIP-14, quad (vendor) | 10 | 2021-12-30 | $5.99 |
```

**Option 2: Combined entry (for related purchases)**
```markdown
| U-Shaped Hair Pins | Brown 2.4" drawer divider clips (IKOCO, 80pcs) | 3 | 2023-01-05, 2023-02-11, 2021-11-08 | $18.38 (3x) |
```

## Organizing by Category

### Choosing the Right Section

Ask: "What is this item primarily used for?"

- **Is it a tool?** → Hand Tools
- **Is it a cable?** → Wire & Cable
- **Does it get consumed/replaced?** → Consumables
- **Is it a component for circuits?** → Components Stock (Passive/Active/ICs)
- **Is it a connector/switch/display?** → Connectors & Breakout Boards
- **Is it for prototyping/testing?** → Prototyping
- **Is it computer-related?** → Computer Peripherals
- **Is it for a project?** → Craft & Project Supplies

### Subsections

Within major sections, use subsections for clarity:

```markdown
## Components Stock

### Passive Components

| Type | Values/Range | Stock | Purchased | Price |
|------|--------------|-------|-----------|-------|
| Resistors | 10KΩ 1/6W 1% metal film (uxcell) | 300 | 2022-12-30 | $9.59 |
| Capacitors | Ceramic 0.1-10uF kit (EEEEE, 10 values 300pcs) | 300 | 2023-01-20 | $8.99 |

### Active Components

| Type | Part Numbers | Stock | Purchased | Price |
|------|--------------|-------|-----------|-------|
| Transistors | IRFZ44N N-ch MOSFET 49A/55V TO-220 (Bridgold) | 20 | 2021-01-11 | $9.99 |
```

## Cross-References

### Referencing Test Equipment

When consumables are for specific equipment:
```markdown
*See [Test Equipment/](Test%20Equipment/) for KSGER T12 soldering station, YaeCCC 858D hot air rework, and Hakko FR-301 desoldering gun.*
```

### Referencing Projects

When materials are for a specific project:
```markdown
*Materials for [DIY TrekPak-Style Dividers](projects/diy-trekpak-dividers/) project - custom drawer and case organizers.*
```

### Referencing Other Equipment

When an item is documented elsewhere but purchase info is relevant:
```markdown
*FT232H Breakout module (purchased 2021-03-15, $10.99) documented in [Test Equipment/ft232h-breakout/](Test%20Equipment/ft232h-breakout/)*
```

## Processing Orders: Amazon and AliExpress

When adding items from online retail orders:

### Common Processing Rules

1. **Date**: Use order placement date (not delivery)
2. **Price**: Use item subtotal (before shipping/tax)
3. **Quantity**: Actual quantity received
4. **Skip**: Household items, food, returned items
5. **Skip**: Items already documented in other inventories

### Components from Invoice Archives

When processing electronics components from invoice archives (Amazon, AliExpress):

**Organization Strategy:**
- Group similar components into the "Components & Assembly Kits (Invoice-Based)" section
- Create subsections for functional categories rather than technology types
- Include both individual items and pre-assembled kits
- Maintain source and date information for future reference/replacement

**Example subsection:**
```markdown
### Breadboards & Prototyping

| Item | Description | Qty | Purchased | Source | Cost |
|------|-------------|-----|-----------|--------|------|
| 3220-Hole Breadboard | Solderless circuit test board | 1 | 2025-04-09 | AliExpress | $16.70 |
| Mini Breadboards SYB-170 | 170 holes, 35x47mm prototype | 10 | 2025-04-07 | AliExpress | $3.70 |
```

**Decision Rule:** If a component appears in multiple invoices:
- Use separate entries per invoice (to track date/source)
- Add combined cost in parentheses if consolidating quantity info
- Example: `| KSGER T12 Tips | ... | 5 | 2023-2025 | AliExpress | $7.79 |`

### Amazon Order Processing

**Example order processing:**
```
Order placed January 11, 2021
Item(s) Subtotal: $51.95

Items:
- DSD TECH Bluetooth Module $7.99 → Add to Prototyping
- Vibration Motors (10pcs) $9.99 → Add to Active Components
- LCD2004 with I2C (2-pack) $15.99 → Add to Connectors (displays)
- MOSFET Transistors (20pcs) $9.99 → Add to Active Components
- Potato chips $8.99 → SKIP (food)
```

### AliExpress Order Processing

AliExpress orders are first archived in `.invoices/aliexpress-{YYYY}.md` files, then items are extracted to appropriate sections in tools-and-components.md.

**Special considerations for AliExpress:**
- Items often arrive in small batches with unpredictable delivery times
- Some orders may lack detailed product descriptions - research and document as needed
- Note any quality issues or counterfeited components (see ONLINE_SHOPPING_PROTOCOL.md)
- Use store/seller names in description for future reference

## Maintaining Accuracy

### What to Track

✅ **DO track:**
- Purchase date and price
- Quantity purchased
- Manufacturer/brand if known
- Key specifications

❌ **DON'T track:**
- Current stock levels (too much maintenance)
- Individual part locations
- Condition/quality ratings
- Detailed specifications (link to datasheets instead)

### Notes Section

Use notes for important context:
```markdown
*G502 for PowerSpec G474 workstation. Mac Mini cable for A1347 repair.*
```

Keep notes concise and relevant.

## Books - See books.md

**Technical books are NOT maintained in tools-and-components.md.**

Books are maintained in a separate `books.md` file following [BOOKS_PROTOCOL.md](BOOKS_PROTOCOL.md).

### Cross-Reference in tools-and-components.md

Add a simple reference note after the main inventory sections:
```markdown
*For technical books, see [books.md](books.md)*
```

## Craft & Project Supplies

For project materials:
- Link to the project if it exists in `projects/`
- Group related materials together
- Include notes about what the materials are for

```markdown
## Craft & Project Supplies

*Materials for [DIY TrekPak-Style Dividers](projects/diy-trekpak-dividers/) project.*

| Item | Description | Qty | Purchased | Price |
|------|-------------|-----|-----------|-------|
| U-Shaped Hair Pins | Brown 2.4" drawer divider clips (IKOCO, 80pcs) | 3 | 2023-01-05, 2023-02-11, 2021-11-08 | $18.38 (3x) |
```

## File Header

The file should start with:
```markdown
# Tools and Components Inventory

Consumables, hand tools, and miscellaneous supplies. For major equipment, see [Test Equipment/](Test%20Equipment/) and [workshop-capabilities.md](workshop-capabilities.md).

---
```

## File Footer

The file should end with:
```markdown
---

*Last updated: Month YYYY*
```

Update the date when making significant changes.

## Common Mistakes to Avoid

❌ **Don't:**
- Add major test equipment (use Test Equipment/ instead)
- Add development boards (use Programmable Devices/ instead)
- Add household/non-technical items
- Mix up sections (cables in Components, etc.)
- Forget to include vendor/brand in description
- Use relative dates ("last week", "recently")

✅ **Do:**
- Use consistent date format (YYYY-MM-DD)
- Include key specs in description
- Cross-reference related equipment
- Group similar items together
- Keep descriptions concise but informative

## Examples of Correct Categorization

| Item | Correct Section | Why |
|------|----------------|-----|
| Rigol DS1102E Oscilloscope | Test Equipment/ | Major bench equipment |
| Oscilloscope probes | Test Leads & Probes | Accessory/consumable |
| Arduino Uno | Programmable Devices/ | Development board |
| Arduino sensor shield | Expansion Boards/ | Shield/expansion |
| 10KΩ resistors (300pcs) | Components Stock → Passive | Component stock |
| IRFZ44N MOSFETs | Components Stock → Active | Component stock |
| USB-C hub | Computer Peripherals | Computer accessory |
| BNC cables | Wire & Cable | Cables/wire |
| Solder paste | Consumables | Gets used up |
| Logic probe | Test Leads & Probes | Test tool/probe |

---

## Version History

*Protocol Version: 1.1*
*Last Updated: 2026-01-17*

### v1.1 (2026-01-17) - Components & Assembly Kits Organization
- Added "Components & Assembly Kits (Invoice-Based)" section (section 12)
- Documented processing strategy for components from invoice archives
- Added AliExpress order processing guidelines
- Updated section numbering (Computer Peripherals now section 13, etc.)
- Added guidance for consolidating multi-source component purchases
- Clarified decision rules for component organization by functional category

### v1.0 (2026-01-07)
- Initial protocol documentation
- Defined section organization and cross-references
- Added processing guidelines for Amazon orders
- Documented common mistakes and categorization examples
