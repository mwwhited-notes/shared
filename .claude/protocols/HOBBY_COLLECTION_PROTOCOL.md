# Hobby Collection Documentation Protocol

Standard procedure for documenting hobby and craftwork equipment, tools, and supplies.

---

## Overview

This protocol ensures consistent documentation of tools and materials for personal hobby projects including leathercraft, sewing, jewelry making, and other crafts. The goal is to maintain an organized inventory with:

- **Tool & equipment inventory** - What you have, condition, and status
- **Material stock tracking** - Consumables, thread colors, leather types, findings, etc.
- **Project ideas** - Inspiration and planned projects using available materials
- **Cross-references** - Links to project files and inspiration sources

---

## Directory Structure

```
Hobby Collection/
├── readme.md                    # Collection index with all hobbies
├── leathercraft/
│   ├── tools/
│   │   └── [tool-specific-files]
│   └── materials/
│       └── [material-inventory]
├── sewing/
│   ├── machines/
│   ├── tools/
│   └── materials/
├── jewelry-making/
│   ├── tools/
│   └── materials/
└── other-crafts/
    └── [craft-specific-organization]
```

---

## Collection Index (readme.md) Format

The master readme should include:

1. **Quick Reference Summary** - Table with hobby type, item count, and key examples
2. **Category Sections** - One section per hobby/craft type with organized tables
3. **Status Legend** - Active, Shelved, Project-candidate definitions
4. **Hackability/Capability Legend** - Rating system for tool capability or project difficulty
5. **Project Ideas** - Organized by hobby type with materials/tools needed
6. **Cross-References** - Links to related project directories

### Quick Reference Format

```markdown
| Hobby | Item Count | Status | Key Example |
|-------|-----------|--------|------------|
| Leathercraft | 12 | Active | Edge beveler set |
| Sewing | 8 | Active | Sewing machine |
| Jewelry Making | 5 | Shelved | Beading supplies |
```

### Detailed Hobby Section Format

```markdown
## [Hobby Name]

[Brief description of hobby and what's included]

| Item | Description | Qty | Condition | Status | Date | Cost/Notes |
|------|-------------|-----|-----------|--------|------|-----------|
| [Item] | [Specs/details] | [Qty] | [Good/Fair/Poor] | [Active/Shelved] | [YYYY-MM-DD] | [Details] |
```

---

## Item Categories by Hobby

### Leathercraft

| Item Type | Examples | Key Attributes |
|-----------|----------|-----------------|
| **Tools** | Edge bevelers, stripers, edge slickers, stamps | Material (steel/brass), sizes, condition |
| **Materials** | Leather hides, dyes, finishes, rivets, snaps | Type (veg-tan/chrome), thickness, color |
| **Hardware** | Rivets, snaps, clasps, buckles | Material, size, finish |
| **Reference** | Pattern books, technique guides | Scope, skill level |

### Sewing

| Item Type | Examples | Key Attributes |
|-----------|----------|-----------------|
| **Machines** | Sewing machines, sergers, embroidery machines | Brand, model, stitch types, condition |
| **Tools** | Shears, scissors, seam rippers, measuring tools | Type, material, quality, sharpness |
| **Materials** | Thread, fabric, elastic, interfacing, zippers | Type, color, weight, quantity |
| **Patterns** | Commercial patterns, DIY designs | Size range, project type, difficulty |

### Jewelry Making

| Item Type | Examples | Key Attributes |
|-----------|----------|-----------------|
| **Tools** | Pliers, wire cutters, beading needles | Type (round-nose, flat-nose), size, quality |
| **Materials** | Beads, wire, findings, clasps | Type, size, material (glass/metal/stone) |
| **Supplies** | Adhesives, polishes, storage containers | Type, quantity, condition |

---

## Status Tracking

Use consistent status labels:

| Status | Meaning |
|--------|---------|
| **Active** | In regular use for current projects |
| **Shelved** | Working but not currently used |
| **Project** | Reserved for specific planned project |
| **Parts** | Non-functional, useful for parts/inspiration |

---

## Condition Tracking

| Condition | Meaning |
|-----------|---------|
| **Good** | Fully functional, minimal wear |
| **Fair** | Functional, some wear/cosmetic issues |
| **Poor** | Functional but significant issues |
| **Needs Repair** | Non-functional, repairable |

---

## Project Ideas Format

Organize by hobby type with materials and tools needed:

```markdown
## Project Ideas

### Leathercraft

- [ ] **Project Name** - Brief description
  - Materials needed: [List]
  - Tools needed: [List]
  - Difficulty: [Beginner/Intermediate/Advanced]
  - Est. time: [Time estimate]
  - Inspiration: [Source/reference]

### Sewing

- [ ] **Project Name** - Brief description
  - Materials: [List]
  - Techniques: [Stitching types, special skills]
  - Difficulty: [Level]

### Jewelry Making

- [ ] **Project Name** - Brief description
  - Beads/materials: [List]
  - Techniques: [Stringing, wire-work, etc.]
  - Difficulty: [Level]
```

---

## Cross-References

### Linking to Projects

If hobby work connects to other projects or repositories:

```markdown
## Related Projects

- [Project Name](../../projects/project-name/) - Brief description
```

### Linking to Equipment

If using equipment from other collections:

```markdown
*This hobby uses equipment documented in [Camera Collection/](../../Camera%20Collection/) for photography of finished pieces.*
```

---

## Data from Invoice Processing

When importing items from purchase invoices:

1. **Extract from invoice** - Identify hobby-related items
2. **Categorize by hobby** - Assign to appropriate section
3. **Add acquisition date** - Use original purchase date from invoice
4. **Add cost information** - Document original purchase price
5. **Research materials** - Determine type, color, quantity where not obvious
6. **Set initial status** - Assume "Active" unless invoice notes otherwise

### Invoice Format Example

When processing invoices, use consistent format:

```markdown
| Item | Description | Qty | Purchased | Source | Cost | Notes |
|------|-------------|-----|-----------|--------|------|-------|
| Leather Hide | Vegetable-tanned brown, 2mm | 1 | 2017-06-15 | Amazon | $29.99 | [Grade/type] |
| Thread Assortment | 20-color polyester set | 1 | 2017-05-20 | Amazon | $12.49 | [Weights included] |
```

---

## Maintenance Tasks

### Regular Inventory Review

| Task | Frequency | Notes |
|------|-----------|-------|
| Condition check | Quarterly | Update status of tools, note any damage |
| Material count | As-needed | When starting new projects |
| Consumable restocking | As-needed | Thread, dyes, adhesives, etc. |
| Project idea update | As-needed | Add new ideas when inspiration strikes |

### Updating from Invoice Processing

When processing new purchase invoices:

1. [ ] Identify all hobby-related items
2. [ ] Categorize by hobby type
3. [ ] Update appropriate section in readme.md
4. [ ] Add purchase date and cost
5. [ ] Research material specifications if needed
6. [ ] Link to project ideas if applicable
7. [ ] Update Quick Reference Summary totals

---

## Common Cross-Collection References

### Equipment that might reference hobbies

Test Equipment → Soldering tools, light tables, microscopes for jewelry
Camera Collection → Photography equipment for documenting finished work
Device Lab → Tablets for viewing patterns/tutorials

### Hobbies that cross-reference projects

Leathercraft → Wallet projects, camera/gear cases
Sewing → Costume projects, bag design, upholstery
Jewelry → Craft display, gift-making

---

## Decision Tree: When to Use This Protocol

```
Is it a hobby or craft-related item?
│
├─ YES - Does it have its own major collection?
│  └─ NO → Use HOBBY_COLLECTION_PROTOCOL
│
└─ NO → Check other protocols
   ├─ Photography? → CAMERA_COLLECTION_PROTOCOL
   ├─ Electronics project? → Programmable Devices, Device Lab, or Projects
   ├─ Major tool/equipment? → EQUIPMENT_DOCUMENTATION_PROTOCOL
   └─ Hand tool/consumable? → TOOLS_AND_COMPONENTS_PROTOCOL
```

---

## Examples

### Well-Documented Leathercraft Section

```markdown
## Leathercraft

Tools and materials for leather working projects including tooling, edge finishing, and hardware attachment.

| Item | Description | Qty | Condition | Status | Date | Notes |
|------|-------------|-----|-----------|--------|------|-------|
| Edge Beveler Set | V-tool bevelers 1-6mm (Tandy) | 1 | Good | Active | 2017-06-15 | Chrome steel, sharp |
| Stripper Tool | Single-line stripper 1/8" (Craftool) | 1 | Fair | Active | 2017-06-15 | Light wear |
| Thread Wax | Beeswax block for conditioning | 1 | Good | Active | 2017-06-15 | Full |
```

---

*Protocol Version: 1.0*
*Last Updated: 2026-01-17*
