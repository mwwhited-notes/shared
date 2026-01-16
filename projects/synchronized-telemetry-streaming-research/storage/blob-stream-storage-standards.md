# Blob & Stream Storage Standards and Options

Comprehensive guide to standardized approaches for persisting large blobs, streaming data, and time-series information. Covers file formats, databases, cloud storage, and archival strategies.

## Table of Contents

1. [File Format Standards](#file-format-standards)
2. [Time-Series Databases](#time-series-databases)
3. [Object & Cloud Storage](#object--cloud-storage)
4. [Distributed Storage Systems](#distributed-storage-systems)
5. [Embedded Storage Engines](#embedded-storage-engines)
6. [Archive & Web Formats](#archive--web-formats)
7. [Storage Strategy Matrix](#storage-strategy-matrix)
8. [Lifecycle & Retention Policies](#lifecycle--retention-policies)

---

## File Format Standards

### HDF5 (Hierarchical Data Format)

**Status:** NASA Earth Science standard (approved 2007)

[HDF5 Specification](https://www.hdfgroup.org/) | [NASA Earthdata](https://www.earthdata.nasa.gov/about/esdis/esco/standards-practices/hdf5)

**What it is:**
Binary format for storing and managing complex, large-scale scientific data. Hierarchical structure (like filesystem) with groups and datasets.

**Key Features:**
- Hierarchical organization (groups → datasets)
- Chunked storage (optimized I/O)
- Compression (gzip, LZO, SZIP)
- Parallel I/O support
- Metadata capabilities
- Self-describing (structure embedded in file)

**Strengths:**
✅ Scientific data standard (climate, satellite, geoscience)
✅ Excellent for multidimensional arrays
✅ Built-in compression
✅ Language support (C, Python, MATLAB, Java)

**Limitations:**
❌ Complex format (steep learning curve)
❌ Slower write than flat formats
❌ Not optimal for streaming (designed for batch access)
❌ Huge file sizes possible (poor for cloud transfer)

**Use Case:** Research data archival, scientific simulations, satellite imagery

**Libraries:**
- h5py (Python)
- PyTables (Python, higher-level)
- MATLAB: built-in
- C/C++ reference library
- Java: jhdf5

---

### NetCDF (Network Common Data Form)

**Status:** Standard (NetCDF-4 = HDF5 + restrictions)

[NetCDF Specification](https://www.unidata.ucar.edu/software/netcdf/) | [NASA Standard](https://www.earthdata.nasa.gov/about/esdis/esco/standards-practices/netcdf-4hdf5)

**What it is:**
Standardized data format for netCDF-4 (HDF5 under the hood) with additional scientific conventions (CF - Climate & Forecast).

**Key Differences from HDF5:**
- CF Conventions (standardized variable names, units, coordinates)
- Simpler, more constrained
- Better for climate/weather data
- Improved tooling

**Example Use:**
Climate model output, weather forecast data, oceanographic measurements

**Cross-references:**
- [Analog Computing Research](../../AnalogComputers/) - Contains climate simulation papers

---

### Apache Parquet

**Status:** Apache Top-Level Project | [Official Spec](https://github.com/apache/parquet-format)

**What it is:**
Columnar storage format optimized for analytics and machine learning. Data stored column-by-column (not row-by-row).

**Key Features:**
- Columnar organization (efficient for analytics)
- Compression per-column (snappy, gzip, brotli, zstd, LZ4)
- Nested data support (Dremel encoding)
- Metadata statistics
- Predicate pushdown (skip reading irrelevant columns)
- Row group concept (parallel I/O)

**Strengths:**
✅ Excellent compression (50-80% vs raw)
✅ Fast queries (only read needed columns)
✅ Standard for Spark, Pandas, Arrow ecosystem
✅ Good for analytics workloads

**Limitations:**
❌ Write-once format (no updates)
❌ Not suitable for streaming writes
❌ Row-order matters for compression
❌ Complex format

**Use Case:**
Historical data archive (data lake), analytical queries, machine learning training

**Integration:**
- Spark: Native
- Pandas: Parquet backend
- Arrow: Native
- DuckDB: Native

---

### XDF (eXtensible Data Format)

**Status:** Lab Streaming Layer standard | [GitHub](https://github.com/sccn/xdf)

**What it is:**
Format designed specifically for multimodal, asynchronous stream recording. Combines binary data chunks with XML metadata.

**Structure:**
```
┌─────────────────────┐
│ XDF File Header     │
├─────────────────────┤
│ Stream 1 (EEG)      │
│  - XML Info         │
│  - Data Chunks      │
├─────────────────────┤
│ Stream 2 (Video)    │
│  - XML Info         │
│  - Data Chunks      │
├─────────────────────┤
│ Global Metadata     │
└─────────────────────┘
```

**Key Features:**
- Multi-stream support (different sampling rates)
- Timestamp per sample (perfect for sync)
- Streaming writes (append data)
- XML metadata (human-readable)
- Extensible (custom stream types)

**Strengths:**
✅ Purpose-built for synchronized recording
✅ Streaming write capability
✅ Perfect timestamp resolution
✅ Multimodal support (audio, video, sensors, markers)

**Limitations:**
❌ Proprietary format (though well-documented)
❌ Larger than binary alternatives
❌ Less optimized compression than Parquet

**Use Case:** EEG + video recording, multimodal research, neuroscience

**Cross-references:**
- [Lab Streaming Layer (LSL)](https://github.com/sccn/labstreaminglayer)
- [event-streaming-and-blob-transfer.md](event-streaming-and-blob-transfer.md) - Detailed LSL coverage

---

### Apache Arrow

**Status:** Apache Top-Level Project | [Specification](https://arrow.apache.org/docs/format/Columnar.html)

**What it is:**
Language-agnostic columnar in-memory format + streaming protocol. Standard for data interchange between systems.

**Key Features:**
- In-memory columnar format
- Streaming IPC protocol (binary messages)
- Zero-copy operations (shared memory)
- Rich type system (nested, user-defined)
- 64-byte memory alignment (optimized)

**Strengths:**
✅ Language-agnostic (Python, C++, Java, Go, Rust, etc.)
✅ Zero-copy reads (performance)
✅ Both in-memory and persistent (via Parquet)
✅ Streaming protocol built-in

**Limitations:**
❌ Not a file format itself (use Parquet for storage)
❌ Less suitable for very large single objects
❌ Complex type system steeper learning curve

**Use Case:** Data interchange between services, real-time stream processing, cross-language pipelines

---

## Time-Series Databases

### InfluxDB

**Status:** Industry standard (owned by InfluxData) | [Official](https://www.influxdata.com/)

**Architecture:**
- Custom tagset data model (not relational)
- Written in Go (InfluxDB 3.0+ in Rust)
- Query: InfluxQL or SQL

**Data Model:**
```
Measurement (table-like)
├─ Tags (indexed, low cardinality: e.g., "host", "region")
├─ Fields (actual data: temperature, pressure, etc.)
└─ Timestamp (UTC nanosecond precision)
```

**Characteristics:**
- **Best at:** Low-cardinality streams (few unique devices)
- **Performance:** Exceptional write throughput (millions/sec)
- **Retention:** Configurable (hours to years)
- **Query:** InfluxQL or SQL (v3.0+)

**Strengths:**
✅ Specialized for time-series (optimized for sequential writes)
✅ Extremely fast ingestion
✅ Low-cardinality ideal (IoT sensors, monitoring)
✅ Built-in retention policies
✅ Cloud and self-hosted options

**Limitations:**
❌ Poor at high-cardinality (many unique devices)
❌ Custom query language (not standard SQL, v3.0+ fixes)
❌ Smaller ecosystem than PostgreSQL

**Use Case:** IoT sensor networks, real-time monitoring, metrics (Prometheus-style)

**Comparison:**
InfluxDB vs. TimescaleDB: InfluxDB ~3.5x faster at low-cardinality, TimescaleDB ~3.5x faster at high-cardinality

---

### TimescaleDB

**Status:** Open Source (Timescale Inc.) | [GitHub](https://github.com/timescale/timescaledb)

**Architecture:**
- PostgreSQL extension (native SQL)
- Hypertables concept (auto-partitioning)
- Standard relational model

**Data Model:**
```
SQL Table with:
├─ Time column (indexed)
├─ Device/source columns (indexed tags)
├─ Measurement columns (values)
└─ Data automatically partitioned by time
```

**Characteristics:**
- **Best at:** High-cardinality streams (many unique devices)
- **Performance:** Excellent throughput (millions/sec)
- **Retention:** SQL-based policies
- **Query:** Standard SQL

**Strengths:**
✅ Standard SQL (PostgreSQL-compatible)
✅ Excellent at high-cardinality (many devices)
✅ Full relational features
✅ PostGIS support (geographic data)
✅ Proven PostgreSQL ecosystem

**Limitations:**
❌ Slower than InfluxDB at low-cardinality
❌ Requires schema definition upfront
❌ PostgreSQL maintenance overhead

**Use Case:** Sensor networks with many devices, applications with complex queries, geospatial telemetry

**Benchmark:** TimescaleDB outperforms InfluxDB at high device count (~3.5x faster at 10,000+ devices)

---

### ClickHouse

**Status:** Open Source (Yandex) | [GitHub](https://github.com/ClickHouse/ClickHouse)

**Architecture:**
- Column-oriented OLAP database
- Designed for analytical queries
- Blazingly fast (millions → billions of rows)

**Characteristics:**
- Exceptional query speed (analytical workloads)
- Compression: 10-40x reduction
- Distributed (multi-node)
- SQL query language

**Use Case:**
High-volume analytics (billions of events), data warehouse, log analysis

**Limitations:**
❌ Not optimized for real-time single-row lookups
❌ Complex distributed setup
❌ Overkill for simple monitoring

---

## Object & Cloud Storage

### Amazon S3 (Simple Storage Service)

**Status:** Industry standard | [AWS Docs](https://docs.aws.amazon.com/AmazonS3/)

**Model:**
- Object storage (key-value)
- Buckets → Objects (files)
- HTTP/HTTPS API (REST)
- No filesystem semantics

**Key Features:**
- Unlimited scalability
- 99.999999999% (11 9's) durability
- Multiple storage classes (Standard, IA, Glacier, Deep Archive)
- Multipart upload (for large files)
- S3 Select (query data in-place)
- Versioning, lifecycle policies

**Strengths:**
✅ De facto standard (99% of cloud users)
✅ Global availability
✅ Excellent price/performance ratio
✅ Rich tooling ecosystem
✅ Multipart for resumable large file uploads

**Limitations:**
❌ Not POSIX-compatible (no file permissions, no directories)
❌ Eventual consistency (old objects briefly inaccessible)
❌ Not suitable for frequent updates
❌ Latency ~10-100ms (not real-time)

**Storage Classes:**

| Class | Cost | Latency | Min Duration | Use Case |
|-------|------|---------|--------------|----------|
| Standard | High | Immediate | None | Hot data |
| IA | Medium | Immediate | 30 days | Infrequent access |
| Glacier Instant | Low | Milliseconds | 90 days | Quarterly access |
| Glacier Flexible | Very Low | 3-5 hours | 90 days | Rare access |
| Glacier Deep | Minimal | 12 hours | 180 days | Long-term archive |

**Use Case:** Research data archival, video/blob storage, data lakes

**Cross-reference:**
- [event-streaming-and-blob-transfer.md](event-streaming-and-blob-transfer.md) - S3 multipart upload details

---

### MinIO (S3-Compatible)

**Status:** Open Source | [GitHub](https://github.com/minio/minio)

**What it is:**
Self-hosted S3-compatible object storage. Bit-for-bit compatible API, can replace S3.

**Strengths:**
✅ 100% S3 API compatible (drop-in replacement)
✅ Self-hosted (data sovereignty)
✅ No egress charges
✅ Works on-premises
✅ Distributed (multi-node replication)

**Limitations:**
❌ Requires operational overhead
❌ Smaller ecosystem than AWS S3
❌ Less mature monitoring/tools

**Use Case:**
Private blob storage, research data, local backup, avoiding AWS egress charges

**Cross-references:**
- [DevOps Playground Cluster](../../projects/devops-playground-cluster/) - Container infrastructure
- [Passive Radar SDR](../../projects/passive-radar-sdr/) - Potential archive target

---

### Google Cloud Storage

**Status:** Cloud standard | [GCS Docs](https://cloud.google.com/storage/docs)

**Model:**
Similar to S3 (object storage, HTTP/REST API)

**Differentiators:**
- Strong-consistency (vs S3 eventual)
- Excellent bandwidth pricing
- Integration with BigQuery (analytics)
- Lifecycle rules

**Use Case:**
Multi-cloud deployments, analytics integration

---

## Distributed Storage Systems

### Ceph (RADOS)

**Status:** Open Source | [GitHub](https://github.com/ceph/ceph)

**Architecture:**
- RADOS (Reliable Autonomic Distributed Object Store) - core layer
- Three interfaces built on RADOS:
  - **RGW:** RADOS Gateway (S3-compatible)
  - **RBD:** RADOS Block Device (virtual disks)
  - **CephFS:** POSIX-compliant filesystem

**Key Features:**
- Self-healing (detects and repairs data)
- Replication or erasure coding
- Automatic rebalancing
- No single point of failure
- CRUSH algorithm (placement logic)

**Strengths:**
✅ Enterprise-grade durability
✅ Self-managing (autonomic)
✅ Multiple interfaces (object, block, file)
✅ Proven in large deployments
✅ Open source

**Limitations:**
❌ Complex to deploy/manage
❌ Higher operational overhead than S3
❌ Smaller ecosystem
❌ Requires multiple nodes (expensive)

**Use Case:**
Large-scale research data centers, enterprise private cloud, data sovereignty requirements

**Related:** [DevOps Playground Cluster](../../projects/devops-playground-cluster/) could explore Ceph

---

## Embedded Storage Engines

### RocksDB

**Status:** Open Source (Facebook) | [GitHub](https://github.com/facebook/rocksdb)

**What it is:**
Embeddable persistent key-value store. LSM (Log-Structured Merge) tree engine.

**Data Model:**
```
Key → Value (arbitrary binary)
Range queries supported
```

**Key Features:**
- Embedded (library, not server)
- High write throughput
- Compression (Snappy, LZ4, Zstd)
- Compaction strategies (configurable)
- Write-ahead logging (durability)

**Strengths:**
✅ Extremely fast (millions of ops/sec)
✅ Configurable compression/speed tradeoff
✅ Perfect for state stores (Kafka Streams, Flink)
✅ Used at Facebook, LinkedIn, Yahoo scale

**Limitations:**
❌ Single-machine only (not distributed)
❌ No query language (key-value only)
❌ Compaction can cause latency spikes

**Use Case:**
Stream processor state store, embedded caching, application-level durability

**Integration:**
- Kafka Streams: State store backend
- Apache Flink: State store backend
- Applications: Direct embedding in C++/Java/Go

**Comparison:**
RocksDB vs. LevelDB: RocksDB is faster (Facebook optimization for multi-core), LevelDB is simpler

---

### LevelDB

**Status:** Google's original | [GitHub](https://github.com/google/leveldb)

**Relationship to RocksDB:**
- RocksDB is a fork/enhancement of LevelDB
- LevelDB is simpler, lighter weight
- RocksDB is faster but more complex

**Use:**
When simplicity is preferred over performance

---

## Archive & Web Formats

### WARC (Web ARChive)

**Status:** ISO 28500:2017 standard | [Official](https://www.loc.gov/preservation/digital/formats/fdd/fdd000236.shtml)

**What it is:**
Archive format for combining multiple web resources (HTTP responses, metadata) into one file.

**Structure:**
```
WARC Header + HTTP Headers + Content Body
WARC Header + HTTP Headers + Content Body
... (repeat)
```

**Key Features:**
- Preserves HTTP metadata (headers, response codes)
- Supports compression (gzip, bzip2)
- Record integrity (checksums)
- Handles overly long records (truncation/segmentation)

**Strengths:**
✅ Web archiving standard (Internet Archive, national libraries)
✅ Preserves all HTTP context
✅ ISO standard (formal recognition)
✅ Good for reproducibility research

**Limitations:**
❌ Verbose (includes all HTTP headers)
❌ Not optimized for search
❌ Large files (no column compression)

**Use Case:**
Web crawling archives, reproducible research, URL-based data collection

**Example:** Internet Archive (archive.org) uses WARC

---

### TAR (Tape Archive)

**Status:** POSIX standard (POSIX.1-1988) | [GNU Tar Docs](https://www.gnu.org/software/tar/)

**Format Variants:**
- **v7 tar:** Original (old, limited)
- **USTAR:** POSIX.1-1988 (modern standard)
- **GNU tar:** Extensions (larger files, etc.)
- **PAX:** POSIX.1-2001 (most portable)

**Structure:**
```
512-byte header block
Data blocks
512-byte header block
Data blocks
...
End marker (2 zero blocks)
```

**Key Features:**
- Sequential (not random-access)
- Streaming writes/reads (perfect for pipes)
- 512-byte aligned (tape-friendly)
- Supports compression (gzip, bzip2, xz wrapper)

**Strengths:**
✅ Universal (every UNIX system has tar)
✅ Streaming-friendly (sequential I/O)
✅ Simple format
✅ Good for backups

**Limitations:**
❌ Sequential-only (can't extract middle file without reading whole file)
❌ No compression built-in (gzip as wrapper)
❌ No indexing (must read sequentially)
❌ No incremental backup support (standard TAR)

**Use Case:**
Software distribution, backup archives, sequential data streams

**Variants for Streaming:**
- **tar.gz:** TAR + gzip compression
- **tar.xz:** TAR + xz compression
- **tar.bz2:** TAR + bzip2 compression

---

## Storage Strategy Matrix

### By Use Case

```
┌─────────────────────────────────────────────────────────┐
│ EEG + Video + Sensors (Multimodal)                      │
│                                                         │
│ → XDF (LSL native)                                      │
│   + H.265 video (separate file)                         │
│   + HDF5 archive (long-term)                            │
│   + S3/MinIO backup                                     │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ SCPI Instruments + IoT Sensors (Time-Series)            │
│                                                         │
│ → InfluxDB or TimescaleDB (live)                        │
│   + Parquet export (daily)                              │
│   + S3/Glacier archive (monthly)                        │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ Large Video Archive (4K, Multi-Day)                     │
│                                                         │
│ → H.265 video + IndexMetadata (JSON)                    │
│   + S3 multipart upload                                 │
│   + Glacier Deep Archive (long-term)                    │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ Real-Time Stream Processing (Kafka)                     │
│                                                         │
│ → RocksDB (state store)                                 │
│   + Parquet (batch output)                              │
│   + S3/MinIO (archival)                                 │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ Scientific Simulation Output                            │
│                                                         │
│ → HDF5 (primary)                                        │
│   → NetCDF (sharing)                                    │
│   → S3 (backup)                                         │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ Research Data Distribution                              │
│                                                         │
│ → TAR.gz (compressed archive)                           │
│   + BitTorrent (P2P distribution)                       │
│   + IPFS (decentralized backup)                         │
│   + WARC (with HTTP metadata)                           │
└─────────────────────────────────────────────────────────┘
```

---

## Lifecycle & Retention Policies

### AWS Glacier Tiers

**Standard Pattern:**
```
Day 0-30:   S3 Standard (hot, instant access)
Day 31-90:  S3 IA (infrequent access)
Day 91+:    Glacier Instant (occasional access)
Year 1+:    Glacier Flexible (rare access)
Year 7+:    Glacier Deep Archive (compliance hold)
```

**Minimum Retention:**
- Glacier Instant: 90 days
- Glacier Flexible: 90 days
- Glacier Deep Archive: 180 days

**Retrieval Times:**
- Standard: Immediate
- Glacier Instant: Milliseconds
- Glacier Flexible: 3-5 hours (or expedited 1-5 min for cost)
- Glacier Deep: 12 hours (standard)

**Cost Progression:**
```
Standard  ($/GB/month): ~$0.023
IA        ($/GB/month): ~$0.0125
Glacier I ($/GB/month): ~$0.004
Glacier F ($/GB/month): ~$0.0036
Glacier D ($/GB/month): ~$0.00099
```

→ **90x cost reduction** from Standard to Deep Archive

**Use Case:** Long-term research data with infrequent access

---

### Self-Hosted Lifecycle Example

**MinIO + TAR.gz:**

```
Week 0:     Streaming write to MinIO (hot data)
Week 4:     Move to cold tier (different disk)
Month 3:    Archive to tape (nearline)
Year 1:     Delete or keep (compliance policy)
```

**Commands:**
```bash
# Create lifecycle policy
mc ilm import minio/bucket < lifecycle.json

# Archive old data
find . -mtime +30 -exec tar czf archive-$(date +%s).tar.gz {} \;
```

---

## Comparison Summary

| Format | Type | Latency | Streaming | Compression | Best For |
|--------|------|---------|-----------|-------------|----------|
| **HDF5** | File | Slow | ❌ | Good | Scientific arrays |
| **NetCDF** | File | Slow | ❌ | Good | Climate data |
| **XDF** | File | Medium | ✅ | Fair | Multimodal sync |
| **Parquet** | File | Fast (analytical) | ❌ | Excellent | Analytics |
| **Arrow** | In-memory | Very fast | ✅ (IPC) | - | Interchange |
| **InfluxDB** | Database | Fast (writes) | ✅ | - | Low-cardinality TS |
| **TimescaleDB** | Database | Fast (writes) | ✅ | - | High-cardinality TS |
| **S3** | Object | Medium | ✅ | Optional | General blobs |
| **MinIO** | Object | Medium | ✅ | Optional | Self-hosted S3 |
| **Ceph** | Distributed | Medium | ✅ | Optional | Enterprise storage |
| **RocksDB** | KV Store | Very fast | ❌ | Good | State stores |
| **TAR** | Archive | Sequential | ✅ | Optional | Backups |
| **WARC** | Archive | Sequential | ✅ | Optional | Web archives |

---

## Recommended Stacks by Scenario

### EEG + Video (Clinical Recording)

**Primary:**
```
XDF (multimodal sync) + H.265 video
└─ Real-time: LSL network
```

**Archive:**
```
HDF5 (long-term research)
└─ Backup: S3 Glacier Flexible or MinIO + tape
```

---

### SCPI Instruments (Continuous Monitoring)

**Real-time:**
```
InfluxDB or TimescaleDB (live dashboard)
└─ State: RocksDB (aggregation)
```

**Archive:**
```
Parquet (daily exports)
└─ Cold: S3 Glacier or Ceph
```

---

### Passive Radar (Multi-Receiver)

**Streaming:**
```
HDF5 (per receiver, parallel writes)
└─ Sync: Central aggregator
```

**Archive:**
```
TAR.gz per day
└─ Long-term: S3 Deep Archive or tape
```

---

### High-Volume IoT (1000s of devices)

**Real-time:**
```
TimescaleDB (high-cardinality)
└─ Buffering: RocksDB compaction
```

**Analytics:**
```
Parquet export (hourly/daily)
└─ Data warehouse: ClickHouse or S3 + Athena
```

---

## Research Data Distribution

**Local Lab:**
```
MinIO (S3-compatible)
```

**Sharing with Colleagues:**
```
TAR.gz + BitTorrent
```

**Public Archival:**
```
IPFS + WARC (with HTTP metadata)
```

**Formal Repository (Zenodo/OSF):**
```
Parquet + Metadata (JSON)
```

---

## Standards References

### Storage Format RFCs
- [ISO 28500:2017 - WARC](https://www.iso.org/standard/68004.html)
- [POSIX.1-1988 - TAR (ustar)](https://pubs.opengroup.org/onlinepubs/9699919799/)

### File Formats (Standards, not RFCs)
- [HDF5 Specification](https://www.hdfgroup.org/HDF5/doc/SpecH5-Datasets.html)
- [NetCDF Documentation](https://www.unidata.ucar.edu/software/netcdf/)
- [Apache Parquet Format](https://github.com/apache/parquet-format)
- [Apache Arrow Format](https://arrow.apache.org/docs/format/Columnar.html)
- [XDF Format](https://github.com/sccn/xdf)

### Database Standards
- [TimescaleDB (PostgreSQL extension)](https://docs.timescale.com/)
- [InfluxDB (proprietary spec)](https://docs.influxdata.com/)
- [RocksDB Documentation](https://rocksdb.org/docs/)

### Cloud Storage
- [AWS S3 API Reference](https://docs.aws.amazon.com/s3/)
- [Ceph Documentation](https://docs.ceph.com/)
- [MinIO API](https://min.io/docs/minio/linux/)

---

*Last updated: 2026-01-16*

*Part of: [Synchronized Telemetry Streaming Research](README.md)*
