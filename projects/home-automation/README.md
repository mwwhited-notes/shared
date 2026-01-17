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

## Equipment Used

### Display Devices
- **[Galaxy Tab4 Nook](../../.personal/incoming/device-lab.md)** - Primary dashboard display (LineageOS + kiosk mode)
- **[Amazon Fire HD](../../.personal/incoming/device-lab.md)** - Secondary display (Google Play + kiosk)

### Controllers & Infrastructure
- **[Raspberry Pi 3](../../.personal/incoming/device-lab.md)** (×2) - With Z-Wave hats/interfaces
- Z-Wave USB Z-Stick - Direct USB Z-Wave controller
- Z-Net bridge - Ethernet-based Z-Wave adapter (HomeSeer)
- **[WD My Cloud PR4100](../../.personal/incoming/device-lab.md)** - Docker host option for Home Assistant
- **[DevOps Playground Cluster](../devops-playground-cluster/)** - Alternative deployment platform

## Next Steps
1. Find and identify Z-Wave USB stick model
2. Check Z-Wave hat models on Pi 3 devices (look for silkscreen/labels)
3. Count total Z-Wave devices to determine hardware requirements
4. Decide on deployment platform (Pi 3 vs dedicated hardware vs Docker)
5. Choose remote access method
6. Flash LineageOS on Galaxy Tab4 Nook for dashboard
7. Set up Fire HD with Google Play for secondary display

## Open Questions
- What model are the Z-Wave hats on the Pi 3s?
- How many Z-Wave devices total in the collection?
- Deploy on PR4100 NAS or DevOps Playground cluster?
- Final hardware choice for Home Assistant deployment?

## Cross-References

- [Device Lab/mobile/](../../Device%20Lab/mobile/) - Dashboard tablet inventory
- [DevOps Playground Cluster](../devops-playground-cluster/) - Alternative deployment platform
- [Device Lab/network-storage/](../../Device%20Lab/network-storage/) - NAS/Docker host options
- [SBC Cluster](../sbc-cluster/) - ARM-based cluster alternative for always-on services
- [Self-Hosted Git Server](../self-hosted-git-server/) - Related infrastructure project on PR4100
- [Radex One Protocol](../radex-one-protocol-reverse-engineering/) - Potential sensor integration
- [project-ideas.md](../project-ideas.md) - Original project concept

---

*Last updated: 2026-01-07*
