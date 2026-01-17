# Personal Request: Test Equipment Inventory

## What We Need

Current inventory of test and measurement equipment from Personal/Test Equipment collection.

## Use Case

`workshop-capabilities.md` documents available test equipment and their capabilities. This information is critical for:
- Equipment summary section (oscilloscopes, multimeters, power supplies, etc.)
- Project planning and equipment requirements
- Troubleshooting guides that reference specific equipment
- Cross-referencing projects to available measurement capabilities

## Information to Extract From Personal/Test Equipment/

For each piece of test equipment, provide:

### Test & Measurement Equipment
- Equipment name and model
- Key specifications (bandwidth, resolution, sample rate, range, etc.)
- Primary capabilities/use cases
- Current status (Active/Shelved/Project/Parts)
- Integration notes (USB, GPIB, serial, Ethernet interfaces)
- Related projects that use this equipment

### Categories Needed

1. **Oscilloscopes** - Frequency range, sample rate, channels, probes
2. **Multimeters** - Resolution (digit count), input impedance, measurement types
3. **LCR Meters** - Frequency range, accuracy, measurement types
4. **Logic Analyzers** - Channel count, sample rate, protocol support
5. **Power Supplies** - Voltage/current ratings, regulation accuracy, channels
6. **Thermal Equipment** - Resolution, temperature range, imaging capability
7. **Microscopes** - Magnification range, lighting, imaging capability
8. **Signal Generators** - Frequency range, waveform types, output capability
9. **Programmers** - Device types supported (AVR, PIC, GAL, FPGA, etc.)
10. **Other Equipment** - Any other test/measurement tools

## Format Requested

Markdown table by category:

**Oscilloscopes**
| Model | Bandwidth | Sample Rate | Channels | Status | Projects |
|---|---|---|---|---|---|
| | | | | | |

**Multimeters**
| Model | Resolution | Features | Status | Projects |
|---|---|---|---|---|
| | | | | |

**Power Supplies**
| Model | Voltage Range | Current Rating | Channels | Status | Projects |
|---|---|---|---|---|---|
| | | | | | |

(And similar tables for other categories)

## Cross-Reference Notes

- Which equipment is referenced in specific projects
- Equipment that can be integrated with automation/SCPI
- Any limitations or calibration status
- Peripheral equipment (probes, adapters, cables)

## Response File Location

Place completed inventory at: `personal/incoming/test-equipment.md`
