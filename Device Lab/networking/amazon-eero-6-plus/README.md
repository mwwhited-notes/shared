# Amazon eero 6+ Mesh WiFi System

**Mesh WiFi 6 system providing whole-home coverage**

## Device Information

| Field | Value |
|-------|-------|
| Manufacturer | Amazon (eero) |
| Model | eero 6+ |
| Release | 2022 |
| Quantity | 9 units |
| Condition | Working |
| Current Use | Primary home network |

## Inventory

| Source | Quantity | Date | Cost |
|--------|----------|------|------|
| Included with house | 6 | N/A | $0 |
| Amazon (3-pack) | 3 | 2024-09-19 | $206.69 |
| **Total** | **9** | | |

## Purchase Information (3-pack)

| Field | Value |
|-------|-------|
| Order Date | September 19, 2024 |
| Order # | 113-4246155-1046655 |
| Seller | Amazon.com |
| Price | $194.99 + $11.70 tax = $206.69 |

## Specifications

| Specification | Value |
|--------------|-------|
| WiFi Standard | WiFi 6 (802.11ax) |
| Bands | Dual-band (2.4 GHz + 5 GHz) |
| Speed | Up to 1 Gbps |
| Coverage (per unit) | ~1,500 sq. ft. |
| Coverage (9 units) | ~13,500 sq. ft. theoretical |
| Max Devices | 75+ per unit |
| Ethernet Ports | 2x Gigabit per unit |
| USB | None |
| Thread | Yes (smart home) |
| Zigbee | No (eero 6+ does not have Zigbee) |

## Network Role

| Role | Unit(s) | Notes |
|------|---------|-------|
| Gateway/Router | 1 | Connected to ISP modem |
| Mesh Nodes | 8 | Extend coverage |

## Topology

```
ISP Modem
    │
    ▼
┌─────────────────┐
│  eero Gateway   │──── MokerLink Switch #1
│  (Primary)      │         │
└─────────────────┘         ├── Servers
         │                  ├── NAS
    WiFi Mesh               └── etc.
         │
    ┌────┴────┐
    │         │
┌───────┐ ┌───────┐
│eero #2│ │eero #3│ ... (8 mesh nodes)
└───────┘ └───────┘
    │         │
    ▼         ▼
  Devices   Devices
```

## Features

| Feature | Status |
|---------|--------|
| Mesh networking | Yes |
| Band steering | Automatic |
| App management | eero app (iOS/Android) |
| Parental controls | Yes (eero Secure subscription) |
| Ad blocking | Yes (eero Secure subscription) |
| Thread border router | Yes |
| Guest network | Yes |
| DHCP server | Yes |
| Port forwarding | Yes (via app) |
| VPN passthrough | Yes |

## Hackability

### Current Status

| Aspect | Status |
|--------|--------|
| Custom firmware | Not available |
| SSH access | Not available |
| Advanced settings | Limited (app-based) |

### Hackability Rating: ★★☆☆☆

Closed ecosystem - managed via eero app only. No OpenWrt or custom firmware support.

### Limitations

- No web-based admin interface
- Must use eero app for configuration
- No per-device bandwidth controls
- VLAN support limited/none
- No direct CLI access

### Workarounds

- Use MokerLink managed switches for VLAN segmentation
- Port forwarding available via app
- Can put in bridge mode if using different router

## Network Configuration

| Setting | Value |
|---------|-------|
| Gateway IP | 192.168.0.1 (assumed) |
| DHCP Range | TBD |
| DNS | TBD |
| Network Name | TBD |

## Integration with Managed Switches

Since eero has limited VLAN support, use the MokerLink switches for segmentation:

```
eero Gateway (192.168.0.1)
    │
    ├─── MokerLink Switch #1 (Servers/Storage)
    │         │
    │         ├── VLAN 10: DevOps Cluster
    │         ├── VLAN 20: NAS
    │         └── VLAN 99: Isolated (MyBookLive)
    │
    └─── MokerLink Switch #2 (Workstations/IoT)
              │
              ├── VLAN 1: Workstations
              └── VLAN 30: IoT
```

## Thread / Smart Home

eero 6+ supports Thread protocol for Matter-compatible smart home devices. This could integrate with Home Assistant.

| Protocol | Support |
|----------|---------|
| Thread | Yes (border router) |
| Matter | Yes (via Thread) |
| Zigbee | No |
| Z-Wave | No (separate controller needed) |

## Documentation

### Official
- [eero 6+ Product Page](https://eero.com/shop/eero-6-plus)
- [eero Support](https://support.eero.com/)

## Local Files

*None yet*

## Notes

- 9 units is significant overkill for most homes - could repurpose some
- Thread support useful for Matter smart home devices
- For advanced networking (VLANs, detailed firewall), rely on MokerLink switches
- eero Secure is a paid subscription for advanced features (ad blocking, parental controls)
- Consider bridge mode if you want more control with a different router
