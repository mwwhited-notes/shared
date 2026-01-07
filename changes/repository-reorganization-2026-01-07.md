# Changelog

Recent changes and work completed on this repository.

## 2026-01-07 Session 2

### Completed
- [x] Renamed diagrams-and-patterns directory structure to lowercase-with-hyphens convention
  - Renamed `Examples/` → `examples/`
  - Renamed `Designs/` → `designs/`
  - Updated `diagrams-and-patterns/README.md` file references
- [x] Reorganized AI ML Stuff directory from Notes/
  - Created new `projects/ai-ml-research/` project for AI/ML research papers and notes
  - Moved `LocalitySensitiveHashing.md` → `projects/vector-search-sqlserver/`
  - Moved `vectorsearch.md` → `projects/vector-search-sqlserver/`
  - Moved `AI ML Papers.md`, `ai notes.md`, `Anti-AI.md` → `projects/ai-ml-research/`
  - Removed empty `Notes/software/AI ML Stuff/` directory
- [x] Updated documentation cross-references
  - Updated `projects/README.md` - Added AI/ML Research project (18 total projects)
  - Updated `projects/vector-search-sqlserver/README.md` - Fixed research notes file paths
  - Updated `Notes/README.md` - Documented AI ML Stuff move

## 2026-01-07 Session 1

### Completed
- [x] Created comprehensive projects index (`projects/README.md`)
  - 18 total projects with quick reference table
  - Projects organized by category
  - Status summary and cross-references
- [x] Created/updated project documentation
  - SBC Cluster (8× ARM boards)
  - Radex One Protocol Reverse Engineering
  - Favero Fencing Scoring System
  - DRL/DTL Logic Boards (reference)
  - Vector Search SQL Server (completed)
  - Gadget Kit Ideas
  - Streaming Channel Planning
  - Passive Radar SDR System
  - Self-Hosted Git Server
- [x] Reorganized Notes/ directory - moved project-specific files to respective projects
  - 74-181 ALU notes → SAP-1 Computer
  - 3D Printer notes → Test Equipment/velleman-k8200
  - FPAA research → Analog Computer Experiments
  - Xilinx FIFO notes → FPGA CPU Design
  - Kubernetes notes → DevOps Playground Cluster
  - HomeSeer backup → Home Automation
  - Favero documentation → Favero Fencing System project
  - Radex One notes → Radex One Protocol project
  - NeTV notes → Programmable Devices/netv-fpga
  - Duet3 notes → Test Equipment/velleman-k8200
  - Linux Serial/USB HID notes → respective projects
- [x] Moved DiagramsAndPatterns to top level
  - `Notes/software/DiagramsAndPatterns/` → `/diagrams-and-patterns/`
  - Renamed directories: ArchitecturePatterns, DesignPatterns, Templates
  - Renamed files: FutureIdeas.md, SuggestedGuidelines.md, TableOfContents.md
- [x] Moved files from root to projects
  - `HammingDistances/` → `projects/vector-search-sqlserver/`
  - `Semantic Search/` → `projects/vector-search-sqlserver/`
  - `docker-cluster.md` → `projects/devops-playground-cluster/`
- [x] Added devices to Device Lab
  - Microsoft HoloLens v1 Developer Edition
  - Xbox 360 Kinect (with PC adapter)
  - Xbox One Kinect
  - Microsoft Surface Book 2 15" (moved from Camera Collection)
- [x] Added NeTV FPGA to Programmable Devices inventory
  - Created comprehensive documentation
  - Added to programmable devices index
- [x] Updated project statuses
  - ATtiny2313 LED Clock → Completed
  - MM-8000K Trainer UI → On Hold
  - DIY TrekPak Dividers → Reference/As Needed
  - Favero Fencing System → Completed
- [x] Created priority infrastructure tasks in TODO.md
  - Deploy Gitea on PR4100
  - Set up Docker on PR4100
  - Fix PR4100 Windows credential issue
- [x] Clarified infrastructure architecture
  - PR4100: Production services (always-on, stable)
  - DevOps Playground Cluster: Experimental (high power, can break)
  - SBC Cluster: ARM learning platform
- [x] Updated documentation cross-references
  - CLAUDE.md
  - Notes/README.md
  - projects/README.md
  - Device Lab/readme.md
  - Programmable Devices/readme.md
  - Multiple project READMEs

---

*For older changes, see git commit history.*
