# Velleman K8200 3D Printer

**RepRap-based 3D Printer Kit (Heavily Modified)**

## Unit Information

| Field | Value |
|-------|-------|
| Manufacturer | Velleman |
| Model | K8200 |
| Type | 3D Printer / CNC |
| Controller | Duet 3 + Raspberry Pi (upgraded) |
| Condition | Working |

## Original Specifications

| Specification | Value |
|--------------|-------|
| Build Volume | 200 x 200 x 200 mm |
| Filament Diameter | 3 mm (originally) |
| Materials | PLA, ABS |
| Heated Bed | Yes |
| Frame | Aluminum extrusion |
| Original Firmware | Repetier |

## Upgrades & Modifications

### Controller Upgrade: Duet 3

| Component | Details |
|-----------|---------|
| Controller | Duet 3 Mainboard |
| SBC | Raspberry Pi |
| Firmware | RepRapFirmware |
| Interface | Duet Web Control |

### Multi-Tool / Multi-Head

- Multiple tool heads supported
- Tool changing capability via Duet 3 firmware

### Multi-Filament Support

- Multiple filament sizes supported
- Not limited to original 3mm specification

### Custom Modifications

See [MyMashedDuet](https://github.com/mwwhited/MyMashedDuet) repository for:
- Custom control circuits
- Duet 3 configuration backup
- G-code scripts and macros
- Tool definitions and offsets
- Utility tools for Duet workflow

## Features

- Open-source RepRap design (fully customizable)
- Aluminum frame construction
- Heated print bed
- Upgraded to modern 32-bit controller
- Web-based control interface (Duet Web Control)
- CNC capability with modifications

## Applications

- Prototype enclosures
- Custom brackets and mounts
- Replacement parts for vintage computers
- Test fixtures and jigs
- Cable management parts

## Documentation

- [Velleman K8200 Product Page](https://www.velleman.eu/products/view/3d-printer-k8200/?id=412554)
- [MyMashedDuet Configuration](https://github.com/mwwhited/MyMashedDuet)
- [Duet 3 Documentation](https://docs.duet3d.com/)
- [RepRapFirmware G-code Reference](https://docs.duet3d.com/en/User_manual/Reference/Gcodes)

## Notes

Originally a kit printer, now heavily customized with a Duet 3 controller replacing the original electronics. The Duet 3 provides modern features like web control, better stepper drivers, and RepRapFirmware compatibility.

## Local Files

*Configuration synced from GitHub repository*

## Revision History

| Date | Change |
|------|--------|
| 2025-12-24 | Initial entry |
