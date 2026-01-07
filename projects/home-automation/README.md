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

## Platform Recommendation
**Home Assistant** - Best fit for requirements:
- Free, open source, no subscriptions
- Excellent Z-Wave support via Z-Wave JS
- Multi-protocol support (Zigbee, Matter, Thread)
- 100% local control
- Active community and development

## Remote Access Options (Self-Hosted)
- **WireGuard VPN** - Simplest, fully self-hosted (recommended)
- **Headscale** - Self-hosted Tailscale alternative
- **Reverse proxy + DuckDNS + Let's Encrypt** - Full control, needs port forwarding
- All options: $0/month, fully self-controlled

## Hardware Deployment Options
1. **Pi 3 + Z-Wave hat** - Will work, may be slow with many devices
2. **Dedicated mini PC (N100)** - Best performance (~$100-150 one-time)
3. **Docker on existing server** - Leverage existing hardware
4. **VM (Proxmox/ESXi)** - Flexible, USB passthrough can be tricky

## Z-Wave Interface Options
- USB Z-Stick: Direct compatibility with Z-Wave JS (easiest)
- Pi Z-Wave hats: Need to identify model (RaZberry, Aeotec Z-Pi, etc.)
- Z-Net bridge: Works via ser2net/socat (TCP to serial bridge)

## Next Steps
1. Find and identify Z-Wave USB stick model
2. Check Z-Wave hat models on Pi 3 devices (look for silkscreen/labels)
3. Count total Z-Wave devices to determine hardware requirements
4. Decide on deployment platform (Pi 3 vs dedicated hardware vs Docker)
5. Choose remote access method

## Open Questions
- What model are the Z-Wave hats on the Pi 3s?
- How many Z-Wave devices total in the collection?
- Do you have existing server/NAS for Docker deployment?
- Final hardware choice for Home Assistant deployment?
