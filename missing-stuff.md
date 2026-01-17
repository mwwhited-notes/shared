# Missing Documentation & Broken References Report

**Generated:** 2026-01-17 (Updated after verification)
**Reason:** Repository audit after removal of personal information and separation into Personal/ folder
**Finding:** MAJOR DISCREPANCY - Files documented as moved don't actually exist

---

## CRITICAL DISCOVERY 🚨

### 1. "MOVED" FILES DON'T EXIST ANYWHERE ⚠️ CRITICAL

Files that were documented as successfully moved to Personal/ **do not exist in the repository**:

1. `tools-and-components.md` - ❌ NOT FOUND
2. `ShoppingOnline.md` - ❌ NOT FOUND
3. `Restaurants.md` - ❌ NOT FOUND
4. `books.md` - ❌ NOT FOUND

**Verification:**
```bash
$ find /current -name "tools-and-components.md"  # Returns nothing
$ find /current -name "ShoppingOnline.md"        # Returns nothing
$ find /current -name "Restaurants.md"            # Returns nothing
$ find /current -name "books.md"                  # Returns nothing
```

**Terminal Output vs Reality:**
- Earlier terminal showed: "✓ tools-and-components.md removed from root"
- Earlier showed files in Personal/ with sizes (49KB, 28KB, 835B)
- **Actual state:** All files completely absent from repository

### 2. EMPTY PERSONAL/ FOLDER ⚠️ CRITICAL

The `Personal/` folder exists but is **completely empty** - no subdirectories, no files, no .claude/protocols/:

**Current State:**
```
Personal/
├── (no files)
└── (no subdirectories)
```

**Expected to Contain (per CLAUDE.md documentation):**
- 8 equipment collections (Programmable Devices, Expansion Boards, Test Equipment, etc.)
- Configuration files (CLAUDE.md, TODO.md, README.md)
- 10 documentation protocols in `.claude/protocols/`
- 2017-2020 Amazon invoices and 2022-2026 AliExpress archives
- 4 moved files (tools-and-components.md, ShoppingOnline.md, Restaurants.md, books.md)

**Status:**
1. Equipment collections were NEVER in this repository OR were deleted
2. "Moved" files don't actually exist
3. Personal/ is a placeholder with no content

---

## What Actually Exists in This Repository

### Root Level Files ✓

| File | Purpose | Status |
|------|---------|--------|
| CLAUDE.md | Project configuration | ✓ EXISTS |
| TODO.md | Task tracking | ✓ EXISTS |
| readme.md | Main entry point | ✓ EXISTS |
| workshop-capabilities.md | Equipment reference | ✓ EXISTS |
| links.md | Reference links | ✓ EXISTS |
| network-diagram.md | Network topology | ✓ EXISTS |
| missing-stuff.md | This report | ✓ EXISTS |
| cross cloud reference.md | Cloud notes | ✓ EXISTS |

### Root Level Directories ✓

| Directory | Purpose | Status |
|-----------|---------|--------|
| projects/ | Active projects | ✓ EXISTS |
| Notes/ | Technical notes | ✓ EXISTS |
| AnalogComputers/ | Research collection | ✓ EXISTS |
| diagrams-and-patterns/ | Architecture patterns | ✓ EXISTS |
| Scripts/ | Utility scripts | ✓ EXISTS |
| Files/ | Static files | ✓ EXISTS |
| changes/ | Archived work | ✓ EXISTS |
| designs/ | Design docs | ✓ EXISTS |
| .claude/ | Protocols (9 files) | ✓ EXISTS |
| Personal/ | Equipment collections | ✗ EMPTY |

### Documentation vs Reality Mismatch

**CLAUDE.md describes equipment collections that don't exist:**
- Section 37-48 documents 8 collections in Personal/
- All references are to directories that don't exist anywhere in the repository
- 50+ lines of CLAUDE.md are dedicated to describing missing items

**Missing Reference Files:**
- `tools-and-components.md` - Referenced 3+ times, doesn't exist
- `ShoppingOnline.md` - Referenced 1+ times, doesn't exist
- `Restaurants.md` - Referenced 1+ times, doesn't exist
- `books.md` - Referenced 1+ times, doesn't exist

---

## Missing Directories (20 Total)

### Equipment Collections (Referenced but Not Found)

| Collection | Referenced In | Location Expected |
|-----------|---------------|-------------------|
| **Programmable Devices/** | CLAUDE.md:40,96,230,305 | Personal/Programmable Devices/ |
| **Expansion Boards/** | CLAUDE.md:41,231,306 | Personal/Expansion Boards/ |
| **Test Equipment/** | CLAUDE.md:42,232,307 | Personal/Test Equipment/ |
| **Vintage Computers/** | CLAUDE.md:43,233,308 | Personal/Vintage Computers/ |
| **Camera Collection/** | CLAUDE.md:44,234,309 | Personal/Camera Collection/ |
| **Device Lab/** | CLAUDE.md:45,235,310 (6 refs total) | Personal/Device Lab/ |
| **Hobby Collection/** | CLAUDE.md:46,236,311 | Personal/Hobby Collection/ |
| **Sports Collection/** | CLAUDE.md:47,237,312 | Personal/Sports Collection/ |

### Device Lab Subdirectories (10 Missing)

Referenced in `network-diagram.md` and `workshop-capabilities.md`:

1. `Device Lab/desktops/powerspec-g474/` - Referenced in workshop-capabilities.md:79
2. `Device Lab/desktops/reduced-bigrig/` - Referenced in workshop-capabilities.md:80
3. `Device Lab/desktops/server-fx8350/` - Referenced in workshop-capabilities.md:81
4. `Device Lab/laptops/microsoft-surface-book-2-15/` - Referenced in workshop-capabilities.md:82
5. `Device Lab/gaming/sony-psvita/` - Referenced in workshop-capabilities.md:106
6. `Device Lab/mobile/samsung-galaxy-tab4-nook/` - Referenced in workshop-capabilities.md:102
7. `Device Lab/mobile/amazon-fire-hd/` - Referenced in workshop-capabilities.md:103
8. `Device Lab/mobile/apple-ipad-mini/` - Referenced in workshop-capabilities.md:104
9. `Device Lab/mobile/apple-iphone-2g/` - Referenced in workshop-capabilities.md:105
10. `Device Lab/network-storage/wd-mycloud-pr4100/` - Referenced in TODO.md:44

### Other Missing Directories

| Directory | Referenced | Type |
|-----------|-----------|------|
| **HammingDistances/** | readme.md:151 | Project collection |
| **Semantic Search/** | readme.md:152 | Project collection |
| **Project subdirectories** | Multiple | Active projects |

---

## Missing Protocol Files (10 Total)

The following protocols are referenced in `CLAUDE.md` but do NOT exist in `.claude/protocols/`:

All 10 collection/shopping protocols were moved to `Personal/.claude/protocols/` but CLAUDE.md still references them as if they're in root:

1. `.claude/protocols/PROGRAMMABLE_DEVICES_DOCUMENTATION_PROTOCOL.md` (CLAUDE.md:79)
2. `.claude/protocols/EXPANSION_BOARDS_DOCUMENTATION_PROTOCOL.md` (CLAUDE.md:93)
3. `.claude/protocols/EQUIPMENT_DOCUMENTATION_PROTOCOL.md` (CLAUDE.md:99)
4. `.claude/protocols/VINTAGE_COMPUTERS_DOCUMENTATION_PROTOCOL.md` (CLAUDE.md:102)
5. `.claude/protocols/CAMERA_COLLECTION_PROTOCOL.md` (CLAUDE.md:116)
6. `.claude/protocols/DEVICE_LAB_PROTOCOL.md` (CLAUDE.md:125)
7. `.claude/protocols/HOBBY_COLLECTION_PROTOCOL.md` (CLAUDE.md:133)
8. `.claude/protocols/SPORTS_COLLECTION_PROTOCOL.md` (CLAUDE.md:140)
9. `.claude/protocols/ONLINE_SHOPPING_PROTOCOL.md` (CLAUDE.md:110)
10. `.claude/protocols/TOOLS_AND_COMPONENTS_PROTOCOL.md` (CLAUDE.md:180)

**Current Status:** These files exist in `Personal/.claude/protocols/` (9 remaining root protocols verified)

---

## Broken References & Hyperlinks

### Active References to Empty Personal/ Folder

| File | Line | Reference | Expected Target |
|------|------|-----------|-----------------|
| CLAUDE.md | 316 | `Personal/.invoices/` | Personal/.invoices/ (empty) |
| CLAUDE.md | 317 | `Personal/tools-and-components.md` | ❌ File moved to Personal (now empty) |
| CLAUDE.md | 318 | `Personal/ShoppingOnline.md` | ❌ File moved to Personal (now empty) |
| CLAUDE.md | 319 | `Personal/Restaurants.md` | ❌ File moved to Personal (now empty) |
| CLAUDE.md | 304-312 | All Personal collection references | ❌ Subdirectories missing |
| workshop-capabilities.md | 195 | `[Personal/tools-and-components.md](...)` | ❌ Hyperlink to empty Personal |

### Path Inconsistencies

| Issue | Location | Problem |
|-------|----------|---------|
| DiagramsAndPatterns naming | readme.md:98 | References "Notes/DiagramsAndPatterns/" but actual path is "diagrams-and-patterns/" at root level |
| README vs readme case | CLAUDE.md lines 305-310 | Mixes uppercase "README.md" and lowercase "readme.md" for same locations |
| Device Lab path in TODO | TODO.md:44 | References "Device Lab/network-storage/wd-mycloud-pr4100/" but should be "Personal/Device Lab/..." |

---

## Orphaned Documentation & References

### TODO Items Referencing Missing Items

| Line | Item | Reference | Status |
|------|------|-----------|--------|
| TODO.md:44 | Infrastructure task | "see Device Lab/network-storage/wd-mycloud-pr4100/windows-credential-fix.md" | ❌ Path incorrect, file in Personal/ if anywhere |

### Project Ideas Referencing Missing Collections

| File | Reference | Expected Location |
|------|-----------|-------------------|
| project-ideas.md | Multiple equipment-based ideas | Reference moved equipment collections in Personal/ |
| workshop-capabilities.md | All collection-based ideas | Reference empty Personal/ subdirectories |

### Cross-Reference Inconsistencies

**CLAUDE.md Documentation References:**
- Lines 304-312: States "All equipment collections have been moved to `Personal/` folder"
- Lines 60-73: Describes collections that should exist but are missing
- Lines 116-122: References Personal/ collection READMEs that don't exist

---

## Documentation Audit Results

### Files Correctly Pointing to Root-Level Content ✓

| File | Status |
|------|--------|
| projects/ | Present and documented |
| Notes/ | Present with README.md |
| Scripts/ | Present and referenced |
| AnalogComputers/ | Present with README.md |
| diagrams-and-patterns/ | Present (but naming inconsistency in readme.md) |
| links.md | Present and documented |
| network-diagram.md | Present (but references missing Device Lab paths) |

### Files with Missing Dependencies ❌

| File | Missing Reference | Type |
|------|-------------------|------|
| CLAUDE.md | 50+ lines describing Personal/ collections | Collections |
| TODO.md | Infrastructure task references | File paths |
| workshop-capabilities.md | Device Lab inventory summaries | Collections |
| readme.md | HammingDistances, Semantic Search | Directories |

---

## Naming & Case Sensitivity Issues

### Directory Naming Inconsistencies

1. **DiagramsAndPatterns (CamelCase vs lowercase-with-hyphens)**
   - CLAUDE.md:62 - "DiagramsAndPatterns/"
   - CLAUDE.md:63-66 - Describes content
   - readme.md:98 - "Notes/DiagramsAndPatterns/" ← INCORRECT PATH
   - **Actual location:** diagrams-and-patterns/ at root level

2. **README vs readme file naming**
   - CLAUDE.md:305 - `Personal/readme.md` (lowercase)
   - CLAUDE.md:308 - `Personal/Programmable Devices/readme.md` (lowercase)
   - CLAUDE.md:304 - `Personal/README.md` (uppercase) ← INCONSISTENT

### Case Sensitivity Across References

| Reference Type | Count | Consistency |
|---|---|---|
| Lowercase `readme.md` | 6 | Inconsistent |
| Uppercase `README.md` | 4 | Inconsistent |
| CamelCase collection names | 8 | Inconsistent |
| lowercase-with-hyphens | 1 | diagrams-and-patterns/ only |

---

## Summary Statistics

| Category | Count | Status |
|----------|-------|--------|
| Missing directory references | 20 | ❌ CRITICAL |
| Missing protocol files | 10 | ⚠️ In Personal/ but refs point to root |
| Empty folders in repository | 1 | ⚠️ Personal/ empty |
| Broken hyperlinks | 4+ | ❌ Point to empty Personal/ |
| Path inconsistencies | 3+ | ⚠️ DiagramsAndPatterns, case sensitivity |
| Orphaned TODO items | 1 | ⚠️ Needs path update |
| Case naming issues | 10+ | ⚠️ readme vs README |

---

## THE CORE PROBLEM

**CLAUDE.md contains ~60 lines describing a repository structure that doesn't exist.**

The file extensively documents:
- 8 equipment collections in Personal/
- 4 purchase/inventory files (tools-and-components.md, ShoppingOnline.md, Restaurants.md, books.md)
- 10 documentation protocols in Personal/.claude/protocols/
- Cross-references to all of these missing items

**None of these items actually exist in the repository.**

This creates a situation where:
1. New contributors read CLAUDE.md expecting to find these collections
2. References in todo items and project ideas point to non-existent equipment
3. Documentation is misleading about what this repository actually contains
4. Links are broken because they reference equipment that doesn't exist

---

## Action Items to Fix CLAUDE.md

### IMMEDIATE (Critical - Must Fix)

1. **Determine Personal/ Status**
   - Was Personal/ contents intentionally deleted?
   - Was Personal/ moved to separate repository?
   - Should Personal/ references be removed from CLAUDE.md?
   - **Action:** Either restore contents or update documentation

2. **Update TODO.md Orphaned References**
   - [ ] Line 44: Update "Device Lab/network-storage/..." path
   - [ ] Options: Change to Personal/ path OR remove if item no longer relevant

3. **Fix Broken Hyperlinks**
   - [ ] CLAUDE.md:317-319 - Remove or correct Personal/ file references
   - [ ] workshop-capabilities.md:195 - Fix hyperlink to Personal/tools-and-components.md

### HIGH PRIORITY (Consistency)

4. **Standardize Directory Naming & References**
   - [ ] Fix readme.md:98 - DiagramsAndPatterns path reference
   - [ ] Standardize README.md vs readme.md across CLAUDE.md
   - [ ] Choose consistent naming convention (CamelCase vs lowercase-with-hyphens)

5. **Clarify Protocol Locations**
   - [ ] Update CLAUDE.md sections 79-186 to clearly indicate:
     - Protocols are in `Personal/.claude/protocols/`
     - OR move them back to `.claude/protocols/` in root
     - OR remove references if not applicable to root

### MEDIUM PRIORITY (Documentation)

6. **Verify Missing Collections**
   - [ ] Confirm equipment collections are in Personal/ or deleted
   - [ ] Update workshop-capabilities.md if Device Lab is gone
   - [ ] Update project-ideas.md if collections referenced in projects are gone

7. **Check External References**
   - [ ] readme.md:151-152 - Verify HammingDistances/ and Semantic Search/ directories exist
   - [ ] If missing, remove from readme.md or create these directories

---

## Questions to Resolve

1. **Personal/ Folder Status:**
   - Is this an empty placeholder?
   - Should it be deleted from root repository?
   - Were contents moved to separate repository?

2. **Equipment Collections:**
   - Are all equipment collections actually in Personal/?
   - Should CLAUDE.md be updated to not reference them in root?

3. **Project Collections:**
   - Do HammingDistances/ and Semantic Search/ directories exist elsewhere?
   - Are they archived or should references be removed?

4. **Naming Conventions:**
   - Should all directories use lowercase-with-hyphens?
   - Should all README files be "readme.md" or "README.md"?

---

*Report generated during repository audit after personal information separation (2026-01-17)*
