# Project Ideas

Project backlog for future development. Once a project has its own directory in `projects/`, it's removed from this file.

**See also:** [Projects Index (README.md)](README.md) - Active projects organized by category

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

### Learning & Exploration

* play around more with diode logic (working though this in combination with trying to reverse engineer programming some old PAL chips helped me understand how "high voltage" programmers work as well as ROM, SRAM, and more about combinational logic)
* D2-1 line follower robot enhancements [add MCU to analog base]
* Velleman K8055 automation projects [USB I/O board for PC control]
* build out multi-axis hand controller to work with oculus/hololens
* design and build a handheld/bench calculator that will also function as a simple I/O interface for parallel and serial interfaces

### DevOps & Infrastructure

*Using DevOps Playground cluster (Reduced BigRig + Server FX machines) and PR4100 NAS. See [devops-playground-cluster/](devops-playground-cluster/) and [self-hosted-git-server/](self-hosted-git-server/).*

* k3s Kubernetes cluster deployment [lightweight K8s for home lab]
* Docker Swarm multi-node setup [built-in orchestration]
* Slurm HPC workload manager [job scheduling, batch processing, GPU resource management, container integration (Singularity), fair share/QOS policies, accounting with slurmdbd]
* CI/CD pipeline deployment [Jenkins, GitLab Runner, or Drone]
* GitOps workflow with ArgoCD or Flux [declarative deployments]
* Ansible playbooks for cluster management [IaC learning]
* Terraform infrastructure as code practice
* Prometheus + Grafana monitoring stack [observability]
* GPU compute experiments on R9 290s [OpenCL kernel development: matrix multiplication, image processing (2D convolution/filters), parallel reduction, performance optimization (memory coalescing, work-group design), .NET integration (Cloo/OpenTK.Compute), AMD vs NVIDIA comparison (R9 290 vs RTX 4070 Ti)]
* Chaos engineering with Litmus [resilience testing]

### Home Automation

*Using home-automation project, Device Lab tablets, and cluster. See [home-automation/](home-automation/).*

* Multi-protocol hub (Z-Wave + Zigbee + Matter)
* Local voice control without cloud services
* Advanced automation scenes and rules
* Energy monitoring and optimization

### Mobile Device Repurposing

*Using Device Lab mobile devices.*

* PSVita CFW + emulation station [retro gaming]
* iPad Mini jailbreak + media player setup
* Fire HD as kitchen recipe display
* iPhone 2G jailbreak + retro iOS exploration
* Tablet-based security camera / baby monitor

### Machine Learning & AI

* **Neural Network from Scratch** - Build neural network without ML frameworks using only NumPy/C#, implement backpropagation, gradient descent, activation functions (ReLU, sigmoid, softmax), train on MNIST or simple datasets, compare performance to framework implementations [understanding fundamentals, manual matrix operations]
* **Machine Learning Model Building** - End-to-end ML pipeline from data preprocessing to deployment, feature engineering, model selection (regression, decision trees, random forests, gradient boosting), hyperparameter tuning, cross-validation, model interpretability (SHAP, LIME), deploy as API endpoint [scikit-learn, XGBoost, practical ML]

### Software Architecture & APIs

* **SSO/Authentication Translation Proxy** - ASP.NET Core proxy service to translate between different authentication schemes (JWT, OAuth2, API keys, header keys, client certificates). Review JWT/OAuth2 key exchange protocols and build APIController + HttpClient-based gateway that can convert inbound auth to appropriate outbound auth based on known service contracts. [.NET Core, identity protocols, reverse proxy patterns]
* **gRPC Microservices** - Build production-ready gRPC services in .NET Core with Protocol Buffers (protobuf), implement all four communication patterns (unary, server streaming, client streaming, bidirectional), add interceptors for logging/metrics/auth, performance comparison vs REST, integrate with ASP.NET Core, deploy in Docker/Kubernetes [enterprise microservices, high-performance APIs]

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
| DevOps Playground Cluster | Docker, Kubernetes, Slurm, CI/CD, monitoring |
| PowerSpec G474 (160GB RAM) | Heavy development, VMs, photo editing |
| WD My Cloud PR4100 | NAS services, Docker host, media server |
| Galaxy Tab4 Nook | Home automation dashboard, kiosk display |
| Sony PSVita | Retro gaming, emulation, homebrew |
| Amazon Fire HD | Smart display, kiosk, Google Play hacking |

---

## Cross-References

### Active Projects

**All active projects have been moved to their own directories.**
See [Projects Index (README.md)](README.md) for the complete list of 12 active projects.

### Equipment & Capabilities

- [workshop-capabilities.md](../workshop-capabilities.md) - Full equipment summary and capabilities
- [Programmable Devices/](../Programmable%20Devices/) - FPGA, MCU, dev board inventory
- [Test Equipment/](../Test%20Equipment/) - Lab equipment inventory
- [Device Lab/](../Device%20Lab/) - Computing devices for hacking/tinkering
- [Vintage Computers/](../Vintage%20Computers/) - Retro computing hardware

---

*Last updated: 2026-01-07*
