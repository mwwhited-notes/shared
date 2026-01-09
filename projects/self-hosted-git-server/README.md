# Self-Hosted Git Server

Local Git hosting for personal repositories and backup of public projects.

## Overview

This project sets up a self-hosted Git server to move personal repositories back onto local hardware and create backups of public projects. Goals include data sovereignty, backup redundancy, and learning self-hosted development workflows.

**Primary use cases:**
- Host private repositories on own hardware (not GitHub/cloud)
- Mirror/backup public GitHub repositories locally
- Local development workflow with web UI and issue tracking
- CI/CD integration for personal projects

## Project Status

**Status:** Planning

**Next Steps:**
1. Choose Git server platform (Gitea vs. bare repos)
2. Decide deployment location (PR4100 vs. DevOps Cluster)
3. Plan backup and sync strategy
4. Configure authentication and access control
5. Migrate first repository as proof-of-concept

## Architecture Options

### Option 1: Bare Git Repositories (Simple)

**Approach:** Traditional bare Git repos on NFS/SMB share

```
PR4100 NAS
  └── /git-repos/
      ├── project1.git/
      ├── project2.git/
      └── backup-mirrors/
          ├── EmbeddedBakery.git
          └── BinaryDataDecoders.git
```

**Pros:**
- Simple, minimal overhead
- Direct Git protocol access
- No web service to maintain
- Lightweight

**Cons:**
- No web UI
- No issue tracking
- No pull request workflow
- Manual repository creation

**Access:**
```bash
git clone ssh://user@pr4100/volume1/git-repos/project1.git
```

---

### Option 2: Gitea (Recommended)

**Approach:** Lightweight self-hosted Git service with web UI

**Deployment:** Docker container on WD My Cloud PR4100

**Features:**
- GitHub-like web interface
- Repository browser and code search
- Issue tracking and project boards
- Pull request workflow
- User/organization management
- Webhook support for CI/CD
- SSH and HTTP(S) Git access
- Git LFS support
- Lightweight (~100MB RAM)

**System Requirements:**
- Docker support ✓ (PR4100 has Docker)
- CPU: Intel N3710 ✓ (sufficient for Gitea)
- RAM: ~200MB per container
- Storage: Repositories on NAS

---

### Option 3: GitLab CE (Full-Featured)

**Approach:** Complete DevOps platform

**Deployment:** Docker container on DevOps Playground Cluster

**Features:**
- Full CI/CD pipelines
- Container registry
- Issue tracking, wikis, snippets
- Advanced user management
- GitLab Runner integration

**System Requirements:**
- CPU: 4+ cores recommended
- RAM: 4GB minimum, 8GB recommended
- More resource-intensive than Gitea

**Note:** May be overkill for personal use, better suited if expanding to full DevOps learning

---

## Recommended Approach

**Primary:** Gitea on WD My Cloud PR4100

**Rationale:**
- **Production service** - PR4100 is always-on, low power (~10W)
- Perfect balance of features and resource usage
- PR4100 already has Docker support
- Stable platform for critical services (Git repos shouldn't go down)
- Web UI for easy repository management
- Issue tracking for personal projects
- **Separate from DevOps Playground Cluster** - Cluster is for learning/experimentation, not production

**Architecture separation:**
- **PR4100:** Production services (Gitea, Nextcloud, persistent data)
- **DevOps Cluster:** Learning environment (can break things, high power, run when needed)

## Deployment Plan

### Hardware Selection

**Target:** [WD My Cloud PR4100](../../Device%20Lab/network-storage/wd-mycloud-pr4100/)
- Intel N3710 CPU (4-core)
- Docker support
- Always-on NAS
- Existing network storage
- ~10W idle power

**Alternative:** DevOps Playground Cluster
- **Not recommended for Git hosting** - Cluster is for learning/experimentation
- High power consumption (not always-on)
- Use cluster for CI/CD integration, not primary Git storage
- Only consider if you need GitLab's full DevOps platform for learning

### Gitea Docker Deployment

**Docker Compose configuration:**
```yaml
version: "3"

services:
  gitea:
    image: gitea/gitea:latest
    container_name: gitea
    environment:
      - USER_UID=1000
      - USER_GID=1000
      - GITEA__database__DB_TYPE=sqlite3
      - GITEA__server__DOMAIN=gitea.local
      - GITEA__server__ROOT_URL=http://gitea.local:3000/
    restart: always
    volumes:
      - /volume1/docker/gitea:/data
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
    ports:
      - "3000:3000"
      - "222:22"
```

### Network Configuration

**Access:**
- Internal network: `http://pr4100.local:3000`
- SSH access: `ssh://git@pr4100.local:222`
- Optional: Reverse proxy with SSL (Nginx/Traefik)

**Firewall:**
- Open port 3000 (HTTP) - internal only
- Open port 222 (SSH Git) - internal only
- Optional: VPN access for remote work

## Repository Migration Strategy

### Phase 1: New Private Repositories
- Create new projects directly on Gitea
- Test workflow and performance
- Establish backup routine

### Phase 2: Migrate Existing Private Repos
- Clone from current hosting
- Push to Gitea
- Update local Git remotes
- Verify all branches/tags migrated

### Phase 3: Mirror Public Repositories

**Repositories to backup:**
- [EmbeddedBakery](https://github.com/mwwhited/EmbeddedBakery)
  - Analysis: [.claude/analysis/EmbeddedBakery/4caaa60-2025-03-14.md](../../../.claude/analysis/EmbeddedBakery/4caaa60-2025-03-14.md) (6,586 files, 28 FPGA projects)
- [BinaryDataDecoders](https://github.com/mwwhited/BinaryDataDecoders)
  - Analysis: [.claude/analysis/BinaryDataDecoders/faac1171-2025-02-14.md](../../../.claude/analysis/BinaryDataDecoders/faac1171-2025-02-14.md) (796K+ downloads, 65 projects)
- [DeviceBridge](https://github.com/mwwhited/DeviceBridge)
  - Analysis: [.claude/analysis/DeviceBridge/a9bc076-2025-08-01.md](../../../.claude/analysis/DeviceBridge/a9bc076-2025-08-01.md) (protocol engineering)
- [MM8000](https://github.com/mwwhited-archives/MM8000) 🔒 Archived
  - Analysis: [.claude/analysis/MM8000/7fbbdec-2026-01-08.md](../../../.claude/analysis/MM8000/7fbbdec-2026-01-08.md) (Intel 8085 emulator)
- [dotex](https://github.com/OutOfBandDevelopment/dotex)
  - Analysis: [.claude/analysis/dotex/687bd7d-2025-08-01.md](../../../.claude/analysis/dotex/687bd7d-2025-08-01.md) (109 projects, .NET 9.0)
- [RunScripts](https://github.com/OutOfBandDevelopment/RunScripts)
  - Analysis: [.claude/analysis/RunScripts/4077d61-2025-10-23.md](../../../.claude/analysis/RunScripts/4077d61-2025-10-23.md) (56 Docker tools)
- Other public projects (see inventory.md)

**Mirror setup:**
```bash
# Create mirror clone
git clone --mirror https://github.com/mwwhited/EmbeddedBakery.git

# Push to Gitea
cd EmbeddedBakery.git
git push --mirror ssh://git@pr4100.local:222/mwwhited/EmbeddedBakery.git

# Set up periodic sync (cron job)
git fetch --all
git push --mirror
```

## Backup Strategy

### Repository Backups
- **Primary storage:** PR4100 RAID array
- **Secondary backup:** External USB drive (scheduled)
- **Tertiary backup:** Cloud backup of critical repos (encrypted)

### Automated Sync
```bash
# Cron job to sync public repo mirrors
0 2 * * * /volume1/scripts/sync-git-mirrors.sh
```

### Gitea Configuration Backup
- Database: SQLite file in `/data/gitea/gitea.db`
- Configuration: `/data/gitea/conf/app.ini`
- Custom files: `/data/gitea/custom/`

## Authentication & Access Control

### User Management
- **Admin account:** Primary user
- **Additional accounts:** Per-device or per-developer if sharing

### SSH Keys
- Generate SSH key per workstation
- Add to Gitea user profile
- Configure SSH config for convenient access

```bash
# ~/.ssh/config
Host gitea
  HostName pr4100.local
  Port 222
  User git
  IdentityFile ~/.ssh/id_rsa_gitea
```

### Organizations
- `personal` - Personal projects
- `archive` - Archived projects
- `backup-mirrors` - Public repo backups

## Integration with DevOps Cluster

### Optional Enhancements

**CI/CD Integration:**
- Gitea webhooks → Jenkins on DevOps Cluster
- Automated testing on push
- Build artifacts stored on PR4100

**Container Registry:**
- Deploy Docker registry on cluster
- Store built images for personal projects

**GitOps Workflow:**
- Use ArgoCD/Flux pointing to Gitea repos
- Declarative infrastructure management

## Maintenance

### Regular Tasks
- [ ] Weekly: Check Gitea container health
- [ ] Monthly: Update Gitea Docker image
- [ ] Quarterly: Verify backups are restorable
- [ ] Quarterly: Review storage usage and clean old repos

### Monitoring
- Container uptime via Portainer (if deployed)
- Disk space monitoring on PR4100
- Access logs for security

## Security Considerations

### Network Security
- Gitea only accessible on internal network
- VPN required for remote access (WireGuard)
- No direct internet exposure

### Data Security
- HTTPS for web access (optional, internal network)
- SSH key authentication only (no passwords)
- Regular backups with encryption
- RAID array for data redundancy

### Access Control
- Strong admin password
- SSH keys required for Git operations
- Disable user registration (invite-only)

## Equipment Used

### Primary Hardware
- [WD My Cloud PR4100](../../Device%20Lab/network-storage/wd-mycloud-pr4100/) - Docker host, storage backend

### Optional Integration
- [DevOps Playground Cluster](../devops-playground-cluster/) - CI/CD, container registry, GitOps

### Network Infrastructure
- Internal network with VPN access
- See [network-diagram.md](../../network-diagram.md) for topology

## Related Projects

- [DevOps Playground Cluster](../devops-playground-cluster/) - CI/CD integration, container registry
- [SBC Cluster](../sbc-cluster/) - Alternative ARM deployment platform
- [Home Automation](../home-automation/) - Configuration management with Git
- [Docker Containers Collection](../containers-collection/) - Container definitions for Gitea deployment
- [dotex Consolidation](../dotex-consolidation/) - Infrastructure project benefiting from self-hosted Git

## Resources & References

### Gitea
- [Gitea Official Docs](https://docs.gitea.io/)
- [Gitea Docker Setup](https://docs.gitea.io/en-us/install-with-docker/)
- [Gitea GitHub](https://github.com/go-gitea/gitea)

### Alternatives
- [Gogs](https://gogs.io/) - Simpler, less features than Gitea
- [GitLab CE](https://about.gitlab.com/install/) - Full DevOps platform
- [Forgejo](https://forgejo.org/) - Gitea fork with different governance

### Git Server Administration
- [Pro Git Book](https://git-scm.com/book/en/v2) - Chapter 4: Git on the Server
- Git mirroring and backup strategies
- SSH key management best practices

## Success Criteria

### Phase 1 (Proof of Concept)
- [ ] Gitea deployed and accessible on PR4100
- [ ] SSH and HTTP Git access working
- [ ] Web UI functional and configured
- [ ] Create first test repository
- [ ] Clone, commit, push workflow verified

### Phase 2 (Migration)
- [ ] Migrate 3+ private repositories
- [ ] All branches and tags preserved
- [ ] Local workstations updated with new remotes
- [ ] Backup scripts configured and tested

### Phase 3 (Mirrors)
- [ ] Mirror 5+ public repositories
- [ ] Automated sync working
- [ ] Verify repositories browsable via web UI

### Phase 4 (Integration)
- [ ] Optional: Webhook to DevOps Cluster CI/CD
- [ ] Optional: Container registry integration
- [ ] Backup verification completed

---

*Last updated: 2026-01-07*
