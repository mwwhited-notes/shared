# Hardware Setup - Greaseweazle + Epson SD-800

## Equipment

- **Greaseweazle V4.1** - Flux-level disk imaging device
- **Epson SD-800** - **Dual-drive unit** (5.25" + 3.5" in one enclosure)
- **34-pin floppy cable** - Standard PC floppy ribbon cable
- **5V power supply** - For the SD-800 drives (Molex or SATA power)

## Epson SD-800 Overview

**This is PERFECT for Apple II archival!**

The SD-800 is a combination drive with:
- **5.25" drive** - For Apple II/IIe/IIc disks (140KB)
- **3.5" drive** - For Apple IIgs disks (800KB)
- **Single 34-pin connector** - Both drives on one cable
- **Shared power** - One Molex connector powers both
- **Drive select jumpers** - Access either or both drives

## Important: SD-800 vs Apple Disk II

### Key Differences

| Feature | Apple Disk II | Epson SD-800 |
|---------|--------------|--------------|
| **Type** | Apple proprietary | Standard PC drive |
| **Tracks** | 35 (0-34) | 40 (0-39) |
| **Speed** | 300 RPM variable | 300 RPM constant |
| **Head Load** | Solenoid | Mechanical |
| **Interface** | Custom Apple controller | Standard PC floppy |
| **Track 0 Sensor** | Optical | Magnetic |
| **Drive Select** | Custom | Standard DS0/DS1 |

### Why This Matters

✅ **Good News:**
- Greaseweazle handles all interface differences at the flux level
- SD-800 can physically read Apple II disks
- 40-track capability covers all 35 Apple II tracks
- Speed is compatible (both 300 RPM)

⚠️ **Potential Issues:**
- Different stepper motor characteristics (may affect track alignment)
- Head positioning accuracy varies between drives
- Some Apple II disks may have marginal signals that Apple drives read better

**Recommendation:** The SD-800 will work, but you may encounter more read errors than with a native Apple Disk II drive. Greaseweazle's retry and error correction should compensate.

---

## Physical Connections

### Power Connection

The Epson SD-800 requires **5V power** from a standard PC power supply.

**Molex 4-pin connector pinout:**
```
     +12V  GND  GND  +5V
      │     │    │    │
    ┌─┴─────┴────┴────┴─┐
    │  1   2    3    4  │
    └────────────────────┘
```

**Options:**
1. **PC Power Supply** - Use old ATX PSU, short green wire to ground to turn on
2. **Molex Adapter** - 5V wall adapter with Molex connector (~$10-15)
3. **Bench Power Supply** - Set to 5V, connect to pins 3 (GND) and 4 (+5V)

**Important:** Only +5V is used. The +12V line is NOT needed for 5.25" drives (only 3.5" drives use +12V for spindle motor).

---

### Data Connection

**Standard 34-pin floppy ribbon cable:**

```
[Greaseweazle V4.1] ──34-pin ribbon cable── [Epson SD-800]
    (USB to PC)                                (Both drives share connector)
```

**Cable orientation:**
- Pin 1 indicated by red stripe on ribbon cable
- Pin 1 on Greaseweazle connector (marked)
- Pin 1 on SD-800 (usually marked with "1" or dot)

### Drive Select Configuration

**Good news: No modifications needed!**

The SD-800 is factory-configured with:
- **5.25" drive:** DS0 (Drive A:)
- **3.5" drive:** DS1 (Drive B:)

**Just plug in and use:**
```bash
# Read from 5.25" drive
gw read --drive A: --format apple2.140 disk_name.scp

# Read from 3.5" drive
gw read --drive B: --format apple2.800 disk_name_800k.scp
```

**Verification:** When you run `gw info`, both drives should be detected automatically. No jumper changes required!

---

### Cable Twist Consideration

**Standard PC floppy cables have a twist** between the two drive connectors:

```
[Controller] ──────┬──── [Drive A connector] ── (twisted section)
                   │
                   └──── [Drive B connector] ── (straight)
```

**Configuration:**
- **If cable has twist:** Set SD-800 to DS0, use connector AFTER twist (Drive A position)
- **If cable is straight:** Set SD-800 to DS1, use either connector

**How to tell:** Look at the ribbon cable between the two drive connectors. If 5-6 wires are twisted 180°, it's a twisted cable.

**Greaseweazle default:** Reads Drive A: (after twist) or Drive B: (no twist)

---

## Greaseweazle Configuration

### Drive Parameters

The Epson SD-800 is a standard PC drive, so Greaseweazle should auto-detect most settings.

**Verify settings:**
```bash
# Check Greaseweazle detects the drive
gw info

# Should show:
# Drive A: Connected
# Drive Type: 5.25" 40-track
```

### Reading Apple II Disks

**For 5.25" disks (140KB - Apple II/IIe/IIc):**
```bash
gw read --drive A: --format apple2.140 disk_name.scp
```

**For 3.5" disks (800KB - Apple IIgs):**
```bash
gw read --drive B: --format apple2.800 disk_name_800k.scp
```

**Potential adjustments needed:**

#### 1. Track Stepping
If you get track alignment errors:

```bash
# Adjust step rate (slower = more reliable)
gw read --drive A: --format apple2.140 \
    --tracks 0-34 \
    --step-rate 6ms \
    disk_name.scp
```

#### 2. RPM Variation
If you get speed errors:

```bash
# Allow for RPM variation
gw read --drive A: --format apple2.140 \
    --rpm-range 295-305 \
    disk_name.scp
```

#### 3. Head Settle Time
For marginal disks:

```bash
# Increase head settle time
gw read --drive A: --format apple2.140 \
    --settle-time 20ms \
    disk_name.scp
```

#### 4. Read Retries
Always use retries for protected disks:

```bash
gw read --drive A: --format apple2.140 \
    --retries 10 \
    disk_name.scp
```

### Recommended Command for SD-800

**Combine all adjustments for best results:**

```bash
gw read --drive A: --format apple2.140 \
    --tracks 0-34 \
    --step-rate 6ms \
    --settle-time 20ms \
    --retries 10 \
    disk_name.scp
```

**For very marginal disks:**

```bash
gw read --drive A: --format apple2.140 \
    --tracks 0-34 \
    --step-rate 8ms \
    --settle-time 30ms \
    --retries 20 \
    --rpm-range 295-305 \
    disk_name.scp
```

---

## Testing Procedure

### 1. Power Check

**Before connecting disk:**
1. Connect 5V power to SD-800
2. Power on
3. Drive LED should light briefly
4. Spindle motor should NOT run (no disk inserted)
5. Listen for stepper motor (may click once at power-on)

**If motor runs continuously:** Power off immediately! Something is wrong.

### 2. Greaseweazle Detection

```bash
# Update Greaseweazle firmware (if needed)
gw update

# Check drive detection
gw info

# Should report:
# Greaseweazle V4.1
# Drive A: 5.25" 40-track (SD-800 5.25" drive)
# Drive B: 3.5" 80-track (SD-800 3.5" drive)
```

**Perfect!** Both drives should be detected.

### 3. Test Disk Read

**Use a sacrificial/duplicate disk first!**

```bash
# Try reading a test disk
gw read --drive A: --format apple2.140 \
    --retries 5 \
    test_disk.scp

# Check output
ls -lh test_disk.scp
# Should be ~600KB to 1.2MB
```

**Success indicators:**
- No error messages
- .SCP file created
- File size reasonable (600KB+)
- No grinding or unusual noises from drive

**Failure indicators:**
- "Track 0 not found" - Check drive select jumpers
- "Speed error" - Adjust RPM range
- "Read timeout" - Check cable connections
- "Weak signal" - Try cleaning drive heads

---

## Drive Maintenance

### Cleaning the SD-800 Heads

**You should clean heads before imaging:**

1. **Remove drive cover** (usually 4 screws)
2. **Locate read/write head** (metal piece that contacts disk)
3. **Clean with isopropyl alcohol** (90%+ recommended)
   - Use cotton swab or foam swab
   - Gently wipe head surface
   - Let dry completely (30 seconds)
4. **Reassemble**

**When to clean:**
- Before first use (if drive is old)
- After every 10-20 disk reads
- If you get increasing read errors
- If you see brown residue on disks after reading

### Head Alignment Check

**The SD-800 may need alignment** if it's very old or has been stored improperly.

**Symptoms of misalignment:**
- Reads track 0, fails on other tracks
- Can read some disks, not others
- Increasing errors toward outer tracks

**Solution:**
- Use Greaseweazle's diagnostic mode to check track positioning
- Or send drive for professional alignment (~$50-100)
- Or replace with another drive if you have spares

**Greaseweazle diagnostic:**
```bash
gw read --drive A: --format apple2.140 \
    --tracks 17-17 \
    --revs 5 \
    test_track17.scp

# Review flux image to see if track is centered
```

---

## Comparison: SD-800 vs Apple Disk II

### Reading Performance

| Disk Condition | Apple Disk II | Epson SD-800 | Notes |
|----------------|---------------|--------------|-------|
| **Mint condition** | Excellent | Excellent | Both read perfectly |
| **Good condition** | Excellent | Good-Excellent | SD-800 may need retries |
| **Fair condition** | Good | Fair-Good | SD-800 may struggle |
| **Poor condition** | Fair | Poor | Apple drive preferred |
| **Marginal bits** | Good | Fair | Native drive advantage |

### Why Apple Disk II is Better (When Available)

1. **Optimized for Apple disks** - Head positioning designed for Apple format
2. **Better weak bit handling** - Apple drives more sensitive
3. **Speed matching** - Exact RPM tuning for Apple disks
4. **Original hardware** - Same as disks were written on

### Why SD-800 is Acceptable

1. **Greaseweazle compensates** - Flux imaging captures marginal data
2. **Retries work** - Multiple reads improve success rate
3. **Most disks work fine** - Good condition disks read perfectly
4. **Readily available** - Easier to find than Apple drives
5. **Cheaper** - PC drives are inexpensive

**Recommendation:** Use the SD-800 for your archival project. If you encounter disks that won't read reliably, consider acquiring an Apple Disk II drive as a backup.

---

## Alternative: Apple Disk II Drive

If you want to use a native Apple drive in the future:

**Options:**
1. **Standalone Disk II** - Apple A2M0003 (requires 12V power + custom cable)
2. **IIc/IIgs Internal Drive** - Can be extracted and used standalone
3. **Daisy Chain** - Use IIc with drive attached, interface via controller card

**Connection to Greaseweazle:**
- Requires custom cable (DA-15 or 19-pin to 34-pin)
- Several adapters available commercially (~$30-50)
- Or build your own (pinout available online)

**Not needed immediately** - Try SD-800 first!

---

## Troubleshooting Guide

### "Track 0 Not Found"

**Causes:**
- Drive select jumper wrong (DS0 vs DS1)
- Cable not fully seated
- Drive not powered

**Solutions:**
```bash
# Check drive select jumper is DS1 (or DS0 if twisted cable)
# Reseat 34-pin cable
# Check 5V power is connected
# Try other drive connector on cable
```

### "Speed Error" or "RPM Out of Range"

**Causes:**
- Drive motor speed incorrect (not 300 RPM)
- Belt slipping (if belt-driven motor)
- Greaseweazle expecting exact speed

**Solutions:**
```bash
# Widen acceptable RPM range
gw read --drive A: --format apple2.140 \
    --rpm-range 290-310 \
    disk_name.scp

# Or disable speed check (not recommended)
--no-rpm-check
```

### "Read Errors on Multiple Tracks"

**Causes:**
- Dirty heads
- Weak disk signal (old/degraded disk)
- Head misalignment

**Solutions:**
1. Clean drive heads thoroughly
2. Increase retries: `--retries 20`
3. Adjust settle time: `--settle-time 30ms`
4. Try different disk (test if it's the drive or the disk)

### "Works for Some Disks, Not Others"

**Normal!** Different disks have different signal quality.

**Strategy:**
- Clean heads before reading each disk
- Use maximum retries for problematic disks
- Try reading at different times (disk may warm up and work better)
- Note which disks fail, try them with Apple Disk II drive later

---

## Power Supply Setup

### Option 1: Old PC Power Supply (Recommended)

**Requirements:**
- Any old ATX power supply (200W+)
- Wire or paperclip to jumper PS_ON

**Setup:**
1. Find green wire (PS_ON) on 24-pin motherboard connector
2. Short to any black wire (GND) to turn on PSU
3. Connect Molex power to SD-800
4. Power is now on continuously while jumper is connected

**Advantages:**
- Free (if you have old PSU)
- Can power multiple drives
- Can also power Greaseweazle via USB

### Option 2: 5V Adapter with Molex

**Buy:**
- 5V 2A wall adapter with Molex connector
- Available on Amazon/eBay for ~$10-15

**Advantages:**
- Clean, compact
- No fan noise
- Safe

### Option 3: Bench Power Supply

**Setup:**
- Set to 5V
- Connect black probe to Molex pin 3 (GND)
- Connect red probe to Molex pin 4 (+5V)
- Set current limit to 1A (drive draws ~500mA)

**Advantages:**
- Adjustable voltage (can fine-tune if needed)
- Current limiting (protects drive)
- Useful for debugging

---

## Complete Setup Checklist

### Hardware
- [ ] Greaseweazle V4.1 connected to PC via USB
- [ ] SD-800 drive powered (5V on Molex)
- [ ] 34-pin ribbon cable connected (Greaseweazle to SD-800)
- [ ] Drive select jumper set to DS1 (or DS0 if twisted cable)
- [ ] Pin 1 alignment correct (red stripe matches pin 1 marks)

### Software
- [ ] Greaseweazle software installed (`pip install greaseweazle`)
- [ ] Firmware updated (`gw update`)
- [ ] Drive detected (`gw info`)

### Testing
- [ ] Drive LED lights when power applied
- [ ] Disk spins when inserted (motor runs)
- [ ] Test read completes without errors
- [ ] .SCP file created with reasonable size

### Cleaning
- [ ] Drive heads cleaned with isopropyl alcohol
- [ ] Drive tested with sacrificial disk first

---

## Summary

**Your hardware setup:**
- ✅ Greaseweazle V4.1 - Excellent flux imager
- ✅ Epson SD-800 - Standard PC drive, will work fine for most Apple II disks
- ⚠️ May struggle with marginal/poor condition disks (compared to Apple Disk II)

**Recommended workflow:**
1. Clean SD-800 heads
2. Set drive select to DS1
3. Use extended read command with retries and settle time
4. Start with good condition disks to build confidence
5. If problematic disks won't read, note them for future attempt with Apple drive

**You're ready to start archiving!** The SD-800 is perfectly capable for this project. Focus on The Print Shop and The Toy Shop disks first as planned.

---

**Created:** 2026-01-19
**Hardware:** Greaseweazle V4.1 + Epson SD-800
**For:** Apple II disk archival project
