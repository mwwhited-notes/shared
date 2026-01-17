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

## Common Request Scenarios

### Request: Equipment Referenced in Projects

**File:** `personal-request-equipment-by-project.md`

**Information Needed:**
- Which equipment exists in Personal collections
- Which projects reference which equipment
- Cross-reference between Personal collections and root projects

**Use Case:** Ensure project documentation accurately reflects available equipment

---

### Request: Component Inventory

**File:** `personal-request-components.md`

**Information Needed:**
- Passive components (resistors, capacitors, inductors)
- Active components (ICs, transistors, diodes)
- Stock levels and organization
- Tools available

**Use Case:** Project planning - verify what components are available before specifying parts

---

### Request: Test Equipment Specs

**File:** `personal-request-test-equipment.md`

**Information Needed:**
- Oscilloscope bandwidth and sample rate
- Multimeter resolution and input impedance
- Power supply voltage/current ratings
- Signal generator frequency range
- Programmers and supported targets

**Use Case:** Document equipment capabilities for troubleshooting guides and workshop-capabilities.md

---

### Request: Camera Collection

**File:** `personal-request-camera-equipment.md`

**Information Needed:**
- Camera bodies (model, sensor size, available features)
- Lenses (focal length, mount type, aperture)
- Accessories and adapters
- Cross-reference to photography projects

**Use Case:** Photo project planning and equipment documentation

---

### Request: Device Lab Inventory

**File:** `personal-request-device-lab.md`

**Information Needed:**
- Computing devices (tablets, phones, desktops, gaming devices)
- Hackability status (root, jailbreak, CFW available)
- Project ideas for each device
- Cross-reference to home-automation or other projects

**Use Case:** Device repurposing ideas and cross-referencing with root projects

---

## File Naming Convention

**Request files:** `personal-request-{topic}.md`
- Examples:
  - `personal-request-test-equipment.md`
  - `personal-request-components.md`
  - `personal-request-camera-equipment.md`
  - `personal-request-device-lab.md`
  - `personal-request-vintage-computers.md`
  - `personal-request-tools-inventory.md`

**Response files:** `.personal/incoming/{topic}.md`
- Examples:
  - `.personal/incoming/test-equipment.md`
  - `.personal/incoming/components.md`
  - `.personal/incoming/camera-equipment.md`
  - `.personal/incoming/device-lab.md`

---

## Implementation Notes

1. **Request files stay in root** - They document what data is needed and why
2. **Response files go to .personal/incoming/** - They're excluded from git but available locally
3. **Link from documentation** - Root files reference `.personal/incoming/` files when displaying Personal data
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
