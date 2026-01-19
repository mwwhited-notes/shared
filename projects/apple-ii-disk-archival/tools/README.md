# Apple II Archival Tools

This directory contains tools for Apple II disk archival and preservation.

## Included Tools (in this directory)

Both tools are included as **git submodules** for easy updating.

### 1. wozardry (Git Submodule)
**Source:** https://github.com/a2-4am/wozardry
**License:** MIT
**Purpose:** Multi-purpose tool for manipulating .woz disk images

**Features:**
- Verify WOZ file structure and metadata
- Print all information in a .woz disk image
- Edit metadata
- Import/export metadata as JSON
- Convert between WOZ 1.0 and 2.0 formats

**Usage:**
```bash
cd wozardry

# Verify a WOZ file
python3 wozardry.py verify ../archive/woz-images/PrintShop_Program.woz

# Print info about a WOZ file
python3 wozardry.py info ../archive/woz-images/PrintShop_Program.woz

# Edit metadata
python3 wozardry.py edit ../archive/woz-images/PrintShop_Program.woz \
    --title "The Print Shop v1.0" \
    --publisher "Broderbund"
```

**Requirements:** Python 3.6+

---

### 2. passport.py (Git Submodule)
**Source:** https://github.com/a2-4am/passport.py
**License:** MIT
**Purpose:** Verification and automated crack tool for Apple II .woz disk images

**Features:**
- Analyzes .woz disk images for copy protection
- Automatically removes protection when possible
- Creates unprotected .dsk images
- Supports 80+ protection schemes (Broderbund nibble count, EA, etc.)

**Usage:**
```bash
cd passport.py

# Analyze and crack a WOZ file
python3 passport.py ../archive/woz-images/PrintShop_Program.woz

# Output will be a .dsk file with protection removed (if successful)
```

**Success Rate:** ~70-80% for commercial Apple II software from 1980s

**Requirements:** Python 3.6+

---

## External Tools (Install Separately)

### 3. Greaseweazle Software
**Source:** https://github.com/keirf/greaseweazle
**License:** Public Domain
**Purpose:** Host tools for Greaseweazle hardware device

**Installation:**
```bash
# Install via pip (recommended)
pip install greaseweazle

# Or install from source
git clone https://github.com/keirf/greaseweazle.git
cd greaseweazle
python3 setup.py install
```

**Key Commands:**
```bash
# Check drive detection
gw info

# Update firmware
gw update

# Read Apple II 5.25" disk to flux image
gw read --drive A: --format apple2.140 \
    --retries 10 \
    disk_name.scp

# Read Apple II 3.5" disk
gw read --drive B: --format apple2.800 \
    disk_name_800k.scp

# Convert SCP to DSK (if unprotected)
gw convert --format apple2.dsk disk_name.scp disk_name.dsk
```

**Documentation:** https://github.com/keirf/greaseweazle/wiki

---

### 4. AppleCommander
**Source:** https://github.com/AppleCommander/AppleCommander
**License:** GPL-2.0
**Purpose:** Manipulate Apple II disk images (view, extract, add files)

**Download:**
- **Latest Release:** https://github.com/AppleCommander/AppleCommander/releases
- Download `AppleCommander-ac-VERSION.jar` for command-line use
- Download `AppleCommander-gui-VERSION.jar` for graphical interface

**Requirements:** Java 21+ (https://adoptium.net/)

**Command-Line Usage:**
```bash
# List files on a disk image
java -jar AppleCommander-ac.jar -l disk.dsk

# Extract a file
java -jar AppleCommander-ac.jar -e disk.dsk FILENAME

# Add a file
java -jar AppleCommander-ac.jar -p disk.dsk FILENAME TYPE

# Get disk info
java -jar AppleCommander-ac.jar -i disk.dsk
```

**GUI Usage:**
```bash
java -jar AppleCommander-gui.jar
```

**Documentation:** https://applecommander.github.io/

---

### 5. CiderPress (Windows Only)
**Source:** https://ciderpress.com/
**License:** BSD-3-Clause
**Purpose:** Windows GUI for Apple II disk image management

**Download:** https://ciderpress.com/downloads/

**Features:**
- Drag-and-drop file extraction
- Disk image conversion
- File viewers (graphics, documents)
- ShrinkIt archive support (.SDK, .BXY)

**Alternative for Linux/Mac:** Use AppleCommander GUI instead

---

## Recommended Workflow

### Setup (One Time)
1. Install Greaseweazle: `pip install greaseweazle`
2. Download AppleCommander JAR from GitHub releases
3. Install Python 3 (for wozardry and passport.py)

### Per-Disk Archival
1. **Flux Image** (Greaseweazle)
   ```bash
   gw read --drive A: --format apple2.140 \
       --retries 10 --settle-time 20ms \
       ../archive/flux-masters/PrintShop_Program.scp
   ```

2. **Convert to WOZ** (wozardry - currently manual, use conversion tool)
   ```bash
   # Note: Direct SCP to WOZ conversion requires additional tools
   # For now, use Applesauce or other converter
   # Then verify with wozardry:
   python3 wozardry/wozardry.py verify \
       ../archive/woz-images/PrintShop_Program.woz
   ```

3. **Remove Protection** (passport.py - optional)
   ```bash
   python3 passport.py/passport.py \
       ../archive/woz-images/PrintShop_Program.woz
   # Creates PrintShop_Program.dsk if successful
   ```

4. **Manage Files** (AppleCommander)
   ```bash
   java -jar AppleCommander-ac.jar -l \
       ../archive/dsk-images/PrintShop_Program.dsk
   ```

---

## SCP to WOZ Conversion

**Current Gap:** Neither wozardry nor passport.py directly converts .SCP to .WOZ

**Solutions:**

### Option A: HxC Floppy Emulator Software (Free)
- **Download:** https://hxc2001.com/download/floppy_drive_emulator/
- Can convert SCP to WOZ format
- Cross-platform (Windows, Linux, Mac)

### Option B: Applesauce Software (Commercial, $90-120)
- **Website:** https://applesaucefdc.com/
- Best SCP to WOZ conversion
- Includes flux imager hardware
- Worth it if you image disks frequently

### Option C: greaseweazle + Manual WOZ Creation
- Use Greaseweazle to convert SCP to IMG/DSK first
- Then use WOZ creation tools
- More complex workflow

**Recommendation:** Start with Greaseweazle → SCP preservation, then use HxC for free WOZ conversion

---

## Tool Summary

| Tool | Purpose | Type | Cost |
|------|---------|------|------|
| **Greaseweazle** | Flux imaging | Python CLI | Free |
| **wozardry** | WOZ manipulation | Python CLI | Free |
| **passport.py** | Protection removal | Python CLI | Free |
| **AppleCommander** | Disk management | Java GUI/CLI | Free |
| **CiderPress** | Disk management | Windows GUI | Free |
| **HxC Software** | Format conversion | GUI | Free |
| **Applesauce** | Everything + hardware | GUI + HW | $90-120 |

---

## Quick Reference Links

### Documentation
- [Greaseweazle Wiki](https://github.com/keirf/greaseweazle/wiki)
- [AppleCommander Docs](https://applecommander.github.io/)
- [WOZ Format Spec](https://applesaucefdc.com/woz/)
- [4am's Work](https://github.com/a2-4am)

### Downloads
- [Greaseweazle](https://github.com/keirf/greaseweazle/releases)
- [AppleCommander](https://github.com/AppleCommander/AppleCommander/releases)
- [HxC Software](https://hxc2001.com/download/floppy_drive_emulator/)
- [CiderPress](https://ciderpress.com/downloads/)

### Communities
- [AppleSqueezer Forum](https://www.applefritter.com/) - Disk preservation
- [/r/apple2](https://reddit.com/r/apple2) - Reddit community
- [comp.sys.apple2](https://groups.google.com/g/comp.sys.apple2) - Usenet

---

## Updating Tools (Git Submodules)

Both wozardry and passport.py are git submodules. Update them with:

### Update All Submodules
```bash
# From project root
cd /current/src/projects/apple-ii-disk-archival
git submodule update --remote

# Or update individually:
git submodule update --remote tools/wozardry
git submodule update --remote tools/passport.py
```

### Update One Tool Manually
```bash
# Update wozardry
cd tools/wozardry
git pull origin master

# Update passport.py
cd tools/passport.py
git pull origin master
```

### Greaseweazle
```bash
pip install --upgrade greaseweazle
```

### AppleCommander
Check https://github.com/AppleCommander/AppleCommander/releases for new versions

---

**Last Updated:** 2026-01-19
**Maintained By:** Matt Whited
