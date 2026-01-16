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

## VR/AR & Motion Sensing

Virtual/augmented reality headsets and depth-sensing cameras for 3D scanning, gesture control, and spatial computing projects.

| Device | Model | Status | Hackability | Project Ideas |
|--------|-------|--------|-------------|---------------|
| [Microsoft HoloLens](vr-ar/microsoft-hololens/) | HoloLens v1 Developer Edition | TBD | ★★★★☆ | AR development, spatial mapping, gesture control |
| [Xbox 360 Kinect](sensors/xbox360-kinect/) | Kinect v1 with PC adapter | TBD | ★★★★★ | 3D scanning, motion capture, robotics |
| [Xbox One Kinect](sensors/xboxone-kinect/) | Kinect v2 (PC version) | TBD | ★★★★☆ | High-res depth sensing, skeletal tracking |

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
| [PowerSpec G474](desktops/powerspec-g474/) | i9-14900KF | 160GB DDR5 | RTX 4070 Ti | Active | Primary workstation |
| [Reduced BigRig](desktops/reduced-bigrig/) | FX-9590 | 32GB DDR3 | 2x R9 290 | Project | [DevOps Playground](projects/docker-cluster.md) |
| [Server](desktops/server-fx8350/) | FX-8350 | 32GB DDR3 | HD 5450 | Project | [DevOps Playground](projects/docker-cluster.md) |
| Mac Mini 2014 | Intel | 8GB | Integrated | TBD | SSD upgraded |
| Mac Mini 2014 | Intel | 4GB | Integrated | TBD | SSD upgraded |

---

## Laptops

Laptops and netbooks for portable projects or Linux experimentation.

| Device | Specs Summary | Status | Current Use |
|--------|--------------|--------|-------------|
| Microsoft Surface Book 2 15" | Intel i7, 2-in-1 | TBD | TBD |
| MacBook Pro A1502 | Intel, 13" Retina | TBD | TBD |
| MacBook (unknown model) | Intel | TBD | TBD |
| Toshiba Satellite R10 | Convertible tablet PC | TBD | TBD |

*Note: Surface Book 2 also documented in [Camera Collection](../Camera%20Collection/readme.md) under Workstation.*

---

## Networking

Routers, switches, and access points.

| Device | Specs | Qty | Status | Notes |
|--------|-------|-----|--------|-------|
| [Amazon eero 6+](networking/amazon-eero-6-plus/) | WiFi 6 mesh, Thread | 9 | Active | 6 w/house + 3-pack |
| [MokerLink 2.5G Switch](networking/mokerlink-2.5g-switch/) | 8x 2.5GbE + 10G SFP, managed | 2 | Active | VLAN, LACP, QoS |
| ipolex SFP+ to RJ45 | 10GBase-T transceiver | 2 | Active | For switch interconnect |
| TP-Link TL-SG1005D | 5-port Gigabit | 1 | TBD | Unmanaged |
| TP-Link TL-SG1008D | 8-port Gigabit | 1 | TBD | Unmanaged |
| D-Link DGS-1100-08 | 8-port Gigabit | 1 | TBD | Smart managed |

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

Printers, media devices, and anything that doesn't fit the categories above.

| Device | Type | Status | Notes |
|--------|------|--------|-------|
| [Brother HL-3170CDW](other/brother-hl-3170cdw/) | Color Laser Printer | Active | 192.168.0.48, Craft Room |
| HD HomeRun Extend | TV Tuner/Streamer | TBD | Network TV tuner |
| JCHICI USB 2.0 Extender | USB over Ethernet | Active | 50m, 4 ports, $29.99 Jan 2024 |
| InnoView Portable Monitor | 14" 4K Touch, USB-C | Active | $299.99 Jan 2024 |
| XGODY X1 Projector | 1080p, Android, WiFi/BT | Active | $179.00 Aug 2023 |

### SBC Cluster

ARM-based cluster for Docker/Kubernetes learning. See [SBC Cluster project](../../projects/sbc-cluster/) for details.

Has custom power controller/network device (code in [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery)).

| Device | Qty | Notes |
|--------|-----|-------|
| BeagleBone Black | 4 | ARM Cortex-A8 |
| Raspberry Pi 2 | 2 | |
| Raspberry Pi Model A | 2 | Composite video output |

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
