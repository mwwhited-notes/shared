# Home Automation Project

## Previous Setup
- **Platform**: HomeSeer HS4
- **Controller Hardware**: Raspberry Pi (upgraded to Pi 3)
- **Z-Wave Interface**: Z-Net bridge (HomeSeer's ethernet-based Z-Wave adapter)

## Available Hardware
- Z-Wave USB Z-Stick (location TBD - needs to be found)
- Two Raspberry Pi 3 devices with Z-Wave hats/interfaces (confirmed Pi 3 - have built-in WiFi, upgraded from Pi 2)
- Option: Dedicated computer or Docker host

## Current Status
- Moved to new home - need full network reconfiguration
- Evaluating platform options (setup was configured years ago)

## Notes
- Z-Net bridge should be reusable with other platforms (presents as standard Z-Wave controller over IP)

## Requirements
- **Z-Wave**: Primary focus - many existing devices to migrate
- **Multi-protocol**: Want support for additional protocols (Zigbee, Matter, Thread, etc.)
- **On-premises**: Local control preferred, not cloud-dependent
- **Remote access**: Required, but NO cloud services - must be self-hosted
- **No subscriptions**: Zero monthly fees - full ownership

## Open Questions
- Specific Z-Wave devices in the collection?
- Hardware to run the platform (keep Pi 3 or upgrade)?
