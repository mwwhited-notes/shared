#!/usr/bin/env python3
"""
SCPI Instrument Communication Module

Provides high-level interface for communicating with SCPI-based instruments
over VISA (Virtual Instrument Software Architecture).
"""

import logging
import time
from typing import List, Dict, Any
import pyvisa

logger = logging.getLogger(__name__)


class ScpiInstrument:
    """High-level SCPI instrument communication wrapper."""

    # SCPI command templates for common measurements
    MEASUREMENT_COMMANDS = {
        'voltage': {
            'dc': 'MEAS:VOLT:DC? {channel}',
            'ac': 'MEAS:VOLT:AC? {channel}',
        },
        'current': {
            'dc': 'MEAS:CURR:DC? {channel}',
            'ac': 'MEAS:CURR:AC? {channel}',
        },
        'resistance': 'MEAS:RES? {channel}',
        'frequency': 'MEAS:FREQ? {channel}',
        'temperature': 'MEAS:TEMP? {channel}',
    }

    # SCPI configuration commands
    CONFIG_COMMANDS = {
        'voltage_range': 'CONF:VOLT:DC:RANGE {range}',
        'sample_rate': 'SAMP:RATE {rate}',
        'count': 'SAMP:COUNT {count}',
        'trigger_source': 'TRIG:SOUR {source}',
    }

    def __init__(self, visa_resource: str, timeout: int = 5000):
        """
        Initialize SCPI instrument connection.

        Args:
            visa_resource: VISA resource string (e.g., 'TCPIP::192.168.1.100::INSTR')
            timeout: Communication timeout in milliseconds
        """
        self.visa_resource = visa_resource
        self.timeout = timeout
        self.rm = pyvisa.ResourceManager()
        self.resource = None
        self._command_cache: Dict[str, str] = {}

        # Connect to instrument
        try:
            self.resource = self.rm.open_resource(visa_resource)
            self.resource.timeout = timeout
            logger.info(f"Connected to {visa_resource}")
        except pyvisa.VisaIOError as e:
            logger.error(f"Failed to connect to {visa_resource}: {e}")
            raise

    def query(self, command: str) -> str:
        """
        Send a SCPI query and return the response.

        Args:
            command: SCPI query command (should end with ?)

        Returns:
            Response string from instrument
        """
        try:
            response = self.resource.query(command)
            return response.strip()
        except pyvisa.VisaIOError as e:
            logger.error(f"SCPI query failed: {command}: {e}")
            raise

    def command(self, cmd: str):
        """
        Send a SCPI command (no response expected).

        Args:
            cmd: SCPI command string
        """
        try:
            self.resource.write(cmd)
        except pyvisa.VisaIOError as e:
            logger.error(f"SCPI command failed: {cmd}: {e}")
            raise

    def measure(self, measurement_type: str, channels: List[int]) -> List[float]:
        """
        Take a measurement on specified channels.

        Args:
            measurement_type: Type of measurement (voltage, current, resistance, etc.)
            channels: List of channel numbers to measure

        Returns:
            List of measurement values
        """
        results = []

        for channel in channels:
            try:
                # Get SCPI command for this measurement type
                if measurement_type not in self.MEASUREMENT_COMMANDS:
                    raise ValueError(f"Unknown measurement type: {measurement_type}")

                cmd_template = self.MEASUREMENT_COMMANDS[measurement_type]

                # Handle nested dicts (e.g., voltage.dc)
                if isinstance(cmd_template, dict):
                    # Use DC as default
                    cmd_template = cmd_template.get('dc', list(cmd_template.values())[0])

                cmd = cmd_template.format(channel=channel)

                # Query the measurement
                response = self.query(cmd)

                # Parse numeric response
                try:
                    value = float(response)
                    results.append(value)
                    logger.debug(f"Ch{channel} {measurement_type}: {value}")
                except ValueError:
                    logger.warning(f"Failed to parse response: {response}")
                    results.append(0.0)

            except Exception as e:
                logger.error(f"Measurement failed (Ch{channel}, {measurement_type}): {e}")
                results.append(0.0)

        return results

    def configure_measurement(self, measurement_type: str, **kwargs):
        """
        Configure measurement parameters.

        Args:
            measurement_type: Type of measurement
            **kwargs: Configuration parameters (range, sample_rate, etc.)
        """
        try:
            if measurement_type == 'voltage':
                if 'range' in kwargs:
                    cmd = self.CONFIG_COMMANDS['voltage_range'].format(range=kwargs['range'])
                    self.command(cmd)

            if 'sample_rate' in kwargs:
                cmd = self.CONFIG_COMMANDS['sample_rate'].format(rate=kwargs['sample_rate'])
                self.command(cmd)

            if 'count' in kwargs:
                cmd = self.CONFIG_COMMANDS['count'].format(count=kwargs['count'])
                self.command(cmd)

            logger.info(f"Configured {measurement_type} measurement: {kwargs}")

        except Exception as e:
            logger.error(f"Configuration failed: {e}")
            raise

    def reset(self):
        """Reset instrument to default state."""
        try:
            self.command('*RST')
            self.command('*CLS')
            logger.info("Instrument reset")
        except Exception as e:
            logger.error(f"Reset failed: {e}")
            raise

    def clear_status(self):
        """Clear instrument status (errors, events)."""
        try:
            self.command('*CLS')
        except Exception as e:
            logger.error(f"Clear status failed: {e}")

    def get_error(self) -> str:
        """
        Query instrument error queue.

        Returns:
            Error message string
        """
        try:
            error = self.query('SYST:ERR?')
            return error
        except Exception as e:
            logger.error(f"Error query failed: {e}")
            return ""

    def get_status(self) -> Dict[str, Any]:
        """
        Get overall instrument status.

        Returns:
            Status dictionary
        """
        status = {}
        try:
            status['identification'] = self.query('*IDN?')
            status['options'] = self.query('*OPT?')

            # Error status
            error_msg = self.get_error()
            status['error'] = error_msg

            # Standard Event Status
            status['event_status'] = self.query('*ESR?')

        except Exception as e:
            logger.error(f"Status query failed: {e}")

        return status

    def fetch_data(self, count: int = 100) -> List[float]:
        """
        Fetch previously acquired data from instrument memory.

        Args:
            count: Number of samples to fetch

        Returns:
            List of data values
        """
        try:
            cmd = f'FETC? {count}'
            response = self.query(cmd)
            # Parse comma-separated values
            values = [float(v.strip()) for v in response.split(',')]
            return values
        except Exception as e:
            logger.error(f"Data fetch failed: {e}")
            return []

    def set_trigger(self, source: str = 'BUS', delay: float = 0):
        """
        Configure instrument triggering.

        Args:
            source: Trigger source (BUS, EXT, INT, etc.)
            delay: Trigger delay in seconds
        """
        try:
            self.command(f'TRIG:SOUR {source}')
            if delay > 0:
                self.command(f'TRIG:DEL {delay}')
            logger.info(f"Trigger configured: source={source}, delay={delay}s")
        except Exception as e:
            logger.error(f"Trigger configuration failed: {e}")

    def arm_trigger(self):
        """Arm the instrument for triggered operation."""
        try:
            self.command('*TRG')
        except Exception as e:
            logger.error(f"Arm trigger failed: {e}")

    def close(self):
        """Close the VISA connection."""
        try:
            if self.resource:
                self.resource.close()
            logger.info("VISA connection closed")
        except Exception as e:
            logger.error(f"Error closing connection: {e}")

    def __enter__(self):
        """Context manager support."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager cleanup."""
        self.close()
        return False

    def __del__(self):
        """Destructor ensures connection is closed."""
        self.close()
