# MokerLink 8 Port 2.5G Managed Ethernet Switch

**Managed 2.5 Gigabit switch with 10G SFP uplink for home lab networking**

## Device Information

| Field | Value |
|-------|-------|
| Manufacturer | MokerLink |
| Model | 8 Port 2.5G Managed Ethernet Switch |
| Quantity | 2 |
| Date Acquired | March 17, 2024 |
| Condition | Working |
| Current Use | Network infrastructure |

## Purchase Information

| Field | Value |
|-------|-------|
| Order Date | March 17, 2024 |
| Order # | 111-8911585-7405822 |
| Seller | 7-ChipStar-US (Amazon) |
| Price (each) | $105.99 |
| Total (2 units) | $211.98 |

## Specifications

| Specification | Value |
|--------------|-------|
| RJ45 Ports | 8x 2.5GBase-T |
| SFP Port | 1x 10G SFP+ |
| Backward Compatible | 10/100/1000Mbps |
| Management | Web-based |
| Cooling | Fanless (passive) |
| Construction | Metal enclosure |

## Features

| Feature | Supported |
|---------|-----------|
| VLAN | Yes |
| LACP (Link Aggregation) | Yes |
| QoS | Yes |
| IGMP Snooping | Yes |
| Port Mirroring | TBD |
| Jumbo Frames | TBD |

## Network Configuration

### Switch #1

| Setting | Value |
|---------|-------|
| IP Address | TBD |
| Hostname | TBD |
| Role | TBD |

### Switch #2

| Setting | Value |
|---------|-------|
| IP Address | TBD |
| Hostname | TBD |
| Role | TBD |

## Related Equipment

Purchased together for 10G connectivity:

| Item | Purpose | Price |
|------|---------|-------|
| ipolex SFP+ to RJ45 10Gb Modules (2-pack) | 10G copper transceivers | $76.98 |
| 15V 2A DC Power Supply | Switch power | $9.99 |

### SFP+ Transceiver Details

- Model: ipolex SFP+ to RJ45 10Gb
- Speeds: 1.25/2.5/5/10GBase-T
- Compatibility: Cisco, Ubiquiti, Mikrotik, Netgear, TP-Link
- Cable: CAT.6a/CAT7, up to 30m at 10G

## Topology Ideas

### Option 1: Stacked (10G Uplink Between Switches)

```
Router
   │
   ▼
┌─────────────────┐    10G SFP+    ┌─────────────────┐
│  Switch #1      │◄──────────────►│  Switch #2      │
│  (Main/Servers) │                │  (Workstations) │
└─────────────────┘                └─────────────────┘
   │ 2.5G ports                       │ 2.5G ports
   ▼                                  ▼
Servers, NAS                       PCs, Laptops
```

### Option 2: Separate Segments

```
Router ─────┬─────────────────┐
            │                 │
            ▼                 ▼
     ┌─────────────┐   ┌─────────────┐
     │  Switch #1  │   │  Switch #2  │
     │  (Servers)  │   │  (IoT/Lab)  │
     └─────────────┘   └─────────────┘
```

## VLAN Configuration (Planned)

| VLAN | Name | Purpose | Ports |
|------|------|---------|-------|
| 1 | Default | Management | Port 1 |
| 10 | Servers | DevOps cluster, NAS | Ports 2-4 |
| 20 | Workstations | PCs, laptops | Ports 5-7 |
| 30 | IoT | Smart home, sensors | Port 8 |
| 99 | Isolated | Security testing | Trunk |

## Documentation

### Official
- MokerLink product page (Amazon listing)

### Related
- [Network Diagram](../../../network-diagram.md)

## Local Files

*None yet*

## Notes

- Fanless design is ideal for quiet home lab
- 2.5G provides 2.5x bandwidth over standard Gigabit
- 10G SFP+ allows high-speed interconnect between switches
- VLAN support enables network segmentation (important for MyBookLive isolation)
- Web management interface - document IP once configured
