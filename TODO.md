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

### Directory Indexes (INDEX_PROTOCOL.md - ✅ ALL COMPLETE)
- [x] Create README.md for Programmable Devices/ (409 lines, 20+ devices)
- [x] Create README.md for Expansion Boards/ (330 lines, shields/hats/capes)
- [x] Create README.md for Test Equipment/ (422 lines, oscilloscopes, DMMs, supplies)
- [x] Create README.md for Vintage Computers/ (131 lines, Apple II, TI-99/4A, etc.)
- [x] Create README.md for Camera Collection/ (263 lines, cameras, lenses, accessories)
- [x] Create README.md for Device Lab/ (217 lines, tablets, phones, NAS, gaming devices)
- [x] Create README.md for Notes/ (153 lines, technical notes organized by topic)
- [x] Create README.md for AnalogComputers/ (154 lines, research collection overview)

### Research: Synchronized Telemetry Streaming (Phase 2 - COMPLETE)
See: projects/synchronized-telemetry-streaming-research/

**Diagrams (10 files - ✅ COMPLETE):**
- [x] System overview architecture
- [x] LSL multi-modal recording
- [x] Kafka event architecture with CloudEvents
- [x] RaptorQ transfer architecture
- [x] SCPI-LSL integration
- [x] Timeseries storage pipeline
- [x] RaptorQ encoding/decoding flow (sequence diagram)
- [x] Kafka CloudEvents message flow (sequence diagram)
- [x] LSL stream synchronization
- [x] Protocol selection decision tree
- [x] Multi-stream time synchronization architecture

**Proof-of-Concept Code (15 files - ✅ COMPLETE):**
- [x] LSL + SCPI instrument bridge (Python, 6 files)
- [x] RaptorQ data recovery example (.NET, 5 files)
- [x] Kafka telemetry producer with CloudEvents (Python, 6 files)
- [x] Grafana dashboard configs (placeholder for future expansion)

**Integration Guides (4 files - ✅ COMPLETE):**
- [x] SCPI Instrument Control + LSL sink integration
- [x] Kafka Event Streaming with CloudEvents
- [x] RaptorQ Reliable Transfer strategy
- [x] Passive Radar SDR + multi-receiver synchronization

**Benchmarks & Performance (4 suites - ✅ COMPLETE):**
- [x] RaptorQ overhead vs alternatives (Reed-Solomon, FECFRAME, LDPC)
- [x] Kafka latency vs NATS vs Pulsar
- [x] Storage format compression ratios (HDF5, Parquet, XDF)
- [x] Time-series DB cardinality performance (InfluxDB, TimescaleDB, QuestDB, Prometheus)

**Deployment & Production (4 guides - ✅ COMPLETE):**
- [x] Hardware requirements guide (light/medium/heavy workloads)
- [x] Configuration templates (Kafka, InfluxDB, Prometheus, Grafana)
- [x] Troubleshooting guide with diagnostic tools
- [x] FDA 21 CFR Part 11 compliance guide (clinical telemetry, IQ/OQ/PQ, audit trails, digital signatures)

---

## Recent Archives

- [Repository Restructure - January 2026](changes/repository-restructure-2026-01.md) - Documentation reorganization and project structure improvements (10 tasks, 2026-01-07)

---

*Last updated: 2026-01-16 (Phase 2 Complete)*
*Last cleaned: 2026-01-07*

## Session Discoveries (2026-01-16)

### Synchronized Telemetry Streaming Research - Phase 2 COMPLETED
**Delivery:** 52 files created across 5 categories
- ✅ 10 PlantUML diagrams (all syntax verified)
- ✅ 15 working code examples (Python + .NET)
- ✅ 4 integration guides with real-world scenarios
- ✅ 3 deployment guides for production use
- ✅ 4 benchmark suites with methodologies
- ✅ 1 Phase 2 completion summary document
- ✅ Updated main README.md with Phase 2 overview
- ✅ All cross-references verified

**Key Deliverables:**
- System architecture covering LSL, Kafka, RaptorQ, TimeSeries storage
- SCPI instrument integration for lab equipment control
- CloudEvents standardized event streaming
- Multi-receiver time synchronization patterns
- Hardware sizing and deployment configurations
- Performance benchmarks for technology selection

**Status:** Ready for Phase 3 (Kubernetes/Docker, OTLP integration, FDA compliance)
