# TODO

> **Session Reminder:** Check at least once per session if new projects have been added externally to `projects/` directory or `projects/project-ideas.md` to ensure awareness of external updates.

## Active Tasks

### Broken Link Cleanup (session 2026-09-15, done)
Went from 379 raw hits to 103, all of which are now accounted for: protocol template
placeholders, intentional external-doc mirror self-links (BEP52/CloudEvents spec copies), and
two genuine content gaps flagged with in-file notes rather than fabricated (see below) instead
of fixed:
- `projects/ai-ml-docker-orchestration/README.md` - describes `compositions/`/`services/`
  subdirs that don't exist on disk despite being marked "Production-Ready"; likely migrated to
  `code/public/containers` during the Docker Containers Collection consolidation - needs
  verifying, not just relinking
- `projects/vector-search-sqlserver/docs/` - links to `sql-implementation.md`,
  `csharp-implementation.md`, `examples/example-2-async-processing.md`,
  `examples/example-3-hybrid-search.md` that were apparently never written

Fixed: network-diagram.md, readme.md (equipment/Notes sections rewritten to match the actual
current structure), the synchronized-telemetry-streaming-research reference/storage/streaming/
transfer cluster, AnalogComputers/README.md, Notes/README.md, projects/README.md,
diagrams-and-patterns casing, ~15 individual project READMEs' equipment-collection links, and
stale `.claude/analysis/{repo}/{hash}.md` links (EmbeddedBakery, MM8000, DeviceBridge current;
BuildFirstOnce/YearOfCode2024 analyses no longer exist, noted as removed).

### Protocol/Interface Project Scan (session 2026-09-15)
- [ ] Review shared/projects/ for serial, network-protocol, and interface work that could move
  to/inform C:\repo\oobdev\dev-term\ (candidates so far: scpi-instrument-control, scoremachine
  (Favero/Zoom H4N serial protocols), radex-one-protocol-reverse-engineering, passive-radar-sdr,
  windows-usb-passthough) - not yet started

### Documentation
- [ ] Review and update workshop-capabilities.md with new projects
- [ ] Consider adding project status tracking to projects/project-ideas.md
- [ ] Update personal-request files when Personal repository is available for data exchange

### Equipment & Tools
- [x] Personal responses received in `.personal/incoming/` (2026-01-17)
  - [x] test-equipment.md - 44 units documented (updated 2026-09-15: added Tektronix 2230 ×2, Rigol DG1022Z)
  - [x] tools-and-components.md - 100+ items documented
  - [x] device-lab.md - 40+ devices documented
  - [x] expansion-boards.md - 30+ boards documented
  - [x] programmable-devices.md - 37 boards documented
  - [x] vintage-computers.md - 4 systems documented
  - [x] books.md - 26 titles documented
  - [x] camera-collection.md - 75+ items documented
- [x] Updated workshop-capabilities.md to reference personal data
- [ ] Update individual project READMEs to link equipment references to personal data

### Infrastructure (Priority)
- [ ] **Deploy Gitea on PR4100** (see projects/self-hosted-git-server/)
- [ ] **Set up Docker on PR4100** for production services (Gitea, Nextcloud)
- [ ] Fix PR4100 Windows credential persistence issue (see Device Lab/network-storage/wd-mycloud-pr4100/windows-credential-fix.md)

### Reclaimed-Cell USB-C PD Pack
- [ ] Acquire programmable DC electronic load (e.g. ATORCH DL24/DL24P) - blocks all cell testing
- [ ] Acquire 18650-capable spot welder
- [ ] Discharge-test and sort accumulated salvaged cells (capacity + IR)
- [ ] Decide final S/P layout once matched-group yield is known, then order exact BMS/boost module part numbers

### Offline Mapping, Search & Routing System
- [ ] Stand up OsmAnd vs. Organic Maps side-by-side as the Phase 0 fast-path baseline
- [ ] Evaluate BRouter vs. Valhalla against the actual need (a van height/weight routing profile)
- [ ] Check iOverlander and Campendium for an official data export/API before considering any scraping
- [ ] Decide home compute target (DevOps Playground Cluster vs. a dedicated SBC) and whether it shares infra with Local Docker Registry
- [ ] Scope Phase 1 data ingestion down to a single test region/corridor before generalizing

### THAT Hybrid Controller (THAThc)
- [ ] Source or build HYBRID port piggyback/breakout board
- [ ] Wire Arduino Mega 2560 per HYBRID port pinout
- [ ] Install THAThc library, verify shell commands against a known circuit on THAT
- [ ] Script first automated `rep` run and confirm captured ADC data

### Home NVR System
- [ ] Confirm Wyze Cam Pan RTSP firmware support (official or community)
- [ ] Decide shared Docker host with home-automation (PR4100 vs. DevOps Playground Cluster)
- [ ] **Verify PR4100's Pentium N3710 supports AVX2** before assuming it can host Frigate
- [ ] Stand up Frigate against one camera as proof of concept
- [ ] Wire first Home Assistant automation from a Frigate detection event

### Serger Timing Repair (Singer 14CG754)
- [ ] Watch Sewing Mastery episode 17 (Cleaning & Oiling) for this exact machine
- [ ] Try clean + oil + rethread before attempting timing adjustments
- [ ] If needed, do functional/visual timing adjustment (no numeric service manual exists for this model) - hand-crank, watch clearance, don't force it
- [ ] If it won't time up reliably, take to a shop rather than forcing further adjustment

### JWS/JWT From Scratch
- [ ] Implement base64url encode/decode against RFC 7515 test vectors
- [ ] Implement HS256 sign + verify, cross-check against System.IdentityModel.Tokens.Jwt output

---

## Recent Archives

- [Synchronized Telemetry Streaming - Phase 2](changes/synchronized-telemetry-streaming-phase2-2026-01.md) - 52 files delivered (diagrams, code, guides, benchmarks), all syntax verified (2026-01-16)
- [Repository Restructure - January 2026](changes/repository-restructure-2026-01.md) - Documentation reorganization and project structure improvements (10 tasks, 2026-01-07)

---

*Last updated: 2026-07-24*
*Last cleaned: 2026-01-17*
*Last reorganized: 2026-01-17 - Integrated personal data responses into workshop-capabilities.md*
