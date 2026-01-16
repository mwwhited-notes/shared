# RaptorQ Overhead vs Alternatives Benchmark

## Methodology
Compare RaptorQ (RFC 6330) against Reed-Solomon, FECFRAME, and LDPC across various packet loss rates.

## Test Scenarios
- File sizes: 1 MB, 10 MB, 100 MB, 1 GB
- Loss rates: 1%, 5%, 10%, 20%, 30%
- Symbol sizes: 16B, 64B, 256B

## Results Summary
RaptorQ optimal for loss >5%, FECFRAME better for streaming <10% loss.

See `benchmark-results.md` for detailed tables and charts.

---
Created: 2026-01-16
