# The Print Shop & The Toy Shop - Archival Guide

## Overview

Specific guide for archiving and preserving Broderbund's The Print Shop and The Toy Shop for Apple II.

**Programs:**
- **The Print Shop** (1984) - Banner/card/sign maker
- **The Toy Shop** (1986) - Create toys and animated scenes

**Publisher:** Broderbund Software
**Protection:** Nibble count + custom RWTS (Read/Write Track Sector)

---

## The Print Shop Details

### Versions and Disk Configurations

#### Original The Print Shop (1984)
- **Program Disk** - Main application (protected)
- **Graphics Library Disks** - Companion disks (usually unprotected)
  - Sampler Graphics
  - Holiday Graphics
  - School & Business Graphics
  - Party Graphics
  - etc.

#### The Print Shop Companion (1985)
- Additional graphics libraries
- Screen Magic animation module

#### The New Print Shop (1988)
- Updated version with more features
- Different protection scheme

### Known Protection Schemes

**Original Print Shop (1984-1987):**
1. **Nibble count protection** on tracks 0-2
2. **Custom RWTS** that checks for specific nibble patterns
3. **Modified address headers** on boot tracks
4. **Half-track data** on some versions (track 1.5)

**Protection Check:**
The program checks specific tracks during boot. If the expected nibble pattern isn't found, it displays an error or refuses to run.

---

## The Toy Shop Details

### Version Information

**The Toy Shop (1986)**
- Single program disk (protected)
- Create toys: dolls, puppets, robots, blocks
- Animate and print creations

### Known Protection

**Similar to Print Shop:**
1. **Nibble count** on boot tracks
2. **Custom RWTS** with protection checks
3. **Sync byte variations**

**Note:** Broderbund used similar protection across their product line (Print Shop, Toy Shop, Lode Runner, Karateka, etc.)

---

## Archival Strategy

### Step 1: Flux-Level Imaging (CRITICAL)

**Why flux imaging for these titles:**
- Nibble count protection can't be captured with sector copiers
- Standard ADTPro or disk utilities will create non-working images
- Greaseweazle preserves exact magnetic patterns

**Command:**
```bash
# For The Print Shop program disk
gw read --drive A: --format apple2.140 --retries 10 \
    "PrintShop_v1_ProgramDisk.scp"

# For each graphics library disk (may not be protected)
gw read --drive A: --format apple2.140 --retries 5 \
    "PrintShop_GraphicsLib_Sampler.scp"

# For The Toy Shop
gw read --drive A: --format apple2.140 --retries 10 \
    "ToyShop_v1.scp"
```

**Expected Results:**
- .SCP file around 600KB - 1.2MB
- This is your PRESERVATION MASTER - back it up immediately!

---

### Step 2: Convert to .WOZ Format

**Why .WOZ:**
- Modern emulators (AppleWin, MAME) support .WOZ
- Preserves protection for authentic experience
- Can run without cracking

**Tools:**
1. **Applesauce software** (if you buy the hardware)
2. **wozardry** - Command line tool
   - GitHub: https://github.com/a2-4am/wozardry

**Example conversion:**
```bash
# Using wozardry (Python tool)
python wozardry.py convert PrintShop_v1_ProgramDisk.scp \
    PrintShop_v1_ProgramDisk.woz

# Test in AppleWin emulator
applewin.exe --disk1=PrintShop_v1_ProgramDisk.woz
```

**Success Criteria:**
- Program boots in emulator
- No "DISK ERROR" or protection messages
- Can create banners/cards normally

---

### Step 3: Test Graphics Library Disks

**Important:** Graphics libraries were often unprotected!

**Test workflow:**
```bash
# Try converting to standard .DSK first
gw convert --format apple2.dsk \
    PrintShop_GraphicsLib_Sampler.scp \
    PrintShop_GraphicsLib_Sampler.dsk

# If successful, the library was unprotected
# If it fails, treat as protected and use .WOZ
```

**Why this matters:**
- Unprotected libraries are easier to work with
- Can transfer to real Apple II via ADTPro
- Can modify or create custom graphics

---

## Creating Usable Backup Copies

**If you want to run on real Apple II hardware or unprotected emulators:**

### Option A: Use Existing Cracks (Easiest)

**Check Asimov Archive:**
- https://ftp.apple.asimov.net/
- Search for "Print Shop" or "Toy Shop"
- Look for files marked [cr] (cracked) or [neatneat]

**Example:**
```
Print.Shop.v1.dsk              (original, won't work)
Print.Shop.v1.[cr].dsk         (cracked, should work)
```

**Verify it's your version:**
- Boot the cracked version
- Compare to your physical disk (title screen, version number)
- If it matches, you have a working backup

**Ethical note:** Since you own the original, using a pre-cracked version for personal backup is generally considered acceptable.

---

### Option B: Use 4am's Crack Tools (Semi-Automated)

**4am's Total Replay project** includes many Broderbund cracks.

**Process:**
1. Convert your .SCP to .WOZ (as above)
2. Use 4am's automated crack pipeline
   - GitHub: https://github.com/a2-4am/4am-crack-pipeline

```bash
# Clone the repository
git clone https://github.com/a2-4am/4am-crack-pipeline.git
cd 4am-crack-pipeline

# Run crack attempt
./crack.sh ../PrintShop_v1_ProgramDisk.woz

# If successful, creates:
#   PrintShop_v1_ProgramDisk.dsk (unprotected)
```

**Success rate:** 70-80% for Broderbund titles

---

### Option C: Manual Crack (Advanced)

**For learning purposes or if automated tools fail:**

#### Print Shop Protection Pattern

The protection is in the boot code (Track 0, Sector 0).

**Common patch locations:**
1. **Boot0 (Track 0, Sector 0)**
   - Contains initial loader
   - Calls protection check routine

2. **Protection Check (usually Track 1 or 2)**
   - Reads specific nibbles
   - Compares count
   - Branches to error if mismatch

**Basic patch strategy:**
```assembly
; Find this pattern in disassembly:
LDX #$00           ; Counter for nibbles
:LOOP
LDA $C08C,X        ; Read nibble from disk
INX
CPX #$20           ; Expected count (example)
BNE :LOOP

; After loop:
CPX #$20           ; Verify exact count
BNE ERROR          ; Branch if protection fails

; Patch options:
; 1. NOP the BNE ERROR instruction
; 2. Change BNE to BEQ (always succeed)
; 3. Force X to expected value before check
```

**Tools needed:**
- AppleWin emulator with debugger
- Merlin assembler or similar
- Copy of "Beneath Apple DOS" book (explains RWTS)

**Steps:**
1. Boot protected .WOZ in AppleWin debugger
2. Break at $0800 (boot code start)
3. Step through until protection check
4. Note address of BNE instruction
5. Patch to NOP (no operation) or BEQ
6. Export as unprotected .DSK

**Complexity:** Moderate to High (requires 6502 assembly knowledge)

---

## Recommended Workflow for Your Disks

### The Print Shop Collection

**Minimum archival (preservation):**
1. Flux image program disk → `PrintShop_Program.scp`
2. Flux image each graphics library → `PrintShop_Graphics_*.scp`
3. Convert all to .WOZ for emulator use
4. **Done** - You have working preservation copies

**Full archival (usable backups):**
1. Above steps 1-3
2. Find/use pre-cracked .DSK from Asimov
3. OR use 4am's tools to crack your .WOZ
4. Transfer cracked .DSK to real Apple II via ADTPro
5. **Done** - You can run on real hardware

---

### The Toy Shop

**Same workflow as Print Shop:**
1. Flux image → `ToyShop.scp`
2. Convert to .WOZ
3. Optional: Find/create unprotected .DSK

---

## Specific Greaseweazle Commands

### For Your Hardware Setup

**Equipment:**
- Greaseweazle V4.1
- Apple IIc internal drive (Disk II compatible)
- 5.25" disks: The Print Shop, The Toy Shop

**Connection:**
```
[PC] --USB--> [Greaseweazle] --34-pin--> [Apple IIc drive]
```

**Reading Print Shop program disk:**
```bash
# Clean drive heads first!
# Use isopropyl alcohol on cotton swab

# Read with multiple retries
gw read --drive A: --format apple2.140 \
    --retries 10 \
    --rate 300 \
    "PrintShop_v1_Program.scp"

# Check file was created
ls -lh PrintShop_v1_Program.scp
# Should be ~600KB to 1.2MB

# Immediate backup
cp PrintShop_v1_Program.scp PrintShop_v1_Program_BACKUP.scp
```

**Reading graphics library disks:**
```bash
# May not be protected, try lower retry count
gw read --drive A: --format apple2.140 \
    --retries 5 \
    "PrintShop_GraphicsLib_Sampler.scp"

# Try converting to DSK (test if protected)
gw convert --format apple2.dsk \
    PrintShop_GraphicsLib_Sampler.scp \
    test.dsk

# If convert succeeds: Unprotected!
# If convert fails: Protected, use .WOZ
```

---

## Troubleshooting

### "Read Error on Track X"

**Possible causes:**
- Dirty drive heads
- Weak magnetic signal from old disk
- Drive speed mismatch

**Solutions:**
```bash
# Try slower speed
gw read --drive A: --format apple2.140 \
    --retries 20 \
    --rate 250 \
    "PrintShop_v1_Program.scp"

# Or adjust for slight speed variation
--rate 290  # Slightly slower
--rate 310  # Slightly faster
```

### "Disk Boots But Protection Fails"

**This shouldn't happen with flux imaging**, but if it does:

**Check:**
1. .SCP file size (should be 600KB+)
2. Drive was set to correct type (apple2.140 for 5.25")
3. Conversion to .WOZ used correct tool

**Solution:**
- Re-read disk with higher retry count
- Try different drive if available
- Check Greaseweazle firmware is updated

### "Graphics Libraries Won't Load"

**In the original program:**
- Graphics libraries must be in correct drive
- Broderbund used specific file naming

**In emulator:**
1. Boot program disk in Drive 1
2. Mount graphics library in Drive 2
3. Or copy library files to program disk (if space available)

---

## Testing Your Archives

### In AppleWin Emulator

**Setup:**
1. Download AppleWin: https://github.com/AppleWin/AppleWin
2. Install on Windows PC

**Test Print Shop:**
```batch
REM Start AppleWin with your .WOZ image
AppleWin.exe --disk1=PrintShop_v1_Program.woz

REM Or with cracked .DSK
AppleWin.exe --disk1=PrintShop_v1_Program.dsk
```

**Verification steps:**
1. Program boots to title screen
2. Can access all menus
3. Graphics library loads when inserted
4. Can design and "print" (to file) a banner

**Success:** If all steps work, your archive is good!

---

### On Real Apple II Hardware

**If you created unprotected .DSK:**

**Using ADTPro:**
1. Boot ADTPro on Apple II (via serial/cassette/audio)
2. Connect to PC via serial cable
3. Send .DSK from PC to Apple II disk
4. Test bootability

**Direct write with Greaseweazle:**
```bash
# Write .DSK to physical disk
gw write --drive A: --format apple2.dsk \
    PrintShop_v1_Program_CRACKED.dsk

# Insert blank disk, then run command
```

**Caution:** Writing with Greaseweazle requires WRITE-ENABLED disk and can fail on modern drives.

---

## Additional Resources

### Print Shop Specific

**Documentation:**
- The Print Shop manual (PDF available on archive.org)
- Graphics library catalogs

**Community:**
- **a2central.com** - Apple II news and forums
- **/r/apple2** - Reddit community
- **AppleSqueezer forum** - Disk preservation experts

### Copy Protection Analysis

**References:**
- **Copy II Plus manual** - Explains Broderbund protection
- **"Beneath Apple DOS"** - RWTS internals
- **Call-A.P.P.L.E. "What's New"** - Protection documentation from 1980s

**Online:**
- **4am's work** - https://github.com/a2-4am (extensive crack documentation)
- **Asimov Apple II site** - https://ftp.apple.asimov.net/

---

## Your Archive Structure

**Recommended directory organization:**

```
AppleII_Archive/
├── PrintShop/
│   ├── Flux_Masters/
│   │   ├── PrintShop_v1_Program.scp
│   │   ├── PrintShop_GraphicsLib_Sampler.scp
│   │   ├── PrintShop_GraphicsLib_Holiday.scp
│   │   └── ...
│   ├── WOZ/
│   │   ├── PrintShop_v1_Program.woz
│   │   └── ...
│   ├── DSK_Cracked/
│   │   ├── PrintShop_v1_Program.dsk
│   │   └── ...
│   ├── Metadata/
│   │   ├── disk_labels.txt
│   │   └── version_info.txt
│   └── Documentation/
│       ├── PrintShop_Manual.pdf
│       └── this_guide.md
│
└── ToyShop/
    ├── Flux_Masters/
    │   └── ToyShop_v1.scp
    ├── WOZ/
    │   └── ToyShop_v1.woz
    └── ...
```

---

## Quick Start Checklist

**For The Print Shop & The Toy Shop:**

- [ ] Clean Apple IIc drive heads
- [ ] Connect Greaseweazle to drive
- [ ] Install Greaseweazle software on PC
- [ ] Read Print Shop program disk to .SCP
- [ ] Read Print Shop graphics libraries to .SCP
- [ ] Read Toy Shop disk to .SCP
- [ ] Backup all .SCP files (3-2-1 rule)
- [ ] Convert to .WOZ for emulator use
- [ ] Test in AppleWin
- [ ] (Optional) Find/create .DSK for real hardware
- [ ] Document disk labels and versions
- [ ] Celebrate successful preservation! 🎉

---

## Next Steps

1. **Start with Print Shop program disk**
   - Most critical disk
   - Test the process
   - Verify .SCP is good quality

2. **Move to graphics libraries**
   - Likely easier (unprotected)
   - Practice workflow

3. **Archive Toy Shop**
   - Apply lessons learned
   - Should go smoothly

4. **Share findings**
   - Document any issues
   - Help preservation community
   - Consider donating .WOZ to Internet Archive

---

**Good luck with your Print Shop and Toy Shop archival!** These are classic programs worth preserving. Your Greaseweazle + Apple IIc setup is perfect for this task.

---

*Created: 2026-01-19*
*Programs: The Print Shop (Broderbund, 1984), The Toy Shop (Broderbund, 1986)*
*Protection: Nibble count + custom RWTS*
*Hardware: Greaseweazle V4.1, Apple IIc*
