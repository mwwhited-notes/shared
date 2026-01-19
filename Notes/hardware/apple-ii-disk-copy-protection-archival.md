# Apple II Disk Copy Protection and Archival Guide

## Overview

Guide for archiving copy-protected Apple II 5.25" and 3.5" floppy disks for personal preservation and backup. Covers common protection schemes, imaging tools, and techniques for creating working disk images from physical media you own.

**Legal Note:** This guide is for preserving software you legally own. Many Apple II programs are now abandonware or have been released as freeware by their creators. Always respect copyright and use this for personal archival purposes.

---

## Common Apple II Copy Protection Schemes

### 5.25" Disk Protection Methods

#### 1. **Nibble Count Protection**
- **How it works:** Non-standard nibble counts between sectors that can't be reproduced by standard DOS WRITE command
- **Used by:** Early Electronic Arts games, some Broderbund titles
- **Detection:** Disk reads specific tracks looking for exact nibble patterns
- **Weakness:** Flux-level imaging captures the exact timing

#### 2. **Half-Track Protection**
- **How it works:** Data written between standard tracks (e.g., track 1.5, 2.5) that normal drives can't write but can read
- **Used by:** Sierra On-Line games, Infocom titles
- **Detection:** Code seeks to half-tracks and reads data
- **Weakness:** Greaseweazle captures all track positions

#### 3. **Bit Timing / Sync Byte Variations**
- **How it works:** Non-standard sync bytes (not 0xD5 0xAA 0x96) or unusual bit timing
- **Used by:** Datasoft, Synergistic Software
- **Detection:** Custom RWTS (Read/Write Track Sector) routines
- **Weakness:** Flux imaging preserves exact timing

#### 4. **Address Field Modifications**
- **How it works:** Intentionally malformed address headers that DOS 3.3 ignores but copy programs fail on
- **Used by:** Beagle Bros, many educational titles
- **Detection:** Checks for specific address field errors
- **Weakness:** Bit-level imaging

#### 5. **Cross-Track Sync**
- **How it works:** Data spans multiple tracks, requiring precise head positioning
- **Used by:** Later Electronic Arts titles
- **Detection:** Reads must maintain exact track alignment
- **Weakness:** Flux imaging with accurate track positioning

#### 6. **Key Disk Protection**
- **How it works:** Separate "key disk" with unique signature must be present
- **Used by:** Professional software (VisiCalc, AppleWorks)
- **Detection:** Program checks for key disk in drive 2
- **Weakness:** Image the key disk separately

### 3.5" Disk Protection Methods

#### 1. **GCR (Group Code Recording) Modifications**
- **How it works:** Non-standard GCR encoding patterns
- **Used by:** Later Apple IIgs titles
- **Detection:** Custom disk drivers check encoding
- **Weakness:** Block-level imaging tools

#### 2. **Bad Block Lists**
- **How it works:** Intentionally marked bad blocks that protection checks for
- **Used by:** Some productivity software
- **Detection:** Expects specific blocks to fail
- **Weakness:** Image includes bad block markers

---

## Tools for Imaging Protected Disks

### 1. **Greaseweazle V4.1** (You Have This!)

**Best for:** Flux-level imaging that captures exact magnetic transitions

#### Advantages
- ✅ Captures all protection schemes (nibbles, half-tracks, timing)
- ✅ Works with any Apple II drive (Disk II, UniDisk 3.5)
- ✅ Creates .SCP (SuperCard Pro) or .IPF flux images
- ✅ Open source and actively maintained
- ✅ Works on modern PCs (USB connection)

#### Setup Requirements
- Greaseweazle V4.1 (you have this)
- 34-pin floppy cable
- Apple Disk II controller card OR DA-15 to 34-pin adapter for UniDisk 3.5
- Greaseweazle software (Python-based)

#### Workflow
```bash
# Install Greaseweazle tools
pip install greaseweazle

# Read 5.25" disk to flux image
gw read --drive A: --format apple2.140 disk_image.scp

# Read 3.5" disk
gw read --drive A: --format apple2.800 disk_image.scp

# Convert to standard DSK/WOZ format later
```

**Note:** Greaseweazle creates flux images that preserve ALL protection. You can then convert to .WOZ (Woz-A-Day format) which is the preservation standard.

---

### 2. **Applesauce**

**Best for:** Modern all-in-one imaging and conversion solution

#### Features
- 🍎 Hardware device + software package (commercial, ~$90-120)
- 🍎 Flux-level imaging like Greaseweazle
- 🍎 Built-in copy protection detection and reporting
- 🍎 Automatic conversion to .WOZ, .DSK, .NIB formats
- 🍎 GUI interface (easier than command line)
- 🍎 Metadata editing and disk cataloging

#### Advantages Over Greaseweazle
- Purpose-built for Apple II preservation
- Automatic protection analysis
- Better documentation for Apple II specific use
- Active community support (AppleSqueezer forum)

**Recommendation:** If you image Apple II disks frequently, Applesauce is worth the investment. Since you have Greaseweazle, start there and upgrade if needed.

---

### 3. **Copy II Plus (Historical Reference)**

**Classic tool:** Apple II native disk copying program

#### Versions
- **Copy II Plus v5.0** - Last version, supports most protections
- **Copy II Plus v9.1** - Final release, extensive bit copier

#### Features
- Runs on actual Apple II hardware
- Bit copy mode for nibble-level copying
- Parameter editor for custom RWTS
- Sector editor for manual fixes

#### Usage
```
1. Boot Copy II Plus disk
2. Select "Bit Copy" option
3. Copy from source drive to destination
4. May require multiple passes for complex protection
```

**Limitation:** Requires working Apple II with two drives, or repeated disk swaps

---

### 4. **ADTPro (Apple Disk Transfer ProDOS)**

**Best for:** Transferring working images between Apple II and modern PC

#### Features
- ✅ Serial or Ethernet connection to modern PC
- ✅ Transfers .DSK, .PO disk images
- ✅ Bootstrap mode (load via cassette or audio)
- ✅ Works with Apple II, IIe, IIc, IIgs

#### Limitation
- Only transfers sector-level images
- Won't preserve copy protection
- Best used AFTER you've removed protection or for unprotected disks

**Use Case:** Transfer your Greaseweazle-imaged and converted .DSK files to real Apple II hardware for verification

---

### 5. **EDD 4 (Enhanced Disk Drive 4)**

**Expert tool:** Sector editor and RWTS builder

#### Features
- Extremely powerful for analyzing protection
- Can create custom RWTS to read protected disks
- Sector-by-sector editing
- Runs on Apple II hardware

**Use Case:** When automated tools fail, EDD 4 lets you manually craft a solution

---

## Recommended Workflow for Your Collection

### Equipment You Have
- ✅ Greaseweazle V4.1
- ✅ Apple IIc (built-in Disk II compatible drive)
- ✅ Apple IIgs (can use both 5.25" and 3.5" drives)

### Phase 1: Flux-Level Archival (Preservation Master)

**Goal:** Create bit-perfect flux images of ALL disks

#### Setup
1. Connect Greaseweazle to 34-pin floppy cable
2. Connect cable to Apple Disk II drive (or IIc/IIgs internal drive via adapter)
3. Install Greaseweazle software on modern PC

#### Process
```bash
# For each 5.25" disk
gw read --drive A: --format apple2.140 --retries 5 \
    "disk_name.scp"

# For each 3.5" disk
gw read --drive A: --format apple2.800 --retries 5 \
    "disk_name_800k.scp"

# Optional: Convert to WOZ format (preservation standard)
# Use Applesauce Floppy Drive Controller software or
# wozardry tool: https://github.com/a2-4am/wozardry
```

**File Storage:**
- Save .SCP flux images as preservation masters
- Store on multiple drives (3-2-1 backup rule)
- Add metadata (disk label, publisher, year)

---

### Phase 2: Conversion to Usable Formats

**Goal:** Create .WOZ or .DSK images for emulators

#### Option A: WOZ Format (Recommended)
- Preserves copy protection for emulators
- Works in AppleWin, MAME, MicroM8
- Best for games that check for protection

#### Option B: DSK Format (Standard)
- Standard sector-based image
- Works in all emulators
- Only works if protection is removed

#### Tools for Conversion

**From .SCP to .WOZ:**
```bash
# Using a2_woz_creator (Python tool)
python a2_woz_creator.py disk_image.scp disk_image.woz
```

**From .SCP to .DSK (if unprotected):**
```bash
# Using Greaseweazle
gw convert --format apple2.dsk disk_image.scp disk_image.dsk
```

---

### Phase 3: Protection Removal (For Personal Use)

**When needed:** If you want to run on modern Apple II or emulators that don't support .WOZ

#### Method 1: Automated Tools

**4am's Crack Pipeline**
- GitHub: https://github.com/a2-4am/4am-crack-pipeline
- Automated scripts for common protections
- Requires .WOZ input
- Outputs cracked .DSK

```bash
# Example usage
./crack.sh disk_image.woz
# Creates disk_image.dsk with protection removed
```

**Success Rate:** 70-80% of commercial titles

---

#### Method 2: Manual RWTS Patching

**For experienced users who understand 6502 assembly**

1. **Identify Protection Check**
   - Disassemble boot code
   - Find RWTS (Read/Write Track Sector) routine
   - Locate protection verification

2. **Common Patterns**
   ```assembly
   ; Nibble count check
   LDX #$00
   :LOOP INX
   LDA $C08C,X  ; Read data latch
   BNE :LOOP
   CPX #$20     ; Expected count
   BNE FAIL     ; Protection fails

   ; Patch: NOP out the BNE, or change to BEQ
   ```

3. **Tools**
   - Merlin assembler
   - AppleCommander (Java tool for extracting files)
   - Hex editor for binary patching

**Resources:**
- Apple II Documentation Project: https://mirrors.apple2.org.za/
- Beneath Apple DOS book (explains RWTS)

---

#### Method 3: Key Disk Imaging

**For programs requiring key disk:**

1. Image the key disk separately (same flux process)
2. Mount both program and key disk in emulator
3. Or merge key disk data into program disk

**Example:** VisiCalc requires specific key disk signature

---

## Protection Removal Techniques by Type

### Nibble Count Protection
```
1. Find nibble count check in boot code
2. Patch to accept any count (NOP the branch)
3. Re-save with standard DOS WRITE
```

### Half-Track Protection
```
1. Read half-track data with flux imager
2. Move data to standard track location
3. Update boot code to read from new location
```

### Sync Byte Variations
```
1. Patch RWTS to accept standard sync bytes
2. Rewrite track with standard encoding
3. Test boot process
```

### Address Field Modifications
```
1. Rebuild track with correct address headers
2. Copy data sectors to new disk image
3. Write standard DOS 3.3 catalog
```

---

## Recommended Software Stack

### For Imaging
- **Greaseweazle** (you have the hardware) - Free
- **Applesauce** (optional upgrade) - $90-120

### For Conversion
- **wozardry** - .WOZ format tools (free)
- **AppleCommander** - Disk image manipulation (free)
- **CiderPress** - Windows disk image manager (free)

### For Emulation & Testing
- **AppleWin** - Windows emulator, excellent .WOZ support
- **MAME** - Multi-platform, accurate Apple II emulation
- **MicroM8** - Modern Apple IIgs emulator

### For Analysis
- **Copy II Plus** - Run on actual hardware or emulator
- **EDD 4** - Expert analysis tool
- **4am's tools** - Automated crack scripts

---

## Step-by-Step: First Disk Archival

### Equipment Setup

```
[PC with Greaseweazle software]
    |
    | USB
    |
[Greaseweazle V4.1]
    |
    | 34-pin floppy cable
    |
[Apple Disk II drive] (from IIc or standalone)
    |
[5.25" disk to archive]
```

### Process

1. **Physical Inspection**
   - Check disk for physical damage
   - Clean drive heads if needed
   - Label disk with sticky note (catalog later)

2. **Initial Read**
   ```bash
   gw read --drive A: --format apple2.140 \
       --retries 10 "game_name_v1.scp"
   ```

3. **Verify Read**
   ```bash
   # Check file size (should be ~600KB for .SCP)
   ls -lh game_name_v1.scp

   # Try conversion to DSK (may fail if protected)
   gw convert --format apple2.dsk \
       game_name_v1.scp test.dsk
   ```

4. **If Conversion Fails** (Protected Disk)
   - Expected! This means protection is preserved
   - Convert to .WOZ instead
   - Use in WOZ-compatible emulator

5. **If Conversion Succeeds** (Unprotected)
   - You now have a working .DSK image
   - Can use in any emulator or transfer to real hardware

6. **Metadata**
   - Create text file: `game_name.txt`
   - Document: title, publisher, year, disk label text
   - Note any issues during read

7. **Backup**
   - Copy to at least 2 additional locations
   - Cloud backup (Google Drive, etc.)
   - External hard drive

---

## Advanced: Half-Track Reading with Greaseweazle

For disks with half-track protection:

```bash
# Read with finer track stepping
gw read --drive A: --format apple2.140 \
    --tracks 0-39.5:step=0.5 \
    "disk_halftrack.scp"

# This captures tracks 0, 0.5, 1, 1.5, ... 39.5
```

The .SCP flux image will contain ALL half-track data.

---

## Troubleshooting

### "Disk Unreadable" Errors
- **Try multiple reads:** `--retries 10`
- **Clean drive heads:** Isopropyl alcohol on swab
- **Try different drive:** If available
- **Adjust drive speed:** Some Greaseweazle commands allow RPM adjustment

### "Conversion Failed" (Even Unprotected Disks)
- May have weak bits from age
- Try reading multiple times and comparing
- Use sector editor to manually reconstruct damaged sectors

### "Game Won't Boot After Removing Protection"
- Protection check may be integral to game code
- May need manual assembly patching
- Check 4am's crack database for existing patches

---

## Legal and Ethical Considerations

### Legal (in most jurisdictions)
- ✅ Archiving software you own for personal backup
- ✅ Preserving abandoned software (abandonware)
- ✅ Creating working copies for personal use
- ❌ Distributing cracked software
- ❌ Selling cracked images
- ❌ Circumventing for piracy

### Ethical Best Practices
- Only crack software you physically own
- Support active developers (buy modern releases)
- Share preservation knowledge, not pirated software
- Contribute to preservation projects (Internet Archive, 4am)

### Abandonware Resources
- **Asimov Archive** - Massive Apple II software collection
- **Internet Archive** - Software Preservation Society
- Many publishers have released titles as freeware

---

## Your Collection Archival Project

Based on your equipment and project ideas, here's a recommended approach:

### Phase 1: Inventory (Week 1)
- Catalog all 5.25" and 3.5" disks
- Note: title, condition, suspected protection
- Prioritize rare/personal disks

### Phase 2: Flux Imaging (Weeks 2-4)
- Image ALL disks with Greaseweazle
- Save .SCP files as masters
- Document any read errors

### Phase 3: Conversion & Testing (Week 5-6)
- Convert to .WOZ for protected disks
- Convert to .DSK for unprotected disks
- Test in AppleWin emulator

### Phase 4: Protection Removal (As Needed)
- Use 4am's tools for common titles
- Manual patching for rare software
- Keep original flux images as masters

### Phase 5: Organization (Week 7)
- Organize by category (games, productivity, education)
- Create README files with metadata
- Final backup to cloud + external drive

---

## Resources

### Documentation
- **Apple II Documentation Project** - https://mirrors.apple2.org.za/
- **Beneath Apple DOS** - Understanding DOS 3.3 internals
- **What's New (Call-A.P.P.L.E.)** - Copy protection analysis newsletter

### Communities
- **AppleSqueezer Forum** - Disk preservation community
- **comp.sys.apple2** - Usenet group (still active!)
- **/r/apple2** - Reddit community

### Tools
- **Greaseweazle** - https://github.com/keirf/greaseweazle
- **Applesauce** - https://applesaucefdc.com/
- **4am crack tools** - https://github.com/a2-4am/
- **wozardry** - https://github.com/a2-4am/wozardry
- **AppleCommander** - https://applecommander.github.io/
- **CiderPress** - https://ciderpress.com/

### Disk Image Archives (Reference)
- **Asimov** - https://ftp.apple.asimov.net/
- **Internet Archive** - https://archive.org/details/softwarelibrary_apple

---

## Next Steps for Your Project

1. **Test Greaseweazle Setup**
   - Connect to Disk II drive
   - Try reading a known-working disk
   - Verify .SCP file creation

2. **Create Archive Directory Structure**
   ```
   AppleII_Archive/
   ├── 5.25_Flux_Masters/    # .SCP preservation files
   ├── 5.25_WOZ/             # .WOZ converted images
   ├── 5.25_DSK/             # .DSK working images
   ├── 3.5_Flux_Masters/     # 3.5" flux images
   ├── 3.5_WOZ/              # 3.5" WOZ images
   ├── Metadata/             # Text files with disk info
   └── Documentation/        # This guide, notes, etc.
   ```

3. **Start with Non-Critical Disks**
   - Practice on duplicates or less valuable disks
   - Build confidence with tools
   - Develop workflow

4. **Document Your Process**
   - Keep notes in your project folder
   - Track successful conversion techniques
   - Share findings with preservation community

---

**Good luck with your archival project!** The combination of Greaseweazle + Apple IIc/IIgs gives you everything needed for comprehensive preservation.

---

*Created: 2026-01-19*
*For: Apple II disk archival project*
*Hardware: Greaseweazle V4.1, Apple IIc, Apple IIgs*
