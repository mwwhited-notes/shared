# Event Streaming Alternatives to Kafka: Patterns & Standards

Comprehensive guide to Kafka alternatives, including when to avoid Kafka, in-process vs. out-of-process options, and protocols for different use cases.

## Table of Contents

- [Why Avoid Kafka?](#why-avoid-kafka)
- [FOSS Alternatives Overview](#foss-alternatives-overview)
- [In-Process Options](#in-process-options)
- [Out-of-Process Options](#out-of-process-options)
- [Comparison Matrix](#comparison-matrix)
- [Technology Profiles](#technology-profiles)
- [Decision Tree](#decision-tree)
- [Recommended Stacks](#recommended-stacks)

## Why Avoid Kafka?

### Kafka's Weaknesses

**Operational Overhead:**
- Requires separate cluster (3+ nodes minimum for production)
- ZooKeeper dependency (adds complexity)
- Requires operational expertise
- Significant resource footprint (not for embedded systems)

**Performance Trade-offs:**
- High throughput (good) but high latency (bad for real-time)
- Not optimized for low-cardinality streams
- Overkill for small/medium deployments
- Compaction can cause GC pauses

**Cost:**
- Cluster infrastructure costs
- Operational overhead (SRE time)
- Network bandwidth
- Storage (for retention)

**Complexity:**
- Learning curve steep
- Consumer group management confusing
- Rebalancing can cause data loss if misconfigured
- Debugging distributed issues hard

**When to Consider Alternatives:**
✅ Embedded/edge systems (resource-constrained)
✅ Low-latency requirements (<10ms)
✅ Single machine or small cluster
✅ Simple pub/sub (no complex processing)
✅ Lightweight IoT/sensor networks
✅ In-process application messaging

---

## Architecture Patterns

### Pattern 1: Out-of-Process Brokers (Separate Service)

**For:** Network communication between services

```
┌─────────────┐         ┌─────────────┐
│   Service A │◄────────│   Broker    │◄────────┐
│  (Producer) │         │  (NATS,     │         │
└─────────────┘         │  RabbitMQ)  │    ┌────────────┐
                        └─────────────┘    │  Service B │
                                           │(Consumer)  │
                                           └────────────┘
```

**Options:**
- NATS
- RabbitMQ (lightweight mode)
- Redis Streams (if you already use Redis)
- Apache Pulsar (if you need Kafka-scale)

---

### Pattern 2: In-Process Queues (Embedded)

**For:** Single-process threading or IPC

```
┌───────────────────────────────────────┐
│         Single JVM Process            │
│                                       │
│  ┌────────────┐    ┌──────────────┐ │
│  │ Producer   │──→ │ Ring Buffer  │ │
│  │ Thread     │    │ (Disruptor)  │ │
│  └────────────┘    └──────────────┘ │
│                            ↓          │
│                    ┌──────────────┐  │
│                    │ Consumer     │  │
│                    │ Thread       │  │
│                    └──────────────┘  │
└───────────────────────────────────────┘
```

**Options:**
- LMAX Disruptor (threads within process)
- Chronicle Queue (JVM-to-JVM IPC)
- Java Queues (ArrayBlockingQueue, ConcurrentLinkedQueue)

---

### Pattern 3: Hybrid (In-Process + Network)

**For:** Local buffering + remote sync

```
┌─────────────────────┐
│  Local Application  │
│  ┌───────────────┐  │
│  │ Disruptor/    │◄─┼─ Network
│  │ Chronicle     │  │  (NATS)
│  └───────────────┘  │
└─────────────────────┘
```

**Use:** Event batching locally, sending to remote broker periodically

---

## Out-of-Process Broker Alternatives

### Apache Pulsar

**Status:** Apache project | [GitHub](https://github.com/apache/pulsar)

**Architecture:**
- Separation of compute (brokers) and storage (BookKeepers)
- Geo-replication built-in
- Multi-tenancy support
- Topic-based (like Kafka)

**Performance:**
- Kafka: 15x faster writes than RabbitMQ, 2x faster than Pulsar
- **Pulsar:** 2.6M msgs/sec consumer throughput (vs Kafka comparable)
- High latency tolerance

**Strengths:**
✅ Kafka-compatible API (if familiar)
✅ Geographically distributed (built-in)
✅ Better separation of concerns (compute/storage)
✅ Good for multi-region deployments

**Limitations:**
❌ Complex (similar to Kafka)
❌ Slower throughput than Kafka
❌ Requires operational overhead
❌ Niche ecosystem

**When to use:**
→ Kafka-scale but need geo-replication
→ Multi-region deployments
→ Complex topic management

**Cross-reference:**
- Similar operational complexity to Kafka, only choose if multi-region is critical

---

### NATS

**Status:** Open Source (Synadia) | [Official](https://nats.io/)

**Model:**
- Subject-based pub/sub (not topics)
- Multiple patterns:
  - Publish/Subscribe (one-way)
  - Request/Reply (two-way)
  - Streams (JetStream - optional persistence)

**Architecture:**
```
Server (lightweight Go binary)
├─ Core NATS (pub/sub, req/reply)
├─ JetStream (optional persistence)
└─ KV Store (optional key-value)
```

**Performance:**
- Millions of msgs/sec
- **Very low latency** (microseconds)
- Lightweight (<20MB memory for server)
- Single binary (easy deployment)

**Strengths:**
✅ Extremely lightweight (deploys easily)
✅ Very low latency (excellent for real-time)
✅ Multiple patterns (pub/sub, req/reply, streams)
✅ Text-based protocol (debuggable)
✅ Minimal operational overhead
✅ Great for IoT/edge

**Limitations:**
❌ Lower throughput than Kafka/Pulsar
❌ Smaller ecosystem
❌ JetStream (persistence) less mature than Kafka

**When to use:**
→ IoT/edge systems (resource-constrained)
→ Real-time, low-latency messaging
→ Simple pub/sub patterns
→ Cloud-native microservices

**Example Configuration:**
```yaml
# nats-server.conf
port: 4222
jetstream:
  store_dir: /var/lib/nats/jetstream
  max_memory_store: 1GB
```

**Comparison with Kafka:**
| Aspect | NATS | Kafka |
|--------|------|-------|
| Latency | Ultra-low (μs) | Higher (ms) |
| Throughput | Good (1M+/s) | Excellent (15M+/s) |
| Operational | Simple | Complex |
| Memory | ~20MB | ~1GB+ |
| Deployment | Single binary | Cluster |

---

### RabbitMQ

**Status:** Industry standard | [Official](https://www.rabbitmq.com/)

**Model:**
- Exchange → Queue → Consumer
- Multiple protocols: AMQP, MQTT, STOMP, HTTP
- Flexible routing (not topic-based)

**New Feature: Streams (v3.11+)**
- Similar to Kafka topics
- Immutable log semantics
- Consumer group tracking

**Performance:**
- Throughput: 48K-500K msgs/sec (depends on config)
- **15x slower than Kafka** (write throughput)
- **Better at** low-cardinality, request/reply patterns

**Strengths:**
✅ Proven, battle-tested (15+ years)
✅ Multiple protocol support (AMQP, MQTT, STOMP)
✅ Traditional queue + new streams option
✅ Excellent for IoT (MQTT)
✅ Good for microservices (request/reply)
✅ Simpler than Kafka

**Limitations:**
❌ Lower throughput than Kafka
❌ Not designed for massive scale
❌ Streams mode still less mature than Kafka

**When to use:**
→ Traditional message queues (not event streams)
→ MQTT integration (IoT)
→ Request/reply patterns
→ Microservice communication
→ Existing RabbitMQ infrastructure

**Deployment Options:**
- Self-hosted
- Managed: CloudAMQP, AWS RabbitMQ, Azure
- Kubernetes: Helm charts available

---

### Redis Streams

**Status:** Redis feature (v5.0+) | [Official](https://redis.io/docs/data-types/streams/)

**Model:**
- Key-value database with stream data type
- Append-only log (immutable)
- Consumer group tracking
- Lightweight persistence (AOF/RDB)

**Performance:**
- **Low-latency** (in-memory)
- Moderate throughput (depends on persistence)
- **Ultra-fast reads** (memory resident)

**Architecture:**
```
Redis Server
├─ In-Memory (primary)
├─ Persistence (optional: RDB snapshots or AOF)
└─ Replication (optional: leader-follower)
```

**Strengths:**
✅ Simple (if you already use Redis)
✅ Low-latency (in-memory)
✅ Multi-purpose (caching + streams)
✅ Easy deployment (single binary)
✅ Good for small-medium scale
✅ Excellent debugging (redis-cli)

**Limitations:**
❌ **Data loss if server crashes** (mitigation: persistence/replication)
❌ Single-machine by default (replication slower)
❌ Lower throughput than Kafka
❌ Memory footprint (everything in RAM)

**When to use:**
→ You already use Redis (combine functionality)
→ Low-latency, small-medium scale
→ Simple pub/sub (upgrade from Redis Pub/Sub)
→ Single-machine OK
→ Budget-conscious (free + your infrastructure)

**Kafka vs. Redis Streams:**

| Aspect | Redis Streams | Kafka |
|--------|--------------|-------|
| **Latency** | Low (ms) | Higher (ms+) |
| **Durability** | Optional | Built-in |
| **Throughput** | Moderate | Excellent |
| **Scale** | Single machine | Distributed clusters |
| **Data Loss Risk** | High (if not replicated) | Low |
| **Operational** | Simple | Complex |
| **Cost** | Low (existing Redis) | High (cluster) |

**Recommendation:**
- **Already use Redis?** → Redis Streams (avoid Kafka complexity)
- **Need durability?** → Configure persistence + replication
- **High throughput needed?** → Kafka or Pulsar
- **Budget tight?** → Redis Streams

---

## In-Process Queues (Single Machine/Process)

### LMAX Disruptor

**Status:** Open Source (LMAX Exchange) | [GitHub](https://github.com/LMAX-Exchange/disruptor)

**What it is:**
Concurrent ring buffer for ultra-fast inter-thread messaging within single JVM.

**Architecture:**
```
┌──────────────────────────────┐
│  Pre-allocated Ring Buffer   │
│                              │
│  ┌─────┬─────┬─────┬─────┐ │
│  │[0]  │[1]  │[2]  │[3]  │ │
│  └─────┴─────┴─────┴─────┘ │
│         ↓                    │
│  Write Pointer → Read Pointer│
└──────────────────────────────┘
```

**Performance:**
- **3 orders of magnitude lower latency** than queue-based approach
- **8x higher throughput** than traditional queues
- Typical latency: **single-digit microseconds**

**Key Features:**
- Pre-allocated (no GC)
- Lock-free algorithms
- Mechanical sympathy (CPU cache-aware)
- Single writer/reader per lane
- Event handler patterns

**Strengths:**
✅ Extremely low latency (microseconds)
✅ No garbage collection
✅ Extremely high throughput (millions/sec)
✅ Deterministic performance
✅ Perfect for high-frequency trading

**Limitations:**
❌ In-process only (single JVM)
❌ Complex API (not simple queue)
❌ Java-only
❌ Overkill for simple use cases

**When to use:**
→ Ultra-low latency critical (<1μs)
→ High-frequency trading, market data
→ Real-time systems (sub-millisecond)
→ Multi-threaded Java applications

**Example:**
```java
Disruptor<Event> disruptor = new Disruptor<>(
    Event::new,
    1024,  // ring buffer size
    Executors.newFixedThreadPool(1)
);
disruptor.handleEventsWith((event, sequence, endOfBatch) -> {
    // Process event
});
disruptor.start();
```

---

### Chronicle Queue

**Status:** Open Source (OpenHFT) | [GitHub](https://github.com/OpenHFT/Chronicle-Queue)

**What it is:**
Broker-less, persisted IPC (inter-process communication) for JVMs on same machine or network.

**Dual Mode:**
1. **IPC Mode** (same machine): Ultra-low latency (~1 microsecond)
2. **Network Mode** (remote): Low latency (~10 microseconds)

**Architecture:**
```
JVM Process 1          JVM Process 2
┌──────────────┐      ┌──────────────┐
│   Producer   │──────│   Consumer   │
│  (writes to  │      │  (reads from │
│ memory-mapped│      │ memory-mapped│
│    file)     │      │    file)     │
└──────────────┘      └──────────────┘
      ↓                     ↑
    Disk/Network: chronicle.dat
```

**Performance:**
- **IPC (same machine):** ~1 microsecond latency
- **Network:** ~10 microseconds
- Millions of messages/sec
- Persisted (survives crash)

**Strengths:**
✅ Ultra-low latency IPC
✅ Persisted (crash-safe)
✅ Multi-process (different JVMs)
✅ No separate broker
✅ Broker-less architecture

**Limitations:**
❌ JVM-only
❌ Memory-mapped file complexity
❌ Smaller ecosystem than Kafka
❌ Requires local disk/network

**When to use:**
→ Multiple JVMs on same machine
→ Ultra-low latency IPC needed
→ Persistence required (but no broker)
→ Trading systems, market data

**Comparison: Disruptor vs. Chronicle Queue**

| Aspect | Disruptor | Chronicle Queue |
|--------|-----------|-----------------|
| **Scope** | Single JVM threads | Multi-JVM or network |
| **Latency** | 1-10 μs | 1 μs (IPC), 10 μs (network) |
| **Persistence** | No | Yes |
| **Complexity** | Complex API | Simpler |
| **Use** | Trading, real-time | Trading, multi-process IPC |

---

## Comparison Matrix: When to Use Each

```
Use Case: Real-time sensor monitoring (1000s of devices)
→ Choice 1: NATS (simplicity, low-latency)
→ Choice 2: Redis Streams (if Redis already in use)
→ Choice 3: InfluxDB + MQTT (specialized)

Use Case: High-frequency trading (microsecond latency)
→ Choice 1: LMAX Disruptor (single JVM)
→ Choice 2: Chronicle Queue (multi-JVM)
→ Choice 3: NATS (if network needed)

Use Case: Microservices communication
→ Choice 1: RabbitMQ (proven)
→ Choice 2: NATS (lightweight)
→ Choice 3: gRPC (if also need RPC)

Use Case: Data pipeline (terabytes/day)
→ Choice 1: Kafka (proven at scale)
→ Choice 2: Apache Pulsar (geo-replicated)
→ Choice 3: Redis Streams (if budget tight)

Use Case: IoT edge devices (resource-constrained)
→ Choice 1: NATS (minimal footprint)
→ Choice 2: MQTT (specialized for IoT)
→ Choice 3: Local Chronicle Queue (per edge)

Use Case: Existing Redis infrastructure
→ Choice 1: Redis Streams (leverage existing)
→ Choice 2: NATS (parallel infrastructure)
→ Choice 3: Kafka (only if scale demands)
```

---

## Protocol Comparison

| Protocol | Type | Encoding | Latency | Throughput | Best For |
|----------|------|----------|---------|-----------|----------|
| **NATS Core** | Pub/Sub | Text | Ultra-low | 1M+ msgs/s | Real-time, simple |
| **AMQP 1.0** | Queue | Binary | Low | 500K msgs/s | Microservices |
| **MQTT** | Pub/Sub | Binary | Very low | 1M+ msgs/s | IoT devices |
| **Kafka Protocol** | Stream | Binary | Medium | 15M+ msgs/s | Data pipelines |
| **Redis Protocol** | Streams | Binary | Low | 1M+ msgs/s | Caching + streams |
| **Disruptor** | In-process | N/A | Ultra-low (1μs) | 50M+ msgs/s | Trading systems |
| **Chronicle IPC** | IPC | Binary | Ultra-low (1μs) | 10M+ msgs/s | Multi-JVM systems |

---

## Decision Tree

```
START: What do you need?

├─ Microsecond latency?
│  └─ YES → LMAX Disruptor (same JVM) or Chronicle Queue (multi-JVM)
│  └─ NO → Continue
│
├─ Multi-region/geo-replication?
│  └─ YES → Apache Pulsar
│  └─ NO → Continue
│
├─ Terabyte-scale data pipeline?
│  └─ YES → Apache Kafka
│  └─ NO → Continue
│
├─ Already using Redis?
│  └─ YES → Redis Streams
│  └─ NO → Continue
│
├─ IoT devices or edge systems?
│  └─ YES → NATS or MQTT
│  └─ NO → Continue
│
├─ Microservices, request/reply?
│  └─ YES → RabbitMQ or NATS
│  └─ NO → Continue
│
└─ Simple pub/sub, low-latency?
   └─ YES → NATS
   └─ NO → Kafka (fallback to industry standard)
```

---

## Hybrid Strategies

### Strategy 1: NATS + Local Buffer

```
NATS Server (central)
     ↑
     │ (async, batched)
     │
Local Ring Buffer
     ↑
Sensor readings (high-frequency)
```

**Benefit:** Capture fast data locally, send to central broker periodically

### Strategy 2: Redis Streams + Kafka

```
Redis Streams (hot data, caching)
     ↓ (batch export)
Kafka (archive, long-term)
```

**Benefit:** Fast reads from Redis, durable storage in Kafka

### Strategy 3: NATS JetStream + Chronicle Queue

```
Chronicle Queue (local persistence)
     ↓
NATS JetStream (network sync)
```

**Benefit:** Ultra-low IPC latency, network fallback

---

## References

### Kafka Alternatives
- [Confluent: Kafka vs. Pulsar](https://www.confluent.io/kafka-vs-pulsar/)
- [Redpanda: Kafka Alternatives](https://www.redpanda.com/guides/kafka-alternatives)
- [RisingWave: Comparing Kafka Alternatives](https://risingwave.com/blog/comparing-apache-kafka-alternatives/)

### In-Process Queues
- [LMAX Disruptor](https://lmax-exchange.github.io/disruptor/)
- [Chronicle Queue Documentation](https://github.com/OpenHFT/Chronicle-Queue)

### Specific Technologies
- [NATS Official Documentation](https://nats.io/)
- [RabbitMQ Streams](https://www.rabbitmq.com/docs/streams)
- [Redis Streams](https://redis.io/docs/data-types/streams/)
- [Apache Pulsar Docs](https://pulsar.apache.org/docs/)

### Comparisons
- [StreamNative: Pulsar vs. RabbitMQ vs. NATS](https://streamnative.io/blog/comparison-of-messaging-platforms-apache-pulsar-vs-rabbitmq-vs-nats-jetstream/)
- [NATS Comparison](https://docs.nats.io/nats-concepts/overview/compare-nats)
- [Better Stack: Redis vs. Kafka](https://betterstack.com/community/comparisons/redis-vs-kafka/)

---

*Last updated: 2026-01-16*

*Part of: [Synchronized Telemetry Streaming Research](README.md)*

*For Kafka decision-making, see decision tree above. For specific use case guidance, see comparison matrix.*
