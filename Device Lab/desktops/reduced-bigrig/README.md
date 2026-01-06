# Reduced BigRig

**AMD FX-9590 gaming rig with dual R9 290 GPUs - older high-performance build**

## Device Information

| Field | Value |
|-------|-------|
| Build Name | Reduced BigRig |
| Platform | AMD AM3+ |
| Year Built | ~2014-2015 era |
| Date Acquired | TBD |
| Condition | Working |
| Current Use | **Project: [DevOps Playground](../../projects/docker-cluster.md)** |

## Specifications

| Component | Model | Notes |
|-----------|-------|-------|
| CPU | AMD FX-9590 | 4.7GHz 8-core, 220W TDP |
| CPU Cooler | ARCTIC Freezer A11 | 74 CFM |
| Motherboard | ASRock 990FX Extreme9 | ATX AM3+ |
| RAM | Corsair Vengeance Pro 32GB | 4x8GB DDR3-1866 CL9 |
| Storage | 2x Seagate BarraCuda 500GB | 3.5" 7200 RPM |
| Storage | 2x Samsung 840 Evo 250GB | 2.5" SSD |
| GPU | 2x Asus DirectCU II R9 290 | 4GB each, CrossFire |
| Case | Corsair Carbide 300R | ATX Mid Tower |
| PSU | Antec High Current Gamer 750W | 80+ Bronze |
| Optical | LG WH14NS40 | Blu-Ray/DVD/CD Writer |
| WiFi | Rosewill RNX-N150PCe | 802.11a/b/g/n |
| OS | Windows 10 Pro | OEM 64-bit |

## Power Considerations

| Metric | Value |
|--------|-------|
| Estimated Draw | ~926W |
| PSU Capacity | 750W |
| Status | **Underpowered** - may need PSU upgrade |

The FX-9590 alone has a 220W TDP, and dual R9 290s can draw 250W+ each under load.

## Hackability

### Current Status

| Aspect | Status |
|--------|--------|
| BIOS Access | Full |
| OS Install | Any |
| Overclocking | Limited (already at max TDP) |
| Hardware Mods | Full access |

### Hackability Rating: ★★★★★

Standard desktop - full control.

### Potential Uses

| Use Case | Feasibility | Notes |
|----------|-------------|-------|
| Linux workstation | Good | Well-supported hardware |
| VM host | Limited | 32GB RAM, older CPU |
| NAS/Storage server | Good | Multiple drive bays |
| Retro gaming | Excellent | Era-appropriate for 2014 titles |
| Compute/rendering | Limited | Old architecture, high power |

## Project Ideas

- [ ] Linux server conversion
- [ ] GPU mining rig (historical interest only)
- [ ] Retro gaming station (2010s era games)
- [ ] Parts donor for other projects
- [ ] Upgrade PSU to 1000W+ for stability

## Known Issues

1. **PSU undersized** - 750W for ~926W estimated load
2. **High power consumption** - FX-9590 is notoriously power-hungry
3. **Heat output** - Requires good cooling and ventilation
4. **Aging platform** - AM3+ is end-of-life, no upgrade path

## Documentation

### PCPartPicker
- [Reduced BigRig Build](https://pcpartpicker.com/user/mwwhited/saved/qD4Pxr)

## Local Files

*None yet*

## Notes

- This is an older high-end build from the AMD FX era
- The FX-9590 was AMD's highest-clocked consumer CPU at the time
- Dual R9 290s in CrossFire was a powerful GPU setup for its era
- Consider upgrading PSU if still in active use
- May be worth more as parts than as a complete system
