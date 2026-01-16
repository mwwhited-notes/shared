# Synchronized Telemetry Streaming Research - Project Index

## Table of Contents

- [Quick Navigation](#quick-navigation)
- [What This Project Contains](#what-this-project-contains)
- [Use Case Quick-Start](#use-case-quick-start)
- [What's Documented](#whats-documented)
- [Key Documents](#key-documents)
- [Related Projects](#related-projects)
- [Download Status](#download-status)
- [Next Steps](#next-steps)

## Quick Navigation

### Core Documentation

| Document | Purpose | Audience |
|----------|---------|----------|
| **[README.md](README.md)** | Project overview, research focus areas, status | Project leads, planners |
| **[RESEARCH_BIBLIOGRAPHY.md](RESEARCH_BIBLIOGRAPHY.md)** | Comprehensive RFC/standard index with cross-references | Researchers, implementers |
| **[event-streaming-and-blob-transfer.md](event-streaming-and-blob-transfer.md)** | Standards for event streams and large file transfer | Engineers selecting technologies |
| **[out-of-order-blob-transfer.md](out-of-order-blob-transfer.md)** | Out-of-order packet protocols (RaptorQ, QUIC, SCTP) | System designers, network engineers |

---

## What This Project Contains

### 1. Research Bibliography ✅

A structured, cross-referenced database of:
- **19 RFCs** covering streaming, synchronization, error correction, transport
- **7 major standards** (CloudEvents, OpenTelemetry, IEEE 1588, MQTT, AMQP 1.0, H.264/265, Opus)
- **12+ academic research papers** on fountain codes, event sourcing, real-time systems
- **100+ implementation resources** (libraries, tools, language bindings)
- **Cross-references** to 8 active projects in this notebook

**Total Standards Documented:** 40+

### 2. Key Findings

#### Don't Build Your Own
- Custom binary format (breaks Year 2)
- Simple FEC (only works ordered)
- Direct TCP (HoL blocking on loss)
- Cost: 100-1000 hours of rework

#### Use Standards Instead
- **RaptorQ (RFC 6330)** - Fountain codes (recover from ANY packet subset)
- **QUIC (RFC 9000)** - Modern transport with encryption
- **Kafka** - Immutable logs for research replay
- **LSL** - Purpose-built for neuroscience multimodal recording
- **CloudEvents** - Unified telemetry envelope

---

## Use Case Quick-Start

### EEG + Video
→ **LSL + XDF + OBS Studio + S3 multipart**

### SCPI Instruments + Sensors
→ **Kafka + Avro + Grafana dashboard**

### Multi-Receiver Radar
→ **IEEE 1588 PTP + RaptorQ (RFC 6330) + HDF5**

### Real-Time Streaming
→ **QUIC (RFC 9000) or RTSP 2.0 (RFC 7826)**

---

## What's Documented

✅ 40+ standards (RFCs, IEEE, CNCF, MQTT, etc.)
✅ Comparison matrices (tech selection guide)
✅ Cross-references to 8 repository projects
✅ Implementation resources (100+ links)
✅ Academic papers (12+ citations)
✅ Out-of-order protocols (RaptorQ deep dive)
✅ Event streaming standards (Kafka, RabbitMQ, MQTT)
✅ Synchronization (NTP, PTP, RTP timestamps)

---

## Key Documents

**[RESEARCH_BIBLIOGRAPHY.md](RESEARCH_BIBLIOGRAPHY.md)**
- Complete RFC/standard catalog
- Cross-references to projects in this notebook
- Implementation resources for each standard
- Academic papers and theory

**[event-streaming-and-blob-transfer.md](event-streaming-and-blob-transfer.md)**
- CloudEvents envelope format
- Kafka event sourcing pattern
- S3/BitTorrent/IPFS blob transfer
- Serialization format comparison

**[out-of-order-blob-transfer.md](out-of-order-blob-transfer.md)**
- RaptorQ fountain codes (recover from ANY subset)
- FECFRAME + sliding window FEC
- QUIC, SCTP, DCCP protocols
- Practical implementation patterns

---

## Related Projects

**Will benefit directly:**
- [SCPI Instrument Control](../../projects/scpi-instrument-control/) - Use LSL sink or Kafka
- [ScoreMachine](../../projects/scoremachine/) - Adopt RaptorQ for backup
- [Passive Radar SDR](../../projects/passive-radar-sdr/) - RaptorQ for multi-receiver
- [Radex Protocol](../../projects/radex-one-protocol-reverse-engineering/) - Gateway pattern

**Will contribute to:**
- [DevOps Cluster](../../projects/devops-playground-cluster/) - Stream processing
- [Home Automation](../../projects/home-automation/) - Sensor patterns
- [Analog Computing](../../AnalogComputers/) - Signal understanding

---

## Download Status

**In `/documents/` folder (8 files):**
- RFC 7826 (RTSP 2.0)
- RFC 8108 (Multiple RTP)
- RFC 8861 (RTP Multi-Stream RTCP)
- RFC 6051 (Rapid RTP Sync)
- RFC 9232 (Network Telemetry)
- RFC 7233 (HTTP Range)
- CloudEvents Spec
- BitTorrent v2 (BEP 52)

**Recommended downloads** (links in RESEARCH_BIBLIOGRAPHY.md):
- RFC 9000 (QUIC)
- RFC 6330 (RaptorQ)
- RFC 9260 (SCTP)
- OpenTelemetry Protocol Spec

---

## Next Steps

**Phase 1 (Current): Research Complete** ✅
- Comprehensive RFC survey
- Comparison matrices
- Project cross-references
- Quick-start guides

**Phase 2: Architecture Design**
- PlantUML diagrams
- Decision trees
- Integration guides
- Proof-of-concept

**Phase 3: Implementation**
- Reference code
- Benchmarks
- Deployment checklist
- Troubleshooting guide

---

*Last updated: 2026-01-16*

*Status: Phase 1 Complete - Ready for Phase 2 (Architecture & POC)*
