# Claude Code Project Guide - Analog Computing Repository

## Quick Start for Resuming Sessions

When resuming work on this repository:

1. **Read this file first** for context
2. **Check `download-sources.md`** for existing sources and what's been downloaded
3. **Check `research-protocol.md`** for search strategies by topic
4. **Use the folder structure below** to place new downloads correctly

## Current Repository Stats

- **Total PDFs**: ~232 files
- **Total Size**: ~660MB
- **Application Notes**: 159 PDFs in 14 subfolders (253MB)
- **Aerospace Simulation**: 53 PDFs in 13 subfolders (234MB)
- **Analog Computer Docs**: 21 PDFs by manufacturer (152MB)

---

## Repository Structure

```
analog-computing-repository/
├── CLAUDE.md                         # THIS FILE - project guide
├── README.md                         # Main repo overview
├── research-protocol.md              # Search strategies and sources
├── download-sources.md               # Registry of all download sources
├── sync.bat                          # Windows sync to OneDrive
│
├── 01-fundamentals/                  # Introduction, op-amp basics
├── 02-components/                    # Summers, integrators, multipliers
├── 03-mathematics/                   # ODEs, PDEs, linear algebra
├── 04-applications/                  # Control systems, physics
├── 05-historical/                    # Mechanical computers, early electronic
├── 06-modern-systems/                # THAT, modern op-amps, DIY
├── 07-tutorials/                     # Hands-on exercises
├── 08-references/                    # Glossary, symbols, bibliography
│
├── 09-datasheets/pdfs/               # Component datasheets
│
├── 10-application-notes/pdfs/        # 159 PDFs organized by category:
│   ├── acoustic-sonar/       (3)     # Sonar signal processing
│   ├── adi-appnotes/         (39)    # Analog Devices MT/AN series
│   ├── anabrid-alpaca/       (37)    # ALPACA application notes
│   ├── biomedical/           (9)     # ECG, EEG, EMG, IONM
│   ├── discrete-circuits/    (25)    # DIY op-amps, nonlinear circuits
│   ├── educational/          (4)     # Course materials
│   ├── historical-computing/ (11)    # Antikythera, perceptron, etc.
│   ├── music-synthesis/      (1)     # Moog, VCO
│   ├── petroleum/            (1)     # Reservoir simulation
│   ├── process-control/      (3)     # PID, dynamometer
│   ├── radar/                (1)     # MTI, pulse Doppler
│   ├── seismology/           (2)     # Earthquake instrumentation
│   ├── sensors/              (4)     # Photodiodes, gas sensors
│   └── ti-appnotes/          (19)    # Texas Instruments app notes
│
├── 11-aerospace-simulation/pdfs/     # 53 PDFs organized by category:
│   ├── aircraft-simulation/  (8)
│   ├── apollo-saturn/        (7)
│   ├── celestial-navigation/ (3)
│   ├── fire-control/         (6)
│   ├── helicopter-vtol/      (3)
│   ├── hybrid-computing/     (6)
│   ├── inertial-navigation/  (2)
│   ├── missile-guidance/     (3)
│   ├── nasa-history/         (2)
│   ├── orbital-mechanics/    (2)
│   ├── practical-applications/ (5)
│   ├── reentry-vehicles/     (4)
│   └── space-shuttle/        (2)
│
└── 12-analog-computer-docs/          # 21 PDFs by manufacturer:
    ├── anabrid-that/
    ├── beckman/
    ├── comdyna-gp6/
    ├── diy-homebrew/
    ├── donner-computers/
    ├── eai-computers/                # TR-10, TR-48, 231R manuals
    ├── general-reference/
    ├── heathkit-ec1/
    ├── systron-donner/
    └── telefunken/
```

---

## Primary Download Sources

| Source | URL | Best For |
|--------|-----|----------|
| NASA NTRS | ntrs.nasa.gov | Flight simulation, spacecraft guidance |
| Bitsavers | bitsavers.org/pdf/ | Vintage computer manuals (EAI, Systron-Donner) |
| Archive.org | archive.org | DTIC mirrors, historical documents |
| Maritime.org | maritime.org/doc/ | Navy fire control manuals |
| Analog Museum | analogmuseum.org | Vintage analog computer specs |
| Computer History Museum | s3data.computerhistory.org/brochures/ | EAI brochures |
| Texas Instruments | ti.com/lit/ | Op-amp application notes |
| Analog Devices | analog.com/en/resources/ | Multipliers, precision amps, tutorials |
| Anabrid | analogparadigm.com | THAT docs, ALPACA notes |
| JHUAPL | secwww.jhuapl.edu/techdigest/ | Sonar, missiles |
| Moog Foundation | moogfoundation.org | Music synthesis history |

---

## Download Commands

```bash
# Standard download
curl -L -o "filename.pdf" "URL" 2>/dev/null

# With user-agent (for archive.org, some blocked sites)
wget --user-agent="Mozilla/5.0" -O "filename.pdf" "URL"

# For SSL certificate issues
wget --no-check-certificate -O "filename.pdf" "URL"
```

---

## File Naming Convention

- Lowercase with hyphens
- Source prefix: `ntrs-`, `dtic-`, `bitsavers-`, `adi-`, `ti-`, `moog-`, etc.
- Descriptive: `ntrs-apollo-guidance-navigation.pdf`

---

## Quality Checks

1. **Verify file size** > 1KB (failed downloads are often tiny HTML error pages)
2. **Check file type**: `file *.pdf` to verify actual PDF format
3. **Remove failed downloads** immediately

---

## Topics Already Covered

### Well-Covered (many PDFs)
- ALPACA analog computing examples (37 files)
- ADI tutorials and app notes (39 files)
- TI op-amp app notes (19 files)
- Discrete circuit design (25 files)
- Apollo/Saturn guidance (7 files)
- Fire control systems (6 files)
- Biomedical signal processing (9 files)
- Historical computing (11 files)

### Lightly Covered (need more)
- Music synthesis (1 file) - search Moog, Buchla, AES
- Petroleum simulation (1 file) - search SPE, reservoir
- Radar MTI (1 file) - search MIT Lincoln Lab
- Seismology (2 files) - search USGS, IRIS
- Process control (3 files) - search ISA, PID

### Not Yet Covered (future searches)
- HVAC control systems
- Automotive engine simulation
- Power grid simulation
- Chemical process control
- Oceanographic instrumentation
- Weather prediction (beyond ENIAC history)

---

## Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| DTIC 403 Forbidden | Use archive.org mirrors |
| Caltech SSL errors | Use `wget --no-check-certificate` |
| Small files (< 1KB) | HTML error page, delete and retry |
| ADI curl fails (exit 92) | Use wget with user-agent |
| ResearchGate paywall | Search for title on other sources |

---

## When Adding New PDFs

1. Check `download-sources.md` for existing sources
2. Follow file naming convention
3. Place in correct category subfolder
4. Update subfolder counts in this file
5. Add new sources to `download-sources.md`

---

## Sync to OneDrive (Windows)

Run `sync.bat` to copy PDFs to OneDrive:
```batch
ROBOCOPY "folder" "target" *.pdf /MIR /S
```

---

## Key Reference Documents

- **TI Handbook of Op-Amp Applications** (sboa092b.pdf) - Comprehensive op-amp guide
- **ADI Multiplier App Guide** (adi-multiplier-app-guide.pdf) - AD633/AD534 applications
- **EAI Handbook of Analog Computation** - Classic analog computing reference
- **NASA Black Magic and Gremlins** - History of analog flight simulation
- **Moog 1964 AES Paper** - Foundation of voltage-controlled synthesis
