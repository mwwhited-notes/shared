# SBC Cluster - Raspberry Pi & BeagleBone Black

**Status**: Planning

Low-power ARM cluster for learning container orchestration, distributed computing, and network device filtering.

## Overview

| Aspect | Details |
|--------|---------|
| Project Type | Home Lab / Learning |
| Status | Planning |
| Start Date | TBD |
| Purpose | **ARM cluster for Docker/Kubernetes learning and device filtering experiments** |
| Architecture | **Lightweight learning environment** - Low power, always-on capable |

**Note:** This is the ARM/SBC cluster. See [DevOps Playground Cluster](../devops-playground-cluster/) for the x86 high-performance cluster (FX-9590/FX-8350).

## Hardware Inventory

| Device | Qty | CPU | RAM | Notes |
|--------|-----|-----|-----|-------|
| BeagleBone Black | 4 | ARM Cortex-A8 (1 GHz) | 512MB | GPIO, PRU cores |
| Raspberry Pi 2 Model B | 2 | ARM Cortex-A7 (900 MHz, quad-core) | 1GB | |
| Raspberry Pi Model A | 2 | ARM11 (700 MHz) | 256MB/512MB | Composite video output |

### Combined Resources

| Resource | Total |
|----------|-------|
| CPU Cores | ~12 cores (4×1 + 2×4 + 2×1) |
| RAM | ~4.5GB |
| Power Draw | ~20-30W total (estimated) |
| Network | Ethernet + USB adapters |

### Supporting Hardware

**Power Controller & Network Device:**
- Custom power controller for cluster management
- Code available in [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery)
- Allows remote power cycling of individual nodes

## Project Goals

### Primary Learning Objectives

1. **Container Orchestration on ARM**
   - Docker Swarm on ARM architecture
   - k3s (lightweight Kubernetes) for resource-constrained devices
   - Compare with x86 DevOps Playground Cluster

2. **Device Filtering & Network Experiments**
   - Docker container network isolation
   - Device filtering and routing
   - Network bridge configurations
   - VLAN experiments

3. **Low-Power Always-On Services**
   - Pi-hole (DNS ad blocking)
   - Lightweight monitoring
   - Network services that don't need high performance

4. **Distributed Computing**
   - Multi-node processing
   - Load balancing across ARM nodes
   - Cross-platform container compatibility (ARM vs x86)

## Architecture vs. DevOps Playground Cluster

| Aspect | SBC Cluster (ARM) | DevOps Playground (x86) |
|--------|-------------------|-------------------------|
| **Hardware** | 8× ARM SBCs | 2× FX-series desktops |
| **Power** | ~20-30W total | ~350-900W total |
| **Runtime** | Always-on capable | Run when needed |
| **Purpose** | Low-power services, ARM learning | High-performance experiments |
| **Use Case** | Network filtering, lightweight services | GPU compute, heavy workloads |

**Complementary roles:**
- **SBC Cluster:** Always-on infrastructure services, network experiments, ARM container testing
- **DevOps Playground:** Heavy compute, GPU workloads, x86 orchestration learning, Slurm/HPC

## Planned Experiments

### Network & Device Filtering

| Experiment | Description | Learning Goal |
|------------|-------------|---------------|
| Docker device filtering | Container access to USB/serial devices | Device isolation, hardware access |
| Network bridge modes | Bridge, overlay, macvlan comparison | Container networking |
| Multi-node networking | Cross-node container communication | Distributed networking |
| VLAN segregation | Network isolation experiments | Network security |

### Container Orchestration

| Technology | Use Case | Priority |
|------------|----------|----------|
| Docker Compose | Multi-container apps on single node | High |
| Docker Swarm | Native clustering across 8 nodes | High |
| k3s (lightweight K8s) | Kubernetes on low-resource ARM | Medium |
| Portainer | Web UI for cluster management | High |

### Services

| Service | Purpose | Node Assignment |
|---------|---------|-----------------|
| Pi-hole | DNS ad blocking | Pi 2 (always-on) |
| Portainer | Cluster management UI | Pi 2 |
| Registry | Local ARM container registry | BeagleBone Black |
| Nginx | Reverse proxy | BeagleBone Black |
| Test workloads | Learning deployments | All nodes |

## Setup Tasks

### Phase 1: Hardware Prep
- [ ] Inventory and test all 8 boards
- [ ] Verify power controller functionality
- [ ] Plan network topology (switch, cabling)
- [ ] Determine node roles (manager vs worker)

### Phase 2: OS Installation
- [ ] Choose ARM Linux distribution (Armbian, Raspberry Pi OS, Debian)
- [ ] Flash SD cards for all nodes
- [ ] Configure static IPs
- [ ] Set up SSH access
- [ ] Configure hostnames

### Phase 3: Cluster Setup
- [ ] Install Docker on all nodes
- [ ] Choose orchestration platform (Swarm vs k3s)
- [ ] Initialize cluster manager
- [ ] Join worker nodes
- [ ] Test cross-node communication

### Phase 4: Services Deployment
- [ ] Deploy Portainer for management
- [ ] Set up local container registry
- [ ] Deploy Pi-hole on dedicated node
- [ ] Configure reverse proxy
- [ ] Test device filtering experiments

## Technical Considerations

### Operating System Options

| Option | Pros | Cons | Decision |
|--------|------|------|----------|
| **Raspberry Pi OS** | Official, well-supported | Pi-only, not BeagleBone | Maybe for Pi nodes |
| **Armbian** | Supports both BBB and Pi | Lighter support | **Recommended** |
| **Debian** | Universal, stable | More manual configuration | Alternative |
| **DietPi** | Extremely lightweight | Smaller community | For low-RAM nodes |

### Orchestration Choice

| Platform | Pros | Cons | Recommendation |
|----------|------|------|----------------|
| **Docker Swarm** | Simple, native Docker, low overhead | Less features than K8s | **Start here** |
| **k3s** | Full Kubernetes, industry-standard | More complex, higher resource use | After Swarm |
| **k0s** | Alternative lightweight K8s | Newer, less documentation | Optional exploration |

### Networking Approach

**Cluster Network:**
```
Router/Switch
  ├── BeagleBone Black #1 (Manager)
  ├── BeagleBone Black #2 (Worker)
  ├── BeagleBone Black #3 (Worker)
  ├── BeagleBone Black #4 (Worker)
  ├── Raspberry Pi 2 #1 (Worker - Pi-hole)
  ├── Raspberry Pi 2 #2 (Worker)
  ├── Raspberry Pi Model A #1 (Worker - low priority)
  └── Raspberry Pi Model A #2 (Worker - low priority)
```

**Recommended static IP range:** `10.0.88.20` - `10.0.88.27` (see [network-diagram.md](../../network-diagram.md))

### Storage Strategy

| Storage Type | Use Case | Implementation |
|--------------|----------|----------------|
| SD cards | OS and Docker images | Local to each node |
| USB drives | Persistent data (optional) | Attach to specific nodes |
| NFS share | Shared storage across cluster | From PR4100 NAS |

## Device Filtering Experiments

### Use Cases

1. **USB Device Access**
   - Pass USB serial devices to specific containers
   - Test device permissions and isolation
   - Docker `--device` flag experiments

2. **GPIO Access**
   - BeagleBone Black PRU cores
   - Container access to `/dev/gpiochip*`
   - Hardware control from containerized apps

3. **Network Device Filtering**
   - Virtual network interfaces
   - Container-specific network access
   - Firewall and routing rules

### Example Experiment: Serial Device

```bash
# Run container with access to USB serial device
docker run -d \
  --device=/dev/ttyUSB0 \
  --name serial-test \
  alpine:latest

# Test from inside container
docker exec -it serial-test ls -l /dev/ttyUSB0
```

## Power Management

### Power Controller Integration

- Custom power controller built with Arduino/ESP (code in EmbeddedBakery)
- Remote power on/off for individual nodes
- Useful for:
  - Selective node shutdown (power saving)
  - Remote restart of hung nodes
  - Testing node failure scenarios

### Always-On vs. On-Demand

| Node Type | Power Strategy | Reason |
|-----------|---------------|---------|
| Pi 2 #1 (Pi-hole) | Always-on | Critical DNS service |
| Manager node | Always-on | Cluster coordination |
| Worker nodes | On-demand | Power saving, experimental |
| Model A nodes | On-demand | Lowest priority, low RAM |

## Comparison with DevOps Playground Cluster

### When to Use SBC Cluster

- **ARM container development** - Test ARM vs x86 compatibility
- **Low-power experiments** - Services that can run 24/7
- **Network learning** - Device filtering, routing, VLANs
- **Distributed algorithms** - Multi-node processing on constrained resources
- **IoT gateway simulations** - Edge computing scenarios

### When to Use DevOps Playground Cluster

- **GPU workloads** - R9 290 GPU compute
- **Heavy CI/CD** - Jenkins, GitLab Runner with parallel jobs
- **Slurm/HPC learning** - Batch job scheduling
- **High-performance services** - Large databases, complex builds

## Related Projects

- [DevOps Playground Cluster](../devops-playground-cluster/) - x86 high-performance cluster
- [Home Automation](../home-automation/) - Home Assistant could use this cluster
- [Self-Hosted Git Server](../self-hosted-git-server/) - Could use cluster for CI/CD integration
- [WD My Cloud PR4100](../../Device%20Lab/network-storage/wd-mycloud-pr4100/) - NFS storage backend

## Equipment Used

### Primary Hardware
- [BeagleBone Black](../../Programmable%20Devices/) (×4) - Check Programmable Devices inventory
- Raspberry Pi 2 Model B (×2) - Check Device Lab inventory
- Raspberry Pi Model A (×2) - Check Device Lab inventory

### Supporting Equipment
- Power controller (custom, code in [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery))
- Network switch (8+ ports)
- SD cards (8×, 16GB+ recommended)
- USB power supplies or powered USB hub
- Ethernet cables

### Optional
- [WD My Cloud PR4100](../../Device%20Lab/network-storage/wd-mycloud-pr4100/) - Shared NFS storage
- USB drives for additional storage
- Case/rack for organizing 8 boards

## Resources

### ARM Docker
- [Docker on ARM](https://www.docker.com/blog/getting-started-with-docker-for-arm-on-linux/)
- [ARM container images](https://hub.docker.com/u/arm32v7)

### k3s (Lightweight Kubernetes)
- [k3s Official Docs](https://k3s.io/)
- [k3s on Raspberry Pi](https://rancher.com/docs/k3s/latest/en/installation/installation-requirements/)
- [k3s cluster setup guide](https://github.com/k3s-io/k3s)

### Docker Swarm
- [Docker Swarm Tutorial](https://docs.docker.com/engine/swarm/swarm-tutorial/)
- [Swarm on Raspberry Pi](https://blog.alexellis.io/get-started-with-docker-on-raspberry-pi/)

### BeagleBone Resources
- [BeagleBone Black Documentation](https://beagleboard.org/black)
- [Armbian for BeagleBone](https://www.armbian.com/beaglebone-black/)

## Notes

- Originally documented as "SBC Cluster (Legacy)" in Device Lab
- Power controller code available in [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery) repository
- Model A Raspberry Pis have composite video output - could be useful for debugging or headless display
- BeagleBone Black has PRU (Programmable Real-time Unit) cores for real-time processing

## Success Criteria

### Phase 1: Basic Cluster
- [ ] All 8 nodes booting and network-accessible
- [ ] Docker installed and running on all nodes
- [ ] Cluster orchestration (Swarm or k3s) initialized
- [ ] Portainer web UI accessible

### Phase 2: Services
- [ ] Pi-hole running and serving DNS
- [ ] Local container registry operational
- [ ] Test service deployed across multiple nodes
- [ ] Power controller integration working

### Phase 3: Learning Goals
- [ ] Device filtering experiments documented
- [ ] ARM vs x86 container comparison notes
- [ ] Network isolation working
- [ ] Cross-reference with DevOps Playground learnings

---

*Last updated: 2026-01-07*
