# DevOps Playground Cluster

**Status**: In Progress

Multi-node home lab cluster for experimenting with container orchestration, HPC workloads, and DevOps tooling.

## Overview

| Aspect | Details |
|--------|---------|
| Project Type | Home Lab / Learning / Development |
| Status | In Progress |
| Start Date | TBD |
| Purpose | **Playground for DevOps and development experimentation** |
| Architecture | **Learning/experimental environment** - NOT for production services |

**Note:** This cluster is for learning and experimentation. Production services (Git, file sync, etc.) run on PR4100. This cluster can be powered down, broken, rebuilt without affecting critical services.

## Target Technologies

| Technology | Category | Use Case |
|------------|----------|----------|
| Docker | Containers | Base container runtime |
| Kubernetes (k8s/k3s) | Orchestration | Container orchestration learning |
| Slurm | HPC/Batch | Job scheduling, HPC workloads |
| Docker Swarm | Orchestration | Simple clustering alternative |
| Ansible | Automation | Configuration management |
| Terraform | IaC | Infrastructure as code practice |
| GitOps (ArgoCD/Flux) | Deployment | Declarative deployments |
| Prometheus/Grafana | Observability | Monitoring and metrics |

## Cluster Nodes

| Node | Hardware | Role | Status |
|------|----------|------|--------|
| **[Reduced BigRig](../../.personal/incoming/device-lab.md)** | FX-9590, 32GB RAM, 2x R9 290 | TBD | Building |
| **[Server](../../.personal/incoming/device-lab.md)** | FX-8350, 32GB RAM, 3TB storage | TBD | Building |

### Combined Resources

| Resource | Total |
|----------|-------|
| CPU Cores | 16 (8+8) |
| RAM | 64GB |
| Storage (HDD) | 3TB+ |
| Storage (SSD) | 500GB+ |
| GPUs | 2x R9 290 (compute potential) |

## Architecture Decisions

### Approach

This is a **learning playground**, not a production environment. The goal is to experiment with multiple technologies, not pick one "winner."

**Plan**: Install and configure multiple orchestration systems to learn their differences:

| System | Learning Goals |
|--------|----------------|
| Docker Compose | Basic multi-container apps |
| Docker Swarm | Simple native clustering |
| Kubernetes (k3s) | Industry-standard orchestration |
| Slurm | HPC job scheduling, batch workloads |
| Nomad | Alternative orchestration comparison |

### Operating System

| Option | Pros | Cons | Decision |
|--------|------|------|----------|
| Ubuntu Server | Familiar, well-supported | Heavier | TBD |
| Debian | Stable, lightweight | Slower updates | TBD |
| Proxmox | VMs + containers | More overhead | TBD |
| Fedora CoreOS | Container-focused, auto-updates | Learning curve | TBD |

### Networking

| Consideration | Options | Decision |
|---------------|---------|----------|
| Container networking | Bridge, Overlay, Macvlan | TBD |
| Service discovery | Built-in, Consul, CoreDNS | TBD |
| Load balancing | Traefik, Nginx, HAProxy | TBD |
| Storage | NFS, GlusterFS, local | TBD |

## Planned Workloads

### Infrastructure Services

| Service | Purpose | Priority |
|---------|---------|----------|
| Portainer | Container management UI | High |
| Traefik | Reverse proxy / ingress | High |
| Prometheus/Grafana | Monitoring and metrics | High |
| Registry | Local container registry | Medium |

### Development & Learning

| Workload | Purpose | Technology |
|----------|---------|------------|
| CI/CD pipelines | Jenkins, GitLab Runner, or Drone | DevOps practice |
| GitOps deployments | ArgoCD or Flux | Declarative deployments |
| Batch jobs | Sample HPC workloads | Slurm learning |
| Microservices demo | Sample distributed app | K8s learning |
| Chaos engineering | Chaos Monkey / Litmus | Resilience testing |

### Practical Services (Optional)

| Service | Purpose | Notes |
|---------|---------|-------|
| Home Assistant | Home automation | Could run here or dedicated |
| Plex | Media server | If storage sufficient |
| Pi-hole | DNS ad blocking | Lightweight |
| Gitea Mirror | Git repo mirror | Learning only - primary Git on PR4100 |

## Hardware Considerations

### Reduced BigRig Node
- **PSU Warning**: 750W may be undersized for full load (~926W estimated)
- **GPU Compute**: R9 290s could be used for GPU workloads (OpenCL)
- **Power consumption**: High - consider for compute-heavy tasks only

### Server Node
- **Storage-focused**: 7 drives, good for persistent storage
- **Lower power**: ~350W estimated, can run 24/7
- **Enterprise drives**: WD RE4 drives rated for continuous operation

## Tasks

### Setup Phase
- [ ] Decide on orchestration platform
- [ ] Choose base operating system
- [ ] Plan network topology
- [ ] Determine node roles (manager/worker)

### Hardware Prep
- [ ] Verify both systems POST and boot
- [ ] Test all RAM modules
- [ ] Check storage health (SMART)
- [ ] Consider PSU upgrade for Reduced BigRig
- [ ] Clean and re-thermal paste CPUs if needed

### Installation
- [ ] Install base OS on both nodes
- [ ] Configure networking (static IPs)
- [ ] Install Docker / container runtime
- [ ] Set up cluster orchestration
- [ ] Configure shared storage

### Services
- [ ] Deploy Portainer for management
- [ ] Set up reverse proxy (Traefik)
- [ ] Migrate/deploy planned services
- [ ] Configure backups

## Related Projects

- [Home Automation](../home-automation/) - Home Assistant could run on this cluster (if not on dedicated Pi)
- [WD My Cloud PR4100](../../Device%20Lab/network-storage/wd-mycloud-pr4100/) - Could provide NFS storage to cluster
- [Self-Hosted Git Server](../self-hosted-git-server/) - Production Git on PR4100; cluster can use for CI/CD webhooks

## Architecture Separation

**PR4100 (Production Services):**
- Always-on, low power (~10W)
- Gitea (primary Git hosting)
- Nextcloud (file sync) - if deployed
- Critical, persistent services

**DevOps Playground Cluster (Learning):**
- High power (FX CPUs), run when needed
- Safe to break/rebuild
- Docker/Kubernetes/Slurm experimentation
- CI/CD integration (not primary services)
- GPU compute experiments

## Equipment Used

- [Reduced BigRig](../../Device%20Lab/desktops/reduced-bigrig/) - FX-9590, 32GB RAM, 2x R9 290 GPUs
- [Server FX-8350](../../Device%20Lab/desktops/server-fx8350/) - FX-8350, 32GB RAM, 3TB storage
- [WD My Cloud PR4100](../../Device%20Lab/network-storage/wd-mycloud-pr4100/) - Optional NFS storage backend

## Notes

- Both machines are AMD AM3+ platform - no upgrade path, but plenty capable for home lab
- Combined 64GB RAM is good for running many containers
- Server node's storage makes it ideal for persistent data
- Consider power costs - FX CPUs are not power-efficient

## Log

| Date | Update |
|------|--------|
| 2025-01 | Project documented in Device Lab |
| 2026-01-07 | Moved to main projects/ directory for better visibility |

