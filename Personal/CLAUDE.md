# CLAUDE.md - Personal Collections

This folder contains personal collections and purchase history documentation, designed to be a standalone repository of personal equipment inventory and transaction records.

## Overview

This repository organizes personal collections of equipment, gear, and materials across multiple categories with comprehensive documentation, cross-references, and purchase history.

**Primary Workflow:** Invoice processing and extraction to collections happens in this folder. All purchase history from Amazon, AliExpress, and other retailers is maintained in `.invoices/` with items extracted to appropriate equipment collections.

## Collections

### Equipment Inventories

- **Programmable Devices/** - FPGA, CPLD, MCU, and development boards with specifications and archived documentation
- **Expansion Boards/** - Arduino shields, Raspberry Pi HATs, BeagleBone capes, and other expansion modules
- **Test Equipment/** - Lab equipment documentation (oscilloscopes, DMMs, power supplies, programmers, 3D printer)
- **Vintage Computers/** - Apple IIc, Apple IIgs, TI-99/4A with peripherals (Floppy Emu, VGA adapters, RAM expansions)

### Personal Collections

- **Camera Collection/** - Photography equipment inventory (cameras, lenses, accessories, M42 vintage glass)
- **Device Lab/** - Computing devices for hacking/tinkering (tablets, phones, gaming handhelds, NAS, desktops)
- **Hobby Collection/** - Hobby and craft equipment (leathercraft, sewing, jewelry making, materials and tools)
- **Sports Collection/** - Sports and outdoor recreation equipment (water sports, biking, camping, fitness)

### Purchase History

- **.invoices/** - Purchase invoices from Amazon and AliExpress (2017-2026)

## Documentation Protocols

All protocols are located in `.claude/protocols/`.

### Programmable Devices
Follow `.claude/protocols/PROGRAMMABLE_DEVICES_DOCUMENTATION_PROTOCOL.md` when:
- Adding new development boards or microcontrollers
- Creating device README files with specifications
- Downloading and verifying datasheets/schematics
- Creating block diagrams for device architecture

**Key requirements:**
- Each device gets its own directory with standardized README.md
- Download PDFs locally (datasheets, schematics, pinouts)
- Verify downloaded files are valid PDFs, not HTML error pages
- Include pinout images and text-based pinout tables
- Document programming tools and interfaces

### Expansion Boards
Follow `.claude/protocols/EXPANSION_BOARDS_DOCUMENTATION_PROTOCOL.md` when:
- Adding shields, HATs, capes, or other expansion modules
- Documenting pin mappings and compatibility with parent boards
- Cross-referencing with boards in Programmable Devices/

### Test Equipment
Follow `.claude/protocols/EQUIPMENT_DOCUMENTATION_PROTOCOL.md` for lab equipment entries, including:
- Oscilloscopes, signal generators, multimeters
- Power supplies and battery backup systems
- Cooling systems and thermal management
- Programmers and protocol tools
- Specifications, manuals, software, and SCPI commands

### Vintage Computers
Follow `.claude/protocols/VINTAGE_COMPUTERS_DOCUMENTATION_PROTOCOL.md` when:
- Adding vintage computer systems or peripherals
- Documenting accessories (Floppy Emu, RAM expansions, video adapters)
- Cross-referencing with related FPGA soft cores or emulation projects

### Camera Collection
Follow `.claude/protocols/CAMERA_COLLECTION_PROTOCOL.md` when:
- Adding camera bodies (digital or film)
- Documenting lenses, teleconverters, and accessories
- Tracking lens mount compatibility
- Cross-referencing with purchase info

**Key focus areas:**
- Inventory with full technical specifications
- Lens mount compatibility and adapters
- Condition and service history
- Cross-references to purchase invoices

### Device Lab
Follow `.claude/protocols/DEVICE_LAB_PROTOCOL.md` when:
- Adding computing devices (tablets, phones, gaming handhelds, NAS, desktops)
- Documenting hackability (root, jailbreak, custom firmware options)
- Tracking devices for tinkering and repurposing projects
- Cross-referencing with home automation and other projects

**Key focus areas:**
- Inventory with full specifications
- Hackability status and options (CFW, root, homebrew)
- Project ideas for repurposing devices

### Hobby Collection
Follow `.claude/protocols/HOBBY_COLLECTION_PROTOCOL.md` when:
- Adding hobby and craft equipment (leathercraft, sewing, jewelry making)
- Documenting materials and supplies inventory
- Tracking project ideas and inspiration
- Cross-referencing with related creative projects

### Sports Collection
Follow `.claude/protocols/SPORTS_COLLECTION_PROTOCOL.md` when:
- Adding sports and outdoor recreation equipment (water sports, biking, camping, fitness)
- Documenting maintenance and service history
- Planning trips and adventures
- Cross-referencing with outdoor projects

### Tools and Components
Follow `.claude/protocols/TOOLS_AND_COMPONENTS_PROTOCOL.md` when:
- If tools-and-components.md exists in parent repository
- Processing orders for tools, wire, components, or consumables
- Organizing inventory into appropriate sections

### Online Shopping & Invoices
Follow `.claude/protocols/ONLINE_SHOPPING_PROTOCOL.md` when:
- Documenting purchase history and seller experiences
- Processing invoices from Amazon and AliExpress
- Tracking pricing, shipping quality, and seller reliability
- Maintaining `.invoices/` archive files

## Key Directories

### Equipment Collections Index

Each collection has its own README.md index:

**Technical Equipment:**
- `Programmable Devices/readme.md` - Device inventory with programmer compatibility
- `Expansion Boards/readme.md` - Shields, HATs, capes index with compatibility info
- `Test Equipment/readme.md` - Lab equipment index (oscilloscopes, meters, supplies)
- `Vintage Computers/readme.md` - Apple II/TI-99/4A systems and peripherals

**Personal Collections:**
- `Camera Collection/readme.md` - Photography equipment (bodies, lenses, mount compatibility)
- `Device Lab/readme.md` - Computing devices for hacking (tablets, phones, NAS, gaming)
- `Hobby Collection/readme.md` - Hobby and craft equipment (leathercraft, sewing, jewelry)
- `Sports Collection/readme.md` - Sports and outdoor recreation equipment

### Purchase History

Invoice archives organized by retailer and year in `.invoices/`:
- `amazon-2017.md` through `amazon-2020.md` - Amazon orders
- `aliexpress-2022.md` through `aliexpress-2026.md` - AliExpress orders

## File Naming Conventions

- Collection directories: Title Case with spaces (`Camera Collection`, `Device Lab`)
- Equipment subdirectories: lowercase with hyphens (`nikon-d800`, `sony-psvita`)
- Protocol files: UPPERCASE_WITH_UNDERSCORES.md
- Invoice archives: `{retailer}-{year}.md` format

## Common Tasks

### Adding a New Camera

1. Create directory in `Camera Collection/` following naming convention
2. Use `.claude/protocols/CAMERA_COLLECTION_PROTOCOL.md` template
3. Include specifications, documentation, and condition notes
4. Add entry to `Camera Collection/readme.md` index
5. Link to relevant invoice in `.invoices/`

### Adding a Device for Hacking

1. Create directory in `Device Lab/` with appropriate category
2. Use `.claude/protocols/DEVICE_LAB_PROTOCOL.md` template
3. Document hackability options (root, custom firmware, bootloader status)
4. Add entry to `Device Lab/readme.md` index
5. Cross-reference with invoice if purchased

### Processing a Purchase

1. Add details to appropriate `.invoices/{retailer}-{year}.md` file
2. Extract items to relevant collection directories
3. Add quality notes if applicable (counterfeits, defects, shipping issues)
4. Cross-reference between invoice and collection items

## Maintenance

### Regular Tasks

| Task | Frequency | Description |
|------|-----------|-------------|
| Condition check | Quarterly | Update status of equipment, note any damage |
| Inventory review | Semi-annually | Verify all items accounted for |
| Invoice processing | As-needed | Process new purchases from receipts |
| Link verification | Quarterly | Ensure all cross-references are valid |

### File Updates

When modifying collections:
- Update collection's README.md index
- Update invoice records if item purchased
- Add cross-references to related items
- Update entry dates and status

## Cross-References

### Within Collections
- Equipment often references purchase invoices by date and amount
- Collections may cross-reference related items (e.g., compatible adapters, spare parts)
- Camera lenses reference compatible camera bodies

### To Parent Repository
When this repository is cloned/moved to another location:
- Parent repository references point to `../path/from/parent/`
- These references should be updated if repository structure changes
- Standalone use requires removing parent repository references

## Status Tracking

Use consistent status labels across all collections:

| Status | Meaning |
|--------|---------|
| **Active** | In regular use |
| **Shelved** | Working but not currently used |
| **Project** | Reserved for specific planned project |
| **Parts** | Non-functional, useful for parts/reference |

## Condition Tracking

| Condition | Meaning |
|-----------|---------|
| **Excellent** | Like new, minimal use/wear |
| **Good** | Normal wear, fully functional |
| **Fair** | Cosmetic issues, minor wear, fully functional |
| **Poor** | Significant wear, still functional with caution |
| **Needs Repair** | Non-functional, repairable with effort |

## Invoice Organization

### Archive Format

Invoices are organized by retailer and year following pattern:
- `.invoices/{retailer}-{year}.md`
- Examples: `amazon-2017.md`, `aliexpress-2025.md`

### Invoice File Structure

```markdown
# [Retailer] Orders - [Year]

**Summary:**
- Period: [YYYY-MM-DD] to [YYYY-MM-DD]
- Total Orders: [#]
- Total Spent: $[amount]

---

## Order Details

### Order #[number] - [Date]
- **Items:** [description]
- **Price:** $[item] + $[shipping] shipping + $[tax] tax = **$[total]**
- **Condition:** [new/used/refurbished]
- **Shipping:** [method]
- **Notes:** [any relevant details]
```

### Quality Alerts

Document any issues discovered:
- Counterfeited components
- Quality defects
- Shipping damage
- Seller reliability issues

## Getting Started

1. **Explore a collection** - Browse `Camera Collection/`, `Device Lab/`, etc.
2. **Check inventory** - Read the README.md in each collection folder
3. **Review purchases** - See `.invoices/` for detailed transaction history
4. **Add new items** - Use the appropriate protocol in `.claude/protocols/`
5. **Update indices** - Keep collection README.md files current

## Invoice Processing Workflow

All invoice and purchase history processing happens in this Personal folder:

### Process Flow

1. **Archive Invoice** - Add new purchase receipt to `.invoices/{retailer}-{year}.md`
   - Record order date, items, quantity, price, seller
   - Note any quality issues (counterfeits, damage, defects)
   - Track shipping status and delivery condition

2. **Extract Items** - Move individual items to appropriate collections
   - Add item to correct collection directory
   - Create README.md with specifications
   - Link back to invoice source

3. **Update Collections** - Maintain collection README.md indices
   - Add entry to collection table
   - Update status (Active/Shelved/Project)
   - Add cross-reference to invoice

4. **Document Sellers** - Update seller tracking
   - Add/update seller notes in root ShoppingOnline.md
   - Track packaging quality and shipping speed
   - Note any problematic sellers

### Archive Format

Invoices follow standardized format in `.invoices/`:

```markdown
# [Retailer] Orders - [Year]

**Summary:**
- Period: YYYY-MM-DD to YYYY-MM-DD
- Total Orders: [#]
- Total Spent: $[amount]

---

### Order #[number] - [Date]
- **Items:** [description]
- **Price:** $[item] + $[shipping] + $[tax] = $[total]
- **Condition:** [new/used/refurbished]
- **Notes:** [any issues or observations]
```

### Quality Alerts

Document any issues discovered:
- Suspected counterfeits
- Quality defects or damage
- Shipping delays
- Seller reliability problems

## Customization

This structure can be adapted for different purposes:
- Remove collections not needed
- Add new collections following existing protocols
- Extend protocols with additional fields
- Customize status/condition labels per collection
- Modify invoice archive structure if needed

---

*Repository Template Version: 1.0*
*Last Updated: 2026-01-17*
*Designed for: Personal equipment collections and purchase history*
