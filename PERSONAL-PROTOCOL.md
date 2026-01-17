# PERSONAL-PROTOCOL.md

This protocol documents the workflow for requesting information from the Personal repository when documentation or data from Personal collections (equipment, tools, invoices, etc.) is needed in the root repository.

---

## Overview

The Personal repository contains:
- Equipment collections (Programmable Devices, Test Equipment, Camera Collection, Device Lab, etc.)
- Purchase history and invoices (.invoices/ with Amazon and AliExpress orders)
- Tool and component inventory (tools-and-components.md)
- Seller notes (ShoppingOnline.md)
- Book collection (books.md)

When root repository documentation or projects need information from these Personal collections, use this protocol.

---

## Workflow

### Step 1: Create a Personal Request File

Create a new file named `personal-request-{topic}.md` in `.personal/requests/` folder with:

1. **Clear description** of what information is needed
2. **Specific prompt/protocol** for extracting that information from Personal
3. **Use case** explaining why the root repository needs this data

**Example filename:** `.personal/requests/personal-request-test-equipment.md`

**Example content:**
```markdown
# Personal Request: Test Equipment Inventory

## What We Need
A summary of test equipment available in Personal/Test Equipment collection.

## Use Case
Projects in the root repository reference specific test equipment (oscilloscopes, multimeters, power supplies). We need a quick reference list to link projects to available equipment.

## To Send This Request
File location: `.personal/requests/personal-request-test-equipment.md`
This file is tracked in git and can be sent to the Personal repository owner.

## Information to Extract From Personal/Test Equipment/

- Equipment name and model
- Key specifications (frequency range, resolution, etc.)
- Current status (Active/Shelved/Project/Parts)
- Location in collection structure
- Any relevant notes

## Protocol
See Personal/CLAUDE.md sections on:
- EQUIPMENT_DOCUMENTATION_PROTOCOL.md
- Test Equipment/readme.md for current inventory

## Format Requested
Markdown table with columns:
- Equipment Name
- Model
- Key Specs
- Status
- Location
```

### Step 2: Provide Response File

When information is ready from Personal repository:

1. **Place response file** in `./.personal/incoming/{topic}.md`
2. **Use the same filename structure** as the request for easy tracking

**Example:** If request was `personal-request-test-equipment.md`, response goes to `.personal/incoming/test-equipment.md`

### Step 3: Link Response Back

In root repository documentation where the information is needed, reference the incoming file:

```markdown
See [`.personal/incoming/test-equipment.md`](.personal/incoming/test-equipment.md) for current test equipment inventory from Personal repository.
```

### Step 4: .gitignore Handling

The `.personal/incoming/` folder is in `.gitignore` because:
- Content is temporary and local to your workflow
- Responses are specific to your working session
- Files may be regenerated when Personal repository is updated
- Keeps root repository clean of frequently-changing Personal data

---

## Active Request Files

The following 8 request files are maintained in `.personal/requests/` and ready to send to the Personal repository owner:

### 1. Programmable Devices
**File:** `.personal/requests/personal-request-programmable-devices.md`

- **Data:** FPGA boards, microcontroller boards, Arduino variants, SoC boards, CPLD/GAL boards, retro boards
- **Use Case:** Device inventory, project compatibility, toolchain documentation, programmer compatibility

### 2. Expansion Boards
**File:** `.personal/requests/personal-request-expansion-boards.md`

- **Data:** Arduino shields, Raspberry Pi HATs, BeagleBone capes, breakout boards
- **Use Case:** Pin mapping, compatibility tracking, project requirements

### 3. Test Equipment
**File:** `.personal/requests/personal-request-test-equipment.md`

- **Data:** Oscilloscopes, multimeters, LCR meters, logic analyzers, power supplies, thermal equipment, microscopes, signal generators, programmers
- **Use Case:** Equipment summary for workshop-capabilities.md, project planning, troubleshooting guides

### 4. Tools & Components
**File:** `.personal/requests/personal-request-tools-and-components.md`

- **Data:** Hand tools, soldering equipment, ESD safety, consumables, passive/active components, prototyping materials, wire/cable stock
- **Use Case:** Component stock verification, project planning, workshop capabilities

### 5. Books & Technical References
**File:** `.personal/requests/personal-request-books.md`

- **Data:** Technical book collection organized by category (software, hardware, security, etc.)
- **Use Case:** Cross-reference with design patterns, learning resources for projects

### 6. Device Lab
**File:** `.personal/requests/personal-request-device-lab.md`

- **Data:** Computing devices (workstations, servers, mobile, network storage), hackability status, project potential
- **Use Case:** Device repurposing projects, home automation integration, cross-references with active projects

### 7. Vintage Computers
**File:** `.personal/requests/personal-request-vintage-computers.md`

- **Data:** Vintage computer systems, peripherals, disk collections, display equipment, storage devices, emulation support tools
- **Use Case:** Preservation planning, archival projects, emulation soft-cores, restoration projects

### 8. Camera Collection
**File:** `.personal/requests/personal-request-camera-collection.md`

- **Data:** Camera bodies (digital/film), lenses by mount type, accessories, teleconverters, flashes, tripods, cases, filters
- **Use Case:** Photography project planning, lens compatibility, vintage glass documentation

---

## File Naming Convention

**Request files:** `personal-request-{topic}.md` in `.personal/requests/`
- Current files:
  - `personal-request-programmable-devices.md`
  - `personal-request-expansion-boards.md`
  - `personal-request-test-equipment.md`
  - `personal-request-tools-and-components.md`
  - `personal-request-books.md`
  - `personal-request-device-lab.md`
  - `personal-request-vintage-computers.md`
  - `personal-request-camera-collection.md`

**Response files:** `.personal/incoming/{topic}.md`
- Expected responses:
  - `.personal/incoming/programmable-devices.md`
  - `.personal/incoming/expansion-boards.md`
  - `.personal/incoming/test-equipment.md`
  - `.personal/incoming/tools-and-components.md`
  - `.personal/incoming/books.md`
  - `.personal/incoming/device-lab.md`
  - `.personal/incoming/vintage-computers.md`
  - `.personal/incoming/camera-collection.md`

---

## Implementation Notes

1. **Request files in `.personal/requests/`** - They document what data is needed and why, tracked in git for sending to Personal owner
2. **Response files go to `.personal/incoming/`** - They're excluded from git but available locally for referencing
3. **Link from documentation** - Root files (projects, workshop-capabilities.md, etc.) reference `.personal/incoming/` files when displaying Personal data
4. **Update frequency** - Regenerate response files when Personal repository is updated
5. **Minimal processing** - Responses should be direct exports from Personal with minimal transformation

---

## Example Workflow

```
1. Root project needs to reference available oscilloscopes
   ↓
2. Create personal-request-test-equipment.md with specific needs
   ↓
3. You provide test-equipment.md in .personal/incoming/
   ↓
4. Root project/doc references .personal/incoming/test-equipment.md
   ↓
5. Documentation stays current with Personal data
```

---

## Questions?

This protocol enables the root repository to reference Personal data without maintaining duplicate copies or hard-coding equipment lists.

Update this protocol if new request patterns emerge or if the workflow needs adjustment.
