#!/usr/bin/env python3
"""
CloudEvents Standard Wrapper (CNCF Specification)

Implements CloudEvents specification v1.0 for standardized event envelopes.
https://cloudevents.io/
"""

import json
import uuid
from datetime import datetime, timezone
from typing import Dict, Any, Optional


class CloudEvent:
    """CloudEvents v1.0 event implementation."""

    REQUIRED_ATTRIBUTES = [
        'specversion',
        'type',
        'source',
        'id',
    ]

    OPTIONAL_ATTRIBUTES = [
        'datacontenttype',
        'dataschema',
        'subject',
        'time',
        'traceparent',
    ]

    def __init__(self, **kwargs):
        """
        Create a CloudEvent.

        Required:
            type: Event type (e.g., com.sensor.data)
            source: Event source (e.g., /sensor/temperature/room1)
            id: Unique event identifier

        Optional:
            specversion: CloudEvents version (default: 1.0)
            datacontenttype: Content type (default: application/json)
            dataschema: Schema URI
            subject: Describes subject
            time: Event timestamp (default: now)
            data: Event payload
            traceparent: W3C Trace Context
        """
        # Set defaults
        self.attributes = {
            'specversion': '1.0',
            'datacontenttype': 'application/json',
        }

        # Set required and optional attributes
        for attr in self.REQUIRED_ATTRIBUTES + self.OPTIONAL_ATTRIBUTES:
            if attr in kwargs:
                self.attributes[attr] = kwargs[attr]

        # Validate required attributes
        for attr in self.REQUIRED_ATTRIBUTES:
            if attr not in self.attributes or self.attributes[attr] is None:
                raise ValueError(f"Required attribute missing: {attr}")

        # Set default timestamp if not provided
        if 'time' not in self.attributes:
            self.attributes['time'] = datetime.now(timezone.utc).isoformat()

        # Data (separate from attributes)
        self.data = kwargs.get('data', {})

        # Extension attributes (arbitrary key-value pairs)
        self.extensions = {k: v for k, v in kwargs.items()
                          if k not in self.REQUIRED_ATTRIBUTES and
                          k not in self.OPTIONAL_ATTRIBUTES and
                          k not in ['data']}

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert to dictionary representation.

        Returns:
            Dictionary with all attributes, extensions, and data
        """
        event_dict = dict(self.attributes)
        event_dict.update(self.extensions)

        if self.data:
            event_dict['data'] = self.data

        return event_dict

    def to_json(self) -> str:
        """Convert to JSON string."""
        return json.dumps(self.to_dict())

    def __repr__(self) -> str:
        return f"<CloudEvent {self.attributes.get('type')} id={self.attributes.get('id')}>"


class CloudEventFactory:
    """Factory for creating CloudEvents with default configuration."""

    def __init__(self, config: Dict[str, Any]):
        """
        Initialize factory with configuration.

        Args:
            config: Configuration dictionary with:
                - source: Default event source
                - dataschema: Default schema URI
                - type_prefix: Event type prefix
        """
        self.config = config
        self.source = config.get('source', '/sensors/default')
        self.dataschema = config.get('dataschema', '')
        self.type_prefix = config.get('type_prefix', 'com.sensor')

    def create(self, payload: Dict[str, Any], **kwargs) -> CloudEvent:
        """
        Create a CloudEvent from payload.

        Args:
            payload: Event data (will be wrapped in 'data' field)
            **kwargs: Override default attributes

        Returns:
            CloudEvent instance
        """
        # Extract sensor info for tracing
        sensor_id = payload.get('sensor_id', 'unknown')
        measurement_type = payload.get('measurement_type', 'data')

        # Build event attributes
        event_kwargs = {
            'type': f"{self.type_prefix}.{measurement_type}",
            'source': self.source,
            'id': f"{sensor_id}-{datetime.now(timezone.utc).isoformat()}",
            'subject': f"sensor/{sensor_id}",
            'data': payload,
        }

        # Add optional schema if configured
        if self.dataschema:
            event_kwargs['dataschema'] = self.dataschema

        # Override with provided kwargs
        event_kwargs.update(kwargs)

        return CloudEvent(**event_kwargs)

    def create_from_measurement(self, sensor_id: str, measurement: str,
                               value: float, unit: str, **metadata) -> CloudEvent:
        """
        Create a CloudEvent from a single measurement.

        Args:
            sensor_id: Sensor identifier
            measurement: Measurement name (e.g., temperature)
            value: Measurement value
            unit: Unit of measurement
            **metadata: Additional metadata fields

        Returns:
            CloudEvent instance
        """
        payload = {
            'sensor_id': sensor_id,
            'measurement_type': measurement,
            'value': value,
            'unit': unit,
            'timestamp': datetime.now(timezone.utc).isoformat(),
        }
        payload.update(metadata)

        return self.create(payload)


class CloudEventValidator:
    """Validate CloudEvents against specification."""

    @staticmethod
    def validate(event: CloudEvent) -> tuple[bool, list[str]]:
        """
        Validate a CloudEvent.

        Args:
            event: CloudEvent to validate

        Returns:
            (is_valid, list_of_errors)
        """
        errors = []

        # Check required attributes
        for attr in CloudEvent.REQUIRED_ATTRIBUTES:
            if attr not in event.attributes:
                errors.append(f"Missing required attribute: {attr}")
            elif event.attributes[attr] is None:
                errors.append(f"Required attribute is None: {attr}")

        # Validate specversion
        if event.attributes.get('specversion') not in ['1.0']:
            errors.append("specversion must be '1.0'")

        # Validate type format (should follow reverse-DNS or reverse-URI)
        event_type = event.attributes.get('type', '')
        if not event_type or '/' not in event_type and '.' not in event_type:
            errors.append("type should use reverse-DNS or reverse-URI notation")

        # Validate time format if present
        if 'time' in event.attributes:
            try:
                datetime.fromisoformat(event.attributes['time'].replace('Z', '+00:00'))
            except (ValueError, AttributeError):
                errors.append("time must be valid RFC3339 format")

        return len(errors) == 0, errors


def parse_cloudevent_json(json_str: str) -> CloudEvent:
    """
    Parse a CloudEvent from JSON string.

    Args:
        json_str: JSON string representation

    Returns:
        CloudEvent instance
    """
    data = json.loads(json_str)

    # Separate data from attributes
    event_data = data.pop('data', {})

    # Create event with remaining attributes
    event = CloudEvent(data=event_data, **data)

    return event
