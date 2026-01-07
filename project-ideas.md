# Project Ideas

Personal project backlog with notes on progress and equipment.

---

## Active / In Progress

* **FPGA CPU Design** - Designing my own CPU/computer (and learn system verilog) [I have most of the ALU and a text graphics engine from a few years ago. Use Arty A7-100.] → [projects/fpga-cpu-design/](projects/fpga-cpu-design/)
* **ATtiny2313 Clock** - Build out that clock (attiny2313) [the new LED screen showed up so I can solder it up now and I need to tweak the counter to see if I can get it to keep time better.] This project was mostly about building something semiuseful with an ATTiny and learning how to built out the ISP (In-circuit Serial Programmer) interface → [projects/attiny2313-clock/](projects/attiny2313-clock/)
* **SCPI Instrument Control** - Play around with SCPI (standard commands for programmable instruments) to control the test equipment on my bench and probably write my own VISA driver for .Net Core (might also build a RS-232/ethernet gateway or USB them into a raspberry pi/beagle bone black) [have HP 34401A, Rigol DM3058E, Rigol DG1022, Korad supplies] → [projects/scpi-instrument-control/](projects/scpi-instrument-control/)
* **Analog Computer Experiments** - Build out an analog computer/integrator (opamps for math because why not) [Have Anabrid THAT now!] → [projects/analog-computer-experiments/](projects/analog-computer-experiments/)
* **MM-8000K Trainer UI** - Build out a UI for an Intel 8085 trainer [MM-8000K hardware + MM8000 emulator on GitHub] → [projects/mm8000-trainer-ui/](projects/mm8000-trainer-ui/)
* **Zynq SoC Exploration** - Play around with SoC (system on a chip) based on the Xilinx Zynq Z7 [Have Arty Z7-20] → [projects/zynq-soc-exploration/](projects/zynq-soc-exploration/)
* **DevOps Playground Cluster** - Building multi-node home lab from Reduced BigRig (FX-9590) + Server (FX-8350) for learning Docker, Kubernetes, Slurm, and other DevOps/development tools → [Device Lab/projects/docker-cluster.md](Device%20Lab/projects/docker-cluster.md)
* **Home Automation Migration** - Migrating from HomeSeer to Home Assistant, repurposing Galaxy Tab4 Nook as dashboard → [projects/home-automation/](projects/home-automation/)

---

## Backlog

### Vintage Computing & Retro

* write a simple game for the NES and Apple II (program in 6502 assembly) [have NESMaker PCBs, Apple IIc, Apple IIgs]
* archive floppy disk collection with Greaseweazle V4.1 [have Apple II 5.25", Apple IIgs 3.5", TI-99/4A disks]
* build Multicomp Z80 CP/M system on EP2C5-DB [have Multicomp kit, Grant Searle designs available]
* build Multicomp 6502 system with BASIC [good prep for Apple II projects]
* build Multicomp 6809 Flex/OS-9 system [learn another 8-bit architecture]
* Gigatron TTL expansion or game development [have Gigatron TTL computer]
* TI-99/4A cartridge development [have TI-99/4A with speech synthesizer]

### FPGA & CPU Design

* 8085 soft core on FPGA [have MM-8000K as reference, Arty A7]
* 65C816 soft core (Apple IIgs compatible) [would enable IIgs clone]
* TMS9900 soft core (TI-99/4A compatible) [would enable TI-99 clone]
* VGA/HDMI framebuffer controller [needed for retro cores]
* custom ISA CPU design [building on ALU work]

### Protocol Bridges & Interfaces

* GPIB/IEEE-488 USB adapter [for HP 34401A and other GPIB instruments, builds on DeviceBridge work]
* **LXI Bridge for Test Equipment** - Web interface for controlling/viewing all bench equipment + IP socket for SCPI access. Note: HP 34401A, Rigol DM3058E, and DG1022 do NOT have native LXI - this would add network capability to legacy instruments. [ESP32/Pi gateway]
* Centronics-to-WiFi print server [builds on DeviceBridge parallel port work]
* H4n recorder remote interface [have protocol documented]
* LANC camera controller expansion [have LANC work in EmbeddedBakery]

### Wireless & IoT

* XBee mesh sensor network with dashboard [have XBee modules + XBIB-U-DEV]
* XBee-to-MQTT gateway [ESP32 + XBee]
* battery-powered remote sensor nodes [ATtiny + XBee]
* ESP32 home automation projects [have Inland ESP32, ESP8266 modules]

### Analog & Mixed Signal

* Lorenz attractor on The Analog Thing [chaos visualization]
* predator-prey ecosystem simulation [classic analog computing demo]
* hybrid analog-digital system [THAT + STM32 interface]
* control system modeling [PID loops, feedback systems]

### Workshop Organization

* **DIY TrekPak-Style Dividers** - Custom drawer and case dividers using corrugated plastic panels, U-shaped hair pins (as locking pins), EVA foam, and felt tape. DIY alternative to [Pelican TrekPak](https://www.pelican.com/us/en/discover/trekpak). → [projects/diy-trekpak-dividers/](projects/diy-trekpak-dividers/)

### Learning & Exploration

* play around more with diode logic (working though this in combination with trying to reverse engineer programming some old PAL chips helped me understand how "high voltage" programmers work as well as ROM, SRAM, and more about combinational logic)
* D2-1 line follower robot enhancements [add MCU to analog base]
* Velleman K8055 automation projects [USB I/O board for PC control]
* build out multi-axis hand controller to work with oculus/hololens
* design and build a handheld/bench calculator that will also function as a simple I/O interface for parallel and serial interfaces

### DevOps & Infrastructure

*Using DevOps Playground cluster (Reduced BigRig + Server FX machines) and PR4100 NAS.*

* **Self-hosted Git Server** - Options: (1) bare git repos on PR4100 SMB/NFS share, or (2) Gitea/Gogs/GitLab Docker container on PR4100. Container approach adds web UI, issue tracking, CI integration. [PR4100 has Docker support, Intel N3710 CPU]
* k3s Kubernetes cluster deployment [lightweight K8s for home lab]
* Docker Swarm multi-node setup [built-in orchestration]
* Slurm HPC workload manager [job scheduling, batch processing]
* CI/CD pipeline deployment [Jenkins, GitLab Runner, or Drone]
* GitOps workflow with ArgoCD or Flux [declarative deployments]
* Ansible playbooks for cluster management [IaC learning]
* Terraform infrastructure as code practice
* Prometheus + Grafana monitoring stack [observability]
* GPU compute experiments on R9 290s [OpenCL workloads]
* Chaos engineering with Litmus [resilience testing]

### Home Automation

*Using home-automation project, Device Lab tablets, and cluster.*

* Home Assistant deployment on cluster or dedicated Pi
* Z-Wave device migration from HomeSeer [have Z-Net bridge, Z-Stick]
* Galaxy Tab4 Nook LineageOS flash + dashboard setup
* Fire HD Google Play + kiosk setup [secondary display]
* Multi-protocol hub (Z-Wave + Zigbee + Matter)
* Self-hosted remote access via VPN or Tailscale [no cloud]
* Local voice control without cloud services

### Mobile Device Repurposing

*Using Device Lab mobile devices.*

* PSVita CFW + emulation station [retro gaming]
* iPad Mini jailbreak + media player setup
* Fire HD as kitchen recipe display
* iPhone 2G jailbreak + retro iOS exploration
* Tablet-based security camera / baby monitor

---

## Equipment Enabling New Projects

Recent inventory additions that enable new project categories:

| Equipment | Projects Enabled |
|-----------|------------------|
| Greaseweazle V4.1 | Floppy disk archival, vintage disk preservation |
| Multicomp EP2C5-DB | Z80/6502/6809 retro computing, CP/M, BASIC |
| Anabrid THAT | Analog computing, chaos systems, hybrid digital |
| XBee modules + XBIB-U-DEV | Mesh networking, remote sensors |
| Gigatron TTL | TTL computing, expansion modules |
| D2-1 Line Follower | Robot enhancement, sensor fusion |
| **DevOps Playground Cluster** | Docker, Kubernetes, Slurm, CI/CD, monitoring |
| PowerSpec G474 (160GB RAM) | Heavy development, VMs, photo editing |
| WD My Cloud PR4100 | NAS services, Docker host, media server |
| Galaxy Tab4 Nook | Home automation dashboard, kiosk display |
| Sony PSVita | Retro gaming, emulation, homebrew |
| Amazon Fire HD | Smart display, kiosk, Google Play hacking |

---

## Cross-References

### Project Directories

- [projects/](projects/) - Active project documentation
  - [fpga-cpu-design/](projects/fpga-cpu-design/) - Custom CPU in SystemVerilog
  - [attiny2313-clock/](projects/attiny2313-clock/) - ATtiny LED clock
  - [scpi-instrument-control/](projects/scpi-instrument-control/) - Test equipment automation
  - [analog-computer-experiments/](projects/analog-computer-experiments/) - Anabrid THAT projects
  - [mm8000-trainer-ui/](projects/mm8000-trainer-ui/) - Intel 8085 trainer interface
  - [zynq-soc-exploration/](projects/zynq-soc-exploration/) - Zynq ARM+FPGA SoC
  - [diy-trekpak-dividers/](projects/diy-trekpak-dividers/) - Workshop organization
  - [home-automation/](projects/home-automation/) - Home Assistant migration

### Device Lab Projects

- [Device Lab/](Device%20Lab/) - Full computing device inventory
- [Device Lab/projects/docker-cluster.md](Device%20Lab/projects/docker-cluster.md) - DevOps Playground cluster

### Equipment & Capabilities

- [workshop-capabilities.md](workshop-capabilities.md) - Full equipment summary

---

*Last updated: January 2026*
