# Troubleshooting Guide - Epson SD-800 + Greaseweazle

## Overview

The Epson SD-800 is a standard PC floppy drive, not an Apple Disk II drive. While it works well for most Apple II disks, you may encounter issues. This guide helps diagnose and fix common problems.

---

## Quick Diagnosis Checklist

Run through this checklist first:

- [ ] Drive powered on (5V connected)
- [ ] Drive LED lights when disk inserted
- [ ] Greaseweazle detects drive (`gw info`)
- [ ] 34-pin cable fully seated
- [ ] Drive heads cleaned recently
- [ ] Disk is not physically damaged
- [ ] Trying with known-good disk first

If all checkboxes pass but still having issues, continue below.

---

## Common Issues and Solutions

### Issue 1: "Track 0 Not Found" or "No Drive Detected"

**Symptoms:**
```
Error: Track 0 not found
Error: Drive not ready
Error: No index pulse detected
```

**Causes:**
1. Drive not powered
2. Cable not connected properly
3. Drive select jumper wrong
4. Greaseweazle firmware issue

**Solutions:**

#### A. Verify Power
```bash
# With disk inserted, drive motor should spin
# LED should light when disk inserted
# Listen for spindle motor (should be audible)
```

If no power:
- Check Molex connector seated firmly
- Verify 5V on pin 4 (yellow wire)
- Check power supply is on (if using ATX, green wire shorted to black)

#### B. Check Cable
```bash
# Ensure 34-pin cable is fully seated
# Pin 1 (red stripe) aligned correctly on both ends
# No bent pins on connector
```

Try:
- Reseat cable at both ends
- Try different connector on cable (if it has two)
- Inspect for damaged cable

#### C. Verify Drive Detection
```bash
gw info

# Should show:
# Drive A: 5.25" 40-track
# Drive B: 3.5" 80-track
```

If drives not detected:
```bash
# Update firmware
gw update

# Force drive type
gw read --drive A: --format apple2.140 --drive-type 40 disk.scp
```

---

### Issue 2: "Speed Error" or "RPM Out of Range"

**Symptoms:**
```
Error: Disk speed 285 RPM (expected 300 RPM)
Error: RPM variation too high
Warning: Speed unstable
```

**Causes:**
1. Drive motor not at 300 RPM
2. Belt slipping (if belt-driven)
3. Greaseweazle expecting exact speed

**Solutions:**

#### A. Widen RPM Range
```bash
# Allow ±5 RPM variation
gw read --drive A: --format apple2.140 \
    --rpm-range 295-305 \
    disk.scp

# For worse drives, allow ±10 RPM
gw read --drive A: --format apple2.140 \
    --rpm-range 290-310 \
    disk.scp
```

#### B. Disable Speed Check (Not Recommended)
```bash
# Only use if disk is VERY important and other methods fail
gw read --drive A: --format apple2.140 \
    --no-rpm-check \
    disk.scp
```

**Warning:** This may result in unusable flux images if speed varies too much!

#### C. Check Drive Motor
- Let drive warm up for 5 minutes
- Try reading same disk multiple times (motor may stabilize)
- If belt-driven, belt may need replacement

---

### Issue 3: Read Errors on Multiple Tracks

**Symptoms:**
```
Error: Track 5: Bad sector read
Error: Track 12: Weak signal
Warning: Multiple retries on track 17
```

**Causes:**
1. Dirty drive heads
2. Weak disk signal (age/degradation)
3. Head alignment issues
4. Incorrect stepping rate

**Solutions:**

#### A. Clean Heads Thoroughly
```bash
# Power off drive
# Remove cover
# Clean R/W heads with 90%+ isopropyl alcohol
# Use cotton swab, wipe gently
# Let dry 30 seconds
# Reassemble and retry
```

#### B. Increase Retries
```bash
gw read --drive A: --format apple2.140 \
    --retries 20 \
    disk.scp

# For very marginal disks
gw read --drive A: --format apple2.140 \
    --retries 50 \
    disk.scp
```

#### C. Adjust Stepping and Settle Time
```bash
# Slow down track stepping for better positioning
gw read --drive A: --format apple2.140 \
    --step-rate 8ms \
    --settle-time 30ms \
    --retries 20 \
    disk.scp
```

**Optimal SD-800 settings:**
```bash
gw read --drive A: --format apple2.140 \
    --tracks 0-34 \
    --step-rate 6ms \
    --settle-time 20ms \
    --retries 10 \
    --rpm-range 295-305 \
    disk.scp
```

#### D. Try Different Track Range
```bash
# Some protection schemes use tracks beyond 34
gw read --drive A: --format apple2.140 \
    --tracks 0-39 \
    disk.scp
```

---

### Issue 4: Works for Some Disks, Not Others

**Symptoms:**
- Known-good disks read fine
- Protected disks fail
- Success rate ~50%

**This is NORMAL with PC drives!**

**Explanation:**
- PC drives (SD-800) have different tolerances than Apple Disk II
- Marginal disks that barely work on Apple drives may fail on PC drives
- Weak bits, timing variations are harder to read

**Solutions:**

#### A. Disk Triage System

**Good Condition Disks:**
```bash
# These should read fine with standard settings
gw read --drive A: --format apple2.140 \
    --retries 10 \
    disk.scp
```

**Fair Condition Disks:**
```bash
# Use extended retries and settling
gw read --drive A: --format apple2.140 \
    --retries 20 \
    --settle-time 30ms \
    disk.scp
```

**Poor Condition Disks:**
```bash
# Maximum retries, slow stepping, wide RPM range
gw read --drive A: --format apple2.140 \
    --retries 50 \
    --step-rate 8ms \
    --settle-time 40ms \
    --rpm-range 290-310 \
    disk.scp
```

#### B. Set Aside Problematic Disks
- Mark disks that won't read reliably
- Try again after successfully archiving good disks
- Consider acquiring Apple Disk II drive for these

---

### Issue 5: "Index Pulse Not Detected"

**Symptoms:**
```
Error: No index pulse detected
Error: Drive not spinning
```

**Causes:**
1. Disk not inserted properly
2. Drive mechanism jammed
3. Drive motor not running
4. Index sensor failure

**Solutions:**

#### A. Check Disk Insertion
- Disk should click when fully inserted
- Drive door/lever should latch
- Motor should start spinning immediately
- Try ejecting and reinserting

#### B. Manual Drive Test
```bash
# Insert disk
# Wait 5 seconds for motor to stabilize
# Run test read
gw read --drive A: --format apple2.140 --tracks 0-0 test.scp
```

If still fails:
- Try different disk (known-good)
- Drive may need repair/replacement

---

## Advanced Troubleshooting

### Head Alignment Check

The SD-800 may have alignment issues if very old.

**Test:**
```bash
# Read track 17 (middle track) multiple times
gw read --drive A: --format apple2.140 \
    --tracks 17-17 \
    --revs 5 \
    test_track17.scp

# Compare file sizes - should be similar
ls -lh test_track17.scp

# Repeat test
gw read --drive A: --format apple2.140 \
    --tracks 17-17 \
    --revs 5 \
    test_track17_2.scp

# Compare with diff or hex editor
```

**If files differ significantly:**
- Head may be misaligned
- Professional alignment needed (~$50-100)
- Or replace drive

---

### Drive Speed Calibration

**Test actual RPM:**
```bash
# Read track 0, check reported RPM
gw read --drive A: --format apple2.140 \
    --tracks 0-0 \
    --info \
    test.scp

# Look for: "RPM: XXX"
# Should be 295-305 RPM
```

**If speed consistently off:**
- May need drive motor adjustment (difficult)
- Use `--rpm-range` to compensate
- Or replace drive

---

### Multiple Read Attempts

**Strategy: Read same disk 3x, compare:**

```bash
# Read 1
gw read --drive A: --format apple2.140 \
    --retries 20 \
    disk_read1.scp

# Read 2
gw read --drive A: --format apple2.140 \
    --retries 20 \
    disk_read2.scp

# Read 3
gw read --drive A: --format apple2.140 \
    --retries 20 \
    disk_read3.scp

# Compare file sizes
ls -lh disk_read*.scp

# If sizes similar (~10KB variation), reads are consistent
# Pick best quality read (fewest errors in log)
```

---

## When to Consider Apple Disk II Drive

### Signs You Need a Native Drive:

1. **Success rate < 50%** with good disks
2. **Many disks won't read** even with max retries
3. **Critical/rare disks failing** consistently
4. **Time is valuable** - native drive saves frustration

### Acquiring Apple Disk II Drive:

**Options:**
1. **Standalone Disk II** (Apple A2M0003)
   - ~$50-150 on eBay
   - Requires 12V power + custom cable

2. **Extract from Apple IIc** (you have one!)
   - Internal drive can be used standalone
   - Needs cable adapter

3. **Use Apple IIc Directly**
   - Connect Greaseweazle via controller card adapter
   - More complex but possible

### Greaseweazle + Apple Disk II Adapter:

**Commercial adapters available:**
- **AppleSauce FDC** ($90-120) - includes adapter + software
- **DIY cable** - DA-15 to 34-pin adapter (pinout online)

---

## Alternative Approaches

### Option 1: Try Different PC Drive

If you have access to other 5.25" drives:
- Different manufacturers have different tolerances
- Some PC drives work better than others
- Try: Teac FD-55, Panasonic JU-475, etc.

### Option 2: Professional Archival Service

**Services that specialize in Apple II archival:**
- **AppleSauce** - https://applesaucefdc.com/
- **Rescue My Floppies** - Various services online
- **Internet Archive** - Will archive and preserve

**Cost:** ~$5-10 per disk
**Worth it if:** Rare disks, large collection, limited time

### Option 3: Focus on Good Disks First

**Strategy:**
1. Archive all disks that read easily (70-80% usually work)
2. Set aside problematic disks
3. Later: acquire Apple Disk II or send to service
4. Complete archive with native drive

**Advantage:** Get most of collection archived quickly

---

## Disk Condition Assessment

### Grading Your Disks:

**Excellent (95%+ readable on PC drive):**
- No visible damage
- Clean, no oxidation
- Stored properly
- < 5 years old when written

**Good (80%+ readable on PC drive):**
- Minor wear
- Light oxidation on hub
- May need extra retries
- 5-15 years old

**Fair (50%+ readable on PC drive):**
- Visible wear
- Hub oxidation
- Label damage
- 15-25 years old
- May need native Apple drive

**Poor (< 50% readable on PC drive):**
- Heavy wear/damage
- Severe oxidation
- Sticky/degraded oxide
- 25+ years old
- Definitely need native drive or service

**For Print Shop/Toy Shop:**
- 1984-1986 vintage
- Likely "Fair" to "Good" condition
- Should read with extended retries on SD-800
- If fail: consider native drive

---

## Success Rate Expectations

### Realistic Expectations with SD-800:

| Disk Condition | SD-800 Success Rate | Native Disk II Success Rate |
|----------------|---------------------|----------------------------|
| Excellent | 95-100% | 99-100% |
| Good | 80-90% | 95-99% |
| Fair | 50-70% | 80-95% |
| Poor | 20-40% | 60-80% |

**Print Shop/Toy Shop (1984):**
- Expected condition: Fair to Good
- Expected SD-800 success: 60-80%
- With retries/optimization: 70-90%

---

## Decision Tree

```
Can you read ANY Apple II disk?
│
├─ NO
│  ├─ Check power connection
│  ├─ Check cable seating
│  ├─ Update Greaseweazle firmware
│  └─ Try known-good PC disk (test drive works)
│
└─ YES
   │
   Can you read MOST disks (>70%)?
   │
   ├─ YES → SD-800 is working well, continue
   │  └─ For failing disks:
   │     ├─ Try extended retries
   │     ├─ Clean heads
   │     └─ Set aside for later (maybe get Disk II)
   │
   └─ NO (< 70% success)
      │
      ├─ Clean heads thoroughly
      ├─ Try optimal settings (above)
      ├─ Test with known-good disk from friend
      │
      └─ Still < 70%?
         ├─ Consider drive alignment issue
         ├─ Try different PC drive if available
         └─ Plan to acquire Apple Disk II drive
```

---

## Getting Help

### When to Ask for Help:

1. **Drive not detected** after checking all connections
2. **Consistent read failures** across all disks
3. **Unusual error messages** not covered here
4. **Success rate < 30%** with good condition disks

### Where to Get Help:

**Communities:**
- **AppleSqueezer Forum** - https://www.applefritter.com/
  - Disk preservation experts
  - Very helpful with troubleshooting

- **/r/apple2 Reddit** - https://reddit.com/r/apple2
  - Active community
  - Quick responses

- **Greaseweazle Discord** - Link in GitHub wiki
  - Direct support from keirf (creator)
  - Hardware troubleshooting

**When posting for help, include:**
1. Greaseweazle version (`gw --version`)
2. Drive model (Epson SD-800)
3. Exact error message
4. Command you're using
5. Disk condition (if known)
6. What you've tried already

---

## Reference Commands

### Minimal (Fast, Good Disks)
```bash
gw read --drive A: --format apple2.140 disk.scp
```

### Standard (Most Disks)
```bash
gw read --drive A: --format apple2.140 \
    --retries 10 \
    disk.scp
```

### Optimal for SD-800
```bash
gw read --drive A: --format apple2.140 \
    --tracks 0-34 \
    --step-rate 6ms \
    --settle-time 20ms \
    --retries 10 \
    --rpm-range 295-305 \
    disk.scp
```

### Maximum Effort (Marginal Disks)
```bash
gw read --drive A: --format apple2.140 \
    --tracks 0-34 \
    --step-rate 8ms \
    --settle-time 40ms \
    --retries 50 \
    --rpm-range 290-310 \
    disk.scp
```

### Diagnostic (Single Track Test)
```bash
gw read --drive A: --format apple2.140 \
    --tracks 17-17 \
    --revs 5 \
    test.scp
```

---

## Bottom Line

**The SD-800 will work for most disks**, but:
- Expect 70-80% success rate
- Some disks will need native Apple drive
- Clean heads regularly
- Use extended retries for marginal disks
- Don't give up if first attempt fails!

**For Print Shop/Toy Shop:**
- Try with optimal SD-800 settings first
- If fails after 2-3 attempts with different settings
- Set aside and continue with other disks
- Can revisit with Apple Disk II later if needed

Good luck! 🍎💾

---

**Created:** 2026-01-19
**For:** Apple II Disk Archival with Epson SD-800
**Hardware:** Greaseweazle V4.1 + Epson SD-800
