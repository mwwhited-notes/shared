# Application Notes

This folder contains application notes and technical documentation relevant to analog computing from Texas Instruments, Analog Devices, Anabrid, and other sources.

## Contents (159 PDFs, 253MB)

The `pdfs/` subfolder contains documents organized by category:

```
pdfs/
├── acoustic-sonar/       (3 files)   # Sonar signal processing
├── adi-appnotes/         (39 files)  # Analog Devices MT/AN series
├── anabrid-alpaca/       (37 files)  # ALPACA application notes
├── biomedical/           (9 files)   # ECG, EEG, EMG, IONM
├── discrete-circuits/    (25 files)  # DIY op-amps, nonlinear circuits
├── educational/          (4 files)   # Course materials
├── historical-computing/ (11 files)  # Antikythera, perceptron, etc.
├── music-synthesis/      (1 file)    # Moog, VCO
├── petroleum/            (1 file)    # Reservoir simulation
├── process-control/      (3 files)   # PID, dynamometer
├── radar/                (1 file)    # MTI, pulse Doppler
├── seismology/           (2 files)   # Earthquake instrumentation
├── sensors/              (4 files)   # Photodiodes, gas sensors
└── ti-appnotes/          (19 files)  # Texas Instruments app notes
```

---

## acoustic-sonar/

Sonar and Acoustic Signal Processing

| File | Description |
|------|-------------|
| jhuapl-sonar-processing.pdf | JHUAPL sonar signal processing techniques |
| intechopen-sonar-signal-processing.pdf | InTech Open sonar signal processing |
| acoustics-today-defense.pdf | Acoustics Today defense applications |

---

## adi-appnotes/

Analog Devices Application Notes and Tutorials

### MT Series (Tutorials)

| File | Description |
|------|-------------|
| adi-mt001.pdf | MT-001: Decoupling Techniques |
| adi-mt003.pdf | MT-003: Understand SINAD, ENOB, SNR, THD |
| adi-mt004.pdf | MT-004: The Good, the Bad, and the Ugly Aspects of ADC Input Noise |
| adi-mt006.pdf | MT-006: ADC Noise Figure |
| adi-mt007.pdf | MT-007: Aperture Time, Jitter, and Precision of Edges |
| adi-mt008.pdf | MT-008: Converting Noise Spectral Densities |
| adi-mt009.pdf | MT-009: Data Converter Codes |
| adi-mt010.pdf | MT-010: The Importance of Data Converter Static Specs |
| adi-mt011.pdf | MT-011: Find Those Elusive ADC/DAC Spoilers |
| adi-mt012.pdf | MT-012: Intermodulation Distortion |
| adi-mt014.pdf | MT-014: Basic DAC Architectures I |
| adi-mt015.pdf | MT-015: Basic DAC Architectures II |
| adi-mt017.pdf | MT-017: Oversampling Interpolating DACs |
| adi-mt020.pdf | MT-020: ADC Architectures I (Pipelined) |
| adi-mt021.pdf | MT-021: ADC Architectures II (SAR) |
| adi-mt022.pdf | MT-022: ADC Architectures III (Sigma-Delta) |
| adi-mt023.pdf | MT-023: ADC Architectures IV (Flash) |
| adi-mt024.pdf | MT-024: ADC Architectures V (Dual Slope) |
| adi-mt025.pdf | MT-025: ADC Noise Figure |
| adi-mt031.pdf | MT-031: Grounding Data Converters |
| adi-mt035.pdf | MT-035: Op Amp Inputs, Outputs, Single-Supply |
| adi-mt036.pdf | MT-036: Op Amp Output Phase Reversal |
| adi-mt038.pdf | MT-038: Op Amp Input Impedance |
| adi-mt042.pdf | MT-042: Op Amp Common-Mode Rejection Ratio |
| adi-mt043.pdf | MT-043: Op Amp Power Supply Rejection Ratio |
| adi-mt044.pdf | MT-044: Op Amp Open-Loop Gain and Open-Loop Gain Nonlinearity |
| adi-mt047.pdf | MT-047: Op Amp Noise |
| adi-mt048.pdf | MT-048: Op Amp Noise Relationships |
| adi-mt049.pdf | MT-049: Op Amp Total Output Noise Calculations |
| adi-mt050.pdf | MT-050: Op Amp Distortion: HD and IMD |

### AN Series (Application Notes)

| File | Description |
|------|-------------|
| adi-an360.pdf | AN-360: Multiplier application notes |
| adi-an397.pdf | AN-397: Electrically induced model motion |

### Other ADI Documents

| File | Description |
|------|-------------|
| adi-multiplier-app-guide.pdf | AD633/AD534 multiplier applications guide |
| adi-inamp-guide.pdf | Instrumentation amplifier guide |
| adi-cn0314-420ma.pdf | CN-0314: 4-20mA current loop interface |
| adi-cn0301-lvdt.pdf | CN-0301: LVDT position sensor interface |
| adi-cn0350-piezo.pdf | CN-0350: Piezoelectric sensor interface |
| adi-ad598-lvdt.pdf | AD598 LVDT signal conditioner |
| adi-ad7745-cap.pdf | AD7745 capacitive sensor |
| adi-lt1025-cjc.pdf | LT1025 thermocouple CJC |
| adi-sensor-handbook-ch6.pdf | Sensor signal conditioning handbook Ch.6 |
| adi-op-amp-data-converters.pdf | Op-amps with data converters |
| adi-nonlinear-circuits-handbook.pdf | Nonlinear circuits design handbook |

---

## anabrid-alpaca/

ALPACA (Analog Paradigm Application Collection of Analog computing)

| File | Topic |
|------|-------|
| alpaca_1-rossler.pdf | Rössler attractor |
| alpaca_2-lorenz.pdf | Lorenz attractor |
| alpaca_3-chua.pdf | Chua's circuit |
| alpaca_4-bouncing-ball.pdf | Bouncing ball |
| alpaca_5-van-der-pol.pdf | Van der Pol oscillator |
| alpaca_6-mathieu.pdf | Mathieu equation |
| alpaca_7-duffing.pdf | Duffing oscillator |
| alpaca_8-pendulum.pdf | Simple pendulum |
| alpaca_11-three-body.pdf | Three-body problem |
| alpaca_12-charged-particle.pdf | Charged particle dynamics |
| alpaca_14-rutherford.pdf | Rutherford scattering |
| alpaca_15-elegant-chaos.pdf | Elegant chaos systems |
| alpaca_17-aizawa.pdf | Aizawa attractor |
| alpaca_19-spacecraft.pdf | Spacecraft dynamics |
| alpaca_20-inverted-pendulum.pdf | Inverted pendulum |
| alpaca_21-double-pendulum.pdf | Double pendulum |
| alpaca_23-pde.pdf | Partial differential equations |
| alpaca_27-music.pdf | Music synthesis |
| alpaca_28-hindmarsh-rose.pdf | Hindmarsh-Rose neuron model |
| alpaca_30-neutron.pdf | Neutron kinetics |
| alpaca_31-sprott-sqm.pdf | Sprott systems |
| alpaca_33-euler-spiral.pdf | Euler spiral |
| alpaca_34-buckling.pdf | Beam buckling |
| alpaca_35-brusselator.pdf | Brusselator oscillator |
| alpaca_36-pursuit.pdf | Pursuit curves |
| alpaca_37-pursuit-4.pdf | Four-body pursuit |
| alpaca_38-pursuit-n.pdf | N-body pursuit |
| alpaca_39-circle.pdf | Circle generation |
| alpaca_40-roessler-hyperchaos.pdf | Rössler hyperchaos |
| alpaca_41-rabinovitch.pdf | Rabinovitch-Fabrikant system |
| alpaca_42-mandelbrot.pdf | Mandelbrot set |
| alpaca_43-linear-ode.pdf | Linear ODEs |
| alpaca_44-nonlinear-ode.pdf | Nonlinear ODEs |
| alpaca_45-logistic-map.pdf | Logistic map |
| alpaca_50-bessel.pdf | Bessel functions |
| alpaca_51-root-finding.pdf | Root finding |
| alpaca_54-stochastic-deq.pdf | Stochastic differential equations |

---

## biomedical/

Biomedical Signal Processing (ECG, EEG, EMG, IONM)

### ECG/Electrocardiography

| File | Description |
|------|-------------|
| ad8232-ecg-front-end.pdf | AD8232 single-lead ECG front end datasheet |
| msu-ecg-circuit-design.pdf | MSU ECE480 electrocardiography circuit design |
| stanford-ecg-project.pdf | Stanford ENGR 40M ECG project |
| oxford-ecg-instrumentation.pdf | Oxford ECG instrumentation notes |
| northeastern-ecg-lab.pdf | Northeastern ECG instrumentation amplifier lab |

### EEG/EMG Signal Processing

| File | Description |
|------|-------------|
| eeg-signal-processing.pdf | EEG Signal Processing textbook (U. Washington) |
| emg-tutorial-merletti.pdf | Surface EMG detection and conditioning tutorial |
| mit-cardiovascular-acceleration.pdf | MIT cardiovascular simulation thesis |

### IONM (Intraoperative Neurophysiological Monitoring)

| File | Description |
|------|-------------|
| kaiser-ionm-policy.pdf | Kaiser IONM clinical policy |

---

## discrete-circuits/

Discrete Component Circuit Design

### Op-Amp Construction

| File | Description |
|------|-------------|
| passdiy-discrete-opamp.pdf | PassDIY: Building discrete op-amps |
| adafruit-discrete-opamp.pdf | Adafruit discrete op-amp tutorial |
| unc-diffpair-mirror.pdf | Differential pair and current mirror |

### Nonlinear Circuits

| File | Description |
|------|-------------|
| triode-diode-function-gen.pdf | Diode function generators |
| kuhn-log-circuits.pdf | Discrete log/antilog circuits |
| gilbert-cell-multiplier.pdf | Gilbert cell analog multiplier |
| ad538-computational.pdf | AD538 computational circuits |

### Analog Switches and VCO

| File | Description |
|------|-------------|
| ucsd-fet-switches.pdf | FET analog switches |
| toronto-vco.pdf | VCO design |
| oxford-peak-detector.pdf | Peak detector circuits |

### Reference Circuits

| File | Description |
|------|-------------|
| bobpease-bandgap.pdf | Bandgap voltage reference design |

### Filter Design

| File | Description |
|------|-------------|
| sloa049d.pdf | TI Active Filter Design Techniques |

(Plus additional discrete circuit files)

---

## educational/

Educational Materials and Getting Started Guides

| File | Description |
|------|-------------|
| THAT_First_Steps.pdf | THE Analog Thing getting started guide |
| uiuc-analog-computing.pdf | UIUC analog computing course |
| uiuc-analog-manual.pdf | UIUC analog computer manual |
| vissim-6dof-tutorial.pdf | VisSim 6-DOF simulation tutorial |

---

## historical-computing/

Historical Analog Computing

### Antikythera Mechanism

| File | Description |
|------|-------------|
| antikythera-cosmos-model-2021.pdf | Nature paper: Model of the Cosmos reconstruction |
| antikythera-modern-reproduction.pdf | Modern reproduction of the mechanism |
| antikythera-reconstruction-arxiv.pdf | ArXiv reconstruction instructions |
| asme-antikythera-landmark.pdf | ASME historical mechanical engineering landmark |

### Tide Prediction Machines

| File | Description |
|------|-------------|
| liverpool-tide-machines.pdf | Tide prediction machines at Liverpool Tidal Institute |
| ostrander-planetarium-calculator.pdf | 1841 planetarium and astronomical calculator |

### Differential Analyzer

| File | Description |
|------|-------------|
| bush-differential-analyzer-1986.pdf | Bush differential analyzer history |

### Early Neural Networks

| File | Description |
|------|-------------|
| rosenblatt-perceptron-1958.pdf | Rosenblatt's original perceptron paper |
| perceptron-lecture-notes.pdf | Perceptron lecture notes |

### Ballistic Computation

| File | Description |
|------|-------------|
| iop-artillery-firing-tables.pdf | Artillery firing tables computation |
| aberdeen-ballistic-computation.pdf | Aberdeen ballistic computer history |

---

## music-synthesis/

Music Synthesis and Audio

| File | Description |
|------|-------------|
| moog-voltage-controlled-modules-1964.pdf | Moog 1964 AES paper on voltage-controlled modules |

---

## petroleum/

Petroleum and Reservoir Simulation

| File | Description |
|------|-------------|
| usgs-petroleum-modeling.pdf | USGS petroleum reservoir modeling |

---

## process-control/

Process Control and Automation

| File | Description |
|------|-------------|
| asee-pid-experiment.pdf | ASEE PID controller modeling and simulation |
| keysight-dyno-testing.pdf | Keysight dynamometer engine testing |
| pmu-dynamometer-design.pdf | Dynamometer design for engine testing |

---

## radar/

Radar Signal Processing

| File | Description |
|------|-------------|
| recw-mti-pulse-doppler.pdf | MTI and pulse Doppler radar processing |

---

## seismology/

Seismology and Earthquake Instrumentation

| File | Description |
|------|-------------|
| seismology-instrumentation.pdf | Seismology instrumentation fundamentals |
| aees-seismic-instrumentation.pdf | AEES seismic instrumentation standards |

---

## sensors/

Sensor Interface Circuits

| File | Description |
|------|-------------|
| vishay-photodiode.pdf | Photodiode application notes |
| sgx-electrochemical-sensor.pdf | Electrochemical gas sensors |
| st-shock-sensor.pdf | Shock/vibration sensors |
| iaea-reactor-simulator.pdf | IAEA nuclear reactor instrumentation |

---

## ti-appnotes/

Texas Instruments Application Notes

### Op-Amp Fundamentals

| File | Description |
|------|-------------|
| sboa092b.pdf | Handbook of Operational Amplifier Applications |
| sboa275.pdf | Integrator circuit design |
| snla140d.pdf | AN-31: Amplifier Circuit Collection |
| snoa621c.pdf | AN-20: Applications Guide for Op Amps |

### Sensor Interface

| File | Description |
|------|-------------|
| ti-transimpedance.pdf | Transimpedance amplifier design |
| ti-strain-gauge.pdf | Strain gauge bridge conditioning |
| ti-thermocouple-cjc.pdf | Thermocouple cold junction compensation |
| ti-rtd-guide.pdf | RTD/PT100 temperature sensor guide |
| ti-pt100-circuit.pdf | PT100 circuit design |
| ti-piezo-charge-amp.pdf | Piezoelectric charge amplifier |
| ti-opt101.pdf | OPT101 photodiode amplifier |
| ti-bridge-conditioning.pdf | Bridge sensor conditioning |
| ti-fdc1004-cap.pdf | FDC1004 capacitive sensing |

### Signal Processing

| File | Description |
|------|-------------|
| ti-lm331-vfc.pdf | LM331 voltage-to-frequency converter |
| ti-cd4046b-pll.pdf | CD4046B PLL circuits |
| ti-sboa068-abs-value.pdf | Absolute value circuits |
| ti-snoa575b-log-amp.pdf | Log amplifier applications |
| ti-tidu024-rectifier.pdf | Precision rectifier circuits |

---

## Quick Reference: Which App Note for What?

| Task | Recommended PDF | Folder |
|------|-----------------|--------|
| Building an integrator | sboa275.pdf, sboa092b.pdf | ti-appnotes/ |
| Designing a filter | sloa049d.pdf | discrete-circuits/ |
| Multiplier circuits | adi-multiplier-app-guide.pdf | adi-appnotes/ |
| Chaos/attractors | alpaca_2-lorenz.pdf, alpaca_3-chua.pdf | anabrid-alpaca/ |
| Solving ODEs | alpaca_43-linear-ode.pdf, alpaca_44-nonlinear-ode.pdf | anabrid-alpaca/ |
| Sensor interface | adi-inamp-guide.pdf, ti-strain-gauge.pdf | adi-appnotes/, ti-appnotes/ |
| VFC circuits | ti-lm331-vfc.pdf | ti-appnotes/ |
| Discrete circuits | passdiy-discrete-opamp.pdf | discrete-circuits/ |
| Physics simulations | alpaca_8-pendulum.pdf, alpaca_11-three-body.pdf | anabrid-alpaca/ |
| ECG/biomedical | ad8232-ecg-front-end.pdf, msu-ecg-circuit-design.pdf | biomedical/ |
| PID control | asee-pid-experiment.pdf | process-control/ |
| Historical computing | antikythera-cosmos-model-2021.pdf | historical-computing/ |
| Sonar processing | jhuapl-sonar-processing.pdf | acoustic-sonar/ |
| Radar MTI | recw-mti-pulse-doppler.pdf | radar/ |

---

## Sources

- **Texas Instruments**: ti.com/lit/
- **Analog Devices**: analog.com/en/resources/
- **Anabrid/Analog Paradigm**: analogparadigm.com/documentation.html
- **JHUAPL**: secwww.jhuapl.edu/techdigest/
- **University courses**: UIUC, Toronto, UCSD, Oxford, MSU, Stanford

---

## See Also

- [Datasheets](../09-datasheets/) - Component datasheets
- [Aerospace Simulation](../11-aerospace-simulation/) - Flight simulation and guidance
- [Analog Computer Docs](../12-analog-computer-docs/) - Computer-specific documentation
