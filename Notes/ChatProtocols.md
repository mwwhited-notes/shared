# Core Instant Messaging & Chat Protocols

## IRC (Internet Relay Chat)
- RFC 1459 – Original IRC protocol (historic)
- RFC 2812 – IRC Client Protocol
- RFC 2811 / RFC 2813 – Channel & Server protocols

Still widely implemented, though officially “historic”.

## XMPP (Extensible Messaging and Presence Protocol)

(formerly Jabber)
- RFC 6120 – XMPP Core
- RFC 6121 – Instant Messaging and Presence
- RFC 7622 – Address Format (JIDs)

Related extensions are defined as XEPs (not RFCs).

## SIP-Based Instant Messaging (SIMPLE)

SIP can carry IM using MESSAGE or session-based methods:
- RFC 3261 – SIP Core
- RFC 3428 – SIP MESSAGE method (page-mode IM)
- RFC 3856 – SIP SIMPLE (Instant Messaging)
- RFC 3863 – Presence Information Data Format (PIDF)

## MSRP (Message Session Relay Protocol)

Used with SIP for chat sessions and file transfer.
- RFC 4975 – MSRP
- RFC 4976 – Relay Extensions

## Message & Payload Formats

These define how IM content is structured, independent of transport:
- RFC 3862 – CPIM (Common Profile for Instant Messaging)
- RFC 4480 – RPID (Rich Presence Extensions)

## Web-Based & Transport-Related RFCs (Often Used for Chat)

Not IM protocols themselves, but commonly used:
- RFC 6455 – WebSocket (used by many modern chat systems)
- RFC 8441 – WebSocket over HTTP/2

## Presence & Notifications
- RFC 6665 – SIP-Specific Event Notification
- RFC 3265 – SIP Event Notification Framework

## Not RFCs (but often confused as such)
- Matrix – Defined via open specs (IETF drafts, not RFCs)
- MQTT – OASIS / ISO standard (not IETF RFC)
- Slack / Discord / WhatsApp – Proprietary protocols
