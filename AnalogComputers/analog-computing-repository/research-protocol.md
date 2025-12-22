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
- **Best for**: Multipliers (AD633), precision amplifiers, tutorials

### 10. RadioNerds
- **URL**: https://radionerds.com/
- **Best for**: Military radio and radar technical manuals

## Search Strategies

### For Aerospace/Flight Simulation
1. Search NTRS with: "analog simulation" + aircraft type or program name
2. Look for NASA TN (Technical Note), NASA TM (Technical Memorandum), NASA CR (Contractor Report)
3. Include decade terms: 1960s, 1970s for vintage analog work

### For Fire Control/Military
1. Check maritime.org for Navy ordnance pamphlets (OP documents)
2. Search archive.org for DTIC documents (ADA/AD numbers)
3. Look for specific systems: M9 director, SCR-584, Mark series

### For Specific Analog Computers
1. Bitsavers for manufacturer documentation
2. Archive.org for scanned manuals
3. Analog Museum (analogmuseum.org) for specifications

### For Application Notes
1. TI application notes (SBOA, SLOA, SNOA series)
2. ADI tutorials (MT series, AN series)
3. Anabrid ALPACA series (alpaca_1 through alpaca_54+)

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

## File Naming Convention
- Use lowercase with hyphens
- Include source prefix: ntrs-, dtic-, bitsavers-, etc.
- Be descriptive: `ntrs-apollo-guidance-navigation.pdf`

## Folder Structure
```
analog-computing-repository/
├── 09-datasheets/pdfs/           # Component datasheets
├── 10-application-notes/pdfs/     # TI, ADI, Anabrid app notes
├── 11-aerospace-simulation/pdfs/  # NASA, DTIC flight/missile docs
└── 12-analog-computer-docs/pdfs/  # Specific computer documentation
```

## Quality Checks
1. Verify file size > 1KB (failed downloads are often tiny)
2. Check PDF opens correctly
3. Remove failed/empty downloads immediately

## Regular Updates
- Check Anabrid for new ALPACA application notes
- Monitor NTRS for newly digitized historical documents
- Check bitsavers for new uploads in analog computer directories
