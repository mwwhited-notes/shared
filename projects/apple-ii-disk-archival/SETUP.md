# Apple II Disk Archival - Setup Guide

Quick setup guide to get started with archiving your Apple II disk collection.

## Prerequisites

- **Python 3.6+** - For Greaseweazle, wozardry, passport.py
- **Java 21+** - For AppleCommander (optional)
- **Greaseweazle V4.1** - Hardware device (you have this!)
- **Epson SD-800** - Dual 5.25"/3.5" drive (you have this!)
- **5V Power Supply** - For SD-800 (PC power supply or adapter)

---

## Step 1: Install Greaseweazle Software

### Option A: Install via pip (Recommended)
```bash
pip install greaseweazle
```

### Option B: Install from source
```bash
pip install --upgrade git+https://github.com/keirf/greaseweazle.git
```

### Verify Installation
```bash
gw --version
gw info
```

**Expected Output:**
```
Greaseweazle V4.1
Drive A: 5.25" 40-track
Drive B: 3.5" 80-track
```

---

## Step 2: Update Greaseweazle Firmware

```bash
# Update to latest firmware (recommended)
gw update

# Or specify firmware file
gw update --file=Greaseweazle-V4.1-F7.upd
```

**Note:** Firmware files available at https://github.com/keirf/greaseweazle-firmware/releases

---

## Step 3: Initialize Git Submodules

Both wozardry and passport.py are included as git submodules.

```bash
# From project root
cd /current/src/projects/apple-ii-disk-archival

# Initialize and fetch submodules
git submodule update --init --recursive
```

### Test Python Tools

### Test wozardry
```bash
cd tools/wozardry
python3 wozardry.py --help
```

### Test passport.py
```bash
cd tools/passport.py
python3 passport.py --help
```

**If you get errors:** Ensure Python 3.6+ is installed:
```bash
python3 --version
# Should show Python 3.6 or higher
```

---

## Step 4: Download AppleCommander (Optional)

### Download Latest Release
1. Visit: https://github.com/AppleCommander/AppleCommander/releases
2. Download **AppleCommander-ac-VERSION.jar** (command-line)
3. Download **AppleCommander-gui-VERSION.jar** (graphical interface)
4. Save to `tools/` directory

### Test AppleCommander
```bash
cd tools
java -jar AppleCommander-ac-*.jar --help
```

**If Java not installed:**
- Download from https://adoptium.net/
- Install OpenJDK 21 or later

---

## Step 5: Hardware Setup

### Connect Greaseweazle to SD-800

```
[PC] --USB--> [Greaseweazle V4.1] --34-pin--> [Epson SD-800]
                                                  ├─ 5.25" (Drive A:)
                                                  └─ 3.5" (Drive B:)
```

### Power the SD-800

**Option A: PC Power Supply**
1. Connect Molex power connector to SD-800
2. Short green wire (PS_ON) to black (GND) on ATX connector
3. Power supply should turn on

**Option B: 5V Adapter**
- Use 5V 2A power adapter with Molex connector
- Connect to SD-800 power jack

**Pin 4 (Yellow) = +5V**
**Pin 3 (Black) = GND**
**Pin 1 (Yellow) = +12V (not used for 5.25" drives)**

### Verify Detection
```bash
gw info
```

**Expected:**
```
Greaseweazle V4.1
Drive A: 5.25" 40-track (ready)
Drive B: 3.5" 80-track (ready)
```

---

## Step 6: Create Archive Directory Structure

```bash
cd /current/src/projects/apple-ii-disk-archival

mkdir -p archive/flux-masters
mkdir -p archive/woz-images
mkdir -p archive/dsk-images
mkdir -p archive/metadata
```

**Directory Purpose:**
- `flux-masters/` - .SCP preservation files (permanent archive)
- `woz-images/` - .WOZ converted images (for emulators)
- `dsk-images/` - .DSK unprotected backups (for real hardware)
- `metadata/` - Text files with disk info

---

## Step 7: Clean Drive Heads

**Before reading any disks:**

1. Power off SD-800
2. Remove drive cover (4 screws usually)
3. Locate read/write heads (metal pieces)
4. Dip cotton swab in 90%+ isopropyl alcohol
5. Gently wipe head surfaces
6. Let dry 30 seconds
7. Reassemble

**When to clean:**
- Before first use
- After every 10-20 disks
- If read errors increase
- If brown residue appears on disks

---

## Step 8: Test Read (Sacrificial Disk)

**Use a duplicate or non-critical disk first!**

```bash
cd archive/flux-masters

# Read a test disk (5.25")
gw read --drive A: --format apple2.140 \
    --retries 10 \
    --settle-time 20ms \
    TEST_DISK.scp

# Check file was created
ls -lh TEST_DISK.scp
# Should be 600KB to 1.2MB
```

**Success Indicators:**
- No error messages
- .SCP file created
- File size reasonable (600KB+)
- No grinding/unusual noises

**Troubleshooting:**
- If "Track 0 not found" → Check drive select jumpers
- If "Speed error" → Try `--rpm-range 295-305`
- If "Read timeout" → Check cable connections
- If "Weak signal" → Clean heads again

---

## Step 9: Read Your First Priority Disk

### The Print Shop Program Disk

```bash
cd archive/flux-masters

# Read with optimal settings for Epson SD-800
gw read --drive A: --format apple2.140 \
    --tracks 0-34 \
    --step-rate 6ms \
    --settle-time 20ms \
    --retries 10 \
    PrintShop_v1_Program.scp

# Backup immediately!
cp PrintShop_v1_Program.scp PrintShop_v1_Program_BACKUP.scp
```

**Record metadata:**
```bash
cd ../metadata
cat > PrintShop_v1_Program.txt << EOF
Title: The Print Shop v1.0
Publisher: Broderbund Software
Year: 1984
Disk Type: 5.25" (140KB)
Protection: Nibble count + custom RWTS
Read Date: $(date +%Y-%m-%d)
Read Quality: Good/Fair/Poor
Notes: Original program disk, good condition
EOF
```

---

## Step 10: Convert to WOZ (For Emulators)

**Note:** Direct SCP to WOZ conversion requires additional software.

### Option A: HxC Floppy Emulator Software (Free)
1. Download from https://hxc2001.com/download/floppy_drive_emulator/
2. Install and run HxCFloppyEmulator
3. Load .SCP file
4. Export as .WOZ format
5. Save to `archive/woz-images/`

### Option B: Applesauce (Commercial - if you buy it)
1. Load .SCP in Applesauce software
2. Export as .WOZ
3. Automatic protection analysis included

### Verify WOZ File
```bash
cd archive/woz-images
python3 ../../tools/wozardry/wozardry.py verify PrintShop_v1_Program.woz
python3 ../../tools/wozardry/wozardry.py info PrintShop_v1_Program.woz
```

---

## Step 11: Test in Emulator

### Using AppleWin (Windows)
1. Download AppleWin from https://github.com/AppleWin/AppleWin/releases
2. Run AppleWin
3. Load .WOZ file as Disk 1
4. Boot and verify program runs

### Using MAME (Cross-platform)
```bash
mame apple2e -flop1 archive/woz-images/PrintShop_v1_Program.woz
```

---

## Step 12: Remove Protection (Optional)

**Only if you want unprotected .DSK for real hardware:**

```bash
cd archive/woz-images
python3 ../../tools/passport.py/passport.py PrintShop_v1_Program.woz

# If successful, creates PrintShop_v1_Program.dsk
mv PrintShop_v1_Program.dsk ../dsk-images/
```

**Success rate:** ~70-80% for Broderbund titles

**If passport.py fails:**
- Check 4am's existing cracks at https://github.com/a2-4am
- Manual patching required (advanced)
- Or just use .WOZ in emulator

---

## Quick Command Reference

### Read 5.25" Disk
```bash
gw read --drive A: --format apple2.140 \
    --retries 10 --settle-time 20ms \
    DISK_NAME.scp
```

### Read 3.5" Disk
```bash
gw read --drive B: --format apple2.800 \
    --retries 10 --settle-time 20ms \
    DISK_NAME_800k.scp
```

### Verify WOZ
```bash
python3 tools/wozardry/wozardry.py verify DISK.woz
```

### Remove Protection
```bash
python3 tools/passport.py/passport.py DISK.woz
```

### List Files on DSK
```bash
java -jar tools/AppleCommander-ac.jar -l DISK.dsk
```

---

## Troubleshooting

### "gw: command not found"
```bash
# Greaseweazle not installed
pip install greaseweazle
```

### "No drives detected"
```bash
# Check USB connection
lsusb | grep -i greaseweazle

# Check power to SD-800
# Verify 34-pin cable connection
```

### "Python module not found"
```bash
# Ensure Python 3.6+
python3 --version

# Install pip if needed
sudo apt install python3-pip  # Ubuntu/Debian
brew install python3          # macOS
```

### "Read errors on multiple tracks"
1. Clean drive heads
2. Increase retries: `--retries 20`
3. Adjust settle time: `--settle-time 30ms`
4. Try different disk (test drive vs disk)

---

## Next Steps

1. ✅ Read The Print Shop program disk
2. ✅ Read The Print Shop graphics libraries
3. ✅ Read The Toy Shop disk
4. Archive rest of collection
5. Test images in emulators
6. Create catalog of collection

---

## Resources

### Official Documentation
- [Greaseweazle Wiki](https://github.com/keirf/greaseweazle/wiki)
- [Hardware Setup Guide](hardware-setup.md)
- [Tools Documentation](tools/README.md)

### Technical Guides
- [Notes/hardware/apple-ii-disk-copy-protection-archival.md](../../Notes/hardware/apple-ii-disk-copy-protection-archival.md)
- [Notes/hardware/apple-ii-printshop-toyshop-guide.md](../../Notes/hardware/apple-ii-printshop-toyshop-guide.md)

### Support
- **AppleSqueezer Forum** - Disk preservation experts
- **/r/apple2** - Reddit community
- **comp.sys.apple2** - Usenet (via Google Groups)

---

**Setup Complete!** You're ready to start archiving your Apple II disk collection.

---

*Last Updated: 2026-01-19*
*Hardware: Greaseweazle V4.1 + Epson SD-800*
