# Event Streaming & Large Blob Transfer Standards

Comprehensive guide to standardized approaches for telemetry event streaming and large data transfer—why "rolling your own" introduces risk and complexity.

## Table of Contents

1. [Event Streaming Standards](#event-streaming-standards)
2. [Large Blob Transfer Standards](#large-blob-transfer-standards)
3. [Serialization Formats for Telemetry](#serialization-formats-for-telemetry)
4. [Recommended Stacks by Use Case](#recommended-stacks-by-use-case)
5. [Why Standards Matter](#why-standards-matter)

---

## Event Streaming Standards

### CloudEvents (CNCF Standard)

**Status:** Graduated project (Jan 2024) | **Version:** 1.0+

[CloudEvents Specification](https://cloudevents.io/) | [GitHub](https://github.com/cloudevents/spec)

**What it is:**
A vendor-neutral specification for describing event data in a common format for interoperability across services, platforms, and systems. Think of it as the RFC for "how to structure an event message."

**Required Attributes:**
```json
{
  "specversion" : "1.0",
  "type" : "com.example.sensor.telemetry",
  "source" : "/sensor/eeg-device-001",
  "id" : "A234-1234-1234",
  "time" : "2026-01-16T12:34:56.789Z",
  "datacontenttype" : "application/avro",
  "data" : { /* binary sensor data */ }
}
```

**Protocol Bindings:**
- HTTP (with JSON or binary encoding)
- AMQP (RabbitMQ)
- Kafka
- MQTT
- gRPC

**Why use it:**
- ✅ Interoperability across tools (one format, many brokers)
- ✅ Time information standardized (crucial for telemetry)
- ✅ Rich metadata support (source, subject, datacontenttype)
- ✅ Extensible (custom attributes allowed)
- ✅ Industry adoption: AWS EventBridge, Google Cloud Eventarc, Knative, Argo, Falco

**When NOT to use:**
- Very high-frequency data (>10,000 Hz per sensor) where envelope overhead matters
- Pure binary streaming with no metadata
- Embedded systems with <1KB memory

### Apache Kafka (Distributed Event Streaming Platform)

**Status:** Production-ready | **Maturity:** 15+ years battle-tested

[Apache Kafka](https://kafka.apache.org/) | [Event Sourcing with Kafka](https://www.confluent.io/blog/event-sourcing-cqrs-stream-processing-apache-kafka-whats-connection/)

**What it is:**
A distributed, horizontally-scalable log that stores immutable sequences of events. Not a message queue (guarantees order, replay, durability).

**Core Concepts:**
- **Topics:** Named streams (e.g., `sensors/eeg/device-001`)
- **Partitions:** Distributed across brokers (parallelism + fault tolerance)
- **Consumer Groups:** Multiple readers can independently consume same events
- **Retention:** Configurable (hours, days, GB, or forever)
- **Replication:** Each partition replicated across N brokers (durability)

**Guarantees:**
```
At-least-once delivery
Exactly-once semantics (within transaction)
Order within partition
No message loss (if replicated)
Instant replay from any point in time
```

**Architecture for Telemetry:**

```
┌─────────────────────────────────────────────────────┐
│ Event Sources (Sensors, SCPI Instruments, etc.)     │
└────────────────┬────────────────────────────────────┘
                 │ Kafka Producer
                 ▼
    ┌────────────────────────────────┐
    │ Kafka Cluster (3+ brokers)     │
    │ ┌──────────────────────────┐   │
    │ │ Topic: eeg.raw           │   │ Replication: 3
    │ │ Partition 0: [event...]  │   │ Retention: 7 days
    │ │ Partition 1: [event...]  │   │
    │ └──────────────────────────┘   │
    │ ┌──────────────────────────┐   │
    │ │ Topic: video.metadata    │   │ (Overlay data)
    │ │ Partition 0: [event...]  │   │
    │ └──────────────────────────┘   │
    └────────────────────────────────┘
      ▲             ▲              ▲
      │             │              │
 ┌────┴──────┐  ┌───┴─────────┐  ┌─┴───────────┐
 │ Consumer  │  │ Stream Proc │  │ Analytics   │
 │ (Recorder)│  │ (Filters)   │  │ (Dashboard) │
 └───────────┘  └─────────────┘  └─────────────┘
```

**Use with Event Sourcing & CQRS:**

Kafka excels at Event Sourcing (storing ALL state changes):

```
Command Side (Write):          Query Side (Read):
┌──────────────────┐          ┌──────────────────┐
│ Device Data In   │          │ Read Models      │
│ (measurements)   │          │ (dashboards,     │
└────────┬─────────┘          │  reports)        │
         │ Events             │                  │
         ▼                    │
    Kafka Topic               │ (separately scaled)
    (immutable log)           │
         │                    │
         └────────────────────┘
         Offset/Replay

Benefit: Can replay entire history to rebuild state
         without re-running original sensors
```

**Why use it:**
- ✅ Durability (no lost telemetry)
- ✅ Replay capability (critical for research)
- ✅ Horizontal scalability (add brokers, add capacity)
- ✅ Consumer flexibility (multiple independent readers)
- ✅ Stream processing (Kafka Streams, Apache Flink)
- ✅ Proven at scale (billions of events/day at Netflix, Uber, etc.)

**When to use:**
- ✅ Research projects where re-analysis is expected
- ✅ Multi-hour or multi-day recording sessions
- ✅ Multiple simultaneous consumers (live view + recording + analysis)
- ✅ Need for audit trail

**When NOT to use:**
- Very low latency critical (<5ms end-to-end)
- Single-sensor, single-consumer scenarios (overkill)
- Embedded systems (requires Java/JVM)

### RabbitMQ (Message Broker + Streams)

**Status:** Production-ready | **Maturity:** 15+ years

[RabbitMQ](https://www.rabbitmq.com/) | [AMQP Standard](https://en.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol)

**What it is:**
A lightweight message broker implementing AMQP 1.0 (ISO/IEC 19464). Can work as traditional queue or stream system.

**Modes:**
1. **Queue Mode:** First-in-first-out, single consumer per message
2. **Stream Mode:** Multiple independent consumers (new in RabbitMQ 3.13)

**Supported Protocols:**
- AMQP 0.9.1, AMQP 1.0 (ISO standard)
- MQTT (IoT telemetry)
- STOMP (simple text protocol)
- HTTP management API

**Why use it:**
- ✅ Lightweight (Python, Node.js friendly)
- ✅ Supports multiple protocol bindings
- ✅ Good for mixed IoT + traditional app scenarios
- ✅ Lower operational overhead than Kafka

**When to use:**
- ✅ Sensor networks with MQTT devices
- ✅ Real-time alerting on telemetry
- ✅ Task queues (one sensor → one processor)
- ✅ Cloud-native (runs in Kubernetes)

**When NOT to use:**
- ❌ Need for replay/event sourcing
- ❌ Multi-month retention
- ❌ Horizontal scaling to 1000+ nodes

---

## Large Blob Transfer Standards

### HTTP Range Requests (RFC 7233)

**Status:** Standard | **RFC:** [RFC 7233](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Range_requests)

**What it is:**
HTTP protocol feature allowing clients to request specific byte ranges from a server. Foundation for resumable downloads.

**Example Request:**
```http
GET /video.mp4 HTTP/1.1
Host: archive.example.com
Range: bytes=0-1023999
```

**Server Response:**
```http
HTTP/1.1 206 Partial Content
Content-Length: 1024000
Content-Range: bytes 0-1023999/1000000000
Content-Type: video/mp4

[1MB of video data]
```

**Features:**
- ✅ Resume interrupted downloads
- ✅ Parallel chunk downloading
- ✅ Seek into large files without downloading all preceding data
- ✅ Byte-accurate (0-based inclusive ranges)

**Why use it:**
- ✅ Standardized (all HTTP/1.1+ servers support)
- ✅ Simple implementation (no extra library needed)
- ✅ Works with existing CDNs
- ✅ Widely supported browsers

**Limitations:**
- Designed for human-initiated downloads
- Not optimal for coordinated multi-client transfer

### Chunked Transfer Encoding (RFC 9112)

**Status:** Standard | **RFC:** [RFC 9112](https://datatracker.ietf.org/doc/rfc9112/)

**What it is:**
HTTP feature for streaming responses where total size isn't known in advance.

**Format:**
```http
HTTP/1.1 200 OK
Transfer-Encoding: chunked
Content-Type: video/mp4

[size in hex]\r\n
[chunk data]\r\n
[size in hex]\r\n
[chunk data]\r\n
...
0\r\n
\r\n
```

**Why use it:**
- ✅ Streaming video/sensor data without knowing final size
- ✅ Lower latency (send as available, don't buffer)
- ✅ Works with real-time data sources

### Amazon S3 Multipart Upload (De Facto Standard)

**Status:** Industry standard | **Spec:** [AWS Multipart Upload](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html)

**What it is:**
Protocol pattern for uploading files >100MB as parallel chunks, with automatic assembly and retry capability.

**How it works:**

```
1. Initiate upload
   POST /video.mp4?uploads
   Response: UploadID=xyz

2. Upload parts in parallel
   PUT /video.mp4?partNumber=1&uploadId=xyz
   PUT /video.mp4?partNumber=2&uploadId=xyz
   ...
   Response: ETag for each part

3. Complete upload
   POST /video.mp4?uploadId=xyz
   <Complete with ETag list>

4. Server combines parts
```

**Key Features:**
- ✅ Parallel uploads (5-100x faster for large files)
- ✅ Automatic retry per part (not entire file)
- ✅ Progress tracking (per part)
- ✅ Multipart size: 5 MB - 5 GB per part, up to 10,000 parts = 50 TB total

**Why use it:**
- ✅ Universal (every cloud provider supports this pattern)
- ✅ Fault-tolerant (resume failed parts only)
- ✅ Tuned for slow/unreliable networks

**Implementations:**
- AWS S3 (native)
- Azure Blob Storage (equivalent: block blobs)
- Google Cloud Storage (resumable uploads)
- MinIO (S3-compatible self-hosted)
- B2, Backblaze (S3-compatible API)

**When to use:**
- ✅ Video file archival
- ✅ Research data backup to cloud
- ✅ Network unreliable (slow connections)
- ✅ Need for checksum verification per part

### IPFS (InterPlanetary File System)

**Status:** Emerging standard | **Spec:** [IPFS Paper](https://ipfs.io/), [BitSwap](https://docs.ipfs.tech/concepts/bitswap/)

**What it is:**
Decentralized P2P file system using content-addressing (hashes). Like BitTorrent + git for files.

**How it works:**

```
File added to IPFS:
┌────────────────┐
│ video.mp4      │
│ (1 GB)         │
└────────────────┘
         ↓ (chunked into blocks)
┌────────────────┐
│ Block 1 (256KB)│ → Hash: Qm...xyz1
│ Block 2 (256KB)│ → Hash: Qm...xyz2
│ Block 3 (256KB)│ → Hash: Qm...xyz3
└────────────────┘
         ↓ (merkle tree)
  Root Hash: Qm...root

Query: GET /ipfs/Qm...root
Response: (assembled from nearest peers)
```

**Features:**
- ✅ Content-addressed (hash-based integrity)
- ✅ P2P distribution (no central server)
- ✅ Instant replication (anyone with hash can seed)
- ✅ Works offline (local cache)
- ✅ Deduplication (identical blocks automatically shared)

**Why use it:**
- ✅ Censorship-resistant archival
- ✅ Distributed backup (no single point of failure)
- ✅ Efficient bandwidth (nodes seed to each other)

**Limitations:**
- Emerging (not yet widespread)
- Requires IPFS daemon
- Slower than direct download
- Long-term reliability unknown

**When to use:**
- ✅ Public research data (want broad distribution)
- ✅ Archival (want decentralized backup)
- ✅ Peer-to-peer sharing within lab network

### BitTorrent (BEP 3 & BEP 52)

**Status:** Mature standard | **Specs:** [BitTorrent v1](https://www.bittorrent.org/beps/bep_0003.html), [BitTorrent v2](https://www.bittorrent.org/beps/bep_0052.html)

**What it is:**
Protocol for peer-to-peer file distribution. Each downloader simultaneously uploads pieces to others.

**How it works:**

```
1. Create .torrent file (metadata)
   - File hashes (v1: SHA-1, v2: SHA-256)
   - Tracker URL
   - File structure

2. Seeders announce to tracker
   - "I have this file"

3. Leechers download
   - Request pieces from multiple peers
   - Verify hashes
   - Simultaneously upload pieces to others

4. Upload/download accelerates
   - Initial: slow (few peers)
   - Later: fast (many peers seeding)
```

**Advantages:**
- ✅ Bandwidth-efficient (peers help distribute)
- ✅ Scales with popularity (more demand = faster download)
- ✅ Works with NAT/firewalls (UTP port mapping)
- ✅ Mature (20+ years proven)
- ✅ No central server needed (trackerless: DHT)

**Limitations:**
- ❌ Slower than direct download initially
- ❌ Requires tracker or DHT
- ❌ Swarm must still have seeders
- ❌ Not designed for streaming

**When to use:**
- ✅ Distributing large research datasets (1GB+)
- ✅ Public release of multi-hour video recordings
- ✅ Dataset redundancy (multiple seeders)
- ✅ Lab-to-lab file transfers (peer discovery via DHT)

**v2 Improvements:**
- SHA-256 (more secure than v1's SHA-1)
- Stronger metadata structure
- Hybrid mode (can support both)

---

## Serialization Formats for Telemetry

### Comparison Matrix

| Format | Schema | Speed | Size | Use Case | Languages |
|--------|--------|-------|------|----------|-----------|
| **Protocol Buffers** | Required | ⚡⚡⚡ | Tiny | Low-latency, high-frequency | All modern |
| **Apache Avro** | Required (embedded) | ⚡⚡ | Small | Kafka/Hadoop ecosystems | Python, Java, C#, JS |
| **MessagePack** | Optional | ⚡⚡ | Small | Embedded, real-time | All modern |
| **JSON** | No | ⚡ | Large | Debugging, web APIs | All |
| **BSON** | Optional | ⚡⚡ | Medium | MongoDB compatibility | All |
| **CBOR** | No | ⚡⚡ | Small | IoT, RFC 8949 standard | All modern |

### Protocol Buffers (Google)

**Best for:** Low-latency telemetry (EEG, SCPI instruments)

```protobuf
syntax = "proto3";

message EEGSample {
  int64 timestamp_us = 1;           // Microsecond precision
  repeated float channels = 2;       // 64 channels @ 250Hz
  int32 sample_counter = 3;
}
```

**Advantages:**
- ✅ Smallest serialized size
- ✅ Fastest encode/decode
- ✅ Strong typing (compile-time checks)
- ✅ Backward/forward compatible evolution

**Disadvantages:**
- ❌ Binary (hard to debug)
- ❌ Requires .proto compilation step
- ❌ Schema evolution rules strict

### Apache Avro

**Best for:** Event streaming (Kafka/Pulsar)

```json
{
  "type": "record",
  "name": "EEGSample",
  "fields": [
    {"name": "timestamp", "type": "long"},
    {"name": "channels", "type": {"type": "array", "items": "float"}},
    {"name": "sample_counter", "type": "int"}
  ]
}
```

**Advantages:**
- ✅ Schema embedded in data (no separate transmission)
- ✅ Excellent compression
- ✅ Native Kafka/Hadoop integration
- ✅ Schema Registry standardization (Confluent)

**Disadvantages:**
- ❌ Requires schema registry for large-scale deployments
- ❌ Slower than Protobuf

### MessagePack

**Best for:** Lightweight, schema-optional telemetry

```json
// Encodes as compact binary
{
  "ts": 1234567890,
  "channels": [0.5, 0.6, 0.7],
  "counter": 42
}
```

**Advantages:**
- ✅ No schema needed (schemaless)
- ✅ Compact binary
- ✅ Fast implementation
- ✅ Good for embedded systems

**Disadvantages:**
- ❌ No type safety
- ❌ Data evolution risky

### Recommended: Hybrid Approach

For maximum flexibility in research:

```
┌────────────────────────────────────────────┐
│ Real-time Streaming (Performance-critical) │
│                                            │
│ Source → Protocol Buffers → Kafka          │
│          (microseconds)   (ms latency)     │
└────────────────────────────────────────────┘

┌──────────────────────────────────────────┐
│ Archive (Storage-optimized)              │
│                                          │
│ Kafka → Avro → HDF5/Parquet → S3         │
│        (schema evolution tracking)       │
└──────────────────────────────────────────┘

┌──────────────────────────────────────────┐
│ Analysis (Format flexibility)            │
│                                          │
│ S3 → Python Pandas → Various formats     │
│      (CSV, JSON, HDF5, NetCDF)           │
└──────────────────────────────────────────┘
```

---

## Recommended Stacks by Use Case

### Use Case 1: EEG + Synchronized Video (Clinical)

**Requirements:**
- Multiple sensors (EEG, ECG, EMG, eye tracking)
- Video synchronized to millisecond
- 8+ hour recording sessions
- Compliance: FDA Title 21 CFR Part 11

**Recommended Stack:**

```
┌─────────────────────────────────────────┐
│ Acquisition Layer                       │
├─────────────────────────────────────────┤
│ Lab Streaming Layer (LSL)               │ Primary
│ + OBS Studio (video overlay)            │
│ + Python LSL client (recording)         │
└─────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│ Event Format                            │
├─────────────────────────────────────────┤
│ XDF (LSL native)                        │ Primary format
│ + JSON metadata (study params)          │
└─────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│ Archive                                 │
├─────────────────────────────────────────┤
│ Local: XDF + H.265 video + JSON         │
│ Cloud: S3/MinIO multipart upload        │
│ Backup: IPFS or BitTorrent seed         │
└─────────────────────────────────────────┘

Tools: Python mne-eeg-data, MATLAB, LSL recording app
```

### Use Case 2: Multi-Sensor Real-Time Dashboard

**Requirements:**
- 10-100 sensors (various protocols)
- Real-time processing (<100ms latency)
- Long-term archive (months)
- Multiple simultaneous consumers (live view, recording, analysis)

**Recommended Stack:**

```
┌─────────────────────────────────────────┐
│ Data Sources (Heterogeneous)            │
├─────────────────────────────────────────┤
│ SCPI Instruments (network)              │
│ USB/Serial (gateway)                    │
│ Sensor networks (MQTT)                  │
│ Video streams (RTSP)                    │
└─────────────────────────────────────────┘
         │ (Adapter code)
         ▼
┌─────────────────────────────────────────┐
│ Event Stream                            │
├─────────────────────────────────────────┤
│ Apache Kafka                            │ Primary broker
│ Topics:                                 │
│   - sensors/temperature/*               │
│   - instruments/scpi/*                  │
│   - video/frame-metadata/*              │
└─────────────────────────────────────────┘
    │                 │                 │
    ▼                 ▼                 ▼
┌────────────┐  ┌────────────┐  ┌────────────┐
│ Recorder   │  │ Processor  │  │ Dashboard  │
│ (Avro→    │  │ (Flink/    │  │ (Web UI/   │
│  HDF5)    │  │  Python)   │  │  Grafana)  │
└────────────┘  └────────────┘  └────────────┘

Event Format: CloudEvents envelope + Avro payload
Storage: HDF5 (research) or Parquet (analytics)
```

### Use Case 3: SCPI Instrument Automation + Logging

**Requirements:**
- Instrument control via SCPI/IEEE-488.2
- Measurement logging + timestamps
- Correlation with external events
- Export for analysis

**Recommended Stack:**

```
┌──────────────────────────────────────────┐
│ SCPI Control                             │
├──────────────────────────────────────────┤
│ PyVISA (Python) or VISA-sharp (C#)      │
│ Custom gateway if no VISA support       │
└──────────────────────────────────────────┘
         │ (.NET Data Access Layer)
         ▼
┌──────────────────────────────────────────┐
│ Event Publishing                         │
├──────────────────────────────────────────┤
│ Option A: LSL sink (+ video sync)       │
│ Option B: Kafka producer (analytics)    │
│ Option C: Direct file write (simple)    │
└──────────────────────────────────────────┘
         │
         ▼
┌──────────────────────────────────────────┐
│ Archive Format                           │
├──────────────────────────────────────────┤
│ Primary: CSV + JSON metadata             │
│ Alternative: Parquet (analysis-ready)   │
│ Video: S3/MinIO with metadata timestamps │
└──────────────────────────────────────────┘

Libraries: PyVISA, python-can, mqtt-paho
```

### Use Case 4: Passive Radar SDR (Multi-Channel Sync)

**Requirements:**
- Multiple synchronized receivers
- Phase-coherent sample capture
- Large continuous recordings (TBs)
- Real-time signal processing

**Recommended Stack:**

```
┌─────────────────────────────────────────┐
│ Receiver Hardware                       │
├─────────────────────────────────────────┤
│ KrakenSDR (synchronized) or             │
│ Multiple RTL-SDR (GPS-PPS sync)         │
└─────────────────────────────────────────┘
         │ (USB 3.0)
         ▼
┌─────────────────────────────────────────┐
│ Real-Time Processing                    │
├─────────────────────────────────────────┤
│ GNU Radio + custom blocks               │
│ (decimation, channel separation)        │
└─────────────────────────────────────────┘
         │ (IQ samples + PTP timestamps)
         ▼
┌─────────────────────────────────────────┐
│ Event Stream                            │
├─────────────────────────────────────────┤
│ Custom format (binary + ASCII index)    │
│ Serialization: MessagePack or Avro      │
└─────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│ Archive                                 │
├─────────────────────────────────────────┤
│ HDF5 (hierarchical structure)           │ Chunked
│ + separate index file (timestamps)      │ Compressed
│ + carrier reference signal backup       │
└─────────────────────────────────────────┘

Timing: PTP v2 (IEEE 1588) for clock sync
```

---

## Why Standards Matter

### Real-World Scenario: The "Homebrew" Cost

**Scenario:** You build custom telemetry system without standards

Year 1 (Project 1):
- ✅ Custom binary format (works!)
- ✅ Direct file writing (simple!)
- ⏱️ ~100 hours development

Year 2 (Project 2):
- ❌ Need to parse Year 1 format (forgot documentation)
- ❌ Need multi-consumer support (redesign needed)
- ❌ Need cloud backup (no standard API)
- ⏱️ ~200 hours (lost 100 hours on format rework)

Year 3 (Project 3):
- ❌ Compatibility with student's Python workflow
- ❌ Export to MATLAB for colleague
- ❌ Streaming to real-time dashboard
- ⏱️ ~400 hours (80% rewrite)

**5-Year Cost:** 700 hours + complexity + bugs

### Using Standards: The Cost

Year 1:
- ✅ Learn Kafka / LSL / Protobuf (20 hours)
- ✅ Build adapter for Project 1 (40 hours)
- ✅ Automatic archive + analysis pipelines (20 hours)

Year 2:
- ✅ Project 2 reuses framework (10 hours)
- ✅ Multi-consumer support (built-in, 0 hours)
- ✅ Cloud backup (S3 standard, 5 hours)

Year 3:
- ✅ Export to Python/MATLAB (standard libraries, 2 hours)
- ✅ Real-time dashboard (plug-and-play Grafana, 3 hours)

**5-Year Cost:** 100 hours + minimal complexity + battle-tested code

### Key Benefits of Standards

| Aspect | Custom | Standard |
|--------|--------|----------|
| **Development time** | High | Low |
| **Team knowledge transfer** | Hard | Easy (documented) |
| **Long-term maintenance** | Costly | Low |
| **Interoperability** | None | Excellent |
| **Community support** | Limited | Excellent |
| **Academic credibility** | Weak | Strong |
| **Future-proofing** | Poor | Good |
| **Debugging** | Difficult | Easy (standard tools) |

---

## Decision Tree: Choosing Your Stack

```
START: What are you recording?
│
├─ EEG/Neuroscience signals + Video?
│  └─→ LSL (Lab Streaming Layer)
│      + XDF format
│      + OBS for video
│
├─ SCPI Instruments + Sensors?
│  ├─ Real-time dashboard required?
│  │  └─→ Kafka + Avro + Grafana
│  └─ Simple logging okay?
│     └─→ LSL sink or CSV + JSON
│
├─ Multi-camera video + metadata overlay?
│  └─→ OBS Studio + WebSocket metadata
│      + H.265 video codec
│      + SRT for streaming
│
├─ Distributed multi-site recording?
│  ├─ Cloud-native / Kubernetes?
│  │  └─→ Kafka + OpenTelemetry
│  └─ On-premises?
│     └─→ RabbitMQ streams + LSL
│
├─ P2P research data distribution?
│  ├─ Public archival?
│  │  └─→ BitTorrent v2 + IPFS
│  └─ Institutional only?
│     └─→ S3/MinIO + HTTP Range Requests
│
└─ Embedded / Low-power devices?
   ├─ Extreme latency critical (<1ms)?
   │  └─→ Raw MessagePack UDP
   └─ Real-time but not critical?
      └─→ MQTT + RabbitMQ
```

---

## Implementation Priority Order

**Start here (most standardized, least risk):**
1. CloudEvents envelope (for ANY telemetry)
2. HTTP Range Requests (for blob transfer)
3. S3 multipart upload pattern (cloud archival)

**Then choose domain stack:**
4. LSL (neuroscience), Kafka (distributed), or RabbitMQ (lightweight)
5. Corresponding serialization (Avro/Protobuf/MessagePack)

**Finally add specialized tools:**
6. BitTorrent/IPFS (if distribution needed)
7. Stream processing (Kafka Streams, Flink)

---

## References

### Standards Documents
- [CloudEvents Spec](https://github.com/cloudevents/spec) (CNCF Graduated)
- [RFC 7233 - HTTP Range Requests](https://datatracker.ietf.org/doc/rfc7233/)
- [RFC 9112 - HTTP Semantics](https://datatracker.ietf.org/doc/rfc9112/)
- [AMQP 1.0 - ISO/IEC 19464](https://www.oasis-open.org/committees/amqp/)
- [BitTorrent v2 - BEP 52](https://www.bittorrent.org/beps/bep_0052.html)

### Tool Documentation
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [RabbitMQ Streams](https://www.rabbitmq.com/docs/streams)
- [Protocol Buffers](https://developers.google.com/protocol-buffers)
- [Apache Avro](https://avro.apache.org/)
- [IPFS Docs](https://docs.ipfs.tech/)

### Comparative Studies
- [Serialization Benchmark](https://github.com/saint1991/serialization-benchmark) (Avro vs Protobuf vs MessagePack)
- [Kafka Event Sourcing](https://www.confluent.io/blog/event-sourcing-cqrs-stream-processing-apache-kafka-whats-connection/)
- [RabbitMQ vs MQTT](https://www.rabbitmq.com/)

### Research Papers
- [CloudEvents Adoption Analysis](https://www.cncf.io/announcements/2024/01/25/cloud-native-computing-foundation-announces-the-graduation-of-cloudevents/)
- [IPFS Paper - Content Addressed P2P System](https://ipfs.io/ipfs/QmR7GSQM93Cx5eAg6a6yRzNde1FQv7uL6X1o4k7zrJa3LX/ipfs.draft3.pdf)

---

*Last updated: 2026-01-16*

*This document complements [README.md](README.md) with deep dives into standardized event streaming and blob transfer approaches.*
