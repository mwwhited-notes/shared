#!/usr/bin/env python3
"""
LSL Outlet Creation and Management Module

Provides factories and wrappers for creating Lab Streaming Layer (LSL) outlets
with properly configured channel information and metadata.
"""

import logging
from typing import Dict, List, Any
import time

try:
    from pylsl import StreamInfo, StreamOutlet
except ImportError:
    StreamInfo = None
    StreamOutlet = None

logger = logging.getLogger(__name__)


class LslOutlet:
    """Wrapper around LSL StreamOutlet with convenience methods."""

    def __init__(self, stream_info):
        """
        Initialize LSL outlet.

        Args:
            stream_info: pylsl.StreamInfo object
        """
        if StreamOutlet is None:
            raise ImportError("pylsl not installed. Install with: pip install pylsl")

        self.info = stream_info
        self.outlet = StreamOutlet(stream_info)
        self.name = stream_info.name()
        self.sample_rate = stream_info.nominal_srate()
        self.channel_count = stream_info.channel_count()
        self.sample_count = 0
        self.start_time = time.time()

        logger.info(f"Created LSL outlet: {self.name} "
                    f"({self.channel_count} ch, {self.sample_rate} Hz)")

    def push_sample(self, data: List[float], timestamp: float = None):
        """
        Push a sample to the outlet.

        Args:
            data: Sample data (list of floats, one per channel)
            timestamp: Optional explicit timestamp; uses local time if None
        """
        if len(data) != self.channel_count:
            logger.warning(f"Expected {self.channel_count} channels, got {len(data)}")

        if timestamp is None:
            timestamp = time.time()

        self.outlet.push_sample(data, timestamp)
        self.sample_count += 1

    def push_chunk(self, data: List[List[float]], timestamps: List[float] = None):
        """
        Push multiple samples in a chunk (more efficient).

        Args:
            data: List of samples (each sample is a list of floats)
            timestamps: Optional list of timestamps
        """
        if timestamps is None:
            current_time = time.time()
            timestamps = [current_time + (i / self.sample_rate) for i in range(len(data))]

        for sample, ts in zip(data, timestamps):
            self.push_sample(sample, ts)

    def get_info(self) -> Dict[str, Any]:
        """Get outlet information."""
        return {
            'name': self.name,
            'channel_count': self.channel_count,
            'sample_rate': self.sample_rate,
            'sample_count': self.sample_count,
            'uptime_seconds': time.time() - self.start_time,
        }


class LslOutletFactory:
    """Factory for creating configured LSL outlets."""

    def __init__(self, config: Dict[str, Any]):
        """
        Initialize outlet factory.

        Args:
            config: Configuration dictionary with 'lsl_stream' and 'measurements' sections
        """
        self.config = config
        self.lsl_config = config.get('lsl_stream', {})
        self.measurement_config = config.get('measurements', {})

    def create_outlets(self) -> Dict[str, LslOutlet]:
        """
        Create LSL outlets based on configuration.

        Returns:
            Dictionary of outlet_name -> LslOutlet
        """
        outlets = {}

        try:
            # Create main measurement outlet
            main_outlet = self._create_measurement_outlet()
            if main_outlet:
                outlets['measurement'] = main_outlet

        except Exception as e:
            logger.error(f"Failed to create measurement outlet: {e}")
            raise

        return outlets

    def _create_measurement_outlet(self) -> LslOutlet:
        """Create the primary measurement outlet with channel info."""
        try:
            # Extract configuration
            stream_name = self.lsl_config.get('name', 'SCPI-Instrument')
            stream_type = self.lsl_config.get('type', 'EEG')
            manufacturer = self.lsl_config.get('manufacturer', 'Unknown')
            model = self.lsl_config.get('model', 'Unknown')
            sample_rate = self.measurement_config.get('sample_rate', 100)
            channels = self.measurement_config.get('channels', [1])
            measurement_type = self.measurement_config.get('type', 'voltage')

            # Create StreamInfo
            stream_info = StreamInfo(
                name=stream_name,
                type=stream_type,
                channel_count=len(channels),
                nominal_srate=sample_rate,
                channel_format='float32',
                source_id=f"{manufacturer}_{model}"
            )

            # Add device info to metadata
            root = stream_info.desc()
            device_el = root.append_child("device")
            device_el.append_child_value("manufacturer", manufacturer)
            device_el.append_child_value("model", model)
            device_el.append_child_value("measurement_type", measurement_type)

            # Add channel information
            channels_el = root.append_child("channels")
            for i, ch_num in enumerate(channels):
                channel_el = channels_el.append_child("channel")
                channel_el.append_child_value("label", f"{measurement_type.upper()}_Ch{ch_num}")
                channel_el.append_child_value("unit", self._get_unit(measurement_type))
                channel_el.append_child_value("type", stream_type)
                channel_el.append_child_value("number", str(ch_num))

            # Create and return outlet
            outlet = LslOutlet(stream_info)
            return outlet

        except Exception as e:
            logger.error(f"Failed to create measurement outlet: {e}")
            raise

    @staticmethod
    def _get_unit(measurement_type: str) -> str:
        """Get SI unit for measurement type."""
        units = {
            'voltage': 'V',
            'current': 'A',
            'resistance': 'Ω',
            'frequency': 'Hz',
            'temperature': '°C',
            'power': 'W',
            'impedance': 'Ω',
        }
        return units.get(measurement_type, '')

    def add_marker_outlet(self) -> LslOutlet:
        """
        Create an additional outlet for event markers/annotations.

        Returns:
            LslOutlet for markers (string samples)
        """
        try:
            stream_info = StreamInfo(
                name=self.lsl_config.get('name', 'Markers') + '_Markers',
                type='Markers',
                channel_count=1,
                nominal_srate=0,  # Irregular sampling
                channel_format='string',
                source_id='scpi_markers'
            )

            outlet = LslOutlet(stream_info)
            return outlet

        except Exception as e:
            logger.error(f"Failed to create marker outlet: {e}")
            raise


# Convenience function for quick outlet creation
def create_lsl_outlet_from_config(config_path: str) -> LslOutlet:
    """
    Quick function to create an LSL outlet from a YAML config file.

    Args:
        config_path: Path to YAML configuration file

    Returns:
        LslOutlet object
    """
    import yaml

    with open(config_path) as f:
        config = yaml.safe_load(f)

    factory = LslOutletFactory(config)
    outlets = factory.create_outlets()

    if 'measurement' in outlets:
        return outlets['measurement']
    else:
        raise ValueError("No outlets created")
