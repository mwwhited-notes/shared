# Hardware Requirements for Telemetry Deployments

## Workload Profiles

### Light Deployment (10 sensors, 100 msgs/sec, 1-day retention)
**Single Server**
- CPU: 4 cores (2.4 GHz)
- RAM: 8 GB
- Storage: 100 GB SSD
- Network: 1 Gbps Ethernet
- Example: Intel i5, 8GB RAM machine

**Estimated costs:**
- Server: $500-1000
- Networking: $200

### Medium Deployment (100 sensors, 10K msgs/sec, 30-day retention)
**3-Node Kafka Cluster**
- CPU per node: 8 cores (2.4 GHz)
- RAM per node: 32 GB
- Storage per node: 2 TB NVMe SSD
- Network: 10 Gbps (recommended)
- Load Balancer: Hardware or software

**Broker specifications:**
- Kafka replication: 2x
- InfluxDB retention: 30 days
- Compression: snappy

**Estimated costs:**
- Servers: $2000-3000/node × 3 = $6K-9K
- Networking: $1K-2K
- Total: $7K-11K

### Heavy Deployment (1000+ sensors, 100K+ msgs/sec, 1-year retention)
**5+ Node Kafka Cluster + Separate Storage**
- Broker nodes: 8-16 cores, 64 GB RAM each
- Storage nodes: 32+ cores, 256 GB RAM, 50+ TB storage
- Network: 10+ Gbps with redundancy
- Monitoring: Prometheus + Grafana cluster

**Estimated costs:**
- Infrastructure: $20K-50K
- Per-year storage: $5K-15K

## Storage Sizing

Formula: `msgs_per_sec × avg_msg_size × retention_days × 86400 × compression_ratio`

Example: 10K msgs/sec, 1 KB/msg, 30-day retention, 0.5 compression ratio
```
10,000 × 1,000 × 30 × 86,400 × 0.5 = 12.96 TB
```

## Network Requirements

- **Peak ingestion**: msgs/sec × avg_msg_size × replication_factor
- **Consumer bandwidth**: 2-3× ingestion rate
- **Recommended NIC**: 10 Gbps for medium/heavy

## References
- Deployment patterns: `guides/deployment/configuration-templates.md`
- Troubleshooting: `guides/deployment/troubleshooting.md`

---
Created: 2026-01-16
