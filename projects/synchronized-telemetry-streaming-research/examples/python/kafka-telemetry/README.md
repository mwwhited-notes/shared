# Kafka Telemetry Producer with CloudEvents

Stream telemetry data to Apache Kafka using the CNCF CloudEvents specification for standardized event envelopes.

## Overview

This example demonstrates:
- **Kafka Producer**: Publish events to Kafka topics with partitioning
- **CloudEvents Envelope**: CNCF standard event format with metadata
- **Multiple Serialization Formats**: JSON, Avro, Protobuf support
- **Sensor Data Simulation**: Generate synthetic telemetry data
- **Distributed Tracing**: Trace context propagation (W3C Trace Context)
- **Partition Strategy**: Partition by sensor ID for ordered consumption

## Requirements

### Software
```bash
pip install -r requirements.txt
```

### Infrastructure
- Apache Kafka 3.x cluster running (local or remote)
- Python 3.8+

### Quick Start with Docker
```bash
# Start Kafka with Docker Compose
docker-compose up -d kafka zookeeper

# Wait for Kafka to be ready (30 seconds)
sleep 30

# Run the producer
python kafka_producer.py
```

## Architecture

### Data Flow
```
Telemetry Source
    ↓
CloudEvents Wrapper
    ↓
Serialization (JSON/Avro)
    ↓
Kafka Producer
    ↓
Kafka Broker Cluster
    ↓
Consumer Groups
```

### CloudEvents Structure
```json
{
  "specversion": "1.0",
  "type": "com.sensor.data",
  "source": "/sensor/temperature/room1",
  "id": "sensor-123-2025-01-16T10:30:45.123Z",
  "time": "2025-01-16T10:30:45.123456Z",
  "datacontenttype": "application/json",
  "dataschema": "https://schema.example.com/sensor-data",
  "subject": "room/living_room",
  "traceparent": "00-trace_id-span_id-01",
  "data": {
    "temperature": 22.5,
    "humidity": 65,
    "unit": "celsius"
  }
}
```

## Module Reference

### `kafka_producer.py`
Main producer implementation with:
- Kafka connection management
- CloudEvents envelope creation
- Partition strategy (by sensor ID)
- Error handling and retries
- Performance metrics

### `cloudevents_wrapper.py`
CloudEvents serialization helper:
- Event creation with standard attributes
- Multiple serialization formats
- Schema validation
- Timestamp correlation

### `telemetry_generator.py`
Synthetic telemetry data generator:
- Simulated sensor values (temperature, humidity, pressure)
- Time-series patterns (diurnal cycles, trends)
- Multi-sensor scenarios
- Anomaly injection for testing

## Configuration

### `config.yaml` Structure
```yaml
kafka:
  bootstrap_servers: ["localhost:9092"]
  topic: "telemetry"

producer:
  serialization: "json"  # json, avro, protobuf
  compression: "snappy"
  batch_size: 100
  linger_ms: 100

telemetry:
  sensors: ["temp", "humidity", "pressure"]
  sample_rate: 10  # Hz

cloudevents:
  source: "/sensors/datacenter1"
  dataschema: "https://schema.example.com/sensor"
```

## Usage Examples

### Basic Producer
```python
from kafka_producer import TelemetryProducer
from telemetry_generator import SensorDataGenerator

producer = TelemetryProducer(config)
generator = SensorDataGenerator(config)

for data in generator.generate():
    producer.publish(data)
```

### With Partitioning
```yaml
# Partition by sensor ID for ordered processing
producer:
  partition_key_field: "sensor_id"  # All events from same sensor → same partition
```

### With Distributed Tracing
```python
# Traces propagate through Kafka
event = producer.create_event(
    sensor_data,
    trace_context="00-abc123-def456-01"  # W3C Trace Context
)
```

## Performance Tuning

### High Throughput
```yaml
producer:
  batch_size: 1000
  linger_ms: 1000  # Wait up to 1s for batch
  compression: "snappy"  # 50% reduction typical
  acks: 1  # Faster (vs. 3 for durability)
```

### Low Latency
```yaml
producer:
  batch_size: 10
  linger_ms: 10
  compression: "none"
  acks: 1
```

### High Durability
```yaml
producer:
  acks: "all"  # Wait for all replicas
  retries: 3
  retry_backoff_ms: 1000
```

## Consuming Telemetry

### Using kafka-python
```python
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'telemetry',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    group_id='analysis_group'
)

for event in consumer:
    print(f"Event: {event.value}")
    # Process CloudEvent
    if event.value['type'] == 'com.sensor.data':
        sensor_data = event.value['data']
        print(f"Temperature: {sensor_data['temperature']}")
```

### Using confluent-kafka-python
```python
from confluent_kafka import Consumer

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'telemetry_group',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['telemetry'])

while True:
    msg = consumer.poll(timeout=1.0)
    if msg is None:
        continue

    event = json.loads(msg.value().decode('utf-8'))
    print(f"Received: {event['source']} - {event['data']}")
```

## Kafka Topics Setup

### Create Topic
```bash
# Via docker-compose service
docker-compose exec kafka kafka-topics.sh --create \
  --topic telemetry \
  --bootstrap-server localhost:9092 \
  --partitions 10 \
  --replication-factor 3

# Or with confluent
confluent kafka topic create telemetry -p 10 -rf 3
```

### Monitor Topic
```bash
# Check topic metadata
docker-compose exec kafka kafka-topics.sh --describe \
  --topic telemetry \
  --bootstrap-server localhost:9092

# Monitor consumer group lag
docker-compose exec kafka kafka-consumer-groups.sh --describe \
  --group analysis_group \
  --bootstrap-server localhost:9092
```

## Monitoring

### Metrics
The producer exports:
- `messages_sent` - Total messages published
- `bytes_sent` - Total bytes transferred
- `errors` - Failed publish attempts
- `latency_ms` - Average round-trip time

### Logs
```bash
# View producer logs
docker-compose logs -f kafka

# Enable debug logging (edit config.yaml)
logging:
  level: DEBUG
```

## Troubleshooting

### Connection Issues
- **"Connection refused"**: Verify Kafka is running (`docker-compose ps`)
- **"Broker not available"**: Check bootstrap_servers in config
- **"Topic does not exist"**: Create topic first

### Performance
- Monitor partition lag: `kafka-consumer-groups.sh --describe`
- Check batch sizes and compression in config
- Increase producer pool size if CPU-bound

### Data Quality
- Validate schema in cloudevents_wrapper.py
- Check telemetry_generator for realistic patterns
- Monitor error rates in metrics

## References

- **CloudEvents Spec**: https://github.com/cloudevents/spec
- **Kafka Documentation**: https://kafka.apache.org/documentation/
- **confluent-kafka-python**: https://github.com/confluentinc/confluent-kafka-python
- **W3C Trace Context**: https://www.w3.org/TR/trace-context/

## License

Educational/research use.

---
**Created**: 2026-01-16
**Updated**: 2026-01-16
