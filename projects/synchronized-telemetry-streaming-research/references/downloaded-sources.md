# Downloaded Sources Registry

This file tracks all downloaded RFC and standards documents for the synchronized-telemetry-streaming-research project.

## RFCs (Real-time Transport Protocol & Streaming)

### RFC 7826 - Real Time Streaming Protocol Version 2.0 (RTSP/2.0)
- **URL:** https://www.rfc-editor.org/rfc/rfc7826.txt
- **File:** RFC7826_RTSP2.0.txt (729 KB)
- **Downloaded:** 2026-01-16
- **Purpose:** Core protocol specification for real-time streaming, essential for understanding RTSP 2.0 capabilities for synchronized telemetry streaming

### RFC 8108 - Multiple RTP Payload Format Grouping Semantics for Multi-Stream Multiplexing
- **URL:** https://www.rfc-editor.org/rfc/rfc8108.txt
- **File:** RFC8108_MultipleRTPStreams.txt (73 KB)
- **Downloaded:** 2026-01-16
- **Purpose:** Defines mechanisms for multiplexing multiple RTP streams, critical for synchronized multi-stream telemetry

### RFC 8861 - RTP Multi-Stream Profile and Payload Format Specifications
- **URL:** https://www.rfc-editor.org/rfc/rfc8861.txt
- **File:** RFC8861_RTPMultiStreamRTCP.txt (43 KB)
- **Downloaded:** 2026-01-16
- **Purpose:** RTCP extensions for multi-stream RTP, enables synchronized feedback and statistics across multiple streams

### RFC 6051 - Rapid Synchronisation of RTP Flows
- **URL:** https://www.rfc-editor.org/rfc/rfc6051.txt
- **File:** RFC6051_RapidRTPSync.txt (53 KB)
- **Downloaded:** 2026-01-16
- **Purpose:** Techniques for rapid RTP synchronization, directly applicable to rapid telemetry stream synchronization

### RFC 7233 - Hypertext Transfer Protocol (HTTP/1.1): Range Requests
- **URL:** https://www.rfc-editor.org/rfc/rfc7233.txt
- **File:** RFC7233_HTTPRangeRequests.txt (46 KB)
- **Downloaded:** 2026-01-16
- **Purpose:** HTTP range request semantics useful for partial telemetry data retrieval and resumable streaming

### RFC 9232 - Application-Layer Traffic Optimization (ALTO) Protocol for Network Telemetry
- **URL:** https://www.rfc-editor.org/rfc/rfc9232.txt
- **File:** RFC9232_NetworkTelemetry.txt (98 KB)
- **Downloaded:** 2026-01-16
- **Purpose:** Network telemetry collection and distribution protocols, relevant for collecting telemetry from network sources

## Standards & Specifications

### CloudEvents Specification
- **URL:** https://raw.githubusercontent.com/cloudevents/spec/main/cloudevents/spec.md
- **File:** CloudEvents_Spec.md (29 KB)
- **Downloaded:** 2026-01-16
- **Repository:** https://github.com/cloudevents/spec
- **Purpose:** Cloud-native event format specification, applicable for standardized telemetry event representation and distribution

### BitTorrent Protocol Version 2 (BEP 52)
- **URL:** https://www.bittorrent.org/beps/bep_0052.html
- **File:** BitTorrentV2_BEP52.md (32 KB)
- **Downloaded:** 2026-01-16
- **Purpose:** Peer-to-peer protocol design patterns, relevant for distributed telemetry streaming and decentralized data collection

## File Organization

All documents are stored in: `/current/src/projects/synchronized-telemetry-streaming-research/documents/`

## Quality Verification

All files have been verified as valid documents:
- RFC text files: ASCII or UTF-8 text format
- Specification markdown: UTF-8 text format
- HTML specifications: Valid XML/HTML documents

## Usage Notes

- RFCs marked "RTSP/Streaming/RTP" are directly applicable to the core synchronization protocol design
- RFC 6051 and RFC 8108/8861 provide the most direct guidance on multi-stream synchronization
- CloudEvents can be used to standardize telemetry event schemas
- BitTorrent v2 design patterns may inform distributed streaming architecture

## Related Resources

- IETF Datatracker: https://datatracker.ietf.org/
- RFC Editor: https://www.rfc-editor.org/
- CloudEvents GitHub: https://github.com/cloudevents/spec
- BitTorrent Enhancement Proposals: https://www.bittorrent.org/beps/

