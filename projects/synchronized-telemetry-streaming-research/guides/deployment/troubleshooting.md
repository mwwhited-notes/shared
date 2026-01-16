# Troubleshooting Guide for Production Deployments

## Common Issues

### Kafka
- **Broker not starting**: Check `logs/` directory, verify disk space
- **High consumer lag**: Increase consumer parallelism, check broker performance
- **Rebalancing storms**: Check topic configuration, broker CPU usage

### InfluxDB
- **Out of memory**: Check cardinality with `SHOW FIELD KEYS`, adjust retention
- **Slow queries**: Add indices on commonly queried tags
- **Compaction delays**: Increase system limits with `ulimit -n 65536`

### Grafana
- **Timeout errors**: Increase query timeout in data source settings
- **Memory leak**: Check for runaway queries, restart service regularly

## Diagnostic Commands

```bash
# Kafka consumer lag
kafka-consumer-groups.sh --bootstrap-server localhost:9092 \
  --group analysis_group --describe

# InfluxDB cardinality
curl -G 'http://localhost:8086/query' \
  --data-urlencode 'db=telemetry' \
  --data-urlencode 'q=SHOW FIELD KEYS'

# System resource monitoring
watch -n 1 'free -h && df -h'
```

## Performance Tuning

1. **Kafka**: Increase `num.io.threads`, tune batch size
2. **InfluxDB**: Enable WAL, tune cache size
3. **Network**: Check MTU size, verify no packet loss
4. **System**: Tune kernel parameters for network performance

---
Created: 2026-01-16
