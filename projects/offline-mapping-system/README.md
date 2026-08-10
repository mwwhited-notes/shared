# Offline Mapping, Search & Routing System

Self-built, self-hosted offline mapping stack — detailed maps, search, routing, and
trip-planning suggestions that work with zero connectivity — built from public/FOSS
geodata plus curated data from public APIs and (carefully, secondarily) community
sources, rather than paying for a stack of commercial subscriptions.

## Overview

The van trips this notebook tracks (`Personal/RoadTrip/`) keep running into the same
problem: a cell booster can show full bars while the actual data connection is dead
(a documented false-positive failure mode — see
[`Personal/RoadTrip/_knowledge/lessons-learned.md`](../../../Personal/RoadTrip/_knowledge/lessons-learned.md)'s
Connectivity section), and Tennessee's "reservations required even for cash/walk-up
sites" rule cost an unplanned night because the tool in hand couldn't answer "where can
we actually stay tonight" with no signal. The immediate fix already logged in
[`Personal/Vans/DriftCampervans/09_Mod_Ideas.md`](../../../Personal/Vans/DriftCampervans/09_Mod_Ideas.md)
is a commercial stack — **Gaia GPS + Trailforks + Avenza Maps**, ~$90/yr plus a
Trailforks subscription, each app siloed to its own data and its own offline cache.

This project is the longer-term alternative: **one self-hosted system**, built on
open data, that can be extended indefinitely (new regions, new POI categories, custom
routing profiles the commercial apps don't offer — like a Sprinter's actual height and
weight) without paying per-app subscriptions or accepting whatever data model each
vendor chose.

**Four capabilities, explicitly, matching what was asked for:**
1. **Offline maps** — detailed base maps + trails + land-management boundaries, usable
   with zero connectivity.
2. **Offline search** — find a place by name/category without a live connection.
3. **Offline routing** — turn-by-turn or trail routing computed locally, including a
   custom **van-height-aware** profile no commercial consumer app offers.
4. **Offline suggestions/planning** — recommend stops matching an interest (the
   standing default interests already tracked in the road-trip skill: hiking, MTB,
   photography, astrophotography, diving, paddling, climbing) from a locally-cached,
   enriched POI database — the part no map app does well, commercial or otherwise.

**Scope: regional per-trip, not world-wide.** *(Clarified 2026-08-10.)* This is not a
"download the planet" system — it's a **pre-plan-with-buffer** workflow: given a road
trip's actual route (already computed by the `road-trip` skill's corridor step), build
a bounding box/corridor around that route plus a buffer margin, and pull/build data only
for that area before departure. This keeps storage and compute modest (a corridor
extract, not a state or planet extract), keeps the data current for the trip actually
being taken, and matches how trips are already planned in `Personal/RoadTrip/` — one
folder per trip, not one static "cover everywhere" dataset. See Construction Method
Phase 1 for the concrete workflow.

**Two build strategies, not mutually exclusive — see Construction Method:**
- **Fast path:** OsmAnd (see Materials) already does #1–#3 well out of the box, plus a
  meaningful slice of #4 via its offline Wikipedia/Wikivoyage layer. Worth standing up
  first as a baseline before building anything custom.
- **Custom path:** self-hosted routing/search/POI-enrichment stack for the parts OsmAnd
  doesn't cover — van-specific routing constraints, a merged/deduplicated POI database
  across multiple sources, and interest-based trip suggestions tailored to this
  household's actual standing interests rather than a generic recommendation feed.

## Materials

| Material | Purpose | Source | Notes |
|----------|---------|--------|-------|
| [OsmAnd](https://osmand.net/) | FOSS offline maps/search/routing app — the fast-path baseline | Free (Android/iOS), open source | Feature-rich but complex UI; has offline Wikipedia/Wikivoyage POI layers already built in |
| [Organic Maps](https://organicmaps.app/) | Simpler FOSS alternative to OsmAnd | Free, open source | Fewer features, no telemetry; worth a side-by-side comparison against OsmAnd before committing |
| OpenStreetMap (OSM) data | Base map layer for everything below — roads, trails, POIs, land use | [Geofabrik](https://download.geofabrik.de/) regional extracts (`.pbf`), clipped down via Overpass, Open Database License | **Scoped per trip** — a buffered corridor around the planned route, not a state/region/planet extract. See Phase 1 |
| [Overpass API](https://overpass-api.de/) / [Overpass Turbo](https://overpass-turbo.eu/) | Query OSM by tag (e.g. all campsites, all trailheads, all dump stations) for custom extracts | Free, public instance or self-hosted | The practical way to build a filtered POI dataset from OSM without downloading everything |
| [Recreation.gov RIDB API](https://ridb.recreation.gov/) | **Official, free, public API** for federal campgrounds/facilities/trails/permits — NPS, USFS, BLM, USACE, BOR, FWS | Free, no auth for basic use; optional free key raises rate limits | **Prefer this over scraping Recreation.gov itself** — it's the legitimate, stable source for exactly this data |
| [NPS Developer API](https://www.nps.gov/subjects/developer/api-documentation.htm) | Official National Park Service data — park info, alerts, designations | Free, API key required | Complements RIDB for NPS-specific detail |
| [BRouter](https://brouter.de/brouter/) | FOSS routing engine — **candidate for the custom van-height profile** | Open source, self-hostable, lightweight enough for a Pi | Per-request custom routing profiles via its own scripting language (which OSM tags weight which edges, access restrictions) — the flexibility a fixed van-height/weight profile needs |
| [Valhalla](https://github.com/valhalla/valhalla) | Alternative FOSS routing engine | Open source, self-hostable | Good on low-spec hardware, all profiles share one graph via dynamic costing — evaluate against BRouter before committing to one |
| [Nominatim](https://nominatim.org/) / [Photon](https://github.com/komoot/photon) | Self-hosted OSM-based geocoding/search | Open source | **Region-limited extracts only** — a planet-wide Nominatim instance needs ~95GB disk + 64GB RAM; a multi-state corridor extract is far lighter and fits actual trip needs |
| [Kiwix](https://www.kiwix.org/) | Offline Wikipedia/Wikivoyage reader | Free, open source | A ready-made way to deliver offline "what's interesting here" content (Wikivoyage) without building a content system from scratch |
| Self-hosted compute | Runs the ingestion pipeline, routing engine, and search index | [DevOps Playground Cluster](../devops-playground-cluster/) or a dedicated SBC | Data prep and periodic re-sync happen at home on real hardware; only the resulting map/index files need to travel in the van |

**Deliberately not primary data sources yet — see the note on scraping below:**
iOverlander (community camping/POI database, own format, no confirmed public API/export
found during initial research — check their own site/community for an official export
before writing a scraper), Campendium, and general forum content (r/vandwellers,
r/overlanding, etc.).

## Construction Method / Build Steps

**Phase 0 — fast path baseline (do this first, low effort):**
1. Stand up OsmAnd with regional OSM downloads for the actual travel corridor,
   including its offline Wikipedia/Wikivoyage layers.
2. Compare against Organic Maps on the same device/trip to see whether the extra
   OsmAnd complexity earns its keep for this household's actual use.
3. Use this as the working baseline while the custom system below is built —
   don't leave the household without offline maps in the meantime.

**Phase 1 — data ingestion, scoped per trip with a buffer:**
1. **Compute the area to pull, don't hardcode a region.** Take the trip's
   start/end points and any firm stops (already known once a `Personal/RoadTrip/`
   trip folder exists), build a bounding box or buffered corridor around the
   planned route — e.g. a fixed-width buffer (25–50 mi either side, tunable) along
   the route line, plus a wider radius (~25 mi) around each overnight stop and
   firm destination, since side quests and "what's nearby" searches happen
   around stops, not just along the drive line. This becomes the actual data
   footprint for the trip, not a whole state or region.
2. Clip Geofabrik OSM extracts (or query Overpass directly with the computed
   bounding box) down to that buffered corridor — **regional per trip, never
   planet-wide or even whole-state by default.**
3. Pull Recreation.gov RIDB + NPS API data filtered to the same bounding box —
   campgrounds, trailheads, permits, facilities.
3. Use Overpass Turbo to build filtered extracts for specific POI categories the
   standing interests care about (trailheads, dive shops, dark-sky sites, put-ins,
   crags) that aren't already well-tagged in the RIDB/NPS pull.
4. **Scraping forums/review sites is a later, lower-priority phase, done carefully:**
   check for an official API or data export first (per source), respect
   `robots.txt` and each site's ToS, rate-limit aggressively, and treat this as
   enrichment/cross-reference data (e.g. corroborating a camping spot's quality)
   rather than a primary source of truth. Don't build automated scraping
   infrastructure before checking whether the target site would rather license or
   export the data directly.
5. Merge/deduplicate POIs across sources into one local database (SQLite is
   probably enough at multi-state scale — no need for a heavier system).

**Phase 2 — routing:**
1. Stand up BRouter (or Valhalla, evaluate both) self-hosted against the regional
   OSM extract.
2. Build a custom van routing profile: height/weight restrictions, prefer
   truck-accessible fuel stops, avoid roads the 2WD Sprinter shouldn't attempt —
   see [`Personal/Vans/DriftCampervans/`](../../../Personal/Vans/DriftCampervans/)
   and the Sprinter profile in
   [`.claude/skills/road-trip/references/vehicles.md`](../../../.claude/skills/road-trip/references/vehicles.md)
   for the actual constraints to encode.
3. Confirm the routing engine's output can be exported/cached for fully offline
   use on a tablet/laptop, not just served live from the home cluster.

**Phase 3 — search:**
1. Stand up Nominatim or Photon against the same regional extract.
2. Confirm offline usability — export whatever the chosen engine needs onto the
   travel device, don't depend on a live query to the home cluster while on the
   road.

**Phase 4 — suggestions/planning (the novel part):**
1. Tag the merged POI database against the standing default interests table in
   [`Personal/RoadTrip/_knowledge/trip-topics.md`](../../../Personal/RoadTrip/_knowledge/trip-topics.md).
2. Start with simple rule-based filtering/scoring (tag match + distance from
   route), not a full recommendation engine — see whether that's already useful
   before building anything more elaborate.
3. Stand up Kiwix with Wikivoyage for offline "what's worth seeing here" reading,
   as a ready-made complement rather than writing original content.

**Phase 5 — packaging for the van:**
1. Decide the actual offline client: a tablet running a custom front-end (MapLibre
   GL is the likely FOSS choice for rendering), OsmAnd/Organic Maps with the custom
   POI data layered in if their import formats allow it, or a small self-hosted
   web app served from a Pi in the van itself.
2. Define the home-to-van sync process — when the van is home, pull the latest
   regional extracts/POI data before the next trip.

## Key Features

- Fully offline maps, search, routing, and interest-based suggestions — no
  dependency on cell signal or a booster's (sometimes false) connectivity
- Custom van-height/weight routing profile — not available in any commercial
  consumer app found so far
- Built on licensed, open, or officially-public data (OSM's ODbL, Recreation.gov's
  public RIDB API, NPS's public API) rather than paid subscriptions or
  unlicensed scraping
- Extensible indefinitely — new regions, new POI categories, new interest
  tags — without waiting on a vendor or paying per-feature

## Advantages Over Commercial/Alternative Solutions

| Feature | This project | Gaia GPS + Trailforks + Avenza |
|---------|--------------|--------------------------------|
| Cost | One-time build + self-hosted compute already owned | ~$90+/yr, growing with more apps |
| Van-specific routing | Custom height/weight profile, buildable | Not available |
| Data model | One merged database, extensible | Siloed per app, fixed to vendor's categories |
| Interest-based suggestions | Purpose-built for this household's standing interests | Generic POI browsing only |
| Offline Wikipedia/Wikivoyage content | Kiwix, free | OsmAnd has this already (a reason to keep OsmAnd as the Phase 0 baseline) |
| Effort | Real build and maintenance work | Zero — install and pay |

## Use Cases

- Trip planning for future `Personal/RoadTrip/` trips — feed suggestions and
  offline routing directly into the road-trip skill's research step
- Turn-by-turn / trail routing with zero cell signal, including a van-safe route
- Answering "what's interesting near here" offline, matched to standing interests
  (hiking, MTB, photography, astrophotography, diving, paddling, climbing)
- A durable answer to the exact failure mode that started this: a booster showing
  bars while the actual connection is dead, or a state's camping rules requiring
  a reservation with no signal to make one

## Project Status

**Status:** Planning

**Next Steps:**
1. Stand up the Phase 0 fast-path baseline (OsmAnd vs. Organic Maps) before
   building anything custom — get a real offline baseline in the van soon rather
   than waiting on the full build.
2. Evaluate BRouter vs. Valhalla directly against the actual need (a van-height
   profile) rather than on general reputation.
3. Check iOverlander and Campendium for an official data export/API before
   considering any scraping of either.
4. Decide the home compute target — likely the
   [DevOps Playground Cluster](../devops-playground-cluster/) — and whether this
   shares infrastructure with the [Local Docker Registry](../local-docker-registry/)
   project.
5. Pick a first real trip from `Personal/RoadTrip/` and build its buffered corridor
   as the pilot dataset — a real trip's actual route, not a synthetic test region.
6. Decide default buffer widths (route-line buffer vs. stop-radius buffer) against
   that pilot before generalizing to a repeatable per-trip pipeline.

**Convergent research note:** a DIY offline-mapping approach (Geofabrik/OSM extracts +
government GIS layers + QGIS to merge + OsmAnd/Organic Maps to consume) was
independently discussed while researching van mod ideas in
[`Personal/Vans/DriftCampervans/change-tracking.md`](../../../Personal/Vans/DriftCampervans/change-tracking.md)
(08/10/2026 entries) before this project existed — that thread and this project should
be reconciled rather than developed in parallel.

## References

- [OsmAnd](https://osmand.net/) · [Organic Maps](https://organicmaps.app/)
- [Geofabrik OSM extracts](https://download.geofabrik.de/) · [Overpass Turbo](https://overpass-turbo.eu/) · [OSM copyright/license (ODbL)](https://www.openstreetmap.org/copyright)
- [Recreation.gov RIDB API](https://ridb.recreation.gov/) · [NPS Developer API](https://www.nps.gov/subjects/developer/api-documentation.htm)
- [BRouter](https://brouter.de/brouter/) · [Valhalla](https://github.com/valhalla/valhalla)
- [Nominatim](https://nominatim.org/) · [Photon](https://github.com/komoot/photon)
- [Kiwix](https://www.kiwix.org/)
- Cross-reference: [`Personal/Vans/DriftCampervans/09_Mod_Ideas.md`](../../../Personal/Vans/DriftCampervans/09_Mod_Ideas.md) — the commercial-stack recommendation (Gaia/Trailforks/Avenza) this project aims to eventually replace or supplement
- Cross-reference: [`Personal/RoadTrip/_knowledge/lessons-learned.md`](../../../Personal/RoadTrip/_knowledge/lessons-learned.md) — the connectivity/offline-planning lessons that motivated this
- Cross-reference: [`.claude/skills/road-trip/references/vehicles.md`](../../../.claude/skills/road-trip/references/vehicles.md) — Sprinter routing constraints to encode in the van profile
- Cross-reference: [`devops-playground-cluster/`](../devops-playground-cluster/), [`local-docker-registry/`](../local-docker-registry/) — likely shared hosting infrastructure

---

*Last updated: 2026-08-10*
