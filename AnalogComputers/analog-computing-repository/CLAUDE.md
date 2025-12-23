# Claude Code Project Guide - Analog Computing Repository

## Project Overview

A comprehensive collection of documents, research, and training materials on analog computers, with primary focus on electronic analog computers using operational amplifier-based elements.

**Current Size**: ~232 PDFs, ~660MB total

## Repository Structure

```
analog-computing-repository/
├── 01-fundamentals/          # Introduction, op-amp basics, analog vs digital
├── 02-components/            # Summers, integrators, multipliers, etc.
├── 03-mathematics/           # ODEs, PDEs, linear algebra operations
├── 04-applications/          # Control systems, physics, signal processing
├── 05-historical/            # Mechanical computers, early electronic, hybrid
├── 06-modern-systems/        # THAT, modern op-amps, DIY projects
├── 07-tutorials/             # Hands-on exercises
├── 08-references/            # Glossary, symbols, bibliography
├── 09-datasheets/pdfs/       # Component datasheets (~20 PDFs)
├── 10-application-notes/pdfs/ # TI, ADI, Anabrid app notes (160 PDFs, 253MB)
├── 11-aerospace-simulation/pdfs/  # NASA, military, navigation (53 PDFs, 234MB)
│   ├── aircraft-simulation/
│   ├── apollo-saturn/
│   ├── celestial-navigation/
│   ├── fire-control/
│   ├── helicopter-vtol/
│   ├── hybrid-computing/
│   ├── inertial-navigation/
│   ├── missile-guidance/
│   ├── nasa-history/
│   ├── orbital-mechanics/
│   ├── practical-applications/
│   ├── reentry-vehicles/
│   └── space-shuttle/
├── 12-analog-computer-docs/  # Computer-specific manuals (19 PDFs, 152MB)
│   ├── anabrid-that/
│   ├── beckman/
│   ├── comdyna-gp6/
│   ├── diy-homebrew/
│   ├── donner-computers/
│   ├── eai-computers/
│   ├── general-reference/
│   ├── heathkit-ec1/
│   ├── systron-donner/
│   └── telefunken/
├── download-sources.md       # Registry of all download sources
├── research-protocol.md      # Search strategies and methods
└── sync.bat                  # Windows script to sync PDFs to OneDrive
```

## Key Files

- **download-sources.md**: Comprehensive list of all sources used for PDF downloads, with URL patterns and search strategies
- **research-protocol.md**: Protocol for finding analog computing resources
- **sync.bat**: Windows batch file for syncing PDFs to OneDrive

## PDF Categories

### Application Notes (10-application-notes/pdfs/)
- Anabrid ALPACA series (analog computing examples)
- Texas Instruments op-amp and sensor app notes
- Analog Devices multipliers, instrumentation amps
- Biomedical signal processing (ECG, EEG, EMG, IONM)
- Historical computing (Antikythera, tide machines, perceptron)
- Music synthesis (Moog voltage-controlled modules)
- Process control and PID
- Sonar/acoustic processing
- Seismology instrumentation

### Aerospace Simulation (11-aerospace-simulation/pdfs/)
- NASA flight simulation history
- Apollo/Saturn guidance systems
- Space Shuttle GNC
- Missile guidance and fire control
- Inertial and celestial navigation
- Reentry vehicle dynamics
- Nuclear reactor simulation
- Weather prediction (ENIAC)
- Tidal harmonic analysis

### Analog Computer Docs (12-analog-computer-docs/)
- EAI PACE computers (TR-10, TR-48, 231R)
- Comdyna GP-6
- Systron-Donner handbooks
- Heathkit EC-1
- Donner 3500
- Anabrid THAT (modern)
- DIY/homebrew resources

## Primary Download Sources

1. **NASA NTRS** (ntrs.nasa.gov) - Flight simulation, spacecraft guidance
2. **Bitsavers** (bitsavers.org/pdf/) - Vintage computer manuals
3. **Archive.org** - DTIC mirrors, historical documents
4. **Maritime.org** - Navy fire control manuals
5. **Analog Museum** (analogmuseum.org) - Vintage analog computer docs
6. **Computer History Museum** - Brochures and marketing materials
7. **Texas Instruments** (ti.com/lit/) - Op-amp application notes
8. **Analog Devices** (analog.com) - Multipliers, precision amps

## Download Commands

```bash
# Standard download
curl -L -o "filename.pdf" "URL" 2>/dev/null

# With user-agent (for archive.org)
wget --user-agent="Mozilla/5.0" -O "filename.pdf" "URL"

# For SSL issues
wget --no-check-certificate -O "filename.pdf" "URL"
```

## File Naming Convention

- Use lowercase with hyphens
- Include source prefix: `ntrs-`, `dtic-`, `bitsavers-`, `adi-`, `ti-`, etc.
- Be descriptive: `ntrs-apollo-guidance-navigation.pdf`

## Quality Checks

1. Verify file size > 1KB (failed downloads are often tiny HTML error pages)
2. Use `file *.pdf` to verify actual PDF format
3. Remove failed/empty downloads immediately

## Common Issues

- **DTIC direct downloads blocked (403)**: Use archive.org mirrors
- **Caltech SSL issues**: Use `wget --no-check-certificate`
- **Small files (< 1KB)**: Usually HTML error pages, delete and retry

## Topics Covered

- Analog computing fundamentals
- Op-amp circuit design
- Differential equations (ODEs, PDEs)
- Flight simulation and aerospace
- Fire control computers (WWII era)
- Guidance systems (Apollo, Saturn, Shuttle)
- Inertial and celestial navigation
- Biomedical signal processing
- Music synthesis (Moog, Buchla)
- Historical computing (differential analyzer, ENIAC, perceptron)
- Modern analog computing (THAT, DIY projects)

## When Adding New PDFs

1. Check `download-sources.md` for existing sources
2. Follow the file naming convention
3. Place in appropriate category folder
4. Update the relevant README.md with new entries
5. Add new sources to `download-sources.md`
