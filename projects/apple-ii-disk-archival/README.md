# Apple II Disk Archival Project

## Overview

Comprehensive archival and preservation of Apple II 5.25" and 3.5" floppy disk collection using flux-level imaging with Greaseweazle V4.1. Includes copy protection removal techniques for creating working backup copies of legally owned software.

**Status:** Active Development
**Priority Disks:** The Print Shop, The Toy Shop (Broderbund)

## Equipment

- ✅ **Greaseweazle V4.1** - Flux-level disk imaging device
- ✅ **Apple IIc** - Built-in Disk II compatible drive
- ✅ **Apple IIgs** - Supports both 5.25" and 3.5" disks
- ✅ **Development PC** - For running Greaseweazle software, emulators

## Objectives

1. **Preservation** - Create bit-perfect flux images (.SCP) of all disks
2. **Usability** - Convert to .WOZ format for emulator use
3. **Backup** - Create unprotected .DSK images for real hardware
4. **Documentation** - Catalog collection with metadata
5. **Knowledge** - Document copy protection schemes and removal techniques

## Disk Collection (To Be Archived)

### High Priority
- **The Print Shop** - Program disk + graphics libraries (Broderbund, 1984)
- **The Toy Shop** - Toy creation program (Broderbund, 1986)

### Future
- TBD as collection is cataloged

## Project Structure

```
apple-ii-disk-archival/
├── README.md                     # This file - project overview
├── SETUP.md                      # Quick setup guide (START HERE!)
├── hardware-setup.md             # Greaseweazle + SD-800 configuration
├── tools/                        # Software tools for archival
│   ├── README.md                 # Tool documentation
│   ├── wozardry/                 # WOZ file manipulation
│   └── passport.py/              # Protection removal (submodule)
└── archive/                      # Created during archival
    ├── flux-masters/             # .SCP preservation files
    ├── woz-images/               # .WOZ converted images
    ├── dsk-images/               # .DSK unprotected backups
    └── metadata/                 # Disk catalogs and notes
```

## Quick Start

**📖 See [SETUP.md](SETUP.md) for complete step-by-step setup instructions!**

### 1. Setup Greaseweazle

```bash
# Install Greaseweazle tools
pip install greaseweazle

# Update firmware
gw update

# Connect hardware:
# [PC] --USB--> [Greaseweazle] --34-pin--> [Epson SD-800 (5.25" + 3.5")]

# Test detection
gw info
# Should show Drive A: (5.25") and Drive B: (3.5")
```

### 2. Read First Disk (The Print Shop)

```bash
# Clean drive heads first!
# Use isopropyl alcohol on cotton swab

# Read flux image
gw read --drive A: --format apple2.140 \
    --retries 10 \
    "archive/flux-masters/PrintShop_Program.scp"

# Backup immediately!
cp archive/flux-masters/PrintShop_Program.scp \
    archive/flux-masters/PrintShop_Program_BACKUP.scp
```

### 3. Convert to .WOZ

```bash
# Install wozardry
pip install wozardry

# Convert
python wozardry.py convert \
    archive/flux-masters/PrintShop_Program.scp \
    archive/woz-images/PrintShop_Program.woz
```

### 4. Test in Emulator

```bash
# Download AppleWin
# https://github.com/AppleWin/AppleWin

# Boot image
AppleWin.exe --disk1=archive/woz-images/PrintShop_Program.woz
```

## Copy Protection Overview

### Common Schemes in Collection

| Program | Protection Type | Difficulty |
|---------|----------------|------------|
| The Print Shop | Nibble count + custom RWTS | Medium |
| The Toy Shop | Nibble count + custom RWTS | Medium |

**Solution:** Flux imaging preserves ALL protection schemes. .WOZ format allows emulator use without cracking.

## Workflow

### Phase 1: Flux Imaging (Preservation Master)
1. Clean drive heads
2. Read disk to .SCP with Greaseweazle
3. Backup .SCP to multiple locations
4. Document disk label, condition, read errors

### Phase 2: Conversion (.WOZ for Emulators)
1. Convert .SCP to .WOZ format
2. Test in AppleWin emulator
3. Verify program boots and runs correctly

### Phase 3: Unprotected Backups (Optional)
1. Use 4am's crack tools or find pre-cracked versions
2. Create .DSK images for real hardware
3. Transfer to Apple II via ADTPro

### Phase 4: Organization
1. Catalog all disks with metadata
2. Organize by category (games, productivity, education)
3. Create README files for each program

## Tools Used

### Hardware
- Greaseweazle V4.1 - Flux imaging
- Epson SD-800 - Dual 5.25"/3.5" floppy drives
- 34-pin floppy cable
- 5V power supply (for SD-800)

### Software (Included as Git Submodules)
- **wozardry** - WOZ file manipulation (tools/wozardry/)
- **passport.py** - Protection removal (tools/passport.py/)

### Software (Install Separately)
- **Greaseweazle** - Flux imaging tool (pip install)
- **AppleWin** - Apple II emulator (Windows)
- **HxC Software** - SCP to WOZ conversion (free)
- **AppleCommander** - Disk image management (Java)
- **CiderPress** - Windows disk image manager (optional)

## Documentation

### Project Guides (Start Here!)
- **[SETUP.md](SETUP.md)** - Step-by-step setup guide (START HERE!)
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Having issues with SD-800? Check here!
- [APPLE-DISK-II-SETUP.md](APPLE-DISK-II-SETUP.md) - Using native Apple Disk II drive (if SD-800 insufficient)
- [hardware-setup.md](hardware-setup.md) - Greaseweazle + SD-800 configuration
- [tools/README.md](tools/README.md) - Software tools documentation

### Reference Guides
- [Notes/hardware/apple-ii-disk-copy-protection-archival.md](../../Notes/hardware/apple-ii-disk-copy-protection-archival.md)
  - Copy protection schemes explained
  - Tool comparison and recommendations
  - Step-by-step archival workflow
  - Protection removal techniques

### Specific Programs
- [Notes/hardware/apple-ii-printshop-toyshop-guide.md](../../Notes/hardware/apple-ii-printshop-toyshop-guide.md)
  - The Print Shop and The Toy Shop details
  - Broderbund protection specifics
  - Quick start checklist

## Related Projects

### Matt's GitHub Repositories
- [PrinterEmulator](https://github.com/mwwhited/PrinterEmulator) - Printer capture work
- [DeviceBridge](https://github.com/mwwhited/DeviceBridge) - IEEE-1284 parallel port capture
- [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery) - Multi-platform embedded projects

### Other Projects in This Repo
- [ImageWriter II Emulator](../imagewriter-ii-emulator/) - Capture Print Shop output to modern printers
- [MM-8000K Trainer UI](../mm8000-trainer-ui/) - Intel 8085 reference hardware
- [Vintage Computers](../../Vintage%20Computers/) - Apple II hardware inventory

## Resources

### Communities
- **AppleSqueezer Forum** - Disk preservation experts
- **comp.sys.apple2** - Usenet group (still active)
- **/r/apple2** - Reddit community
- **a2central.com** - Apple II news and forums

### Archives
- **Asimov** - https://ftp.apple.asimov.net/
- **Internet Archive** - https://archive.org/details/softwarelibrary_apple
- **4am's work** - https://github.com/a2-4am/

### Documentation
- **Apple II Documentation Project** - https://mirrors.apple2.org.za/
- **Beneath Apple DOS** - RWTS internals book
- **What's New (Call-A.P.P.L.E.)** - Copy protection newsletter

## Legal and Ethical Notes

### Legal (most jurisdictions)
- ✅ Archiving software you own for personal backup
- ✅ Preserving abandoned software (abandonware)
- ✅ Creating working copies for personal use
- ❌ Distributing cracked software
- ❌ Selling cracked images
- ❌ Circumventing for piracy

### Best Practices
- Only archive software you physically own
- Support active developers (buy modern releases)
- Share preservation knowledge, not pirated software
- Contribute to preservation projects (Internet Archive, 4am)

## Progress Tracking

### Status
- [ ] Greaseweazle setup verified
- [ ] The Print Shop program disk archived
- [ ] The Print Shop graphics libraries archived
- [ ] The Toy Shop archived
- [ ] .WOZ conversions tested in emulator
- [ ] Archive backed up (3-2-1 rule)
- [ ] Collection catalog created

### Archive Statistics
- **Disks imaged:** 0 / TBD
- **Flux size:** 0 MB
- **Programs preserved:** 0

## Next Steps

1. Set up Greaseweazle hardware connection
2. Test with a known-working disk
3. Read The Print Shop program disk
4. Convert to .WOZ and test in emulator
5. Continue with graphics libraries
6. Archive The Toy Shop
7. Begin collection catalog

## Contributing

Preservation findings and techniques documented here may help the broader Apple II community. Consider:
- Sharing metadata with Internet Archive
- Contributing protection analysis to 4am's work
- Documenting rare or unknown protection schemes

---

**Started:** 2026-01-19
**Last Updated:** 2026-01-19
**Author:** Matt Whited ([mwwhited](https://github.com/mwwhited))
