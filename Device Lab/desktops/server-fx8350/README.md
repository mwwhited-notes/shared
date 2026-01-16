# Server (AMD FX-8350)

**AMD FX-8350 based home server with multiple storage drives**

## Device Information

| Field | Value |
|-------|-------|
| Build Name | Server |
| Platform | AMD AM3+ |
| Year Built | ~2013-2014 era |
| Date Acquired | TBD |
| Condition | Working |
| Current Use | **Project: [DevOps Playground](../../../projects/devops-playground-cluster/)** |

## Specifications

| Component | Model | Notes |
|-----------|-------|-------|
| CPU | AMD FX-9590	 | 4.7GHz 8-core, 220W TDP |
| Motherboard | Asus M5A97 R2.0 | ATX AM3+ |
| RAM | Corsair Vengeance 32GB | 4x8GB DDR3-1866 CL9 |
| Storage (HDD) | WD Caviar Black 1TB | Primary HDD |
| Storage (HDD) | 2x WD RE4 1TB | Enterprise drives |
| Storage (SSD) | 4x Intel X25-M 80GB | Boot/cache drives |
| GPU | XFX Radeon HD 5450 | 1GB, display output only |
| PSU | Corsair CX500M | 500W 80+ Bronze Semi-modular |
| Networking | Netis 1-Port PCIe Ethernet | Additional NIC |
| Storage Expansion | Vantec UGT-ST622 | 2-Channel SATA PCIe card |

### Storage Summary

| Type | Capacity | Count | Total |
|------|----------|-------|-------|
| HDD | 1TB | 3 | 3TB |
| SSD | 80GB | 4 | 320GB |
| **Total** | | 7 drives | ~3.3TB |

## Power

| Metric | Value |
|--------|-------|
| Estimated Draw | ~350W |
| PSU Capacity | 500W |
| Status | Adequate headroom |

## Hackability

### Current Status

| Aspect | Status |
|--------|--------|
| BIOS Access | Full |
| OS Install | Any |
| Hardware Mods | Full access |
| Drive Expansion | Limited (SATA card added) |

### Hackability Rating: ★★★★★

Standard desktop/server - full control.

### Server Software Options

| Software | Use Case | Notes |
|----------|----------|-------|
| Proxmox VE | Virtualization | Free, good for home lab |
| TrueNAS | NAS/Storage | ZFS support |
| Ubuntu Server | General purpose | Well-supported |
| Unraid | NAS + Docker + VMs | Paid license |
| Windows Server | If needed | Eval or license |

## Project Ideas

- [ ] Proxmox virtualization host
- [ ] TrueNAS storage server
- [ ] Docker host for home services
- [ ] Backup target for other machines
- [ ] Plex media server
- [ ] Home Assistant dedicated host

## Potential Upgrades

| Upgrade | Benefit | Notes |
|---------|---------|-------|
| More RAM | VM capacity | DDR3 still available |
| Larger HDDs | Storage capacity | Replace 1TB with 4TB+ |
| SSD upgrade | Boot speed | Replace X25-M with modern SATA SSD |
| Network card | 10GbE | For faster transfers |

## Documentation

### PCPartPicker
- [Server Build](https://pcpartpicker.com/user/mwwhited/saved/7yrtt6)

## Local Files

*None yet*

## Notes

- Low-power GPU (HD 5450) indicates server/headless use
- Multiple storage drives suggest NAS/storage focus
- Intel X25-M SSDs are old but reliable (MLC NAND)
- WD RE4 are enterprise drives - good for 24/7 operation
- 32GB RAM is decent for VM hosting
- FX-8350 has 8 cores - good for multi-threaded server workloads

### Considerations

- AM3+ platform is end-of-life - no CPU upgrade path
- DDR3 RAM limits future expansion
- May be worth migrating workloads to newer hardware
- Good candidate for parts recycling or dedicated single-purpose server
