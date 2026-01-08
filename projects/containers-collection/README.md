# Docker Containers Collection Project

**Status**: Planning

Create a centralized repository to collect, organize, and document all Docker containers, compose files, and containerization efforts across all projects.

## Overview

| Aspect | Details |
|--------|---------|
| Project Type | Infrastructure / Container Repository |
| Status | Planning |
| Start Date | 2026-01-08 |
| Purpose | **Centralize Docker assets from scattered projects** |
| Target Repository | containers (to be created) |

## Problem Statement

Docker assets are currently scattered across multiple repositories:
- Custom Dockerfiles in various projects
- Docker Compose stacks in different locations
- No centralized catalog of available images
- Difficult to discover and reuse containerization work
- Duplication of common patterns

## Solution

Create a new `containers` repository to consolidate all Docker-related assets:
- Custom Docker images with build scripts
- Docker Compose stacks for common environments
- Container management scripts and utilities
- Complete documentation and catalogs

## Proposed Repository

**Name:** containers (or docker-containers)
**Organization:** OutOfBandDevelopment or mwwhited
**URL:** https://github.com/[org]/containers.git (to be created)
**Purpose:** Centralized Docker container definitions, compose files, and containerization utilities

## Repository Structure

```
containers/
├── README.md
├── CLAUDE.md
├── images/                    # Custom Docker images
│   ├── dev-tools/
│   │   ├── dotnet-sdk/
│   │   ├── node-dev/
│   │   └── python-dev/
│   ├── runtime/
│   │   ├── dotnet-runtime/
│   │   └── node-runtime/
│   ├── databases/
│   │   ├── postgres-with-extensions/
│   │   └── sqlserver-with-tools/
│   └── ai-ml/
│       ├── ollama/
│       ├── qdrant/
│       └── sbert/
├── compose/                   # Docker Compose files
│   ├── dev-environments/
│   │   ├── dotnet-full-stack/
│   │   ├── node-react-stack/
│   │   └── python-data-science/
│   ├── databases/
│   │   ├── postgres-pgadmin/
│   │   └── sqlserver-management/
│   ├── ai-ml-stacks/
│   │   ├── ollama-qdrant/
│   │   ├── sbert-opensearch/
│   │   └── full-ai-stack/
│   └── utilities/
│       ├── portainer/
│       └── monitoring/
├── scripts/                   # Container management scripts
│   ├── build-all.sh
│   ├── push-all.sh
│   ├── cleanup.sh
│   └── utils/
├── docs/                      # Documentation
│   ├── image-catalog.md
│   ├── compose-catalog.md
│   ├── best-practices.md
│   └── migration-guide.md
└── .github/
    └── workflows/
        ├── build-images.yml
        └── test-compose.yml
```

## Initial Docker Asset Scan

Assets found across current repositories:

### Public Dockerfiles

| Location | Base Image | Purpose |
|:---------|:-----------|:--------|
| code/public/CQRS-Examples/ | mcr.microsoft.com/dotnet/aspnet:7.0 | CQRS/Event Sourcing example |
| code/public/YearOfCode2024/ | TBD | Hybrid search example |
| code/public/YearOfLanguages2023/ | tensorflow | TensorFlow demo |

### Public Docker Compose Files

| Location | Services | Purpose |
|:---------|:---------|:--------|
| RunScripts | Multiple | Docker wrapper scripts for dev tools |

### Private Assets

**Private Docker assets documented separately:** See `../../private/docker-assets/` for detailed inventory of private containers requiring sanitization review before migration.

Key private assets include production-quality AI/ML infrastructure with GPU support. Details in private documentation.

## Migration Sources

### Public Sources

| Source Repository | Docker Assets | Migration Target |
|:------------------|:--------------|:-----------------|
| RunScripts | Docker wrapper scripts | scripts/wrappers/ |
| dotex | Possible dev containers | images/dev-tools/dotnet-sdk/ |
| CQRS-Examples | Example containers | examples/dotnet-cqrs/ |
| YearOfCode2024 | Hybrid search example | examples/hybrid-search/ |
| YearOfLanguages2023 | TensorFlow example | examples/tensorflow/ |

### Private Sources

**See:** `../../private/docker-assets/` for details on private Docker assets requiring sanitization review.

## Privacy Considerations

**IMPORTANT**: Many Docker assets are in PRIVATE repositories.

**Process**:
1. Scan and inventory all Docker assets
2. **PRIVATE** assets require review before publishing
3. **PUBLIC** assets can be migrated immediately
4. Create sanitized/generic versions of private assets where appropriate

### Sanitization Requirements

When migrating PRIVATE assets to PUBLIC repository, **ALL** company/client information must be removed:

**Company Name Sanitization (Two-Step Process):**

Step 1: Replace ALL client/employer names with your company (treat as PII)
- Client/employer names: Cadwell, ERisk, Nationwide, Eliassen, BMW, Chase, JPMC, Itrica, GreenOnion, LifeTime, etc.
- **All become:** "Out-of-Band Development"

Step 2: For public templates, use generic placeholder
- "Out-of-Band Development" → "YourCompany" (in .env.template and example configs)

**Sensitive Data Removal:**
- API keys → `${API_KEY}` or `your-api-key-here`
- Database credentials → `${DB_USER}`, `${DB_PASSWORD}`
- Connection strings → Environment variables with `.env.template`
- Domain names → `outofband.dev` or `example.com`
- Internal IPs → RFC 1918 ranges (192.168.x.x, 10.x.x.x)
- Email addresses → `admin@example.com`

**Create `.env.template` files** with all required environment variables documented with placeholder values.

## Migration Workflow

See `.claude/protocols/DOCKER_CONTAINERS_COLLECTION_PROTOCOL.md` for complete workflow.

### High-Level Steps

1. **Scan** - Find all Dockerfiles and compose files across projects
2. **Categorize** - Public vs Private, by purpose
3. **Create Repository** - Initialize containers repo
4. **Migrate Public** - Copy public assets with documentation
5. **Review Private** - Identify what can be made public (sanitized versions)
6. **Document** - Create catalogs and usage guides
7. **Integrate** - Add as submodule to main collection

## Benefits

1. **Centralized Management** - All containers in one place
2. **Easy Discovery** - Catalogs show what's available
3. **Reusability** - Share compose stacks across projects
4. **Version Control** - Track image evolution
5. **Documentation** - Clear purpose and usage for each
6. **CI/CD** - Automated building and testing
7. **Resume Value** - "Maintained collection of containerized environments"

## Current Status

**Phase**: Inventory Complete - Ready for Repository Creation

- [x] Create collection protocol
- [x] Initial Docker asset scan
- [x] Document project in shared notes
- [x] Identify privacy concerns (PRIVATE vs PUBLIC)
- [x] **Complete asset inventory with details**
  - Public: 3+ Dockerfiles, multiple compose files
  - Private: Documented in `../../private/docker-assets/` (requires sanitization)
- [ ] Create GitHub repository
- [ ] Set up repository structure
- [ ] Begin migrating PUBLIC assets
- [ ] Review PRIVATE assets for publication (especially ContainerStore)

## Immediate Next Steps

1. ~~Complete detailed inventory of all Docker assets~~ ✅ **DONE** - See `docker-assets-inventory.md`
2. ~~Document base images and purposes~~ ✅ **DONE**
3. ~~Categorize by public/private status~~ ✅ **DONE**
4. **Create the containers repository on GitHub** ← NEXT
5. Set up repository structure following `docker-assets-inventory.md` proposed layout
6. Migrate CQRS-Examples Dockerfile (PUBLIC)
7. Create .dockerignore templates from public examples
8. Review private Docker assets for sanitization (see `../../private/docker-assets/`)
   - Sanitize company/client references
   - Remove/genericize all credentials and API keys
   - Create .env.template files

## Related Files

**Protocols:**
- `.claude/protocols/DOCKER_CONTAINERS_COLLECTION_PROTOCOL.md` - Complete migration workflow
- `.claude/protocols/SINGLE_REPOSITORY_ANALYSIS_PROTOCOL.md` - Repository analysis process

**Inventory:**
- `../../docker-assets-inventory.md` - Complete scan results (public + private)
- `../../private/docker-assets/` - Private Docker asset details (sanitization required)

**Public Source Locations:**
- `code/public/RunScripts/` - Docker wrapper scripts
- `code/public/CQRS-Examples/` - Example application
- `code/public/YearOfCode2024/` - Learning projects
- `code/public/YearOfLanguages2023/` - Learning projects

**Private Source Details:** See `../../private/docker-assets/` - requires sanitization review

## Technologies

**Container Images:**
- .NET SDK/Runtime
- Node.js development
- Python data science
- Database images (PostgreSQL, SQL Server)
- AI/ML (Ollama, Qdrant, SBERT)

**Compose Stacks:**
- Full-stack development environments
- AI/ML research stacks
- Database management tools
- Monitoring and observability

**Infrastructure:**
- GitHub Actions for CI/CD
- Automated image building
- Docker Hub or GitHub Container Registry

## References

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Best Practices](https://docs.docker.com/compose/production/)
- [RunScripts Repository](https://github.com/OutOfBandDevelopment/RunScripts)

---

*Last updated: 2026-01-08*
*Next review: After asset inventory complete*
