# Configuration Templates for Production Deployment

## Kafka Broker Configuration (server.properties)

```properties
# High throughput, balanced latency
num.network.threads=8
num.io.threads=8
num.replica.fetchers=2
socket.send.buffer.bytes=102400
socket.receive.buffer.bytes=102400
socket.request.max.bytes=104857600

# Replication and durability
min.insync.replicas=2
default.replication.factor=3
unclean.leader.election.enable=false

# Retention
log.retention.hours=168
log.segment.bytes=1073741824
compression.type=snappy

# Performance
auto.leader.rebalance.enable=true
```

## InfluxDB Configuration

```yaml
[data]
  dir = "/var/lib/influxdb"
  wal-dir = "/var/lib/influxdb/wal"
  wal-enable = true
  
[retention]
  enabled = true
  check-interval = "24h"

[http]
  bind-address = ":8086"
  auth-enabled = true
```

## Prometheus Configuration

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'kafka-broker'
    static_configs:
      - targets: ['localhost:9308']
```

## Docker Compose Stack

See `examples/configs/` for complete docker-compose.yaml

---
Created: 2026-01-16
