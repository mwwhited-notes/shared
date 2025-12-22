# Download Sources Registry

This document tracks the sources used to download PDFs, organized by reliability and content type.

## Primary Sources (High Success Rate)

### NASA Technical Reports Server (NTRS)
- **Base URL**: `https://ntrs.nasa.gov/`
- **Download Pattern**: `https://ntrs.nasa.gov/api/citations/{ID}/downloads/{ID}.pdf`
- **Content**: Flight simulation, spacecraft guidance, aerospace dynamics, hybrid computing
- **Files Downloaded**:
  - ntrs-analog-hybrid-digital-simulation.pdf (19700002547)
  - ntrs-generalized-engine-simulation.pdf (19740019181)
  - ntrs-flight-dynamics-elastic-aircraft.pdf (19880004717)
  - ntrs-x15-analog-digital-inertial.pdf (19680019932)
  - ntrs-analog-computation-study.pdf (19670009392)
  - ntrs-saturn-v-guidance-control.pdf (19700023342)
  - ntrs-apollo-guidance-navigation.pdf (19720063753)
  - ntrs-lunar-descent-guidance-analog.pdf (19660003940)
  - ntrs-flight-control-block-diagrams.pdf (19750009300)
  - ntrs-apollo-gnc-hardware.pdf (20090016290)
  - ntrs-reentry-vehicle-atmosphere.pdf (19640016000)
  - ntrs-analog-digital-hybrid-computing.pdf (19660003789)
  - ntrs-spacecraft-reentry-simulation.pdf (19770021262)
  - ntrs-reentry-guidance-scheme.pdf (19660015097)
  - ntrs-optimum-reentry-trajectories.pdf (19800007820)
  - ntrs-ch47b-helicopter-simulation.pdf (19850001726)
  - ntrs-single-rotor-helicopter-model.pdf (19830001781)
  - ntrs-vtol-rate-control-simulator.pdf (19720025376)
  - ntrs-shuttle-gnc-equations.pdf (19710023202)
  - ntrs-shuttle-avionics-system.pdf (19900015844)
  - ntrs-lunar-module-navigation.pdf (19670008826)
  - ntrs-lunar-module-docking-sim.pdf (19670017943)
  - ntrs-visual-simulation-lunar.pdf (19660024158)
  - ntrs-dynamic-stability-derivatives.pdf (20040008871)
  - ntrs-nuclear-reactor-simulator.pdf (19670023042)
- **Notes**: Very reliable, direct PDF links work well with curl

### Bitsavers
- **Base URL**: `https://bitsavers.org/pdf/`
- **Alternative**: `http://www.bitsavers.org/pdf/`
- **Content**: Vintage computer manuals, EAI, Systron-Donner, Comdyna
- **Key Directories**:
  - `/eai/` - Electronic Associates Inc computers
  - `/systronDonner/` - Systron-Donner computers
  - `/comdyna/` - Comdyna GP-6
  - `/generalPrecision/` - AN/ASN-24 navigation computers
- **Files Downloaded**:
  - eai-handbook-analog-computation-1967.pdf
  - eai-tr48-operators-manual-1963.pdf
  - comdyna-gp6-manual.pdf (Comdyna-GP6-AnalogComputer.pdf)
  - eai-tr48-specifications.pdf (AC64061_PACE_TR-48...)
  - bitsavers-asn24g-computer-sets.pdf
- **Notes**: Some files also mirrored on archive.org

### Computer History Museum
- **Base URL**: `https://s3data.computerhistory.org/brochures/`
- **Content**: Analog computer brochures, marketing materials
- **Files Downloaded**:
  - eai-231r-analog-computer-1961.pdf (eai.231r.1961.102646219.pdf)
  - eai-8800-computing-system-1965.pdf (eai.8800.1965.102646095.pdf)
  - eai-680-computing-system-1965.pdf (eai.680.1965.102646244.pdf)
  - systron-donner-series-10-80-brochure.pdf (systrondonner.series-10-20-40-80.1966.102646233.pdf)
- **Notes**: High-quality scans, reliable downloads

### Internet Archive
- **Base URL**: `https://archive.org/`
- **Download Pattern**: `https://archive.org/download/{ITEM_ID}/{FILENAME}`
- **Content**: Mirrors of bitsavers, DTIC documents, historical manuals
- **Files Downloaded**:
  - dtic-missile-dynamics-equations.pdf (DTIC_ADA151529)
  - dtic-missile-autopilot-models.pdf (DTIC_ADA407845)
  - systron-donner-handbook-1967.pdf (bitsavers_systrondonComputationJun67)
  - scr584-mk56-fire-control-getting.pdf (SCR584B)
- **Notes**: Good fallback when direct DTIC downloads fail; use wget with user-agent

### Analog Museum
- **Base URL**: `https://www.analogmuseum.org/library/`
- **Content**: Analog computer manuals, handbooks, historical documents
- **Files Downloaded**:
  - heathkit-ec1-operation-manual.pdf (heathkit_ec1_operation_manual.pdf)
  - eai-tr48-small.pdf (eai_tr-48_small.pdf)
  - donner-3500-instruction-manual.pdf (Donner_3500_Instruction-Manual.pdf)
  - analogmuseum-handbook-analog-computation.pdf (handbook_of_analog_computation.pdf)
  - navarro-analog-computer-fundamentals-1962.pdf (Navarro1962.pdf)
  - rubin-analog-hybrid-what-is-it.pdf (analog_hybrid_what_is_it.pdf)
- **Notes**: Excellent source for vintage analog computer documentation

### Anabrid / THE Analog Thing
- **Base URL**: `https://the-analog-thing.org/`
- **Content**: THAT documentation, modern analog computing
- **Files Downloaded**:
  - that-first-steps.pdf (THAT_First_Steps.pdf)
- **Alt Sources**:
  - https://analogparadigm.com/documentation.html (ALPACA application notes)
  - https://github.com/anabrid/the-analog-thing-docs
- **Notes**: Active project with regular updates

### Maritime.org
- **Base URL**: `https://maritime.org/doc/`
- **Content**: Navy ordnance pamphlets, fire control manuals
- **Files Downloaded**:
  - navy-op1140-fire-control-mechanisms.pdf (op1140/op1140-1.pdf)
  - navy-fire-control-fundamentals.pdf (pdf/fc2.pdf)
- **Notes**: Excellent for WWII-era fire control computer documentation

### MIT STS Archive
- **Base URL**: `https://web.mit.edu/STS.035/www/PDFs/`
- **Content**: Historical computing papers, fire control computers
- **Files Downloaded**:
  - mit-ford-newell-fire-control.pdf (Newell.pdf)
  - mit-sperry-gyroscope.pdf (sperry.pdf)
- **Notes**: Academic papers on computing history

### DVQ.com
- **Base URL**: `https://www.dvq.com/docs/`
- **Content**: Comdyna manuals, vintage analog computer docs
- **Files Downloaded**:
  - comdyna-gp6-operators.pdf (comdyna/gp6-op.pdf)
- **Notes**: Good secondary source for Comdyna

### JHUAPL Technical Digest
- **Base URL**: `https://secwww.jhuapl.edu/techdigest/`
- **Content**: Missile guidance, defense systems
- **Files Downloaded**:
  - jhuapl-6dof-missile-simulation.pdf (content/techdigest/pdf/V29-N01/29-01-Hawley.pdf)
- **Notes**: Reliable technical publications

### RadioNerds
- **Base URL**: `https://radionerds.com/`
- **Content**: Military radio and radar technical manuals
- **Files Downloaded**:
  - radionerds-scr584-tm11-487c.pdf (images/7/7b/TM_11-487C.pdf)
- **Notes**: Good for WWII-era military electronics

### University Sources
- **Cornell**: courses.cit.cornell.edu - Aircraft stability (cornell-aircraft-stability-control.pdf)
- **Iowa State**: home.engineering.iastate.edu - Flight dynamics (iastate-flight-stability-control.pdf)
- **SJSU**: www.sjsu.edu - Three-body problem (sjsu-three-body-simulation.pdf)
- **UC Berkeley**: www2.eecs.berkeley.edu - Technical reports
- **UCD Ireland**: maths.ucd.ie - Weather prediction history (lynch-eniac-weather-bams.pdf)
- **AeroStudents**: aerostudents.com - Flight dynamics summary

### NOAA
- **Base URL**: `https://tidesandcurrents.noaa.gov/publications/`
- **Content**: Tidal prediction, harmonic analysis
- **Files Downloaded**:
  - noaa-harmonic-tides-sp98.pdf (SpecialPubNo98.pdf)
- **Notes**: Official government publications

### CORE (Open Access Research)
- **Base URL**: `https://core.ac.uk/download/pdf/`
- **Content**: Academic papers, theses
- **Files Downloaded**:
  - core-analog-power-system.pdf (190333943.pdf)
- **Notes**: Aggregates open access research papers

### Caltech
- **Base URL**: Various departments
- **Content**: Orbital mechanics, mission design
- **Files Downloaded**:
  - caltech-three-body-mission-design.pdf (from cds.caltech.edu)
- **Notes**: May need wget with --no-check-certificate

### PassDIY
- **Base URL**: `https://www.passdiy.com/pdf/`
- **Content**: DIY audio and op-amp circuits
- **Files Downloaded**:
  - passdiy-discrete-opamps.pdf (diyopamp.pdf)
- **Notes**: Good for discrete component designs

## Secondary Sources (Variable Success)

### DTIC (Defense Technical Information Center)
- **Base URL**: `https://apps.dtic.mil/sti/`
- **Note**: Direct downloads often blocked (403 Forbidden)
- **Workaround**: Use archive.org mirrors instead
- **Search Pattern**: Look for AD/ADA numbers, then find on archive.org

### ResearchGate
- **Base URL**: `https://www.researchgate.net/`
- **Note**: Often requires login for full PDFs
- **Use for**: Finding paper references, then search elsewhere

### Scribd
- **Note**: Paywalled, limited free access
- **Use for**: Identifying documents to find elsewhere

### IEEE Xplore
- **Base URL**: `https://ieeexplore.ieee.org/`
- **Note**: Paywalled for most content
- **Use for**: Finding paper titles/abstracts to search elsewhere

## Failed Sources (For Reference)

### Sources That Blocked Downloads
- DTIC direct links (403 Forbidden) - use archive.org mirrors
- Some Caltech links (SSL certificate issues) - use wget --no-check-certificate
- Systron-Donner Design_of_an_Analog_Computer_1966.pdf on bitsavers (returned HTML)

## Search Strategies by Topic

### Flight Simulation / Aerospace
1. Start with NTRS (ntrs.nasa.gov)
2. Search terms: "analog simulation", "equations of motion", aircraft name
3. Look for NASA TN, TM, CR document types

### Fire Control / Military
1. Start with maritime.org for Navy docs
2. Check archive.org for DTIC mirrors
3. MIT STS archive for historical papers

### Vintage Analog Computers
1. Start with bitsavers.org/pdf/
2. Check analogmuseum.org/library/
3. Computer History Museum brochures

### Modern Analog Computing
1. Anabrid/THE Analog Thing documentation
2. Analog Paradigm application notes (ALPACA series)

### Practical Applications
1. NTRS for aerospace/nuclear applications
2. NOAA for tidal prediction
3. University repositories for specific topics

## Download Commands

### Standard curl
```bash
curl -L -o "filename.pdf" "URL" 2>/dev/null
```

### wget with user-agent (for archive.org, some others)
```bash
wget --user-agent="Mozilla/5.0" -O "filename.pdf" "URL"
```

### wget for SSL issues
```bash
wget --no-check-certificate -O "filename.pdf" "URL"
```

## File Naming Convention
- Source prefix: ntrs-, dtic-, bitsavers-, mit-, navy-, etc.
- Descriptive name with hyphens
- Example: `ntrs-apollo-guidance-navigation.pdf`
