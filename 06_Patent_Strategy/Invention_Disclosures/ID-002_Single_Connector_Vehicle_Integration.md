# Invention Disclosure: ID-002

## Title
Unified Hybrid Connector System for Automotive ADAS ECU Vehicle Integration

## Date
June 2026

## Inventors
[To be filled]

## Status
DRAFT - Awaiting prior art search

---

## Problem Statement

Current ADAS ECUs require multiple separate connectors for power, CAN bus, camera coax links, and auxiliary signals. This increases:
- Harness complexity and cost
- Assembly time at vehicle integration
- Potential failure points (multiple connector matings)
- Sealed enclosure design difficulty (multiple penetrations)

## Proposed Solution

A single sealed hybrid automotive connector that carries:

1. Power (12V battery + ground returns)
2. CAN-FD differential pair(s)
3. FPD-Link III coaxial camera channels (1-4 links)
4. Auxiliary signals (ignition sense, wake, GNSS antenna feed)
5. Shield/chassis ground

All within one connector body with appropriate isolation and shielding between domains.

## Key Novel Elements

- Coaxial contacts for high-speed video integrated with power and low-speed data in single housing
- Domain isolation within connector body (power/signal/RF separation)
- Single-action vehicle installation (one plug = full system connection)
- Scalable contact count for platform variants (Entry: fewer coax, High: more coax)

## Market Differentiation

- Competitors (Mobileye, Continental, Bosch ADAS units) typically use 3-5 separate connectors
- Single-connector integration is a visible competitive advantage for OEM vehicle integration teams
- Reduces OEM harness cost and assembly labor

## Next Steps

- [ ] Survey existing hybrid connector families (Amphenol, TE, Molex automotive)
- [ ] Prior art search on combined power/data/coax connector systems
- [ ] Feasibility check: can coax and power share a housing with acceptable isolation?
- [ ] Design patent candidate for connector industrial design
- [ ] Utility patent candidate for multi-domain isolation method
