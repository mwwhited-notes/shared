# NESMaker Compatible NES PCB

**Homebrew NES Cartridge PCB**

## Unit Information

| Field | Value |
|-------|-------|
| Manufacturer | mrTentacle (Sweden) |
| Type | NES Cartridge PCB |
| Compatibility | NESMaker |
| Condition | New |

## Specifications

| Specification | Value |
|--------------|-------|
| Mapper | UNROM-compatible |
| PRG ROM | 512 KB (39SF040/29F040) |
| CHR RAM | 8 KB (6264) |
| Flash Package | PLCC or DIP |

## Required Components

| Component | Part Number | Quantity |
|-----------|-------------|----------|
| Flash ROM | 39SF040 or 29F040 | 1 |
| SRAM | 62256 (256K) | 1 |
| Microcontroller | ATtiny13 | 1 |
| Logic IC | 74LS32 | 2 |
| Logic IC | 74LS139 | 1 |
| Logic IC | 74LS377 | 1 |
| Capacitor | 100nF ceramic | 3 |

## Features

- Compatible with NESMaker programmer
- Accepts standard flash chips (PLCC or DIP)
- Works with INFneslives programmer
- Can also use standard chip programmers
- Low-cost cartridge production

## Programming Options

1. **NESMaker Programmer** (INFneslives) - Direct programming
2. **TL866II Plus** - Flash and ATtiny separately
3. **USBasp** - For ATtiny programming

## ATtiny13 Firmware

The ATtiny13 must be programmed with AVRCiCzz code for mapper emulation.

## Applications

- Publishing NESMaker games as physical cartridges
- Homebrew NES game distribution
- Learning NES hardware
- Retro game development

## Documentation

- [Tindie Product Page](https://www.tindie.com/products/mrtentacle/nesmaker-compatible-nes-pcb/)
- [NESMaker Official Site](https://www.thenew8bitheroes.com/)

## Notes

This is a bare PCB - requires sourcing and soldering all components. Designed for use with games created in NESMaker, a tool for creating homebrew NES games without assembly programming.

## Local Files

*Documentation to be downloaded*

## Revision History

| Date | Change |
|------|--------|
| 2025-12-24 | Initial entry |
