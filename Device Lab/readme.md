# Device Lab

Personal inventory of computing devices for hacking, tinkering, and repurposing projects.

## Quick Stats

| Category | Count | Hackable |
|----------|-------|----------|
| Mobile Devices | 4 | TBD |
| Gaming Devices | 1 | TBD |
| Network Storage | 2 | TBD |
| Desktops | 3 | ★★★★★ |
| Laptops | 1 | TBD |
| Networking | 2 switches + 2 SFP+ | ★★★★☆ |
| Audio | 3 | ★★☆☆☆ |

---

## Mobile Devices

Tablets, phones, and e-readers for kiosk displays, home automation dashboards, or custom ROM experimentation.

| Device | Model | Status | Hackability | Project Ideas |
|--------|-------|--------|-------------|---------------|
| [Samsung Galaxy Tab4 Nook](mobile/samsung-galaxy-tab4-nook/) | SM-T230NU | Project | ★★★★☆ | Home automation dashboard |
| [Amazon Fire HD](mobile/amazon-fire-hd/) | TBD | TBD | TBD | Kids tablet, smart display |
| [Apple iPad Mini](mobile/apple-ipad-mini/) | TBD | TBD | TBD | Media player, HomeKit hub |
| [Apple iPhone 2G](mobile/apple-iphone-2g/) | A1203 | TBD | Jailbreakable | Retro collectible, iPod |

---

## Gaming Devices

Handhelds and consoles for homebrew, emulation, and portable gaming projects.

| Device | Model | Status | Hackability | Project Ideas |
|--------|-------|--------|-------------|---------------|
| [Sony PSVita](gaming/sony-psvita/) | TBD | TBD | TBD | Emulation, homebrew |

---

## Network Storage

NAS devices for home lab, media server, and backup solutions.

| Device | Model | Capacity | Status | Hackability | Project Ideas |
|--------|-------|----------|--------|-------------|---------------|
| [WD My Cloud PR4100](network-storage/wd-mycloud-pr4100/) | PR4100 | TBD | TBD | TBD | Media server, Docker host |
| [WD MyBookLive](network-storage/wd-mybooklive/) | TBD | TBD | TBD | TBD | Backup, archive |

---

## Desktops

Desktop computers for servers, workstations, or parts.

| Device | CPU | RAM | GPU | Status | Current Use |
|--------|-----|-----|-----|--------|-------------|
| [PowerSpec G474](desktops/powerspec-g474/) | i9-14900KF | 96GB DDR5 | RTX 4070 Ti | Active | Primary workstation |
| [Reduced BigRig](desktops/reduced-bigrig/) | FX-9590 | 32GB DDR3 | 2x R9 290 | Project | [DevOps Playground](projects/docker-cluster.md) |
| [Server](desktops/server-fx8350/) | FX-8350 | 32GB DDR3 | HD 5450 | Project | [DevOps Playground](projects/docker-cluster.md) |

---

## Laptops

Laptops and netbooks for portable projects or Linux experimentation.

| Device | Specs Summary | Status | Current Use |
|--------|--------------|--------|-------------|
| Microsoft Surface Book 2 15" | Intel i7, 2-in-1 | TBD | TBD |

*Note: Surface Book 2 also documented in [Camera Collection](../Camera%20Collection/readme.md) under Workstation.*

---

## Networking

Routers, switches, and access points.

| Device | Specs | Qty | Status | Notes |
|--------|-------|-----|--------|-------|
| [Amazon eero 6+](networking/amazon-eero-6-plus/) | WiFi 6 mesh, Thread | 9 | Active | 6 w/house + 3-pack |
| [MokerLink 2.5G Switch](networking/mokerlink-2.5g-switch/) | 8x 2.5GbE + 10G SFP, managed | 2 | Active | VLAN, LACP, QoS |
| ipolex SFP+ to RJ45 | 10GBase-T transceiver | 2 | Active | For switch interconnect |

*See [Network Diagram](../network-diagram.md) for topology and IP assignments.*

---

## Audio Equipment

Home stereo and audio equipment.

| Device | Model | Status | Notes |
|--------|-------|--------|-------|
| [Sonos Port](audio/) | Streaming component | Active | Sonos/stereo integration |
| [Stereo Sound Mixer](audio/) | 4-channel mixer | Active | Richer-R |
| [SOLUPEAK NA2](audio/) | Phono preamp (MM) | Active | Turntable preamp |

---

## Other Devices

Anything that doesn't fit the categories above.

| Device | Type | Status | Notes |
|--------|------|--------|-------|
| *To be documented* | | | |

---

## Hackability Legend

| Rating | Meaning |
|--------|---------|
| ★★★★★ | Fully open, excellent community support |
| ★★★★☆ | Good support, minor limitations |
| ★★★☆☆ | Hackable with effort |
| ★★☆☆☆ | Limited options available |
| ★☆☆☆☆ | Minimal/no hackability |

## Status Legend

| Status | Meaning |
|--------|---------|
| Active | In regular use |
| Shelved | Working, not currently used |
| Project | Designated for hacking/modification |
| Parts | Non-functional, for parts/reference |

---

## Active Projects

| Project | Status | Devices Involved |
|---------|--------|------------------|
| [DevOps Playground Cluster](projects/docker-cluster.md) | In Progress | Reduced BigRig, Server |
| [Home Automation Dashboard](../home-automation/) | Planned | Galaxy Tab4 Nook |

---

## Cross-References

- [Network Diagram](../network-diagram.md) - IP assignments, topology, VLANs
- [Programmable Devices](../Programmable%20Devices/) - Dev boards, MCUs, FPGAs
- [Vintage Computers](../Vintage%20Computers/) - Apple II, TI-99/4A, classic systems
- [Test Equipment](../Test%20Equipment/) - Lab equipment
- [workshop-capabilities.md](../workshop-capabilities.md) - Project ideas and equipment summary

---

## Documentation Protocol

See [DEVICE_LAB_PROTOCOL.md](../.claude/protocols/DEVICE_LAB_PROTOCOL.md) for documentation standards.
