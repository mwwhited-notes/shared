# KSGER T12 Soldering Station

**STM32-Controlled T12 Soldering Station with FX9501 Handle**

## Unit Information

| Field | Value |
|-------|-------|
| Manufacturer | KSGER |
| Model | T12 STM32 V2.1S |
| Handle | FX9501 |
| Type | Temperature-Controlled Soldering Station |
| Condition | Working |

## Specifications

| Specification | Value |
|--------------|-------|
| Input Voltage | 110-240V AC |
| Output Voltage | 24V DC |
| Power | 75W |
| Temperature Range | 150°C - 480°C |
| Temperature Stability | ±10°C (no load) |
| Heat-up Time | ~8 seconds |
| Controller | STM32 (or MM32 post-2021) |
| Display | OLED |
| Case Size | 130 × 88 × 38mm |
| Case Material | Aluminum alloy |

## Features

- PID temperature control
- OLED display with real-time temperature
- 5 temperature presets
- Per-tip calibration support
- Auto-sleep function
- Quick heating (~8 seconds to working temp)
- Thermocouple cold junction compensation (-9 to 99°C)

## Installed Tips

| Tip | Type | Use Case |
|-----|------|----------|
| JL02 | Bent conical | Drag soldering, tight spaces |
| D24 | Chisel 2.4mm | General purpose |
| K | Knife | Drag soldering, SMD |
| C4 | Bevel 4mm | Large joints, ground planes |
| D52 | Chisel 5.2mm | Large joints, desoldering |
| J02 | Bent chisel | Tight angles |
| KF | Knife fine | Fine pitch SMD |
| KU | Knife | General SMD work |
| C1 | Bevel 1mm | Fine work |
| ILS | Conical long | Through-hole, tight spaces |

## Recommended Temperatures

| Solder Type | Melting Point | Working Temp |
|-------------|---------------|--------------|
| Leaded (Sn63/Pb37) | 183°C | 300-350°C |
| Lead-free (SAC305) | 217-227°C | 350-400°C |

## Documentation

- [KSGER Official Store](https://www.aliexpress.com/store/1486111)

## Software

The STM32 firmware supports:
- Temperature calibration per tip
- Sleep timer configuration
- Power-on defaults
- Display orientation

## Notes

- Tips are Hakko T12-compatible
- FX9501 handle uses silicone cable (heat resistant)
- Post-December 2021 units use MM32 chip (same firmware compatibility)
- Ground the tip to ESD ground when working on sensitive components

## Local Files

*Documentation to be downloaded*

## Revision History

| Date | Change |
|------|--------|
| 2025-12-24 | Initial entry |
