# EEG file formats

Machine-readable descriptions are in `../ksy/` (Kaitai Struct). This file is the human-readable summary. Layouts below were rendered as block diagrams in the original chat; they are redrawn here as text.

Confidence: layouts for EDF, BDF, XDF, EEGLAB `.fdt` and BrainVision `.eeg` are encoded in the `.ksy` files and parsed successfully against synthetic data **[tested]**, but that only proves internal consistency, not agreement with real vendor files. FIF constants are **[memory]**.

## Where the specs live [memory, verify links]

| Format | Spec or docs |
|---|---|
| EDF / EDF+ | edfplus.info |
| BDF (BioSemi) | biosemi.com, file format FAQ. 24-bit variant of EDF |
| BrainVision (.vhdr/.vmrk/.eeg) | Brain Products support pages |
| EEGLAB (.set/.fdt) | sccn.ucsd.edu/eeglab |
| FIF | mne.tools; MNE-Python `constants.py` |
| XDF | github.com/sccn/xdf |
| BIDS-EEG | bids-specification.readthedocs.io [found] |
| Cadwell Arc | no public spec known; export to EDF from Arc |

## EDF / EDF+

```
+---------------------------+  bytes 0-255
| Main header (256 bytes)   |
+---------------------------+
| Signal headers            |  256 bytes x number of signals, FIELD-MAJOR
+---------------------------+  (each field is written once per signal before the next field)
| Data record 0             |  for each signal: samples_per_record x int16 little-endian
| Data record 1             |
| ...                       |
| Data record N-1           |
+---------------------------+
```

Main header fields (all ASCII, space padded):

| Field | Bytes | Notes |
|---|---|---|
| Version | 8 | always "0" |
| Patient id | 80 | EDF+: code, sex, birthdate, name |
| Recording id | 80 | EDF+: Startdate, admin code, technician, equipment |
| Start date | 8 | dd.mm.yy |
| Start time | 8 | hh.mm.ss, no timezone |
| Header bytes | 8 | 256 + 256 x signals |
| Reserved | 44 | EDF+C (continuous) or EDF+D (discontinuous) |
| Data records | 8 | count, -1 if unknown |
| Record duration | 8 | seconds |
| Signals | 4 | number of signals |

Signal header fields, each repeated once per signal, in this order: label 16, transducer 80, physical dimension 8, physical min 8, physical max 8, digital min 8, digital max 8, prefiltering 80, samples per record 8, reserved 32.

EDF+ annotations: a signal labelled "EDF Annotations" holds ASCII time-stamped annotation lists (TALs) inside its int16 slots.

```
TAL:  +onset  0x15  duration  0x14  text  0x14  0x00
```

Duration (with its 0x15 separator) is optional. The first TAL in each record has empty text and gives that record's start time.

Scaling to physical units: `value = (digital - dig_min) * (phys_max - phys_min) / (dig_max - dig_min) + phys_min`.

## BDF (BioSemi) [tested]

Same layout as EDF with two differences:
- Header starts with byte 0xFF followed by "BIOSEMI" instead of "0".
- Samples are 24-bit signed little-endian (three bytes: b0 low, b1, b2 high). One step is 1/32 uV (31.25 nV) on BioSemi hardware **[memory]**.
- A "Status" signal usually carries trigger bits.

## FIF (Neuromag / Elekta / MEGIN, used by MNE-Python) [memory]

Flat stream of tags, big-endian:

```
Tag = kind (4) | type (4) | size (4) | next (4) | data (size bytes)
```

- `next`: 0 means the next tag follows, -1 means no further tag, positive means absolute file offset.
- The type's low 16 bits are the base type; upper bits encode matrix and sparse-matrix variants.
- Block nesting is expressed by BLOCK_START and BLOCK_END tags, not by byte layout.
- The `.ksy` decodes FILE_ID only; other payloads stay raw bytes.
- Constants in the `.ksy` were written from memory. Verify against MNE-Python's `constants.py`.

## XDF (Lab Streaming Layer recordings) [tested]

```
"XDF:" magic, then chunks:
Chunk = length-size byte (1, 4 or 8) | length | tag (u2) | content
```

`length` counts tag plus content. Tags: 1 file header (XML), 2 stream header (stream id + XML), 3 samples, 4 clock offset, 5 boundary (fixed 16-byte marker), 6 stream footer.

Sample payloads are left as raw bytes in the `.ksy` because channel format and count come from the stream-header XML. Each sample has an optional timestamp (flag byte 0, or 8 followed by a double) then one value per channel.

## EEGLAB `.fdt` and BrainVision `.eeg` [tested]

Both are headerless. The file is a sequence of frames, one per time point, each holding one value per channel (channel-fastest, "multiplexed").

```
Frame 0 | Frame 1 | ... | Frame n-1
Frame  = Ch0 | Ch1 | ... | Ch(n-1)
```

- EEGLAB `.fdt`: float32 little-endian. Shape (channels, points, trials) comes from the paired `.set`, which is a MATLAB file.
- BrainVision `.eeg`: int16 or float32 as declared in the `.vhdr`. The `.ksy` covers MULTIPLEXED orientation only. VECTORIZED stores all of channel 0, then channel 1, and so on.
- For INT_16, multiply by the channel resolution in the `.vhdr` to get physical units.

## Not covered

EEGLAB `.set` (MATLAB MAT), BrainVision `.vhdr` and `.vmrk` (INI-style text), BIDS (a folder convention), Cadwell Arc (proprietary, no public spec).
