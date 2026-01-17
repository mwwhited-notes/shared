# Device Lab

Complete inventory of computing devices for hacking, tinkering, and repurposing projects including desktops, laptops, mobile devices, gaming gear, VR/AR hardware, and network infrastructure.

**Quick Reference:** 40+ devices across 8 categories | [Documentation Protocol](../.claude/protocols/DEVICE_LAB_PROTOCOL.md) | [Network Diagram](../network-diagram.md)

## Table of Contents

- [Quick Stats](#quick-stats)
- [Mobile Devices](#mobile-devices)
- [Gaming Devices](#gaming-devices)
- [VR/AR & Motion Sensing](#vrar--motion-sensing)
- [Network Storage](#network-storage)
- [Desktops](#desktops)
- [Laptops](#laptops)
- [Networking](#networking)
- [Audio](#audio)
- [Single Board Computers](#single-board-computers)
- [Other Devices](#other-devices)
- [Projects](#projects)
- [Cross-References](#cross-references)

---

## Quick Stats

| Category | Count | Hackable |
|----------|-------|----------|
| Mobile Devices | 4 | TBD |
| Gaming Devices | 1 | TBD |
| VR/AR & Motion Sensing | 3 | ★★★★☆ |
| Network Storage | 2 | TBD |
| Desktops | 5 (+ 2 Mac Mini) | ★★★★★ |
| Laptops | 4 | TBD |
| Networking | 5 switches + 9 eero + 2 SFP+ | ★★★★☆ |
| Audio | 3 | ★★☆☆☆ |
| SBCs | 8 (legacy cluster) | ★★★★★ |
| Other | 3+ | TBD |

---

## Mobile Devices

Tablets, phones, and e-readers for kiosk displays, home automation dashboards, or custom ROM experimentation.

| Device | Model | Status | Hackability | Git Hash | Project Ideas |
|--------|-------|--------|-------------|----------|---------------|
| [Samsung Galaxy Tab4 Nook](mobile/samsung-galaxy-tab4-nook/) | SM-T230NU | Project | ★★★★☆ | xxxxxxx | Home automation dashboard |
| [Amazon Fire HD](mobile/amazon-fire-hd/) | TBD | TBD | TBD | xxxxxxx | Kids tablet, smart display |
| [Apple iPad Mini](mobile/apple-ipad-mini/) | TBD | TBD | TBD | xxxxxxx | Media player, HomeKit hub |
| [Apple iPhone 2G](mobile/apple-iphone-2g/) | A1203 | TBD | Jailbreakable | xxxxxxx | Retro collectible, iPod |

---

## Gaming Devices

Handhelds and consoles for homebrew, emulation, and portable gaming projects.

| Device | Model | Status | Hackability | Git Hash | Project Ideas |
|--------|-------|--------|-------------|----------|---------------|
| [Sony PSVita](gaming/sony-psvita/) | TBD | TBD | TBD | xxxxxxx | Emulation, homebrew |

---

## VR/AR & Motion Sensing

Virtual/augmented reality headsets and depth-sensing cameras for 3D scanning, gesture control, and spatial computing projects.

| Device | Model | Status | Hackability | Git Hash | Project Ideas |
|--------|-------|--------|-------------|----------|---------------|
| [Microsoft HoloLens](vr-ar/microsoft-hololens/) | HoloLens v1 Developer Edition | TBD | ★★★★☆ | xxxxxxx | AR development, spatial mapping, gesture control |
| [Xbox 360 Kinect](sensors/xbox360-kinect/) | Kinect v1 with PC adapter | TBD | ★★★★★ | xxxxxxx | 3D scanning, motion capture, robotics |
| [Xbox One Kinect](sensors/xboxone-kinect/) | Kinect v2 (PC version) | TBD | ★★★★☆ | xxxxxxx | High-res depth sensing, skeletal tracking |

---

## Network Storage

NAS devices for home lab, media server, and backup solutions.

| Device | Model | Capacity | Status | Hackability | Git Hash | Project Ideas |
|--------|-------|----------|--------|-------------|----------|---------------|
| [WD My Cloud PR4100](network-storage/wd-mycloud-pr4100/) | PR4100 + WD Red Plus 12TB | 12TB | Active | TBD | xxxxxxx | Media server, Docker host |
| [WD MyBookLive](network-storage/wd-mybooklive/) | TBD | TBD | TBD | TBD | xxxxxxx | Backup, archive |

---

## Desktops

Desktop computers for servers, workstations, or parts.

| Device | CPU | RAM | GPU | Status | Git Hash | Current Use |
|--------|-----|-----|-----|--------|----------|-------------|
| [PowerSpec G474](desktops/powerspec-g474/) | i9-14900KF | 160GB DDR5 | RTX 4070 Ti | Active | xxxxxxx | Primary workstation |
| [Reduced BigRig](desktops/reduced-bigrig/) | FX-9590 | 32GB DDR3 | 2x R9 290 | Project | xxxxxxx | [DevOps Playground](projects/docker-cluster.md) |
| [Server](desktops/server-fx8350/) | FX-8350 | 32GB DDR3 | HD 5450 | Project | xxxxxxx | [DevOps Playground](projects/docker-cluster.md) |
| Mac Mini 2014 | Intel | 8GB | Integrated | TBD | xxxxxxx | SSD upgraded |
| Mac Mini 2014 | Intel | 4GB | Integrated | TBD | xxxxxxx | SSD upgraded |

---

## Laptops

Laptops and netbooks for portable projects or Linux experimentation.

| Device | Specs Summary | Status | Git Hash | Current Use |
|--------|--------------|--------|----------|-------------|
| Microsoft Surface Book 2 15" | Intel i7, 2-in-1 | TBD | xxxxxxx | TBD |
| MacBook Pro A1502 | Intel, 13" Retina | TBD | xxxxxxx | TBD |
| MacBook (unknown model) | Intel | TBD | xxxxxxx | TBD |
| Toshiba Satellite R10 | Convertible tablet PC | TBD | xxxxxxx | TBD |

*Note: Surface Book 2 also documented in [Camera Collection](../Camera%20Collection/readme.md) under Workstation.*

---

## Networking

Routers, switches, and access points.

| Device | Specs | Qty | Status | Git Hash | Notes |
|--------|-------|-----|--------|----------|-------|
| [Amazon eero 6+](networking/amazon-eero-6-plus/) | WiFi 6 mesh, Thread | 9 | Active | xxxxxxx | 6 w/house + 3-pack |
| [MokerLink 2.5G Switch](networking/mokerlink-2.5g-switch/) | 8x 2.5GbE + 10G SFP, managed | 2 | Active | xxxxxxx | VLAN, LACP, QoS |
| ipolex SFP+ to RJ45 | 10GBase-T transceiver | 2 | Active | xxxxxxx | For switch interconnect |
| TP-Link TL-SG1005D | 5-port Gigabit | 1 | TBD | xxxxxxx | Unmanaged |
| TP-Link TL-SG1008D | 8-port Gigabit | 1 | TBD | xxxxxxx | Unmanaged |
| D-Link DGS-1100-08 | 8-port Gigabit | 1 | TBD | xxxxxxx | Smart managed, 2019-01-03, $33.39 |
| TP-Link AC750 TL-WR902AC | Wireless portable travel router | 1 | Shelved | xxxxxxx | 2020-01-30, $34.97 |
| WiFi Card AC 1730Mbps | 802.11ac module | 1 | TBD | xxxxxxx | 2019-05-30, $38.99 |

*See [Network Diagram](../network-diagram.md) for topology and IP assignments.*

---

## Audio Equipment

Home stereo and audio equipment.

| Device | Model | Status | Git Hash | Notes |
|--------|-------|--------|----------|-------|
| [Sonos Port](audio/) | Streaming component | Active | xxxxxxx | Sonos/stereo integration |
| [Stereo Sound Mixer](audio/) | 4-channel mixer | Active | xxxxxxx | Richer-R |
| [SOLUPEAK NA2](audio/) | Phono preamp (MM) | Active | xxxxxxx | Turntable preamp |

---

## Other Devices

Printers, media devices, and anything that doesn't fit the categories above.

| Device | Type | Status | Git Hash | Notes |
|--------|------|--------|----------|-------|
| [Brother HL-3170CDW](other/brother-hl-3170cdw/) | Color Laser Printer | Active | xxxxxxx | 192.168.0.48, Craft Room |
| HD HomeRun Extend | TV Tuner/Streamer | TBD | xxxxxxx | Network TV tuner |
| JCHICI USB 2.0 Extender | USB over Ethernet | Active | xxxxxxx | 50m, 4 ports, $29.99 Jan 2024 |
| InnoView Portable Monitor | 14" 4K Touch, USB-C | Active | xxxxxxx | $299.99 Jan 2024 |
| XGODY X1 Projector | 1080p, Android, WiFi/BT | Active | xxxxxxx | $179.00 Aug 2023 |
| Sony BDPS1700 Blu-Ray Player | Streaming player (Refurbished) | Shelved | xxxxxxx | 2018-01-15, $39.99 |
| Wyze Cam Pan 1080p | Smart home camera (×2) | Active | xxxxxxx | 2018-10-19 & 2018-10-25, $37.98 each |
| Esky Barcode Scanner | USB Laser Scanner with Stand | Shelved | xxxxxxx | 2018-01-22, $16.99 |
| Gibbon Mounts Monitor Arm | Gas spring desk mount VESA 75/100 | Active | xxxxxxx | 2020-12-29, $59.99 |
| TOTU 13-in-1 USB-C Hub | Docking with Ethernet, HDMI, PD | Active | xxxxxxx | 2020-03-11, $79.99 |

### SBC Cluster

ARM-based cluster for Docker/Kubernetes learning. See [SBC Cluster project](../../projects/sbc-cluster/) for details.

Has custom power controller/network device (code in [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery)).

| Device | Qty | Git Hash | Notes |
|--------|-----|----------|-------|
| BeagleBone Black | 4 | xxxxxxx | ARM Cortex-A8 |
| Raspberry Pi 2 | 2 | xxxxxxx | |
| Raspberry Pi Model A | 2 | xxxxxxx | Composite video output |

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

*Index Version: 1.0*
*Last Updated: 2026-01-16*
*Total Devices: 40+ across 8 categories*
*Scope: Laptops, desktops, mobile devices, gaming handhelds, VR/AR, network storage, networking infrastructure, and specialty computing hardware for tinkering and repurposing*

See [DEVICE_LAB_PROTOCOL.md](../.claude/protocols/DEVICE_LAB_PROTOCOL.md) for documentation standards.
