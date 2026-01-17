# Personal Collections Repository

Complete inventory of personal equipment, collections, and purchase history organized by category.

**Quick Reference:** 40+ collections across 8 categories | [Configuration](CLAUDE.md) | [Task Tracking](TODO.md) | [Protocols](.claude/protocols/README.md)

---

## Collections Overview

### Technical Equipment (Work-Related)

Professional development tools and lab equipment for electronics, embedded systems, and retro computing projects.

| Collection | Items | Status | Category |
|---|---|---|---|
| [Programmable Devices](Programmable%20Devices/) | 20+ | Active | Development boards (FPGA, CPLD, MCU) |
| [Expansion Boards](Expansion%20Boards/) | 30+ | Active | Shields, HATs, capes |
| [Test Equipment](Test%20Equipment/) | 40+ | Active | Lab instruments (oscilloscopes, meters, supplies) |
| [Vintage Computers](Vintage%20Computers/) | 5+ | Active | Apple II, TI-99/4A systems & peripherals |

### Personal Collections (Hobby & Recreation)

Equipment and materials for personal hobbies, recreation, and lifestyle activities.

| Collection | Items | Status | Category |
|---|---|---|---|
| [Camera Collection](Camera%20Collection/) | 20+ | Active | Photography gear (bodies, lenses, accessories) |
| [Device Lab](Device%20Lab/) | 40+ | Active | Computing devices for hacking (tablets, phones, NAS) |
| [Hobby Collection](Hobby%20Collection/) | 12+ | Active | Craft equipment (leathercraft, sewing, jewelry) |
| [Sports Collection](Sports%20Collection/) | 10+ | Active | Recreation gear (water sports, biking, camping, fitness) |

---

## Purchase History

Complete transaction records from major retailers:

- **Amazon** - Orders from 2017-2020 (100+ orders, $9,000+ total)
- **AliExpress** - Orders from 2022-2026 (61 orders, $821.22 total)

All invoices archived in [.invoices/](.invoices/) organized by retailer and year.

---

## Documentation Standards

All collections follow standardized protocols documented in `.claude/protocols/`:

| Protocol | Purpose | Target Collections |
|---|---|---|
| PROGRAMMABLE_DEVICES_DOCUMENTATION_PROTOCOL.md | Development board documentation | Programmable Devices, Expansion Boards |
| EQUIPMENT_DOCUMENTATION_PROTOCOL.md | Test equipment documentation | Test Equipment |
| VINTAGE_COMPUTERS_DOCUMENTATION_PROTOCOL.md | Vintage system documentation | Vintage Computers |
| CAMERA_COLLECTION_PROTOCOL.md | Photography equipment | Camera Collection |
| DEVICE_LAB_PROTOCOL.md | Computing devices | Device Lab |
| HOBBY_COLLECTION_PROTOCOL.md | Hobby equipment | Hobby Collection |
| SPORTS_COLLECTION_PROTOCOL.md | Sports gear | Sports Collection |
| ONLINE_SHOPPING_PROTOCOL.md | Purchase tracking | All collections |

---

## Quick Start

1. **Explore a Collection** - Click any collection above to browse inventory
2. **Check Purchase History** - See [.invoices/](.invoices/) for transaction records
3. **Review Standards** - Read [CLAUDE.md](CLAUDE.md) for documentation guidelines
4. **Add New Items** - Follow appropriate protocol in [.claude/protocols/](.claude/protocols/)
5. **Track Tasks** - See [TODO.md](TODO.md) for pending work

---

## Collection Structure

Each collection follows this standard format:

```
Collection/
├── readme.md              # Index with item table, quick reference
├── item-name/
│   ├── README.md          # Full specifications and documentation
│   ├── datasheet.pdf      # Technical documentation
│   ├── manual.pdf         # User manual
│   └── notes.md           # Usage notes, modifications, condition
└── ...
```

---

## Key Features

### Comprehensive Documentation
- Full specifications for all major equipment
- Archived PDFs for datasheets and manuals
- Purchase history and sourcing information
- Condition tracking and service records

### Cross-References
- Links between related items
- Purchase invoice references
- Project connections (where applicable)
- Supplier/seller tracking

### Standards Compliance
- Consistent README format across collections
- Standardized metadata and status tracking
- Regular index maintenance
- Documentation protocol adherence

---

## Repository Information

| Aspect | Details |
|---|---|
| **Purpose** | Personal equipment inventory and transaction history |
| **Structure** | 8 equipment collections + purchase archives |
| **Organization** | Category-based with standardized documentation |
| **Standards** | 10 protocols in `.claude/protocols/` |
| **Configuration** | [CLAUDE.md](CLAUDE.md) |
| **Task Tracking** | [TODO.md](TODO.md) |
| **Last Updated** | 2026-01-17 |
| **Status** | Active maintenance |

---

## Usage Notes

### Standalone Repository
This folder can be used as a standalone repository separate from the parent documentation project. When moving to a different location:

1. Verify all collection directories are present
2. Check `.claude/protocols/` has all relevant protocols
3. Verify `.invoices/` has purchase history archives
4. Update any external cross-references as needed

### Integration with Parent Repository
When part of a larger project repository, this folder maintains these collections while parent repository maintains:
- Public reference documentation
- Project files
- Shared configurations

---

## Status Legend

| Status | Meaning |
|---|---|
| **Active** | In regular use |
| **Shelved** | Working but not currently used |
| **Project** | Reserved for specific planned project |
| **Parts** | Non-functional, useful for parts/reference |

---

*Repository Version: 1.0*
*Last Updated: 2026-01-17*
*Type: Personal Equipment Collections and Purchase History*
