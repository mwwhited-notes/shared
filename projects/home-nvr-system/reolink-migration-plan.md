# Home Camera System — Reolink Migration Plan

## Context

Replacing an existing Google Nest camera system (7 positions: doorbell, north/south side walks, alley, back fenced yard, back yard, parking lot) with Reolink, plus adding a second doorbell, a fence camera, and interior pet-monitoring cameras. All current Nest camera locations already have outlet power (WiFi cameras, not battery). Some locations do not yet have Ethernet run to them.

## Core requirements driving this build

- **Local-first, no forced cloud dependency.** Footage stored on-site; no vendor can revoke access to historical recordings.
- **No vendor lock-in risk.** Avoid a repeat of the Nest/Google "declared unsupported" scenario — prefer hardware that speaks open protocols (ONVIF/RTSP) so it can migrate to FOSS tooling (Frigate) later if needed.
- **Reduce WiFi load** by moving cameras to PoE wherever a cable run is feasible now; use mains-powered WiFi (not battery) cameras where cable isn't available yet.
- **Remote access without mandatory cloud relay** — local VPN preferred over vendor P2P.
- **Local webhook support** to integrate camera events with home-grown automation.
- **Pet-monitoring interior cameras** with an easy way to disable recording/live view when home.
- **Multi-device access**: iPhone, iPad, Windows, Mac, Samsung/Sony TVs, Apple TV.

## Architecture decisions

### NVR
**Reolink RLN16-410** — 16-channel PoE NVR, 4TB HDD, supports mixed PoE + plug-in WiFi + battery WiFi cameras simultaneously on one system. Chosen over the 8-channel RLN8-410 for headroom (9 exterior positions + doorbells + interior pet cams).

- Local storage only, no mandatory subscription.
- Supports HTTP webhooks per camera → can POST JSON directly to a self-hosted endpoint (n8n, Home Assistant, custom server) with no cloud relay involved.
- Live-view concurrency is capped (~2 full-res "main stream" viewers at once on typical models); recording is unaffected by this cap. A Frigate/go2rtc relay layer removes this limit entirely for multi-viewer/multi-TV access.

### Camera assignment by position

| Position | Camera | Power | Notes |
|---|---|---|---|
| Doorbell #1 | Video Doorbell WiFi | Existing power+button wiring | Direct Nest-equivalent swap — **not** the PoE model, since there's no Ethernet run to the door. Existing mechanical chime will be bypassed in favor of Reolink Chime (transformer must be 8–24V AC to work). |
| Doorbell #2 | Video Doorbell WiFi (or PoE if Ethernet is run) | Existing wiring or new PoE run | Same wiring caveat applies. |
| N/S side walks | RLC-810A (4K PoE, 2-pack) | PoE | Run cable if feasible; near-house positions are good PoE candidates. |
| Back fenced yard | RLC-810A (PoE) | PoE | |
| Back yard (open) | Duo 3 PoE (16MP dual-lens, 180° panoramic) | PoE | Wide coverage for open area. |
| Alley | E1 Outdoor (mains-powered WiFi, 3x zoom) | Existing outlet power | No cable yet — swap to PoE version later if a run becomes feasible. |
| Parking lot | E1 Outdoor (mains WiFi, zoom for plates) | Existing outlet power | Same upgrade path as alley. |
| Fence line | Duo 3 WiFi or E1 Outdoor (mains WiFi) | Existing outlet power | No battery/solar needed — power already present at all locations. |
| Interior (pet monitoring) | E1 Pro (indoor pan-tilt) | Outlet power | Has one-tap **Privacy Mode** to disable live view + recording without unplugging. |

**Important product nuance:** Reolink sells PoE and WiFi as separate SKUs of the same camera body, not a switchable mode. Converting a WiFi position to PoE later means buying the PoE version and swapping the unit — the mount can be reused.

### Networking

- **Reolink RLA-PS1** — 8-port PoE switch, powers all wired cameras/doorbells through the NVR.
- For locations without cable access: consider **powerline networking adapters** (Ethernet-over-electrical-wiring) at the existing outlet, feeding a small PoE injector — a way to get PoE reliability without fishing new cable, worth testing at one location first since quality depends on home wiring.
- Existing Nest mounting brackets can be reused via a **universal 1/4"-20 adapter mount** (Reolink cameras use the same standard thread as Nest/Ring/Arlo/etc.) — no new drilling needed at existing positions.

### Remote access / privacy

- **Local storage**: footage lives on the NVR's HDD; Reolink never holds a copy that could be subpoenaed independently of physical access to the device.
- **Default P2P app access** relays the *connection* through Reolink's servers (not the footage). For zero cloud touchpoint:
  - Disable UID/P2P remote access in NVR network settings.
  - Use a self-hosted VPN (WireGuard/Tailscale) into the home network for remote viewing instead of Reolink's relay/port-forwarding.
- **Webhooks**: configure per-camera under Settings > Surveillance > Push > Webhook. Fires a direct HTTP POST (JSON body) to a self-hosted URL — no cloud relay. Useful for wiring motion/person/vehicle events into Home Assistant, n8n, or a custom service.
- **Face recognition**: Reolink does not offer this by policy (only person/vehicle/pet *detection*, not identity recognition). If needed, add Frigate + a local face-recognition add-on (e.g. CompreFace, double-take) running on owned hardware — no cloud API calls.

### Vendor-independence / migration path

- Reolink PoE cameras speak ONVIF/RTSP and are widely used in Frigate setups — full migration to a self-hosted NVR (Frigate, Synology Surveillance Station, Blue Iris) is straightforward for PoE units.
- **Battery-powered WiFi cameras cannot do RTSP/ONVIF standalone** (power-saving requirement) — this is a physics limitation across all battery camera brands, not Reolink-specific. Since all positions in this build have outlet power, no battery cameras are used, avoiding this limitation entirely.
- Plug-in (mains) WiFi cameras generally do support RTSP/ONVIF (unlike battery models) but may need RTSP/ONVIF manually enabled in camera network settings (off by default on some models).

### Pet camera / "disable when home" behavior

Options, in order of effort:
1. Manual per-camera on/off toggle in Reolink app.
2. Built-in recording schedule (e.g., only record 9am–5pm) per camera.
3. **Geofencing automation** via Home Assistant: iPhone location (via Companion App or Shortcuts) triggers camera disable/enable on arrival/departure. Requires Home Assistant running on an always-on machine (spare Mac/PC, Mini PC, or Raspberry Pi).
4. Alternative to full disable: use motion zones to mask human-occupied areas (kitchen, hallway) and only trigger on pet-specific zones (bed, litter area).

### Multi-device access

- **iPhone/iPad**: Reolink App (iOS 11+).
- **Windows/Mac**: Reolink Client desktop app.
- **Apple TV / Samsung / Sony TVs**: no native Reolink app exists for any smart TV platform. Best path: run Home Assistant or Frigate's web dashboard, viewable in any TV's browser (or Home app on Apple TV via HA's tvOS integration), rather than chasing per-brand app support.

## Shopping list

| Item | Reolink (official) | Amazon |
|---|---|---|
| RLN16-410 (16-ch PoE NVR, 4TB) | [reolink.com](https://reolink.com/us/product/rln16-410/) | [amazon.com](https://www.amazon.com/Security-Recorder-Surveillance-Recording-RLN16-410/dp/B01DELNN82) |
| Video Doorbell PoE | [reolink.com](https://reolink.com/product/reolink-video-doorbell-poe/) | [amazon.com](https://www.amazon.com/REOLINK-Doorbell-Security-Diagonal-Detection/dp/B0B7S1HMPC) |
| Video Doorbell WiFi | [reolink.com](https://reolink.com/__/product/reolink-video-doorbell/) | [amazon.com](https://www.amazon.com/REOLINK-Doorbell-Detection-Storage-Assistant/dp/B0B7S3JSG7) |
| RLC-810A (4K PoE, 2-pack) | [reolink.com](https://reolink.com/product/rlc-810a/) | [amazon.com](https://www.amazon.com/REOLINK-Pack-Detection-Timelapse-Recording/dp/B08X6YQXRL) |
| Duo 3 PoE (16MP dual-lens) | [reolink.com](https://reolink.com/us/product/reolink-duo-3-poe/) | [amazon.com](https://www.amazon.com/REOLINK-Dual-Lens-Panoramic-Detection-Recording/dp/B0CM39K7CB) |
| E1 Outdoor (mains WiFi, PTZ, 3x zoom) | [reolink.com](https://reolink.com/product/e1-outdoor/) | [amazon.com](https://www.amazon.com/Reolink-Security-Tracking-Detection-Waterproof/dp/B09C8735S8) |
| E1 Pro (indoor pan-tilt, Privacy Mode) | [reolink.com](https://store.reolink.com/e1-series-cameras/) | [amazon.com](https://www.amazon.com/REOLINK-E1-Monitoring-Tracking-Detection/dp/B08RS4C67L) |
| RLA-PS1 (8-port PoE switch) | [reolink.com](https://support.reolink.com/articles/16958961315609-Introduction-to-RLA-PS1-PoE-Switch/) | [amazon.com](https://www.amazon.com/Reolink-Gigabit-Cameras-IEEE802-3af-Desktop/dp/B0BWHKQ5N9) |
| Universal 1/4"-20 mount adapter (reuse Nest brackets) | — | [amazon.com](https://www.amazon.com/Holicfun-Magnetic-Universally-Compatible-Simplisafe/dp/B0CNZRT7NV) |

Not linked (buy locally based on actual run lengths): Cat6 cable, keystone jacks, doorbell transformer verification (8–24V AC required for chime compatibility).

## Open items / next steps

- [ ] Confirm which specific positions currently lack Ethernet access (assumed: alley, parking lot, fence — confirm before ordering E1 Outdoor units).
- [ ] Verify existing doorbell transformer voltage (8–24V AC) before ordering Video Doorbell WiFi.
- [ ] Decide on Home Assistant host machine for geofencing automation + TV dashboard.
- [ ] Test powerline networking at one no-cable location before committing to that approach broadly.
- [ ] Plan resolution settings per camera (1080p/2K for lower-priority angles like alley/parking lot, 4K for doorbells and detail-critical spots) to balance retention vs. clarity.
