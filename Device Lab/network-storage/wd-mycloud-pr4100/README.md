# WD My Cloud PR4100

**4-bay prosumer NAS with Intel CPU, suitable for Docker and advanced applications**

## Device Information

| Field | Value |
|-------|-------|
| Manufacturer | Western Digital |
| Model | My Cloud PR4100 |
| Model Number | WDBNFA0000NBK |
| Generation/Year | 2016 |
| Date Acquired | TBD |
| Condition | TBD |
| Current Use | TBD |

## Specifications

| Specification | Value |
|--------------|-------|
| CPU | Intel Pentium N3710 (4 cores, 1.6-2.56 GHz) |
| RAM | 4 GB DDR3L |
| Drive Bays | 4x 3.5" SATA (hot-swap) |
| Max Capacity | 64 TB (4x 16TB) |
| RAID Modes | JBOD, RAID 0, 1, 5, 10, Spanning |
| Network | 2x Gigabit Ethernet (link aggregation) |
| USB | 2x USB 3.0 |
| Display | LCD status panel |
| Power | Internal PSU |
| OS | My Cloud OS (Linux-based) |

## Hackability

### Current Status

| Aspect | Status |
|--------|--------|
| SSH Access | Available (enable in settings) |
| Root Access | Available |
| Docker | Supported (official) |
| Third-party Apps | Available |

### Hackability Rating: ★★★★☆

Good hackability - Intel x86 CPU, SSH access, Docker support. Some WD restrictions but workarounds exist.

### Available Modifications

| Modification | Availability | Notes |
|-------------|--------------|-------|
| SSH Root | Built-in | Enable in dashboard |
| Docker | Official | My Cloud OS 5+ |
| Plex Media Server | Official app | Good transcoding with Intel CPU |
| Third-party apps | Community | Various packages available |
| Debian chroot | Community | Full Linux environment |

### My Cloud OS Versions

| Version | Features |
|---------|----------|
| OS 3.x | Legacy, more open |
| OS 5.x | Current, Docker support, some restrictions |

### Hackability Resources

- [WD Community Forums](https://community.wd.com/)
- [/r/wdmycloud](https://reddit.com/r/wdmycloud)
- [My Cloud PR4100 on GitHub](https://github.com/search?q=pr4100)

## Project Ideas

- [ ] Plex media server (Intel Quick Sync for transcoding)
- [ ] Docker host for home services
- [ ] Time Machine backup target
- [ ] Surveillance station (IP camera recording)
- [ ] Home Assistant data storage
- [ ] Rsync backup target

## Docker Containers to Consider

| Container | Purpose |
|-----------|---------|
| Plex | Media server |
| Portainer | Docker management |
| Nextcloud | Personal cloud |
| Home Assistant | Home automation |
| Pi-hole | DNS ad blocking |
| Duplicati | Backup software |

## Documentation

### Official
- [WD PR4100 Product Page](https://www.westerndigital.com/products/network-attached-storage/wd-my-cloud-pro-series-pr4100)
- [WD PR4100 User Manual](https://support-en.wd.com/)
- [WD Knowledge Base](https://support-en.wd.com/)

### Community
- [WD Community](https://community.wd.com/)
- [/r/wdmycloud](https://reddit.com/r/wdmycloud)
- [/r/homelab](https://reddit.com/r/homelab)

## Local Files

*None yet - download user manual*

## Notes

### Security Considerations

- **Critical**: Older My Cloud devices had serious vulnerabilities
- Keep firmware updated
- Do NOT expose directly to internet
- Use VPN for remote access

### Performance Notes

- Intel Pentium N3710 supports Quick Sync - good for Plex transcoding
- 4 GB RAM is adequate but not expandable
- Dual Gigabit with link aggregation for better throughput

### Current Configuration

- Installed drives: TBD
- RAID configuration: TBD
- Current firmware: TBD
- Services running: TBD
