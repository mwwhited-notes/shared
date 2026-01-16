#!/usr/bin/env python3
"""
Synthetic Telemetry Data Generator

Generates realistic sensor data for testing Kafka producers and consumers.
Includes patterns like diurnal cycles, trends, and anomalies.
"""

import random
import math
import time
from typing import Dict, List, Any, Generator
from datetime import datetime, timedelta


class SensorDataGenerator:
    """Generate synthetic sensor data with realistic patterns."""

    def __init__(self, config: Dict[str, Any]):
        """
        Initialize generator.

        Args:
            config: Configuration with 'telemetry' section
        """
        self.config = config
        self.telemetry_config = config.get('telemetry', {})
        self.sensors = self.telemetry_config.get('sensors', ['temperature', 'humidity'])
        self.sample_rate = self.telemetry_config.get('sample_rate', 10)  # Hz

        self.start_time = datetime.now()
        self.sample_count = 0

        # Sensor parameters
        self.sensor_params = {
            'temperature': {
                'min': 15.0,
                'max': 30.0,
                'mean': 22.0,
                'std': 2.0,
                'drift': 0.01,  # Slow trend
            },
            'humidity': {
                'min': 20.0,
                'max': 80.0,
                'mean': 50.0,
                'std': 10.0,
                'drift': 0.05,
            },
            'pressure': {
                'min': 980.0,
                'max': 1020.0,
                'mean': 1013.0,
                'std': 5.0,
                'drift': 0.001,
            },
        }

    def generate(self) -> Generator[Dict[str, Any], None, None]:
        """
        Generate infinite stream of sensor readings.

        Yields:
            Dictionary with sensor measurements
        """
        sensor_id = 1
        sensor_values = {name: self._initialize_value(name) for name in self.sensors}

        while True:
            timestamp = datetime.now()
            hour = timestamp.hour
            minute = timestamp.minute

            # Generate measurements for each sensor
            measurements = {
                'sensor_id': f'sensor_{sensor_id:03d}',
                'timestamp': timestamp.isoformat(),
                'measurements': {},
            }

            for sensor_name in self.sensors:
                # Get next value with patterns
                value = self._generate_value(
                    sensor_name,
                    sensor_values[sensor_name],
                    hour,
                    self.sample_count
                )

                # Add diurnal cycle (temperature higher during day)
                if sensor_name == 'temperature':
                    diurnal = 3.0 * math.sin(2 * math.pi * (hour + minute / 60) / 24)
                    value += diurnal

                # Clamp to valid range
                params = self.sensor_params[sensor_name]
                value = max(params['min'], min(params['max'], value))

                measurements['measurements'][sensor_name] = {
                    'value': round(value, 2),
                    'unit': self._get_unit(sensor_name),
                }

                sensor_values[sensor_name] = value

            # Inject occasional anomalies (0.1% chance)
            if random.random() < 0.001:
                anomaly_sensor = random.choice(self.sensors)
                measurements['measurements'][anomaly_sensor]['value'] *= 1.5
                measurements['anomaly'] = True

            # Add metadata
            measurements['measurement_type'] = 'sensor_reading'

            yield measurements

            self.sample_count += 1
            time.sleep(1.0 / self.sample_rate)

    def _initialize_value(self, sensor_name: str) -> float:
        """Initialize sensor value from mean."""
        params = self.sensor_params[sensor_name]
        return params['mean']

    def _generate_value(self, sensor_name: str, current_value: float,
                       hour: int, sample_count: int) -> float:
        """
        Generate next value with realistic patterns.

        Includes:
        - Gaussian noise
        - Slow drift (trend)
        - Hourly variations
        """
        params = self.sensor_params[sensor_name]

        # Gaussian noise
        noise = random.gauss(0, params['std'] / 3)

        # Drift (slow trend)
        drift = params['drift'] * (sample_count % 3600)  # Hourly period

        # New value
        new_value = current_value + noise + drift

        # Revert to mean (mean reversion)
        mean_reversion = 0.01 * (params['mean'] - new_value)
        new_value += mean_reversion

        return new_value

    @staticmethod
    def _get_unit(sensor_name: str) -> str:
        """Get SI unit for sensor."""
        units = {
            'temperature': '°C',
            'humidity': '%',
            'pressure': 'hPa',
            'co2': 'ppm',
            'light': 'lux',
        }
        return units.get(sensor_name, '')


class MultiSensorGenerator:
    """Generate data from multiple heterogeneous sensors."""

    def __init__(self, sensor_configs: List[Dict[str, Any]]):
        """
        Initialize with multiple sensor configurations.

        Args:
            sensor_configs: List of sensor configuration dicts
        """
        self.generators = [
            SensorDataGenerator({'telemetry': config})
            for config in sensor_configs
        ]

    def generate(self) -> Generator[Dict[str, Any], None, None]:
        """Generate from all sensors in round-robin."""
        generators = [gen.generate() for gen in self.generators]

        while True:
            for gen in generators:
                yield next(gen)


def create_scenario(scenario_name: str, duration_seconds: int = 60) -> List[Dict]:
    """
    Create a predefined test scenario.

    Scenarios:
        - normal: Standard operation
        - spike: Temperature spike anomaly
        - drift: Slow sensor drift
        - outage: Sensor goes offline

    Args:
        scenario_name: Name of scenario
        duration_seconds: Duration to generate

    Returns:
        List of sensor readings
    """
    config = {
        'telemetry': {
            'sensors': ['temperature', 'humidity', 'pressure'],
            'sample_rate': 10,
        }
    }

    gen = SensorDataGenerator(config)
    readings = []

    gen_iter = gen.generate()
    end_time = time.time() + duration_seconds

    while time.time() < end_time:
        reading = next(gen_iter)

        # Apply scenario modifications
        if scenario_name == 'spike':
            if 20 < gen.sample_count < 30:
                reading['measurements']['temperature']['value'] *= 2

        elif scenario_name == 'drift':
            reading['measurements']['temperature']['value'] += 0.1 * (gen.sample_count / 10)

        elif scenario_name == 'outage':
            if gen.sample_count > 50:
                reading['measurements']['temperature']['value'] = None

        readings.append(reading)

    return readings


if __name__ == '__main__':
    # Quick test
    config = {
        'telemetry': {
            'sensors': ['temperature', 'humidity'],
            'sample_rate': 1,  # 1 Hz for demo
        }
    }

    gen = SensorDataGenerator(config)
    gen_iter = gen.generate()

    print("Generating 10 samples...")
    for _ in range(10):
        reading = next(gen_iter)
        print(f"  {reading['sensor_id']}: {reading['measurements']}")
