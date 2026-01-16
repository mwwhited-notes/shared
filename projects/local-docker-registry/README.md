# Local Docker Registry

**Status**: Planning | **Type**: DevOps / Infrastructure

---

## Overview

Private, self-hosted Docker image registry running locally for faster image pulls, reduced bandwidth, offline deployment, and complete control over image distribution. Essential for development, testing, and production deployments without dependency on Docker Hub public registry or cloud-hosted registries.

**Key Use Cases:**
- **Development:** Cache images locally for team (faster builds, no internet required)
- **Air-gapped Systems:** Offline deployment to networks without public internet
- **CI/CD Pipeline:** Private registry for internal images before pushing to public registries
- **Pull Optimization:** Mirror public images locally, enable image deduplication
- **Image Scanning:** Centralized security scanning and compliance checks before deployment
- **Bandwidth Savings:** Reduce egress costs and improve deployment speed
- **Integration:** Central source for DevOps Playground Cluster, SBC Cluster, Cline, and other services

**Architecture:**
```
┌─────────────────────────────────────────────┐
│      Local Docker Registry (5000)            │
│  (Docker Registry image running in Docker)   │
│  ├─ Image Storage (/data/docker/registry)   │
│  ├─ Web UI (Optional: Registry UI)           │
│  └─ REST API (Docker API compatible)        │
└─────────────────────────────────────────────┘
          ↑                     ↑
          │                     │
    ┌─────────────┐     ┌──────────────┐
    │   Docker    │     │  DevOps      │
    │  Builders   │     │  Playground  │
    │  (Dev Env)  │     │  Cluster     │
    └─────────────┘     └──────────────┘

    ┌─────────────┐     ┌──────────────┐
    │   Cline     │     │  SBC         │
    │  Container  │     │  Cluster     │
    └─────────────┘     └──────────────┘
```

---

## Project Goals

1. **Set up local Docker Registry** - Configure and deploy registry with persistent storage
2. **Image Management Tools** - Scripts for mirroring, tagging, and managing images
3. **Web UI Integration** - Optional: Deploy registry web UI for browsing images
4. **CI/CD Integration** - Configure registry as target for automated builds
5. **Cluster Integration** - Enable DevOps Playground and SBC Cluster to pull from local registry
6. **Security & Monitoring** - Image scanning, authentication, usage tracking
7. **Documentation** - Setup guides, best practices, troubleshooting

---

## Hardware & Infrastructure

**Host Machine Options:**

| Option | Hardware | Use Case |
|--------|----------|----------|
| **NAS** | WD My Cloud PR4100 | Always-on, persistent storage, network accessible |
| **DevOps Cluster** | FX-9590/FX-8350 machines | Integrated with cluster infrastructure |
| **Dedicated Host** | Spare server/Pi | Dedicated registry host |
| **Development Workstation** | Dev machine (RTX 4070 Ti) | Local-only during development |

**Recommended:** WD My Cloud PR4100 NAS (always-on, centralized, network-accessible)

**Storage Requirements:**
- Base Registry image: ~40MB
- Typical image set (10-20 images): 10-50GB
- Growth factor: Plan for 2-3x current size

---

## Architecture & Components

### Core Components

1. **Docker Registry** (official Docker image)
   - REST API compatible with Docker CLI
   - Runs on port 5000 (configurable)
   - Filesystem backend (default) or S3/Azure compatible

2. **Optional: Registry UI**
   - Web interface for browsing images
   - Port 8080 (configurable)
   - Real-time image search and inspection

3. **Optional: Registry Garbage Collector**
   - Cleanup unused image layers
   - Scheduled cleanup jobs

4. **Image Storage**
   - Persistent volume `/data/docker/registry`
   - Should be on fast storage (SSD preferred)

### Supporting Infrastructure

- **Networking:** Registry accessible on network (Docker bridge or host network)
- **Authentication:** Optional TLS, htpasswd, or OAuth2
- **Monitoring:** Track registry usage, image pulls, storage usage
- **Backup:** Automated backup of registry storage to secondary location

---

## Detailed Specifications

### Docker Registry Configuration

```yaml
# Core settings
version: 0.1
log:
  level: info
storage:
  filesystem:
    rootdirectory: /data/docker/registry
  delete:
    enabled: true  # Allow image deletion
  cache:
    blobdescriptor: inmemory  # Cache layer descriptors in memory

http:
  addr: 0.0.0.0:5000
  headers:
    X-Content-Type-Options:
      - nosniff
    Access-Control-Allow-Origin:
      - '*'
    Access-Control-Allow-Methods:
      - GET, HEAD, OPTIONS

# Optional: Cleanup old images
gc:
  enabled: true
  deleteuntagged: true
  deleteunreferencedlayers: true

# Optional: Enable TLS
tls:
  certificate: /certs/registry.crt
  key: /certs/registry.key
```

### Networking Options

**Option 1: Host Network (Simple)**
```bash
docker run -d --network host \
  -v /data/docker/registry:/data \
  registry:2
```
- Access: `http://localhost:5000`
- All containers on host can access
- Best for single-machine setups

**Option 2: Custom Bridge Network (Recommended)**
```bash
docker network create registry-network

docker run -d --name registry \
  --network registry-network \
  -p 5000:5000 \
  -v /data/docker/registry:/data \
  registry:2
```
- Access: `http://registry:5000` (from other containers)
- Access: `http://localhost:5000` (from host)
- Cleaner isolation, supports multiple services

**Option 3: Docker Compose (Best)**
```yaml
version: '3.8'
services:
  registry:
    image: registry:2
    ports:
      - "5000:5000"
    volumes:
      - registry_data:/var/lib/registry
    networks:
      - docker-network

volumes:
  registry_data:

networks:
  docker-network:
```

---

## Implementation Plan

### Phase 1: Basic Registry Setup
- [ ] Choose host machine (NAS or DevOps Cluster preferred)
- [ ] Create persistent storage location (/data/docker/registry)
- [ ] Deploy Registry container (docker run or docker-compose)
- [ ] Verify API endpoint (`curl http://localhost:5000/v2/`)
- [ ] Test push/pull from development machine
- [ ] Document network access (hostname/IP, port)

### Phase 2: Configuration & Security
- [ ] Configure TLS certificates (for HTTPS)
- [ ] Set up authentication (htpasswd or OAuth2)
- [ ] Configure image retention policies
- [ ] Enable garbage collection/cleanup
- [ ] Set resource limits (memory, CPU)

### Phase 3: Web UI & Monitoring
- [ ] Deploy optional Registry UI container
- [ ] Configure UI to connect to Registry API
- [ ] Set up basic monitoring (container stats, storage usage)
- [ ] Create dashboard or simple tracking script

### Phase 4: Integration
- [ ] Update DevOps Playground Cluster docker configs to use local registry
- [ ] Configure Cline dockerfile to pull base images from registry
- [ ] SBC Cluster: Configure k3s to use local registry
- [ ] CI/CD: Point image builds to `localhost:5000`

### Phase 5: Image Management
- [ ] Create script to mirror popular base images
- [ ] Implement image pruning schedule
- [ ] Document image retention policy
- [ ] Set up backup strategy

### Phase 6: Documentation
- [ ] Write setup guide (quick start + detailed)
- [ ] Document configuration options
- [ ] Create troubleshooting guide
- [ ] Document integration points
- [ ] Build management playbooks

---

## Key Considerations

### Storage Strategy

**Fast Path (Recommended):**
- Registry on SSD (local or NAS)
- Layer caching in-memory for frequent images
- Backup to secondary storage weekly

**Example Docker Compose:**
```yaml
services:
  registry:
    image: registry:2
    volumes:
      - /fast-storage/docker-registry:/var/lib/registry  # SSD
    environment:
      REGISTRY_STORAGE_CACHE_BLOBDESCRIPTOR: inmemory
```

### Image Lifecycle

```
Public Registry (Docker Hub, Quay.io)
           ↓ (docker pull myimage)
Local Registry (Cache)
           ↓ (docker pull from :5000)
Container Runtimes
           ↓ (after use)
Image Cleanup (GC weekly)
```

### Performance Metrics to Track

| Metric | Target | Notes |
|--------|--------|-------|
| Registry API response | <100ms | ping `/v2/` endpoint |
| Image pull (local) | <5s | cached/local image |
| Image push (new) | <30s | depends on size |
| Disk usage | <80% capacity | trigger cleanup at 75% |
| Storage utilization | Track over time | plan for growth |

---

## Integration with Existing Projects

### DevOps Playground Cluster
- Configure Docker daemon on FX-9590/FX-8350 to trust local registry
- Update docker-compose.yml files to use `localhost:5000/image:tag`
- Build images locally, push to registry instead of Docker Hub

### Cline Docker Setup
```dockerfile
# Use local registry for base image
FROM localhost:5000/node:20-slim

# Install Cline
RUN npm install -g @cline/cli
```

Then build and push to registry:
```bash
docker build -t localhost:5000/cline-local .
docker push localhost:5000/cline-local
```

### SBC Cluster
Configure k3s to use local registry:
```bash
# On SBC k3s clusters, set registries.yaml
mkdir -p /etc/rancher/k3s/
cat > /etc/rancher/k3s/registries.yaml <<EOF
mirrors:
  docker.io:
    endpoint:
      - "http://registry-host:5000"
EOF
```

---

## Common Workflows

### Push Image to Local Registry

```bash
# Build locally
docker build -t myimage:latest .

# Tag for registry
docker tag myimage:latest localhost:5000/myimage:latest

# Push to local registry
docker push localhost:5000/myimage:latest

# Pull from anywhere on network
docker pull localhost:5000/myimage:latest
```

### Mirror Public Images

```bash
# Pull from Docker Hub
docker pull node:20-alpine

# Tag for local registry
docker tag node:20-alpine localhost:5000/node:20-alpine

# Push to local registry
docker push localhost:5000/node:20-alpine

# Automated mirroring script (see Phase 5)
./mirror-images.sh official/node:20-alpine ubuntu:22.04 alpine:latest
```

### List Available Images

```bash
# Using registry API
curl http://localhost:5000/v2/_catalog | jq .

# Using registry UI (if deployed)
# Browse to http://localhost:8080
```

### Clean Up Old Images

```bash
# Run garbage collection
docker exec registry \
  registry garbage-collect /etc/docker/registry/config.yml

# Or automated script
./cleanup-registry.sh --keep-last 5 --max-age 30
```

---

## Troubleshooting

### Registry not accessible

```bash
# Check if running
docker ps | grep registry

# Check logs
docker logs registry

# Test connectivity
curl http://localhost:5000/v2/

# From another host
curl http://registry-host:5000/v2/
```

### Push fails: "Denied"

```bash
# Check authentication
docker login localhost:5000 -u user -p password

# If using htpasswd, regenerate credentials
htpasswd /data/docker/registry/htpasswd username
docker restart registry
```

### Storage quota exceeded

```bash
# Check disk usage
du -sh /data/docker/registry/

# Run garbage collection
docker exec registry registry garbage-collect \
  /etc/docker/registry/config.yml --delete-untagged

# Delete specific images
# List: curl http://localhost:5000/v2/_catalog | jq .repositories[]
# Delete: curl -X DELETE http://localhost:5000/v2/myimage/manifests/<digest>
```

### Slow pulls

```bash
# Enable in-memory caching
REGISTRY_STORAGE_CACHE_BLOBDESCRIPTOR=inmemory

# Move storage to faster disk
# Migrate /data/docker/registry to SSD

# Check network connectivity
iperf3 between registry and clients
```

---

## Tools & Resources

### Official Documentation
- [Docker Registry GitHub](https://github.com/distribution/distribution)
- [Registry Configuration Reference](https://distribution.github.io/distribution/about/configuration/)
- [Registry API Spec](https://docs.docker.com/registry/spec/api/)

### Supporting Tools
- **Registry Cleanup:** `registry-cli` (npm package for image management)
- **Web UI:** `docker-registry-ui` or `joxit/docker-registry-ui`
- **Image Scanning:** `trivy` (vulnerability scanning)
- **Monitoring:** `promregator` + Prometheus/Grafana

### Docker Compose Examples
- **Simple:** Single registry with local storage
- **Advanced:** Registry + UI + Monitoring + Backup
- **HA:** Multiple registries with shared backend storage

---

## Cross-References

### Related Projects
- [devops-playground-cluster/](../devops-playground-cluster/) - Primary integration target
- [sbc-cluster/](../sbc-cluster/) - ARM-based cluster integration
- [cline-qwen3-coder-30b/](../cline-qwen3-coder-30b/) - Docker base images
- [self-hosted-git-server/](../self-hosted-git-server/) - Related infrastructure

### Equipment
- [WD My Cloud PR4100](../../Test%20Equipment/) - Recommended host (always-on NAS)
- [DevOps Playground Cluster](../devops-playground-cluster/) - Cluster infrastructure

### Documentation
- [tools-and-components.md](../../tools-and-components.md) - Related tools
- [network-diagram.md](../../network-diagram.md) - Network topology/IP assignments

---

## Notes

- **Private by Design:** Registry only accessible on trusted networks (not internet-facing)
- **No Authentication by Default:** Configure auth (htpasswd, TLS) for security if exposed
- **Storage:** Plan for 2-3x growth; monitor with automated alerts
- **Backup:** Critical infrastructure - backup registry storage separately
- **Performance:** Local registry pulls are typically 10-100x faster than public registries
- **Bandwidth Savings:** Estimated 80%+ reduction in Docker Hub bandwidth with full caching

---

## Progress Tracking

| Phase | Status | Notes |
|-------|--------|-------|
| Planning | In progress | Architecture defined |
| Basic Setup | Not started | Awaiting hardware decision |
| Configuration | Not started | |
| UI & Monitoring | Not started | |
| Integration | Not started | |
| Management | Not started | |
| Documentation | Pending | README created |

---

**Project Created:** 2026-01-16
**Last Updated:** 2026-01-16
**Status:** Planning - Ready for hardware allocation and setup

