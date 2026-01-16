#!/usr/bin/env python3
"""
Kafka Telemetry Producer with CloudEvents

Publishes telemetry data to Kafka topics using CloudEvents standard envelope format.
"""

import logging
import time
import json
from typing import Dict, Any, Optional
import signal
import threading
from datetime import datetime
import uuid

try:
    from kafka import KafkaProducer
    from kafka.errors import KafkaError
except ImportError:
    raise ImportError("Install kafka-python: pip install kafka-python")

try:
    from cloudevents_wrapper import CloudEvent, CloudEventFactory
except ImportError:
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent))
    from cloudevents_wrapper import CloudEvent, CloudEventFactory

import yaml

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class TelemetryProducer:
    """Kafka producer for telemetry events with CloudEvents envelope."""

    def __init__(self, config: Dict[str, Any]):
        """
        Initialize producer.

        Args:
            config: Configuration dictionary
        """
        self.config = config
        self.kafka_config = config.get('kafka', {})
        self.producer_config = config.get('producer', {})
        self.cloudevents_config = config.get('cloudevents', {})

        self.producer = None
        self.running = False
        self.stats = {
            'messages_sent': 0,
            'messages_failed': 0,
            'bytes_sent': 0,
        }

        # Register signal handlers
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)

        self._connect()
        logger.info("TelemetryProducer initialized")

    def _connect(self):
        """Connect to Kafka broker."""
        try:
            bootstrap_servers = self.kafka_config.get('bootstrap_servers', ['localhost:9092'])
            topic = self.kafka_config.get('topic', 'telemetry')

            producer_kwargs = {
                'bootstrap_servers': bootstrap_servers,
                'value_serializer': lambda v: json.dumps(v).encode('utf-8'),
                'acks': self.producer_config.get('acks', 1),
                'retries': self.producer_config.get('retries', 3),
                'batch_size': self.producer_config.get('batch_size', 16384),
                'linger_ms': self.producer_config.get('linger_ms', 10),
                'compression_type': self.producer_config.get('compression', 'snappy'),
            }

            self.producer = KafkaProducer(**producer_kwargs)
            self.topic = topic

            logger.info(f"Connected to Kafka: {bootstrap_servers}")
            logger.info(f"Target topic: {topic}")

        except Exception as e:
            logger.error(f"Failed to connect to Kafka: {e}")
            raise

    def publish(self, event_data: Dict[str, Any], sensor_id: Optional[str] = None) -> bool:
        """
        Publish an event to Kafka.

        Args:
            event_data: Event payload (will be wrapped in CloudEvents)
            sensor_id: Optional sensor ID for partitioning

        Returns:
            True if successful, False otherwise
        """
        try:
            # Create CloudEvent
            factory = CloudEventFactory(self.cloudevents_config)
            cloud_event = factory.create(event_data)

            # Determine partition key (for ordered processing per sensor)
            partition_key = None
            if sensor_id:
                partition_key = sensor_id.encode('utf-8')
            elif 'sensor_id' in event_data:
                partition_key = str(event_data['sensor_id']).encode('utf-8')

            # Send to Kafka
            future = self.producer.send(
                self.topic,
                value=cloud_event.to_dict(),
                key=partition_key
            )

            # Wait for send to complete
            record_metadata = future.get(timeout=10)

            self.stats['messages_sent'] += 1
            self.stats['bytes_sent'] += len(json.dumps(cloud_event.to_dict()).encode('utf-8'))

            logger.debug(f"Published to topic={record_metadata.topic}, "
                         f"partition={record_metadata.partition}, "
                         f"offset={record_metadata.offset}")

            return True

        except KafkaError as e:
            logger.error(f"Kafka error: {e}")
            self.stats['messages_failed'] += 1
            return False
        except Exception as e:
            logger.error(f"Error publishing event: {e}")
            self.stats['messages_failed'] += 1
            return False

    def publish_batch(self, events: list) -> int:
        """
        Publish multiple events efficiently.

        Args:
            events: List of event data dictionaries

        Returns:
            Number of successfully published events
        """
        successful = 0

        for event in events:
            if self.publish(event):
                successful += 1

        # Flush pending messages
        self.flush()

        return successful

    def flush(self, timeout_ms: int = 10000):
        """
        Flush pending messages.

        Args:
            timeout_ms: Timeout in milliseconds
        """
        if self.producer:
            self.producer.flush(timeout=timeout_ms / 1000)

    def get_stats(self) -> Dict[str, Any]:
        """Get producer statistics."""
        total_messages = self.stats['messages_sent'] + self.stats['messages_failed']
        success_rate = (self.stats['messages_sent'] / total_messages * 100) if total_messages > 0 else 0

        return {
            'messages_sent': self.stats['messages_sent'],
            'messages_failed': self.stats['messages_failed'],
            'bytes_sent': self.stats['bytes_sent'],
            'success_rate': f"{success_rate:.1f}%",
        }

    def close(self):
        """Close the producer."""
        if self.producer:
            self.flush()
            self.producer.close()
            logger.info("Producer closed")

    def _signal_handler(self, sig, frame):
        """Handle shutdown signals."""
        logger.info(f"Received signal {sig}, shutting down...")
        self.close()

    def __enter__(self):
        """Context manager support."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager cleanup."""
        self.close()
        return False


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Kafka Telemetry Producer')
    parser.add_argument('-c', '--config', default='config.yaml',
                        help='Configuration file')
    parser.add_argument('-n', '--messages', type=int, default=0,
                        help='Number of messages to send (0=infinite)')
    args = parser.parse_args()

    # Load config
    try:
        with open(args.config) as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        logger.error(f"Config not found: {args.config}")
        return 1
    except yaml.YAMLError as e:
        logger.error(f"Invalid YAML: {e}")
        return 1

    # Create producer
    try:
        with TelemetryProducer(config) as producer:
            from telemetry_generator import SensorDataGenerator

            generator = SensorDataGenerator(config)
            count = 0

            logger.info("Starting to publish events...")
            for sensor_data in generator.generate():
                if args.messages > 0 and count >= args.messages:
                    break

                sensor_id = sensor_data.get('sensor_id')
                if producer.publish(sensor_data, sensor_id):
                    count += 1
                    if count % 100 == 0:
                        stats = producer.get_stats()
                        logger.info(f"Published {count} events. Stats: {stats}")

                time.sleep(1.0 / config.get('telemetry', {}).get('sample_rate', 10))

            # Final stats
            stats = producer.get_stats()
            logger.info(f"Final stats: {stats}")

    except KeyboardInterrupt:
        logger.info("Interrupted by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        return 1

    return 0


if __name__ == '__main__':
    exit(main())
