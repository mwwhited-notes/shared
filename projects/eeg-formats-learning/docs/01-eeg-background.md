# EEG background

Confidence tags used throughout this project:
- **[found]** appeared in web search results during the original chat
- **[tested]** checked by running code (only the `.ksy` files)
- **[memory]** from the model's general knowledge, not verified. Check before relying on it.

## Artifact reduction [memory]

Removing non-brain signals (artifacts) from EEG so the data reflects neural activity.

- **Biological artifacts:** eye blinks and movements (EOG), muscle (EMG), heartbeat (ECG), sweat or skin potentials.
- **Technical artifacts:** electrode pops, poor contact, cable movement, 50/60 Hz line noise.
- **Methods:** prevention (skin prep, stable impedance, shielding), filtering (high-pass about 0.1-1 Hz, low-pass, notch), rejecting contaminated epochs, ICA component removal, regression against EOG/ECG channels, and automated pipelines (ASR, ICLabel, PREP in EEGLAB or MNE-Python).
- **Tradeoff:** remove noise without stripping real brain signal, so pipelines combine methods and check results visually.

## "3D EEG" = EEG source imaging [memory]

Estimating where in the brain activity originates from scalp recordings.

1. Record with many electrodes (64-256, ideally high density).
2. Build a head model (MRI or template; scalp, skull, CSF, brain with conductivities).
3. Forward problem: simulate the scalp pattern for a source at each brain location (the lead field).
4. Inverse problem: estimate sources from the scalp data. It is ill-posed, so constraints are added.
5. Display on a 3D cortical surface or volume.

Inverse methods: minimum norm / LORETA / sLORETA (distributed), beamformers, dipole fitting. Resolution is roughly centimeters, far coarser than fMRI spatially but with millisecond timing. Tools: MNE-Python, EEGLAB, Brainstorm.

## High-density EEG (HD-EEG) and more than 500 channels

- Few scalp studies record more than 500 channels. Most "ultra-high-density" work stops at 256. [found]
- The g.tec g.Pangolin uHD system supports up to 1,024 channels. Typical configurations are 16-1,024. [found]
- The central sulcus mapping paper used 256 of the 1,024 possible electrodes (8.6 mm spacing); 95.2% of channels were correctly classified as anterior or posterior to the central sulcus. [found]
- g.tec's own write-up describes a 1,024-channel system on five subjects. [found] The paper and the write-up differ on how many channels were actually used.
- Instrumentation reviews say systems of up to about 1,000 electrodes are possible. [found]
- Invasive recordings (ECoG, Neuropixels) routinely exceed 500 channels but are not scalp EEG. [memory]
- For a list of studies, search PubMed or Google Scholar for "ultra-high-density EEG" or "uHD EEG" and check each methods section.

### Vendors with HD-EEG [memory]

EGI/Magstim (Geodesic, 128/256), BioSemi (ActiveTwo, 128-256+), Brain Products (actiCHamp Plus, up to 256), ANT Neuro (eego, 64-256), g.tec (g.HIamp, g.Pangolin), Compumedics Neuroscan, Cognionics/CGX (dry caps), Micromed and Natus (clinical HD-EEG).

### Cadwell [found]

- Arc Essentia and Arc Apollo+: 32 channels, and Apollo+ also offers a 64-channel amplifier. Standard clinical density.
- Arc Zenith: 144 channels per amplifier at 1 MHz sampling; the latest Arc software connects up to three for 432 channels. Older pages and brochures say 288, so the limit appears to have been raised recently.
- Zenith targets the epilepsy monitoring unit and the OR with intracranial and cortical stimulation, not dense scalp caps.

### Why clinical vendors differ from research vendors [memory]

- Clinical (Cadwell and similar): fast setup, video-EEG sync, remote review, reports, FDA clearance and billing codes, rugged amplifiers, 21-64 scalp channels or intracranial grids.
- Research (BioSemi, EGI, Brain Products, g.tec): 128-256+ channels, very low noise, precise trigger timing, open raw data export, custom layouts, combination with TMS, fMRI or eye tracking.
- The lines blur. Some labs use clinical systems for epilepsy research, and companies like EGI and Natus sell into both markets.
