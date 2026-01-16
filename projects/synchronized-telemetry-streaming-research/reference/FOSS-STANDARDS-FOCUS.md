# FOSS & Open Standards Focus

This document prioritizes free and open-source software (FOSS) and open standards for blob/stream storage and event streaming, with commercial/proprietary options noted as alternatives.

## Table of Contents

- [Philosophy](#philosophy)
- [FOSS Event Streaming Solutions](#foss-event-streaming-solutions)
- [FOSS Storage Solutions](#foss-storage-solutions)
- [FOSS Databases (Time-Series)](#foss-databases-time-series)
- [Commercial/Platform-Specific Options (For Comparison)](#commercialplatform-specific-options-for-comparison)
- [FOSS Recommended Stacks](#foss-recommended-stacks)
- [FOSS Project Status & Sustainability](#foss-project-status--sustainability)
- [Compliance & Academic Use](#compliance--academic-use)
- [Recommendation Summary](#recommendation-summary)
- [Resources](#resources)

## Philosophy

**Primary Recommendation:** FOSS + Open Standards
- Freedom to use, modify, redistribute
- Community-driven development
- No vendor lock-in
- Transparent development
- Long-term sustainability (not tied to company viability)

**Alternative:** Commercial options
- Listed for comparison
- Better support (sometimes)
- Proprietary optimizations (sometimes)
- Cloud integration (sometimes)

---

## FOSS Event Streaming Solutions

### ✅ PRIMARY RECOMMENDATIONS (FOSS + Open Standards)

#### 1. NATS (Cloud Native Computing Foundation)

**Status:** FOSS | **License:** Apache 2.0 | **GitHub:** [NATS](https://github.com/nats-io/nats-server)

**Open Standards:**
- NATS Protocol (open specification)
- JetStream (streaming layer, open protocol)
- NATS CLI (standard tooling)

**Deployment:**
- Self-hosted (complete control)
- Kubernetes (CNCF project, works everywhere)
- Cloud-agnostic (no vendor lock-in)

**Strengths:**
✅ Open standards (not proprietary protocol)
✅ FOSS (Apache 2.0, development transparent)
✅ Minimal dependencies (single binary)
✅ CNCF graduated project (backed by Linux Foundation)
✅ Active community
✅ Excellent documentation
✅ No telemetry/phone-home

**Perfect for Telemetry:**
- IoT sensors (lightweight, MQTT support)
- Edge computing (minimal footprint)
- Multi-node research clusters
- Data center monitoring

**Integration with Research:**
```
Sensors → NATS → LSL or HDF5 archive
        → Real-time dashboard (Grafana)
        → S3/MinIO long-term storage
```

---

#### 2. Apache Kafka (Apache Software Foundation)

**Status:** FOSS | **License:** Apache 2.0 | **GitHub:** [Kafka](https://github.com/apache/kafka)

**Open Standards:**
- Kafka Protocol (fully documented, open-source reference)
- Topic/Partition model (well-specified)
- Consumer Group Protocol (open spec)

**Strengths:**
✅ Industry standard (battle-tested)
✅ FOSS (Apache 2.0)
✅ Open protocol (many implementations)
✅ Mature ecosystem
✅ Strong community

**Limitations:**
❌ Operational complexity (JVM, ZooKeeper/KRaft)
❌ Resource intensive
❌ Overkill for small deployments

**When appropriate:**
- Large-scale data pipelines (TB/day)
- Existing Kafka investment
- Need for exactly-once processing

---

#### 3. RabbitMQ (Mozilla Public License 2.0)

**Status:** FOSS | **License:** MPL 2.0 | **GitHub:** [RabbitMQ](https://github.com/rabbitmq/rabbitmq-server)

**Open Standards:**
- AMQP 1.0 (ISO/IEC 19464 standard protocol)
- MQTT (IoT standard)
- STOMP (open protocol)
- HTTP management API (open)

**Strengths:**
✅ FOSS (MPL 2.0, full source available)
✅ Open protocols (AMQP, MQTT, not proprietary)
✅ Proven, mature
✅ Multi-protocol support
✅ Excellent for IoT (MQTT)
✅ Smaller footprint than Kafka

**Perfect for Research:**
- Sensor networks (MQTT support)
- IoT integration
- Multi-protocol environments
- Microservices communication

---

#### 4. Apache Pulsar (Apache Software Foundation)

**Status:** FOSS | **License:** Apache 2.0 | **GitHub:** [Pulsar](https://github.com/apache/pulsar)

**Open Standards:**
- Pulsar Protocol (open specification)
- Managed Ledger (consensus protocol, documented)
- BookKeeper (append-only log, open standard)

**Strengths:**
✅ FOSS (Apache 2.0)
✅ Open protocols
✅ Geo-replication native
✅ Multi-tenancy built-in
✅ Apache ecosystem

**When appropriate:**
- Multi-region deployments
- Geo-distributed research
- Kafka-scale needs + replication

---

#### 5. Redis (BSD 3-Clause License)

**Status:** FOSS | **License:** BSD 3-Clause | **GitHub:** [Redis](https://github.com/redis/redis)

**Open Standards:**
- Redis Serialization Protocol (RESP - open specification)
- Redis Streams (open protocol)
- Redis Pub/Sub (open protocol)

**Strengths:**
✅ FOSS (BSD 3-Clause, permissive)
✅ Open protocols
✅ Simple, lightweight
✅ Multi-purpose (cache + streams)
✅ Excellent for small-medium scale

**Perfect for Research:**
- Real-time telemetry + caching
- Small to medium deployments
- Developers already familiar with Redis

---

### ✅ RECOMMENDED (In-Process FOSS)

#### LMAX Disruptor

**Status:** FOSS | **License:** Apache 2.0 | **GitHub:** [Disruptor](https://github.com/LMAX-Exchange/disruptor)

**Open Standards:**
- Ring buffer algorithm (well-documented)
- Lock-free patterns (published research)
- No proprietary components

**Strengths:**
✅ FOSS (Apache 2.0)
✅ Open algorithms (from academic research)
✅ Transparent implementation
✅ No vendor lock-in
✅ Widely studied/understood

**Perfect for Research:**
- Ultra-low latency telemetry (microsecond-scale)
- Real-time signal processing
- High-frequency data streams

---

#### Chronicle Queue (OpenHFT)

**Status:** FOSS | **License:** CeCILL 3.0 | **GitHub:** [Chronicle-Queue](https://github.com/OpenHFT/Chronicle-Queue)

**Open Standards:**
- Memory-mapped file format (documented)
- Multi-process IPC (standard patterns)
- Chronicle data format (open spec)

**Strengths:**
✅ FOSS (CeCILL 3.0, GPL-compatible)
✅ Open format
✅ Ultra-low latency IPC
✅ Persistence built-in
✅ Used in financial systems

**Perfect for Research:**
- Multi-process synchronization
- Persistent local IPC
- Distributed sensor nodes (one per machine)

---

## FOSS Storage Solutions

### ✅ PRIMARY RECOMMENDATIONS

#### HDF5 (NCSA - University of Illinois)

**Status:** FOSS | **License:** BSD-like (NCSA license) | **Home:** [HDF Group](https://www.hdfgroup.org/)

**Open Standard:**
- HDF5 format specification (published, open)
- Multiple independent implementations
- NASA/NOAA standard

**Strengths:**
✅ FOSS (permissive license)
✅ Open format (no vendor control)
✅ Scientific standard (NASA approved)
✅ Excellent for arrays/matrices
✅ Rich ecosystem (Python, MATLAB, C/C++, Java)

**Perfect for Research:**
- Scientific simulations
- Experimental data archival
- Multi-dimensional arrays
- High-resolution video frames

---

#### NetCDF (Unidata - University Corporation for Atmospheric Research)

**Status:** FOSS | **License:** BSD 3-Clause | **Home:** [Unidata NetCDF](https://www.unidata.ucar.edu/software/netcdf/)

**Open Standard:**
- NetCDF-4 format (based on HDF5 + CF conventions)
- CF Conventions (Climate & Forecast, community-driven)
- Complete specification available

**Strengths:**
✅ FOSS (BSD 3-Clause)
✅ Open format (standards-based)
✅ Climate/weather standard
✅ Interoperability (CF conventions)
✅ Cross-platform tools

**Perfect for Research:**
- Climate/weather data
- Geospatial time-series
- Standards-compliant archival

---

#### Apache Parquet

**Status:** FOSS | **License:** Apache 2.0 | **GitHub:** [Parquet](https://github.com/apache/parquet-format)

**Open Standard:**
- Parquet format specification (public, versioned)
- Dremel encoding (Google published research)
- Language-agnostic spec

**Strengths:**
✅ FOSS (Apache 2.0)
✅ Open format (multiple implementations)
✅ Excellent compression
✅ Industry standard (Spark, Pandas, Arrow)
✅ Analytical queries optimized

**Perfect for Research:**
- Data lake storage
- Analytics queries
- Machine learning training
- Archive for analysis

---

#### XDF (Lab Streaming Layer)

**Status:** FOSS | **License:** BSD 3-Clause | **GitHub:** [XDF](https://github.com/sccn/xdf)

**Open Standard:**
- XDF format specification (documented, open)
- Multi-stream timestamp precision (published)
- XML metadata (standard)

**Strengths:**
✅ FOSS (BSD 3-Clause)
✅ Open format
✅ Purpose-built for research
✅ Multimodal support
✅ Exact timing for synchronization

**Perfect for Research:**
- EEG/neuroscience recordings
- Multimodal synchronized data
- Academic standard (SCCN)

---

#### Apache Arrow

**Status:** FOSS | **License:** Apache 2.0 | **GitHub:** [Arrow](https://github.com/apache/arrow)

**Open Standard:**
- Arrow columnar format (published specification)
- IPC protocol (documented)
- Language-agnostic

**Strengths:**
✅ FOSS (Apache 2.0)
✅ Open format
✅ In-memory + streaming
✅ Zero-copy interoperability
✅ Multi-language support

**Perfect for Research:**
- Data interchange between tools
- Real-time stream processing
- Cross-language pipelines

---

### Self-Hosted FOSS Storage

#### MinIO (AGPL 3.0)

**Status:** FOSS | **License:** AGPL 3.0 (commercial license available) | **GitHub:** [MinIO](https://github.com/minio/minio)

**Open Standard:**
- S3-compatible API (open protocol)
- MinIO extensible via plugins
- Object storage standard (de facto)

**Strengths:**
✅ FOSS (AGPL 3.0 - freedom to modify)
✅ Open protocol (S3 compatible)
✅ Full data control (self-hosted)
✅ No egress costs
✅ On-premises or cloud

**Perfect for Research:**
- Private blob storage
- Data sovereignty (no cloud vendor)
- Local backup/archive
- Research data repositories

**Note:** AGPL means if you modify and deploy, you must release source. Use community FOSS license for simplicity, or contact MinIO for commercial license.

---

#### Ceph (Apache 2.0 + LGPL)

**Status:** FOSS | **License:** Mix (Apache 2.0, LGPL) | **GitHub:** [Ceph](https://github.com/ceph/ceph)

**Open Standard:**
- RADOS protocol (documented)
- Crush algorithm (published research)
- RGW S3 API (open, compatible)

**Strengths:**
✅ FOSS (open licenses)
✅ Open protocols
✅ Enterprise-grade (large deployments)
✅ Self-healing
✅ Multiple interfaces (block, object, file)

**Perfect for Research:**
- Large research data centers
- Multi-institution storage
- Data redundancy without clouds
- Complete infrastructure control

---

#### PostgreSQL + TOAST/BYTEA

**Status:** FOSS | **License:** PostgreSQL License (permissive) | **GitHub:** [PostgreSQL](https://github.com/postgres/postgres)

**Open Standard:**
- SQL standard (ISO/IEC 9075)
- TOAST mechanism (documented in source)
- BYTEA binary type (standard SQL)

**Strengths:**
✅ FOSS (PostgreSQL License - permissive)
✅ Open standard (SQL)
✅ Proven, reliable
✅ Multi-purpose (queries + blobs)
✅ Excellent for structured data + attachments

**Perfect for Research:**
- Research database + attachments
- Experiment metadata + files
- Structured data with blobs
- Standard SQL interface

---

## FOSS Databases (Time-Series)

### ✅ PRIMARY RECOMMENDATIONS

#### TimescaleDB (Apache 2.0 + Community License)

**Status:** FOSS | **License:** Apache 2.0 (core) + Community License (enterprise features) | **GitHub:** [TimescaleDB](https://github.com/timescale/timescaledb)

**Open Standard:**
- PostgreSQL extension (SQL standard)
- Hypertable optimization (published research)
- Standard SQL interface

**Strengths:**
✅ FOSS (Apache 2.0 core)
✅ Open standard (PostgreSQL extension)
✅ High-cardinality support (many sensors)
✅ Standard SQL (easy learning)
✅ Proven at scale

**Perfect for Research:**
- Multi-sensor time-series
- SQL queries on telemetry
- Structured + time-series mix
- Long-term analysis

---

#### InfluxDB OSS (AGPL 3.0)

**Status:** FOSS | **License:** AGPL 3.0 (commercial available) | **GitHub:** [InfluxDB](https://github.com/influxdata/influxdb)

**Open Standard:**
- Line Protocol (open, documented)
- InfluxQL (open specification)
- SQL (v3.0+, ISO standard)

**Strengths:**
✅ FOSS (AGPL 3.0 - freedom to modify)
✅ Open protocols
✅ Time-series specialized
✅ Excellent write throughput
✅ Simple deployment

**Perfect for Research:**
- Real-time sensor monitoring
- Low-cardinality streams (few devices)
- Simple dashboards
- Time-series analysis

**Note:** AGPL means source release required if deployed. Alternative: commercial InfluxDB license for convenience.

---

## Commercial/Platform-Specific Options (For Comparison)

Listed as alternatives if FOSS doesn't meet needs:

| Name | License | Type | Notes |
|------|---------|------|-------|
| **Google Pub/Sub** | Proprietary | Cloud | Managed, serverless, vendor lock-in |
| **AWS Kinesis** | Proprietary | Cloud | AWS-specific, egress costs |
| **AWS SQS** | Proprietary | Cloud | Queue only, no streaming |
| **Azure Service Bus** | Proprietary | Cloud | Azure-specific |
| **Confluent Cloud** | Proprietary | Cloud | Managed Kafka + enterprise features |
| **InfluxDB Cloud** | Proprietary | Cloud | Managed InfluxDB, hosted by InfluxData |
| **Datadog** | Proprietary | SaaS | Full observability, expensive |
| **New Relic** | Proprietary | SaaS | Monitoring + streams, vendor lock-in |

**When to consider:**
- Managed services (avoid operations)
- Native cloud integration (Lambda, Cloud Functions)
- Enterprise support contract needed
- Organization already committed to platform

**Caution:**
- Egress charges (exit costs)
- Vendor lock-in
- Data governance restrictions
- Cost scales with volume

---

## FOSS Recommended Stacks

### Stack 1: Full FOSS Research Data Pipeline

```
Data Collection:
  NATS (lightweight transport)
  + MQTT (IoT devices)

Real-time Processing:
  Apache Kafka (if scale demands)
  or Redis Streams (simplicity)

Storage:
  Primary: HDF5 or XDF (research format)
  Archive: MinIO (self-hosted S3-compatible)
  Analysis: Parquet (via Spark, Pandas)

Time-Series:
  TimescaleDB (SQL-based)
  or InfluxDB OSS (time-series specialized)

Visualization:
  Grafana (open-source dashboard)
  + Prometheus (monitoring)

All Components:
  ✅ FOSS
  ✅ Open Standards
  ✅ Data Sovereignty (self-hosted)
  ✅ No Lock-in
  ✅ Research Reproducibility
```

### Stack 2: Lightweight Edge Deployment

```
Edge Device (Sensor):
  NATS (minimal footprint)
  + Chronicle Queue (local persistence)

Central Hub:
  NATS Server (control plane)
  + RabbitMQ (MQTT gateway)

Storage:
  PostgreSQL (local metadata)
  + MinIO (distributed archive)

All Components:
  ✅ FOSS
  ✅ Deployable on Raspberry Pi
  ✅ Multi-site replication
  ✅ No cloud dependency
```

### Stack 3: Ultra-Low Latency Real-Time

```
Telemetry Collection:
  LMAX Disruptor (in-process, microsecond)
  or Chronicle Queue (multi-process IPC)

Network Transport:
  NATS (cloud-native, low latency)

Storage:
  Chronicle Queue (persistent IPC)
  + HDF5 (research archive)

All Components:
  ✅ FOSS
  ✅ Open Algorithms
  ✅ Deterministic Performance
  ✅ Research Reproducibility
```

---

## FOSS Project Status & Sustainability

### **Gold Standard** (Established, Well-Funded)
- ✅ **NATS** - CNCF graduated, Linux Foundation backing
- ✅ **Kafka** - Apache top-level project, wide adoption
- ✅ **PostgreSQL** - Global development community, 25+ years
- ✅ **HDF5** - Government-backed (NCSA), NASA standard
- ✅ **Redis** - Stable, multiple companies contribute
- ✅ **RabbitMQ** - VMware backing, enterprise support available

### **Excellent** (Actively Maintained, Community-Driven)
- ✅ **Pulsar** - Apache project, Datastax/StreamNative backing
- ✅ **TimescaleDB** - Timescale Inc. employs core maintainers
- ✅ **Arrow** - Apache project, industry consensus
- ✅ **MinIO** - Commercial company, active development
- ✅ **Ceph** - OpenStack backing, enterprise deployments
- ✅ **NetCDF** - UCAR university backing

### **Stable** (Community Maintained, Mature)
- ✅ **Disruptor** - LMAX active, stable since 2011
- ✅ **Chronicle Queue** - OpenHFT maintains
- ✅ **InfluxDB OSS** - Still supported, older versions stable

---

## Compliance & Academic Use

All recommended FOSS projects acceptable for:
- Academic research (no license restrictions)
- Government use (many preferred)
- Commercial use (check license compatibility)
- Data sovereignty requirements (self-hosted)
- Reproducible research (open-source auditable)
- Regulatory compliance (no vendor lock-in)

---

## Recommendation Summary

### **Best for Research:** NATS + HDF5/XDF + TimescaleDB

| Component | Choice | Why |
|-----------|--------|-----|
| **Messaging** | NATS | FOSS, open standard, lightweight, CNCF |
| **Primary Storage** | HDF5 or XDF | FOSS, open formats, research standard |
| **Time-Series** | TimescaleDB | FOSS, SQL standard, high-cardinality |
| **Archive** | MinIO | FOSS, self-hosted S3, no egress costs |
| **Backup** | Ceph or Tar | FOSS, self-hosted, data control |
| **Visualization** | Grafana | FOSS, works with any data source |

### **All components:**
✅ FOSS (Apache 2.0, BSD, PostgreSQL License)
✅ Open Standards (no proprietary protocols)
✅ Self-Hosted (complete data control)
✅ No Vendor Lock-in (can switch components)
✅ Research Reproducible (transparent, auditable)
✅ Cost-Effective (free software + infrastructure)

---

## Resources

### FOSS Project Homes
- [NATS.io](https://nats.io/)
- [Apache Kafka](https://kafka.apache.org/)
- [Apache Pulsar](https://pulsar.apache.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/)
- [RabbitMQ](https://www.rabbitmq.com/)
- [HDF Group](https://www.hdfgroup.org/)
- [Unidata NetCDF](https://www.unidata.ucar.edu/)
- [Apache Arrow](https://arrow.apache.org/)
- [TimescaleDB](https://www.timescale.com/)
- [InfluxDB OSS](https://www.influxdata.com/open-source/)
- [MinIO](https://min.io/)
- [Ceph](https://ceph.io/)

### FOSS Communities
- [Linux Foundation](https://www.linuxfoundation.org/)
- [Apache Software Foundation](https://www.apache.org/)
- [Cloud Native Computing Foundation](https://www.cncf.io/)
- [OpenStack Foundation](https://www.openstack.org/)

### Research Standards
- [Lab Streaming Layer](https://github.com/sccn/labstreaminglayer) - Neuroscience standard
- [WARC Format](https://www.loc.gov/preservation/digital/formats/fdd/fdd000236.shtml) - Archival standard (ISO 28500)
- [POSIX Standards](https://pubs.opengroup.org/onlinepubs/9699919799/) - Operating system standard

---

*Last updated: 2026-01-16*

*Philosophy: Free and open-source software (FOSS) + open standards as primary recommendations, with commercial options noted for specific scenarios.*

*Part of: [Synchronized Telemetry Streaming Research](README.md)*
