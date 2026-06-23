# ADVIS ERC Waiver Policy

**Document ID:** ADVIS-ERC-POL-001  
**Version:** 0.1.0  
**Status:** Draft  
**Last Updated:** 2024-01-15

---

## 1. Purpose

This document defines the Electrical Rules Check (ERC) waiver policy for the ADVIS ECU
schematic design. It establishes which ERC violations can be waived, the approval process,
documentation requirements, and common automotive-specific exceptions.

---

## 2. ERC Waiver Philosophy

The default position is: all ERC errors must be resolved, not waived. Waivers are granted
only when the flagged condition is an intentional design choice that has been technically
justified and reviewed.

### Principles

1. **Fix first** - Attempt to resolve the ERC error by correcting the design
2. **Justify second** - If the design is intentional, document the engineering rationale
3. **Approve third** - A second engineer must verify and approve the waiver
4. **Track always** - All waivers are logged with revision traceability

---

## 3. Waiver Classification

### 3.1 Waivable Conditions

| ERC Error Type | Waivable? | Common Justification |
|----------------|-----------|---------------------|
| Unconnected pin | Yes (with justification) | NC pin per datasheet recommendation |
| Multiple power symbols on net | Yes | Star-point ground topology by design |
| Pin type conflict (output-output) | Rarely | Open-drain shared bus (requires review) |
| Net with only one connection | Yes | Test point or intentional stub |
| Missing pull-up on open-drain | Yes (conditional) | External pull-up on another sheet |
| Power pin not driven | No | Must always have explicit supply |
| Duplicate net name | No | Must resolve naming conflict |
| Short between different nets | No | Design error - must fix |

### 3.2 Non-Waivable Conditions

The following ERC conditions MUST be resolved and cannot be waived:

- Power pin without supply connection
- Short circuits between nets
- Duplicate reference designators
- Missing ground connections
- Unresolved bus connections
- Net name conflicts across hierarchical boundaries

---

## 4. Approval Process

### 4.1 Workflow

```
+----------+     +-----------+     +----------+     +---------+
| Designer | --> | Document  | --> | Peer     | --> | Waiver  |
| Flags    |     | Rationale |     | Review   |     | Logged  |
+----------+     +-----------+     +----------+     +---------+
                                        |
                                        v (if rejected)
                                   +---------+
                                   | Resolve |
                                   | Error   |
                                   +---------+
```

### 4.2 Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| Schematic Designer | Identifies waiver need, documents rationale |
| Peer Reviewer | Verifies technical justification, approves/rejects |
| HW Lead | Final approval for safety-related waivers |
| Configuration Manager | Logs waiver in revision history |

### 4.3 Safety-Related Waivers

Any waiver touching the following subsystems requires HW Lead approval:
- Power supervision (TPS3808G33-Q1)
- Watchdog (TPS3431-Q1)
- CAN-FD communication path
- Reset distribution

---

## 5. Waiver Documentation Requirements

Each waiver entry must include:

| Field | Description |
|-------|-------------|
| Waiver ID | Sequential identifier (ERC-W-001, ERC-W-002, ...) |
| ERC Rule | Which ERC rule is violated |
| Sheet | Which schematic sheet |
| Net/Component | Affected net name or component RefDes |
| Error Message | Exact ERC tool error message |
| Rationale | Engineering justification for why this is intentional |
| Risk Assessment | Impact if the waiver masks a real error |
| Approved By | Reviewer name and date |
| Schematic Rev | Schematic revision when waiver was granted |

---

## 6. Common Automotive ERC Exceptions

### 6.1 Ground Domain Separation

**Condition:** ERC flags "multiple power symbols" on ground nets
**Rationale:** ADVIS uses intentional ground domain separation (PGND_IN, BOARD_GND,
CHASSIS_GND) with star-point connection. ERC tools may flag the split ground topology.
**Policy:** Waivable if ground domain architecture document confirms intentional separation.

### 6.2 Power Sequencing Enable Chains

**Condition:** ERC flags "output driving output" on enable chain
**Rationale:** Power Good output of one regulator drives Enable input of next regulator.
Both may be typed as "output" in symbol libraries.
**Policy:** Waivable. Update symbol pin types to resolve if possible; otherwise waive
with reference to Power_Tree_Architecture.md sequencing diagram.

### 6.3 Unused SoM Pins

**Condition:** ERC flags unconnected pins on SoM connector
**Rationale:** Not all SoM pins are used on every carrier variant. Unused pins are
intentionally left unconnected per SoM vendor guidance.
**Policy:** Waivable with reference to SoM datasheet no-connect recommendations.

### 6.4 CAN Bus Termination

**Condition:** ERC flags "pin type mismatch" on split termination network
**Rationale:** Split termination uses capacitor to ground between two resistors.
ERC may flag the capacitor connection as unexpected.
**Policy:** Waivable with reference to CAN physical layer specification.

### 6.5 Open-Drain Shared Signals

**Condition:** ERC flags "output-output conflict" on I2C lines or interrupt lines
**Rationale:** I2C bus is open-drain with shared SCL/SDA. Multiple devices drive
the same line through open-drain outputs.
**Policy:** Waivable for confirmed open-drain pins with external pull-up present.

### 6.6 Test Points and Stubs

**Condition:** ERC flags "net with only one connection"
**Rationale:** Test points intentionally create single-connection stubs for probe access.
**Policy:** Waivable if the net connects to a designated test point footprint.

---

## 7. Waiver Log Template

| Waiver ID | ERC Rule | Sheet | Net/Component | Rationale | Approved By | Rev |
|-----------|----------|-------|---------------|-----------|-------------|-----|
| ERC-W-001 | -- | -- | -- | -- | -- | -- |
| ERC-W-002 | -- | -- | -- | -- | -- | -- |

---

## 8. Periodic Review

- All waivers reviewed at each major schematic revision milestone
- Waivers from previous revisions re-validated after schematic changes
- Obsolete waivers (resolved by design change) removed from active list
- Waiver count tracked as quality metric (target: minimize)

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1.0 | 2024-01-15 | -- | Initial ERC waiver policy definition |
