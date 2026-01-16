# Glossary of Terms

Comprehensive glossary of technical terms used in the Synchronized Telemetry Streaming Research project.

## Table of Contents

- [Streaming & Protocol Terms](#streaming--protocol-terms)
- [Synchronization Terms](#synchronization-terms)
- [Blob Transfer & Storage Terms](#blob-transfer--storage-terms)
- [Storage Format Terms](#storage-format-terms)
- [Time-Series Database Terms](#time-series-database-terms)
- [Event Streaming Terms](#event-streaming-terms)
- [Architecture & Deployment Terms](#architecture--deployment-terms)
- [Networking Terms](#networking-terms)
- [Standards & Organizations](#standards--organizations)
- [Data Synchronization Terms](#data-synchronization-terms)
- [Telemetry-Specific Terms](#telemetry-specific-terms)
- [Miscellaneous Terms](#miscellaneous-terms)

## Streaming & Protocol Terms

### RTSP (Real-Time Streaming Protocol)
RFC 7826. Client-server protocol for establishing and controlling media streams. Handles session setup, teardown, and stream control without actually transporting media data.

### RTP (Real-Time Transport Protocol)
RFC 3550. Application-level transport protocol that provides end-to-end network transport functions suitable for applications transmitting real-time data. Carries payload data with timing and sequencing information.

**Wikipedia:** [Real-time Transport Protocol](https://en.wikipedia.org/wiki/Real-time_Transport_Protocol)

### RTCP (RTP Control Protocol)
RFC 3550. Companion protocol to RTP providing out-of-band statistics and control information. Used for feedback, synchronization, and stream correlation. See also RFC 8861 for multi-stream extensions.

### RTP Timestamp
A 32-bit timestamp field in RTP headers that increments at the media clock rate. Used for media synchronization and jitter buffer calculations. Different from wall-clock time.

### SRTP (Secure Real-Time Protocol)
RFC 3711. Encryption and authentication framework for RTP and RTCP, providing confidentiality, message authentication, and replay protection.

### QUIC (Quick UDP Internet Connections)
RFC 9000. Modern transport protocol built on UDP with integrated TLS encryption, connection migration, and per-stream out-of-order delivery support. Suitable for unreliable or mobile networks.

### SCTP (Stream Control Transmission Protocol)
RFC 9260. Transport protocol providing reliable message delivery with support for unordered delivery options and multi-stream multiplexing.

### UDP (User Datagram Protocol)
Connectionless transport protocol with minimal overhead but no delivery guarantees. Preferred for real-time applications where latency is more important than perfect reliability.

**Wikipedia:** [User Datagram Protocol](https://en.wikipedia.org/wiki/User_Datagram_Protocol)

### TCP (Transmission Control Protocol)
Connection-oriented transport protocol ensuring in-order, reliable delivery. Higher latency overhead than UDP but guarantees message delivery.

**Wikipedia:** [Transmission Control Protocol](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)

### Multicast
Network delivery method where a single message is sent from one source to multiple recipients simultaneously using a reserved address range (224.0.0.0/4 for IPv4).

**Wikipedia:** [Multicast](https://en.wikipedia.org/wiki/Multicast)

### Unicast
Standard point-to-point network delivery from one sender to one receiver.

## Synchronization Terms

### NTP (Network Time Protocol)
RFC 5905. Internet protocol for synchronizing clocks across networks. Typical accuracy: milliseconds. Good for distributed systems where modest sync tolerance acceptable.

**Wikipedia:** [Network Time Protocol](https://en.wikipedia.org/wiki/Network_Time_Protocol)

### PTP (Precision Time Protocol)
IEEE 1588. Network-based time synchronization protocol with nanosecond-level accuracy. Preferred for applications requiring tight temporal correlation between sensors.

**Wikipedia:** [Precision Time Protocol](https://en.wikipedia.org/wiki/Precision_Time_Protocol)

### Clock Recovery
Process of extracting timing information from received media (e.g., RTP timestamps) and adjusting local playback clock to match sender's clock. Essential for multi-stream synchronization.

### Jitter Buffer
Adaptive buffer that stores arriving packets and compensates for network jitter and clock drift. Introduces latency tradeoff for improved playback continuity.

### Synchronization Point
Explicit timestamp or marker where multiple streams are guaranteed to be temporally aligned. Used to resynchronize streams after clock divergence.

### Wall Clock Time
Absolute time (epoch-based), typically from system clock or NTP. Different from RTP timestamp which is relative to media clock.

### Media Clock
Virtual clock running at the rate of the media being transported. RTP timestamps are relative to media clock, not wall clock.

### Rapid Synchronization
RFC 6051. Techniques for achieving rapid clock convergence between RTP streams, using explicit synchronization primitives and reduced jitter buffer latency.

## Blob Transfer & Storage Terms

### Blob
Large binary object (video file, sensor recording, etc.). Typical size: megabytes to terabytes.

### Fountain Codes
Erasure code technique where any subset of encoded symbols can be used to recover the original data. Perfect for out-of-order packet delivery. See RaptorQ.

**Wikipedia:** [Fountain Code](https://en.wikipedia.org/wiki/Fountain_code)

### RaptorQ
RFC 6330. Systematic fountain code standard enabling recovery of data from any K+δ encoded symbols regardless of order. Overhead <0.2% (vs 50% for naive approaches).

**Wikipedia:** [Raptor Code](https://en.wikipedia.org/wiki/Raptor_code)

### FEC (Forward Error Correction)
Technique of adding redundancy to data allowing recovery from lost packets without retransmission. Examples: Reed-Solomon codes, fountain codes, Hamming codes.

**Wikipedia:** [Forward Error Correction](https://en.wikipedia.org/wiki/Forward_error_correction)

### FECFRAME
RFC 6363, RFC 8680. Framework for applying FEC to any packet flow while maintaining compatibility with existing protocols.

### Erasure Coding
FEC variant encoding data as M symbols, any K of which can recover original. Used in distributed storage (Ceph, RAID) and reliable transfer.

**Wikipedia:** [Erasure Code](https://en.wikipedia.org/wiki/Erasure_code)

### Symbol
Single unit in encoded data (typically one packet's worth). In RaptorQ, K+δ symbols needed to recover K-symbol original.

### Checksum / Parity
Calculated redundancy allowing detection of transmission errors. CRC common for reliability checks; not sufficient alone for recovery.

### Out-of-Order Delivery
Arrival of packets in sequence different from transmission. Typical in UDP-based protocols and over multicast. RTP and QUIC handle reordering; TCP guarantees ordering.

### Datagrams
Individual packets in connection-less protocols (UDP). Each datagram is independent and can take different network paths.

## Storage Format Terms

### HDF5 (Hierarchical Data Format 5)
Scalable format for storing massive scientific datasets with hierarchical organization. Excellent for time-series and multi-channel sensor data. NASA standard.

### NetCDF (Network Common Data Form)
Self-describing data format optimized for scientific data with metadata, dimensions, and variables. Widely used in climate and earth science.

### Parquet
Columnar storage format with excellent compression and query performance. Preferred for analytics workloads. Apache project.

### XDF (Extensible Data Format)
Open format developed for Lab Streaming Layer. Optimizes for multi-modal physiological data with timestamps. Becoming standard in neuroscience.

### Arrow (Apache Arrow)
Columnar in-memory format with standardized IPC (Inter-Process Communication) protocol. Enables zero-copy data sharing between processes/languages.

### WARC (Web ARChive)
ISO 28500 standard format for archiving web resources including metadata and capture context. Good for audit trails and historical records.

### TAR / USTAR
POSIX.1-1988 archival format creating single files from multiple source files. Not compressed by default; usually combined with gzip/bzip2.

**Wikipedia:** [Tar (computing)](https://en.wikipedia.org/wiki/Tar_(computing))

### Protobuf
Binary serialization format from Google with excellent compression and speed. Language-neutral with schema versioning support.

**Wikipedia:** [Protocol Buffers](https://en.wikipedia.org/wiki/Protocol_Buffers)

### Avro
Data serialization system optimized for Kafka and Hadoop. Self-describing with schema evolution capabilities.

### MessagePack
Efficient binary format like JSON but faster and more compact. Good for inter-process communication.

**Wikipedia:** [MessagePack](https://en.wikipedia.org/wiki/MessagePack)

### Columnar Format
Storage organizing data by column rather than row. Excellent for analytics and compression where many rows share patterns.

**Wikipedia:** [Column-oriented DBMS](https://en.wikipedia.org/wiki/Column-oriented_DBMS)

### Row-Oriented Format
Storage organizing data by row (traditional). Better for random access patterns and transactional workloads.

**Wikipedia:** [Row-oriented Database](https://en.wikipedia.org/wiki/Row-oriented_database)

## Time-Series Database Terms

### Time-Series Data
Sequence of values indexed by time with consistent intervals (or marked irregularly). Characterized by: write-heavy, append-only, immutable past, delete-from-tail patterns.

### Cardinality
Number of unique label combinations in a time-series database. High-cardinality = many unique combinations; causes memory pressure in some TSDB designs.

### Retention Policy
Time-based or size-based rule for data expiration. Common in metrics: 15 days realtime, 1 year archived.

### Downsampling / Aggregation
Process of combining multiple high-frequency data points into lower-frequency summary (e.g., second to minute averages). Reduces storage while preserving trends.

### Rollup
Automated process to aggregate old data into lower resolution. E.g., minute data aggregated to hourly after 7 days.

### Query Language (InfluxQL, SQL, Flux)
Domain-specific language for time-series queries. InfluxQL (time-specific), SQL (standard), Flux (functional programming).

## Event Streaming Terms

### Event
Immutable record of something that happened, containing data and timestamp. Core unit of event-driven systems.

### Event Stream
Ordered sequence of events from a source. Can be: total ordering (single source) or partial ordering (multiple sources).

### Event Sourcing
Pattern storing all state changes as immutable events rather than current state. Enables perfect audit trail and temporal queries.

**Wikipedia:** [Event Sourcing](https://en.wikipedia.org/wiki/Event_sourcing)

### Topic / Channel
Named stream or message queue. Publishers write to topic; subscribers read from topic. Kafka-style abstraction.

### Partition / Shard
Subset of a topic's messages, typically split by key. Enables parallelism: different partitions processed by different consumers.

### Consumer Group
Set of consumers sharing responsibility for consuming a topic. Messages distributed so each goes to exactly one consumer in group.

### Offset / Cursor
Position within a stream. Consumers track offset to know which messages already processed. Enables restart and replay.

### Lag
Difference between latest message in stream and consumer's current position. High lag = consumer falling behind.

### Throughput
Messages per second a system can sustain. Important for high-volume telemetry.

### Latency (End-to-End)
Time from message creation to delivery to consumer. Critical for real-time applications. Often measured as p99 or p999.

### Message Ordering Guarantee
- **Total Order:** All messages globally ordered (usually per topic or partition)
- **Causal Order:** If A causally precedes B, they're ordered
- **FIFO per Source:** Messages from same source in order (different sources may interleave)

### Exactly-Once Semantics
Guarantee each message processed exactly once despite failures. Difficult to achieve; many systems provide "effectively-once" instead.

### Dead Letter Queue (DLQ)
Destination for messages that fail processing after retries. Prevents infinite loops and enables manual intervention.

## Architecture & Deployment Terms

### In-Process
Code libraries running in same process/address space. Ultra-low latency (<1μs), shared memory, no network overhead. Examples: LMAX Disruptor, Chronicle Queue.

### Out-of-Process
Separate service/daemon communicating via IPC or network. Isolation, independent scaling, network overhead. Examples: NATS server, Kafka broker.

### Embedded
Library variant designed for in-process use. Examples: NATS embedded client, SQLite.

### Distributed
System spanning multiple machines/processes with network communication. Adds complexity but enables fault tolerance and scaling.

### Pub/Sub (Publish/Subscribe)
Messaging pattern where publishers emit messages to topics and subscribers receive without knowing publishers. Decouples producers from consumers.

**Wikipedia:** [Publish–Subscribe Pattern](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)

### Request/Reply
Messaging pattern where sender waits for response before continuing. More tightly coupled than pub/sub but simpler.

### Queue (FIFO Queue)
Ordered data structure: First-In-First-Out. Messages processed in arrival order. Examples: RabbitMQ queues, Redis lists.

**Wikipedia:** [Queue (Abstract Data Type)](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))

### Ring Buffer
Circular data structure fixed-size buffer with head/tail pointers. Enables lock-free implementations. Examples: LMAX Disruptor.

**Wikipedia:** [Circular Buffer](https://en.wikipedia.org/wiki/Circular_buffer)

### Lock-Free
Concurrency technique using atomic operations instead of locks. Lower latency, better cache behavior, but more complex.

**Wikipedia:** [Lock-free Programming](https://en.wikipedia.org/wiki/Lock-free_programming)

### High Availability (HA)
System remaining operational despite failures. Typically 3+ node cluster with replication and failover.

### Replication
Maintaining copies of data across multiple nodes. Enables fault tolerance and read scalability at cost of write complexity.

**Wikipedia:** [Replication (Computing)](https://en.wikipedia.org/wiki/Replication_(computing))

### Quorum
Majority consensus approach: writes succeed when majority acknowledge. Balances consistency and availability.

**Wikipedia:** [Quorum (Distributed Systems)](https://en.wikipedia.org/wiki/Quorum_(distributed_systems))

## Networking Terms

### QoS (Quality of Service)
Network characteristics: latency, jitter, packet loss, bandwidth. Different applications have different QoS requirements.

**Wikipedia:** [Quality of Service](https://en.wikipedia.org/wiki/Quality_of_service)

### Packet Loss
Percentage of packets not reaching destination. Typical: 0.1-5% over WAN, <0.01% LAN. Critical factor in choosing protocols.

**Wikipedia:** [Packet Loss](https://en.wikipedia.org/wiki/Packet_loss)

### Jitter
Variation in packet arrival times. High jitter requires larger buffers. Caused by variable network queuing.

**Wikipedia:** [Jitter](https://en.wikipedia.org/wiki/Jitter)

### Congestion Control
Mechanism for senders to detect network congestion and reduce transmission rate. Examples: QUIC congestion control, TCP Reno.

**Wikipedia:** [Congestion Control](https://en.wikipedia.org/wiki/Congestion_control)

### Adaptive Bitrate
Technique of adjusting media quality/compression based on detected network conditions. Common in video streaming (HLS, DASH).

**Wikipedia:** [Adaptive Bitrate Streaming](https://en.wikipedia.org/wiki/Adaptive_bitrate_streaming)

### Bandwidth
Maximum data transmission rate. Often bottleneck in remote telemetry scenarios.

**Wikipedia:** [Bandwidth (Computing)](https://en.wikipedia.org/wiki/Bandwidth_(computing))

### Latency
Time for data to travel from source to destination. Critical for real-time applications.

**Wikipedia:** [Latency](https://en.wikipedia.org/wiki/Latency_(engineering))

## Standards & Organizations

### RFC (Request for Comments)
Standards documents from IETF. Not all RFCs are standards (some informational). Status: Proposed Standard → Draft Standard → Internet Standard.

### IETF (Internet Engineering Task Force)
Organization developing internet standards through consensus. RFCs published through IETF.

### IEEE (Institute of Electrical and Electronics Engineers)
Standards organization publishing numbered standards (IEEE 802.11 WiFi, IEEE 1588 PTP, etc.).

### ISO (International Organization for Standardization)
International standards body. Example: ISO 28500 is WARC standard.

### CNCF (Cloud Native Computing Foundation)
Organization under Linux Foundation promoting cloud-native technologies. Examples: Kubernetes, CloudEvents, NATS, Prometheus.

### OASIS (Organization for the Advancement of Structured Information Standards)
Standards organization. Examples: MQTT, AMQP standards.

### FOSS (Free and Open Source Software)
Software with source code freely available and permissive licensing. Examples: Apache 2.0, BSD, GPL, AGPL.

### Open Standard
Published specification allowing independent implementations. Not vendor-controlled.

### Proprietary Standard
Standard controlled by single vendor. Often not published. Example: AWS S3 API (de facto standard but not formally specified).

### De Facto Standard
Technology widely adopted without formal standardization. Example: S3 API (many implementations but not ISO/IETF standard).

## Data Synchronization Terms

### Multi-Sensor Synchronization
Aligning data from multiple sensors with different clocks and sample rates. Requires timestamps and clock recovery.

### Temporal Correlation
Matching events across streams based on timestamps. Essential for correlating EEG, video, and sensor data.

### Timestamp
Time point associated with data. Absolute (wall clock) or relative (sample count).

### Sample Rate / Sampling Frequency
Frequency of data collection. Examples: EEG 256 Hz, video 60 Hz. Must be synchronized for correlation.

### Skew / Clock Drift
Divergence between clocks over time. Linear drift (steady rate) vs random walk (noisy drift).

### Slew
Gradual adjustment of clock frequency to correct drift without step change. Preferred over reset to avoid discontinuities.

### Frame
Single unit of video or sampled data. Frame number provides temporal indexing.

### Frame Rate
Video frames per second. Must match recording frame rate (60, 120, etc.).

### Codec
Algorithm for compressing/decompressing media. Examples: H.264 video, AAC audio.

**Wikipedia:** [Codec](https://en.wikipedia.org/wiki/Codec)

## Telemetry-Specific Terms

### EEG (Electroencephalography)
Measurement of electrical brain activity. Typical sampling: 256-1000 Hz, 0-40 microvolts signal, 16-32 channels.

**Wikipedia:** [Electroencephalography](https://en.wikipedia.org/wiki/Electroencephalography)

### SCPI (Standard Commands for Programmable Instruments)
Standard language for controlling test equipment (oscilloscopes, multimeters, power supplies).

**Wikipedia:** [Standard Commands for Programmable Instruments](https://en.wikipedia.org/wiki/Standard_Commands_for_Programmable_Instruments)

### Sensor
Device measuring physical quantity (temperature, pressure, acceleration, etc.). Generates time-series data.

### DAQ (Data Acquisition)
Hardware/software for collecting sensor data. Examples: NI DAQmx, Measurement Computing.

### Telemetry
Remote measurement and data collection. Key distinction: raw sensor data (local), telemetry (transmitted/recorded).

### Metadata
Data describing data. In telemetry: channel names, units, calibration, timestamps, source identification.

## Miscellaneous Terms

### Latency Budget
Target breakdown of where latency can occur. Example: 100ms total = 10ms network + 20ms processing + 70ms buffer.

### Overhead
Additional data/processing needed beyond core functionality. RaptorQ overhead <0.2% means <2GB needed to transfer 1GB data.

### Scalability
Ability to handle increased load. Vertical (single machine) vs horizontal (multiple machines).

**Wikipedia:** [Scalability](https://en.wikipedia.org/wiki/Scalability)

### Throughput
Amount of work completed per unit time. Messages/sec, bytes/sec, operations/sec depending on context.

### Idempotent
Operation producing same result regardless of repetition. Important for exactly-once semantics.

**Wikipedia:** [Idempotence](https://en.wikipedia.org/wiki/Idempotence)

### Graceful Degradation
System continuing to function with reduced capacity when components fail.

### Back-Pressure
Mechanism for consumers to signal producers to slow down. Prevents buffer overflow and queue accumulation.

### Buffering
Temporary storage of data accommodating timing differences. Larger buffer = more latency but tolerance for jitter/clock drift.

---

**Last Updated:** 2026-01-16
**Scope:** Synchronized Telemetry Streaming Research Project
