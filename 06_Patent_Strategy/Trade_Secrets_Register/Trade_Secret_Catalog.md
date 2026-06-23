# IND-VIAS Trade Secret Register

## Purpose

This document catalogs all technical information protected as trade secrets. These items must NEVER appear in:
- Patent applications (which become public)
- Marketing materials
- Conference presentations
- Public GitHub repositories
- Customer-facing documentation (unless under NDA)

---

## Active Trade Secrets

| ID | Description | Protection Level | Access Control |
|----|-------------|-----------------|----------------|
| TS-001 | Carrier-to-SoM connector pinout specification | Critical | Named engineers only |
| TS-002 | High-speed signal routing topology and layer assignment | High | HW team + layout contractor under NDA |
| TS-003 | Platform configuration database structure | High | FW team + architect |
| TS-004 | Power sequencing timing parameters per SoC variant | Medium | HW + FW teams |
| TS-005 | PoC network optimization methodology | Medium | HW team |
| TS-006 | Variant generation algorithm and BOM derivation rules | Medium | Engineering + operations |
| TS-007 | Manufacturing test sequences and pass/fail criteria | Medium | Test engineering + CM under NDA |

---

## Protection Measures

### Technical Controls
- Repository access restricted to named team members
- No public branches or forks permitted
- Trade secret files excluded from any open-source releases
- Encrypted storage for TS-001 level documents

### Administrative Controls
- All team members sign IP assignment + trade secret acknowledgment
- Exit interviews include trade secret reminder
- Vendor NDAs cover all TS-marked information
- Annual trade secret audit

### Physical Controls
- Layout files not transmitted by email (secure file share only)
- Prototype boards tracked by serial number
- Scrapped prototypes physically destroyed

---

## Review Schedule

- Quarterly: Review catalog for completeness
- Annually: Full audit of access controls and compliance
- On personnel change: Update access lists
