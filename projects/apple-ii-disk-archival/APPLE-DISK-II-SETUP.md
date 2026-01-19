# Using Apple Disk II Drive with Greaseweazle

## Overview

While the Epson SD-800 works for most disks, a native Apple Disk II drive provides better results for marginal or heavily protected disks. This guide shows how to connect an Apple Disk II drive to the Greaseweazle V4.1.

**Difficulty:** Moderate (requires cable adapter or DIY wiring)

---

## Apple Disk II Drive Types

### 1. **Standalone Disk II** (External)
- Model: Apple A2M0003, Disk II
- Connector: DB-19 (19-pin D-sub)
- Common on: Apple II, II+, IIe
- **Easiest to use** with Greaseweazle

### 2. **UniDisk 5.25"**
- Model: Apple A9M0104
- Connector: DA-15 (15-pin D-sub) or DB-19
- Common on: Apple IIc, IIe (UniDisk)
- Similar to Disk II

### 3. **Built-in Drives** (IIc, IIgs)
- Apple IIc internal drive
- Apple IIgs internal 5.25" drive
- Connector: Internal ribbon cable
- **Most difficult** - requires extraction or special adapter

---

## Power Requirements

### Apple Disk II (External)
**Power:** 12V DC, ~500mA
**Connector:** 4-pin DIN or barrel jack (depending on model)

**Power Options:**

#### Option A: Original Apple Power Supply
- Use the Apple Disk II power supply if you have it
- Typically 12V DC, center positive
- Safest option

#### Option B: Universal 12V Adapter
- 12V DC, 1A minimum
- Center positive (check polarity!)
- 2.1mm or 2.5mm barrel jack (depending on drive)

**IMPORTANT:** Verify polarity before connecting! Wrong polarity will damage the drive.

#### Option C: Bench Power Supply
- Set to 12V DC
- Current limit to 1A
- Connect to drive power jack (verify polarity)

### Built-in Drives (IIc/IIgs)
**Power:** 5V from computer
- If extracted, need 5V supply (like SD-800)
- More complex, not recommended

---

## Connection Methods

### Method 1: Commercial Adapter (Easiest)

**AppleSauce Floppy Drive Controller** (~$90-120)
- **Website:** https://applesaucefdc.com/
- Includes hardware + software
- DB-19 to USB connection
- Works with Greaseweazle protocol
- **Best option if buying hardware**

**Advantages:**
- Plug-and-play
- No wiring needed
- Includes software
- Can use standalone or with Greaseweazle

**Disadvantages:**
- Cost ($90-120)
- Might be overkill if you already have Greaseweazle

---

### Method 2: DIY Adapter Cable (Moderate)

Build a DB-19 (Apple) to 34-pin (PC floppy) adapter cable.

**Parts Needed:**
- DB-19 male connector (connects to Disk II)
- 34-pin IDC connector (connects to Greaseweazle)
- 34-conductor ribbon cable (~3 feet)
- Soldering iron, wire, heat shrink

**Pinout Below** ↓

---

### Method 3: Use Apple Disk II Controller Card (Advanced)

**If you have an Apple II with controller card:**

1. Install Greaseweazle in PC
2. Connect Apple II controller card via custom cable
3. Connect Disk II to controller card as normal
4. Use special Greaseweazle mode

**Complex** - not recommended unless you're experienced

---

## Pin Mapping: DB-19 to 34-pin Floppy

### Apple Disk II DB-19 Pinout

```
DB-19 Female (looking at drive connector):

  1  2  3  4  5  6  7  8  9 10
 11 12 13 14 15 16 17 18 19

Pin  Signal          Description
---  -------------   ---------------------------
1    GND             Ground
2    GND             Ground
3    GND             Ground
4    GND             Ground
5    -12V            Negative 12V (not used on most drives)
6    N/C             Not connected
7    N/C             Not connected
8    DRIVESEL        Drive select (enable)
9    PHASE0          Stepper motor phase 0
10   PHASE1          Stepper motor phase 1
11   PHASE2          Stepper motor phase 2
12   PHASE3          Stepper motor phase 3
13   WRDATA          Write data
14   WRREQ           Write request (write gate)
15   RDDATA          Read data
16   SENSE           Write protect sense
17   +12V            +12V power
18   Q3              Stepper motor Q3 output
19   WRENABLE        Write enable (some drives)
```

### Standard 34-pin Floppy Pinout

```
34-pin IDC Connector (odd pins = ground):

Pin  Signal          Pin  Signal
---  -------------   ---  -------------
2    /REDWC (N/C)    1    GND
4    N/C             3    GND
6    N/C             5    GND
8    /INDEX          7    GND
10   /MOTEA          9    GND
12   /DRVSB          11   GND
14   /DRVSA          13   GND
16   /MOTEB          15   GND
18   /DIR            17   GND
20   /STEP           19   GND
22   /WDATA          21   GND
24   /WGATE          23   GND
26   /TRK00          25   GND
28   /WPT            27   GND
30   /RDATA          29   GND
32   /SIDE1          31   GND
34   /DSKCHG (N/C)   33   GND
```

### Mapping Table

| Apple DB-19 | Signal | 34-pin Floppy | Notes |
|-------------|--------|---------------|-------|
| 1,2,3,4 | GND | 1,3,5,7...33 (odd) | All grounds connected |
| 8 | DRIVESEL | 12 or 14 | Drive select (use 14 for DS0) |
| 9 | PHASE0 | 18 | Direction (requires logic) |
| 10 | PHASE1 | 20 | Step (requires logic) |
| 11 | PHASE2 | - | Not directly mapped |
| 12 | PHASE3 | - | Not directly mapped |
| 13 | WRDATA | 22 | Write data |
| 14 | WRREQ | 24 | Write gate |
| 15 | RDDATA | 30 | Read data |
| 16 | SENSE | 28 | Write protect |
| 17 | +12V | *External* | Need separate 12V supply |

**IMPORTANT:** Apple Disk II uses 4-phase stepper (PHASE0-3), while PC drives use DIR+STEP signals. This requires **logic conversion** or Greaseweazle smart mode.

---

## WARNING: Phase Stepper Incompatibility

**The Problem:**
- Apple Disk II: 4-phase stepper motor (PHASE0, PHASE1, PHASE2, PHASE3)
- PC Floppy: Direction + Step signals (DIR, STEP)
- **These are NOT directly compatible!**

**Solutions:**

### Option A: Greaseweazle "Apple Mode"

Greaseweazle firmware has special support for Apple drives:

```bash
# Use apple.35 format (35-track Apple mode)
gw read --drive A: --format apple.35 disk.scp
```

**However:** This still requires proper signal mapping in the cable.

### Option B: Logic Converter Circuit

Build a small circuit to convert PC signals to Apple 4-phase:
- Use 74LS logic chips
- Convert DIR+STEP → PHASE0-3
- **Complex** - requires electronics knowledge

### Option C: Use AppleSauce Hardware

AppleSauce FDC handles all signal conversion in hardware:
- No logic conversion needed
- Just plug in and go
- **This is why AppleSauce costs $90-120**

---

## Recommended Approach

### For Most Users: **Use SD-800 First**

1. Archive all disks with SD-800 (70-90% success rate)
2. Set aside disks that won't read
3. **Then** decide if you need Apple Disk II drive

### If You Need Apple Disk II Drive:

#### Best Option: **Buy AppleSauce FDC**
- **Cost:** $90-120
- **Includes:** Hardware + software + cable
- **Works:** Standalone or with Greaseweazle mode
- **Website:** https://applesaucefdc.com/

**Why AppleSauce is worth it:**
- No DIY wiring
- Signal conversion built-in
- Excellent software (auto-detects protection)
- Active support/updates
- Can sell after archival if needed

#### Budget Option: **DIY Cable + Greaseweazle**
- Requires electronics knowledge
- Must handle phase stepper conversion
- Risk of damaging drive if wired wrong
- Save ~$50-70 vs AppleSauce
- **Only if you're experienced with electronics**

---

## Using Apple IIc Internal Drive

Your Apple IIc has a built-in Disk II drive. Two approaches:

### Option A: Use IIc Directly (Not Recommended)
- Connect Greaseweazle to IIc controller via adapter
- Complex wiring
- Risk to IIc hardware
- **Don't do this unless expert**

### Option B: Extract Drive (Advanced)
1. Open IIc case (requires special tools)
2. Disconnect internal drive ribbon cable
3. Build adapter from internal connector to DB-19
4. Use as standalone drive with 5V power

**Complexity:** High
**Risk:** Medium (could damage IIc)
**Recommendation:** Leave IIc intact, use standalone Disk II if needed

---

## Standalone Disk II Drive Setup

If you acquire a standalone Apple Disk II drive:

### Step 1: Verify Drive Works
**Test with real Apple II first:**
1. Connect to Apple IIc or IIe
2. Verify drive spins, reads disks
3. Ensure power supply works

### Step 2: Acquire Adapter
**Options:**
1. **AppleSauce FDC** - $90-120 (recommended)
2. **DIY cable** - Build DB-19 to 34-pin with logic
3. **Existing adapter** - Check eBay for pre-made cables

### Step 3: Connect to Greaseweazle
```
[Disk II Drive] --DB-19--> [Adapter] --34-pin--> [Greaseweazle] --USB--> [PC]
                                                        └─ Power: 12V DC
```

### Step 4: Configure Greaseweazle
```bash
# Update firmware
gw update

# Test detection (may need special mode)
gw info

# Read disk with Apple format
gw read --drive A: --format apple.35 disk.scp
```

---

## AppleSauce FDC Setup (If Using)

### What is AppleSauce?
- Dedicated Apple II disk imaging hardware
- USB device (like Greaseweazle)
- Custom software + Greaseweazle-compatible mode

### Using AppleSauce

#### Standalone Mode (Recommended)
```bash
# Use AppleSauce software (GUI)
# 1. Connect drive to AppleSauce
# 2. Launch AppleSauce app
# 3. Click "Image Disk"
# 4. Automatic protection detection
# 5. Export as WOZ, DSK, or NIB
```

#### Greaseweazle Mode (Advanced)
```bash
# AppleSauce can act as Greaseweazle
# Use standard gw commands
gw read --drive A: --format apple.35 disk.scp
```

**Advantages of AppleSauce Software:**
- Auto-detects copy protection
- Real-time quality display
- Built-in metadata editor
- Export multiple formats

---

## Comparison: SD-800 vs Disk II vs AppleSauce

| Feature | SD-800 | Disk II + DIY | AppleSauce |
|---------|--------|---------------|------------|
| **Cost** | $0 (you have it) | ~$50-100 | ~$90-120 |
| **Setup Difficulty** | Easy | Hard | Easy |
| **Success Rate** | 70-80% | 95%+ | 95%+ |
| **Wiring** | Standard cable | Custom cable | Plug-and-play |
| **Software** | Greaseweazle | Greaseweazle | AppleSauce + GW |
| **Protection Detection** | Manual | Manual | Automatic |
| **Best For** | Most disks | Budget + skills | Best results |

---

## Decision Guide

### Use SD-800 If:
- ✅ Archiving good condition disks
- ✅ Success rate acceptable (70-80%)
- ✅ Budget-conscious
- ✅ Don't want to buy/build adapters

### Use Disk II + DIY If:
- ✅ Already have Disk II drive
- ✅ Comfortable with electronics
- ✅ Want best results without buying AppleSauce
- ✅ Enjoy DIY projects

### Use AppleSauce If:
- ✅ Need best possible results
- ✅ Want plug-and-play solution
- ✅ Large collection to archive
- ✅ Value time over cost
- ✅ Want automatic protection detection

---

## Step-by-Step: SD-800 → AppleSauce Upgrade Path

### Phase 1: Archive with SD-800 (Week 1-2)
```bash
# Archive all disks with SD-800
# Track which disks fail
# Success rate: ~70-80%
```

### Phase 2: Evaluate Results (Week 3)
```bash
# Count successful vs failed disks
# If < 20% failed → stick with SD-800
# If > 20% failed → consider upgrade
```

### Phase 3: Upgrade Decision
- **< 5 failed disks** → Not worth upgrading
- **5-20 failed disks** → Consider AppleSauce
- **> 20 failed disks** → Definitely get AppleSauce

### Phase 4: Re-archive Failed Disks
```bash
# Use AppleSauce for disks that SD-800 couldn't read
# Should get 90%+ of remaining disks
```

---

## Where to Buy

### AppleSauce FDC
- **Official:** https://applesaucefdc.com/
- **Price:** ~$90-120 depending on model
- Ships worldwide

### Standalone Disk II Drives
- **eBay:** Search "Apple Disk II A2M0003"
- **Price:** $50-150 (varies with condition)
- Verify working before buying

### DIY Parts
- **DB-19 connector:** Mouser, Digi-Key (~$5-10)
- **34-pin IDC:** Amazon, eBay (~$2-5)
- **Logic ICs:** If building converter (~$5-10)

---

## Alternative: Professional Archival Service

If you have many failed disks and don't want to invest in hardware:

### Services
- **AppleSauce Archival Service** - Mail disks to be imaged
- **RetroFloppy** - Professional disk archival
- **Internet Archive** - Free archival (they keep copies)

### Cost
- ~$5-10 per disk
- Bulk discounts available
- Worth it for rare/valuable software

---

## Bottom Line

**For The Print Shop / Toy Shop:**
1. **Try SD-800 first** with optimal settings
2. If both disks read successfully → done!
3. If one fails after 3 attempts → consider:
   - Set aside for now
   - Continue archiving other disks
   - Later: AppleSauce or professional service

**You don't need Apple Disk II immediately.** Most disks (70-80%) work fine with SD-800. Only upgrade if you have many failures.

---

## Resources

### Documentation
- [AppleSauce FDC](https://applesaucefdc.com/)
- [Greaseweazle Wiki](https://github.com/keirf/greaseweazle/wiki)
- [Apple II Documentation Project](https://mirrors.apple2.org.za/)

### Communities
- **AppleSqueezer Forum** - Disk preservation experts
- **VCF Forum** - Vintage computer hardware
- **/r/apple2** - Reddit community

### Pinouts & Schematics
- [Apple Disk II Schematics](https://mirrors.apple2.org.za/ftp.apple.asimov.net/documentation/hardware/disk_drives/)
- [Understanding Apple Disk II](http://www.brutaldeluxe.fr/documentation/diskii/)

---

**Summary:** Start with SD-800, upgrade to AppleSauce if needed. Don't rush to build DIY cables unless you enjoy electronics and have the skills!

---

**Created:** 2026-01-19
**For:** Apple II Disk Archival Project
**Hardware Options:** SD-800 vs Disk II vs AppleSauce
