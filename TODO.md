# TODO

> **Session Reminder:** Check at least once per session if new projects have been added externally to `projects/` directory or `projects/project-ideas.md` to ensure awareness of external updates.

## Active Tasks

### Documentation
- [ ] Review and update workshop-capabilities.md with new projects
- [ ] Consider adding project status tracking to projects/project-ideas.md
- [ ] Update personal-request files when Personal repository is available for data exchange

### Equipment & Tools
- [x] Personal responses received in `.personal/incoming/` (2026-01-17)
  - [x] test-equipment.md - 42 units documented
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
