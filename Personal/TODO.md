# TODO - Personal Collections Repository

Personal equipment inventory and purchase history task tracking.

---

## Equipment Inventory

### Technical Equipment Status

| Equipment Type | Status | Priority |
|---|---|---|
| Programmable Devices | Active | Maintain |
| Expansion Boards | Active | Maintain |
| Test Equipment | Active | Maintain |
| Vintage Computers | Active | Archive |

### Personal Collections Status

| Collection | Status | Items | Priority |
|---|---|---|---|
| Camera Collection | Active | Photography gear | Maintain |
| Device Lab | Active | Computing devices | Maintain |
| Hobby Collection | Active | Craft equipment | Maintain |
| Sports Collection | Active | Recreation gear | Maintain |

---

## Active Tasks

### Invoice Processing (Primary Workflow)

**Amazon Orders:**
- [x] Process Amazon 2017-2020 invoices
- [ ] Process Amazon 2016 invoices - extract items to collections
- [ ] Process Amazon 2015 invoices - extract items to collections
- [ ] Process Amazon 2014 invoices - extract items to collections
- [ ] Process Amazon 2013 invoices - extract items to collections
- [ ] Process Amazon 2012 invoices - extract items to collections
- [ ] Process Amazon 2011 invoices - extract items to collections
- [ ] Process Amazon 2010 invoices - extract items to collections
- [ ] Process Amazon 2009 invoices - extract items to collections
- [ ] Process Amazon 2008 invoices - extract items to collections
- [ ] Process Amazon 2007 invoices - extract items to collections
- [ ] Process Amazon 2006 invoices - extract items to collections
- [ ] Process Amazon 2005 invoices - extract items to collections
- [ ] Process Amazon 2004 invoices - extract items to collections

**AliExpress Orders:**
- [x] Archive AliExpress 2022-2026 invoices in `.invoices/`
- [ ] Extract AliExpress 2022-2026 items to collections
- [ ] Add quality notes for known issues (counterfeits, defects)
- [ ] Complete itemization for incomplete orders

**Other Retailers:**
- [ ] Process Mouser orders if archived
- [ ] Process eBay seller tracking updates
- [ ] Add any other retailer orders to archive

### Documentation

- [ ] Verify all collections have updated README.md indices
- [ ] Update cross-references between related collections
- [ ] Document equipment condition and service history
- [ ] Add missing specifications to inventory items
- [ ] Update ShoppingOnline.md seller notes from invoices

### Equipment Organization

- [ ] Verify all major equipment has dedicated directory
- [ ] Check for items missing from collections
- [ ] Update status tracking (Active/Shelved/Project/Parts)
- [ ] Identify equipment needing repair or maintenance
- [ ] Cross-reference new items to purchase invoices

---

## Reference

### Collections Overview

```
Personal/
├── Programmable Devices/      - Dev boards (FPGA, CPLD, MCU)
├── Expansion Boards/          - Shields, HATs, capes
├── Test Equipment/            - Lab instruments
├── Vintage Computers/         - Apple II, TI-99/4A systems
├── Camera Collection/         - Photography equipment
├── Device Lab/                - Computing devices for hacking
├── Hobby Collection/          - Craft equipment
├── Sports Collection/         - Recreation gear
├── .invoices/                 - Purchase history
└── .claude/protocols/         - Documentation standards
```

### Important Files

- `.claude/protocols/PROGRAMMABLE_DEVICES_DOCUMENTATION_PROTOCOL.md` - Dev board standards
- `.claude/protocols/EXPANSION_BOARDS_DOCUMENTATION_PROTOCOL.md` - Shield documentation
- `.claude/protocols/EQUIPMENT_DOCUMENTATION_PROTOCOL.md` - Lab equipment standards
- `.claude/protocols/VINTAGE_COMPUTERS_DOCUMENTATION_PROTOCOL.md` - Vintage systems
- `.claude/protocols/CAMERA_COLLECTION_PROTOCOL.md` - Photography gear standards
- `.claude/protocols/DEVICE_LAB_PROTOCOL.md` - Computing device standards
- `.claude/protocols/HOBBY_COLLECTION_PROTOCOL.md` - Hobby equipment standards
- `.claude/protocols/SPORTS_COLLECTION_PROTOCOL.md` - Sports gear standards
- `.claude/protocols/ONLINE_SHOPPING_PROTOCOL.md` - Purchase history standards

### Invoice Archives

All purchase history organized in `.invoices/`:
- `amazon-2017.md` through `amazon-2020.md` - Amazon orders
- `aliexpress-2022.md` through `aliexpress-2026.md` - AliExpress orders

---

## Maintenance Schedule

| Task | Frequency | Last Done |
|---|---|---|
| Equipment condition check | Quarterly | 2026-01-17 |
| Invoice processing | As-needed | 2026-01-17 |
| Collection index review | Semi-annually | 2026-01-17 |
| Protocol updates | As-needed | 2026-01-17 |

---

*Last updated: 2026-01-17*
*Repository type: Personal Equipment Collections*
*Designed for standalone use or as subdirectory of larger repository*
