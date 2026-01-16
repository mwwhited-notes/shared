# Time-Series Database Cardinality Performance Benchmark

## Databases Tested
- InfluxDB 2.x
- TimescaleDB
- QuestDB
- Prometheus

## Cardinality Levels
Test ingestion and query performance with:
- 1K series
- 10K series
- 100K series
- 1M series

## Key Results
- QuestDB: Best for high cardinality (1M+)
- TimescaleDB: SQL compatibility with good cardinality support
- InfluxDB: Ease of use, moderate cardinality limits

See `benchmark-results.md` for performance tables.

---
Created: 2026-01-16
