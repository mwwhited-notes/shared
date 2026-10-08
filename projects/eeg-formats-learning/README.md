# EEG file formats, storage and synchronization: learning project

This project captures a long exploratory conversation (2026-10-07) that started with basic EEG questions and ended with the design of a time-synchronized, losslessly compressed multichannel recording format for overnight (sleep) studies with video. It is meant to be dropped into a Claude Code project as context and a starting point.

## Confidence tags

Almost everything here was produced from the model's general knowledge during a chat. Treat it as a map of what to verify, not as a reference.

| Tag | Meaning |
|---|---|
| **[tested]** | checked by running code. Only the `.ksy` files, against synthetic data |
| **[found]** | appeared in web search results during the chat (often titles and snippets only) |
| **[memory]** | from the model's knowledge, not verified |

## What is in this folder

```
README.md                 this file
CLAUDE.md                 short project context for Claude Code
ksy/                      Kaitai Struct descriptions of six EEG formats
  edf.ksy                 EDF / EDF+
  bdf.ksy                 BioSemi BDF (24-bit)
  fif.ksy                 FIF (Neuromag/MNE tag stream)
  xdf.ksy                 XDF (Lab Streaming Layer)
  eeglab_fdt.ksy          EEGLAB .fdt raw data (parameterized)
  brainvision_eeg.ksy     BrainVision .eeg multiplexed (parameterized)
tools/
  check.js                compile every .ksy to Python
  roundtrip.py            parse synthetic EDF/BDF/FIF/XDF/fdt/BrainVision files
  run_checks.sh           runs both
  package.json            node dependencies for check.js
docs/
  01-eeg-background.md              artifact reduction, source imaging, HD-EEG, vendors, Cadwell
  02-file-formats.md                spec locations and text layouts for each format
  03-storage-resolution-compression.md   ADC vs float, bit depth rule, mixed depths, compression, standards
  04-canonical-format-design.md     draft design for a seekable compressed format
  05-time-and-sync.md               time coding, multi-amp sync, video/audio sync, IR/TTL/LTC design
  sources.md                        every link gathered, tagged found vs memory
```

The chat also rendered block diagrams inline for EDF+, BDF, FIF, XDF and the headerless formats. They are not files; `docs/02-file-formats.md` redraws them as text.

## How the conversation went

1. **Artifact reduction** in EEG (background).
2. **How "3D EEG" works** (source imaging).
3. **Studies with more than 500 channels.** Very few; mostly 256. The g.Pangolin uHD system reaches 1,024 channels.
4. **Brands** supporting HD-EEG, then **Cadwell** (clinical, 32/64 channels, Zenith up to 432 intracranial), and why clinical and research products differ.
5. **Where file format specs live,** then **Kaitai Struct `.ksy` files** for the formats that have a fixed binary layout.
6. **Public datasets** (Hugging Face, OpenNeuro, PhysioNet, Kaggle, MNE sample data) and a **source list**.
7. **Block diagrams** for EDF+ and the other formats.
8. **Storage:** raw ADC integers vs float, typical resolution, a rule for non-multiple-of-8 ADC depths, how often channels differ in depth.
9. **Compression:** no listed format compresses natively; what to use instead; standard telemetry formats (miniSEED, MDF4, IRIG 106, HDF5/NWB/Zarr).
10. **A draft canonical format:** byte-aligned widths, block compression, seek index.
11. **Time coding** in existing formats, **multi-amplifier sync,** how **gaps** are accounted for.
12. **Syncing to video and audio:** network cameras with sync, PTZ cameras, night-study constraints (no visible strobes), a TTL + IR LED + audio design, rolling Gray-code and LTC time codes.

## Key takeaways

- Archive raw ADC integers at storage width `ceil(bits/8)` bytes (right-justified, sign-extended); use float32 for processed data.
- No common EEG format compresses natively. For seekable lossless compression use Zarr/HDF5 (NWB) with Blosc, or look at miniSEED, before writing a custom format.
- A custom format can be append-only: independent compressed blocks (delta, zigzag, byte shuffle, zstd) with a first-sample index per block and a footer index for time seeking.
- Represent gaps by sample-index jumps plus a discontinuity flag and optional validity bitmap, not by silent fill.
- Sync amplifiers and video with one pulse source: TTL into every amplifier, an IR LED (940 nm) in the camera's view, and a line-level audio code. Use aperiodic coded pulses, and fit offset and drift by regression. For a whole night, drift (about 0.6 s at 20 ppm) is the reason this matters.
- Night studies: use electrical strobes and IR, never visible flashes or audible clicks; isolate anything connected near the patient and get biomedical engineering sign-off.

## The Kaitai Struct files

| Format | File | Coverage | Status |
|---|---|---|---|
| EDF / EDF+ | `ksy/edf.ksy` | full header, signal headers, data records; unknown record count (-1) read to EOF | compiles; parses synthetic data [tested] |
| BDF | `ksy/bdf.ksy` | as EDF with 0xFF "BIOSEMI" magic and 24-bit samples | compiles; parses synthetic data [tested] |
| FIF | `ksy/fif.ksy` | tag stream, FILE_ID decoded, other payloads raw | compiles; constants from memory |
| XDF | `ksy/xdf.ksy` | chunks, headers, clock offsets, boundary; sample payload raw | compiles; parses synthetic data [tested] |
| EEGLAB `.fdt` | `ksy/eeglab_fdt.ksy` | float32 frames; needs channel count and frame count as parameters | compiles; parses synthetic data [tested] |
| BrainVision `.eeg` | `ksy/brainvision_eeg.ksy` | multiplexed int16 or float32 | compiles; parses synthetic data [tested] |

"Tested" means the generated Python parser read back hand-built files correctly. It does not mean the files agree with real vendor recordings. Next step: parse a real file of each format (see `docs/sources.md`).

Not described: EEGLAB `.set` (MATLAB), BrainVision `.vhdr`/`.vmrk` (INI text), BIDS (folder convention), Cadwell Arc (proprietary, no public spec known).

### Running the checks

Needs node/npm, python3, and `pip install kaitaistruct`.

```
cd tools
./run_checks.sh
```

This compiles every `.ksy` to Python (kaitai-struct-compiler 0.11+, whose JS module is the compiler object itself) and runs `roundtrip.py` against synthetic files.

## Open questions and next steps

- Parse one real file per format with the `.ksy` files; fix any disagreements.
- Verify FIF tag kinds and types against MNE-Python's `constants.py`.
- Confirm `.xdfz` support in LabRecorder and pyxdf.
- Compare miniSEED v3 and NWB for EEG against the draft in `docs/04-canonical-format-design.md`; decide whether to build a custom format.
- If building it: write a `.ksy` for it (block header, channel groups, footer index), pick block size and codecs, and measure compression on real recordings.
- Write the microcontroller sketch for the TTL + IR + audio sync source, and the detection and regression script for alignment.
- Confirm specs for candidate cameras (PTP, trigger/strobe, stereo line-in, IR cut filter) from datasheets; the PTZ leads in `docs/05-time-and-sync.md` came from titles only.
- Check hardware figures (BioSemi 31.25 nV step, BrainAmp 0.1 uV, vendor channel counts) against datasheets.
- Get biomedical engineering review of any wiring near patients (isolation, IEC 60601).

## Caveats

- Specific model names, channel limits, links and numeric claims marked [memory] may be wrong or out of date.
- The two Hugging Face dataset leads and the Mendeley XDF dataset were found but not opened; file formats inside them are unconfirmed.
- Nothing here is medical-device or clinical guidance.
