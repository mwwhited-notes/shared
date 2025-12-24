# Analog Computing Research Protocol

## Purpose
This document outlines the protocol for finding and archiving analog computing resources, including application notes, datasheets, aerospace simulations, and hardware documentation.

## Primary Sources

### 1. NASA Technical Reports Server (NTRS)
- **URL**: https://ntrs.nasa.gov/
- **Best for**: Flight simulation, spacecraft guidance, aerospace analog computing
- **Search tips**: Use terms like "analog computer", "simulation equations", "hybrid computer"

### 2. Defense Technical Information Center (DTIC)
- **URL**: https://apps.dtic.mil/
- **Best for**: Military fire control, missile guidance, ballistic trajectory
- **Note**: Some direct downloads blocked; use archive.org mirrors

### 3. Internet Archive
- **URL**: https://archive.org/
- **Best for**: Historical manuals, DTIC mirrors, vintage documentation
- **Search tips**: Include "PDF" in searches for downloadable documents

### 4. Bitsavers
- **URL**: https://bitsavers.org/pdf/
- **Best for**: EAI, Systron-Donner, and other vintage analog computer manuals
- **Key directories**: /eai/, /systronDonner/, /generalPrecision/

### 5. Maritime.org
- **URL**: https://maritime.org/doc/
- **Best for**: Navy fire control computers, OP manuals
- **Key documents**: OP 1140, Fire Control Fundamentals

### 6. Computer History Museum
- **URL**: https://s3data.computerhistory.org/brochures/
- **Best for**: EAI brochures, analog computer marketing materials

### 7. Anabrid / Analog Paradigm
- **URL**: https://analogparadigm.com/documentation.html
- **URL**: https://the-analog-thing.org/
- **Best for**: Modern analog computing, THAT documentation, ALPACA notes

### 8. Texas Instruments
- **URL**: https://www.ti.com/lit/
- **Best for**: Op-amp application notes, integrators, differentiators

### 9. Analog Devices
- **URL**: https://www.analog.com/en/resources/
- **Best for**: Multipliers (AD633), precision amplifiers, tutorials (MT/AN series)

### 10. RadioNerds
- **URL**: https://radionerds.com/
- **Best for**: Military radio and radar technical manuals

### 11. University Sources
- **Cambridge**: cl.cam.ac.uk/techreports/ - INS, technical reports
- **MSU/Stanford/Oxford/Northeastern**: ECG circuit design labs
- **ICTP**: indico.ictp.it - Conference materials
- **Roberto Merletti**: robertomerletti.it - EMG tutorials

### 12. Specialized Sources
- **JHUAPL**: secwww.jhuapl.edu/techdigest/ - Sonar, missiles
- **IAEA**: www-pub.iaea.org - Nuclear reactor simulators
- **USGS**: pubs.usgs.gov - Petroleum modeling
- **Moog Foundation**: moogfoundation.org - Music synthesis history

---

## Search Strategies by Topic

### Aerospace/Flight Simulation
1. Search NTRS with: "analog simulation" + aircraft type or program name
2. Look for NASA TN, TM, CR document types
3. Include decade terms: 1960s, 1970s for vintage analog work

### Fire Control/Military
1. Check maritime.org for Navy ordnance pamphlets (OP documents)
2. Search archive.org for DTIC documents (ADA/AD numbers)
3. Look for specific systems: M9 director, SCR-584, Mark series

### Specific Analog Computers
1. Bitsavers for manufacturer documentation
2. Archive.org for scanned manuals
3. Analog Museum (analogmuseum.org) for specifications

### Application Notes
1. TI application notes (SBOA, SLOA, SNOA series)
2. ADI tutorials (MT series, AN series)
3. Anabrid ALPACA series (alpaca_1 through alpaca_54+)

### Biomedical Signal Processing
1. University course materials (MSU, Stanford, Oxford, Northeastern)
2. Roberto Merletti's publications for EMG
3. Analog Devices datasheets (AD8232 for ECG)
4. Kaiser/Premera medical policies for IONM

### Acoustic/Sonar Processing
1. JHUAPL Technical Digest
2. InTech Open publications
3. Acoustics Today journal

### Seismology/Earthquake
1. Vibrationdata.com tutorials
2. AEES conference materials
3. USGS earthquake hazards

### Radar Signal Processing
1. MIT Lincoln Laboratory
2. RECW academic materials
3. Radar tutorial sites

### Historical Computing
1. UCL Discovery for Nature papers (Antikythera)
2. ArXiv for reconstruction papers
3. ASME for engineering landmarks
4. Copernicus journals for history of science
5. Moog Foundation for music synthesis history

### Music Synthesis
1. Moog Foundation archives
2. AES historical papers
3. Buchla documentation

---

## Download Methods

### Primary Method (curl)
```bash
curl -L -o "output-name.pdf" "URL" 2>/dev/null
```

### Fallback Method (wget)
```bash
wget --user-agent="Mozilla/5.0" -O "output-name.pdf" "URL"
```

### For SSL Issues
```bash
wget --no-check-certificate -O "output-name.pdf" "URL"
```

---

## File Naming Convention
- Use lowercase with hyphens
- Include source prefix: ntrs-, dtic-, bitsavers-, adi-, ti-, etc.
- Be descriptive: `ntrs-apollo-guidance-navigation.pdf`

---

## Folder Structure

```
analog-computing-repository/
├── 09-datasheets/pdfs/               # Component datasheets
├── 10-application-notes/pdfs/        # Organized by category:
│   ├── acoustic-sonar/               # Sonar signal processing
│   ├── adi-appnotes/                 # Analog Devices tutorials (MT/AN series)
│   ├── anabrid-alpaca/               # ALPACA application notes
│   ├── biomedical/                   # ECG, EEG, EMG, IONM
│   ├── discrete-circuits/            # DIY op-amps, nonlinear circuits
│   ├── educational/                  # Course materials, getting started
│   ├── historical-computing/         # Antikythera, differential analyzer, perceptron
│   ├── music-synthesis/              # Moog, VCO, audio synthesis
│   ├── petroleum/                    # Reservoir simulation
│   ├── process-control/              # PID, dynamometer
│   ├── radar/                        # MTI, pulse Doppler
│   ├── seismology/                   # Earthquake instrumentation
│   ├── sensors/                      # Photodiodes, gas sensors
│   └── ti-appnotes/                  # Texas Instruments app notes
├── 11-aerospace-simulation/pdfs/     # Organized by category:
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
└── 12-analog-computer-docs/          # By manufacturer:
    ├── anabrid-that/
    ├── beckman/
    ├── comdyna-gp6/
    ├── diy-homebrew/
    ├── donner-computers/
    ├── eai-computers/
    ├── general-reference/
    ├── heathkit-ec1/
    ├── systron-donner/
    └── telefunken/
```

---

## Quality Checks
1. Verify file size > 1KB (failed downloads are often tiny HTML error pages)
2. Use `file *.pdf` to verify actual PDF format
3. Remove failed/empty downloads immediately

---

## Regular Updates
- Check Anabrid for new ALPACA application notes
- Monitor NTRS for newly digitized historical documents
- Check bitsavers for new uploads in analog computer directories
- Search ResearchGate and Academia.edu for new papers
