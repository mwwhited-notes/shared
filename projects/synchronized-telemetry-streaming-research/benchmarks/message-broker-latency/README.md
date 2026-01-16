# Message Broker Latency Benchmark

## Methodology
Measure end-to-end latency (producer → broker → consumer) for Kafka, NATS, and Pulsar.

## Test Configuration
- Message sizes: 100B, 1KB, 10KB, 100KB
- Broker configurations: default, optimized for latency, optimized for throughput
- Replication factors: 1, 3

## Key Findings
- NATS: Lowest latency (sub-millisecond)
- Kafka: Highest throughput, mid-range latency
- Pulsar: Balanced performance

See `benchmark-results.md` for latency distributions and charts.

---
Created: 2026-01-16
