# Sports Collection Documentation Protocol

Standard procedure for documenting sports equipment, outdoor gear, and recreational equipment.

---

## Overview

This protocol ensures consistent documentation of sports and outdoor recreation equipment. The goal is to maintain an organized inventory with:

- **Equipment inventory** - What you have, condition, functionality, and readiness
- **Specification tracking** - Sizes, weights, capacities, material composition
- **Maintenance status** - When last serviced/maintained, known issues, upgrades
- **Activity-based organization** - Grouped by sport/activity for easy planning
- **Project ideas** - Planned trips, upgrades, or projects using available equipment

---

## Directory Structure

```
Sports Collection/
├── readme.md                    # Collection index with all sports/activities
├── water-sports/
│   ├── paddling/                # Kayaks, paddleboards, canoes, etc.
│   ├── diving/
│   └── swimming/
├── biking/
│   ├── bikes/
│   ├── accessories/
│   └── parts/
├── fitness-exercise/
│   ├── strength/
│   └── recovery/
├── camping-hiking/
│   ├── shelter/
│   ├── sleeping/
│   ├── cooking/
│   └── accessories/
├── winter-sports/
│   ├── skiing-snowboarding/
│   └── winter-hiking/
└── reference-materials/
    └── [books, guides, instructional materials]
```

---

## Collection Index (readme.md) Format

The master readme should include:

1. **Quick Reference Summary** - Table with sport type, item count, and total investment
2. **Sport/Activity Sections** - Organized by activity type
3. **Status Legend** - Ready for use, maintenance needed, storage, parts
4. **Project Ideas** - Trips, upgrades, and adventures
5. **Maintenance Tracking** - When equipment was last serviced
6. **Cross-References** - Related project directories

### Quick Reference Format

```markdown
| Sport/Activity | Item Count | Status | Value | Key Example |
|----------------|-----------|--------|-------|------------|
| Water Sports | 4 | Ready | $1,200+ | Oru Bay kayak |
| Biking | 3 | Ready | $500+ | Brompton folding bike |
| Camping & Outdoor | 8 | Ready | $300+ | Backpacking gear |
| Fitness | 5 | Active | $150+ | Foam rollers |
```

### Detailed Sport Section Format

```markdown
## [Sport/Activity Name]

[Brief description of activity and equipment philosophy]

| Item | Description | Type/Size | Condition | Status | Date | Notes |
|------|-------------|-----------|-----------|--------|------|-------|
| [Name] | [Specs/details] | [Size/capacity] | [Good/Fair] | [Ready/Storage] | [YYYY-MM-DD] | [Details] |
```

---

## Equipment Categories by Sport

### Water Sports

| Equipment Type | Examples | Key Attributes |
|----------------|----------|-----------------|
| **Boats** | Kayaks, paddleboards, canoes | Capacity, material (plastic/composite/fabric), length, weight |
| **Paddles** | Kayak paddles, canoe paddles, oars | Length, material, weight, condition |
| **Safety** | PFDs, throw bags, rescue gear | Size, rating (Type I-V), condition |
| **Accessories** | Dry bags, bilge pumps, tie-downs, cart | Capacity, waterproof rating, condition |

### Biking

| Equipment Type | Examples | Key Attributes |
|----------------|----------|-----------------|
| **Bikes** | Road, mountain, gravel, folding | Frame size, weight, gears, components |
| **Accessories** | Lights, bells, mirrors, pumps | Type, power source, condition |
| **Parts** | Tires, chains, brake pads, cables | Size, type, compatibility, quantity |
| **Storage** | Bike boxes, racks, covers, stands | Size, capacity, protection level |

### Camping & Hiking

| Equipment Type | Examples | Key Attributes |
|----------------|----------|-----------------|
| **Shelter** | Tents, tarps, bivvies | Capacity, seasons (3-4 season), weight, condition |
| **Sleeping** | Sleeping bags, pads, pillows | Temperature rating, material, packability |
| **Cooking** | Stoves, fuel, cookware, utensils | Type, fuel compatibility, capacity |
| **Navigation** | Maps, compass, GPS, guide books | Coverage area, condition, battery status |
| **Clothing** | Hiking boots, layers, rain gear | Size, insulation, condition |

### Fitness & Exercise

| Equipment Type | Examples | Key Attributes |
|----------------|----------|-----------------|
| **Recovery** | Foam rollers, massage tools, stretching | Type, material, firmness/intensity |
| **Strength** | Weights, resistance bands, kettlebells | Weight/resistance, quantity, condition |
| **Cardio** | Jump ropes, rowing machine, treadmill | Type, adjustability, power (if electric) |

### Winter Sports

| Equipment Type | Examples | Key Attributes |
|----------------|----------|-----------------|
| **Skis/Board** | Skis, snowboard, bindings | Size, type (alpine/cross-country), condition |
| **Apparel** | Jacket, pants, gloves, boots | Size, insulation, waterproof rating |
| **Accessories** | Poles, goggles, helmet, backpack | Type, condition, compatibility |

---

## Status Tracking

Use consistent status labels:

| Status | Meaning |
|--------|---------|
| **Ready** | In working condition, ready for immediate use |
| **Storage** | Working but stored for off-season/inactive use |
| **Maintenance Needed** | Known issues requiring repair/tuning |
| **Parts** | Non-functional, useful for spares or reference |

---

## Condition Tracking

| Condition | Meaning |
|-----------|---------|
| **Excellent** | Like new, minimal use/wear |
| **Good** | Normal wear, fully functional |
| **Fair** | Cosmetic issues, minor wear, fully functional |
| **Poor** | Significant wear, still functional with caution |
| **Needs Repair** | Non-functional, repairable with effort |

---

## Maintenance Tracking

Track last service date and maintenance needs:

```markdown
### Maintenance Log

| Item | Last Service | Service Type | Next Due | Notes |
|------|--------------|--------------|----------|-------|
| [Equipment] | YYYY-MM-DD | Tune-up/repair | YYYY-MM-DD | [Details] |
```

---

## Project Ideas / Trip Planning Format

```markdown
## Planned Adventures & Upgrades

### Water Sports

#### Paddling Trips

- [ ] **Trip Name** - Location, duration
  - Equipment needed: [Which boats, paddles, safety gear]
  - Route difficulty: [Easy/Moderate/Advanced]
  - Estimated dates: [Season/timeframe]
  - Prep needed: [Maintenance, training, purchases]

#### Equipment Upgrades

- [ ] **Upgrade Name** - What and why
  - Equipment affected: [Which items]
  - Budget: $[amount]
  - Priority: [High/Medium/Low]

### Biking

- [ ] **Bike Ride/Tour** - Location, distance, duration
  - Bike: [Which bike]
  - Route: [Path/difficulty]
  - Companions: [Solo/group]
  - Special prep: [Repairs, new parts]

### Camping/Hiking

- [ ] **Trip Name** - Location, dates, difficulty
  - Duration: [Number of days]
  - Season: [Spring/Summer/Fall/Winter]
  - Participants: [Number of people]
  - Gear: [Tent capacity, sleeping bag temps, etc.]
  - Special requirements: [Permits, training, etc.]
```

---

## Cross-References

### Linking to Projects

If sports/outdoor activities connect to build projects:

```markdown
## Related Projects

- [Project Name](../../projects/project-name/) - How equipment is used
```

### Linking to Other Collections

Sports equipment might reference:
- Camera Collection → Action cameras, photography during activities
- Device Lab → Tablets for GPS/mapping, action cameras
- Tools & Components → Maintenance tools, repair supplies

---

## Data from Invoice Processing

When importing items from purchase invoices:

1. **Extract from invoice** - Identify sports/outdoor equipment items
2. **Categorize by sport** - Assign to appropriate section
3. **Add acquisition date** - Use original purchase date from invoice
4. **Add cost information** - Document original purchase price (useful for insurance/replacement value)
5. **Research specifications** - Determine exact model, size, capacity from description
6. **Set initial status** - Assume "Ready" for new equipment unless noted otherwise
7. **Identify consumables** - Note items that need replacement (fuel, batteries, etc.)

### Invoice Format Example

```markdown
| Item | Description | Type/Size | Purchased | Source | Cost | Notes |
|------|-------------|-----------|-----------|--------|------|-------|
| Oru Bay Kayak | Folding kayak, tan/brown | Single seat | 2017-10-15 | Amazon | $996.70 | Lightweight travel |
| Kayak Paddle | Aluminum shaft, plastic blade | Standard length | 2017-10-15 | Amazon | $45.00 | Standard paddle |
```

---

## Maintenance Tasks

### Seasonal Maintenance

| Season | Task | Description |
|--------|------|-------------|
| **Spring** | Water sports prep | Clean kayak/equipment, check PFD, inspect padding |
| **Summer** | Active use monitoring | Regular maintenance log, watch for issues |
| **Fall** | Preparation for winter | Winterize if needed, store seasonal equipment |
| **Winter** | Off-season review | Deep clean, repair, upgrade planning |

### Regular Tasks

| Task | Frequency | Notes |
|------|-----------|-------|
| Condition check | Monthly (active season) | Look for damage, wear, needed repairs |
| Maintenance log | After each use | Note condition, any issues, maintenance needed |
| Equipment inventory | Quarterly | Verify all equipment accounted for, condition status |
| Trip planning review | As-needed | Update planned adventures, prep needs |

---

## Decision Tree: When to Use This Protocol

```
Is it sports or outdoor recreation equipment?
│
├─ YES - Is it photography/action camera gear?
│  └─ YES → Consider CAMERA_COLLECTION_PROTOCOL instead
│
├─ YES - Does it connect to an active project?
│  └─ YES → Cross-reference PROJECTS_PROTOCOL
│
├─ YES - Is it a hand tool or consumable?
│  └─ YES → Cross-reference TOOLS_AND_COMPONENTS_PROTOCOL
│
└─ Use SPORTS_COLLECTION_PROTOCOL
```

---

## Examples

### Well-Documented Water Sports Section

```markdown
## Water Sports

Equipment for kayaking, paddling, and water-based recreation.

| Item | Description | Type/Size | Condition | Status | Date | Cost | Notes |
|------|-------------|-----------|-----------|--------|------|------|-------|
| Oru Bay Kayak | Folding kayak, tan/brown | Single seat | Good | Ready | 2017-10-15 | $996.70 | Lightweight, excellent for travel |
| Kayak Paddle | Aluminum shaft, plastic blade | Standard | Fair | Ready | 2017-10-15 | $45.00 | Good condition |
| PFD | Coast Guard Type III | Adult M | Excellent | Ready | 2017-10-20 | $89.99 | Bright orange |
| Dry Bag | 30L waterproof | Roll-top | Good | Ready | 2017-10-20 | $35.00 | Orange, clip closure |
```

---

## Supplier & Retailer Notes

When documenting purchases from invoices:

- **Amazon** - Check seller ratings, especially for water sports equipment
- **Specialty retailers** - REI, Backcountry, local bike shops
- **Direct from manufacturer** - Oru Kayak, specialized equipment makers
- **Used/vintage** - eBay, local classifieds, pawn shops (note condition carefully)

---

*Protocol Version: 1.0*
*Last Updated: 2026-01-17*
