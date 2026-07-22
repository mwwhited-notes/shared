# Reclaimed-Cell USB-C PD Pack - Parts List (BOM)

Layout (S/P) not yet finalized — cell sorting must happen first (see [README.md](README.md)).
Items below are flexible multi-S picks that work across 2S-4S; once the matched-group yield is
known, BMS and boost module choices narrow to exact part numbers/wattage.

## Boards / ICs

| Item | Qty | Notes |
|------|-----|-------|
| Multi-S BMS board (2S-4S selectable) | 2-3 | Buy for max possible S count (4S) — works fine on 2S/3S too |
| 100W-class PD boost module (SW3518 / CH224K-based) | 2 | Designed for multi-cell pack input, outputs real PD up to 20V |
| USB-C PD trigger board (standalone) | 1 | Bench-test voltage negotiation independent of the boost module |

## Cell Testing & Sorting

*Do this before buying pack hardware.*

| Item | Qty | Notes |
|------|-----|-------|
| Programmable DC electronic load (ATORCH DL24/DL24P, Makerhawk, or Riden-style) | 1 | **Key gap — not currently owned.** Needed for constant-current discharge testing (mAh, cutoff voltage) and later load-testing the finished pack's PD output. A USB-input model (DL24P) rated ~20V/5A covers both. |
| Internal-resistance-capable tester | 1 | Check if the chosen e-load reports IR (mΩ) directly before buying a separate device |
| Battery holders (single-cell) | qty = cell count | Test cells individually before committing to spot welds |
| Li-ion safe charging/storage bag | 1-2 | While sorting a pile of unknown-condition cells |

**Budget alternative to a real e-load:** known-value power resistors (sized for ~0.5-1A draw) +
existing multimeter + a timer, discharging each cell and calculating mAh by hand. Slower/less
precise, and won't help with later load-testing the finished pack's PD output.

## Battery Assembly

| Item | Qty | Notes |
|------|-----|-------|
| Spot welder (18650-capable) | 1 | Preferred over soldering directly to cell tops |
| Nickel strip (0.15-0.2mm, pure nickel) | 1-2 rolls | Spot welding series/parallel links |
| JST-XH balance connector + housing kit | 1 kit | BMS balance leads once S >= 2 |
| Fish paper / battery wrap insulation | 1 roll | Between series groups |
| Kapton tape | 1 roll | Insulation at weld points |

## Wiring / Assembly (General)

| Item | Qty | Notes |
|------|-----|-------|
| Silicone wire, mixed 18-22AWG | 1 roll each | Heavier gauge for main pack leads |
| Heat shrink assortment | 1 kit | |
| Perfboard or project box / 3D printed case | as needed | Housing per pack |

## Test & Measurement

| Item | Qty | Notes |
|------|-----|-------|
| USB-C cable rated for target wattage | 1-2 | Cheap cables can bottleneck current even if module and load are fine |

## On Hand vs. Need to Purchase

- Already have: multimeter, bench power supplies (see [Test Equipment inventory](../../.personal/incoming/test-equipment.md))
- Need to buy: electronic load (key gap), multi-S BMS boards, PD boost modules, PD trigger board,
  spot welder, nickel strip, JST-XH kit, fish paper, Kapton tape

---

*Last updated: 2026-07-22*
