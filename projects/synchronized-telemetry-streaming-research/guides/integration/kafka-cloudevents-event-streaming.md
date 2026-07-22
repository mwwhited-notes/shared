# Kafka Event Streaming with CloudEvents Integration Guide

## Overview
Implement event-driven telemetry using Kafka and CloudEvents CNCF standard for inter-service communication and data integration.

## Architecture
```
Telemetry Sources
    ↓
CloudEvents Wrapper
    ↓
Kafka Cluster (Topics)
    ↓
Consumer Groups (Analytics, Storage, Alerts)
```

## Setup
1. Install Kafka: `docker-compose up kafka zookeeper`
2. Create topics: `kafka-topics.sh --create --topic telemetry`
3. Run producer: `python examples/python/kafka-telemetry/kafka_producer.py`

## CloudEvents Benefits
- **Standardized envelopes**: Metadata and data separation
- **Schema evolution**: Add fields without breaking consumers
- **Distributed tracing**: W3C Trace Context propagation
- **Cross-system interoperability**: Cloud-native standards

## Configuration
```yaml
kafka:
  bootstrap_servers: ["localhost:9092"]
  topic: "telemetry"
producer:
  acks: 1
  compression: "snappy"
```

## Consumer Example
```python
consumer = KafkaConsumer('telemetry', bootstrap_servers=['localhost:9092'])
for msg in consumer:
    event = json.loads(msg.value())
    print(f"Event: {event['type']} from {event['source']}")
```

## Diagrams

### Event Streaming Architecture

```plantuml
@startuml Kafka Event Streaming with CloudEvents
skinparam backgroundColor #FEFECE
skinparam defaultFontName Helvetica
skinparam defaultFontSize 10

title Kafka Event Streaming Architecture with CloudEvents Envelope

package "Event Producers" {
    component [Sensor Producer 1] as prod1
    component [Sensor Producer 2] as prod2
    component [Instrument Producer] as prod3
    component [Stream Processor] as prod4
}

package "CloudEvents Envelope" {
    note "CloudEvents Wrapper - specversion - type - source - subject - datacontenttype - timestamp - dataschema" as ce_note
}

package "Kafka Cluster" {
    component [Broker 1] as broker1
    component [Broker 2] as broker2
    component [Broker 3] as broker3
}

package "Topics (Partitioned)" {
    queue [telemetry-raw (Partition 0-7)] as topic_raw
    queue [telemetry-processed (Partition 0-3)] as topic_proc
    queue [events-alarms (Partition 0-4)] as topic_alarms
}

package "Consumer Groups" {
    component [Storage Consumer (Group storage)] as consumer_storage
    component [Analytics Consumer (Group analytics)] as consumer_analytics
    component [Alert Consumer (Group alerts)] as consumer_alerts
}

package "Downstream Processing" {
    component [S3 Sink] as s3_sink
    component [InfluxDB Sink] as influx_sink
    component [Alert Engine] as alert_engine
    component [ML Pipeline] as ml_pipe
}

prod1 --> ce_note
prod2 --> ce_note
prod3 --> ce_note
prod4 --> ce_note

ce_note --> topic_raw
ce_note --> topic_proc
ce_note --> topic_alarms

topic_raw --> broker1
topic_proc --> broker2
topic_alarms --> broker3

broker1 --> consumer_storage
broker2 --> consumer_analytics
broker3 --> consumer_alerts

consumer_storage --> s3_sink
consumer_analytics --> influx_sink
consumer_analytics --> ml_pipe
consumer_alerts --> alert_engine

note right of prod1
  Serialization:
  JSON human-readable
  Avro schema evolution
  Protobuf compact
end note

note right of broker1
  Replication Factor 3
  Min ISR 2
  Retention 7 days
  Compression snappy
end note

note right of consumer_storage
  Consumer Properties:
  auto.offset.reset earliest
  enable.auto.commit false
  isolation.level read_committed
end note

@enduml
```

### CloudEvents Message Flow (CNCF Standard)

```plantuml
@startuml Kafka CloudEvents Message Flow
skinparam backgroundColor #FEFEFE
skinparam defaultFontName Helvetica
skinparam defaultFontSize 10
skinparam sequenceArrowThickness 2

title Kafka CloudEvents Message Flow (CNCF Standard)

participant "Event Producer" as prod
participant "Kafka Producer API" as ka
participant "Broker Partition" as broker
participant "Consumer Group" as cg
participant "Event Consumer" as cons

autonumber

prod -> prod: CreateCloudEvent
note right of prod
  specversion 1.0
  type com.sensor.data
  source /sensor/temp001
  id abc-123
  time 2025-01-16T10:30:45Z
  datacontenttype application/json
  payload {temp: 22.5, humidity: 65}
end note

prod -> ka: send(topic, key, value, headers)

ka -> broker: WriteRecord
note right of broker
  partition 0
  offset 12345
  key_len 19
  value_len 285
  timestamp Unix-ms
end note

broker -> broker: PersistToLog
note right of broker
  replication 3x
  min_isr 2
end note

broker -> cg: FetchRecords
note right of broker
  partition 0
  offset 12345
  max_records 100
end note

cg -> cons: onMessage
note right of cons
  event_headers
  event_body
  metadata
end note

cons -> cons: ParseCloudEvent
note right of cons
  verify_required_attrs
  parse_data_schema
end note

cons -> cons: ValidatePayload
note right of cons
  dataschema JSON-Schema
  result valid
end note

cons -> cons: ProcessEvent
note right of cons
  temp 22.5
  humidity 65
  room living_room
  timestamp 2025-01-16T10:30:45Z
end note

cons -> cons: EmitMetrics
note right of cons
  influxdb_point temp
  tags sensor/temp001,room
  fields value 22.5
end note

cg -> ka: commitOffset
note right of cg
  partition 0
  offset 12345
end note

ka -> broker: OffsetCommit
note right of broker
  consumer_group analytics
  offset_store __consumer_offsets
end note

note right of cons
  Benefits:
  Schema evolution safe
  Metadata standardized
  Cross-system interop
  Traceable
end note

note left of broker
  Scaling Strategy:
  Partitioning by source
  Consumer groups parallel
  Rebalancing transparent
end note

@enduml
```

## References
- Code: `examples/python/kafka-telemetry/`
- CloudEvents Spec: https://cloudevents.io/

---
Created: 2026-01-16
