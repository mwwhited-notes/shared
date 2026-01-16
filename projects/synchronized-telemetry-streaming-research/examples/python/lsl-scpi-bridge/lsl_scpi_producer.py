#!/usr/bin/env python3
"""
LSL-SCPI Bridge: Real-time SCPI instrument data streaming to Lab Streaming Layer

This module provides the main orchestrator for:
- Connecting to SCPI instruments via VISA
- Querying measurements at configurable rates
- Publishing data to LSL streams with synchronized timestamps
- Handling reconnection and error recovery
"""

import time
import logging
import signal
import yaml
from typing import Dict, List, Optional
from datetime import datetime
import threading

try:
    from scpi_instrument import ScpiInstrument
    from lsl_outlet import LslOutletFactory
except ImportError:
    # Allow relative imports if running from other directories
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent))
    from scpi_instrument import ScpiInstrument
    from lsl_outlet import LslOutletFactory

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ScpiLslBridge:
    """Bridge between SCPI instruments and LSL network."""

    def __init__(self, config: Dict):
        """
        Initialize the bridge with configuration.

        Args:
            config: Configuration dictionary from YAML
        """
        self.config = config
        self.instrument: Optional[ScpiInstrument] = None
        self.outlets: Dict[str, object] = {}
        self.running = False
        self.thread: Optional[threading.Thread] = None

        # Register signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)

        logger.info("LSL-SCPI Bridge initialized")

    def start(self):
        """Start the bridge in a background thread."""
        if self.running:
            logger.warning("Bridge already running")
            return

        self.running = True
        self.thread = threading.Thread(target=self._run, daemon=False)
        self.thread.start()
        logger.info("Bridge started")

    def stop(self):
        """Stop the bridge gracefully."""
        if not self.running:
            return

        self.running = False
        if self.thread:
            self.thread.join(timeout=5)

        self._disconnect()
        logger.info("Bridge stopped")

    def _signal_handler(self, sig, frame):
        """Handle SIGINT and SIGTERM signals."""
        logger.info(f"Received signal {sig}, shutting down...")
        self.stop()

    def _run(self):
        """Main bridge loop (runs in thread)."""
        reconnect_delay = 5  # seconds
        max_reconnect_attempts = 5
        reconnect_attempt = 0

        while self.running:
            try:
                # Connect to instrument
                if not self.instrument:
                    if reconnect_attempt >= max_reconnect_attempts:
                        logger.error(f"Max reconnection attempts ({max_reconnect_attempts}) reached")
                        break

                    if reconnect_attempt > 0:
                        logger.info(f"Reconnection attempt {reconnect_attempt}/{max_reconnect_attempts}")
                        time.sleep(reconnect_delay)

                    self._connect()
                    reconnect_attempt += 1

                # Create LSL outlets if not exist
                if not self.outlets:
                    self._create_outlets()

                # Measurement acquisition loop
                sample_interval = 1.0 / self.config['measurements']['sample_rate']
                last_sample_time = time.time()

                while self.running and self.instrument:
                    now = time.time()

                    # Poll at configured rate
                    if now - last_sample_time >= sample_interval:
                        self._acquire_and_publish()
                        last_sample_time = now

                    # Small sleep to avoid busy waiting
                    time.sleep(0.001)

                reconnect_attempt = 0  # Reset on successful operation

            except Exception as e:
                logger.error(f"Bridge error: {e}", exc_info=True)
                self._disconnect()
                if self.running:
                    reconnect_attempt += 1

    def _connect(self):
        """Connect to the SCPI instrument."""
        try:
            visa_resource = self.config['instrument']['visa_resource']
            timeout = self.config['instrument'].get('visa_timeout', 5000)

            self.instrument = ScpiInstrument(
                visa_resource=visa_resource,
                timeout=timeout
            )

            # Verify connection
            idn = self.instrument.query("*IDN?")
            logger.info(f"Connected to instrument: {idn}")

            # Optional: Reset instrument
            if self.config['instrument'].get('reset_on_startup', False):
                self.instrument.command("*RST")
                time.sleep(1)
                logger.info("Instrument reset")

        except Exception as e:
            logger.error(f"Failed to connect to instrument: {e}")
            self._disconnect()
            raise

    def _disconnect(self):
        """Disconnect from the SCPI instrument."""
        if self.instrument:
            try:
                self.instrument.close()
            except Exception as e:
                logger.warning(f"Error closing instrument: {e}")
            self.instrument = None

    def _create_outlets(self):
        """Create LSL outlets based on configuration."""
        try:
            factory = LslOutletFactory(self.config)
            self.outlets = factory.create_outlets()

            logger.info(f"Created {len(self.outlets)} LSL outlet(s)")
            for name, outlet in self.outlets.items():
                logger.info(f"  - {name}")

        except Exception as e:
            logger.error(f"Failed to create outlets: {e}")
            raise

    def _acquire_and_publish(self):
        """Acquire a single measurement and publish to all outlets."""
        try:
            measurement_type = self.config['measurements']['type']
            channels = self.config['measurements']['channels']
            averaging_count = self.config['measurements'].get('averaging_count', 1)

            # Acquire sample (with optional averaging)
            sample_data = []
            for _ in range(averaging_count):
                data = self.instrument.measure(measurement_type, channels)
                sample_data.append(data)

            # Average if configured
            if averaging_count > 1:
                import numpy as np
                data = np.mean(sample_data, axis=0).tolist()
            else:
                data = sample_data[0]

            # Get timestamp
            timestamp = self._get_timestamp()

            # Publish to all outlets
            for outlet_name, outlet in self.outlets.items():
                try:
                    outlet.push_sample(data, timestamp)
                except Exception as e:
                    logger.warning(f"Failed to push sample to {outlet_name}: {e}")

        except Exception as e:
            logger.error(f"Measurement acquisition failed: {e}")
            self._disconnect()

    def _get_timestamp(self) -> float:
        """Get current timestamp with optional NTP correction."""
        timestamp = time.time()

        # Optional NTP-based time correction
        if self.config['time_sync'].get('use_ntp', False):
            try:
                import ntplib
                ntp_server = self.config['time_sync'].get('ntp_server', 'pool.ntp.org')
                client = ntplib.NTPClient()
                response = client.request(ntp_server, version=3, timeout=2)
                timestamp = response.tx_time
            except Exception as e:
                logger.debug(f"NTP sync failed: {e}, using system time")

        return timestamp

    def wait(self):
        """Wait for the bridge thread to finish (blocking)."""
        if self.thread:
            self.thread.join()


def main():
    """Main entry point for the LSL-SCPI bridge."""
    import argparse

    parser = argparse.ArgumentParser(description='LSL-SCPI Bridge')
    parser.add_argument('-c', '--config', default='config.yaml',
                        help='Configuration file path')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Enable verbose logging')
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Load configuration
    try:
        with open(args.config) as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        logger.error(f"Configuration file not found: {args.config}")
        return 1
    except yaml.YAMLError as e:
        logger.error(f"Invalid YAML configuration: {e}")
        return 1

    # Run bridge
    try:
        bridge = ScpiLslBridge(config)
        bridge.start()
        logger.info("Bridge running. Press Ctrl+C to stop.")
        bridge.wait()
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        return 1

    return 0


if __name__ == '__main__':
    exit(main())
