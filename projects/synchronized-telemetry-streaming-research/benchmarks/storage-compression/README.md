# Storage Format Compression Ratios Benchmark

## Formats Tested
- HDF5 (gzip, lzf)
- Parquet (snappy, zstd)
- XDF (no compression)
- TSV + gzip

## Test Data
- Timeseries (EEG 256 channels, 500 Hz)
- Tabular (sensor logs with tags)
- Binary (waveforms, spectrograms)

## Results
Parquet+zstd achieves 85% compression on typical telemetry data.

See `benchmark-results.md` for detailed comparisons.

---
Created: 2026-01-16
