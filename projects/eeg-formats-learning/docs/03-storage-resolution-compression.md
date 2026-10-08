# Storage, resolution and compression

All content here is **[memory]** unless tagged. Verify against vendor datasheets before relying on specific numbers.

## Raw ADC integers or floating point?

Archive raw ADC integers with a stored scale factor. Use float32 for processed derivatives.

- Integers hold exactly what the hardware measured. A float adds no information beyond the ADC bits.
- Processed data (filtered, re-referenced, ICA-cleaned) is non-integer, so float32 is the natural container. float32 has about 7 significant digits, which is picovolt resolution at 100 uV. Double is not needed.
- MNE's `.fif` saves float32 by default; EEGLAB `.fdt` is float32.
- Never overwrite the raw file with processed output.

## Typical resolution

| Format / hardware | Width | Typical step |
|---|---|---|
| EDF | 16-bit | about 0.1 uV with a +/-3.2 mV range |
| BDF (BioSemi) | 24-bit | 1/32 uV (31.25 nV), range about +/-262 mV |
| BrainVision `.eeg` | INT_16 or IEEE_FLOAT_32 | commonly 0.1 uV for INT_16 on BrainAmp |
| XDF | per stream: int16, int32, float32, double | whatever the stream declares |

Real EEG is about 10-100 uV with a noise floor around 0.1-1 uV, so steps finer than the noise add nothing. 24-bit matters for DC-coupled systems, where electrode offsets of hundreds of mV need a wide range to avoid clipping.

EDF scaling: choose physical and digital min/max so one step is about 0.1 uV or finer. If the ADC is 24-bit, do not use EDF; use BDF or int32/float32.

## Rule for non-multiple-of-8 ADC depths

Store at `storage_bytes = (adc_bits + 7) // 8`:

| ADC bits | Bytes |
|---|---|
| 12, 16 | 2 |
| 18, 20, 24 | 3 |
| 32 | 4 |

- Keep both the real ADC bit depth and the storage width in the header per channel.
- Right-justify and sign-extend (two's complement), so the stored value equals the ADC code and scaling is identical at every width.
- Avoid left-justifying; if used, record the shift.
- Convert unsigned or offset-binary ADC codes to signed by subtracting the mid-code, and note it in the header.
- Allow widths up to 8 bytes (48-bit samples exist).
- Padding costs almost nothing after compression: the extra bytes are pure sign extension, which byte-plane shuffling isolates and zstd collapses.

## Mixed bit depths and sample rates

- Between EEG electrodes on one amplifier: almost never mixed.
- Between EEG and auxiliary channels: common. Examples: 24-bit EEG with a 16-bit accelerometer (OpenBCI Cyton), a 24-bit status or trigger channel, 32-bit counters, battery.
- Format behavior: EDF, BDF and BrainVision use one width for the whole file (EDF can vary sample rate and scale per signal). XDF is one format per stream. HDF5/NWB/Zarr are one dtype per array. miniSEED and MDF4 are per-channel.
- Recommendation: group channels by (storage width, sample rate, scale), like MDF4 channel groups or XDF streams, and store each group as its own channel-major section in a block.

## Compression support in existing formats

| Format | Compression |
|---|---|
| EDF, BDF, BrainVision `.eeg`, EEGLAB `.fdt` | none; whole-file gzip only, not seekable |
| FIF | none in the format; MNE reads and writes `.fif.gz` (whole file) |
| XDF | none in the spec; chunking suits live appending. A gzip variant `.xdfz` is supported by LabRecorder/pyxdf, as I recall: verify |
| EEGLAB `.set` | MAT v7 compresses internally; v7.3 is HDF5 with chunking |

Formats that do support seekable compression: HDF5 (and NWB), Zarr (chunked with Blosc or zstd), Arrow/Parquet with zstd or LZ4.

Lossless compression of raw EEG typically gets about 2-3x because the low bits are noisy. Test on your own recordings.

## Standard formats for multichannel telemetry

Closest to "compressed, byte-aligned, seekable by time":
- **miniSEED** (seismology, FDSN): self-describing records with start time and sample rate, Steim delta compression, live streaming. Version 3 adds CRCs, variable-length records and nanosecond time.
- **ASAM MDF4** (automotive and industrial): channel groups, linear scaling, optional compressed (transposed deflate) data blocks, block lists for seeking.
- **IRIG 106 Chapter 10** (flight test): time-stamped packets with index packets for seeking; compression is not part of it.
- **HDF5 / NetCDF-4 / Zarr / NWB:** chunked storage with pluggable filters.
- **FLAC:** lossless and seekable, but limited to 8 channels.
- Biosignal: EDF/EDF+, BDF, GDF, SCP-ECG (Huffman-style compression), MFER, DICOM Waveform.
- Others: CCSDS Space Packet, Arrow IPC, Parquet.

Next to read: miniSEED v3 spec; compare miniSEED and NWB for EEG.
