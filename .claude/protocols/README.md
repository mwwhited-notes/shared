# Documentation Protocols Index

This directory contains protocols for documenting equipment, projects, and inventory in this repository.

## Available Protocols

### Equipment & Inventory

| Protocol | Purpose | Key Sections |
|----------|---------|--------------|
| [PROGRAMMABLE_DEVICES_DOCUMENTATION_PROTOCOL.md](PROGRAMMABLE_DEVICES_DOCUMENTATION_PROTOCOL.md) | Document FPGA, CPLD, MCU, and development boards | Specifications, datasheets, pinouts, programming tools |
| [EXPANSION_BOARDS_DOCUMENTATION_PROTOCOL.md](EXPANSION_BOARDS_DOCUMENTATION_PROTOCOL.md) | Document Arduino shields, Pi HATs, BeagleBone capes | Pin mappings, compatibility, parent board cross-refs |
| [EQUIPMENT_DOCUMENTATION_PROTOCOL.md](EQUIPMENT_DOCUMENTATION_PROTOCOL.md) | Document test equipment (scopes, meters, supplies) | Specifications, manuals, software, SCPI commands |
| [VINTAGE_COMPUTERS_DOCUMENTATION_PROTOCOL.md](VINTAGE_COMPUTERS_DOCUMENTATION_PROTOCOL.md) | Document vintage computers and peripherals | System specs, peripherals, FPGA soft core cross-refs |
| [CAMERA_COLLECTION_PROTOCOL.md](CAMERA_COLLECTION_PROTOCOL.md) | Document cameras, lenses, and accessories | Bodies, lenses, mount compatibility, astrophotography |
| [DEVICE_LAB_PROTOCOL.md](DEVICE_LAB_PROTOCOL.md) | Document computing devices for hacking/tinkering | Tablets, phones, NAS, hackability, repurposing projects |
| [TOOLS_AND_COMPONENTS_PROTOCOL.md](TOOLS_AND_COMPONENTS_PROTOCOL.md) | Maintain tools-and-components.md inventory | Hand tools, wire, consumables, component stock |

### Projects & Documentation

| Protocol | Purpose | Key Sections |
|----------|---------|--------------|
| [PROJECTS_PROTOCOL.md](PROJECTS_PROTOCOL.md) | Document active projects in projects/ directory | README format, build logs, parts lists, status tracking |
| [PROJECT_REVIEW_PROTOCOL.md](PROJECT_REVIEW_PROTOCOL.md) | Periodic inventory review and maintenance | Full review workflow, quick sync, cross-reference checks |
| [ONLINE_SHOPPING_PROTOCOL.md](ONLINE_SHOPPING_PROTOCOL.md) | Track seller experiences and purchases | Good/bad sellers, pricing, shipping quality |

### Maintenance & Performance

| Protocol | Purpose | Key Sections |
|----------|---------|--------------|
| [CLAUDE_MD_MAINTENANCE_PROTOCOL.md](CLAUDE_MD_MAINTENANCE_PROTOCOL.md) | Keep CLAUDE.md concise for performance | Content structure, refactoring process, length guidelines |
| [TODO_MD_ARCHIVAL_PROTOCOL.md](TODO_MD_ARCHIVAL_PROTOCOL.md) | Archive completed tasks to changes/ directory | Archival triggers, file naming, archive format, cleanup process |

## Quick Reference

### When Adding New Equipment

**Is it a...**
- Development board (MCU/FPGA/CPLD)? → [PROGRAMMABLE_DEVICES_DOCUMENTATION_PROTOCOL.md](PROGRAMMABLE_DEVICES_DOCUMENTATION_PROTOCOL.md)
- Shield/HAT/cape? → [EXPANSION_BOARDS_DOCUMENTATION_PROTOCOL.md](EXPANSION_BOARDS_DOCUMENTATION_PROTOCOL.md)
- Oscilloscope/meter/supply? → [EQUIPMENT_DOCUMENTATION_PROTOCOL.md](EQUIPMENT_DOCUMENTATION_PROTOCOL.md)
- Vintage computer/peripheral? → [VINTAGE_COMPUTERS_DOCUMENTATION_PROTOCOL.md](VINTAGE_COMPUTERS_DOCUMENTATION_PROTOCOL.md)
- Camera/lens/photo accessory? → [CAMERA_COLLECTION_PROTOCOL.md](CAMERA_COLLECTION_PROTOCOL.md)
- Tablet/phone/NAS/gaming device? → [DEVICE_LAB_PROTOCOL.md](DEVICE_LAB_PROTOCOL.md)
- Hand tool/wire/component/consumable? → [TOOLS_AND_COMPONENTS_PROTOCOL.md](TOOLS_AND_COMPONENTS_PROTOCOL.md)

### When Working on Projects

**Are you...**
- Starting a new build project? → [PROJECTS_PROTOCOL.md](PROJECTS_PROTOCOL.md)
- Doing quarterly inventory review? → [PROJECT_REVIEW_PROTOCOL.md](PROJECT_REVIEW_PROTOCOL.md)
- Documenting a seller experience? → [ONLINE_SHOPPING_PROTOCOL.md](ONLINE_SHOPPING_PROTOCOL.md)

### When Managing Documentation

**Are you...**
- CLAUDE.md getting too long (>600 lines)? → [CLAUDE_MD_MAINTENANCE_PROTOCOL.md](CLAUDE_MD_MAINTENANCE_PROTOCOL.md)
- TODO.md has >10 completed tasks? → [TODO_MD_ARCHIVAL_PROTOCOL.md](TODO_MD_ARCHIVAL_PROTOCOL.md)
- Major topic/milestone completed? → [TODO_MD_ARCHIVAL_PROTOCOL.md](TODO_MD_ARCHIVAL_PROTOCOL.md)
- Performance issues from large context? → Check both maintenance protocols

## Protocol Maintenance

### Version History

All protocols should include:
```markdown
---

*Protocol Version: X.Y*
*Last Updated: Month YYYY*
```

### When to Update Protocols

Update protocols when:
- Adding new inventory categories
- Changing documentation standards
- Improving templates or workflows
- Clarifying ambiguous sections
- Adding new cross-reference patterns

### Protocol Consistency

All protocols follow these common patterns:
1. **Overview** - What the protocol covers
2. **When to Use** - Specific triggers for using the protocol
3. **Directory Structure** - File organization
4. **Templates** - README/documentation formats
5. **Cross-References** - Links to related inventories
6. **Common Mistakes** - What to avoid
7. **Examples** - Real-world usage

## Cross-Protocol Dependencies

### Equipment Hierarchies

```
Major Equipment (own directories)
├── Test Equipment/
├── Programmable Devices/
├── Expansion Boards/
├── Vintage Computers/
├── Camera Collection/
└── Device Lab/

Supporting Items (tools-and-components.md)
├── Consumables (solder, flux, batteries)
├── Accessories (probes, cables, adapters)
├── Component stock (resistors, ICs)
└── Hand tools
```

### Project Relationships

```
project-ideas.md (backlog)
    ↓
projects/ (active implementation)
    ↓
workshop-capabilities.md (completed capabilities)
```

Equipment from inventories supports projects, which reference back to equipment.

## Common Cross-References

### From Equipment to Projects
```markdown
## Related Projects

- [Project Name](../../projects/project-name/) - Brief description
```

### From Projects to Equipment
```markdown
## Equipment Used

- [Equipment Name](../../Test%20Equipment/equipment-name/) - What it's used for
```

### From Tools to Equipment
```markdown
*See [Test Equipment/](Test%20Equipment/) for full documentation of [equipment name].*
```

## Finding the Right Protocol

### Decision Tree

```
What are you documenting?
│
├─ Is it major bench equipment?
│  └─ YES → EQUIPMENT_DOCUMENTATION_PROTOCOL.md
│
├─ Is it a development board with its own firmware/bootloader?
│  └─ YES → PROGRAMMABLE_DEVICES_DOCUMENTATION_PROTOCOL.md
│
├─ Does it plug into a dev board as an expansion?
│  └─ YES → EXPANSION_BOARDS_DOCUMENTATION_PROTOCOL.md
│
├─ Is it a pre-2000s computer or peripheral?
│  └─ YES → VINTAGE_COMPUTERS_DOCUMENTATION_PROTOCOL.md
│
├─ Is it camera/photography equipment?
│  └─ YES → CAMERA_COLLECTION_PROTOCOL.md
│
├─ Is it a computing device for hacking/repurposing?
│  └─ YES → DEVICE_LAB_PROTOCOL.md
│
├─ Is it a hand tool, wire, component, or consumable?
│  └─ YES → TOOLS_AND_COMPONENTS_PROTOCOL.md
│
├─ Is it an active build project?
│  └─ YES → PROJECTS_PROTOCOL.md
│
├─ Is it a purchase experience to document?
│  └─ YES → ONLINE_SHOPPING_PROTOCOL.md
│
├─ Is CLAUDE.md getting too long or cluttered?
│  └─ YES → CLAUDE_MD_MAINTENANCE_PROTOCOL.md
│
└─ Do you have >10 completed tasks in TODO.md?
   └─ YES → TODO_MD_ARCHIVAL_PROTOCOL.md
```

## Getting Started

1. **Identify what you're documenting** - Use decision tree above
2. **Read the relevant protocol** - Follow the templates and guidelines
3. **Check existing examples** - Look at similar items already documented
4. **Cross-reference appropriately** - Link related equipment/projects
5. **Update last-modified dates** - Keep timestamps current

## Questions or Improvements

If you encounter:
- **Unclear guidance** → Update protocol with clarification
- **Missing category** → Add to protocol or create new protocol
- **Conflicting protocols** → Resolve and document the decision
- **New use case** → Add example to protocol

---

*Protocol Index Version: 1.1*
*Last Updated: 2026-01-07*
