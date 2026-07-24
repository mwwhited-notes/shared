# Home NVR System (Self-Hosted, Local-Only)

Replace cloud-dependent camera apps with a self-hosted, local-only NVR — AI object detection,
Home Assistant integration, no subscriptions, no third-party servers.

## Overview

Consumer security cameras (including the 2 owned [Wyze Cam Pan 1080p units](../../.personal/incoming/device-lab.md))
default to cloud recording and cloud-gated features. This project evaluates open-source,
self-hosted NVR software that ingests RTSP camera streams directly, does local AI-based object
detection, and integrates with the existing [Home Assistant](../home-automation/) deployment for
detection-triggered automations (e.g. porch motion → turn on the spotlight).

This follows the same self-hosted/no-subscription requirements already set for
[home-automation](../home-automation/) (100% local control, no cloud dependency) and would likely
share deployment infrastructure with that project — the WD My Cloud PR4100 or DevOps Playground
Cluster are both already under consideration as the Home Assistant host.

**Core requirements carried over from home-automation:**
- Local-only: no footage or metadata leaves the network
- No subscriptions
- Integrates with Home Assistant for automations
- Should not require replacing existing cameras if they can be made to speak RTSP locally

## Candidate Software

### Frigate (primary candidate)

Docker-based open-source NVR with AI object detection, described in
["I replaced a dedicated NVR with Frigate" (XDA Developers)](https://www.xda-developers.com/replaced-a-dedicated-nvr-with-frigate/).

- Runs as a Docker container — deployable on Synology/PR4100-class NAS or a dedicated box, same as
  the Home Assistant deployment options already being weighed
- Ingests RTSP streams from "almost any IP camera" — no brand lock-in
- AI object detection with configurable zones/rules; works with CPU-only detection but strongly
  benefits from a GPU or Coral TPU expansion card for real-time performance
- Home Assistant integration (add-on or Docker) is the standout feature per the article — camera
  detections become automation triggers (motion → lights, etc.), directly matching this project's
  motivation
- Config is YAML-based (cameras, connections, detection zones/rules) — documented, but requires
  some upfront reading
- Author's stated pain points with the dedicated NVR it replaced: limited camera compatibility,
  outdated web UI, storage/retention limits, per-camera count caps, no Home Assistant integration,
  proprietary recording formats — all directly avoided by this approach

### Viseron (alternative candidate)

Self-hosted local-only NVR + AI computer vision software: [viseron.netlify.app](https://viseron.netlify.app/)

- Broader AI feature set than Frigate out of the box: object detection/tracking, face recognition
  (known/unknown faces), license plate recognition, image classification, plus motion detection
- Hardware acceleration: CUDA (NVIDIA), Google Coral EdgeTPU, Jetson Nano, others
- WebRTC low-latency live viewing; continuous 24/7 recording with retention policies
- Docker deployment: `docker run` + edit `config.yaml` via the built-in web editor
- Claims to be "camera agnostic" — works with any camera brand/type (specific protocol support not
  confirmed during research; verify RTSP support for the Wyze cams specifically before committing)
- No confirmed Home Assistant integration found during research (Frigate's HA add-on story is more
  established) — worth checking current Viseron docs directly before choosing between the two

### Frigate — hardware requirements (from official docs)

Per [frigate.video](https://frigate.video/) and [docs.frigate.video/frigate/hardware/](https://docs.frigate.video/frigate/hardware/):

- Frigate is free/open-source (a paid "Frigate+" tier exists for custom detection models — not
  required to get started); does 100+ detections/sec with an accelerator, zone-based detection
  refinement, and integrates with Home Assistant, OpenHAB, Node-RED, and MQTT generally
- **Server CPU requirement: Intel CPU with AVX + AVX2, capable of running Debian Linux.**
  **This needs checking against the PR4100 before assuming it's a viable Frigate host** — the
  PR4100 uses an Intel Pentium N3710 (Braswell/Airmont, ~2016). Braswell-generation Atom cores are
  widely documented as lacking AVX2 (AVX2 didn't reach Atom-derived low-power cores until Goldmont
  Plus/Tremont generations, years later) — Intel's own spec page returned a 403 during research so
  this couldn't be directly confirmed, but if it holds, **the PR4100 cannot run Frigate's
  detection pipeline** and a different host (DevOps Playground Cluster, or a small dedicated Intel
  N100 box like the recommended Beelink EQ13) would be required instead. Verify before committing
  to PR4100 as the shared Docker host for both this project and Home Assistant.
- Recommended reference hardware: Beelink EQ13 (N100, dual NIC), Intel 1120P, Intel 125H (has NPU)
- AI accelerators: Coral TPU is **no longer the recommended pick for new installs** (Frigate's docs
  now favor Hailo-8/8L M.2 modules, ~7-11ms inference); Coral still fine for low-power/small setups
- GPU acceleration also available via Intel OpenVINO (6th gen+ iGPU or Arc), NVIDIA (CUDA 12.x,
  driver 545+), AMD ROCm, or Apple Silicon — likely moot unless the eventual host has one of these
- **Camera brand guidance:** Frigate's docs recommend Dahua, Hikvision, or Amcrest (rebranded
  Dahua) — Wyze is not in their recommended list. Explicitly **avoid 4K+ Reolink models**. Prefer
  wired cameras — Frigate's docs call WiFi cameras "less reliable, cause connection loss." This is
  a data point against relying solely on the existing Wyze Cam Pan units long-term, even once RTSP
  is confirmed working on them.

### Wyze Cam local RTSP (camera-side prerequisite)

The 2 owned Wyze Cam Pan 1080p units are cloud-locked by default. Wyze has historically shipped an
official RTSP firmware add-on for select models, and there's a well-known community
("wz_mini_hacks"-style) firmware route for models Wyze doesn't officially support. **Needs
verification before building anything else**: confirm the specific Wyze Cam Pan hardware revision
owned supports either the official RTSP firmware or a community alternative — this is the
prerequisite that makes either Frigate or Viseron usable with existing cameras instead of buying
new ones.

### Nest Cam local recording (reference, unverified)

[LinusTechTips forum: "Record Nest Cam Locally, FREE, in under 10 steps"](https://linustechtips.com/topic/1048515-record-nest-cam-locally-free-in-under-10-steps/)
was flagged as a possible reference for pulling a local feed off a Nest camera instead of relying
on Google's cloud service. **The page returned HTTP 403 on every fetch attempt during research —
content could not be verified.** Only relevant if a Nest camera is in play; if the camera plan
stays Wyze-only, this can be dropped. Open the thread directly before relying on it.

## Materials

| Material | Purpose | Source | Notes |
|----------|---------|--------|-------|
| Wyze Cam Pan 1080p (×2) | Camera source | Already owned ([device lab inventory](../../.personal/incoming/device-lab.md)) | Needs RTSP-capable firmware confirmed first |
| Docker host (PR4100 or DevOps Playground Cluster) | Runs Frigate/Viseron container | Shared with [home-automation](../home-automation/) | Same infra decision as Home Assistant host |
| GPU or Coral EdgeTPU (optional) | Real-time AI detection acceleration | To source if CPU-only detection proves too slow | Not required to get started |
| Storage | Video retention | PR4100 NAS storage | Capacity budget depends on camera count/resolution/retention policy |

## Construction Method / Build Steps

1. Confirm Wyze Cam Pan RTSP capability (official firmware or community alternative) — this gates
   everything else
2. Decide deployment host — align with whatever [home-automation](../home-automation/) settles on
   (PR4100 vs. DevOps Playground Cluster) to avoid running two separate always-on Docker hosts
3. Stand up Frigate first (better-documented Home Assistant integration) via Docker, point it at
   one Wyze camera's RTSP stream, verify live view and recording before adding detection
4. Enable object detection (CPU-only first), evaluate whether detection is fast enough or whether
   a Coral TPU is needed
5. Wire Frigate → Home Assistant so a camera detection can trigger a real automation (e.g. porch
   motion → light), matching the source article's stated killer feature
6. Once Frigate is working, optionally stand up Viseron side-by-side (different Docker
   port/container) to compare its face-recognition/license-plate features and WebRTC viewing
   before deciding which one to keep long-term
7. If a second camera source becomes relevant (e.g. a Nest cam), revisit the LTT thread above and
   verify its steps directly rather than relying on the unfetched summary here

## Key Features

- Local-only recording and AI detection — no footage leaves the network, no subscription
- Home Assistant automation triggers from camera detections
- No camera brand lock-in once a camera can speak RTSP
- Shares Docker infrastructure with the home-automation project instead of standing up new hardware

## Advantages Over Dedicated/Cloud NVR

| Feature | Frigate/Viseron (self-hosted) | Dedicated NVR / Cloud Cam App |
|---------|-------------------------------|-------------------------------|
| Camera compatibility | Any RTSP-capable camera | Often locked to matching brand |
| Home Assistant integration | Native (Frigate) | Usually none |
| Recording format | Open, standard | Often proprietary |
| Cost | One-time hardware, no subscription | Subscription or capacity-limited hardware |
| Data location | Local only | Third-party cloud (unless purely local NVR) |

## Use Cases

- Porch/entry motion detection triggering exterior lighting via Home Assistant
- Local-only recorded footage for the existing Wyze cameras without a Wyze cloud subscription
- Future camera additions (Nest or otherwise) folded into the same local pipeline instead of a
  separate cloud app per camera brand

## Project Status

**Status:** Planning

**Next Steps:**
1. **Verify PR4100's Pentium N3710 actually supports AVX2** (`cat /proc/cpuinfo | grep avx2` if
   SSH'd in) before assuming it can host Frigate — may rule it out as the shared host
2. Verify Wyze Cam Pan RTSP firmware support for the specific units owned
3. Decide shared Docker host with [home-automation](../home-automation/) informed by (1)
4. Stand up Frigate against one camera as a proof of concept
5. Evaluate CPU-only detection performance before deciding on a Hailo-8/8L or Coral accelerator
6. Wire up first Home Assistant automation from a Frigate detection event
7. Side-by-side evaluate Viseron if Frigate's feature set proves insufficient

## References

- [I replaced a dedicated NVR with Frigate - XDA Developers](https://www.xda-developers.com/replaced-a-dedicated-nvr-with-frigate/)
- [Frigate - official site](https://frigate.video/)
- [Frigate hardware requirements - official docs](https://docs.frigate.video/frigate/hardware/)
- [Viseron - self-hosted local NVR + AI computer vision](https://viseron.netlify.app/)
- [Record Nest Cam Locally, FREE, in under 10 steps - LinusTechTips forum](https://linustechtips.com/topic/1048515-record-nest-cam-locally-free-in-under-10-steps/) (unverified — 403 on fetch)
- Cross-reference: [home-automation/](../home-automation/) - shares Docker host and local-only/no-subscription requirements
- Cross-reference: [Device Lab inventory](../../.personal/incoming/device-lab.md) - existing Wyze Cam Pan units

---

*Last updated: 2026-07-24*
