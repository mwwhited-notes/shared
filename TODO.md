# TODO

> **Session Reminder:** Check at least once per session if new projects have been added externally to `projects/` directory or `projects/project-ideas.md` to ensure awareness of external updates.

## Active Tasks

### Order Processing
- [ ] Review amazon orders from 2020 and before
- [ ] Review aliexpress orders
- [ ] Review mouser orders

### Documentation
- [ ] Review and update workshop-capabilities.md with new projects
- [ ] Consider adding project status tracking to projects/project-ideas.md

### Equipment
- [ ] Continue cataloging remaining equipment purchases
- [ ] Verify all equipment has cross-references to related projects

### Infrastructure (Priority)
- [ ] **Deploy Gitea on PR4100** (see projects/self-hosted-git-server/)
- [ ] **Set up Docker on PR4100** for production services (Gitea, Nextcloud)
- [ ] Fix PR4100 Windows credential persistence issue (see Device Lab/network-storage/wd-mycloud-pr4100/windows-credential-fix.md)

### Directory Indexes (INDEX_PROTOCOL.md)
- [ ] Create README.md for Programmable Devices/ (20+ devices, 5 categories)
- [ ] Create README.md for Expansion Boards/ (shields/hats/capes)
- [ ] Create README.md for Test Equipment/ (oscilloscopes, DMMs, supplies)
- [ ] Create README.md for Vintage Computers/ (Apple II, TI-99/4A, etc.)
- [ ] Create README.md for Camera Collection/ (cameras, lenses, accessories)
- [ ] Create README.md for Device Lab/ (tablets, phones, NAS, gaming devices)
- [ ] Create README.md for Notes/ (technical notes organized by topic)
- [ ] Create README.md for AnalogComputers/ (research collection overview)

### Research: Synchronized Telemetry Streaming (Phase 2)
See: projects/synchronized-telemetry-streaming-research/

**Diagrams:**
- [ ] Create PlantUML diagrams for system architecture (5-6 major patterns)
- [ ] Create protocol flow diagrams (RaptorQ, Kafka, Lab Streaming Layer)
- [ ] Create decision tree visualization
- [ ] Create multi-stream synchronization architecture diagram

**Proof-of-Concept Code:**
- [ ] LSL + SCPI instrument bridge (Python)
- [ ] RaptorQ data recovery example (.NET)
- [ ] Kafka telemetry producer (Python)
- [ ] Real-time dashboard (Grafana + OTLP)

**Integration Guides:**
- [ ] SCPI Instrument Control + LSL sink integration
- [ ] ScoreMachine + RaptorQ backup strategy
- [ ] Passive Radar SDR + multi-receiver sync
- [ ] DevOps Cluster + stream processing pipelines

**Benchmarks & Performance:**
- [ ] RaptorQ overhead vs alternatives
- [ ] Kafka latency vs NATS vs Pulsar
- [ ] Storage format compression ratios
- [ ] Time-series DB cardinality performance

**Deployment & Production:**
- [ ] Hardware requirements guide
- [ ] Configuration templates
- [ ] Troubleshooting guide
- [ ] Compliance checklist (FDA 21 CFR Part 11 for clinical use)

---

## Recent Archives

- [Repository Restructure - January 2026](changes/repository-restructure-2026-01.md) - Documentation reorganization and project structure improvements (10 tasks, 2026-01-07)

---

*Last updated: 2026-01-16 15:30*
*Last cleaned: 2026-01-07*

## Session Discoveries (2026-01-16)

### Index Protocol Implementation
- Created INDEX_PROTOCOL.md for standardizing directory indexes
- Identified 8 top-level directories needing README.md indexes
- Follows pattern: Executive Summary → TOC → Content → Footer

### Synchronized Telemetry Streaming Research
- Phase 1 (research) completed: 40+ standards, 100+ resources documented
- Phase 2 work identified: PlantUML diagrams, PoC code, integration guides, benchmarks, deployment
- 24 subtasks added to track Phase 2 implementation
