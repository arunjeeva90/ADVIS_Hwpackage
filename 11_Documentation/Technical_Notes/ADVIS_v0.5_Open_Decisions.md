# ADVIS v0.5 Open Decisions Register

**Classification:** CONFIDENTIAL - ENGINEERING USE ONLY  
**Status:** ACTIVE - Tracking document for open technical decisions  
**Version:** v0.1 - July 2026  
**Document ID:** TN-004

---

## 1. Purpose

This document tracks all open technical decisions for the ADVIS v0.5 Compact Module. Each decision is categorized by subsystem, priority, and target resolution date. Decisions marked OPEN require action before the corresponding design milestone can proceed.

---

## 2. Decision Status Legend

| Status | Meaning |
|--------|---------|
| OPEN | Decision not yet made, action required |
| IN REVIEW | Options identified, under evaluation |
| PRELIMINARY | Tentative selection made, awaiting confirmation |
| CLOSED | Decision finalized and committed |

---

## 3. SoC Selection Decisions

### OD-001: Primary SoC for ADVIS Assist v0.5

| Field | Value |
|-------|-------|
| **ID** | OD-001 |
| **Subsystem** | Compute / SoC |
| **Priority** | P1 - Critical (blocks PCB layout start) |
| **Status** | OPEN |
| **Owner** | Systems Engineering |
| **Target Date** | TBD |
| **Options** | TDA4VL-Q1, AM62A, J722S |
| **Recommendation** | TDA4VL-Q1 (PRELIMINARY) |
| **Rationale** | Lowest cost/power with 2x CSI-2 ports and adequate ~1 TOPS for warning-level perception. AM62A has single ISP pipeline concern for dual-camera. J722S is newer with less mature SDK. |
| **Blocking** | PCB schematic entry, BGA fanout, DDR routing, power tree sizing |
| **Dependencies** | OD-002 (sensor selection affects CSI lane requirements), OD-009 (SDK evaluation) |

### OD-002: Primary SoC for ADVIS Control v0.5

| Field | Value |
|-------|-------|
| **ID** | OD-002 |
| **Subsystem** | Compute / SoC |
| **Priority** | P1 - Critical |
| **Status** | OPEN |
| **Owner** | Systems Engineering |
| **Target Date** | TBD |
| **Options** | TDA4VM-Q1 (primary), J722S (if 4 TOPS sufficient) |
| **Recommendation** | TDA4VM-Q1 (PRELIMINARY) |
| **Rationale** | Only candidate with ~8 TOPS MMA for AEB/ACC/LKA safety-critical inference. J722S at ~4 TOPS may be insufficient for safety margins. |
| **Blocking** | PCB layout (23x23mm BGA requires more area), thermal design, power budget |
| **Dependencies** | OD-010 (thermal feasibility in windshield mount) |

### OD-003: PCB Compatibility Strategy (Single PCB vs. Dual PCB)

| Field | Value |
|-------|-------|
| **ID** | OD-003 |
| **Subsystem** | Platform Architecture |
| **Priority** | P1 - Critical |
| **Status** | OPEN |
| **Owner** | Hardware Architecture |
| **Target Date** | TBD |
| **Options** | (A) Single PCB with superset footprint supporting TDA4VL and TDA4VM via BOM variants; (B) Two separate PCB designs optimized per SoC |
| **Recommendation** | None yet - requires BGA pinout compatibility analysis |
| **Rationale** | Single PCB reduces NRE but may compromise board area and layer count. Dual PCB allows per-tier optimization. |
| **Blocking** | PCB stackup definition, mechanical envelope finalization |
| **Dependencies** | OD-001, OD-002, OD-011 |

---

## 4. Forward Camera Sensor Decisions

### OD-004: Forward Camera Sensor Selection (Assist Tier)

| Field | Value |
|-------|-------|
| **ID** | OD-004 |
| **Subsystem** | Camera / Optics |
| **Priority** | P1 - Critical |
| **Status** | OPEN |
| **Owner** | Systems Engineering |
| **Target Date** | TBD |
| **Options** | OX03C10 (OmniVision), AR0233 (onsemi), IMX390 (Sony) |
| **Recommendation** | OX03C10 (PRELIMINARY, cost-down) |
| **Rationale** | OX03C10 offers 2.5MP HDR at lower cost than IMX390. AR0233 is alternative with excellent LFM. IMX390 is premium but may be cost-prohibitive for Assist tier. |
| **Blocking** | Lens selection, ISP tuning effort estimation, optical design |
| **Dependencies** | OD-001 (SoC ISP compatibility), OD-006 (MIPI lane allocation) |

### OD-005: Forward Camera Sensor Selection (Control Tier)

| Field | Value |
|-------|-------|
| **ID** | OD-005 |
| **Subsystem** | Camera / Optics |
| **Priority** | P2 - High |
| **Status** | OPEN |
| **Owner** | Systems Engineering |
| **Target Date** | TBD |
| **Options** | IMX390 (Sony), OX03C10 (OmniVision) |
| **Recommendation** | IMX390 (PRELIMINARY) |
| **Rationale** | Best night vision (3um pixel), most mature TI ISP tuning available, widely validated in ADAS applications. Higher cost acceptable for Control tier. |
| **Blocking** | ISP tuning resource allocation, evaluation sample procurement |
| **Dependencies** | OD-002 (TDA4VM VPAC3 ISP support) |

### OD-006: Forward Camera MIPI Lane Count

| Field | Value |
|-------|-------|
| **ID** | OD-006 |
| **Subsystem** | Signal Integrity / Camera |
| **Priority** | P2 - High |
| **Status** | OPEN |
| **Owner** | SoC Lead |
| **Target Date** | TBD |
| **Options** | 2-lane CSI-2 (lower bandwidth, simpler routing) vs. 4-lane CSI-2 (full bandwidth, more complex) |
| **Recommendation** | 4-lane for TDA4VM (Control), 2-lane adequate for TDA4VL (Assist at 30fps) |
| **Rationale** | 2-lane at 2.5 Gbps/lane = 5 Gbps total, sufficient for 2.5MP RAW10 @ 30fps. 4-lane needed for 60fps or future resolution increase. |
| **Blocking** | PCB routing (4-lane requires more space), FPC pin count |
| **Dependencies** | OD-004, OD-005 (sensor frame rate requirements) |

---

## 5. DMS Camera Sensor Decisions

### OD-007: DMS Camera Sensor Selection (Assist Tier)

| Field | Value |
|-------|-------|
| **ID** | OD-007 |
| **Subsystem** | Camera / DMS |
| **Priority** | P1 - Critical |
| **Status** | OPEN |
| **Owner** | Systems Engineering |
| **Target Date** | TBD |
| **Options** | OX01N1B (OmniVision), AR0144 (onsemi), RGB-IR option |
| **Recommendation** | OX01N1B (PRELIMINARY) |
| **Rationale** | Smallest die, lowest cost, excellent NIR quantum efficiency for dedicated DMS function. AR0144 global shutter adds cost with marginal benefit for static-mount DMS. RGB-IR adds complexity. |
| **Blocking** | IR LED wavelength selection (850nm vs. 940nm), flex cable design |
| **Dependencies** | OD-012 (IR illumination design) |

### OD-008: DMS Camera Sensor Selection (Control Tier)

| Field | Value |
|-------|-------|
| **ID** | OD-008 |
| **Subsystem** | Camera / DMS |
| **Priority** | P2 - High |
| **Status** | OPEN |
| **Owner** | Systems Engineering |
| **Target Date** | TBD |
| **Options** | OX01H1B (OmniVision), OX01N1B, AR0144 |
| **Recommendation** | OX01H1B (PRELIMINARY) |
| **Rationale** | Higher resolution (1.3MP) provides better gaze and attention tracking accuracy for driver-aware moderation in Control tier. Cost increment is small. |
| **Blocking** | ISP tuning, DMS algorithm validation at higher resolution |
| **Dependencies** | OD-002 (SoC ISP pipeline bandwidth) |

---

## 6. Software and SDK Decisions

### OD-009: SDK Selection and Development Start Platform

| Field | Value |
|-------|-------|
| **ID** | OD-009 |
| **Subsystem** | Software / Firmware |
| **Priority** | P1 - Critical |
| **Status** | OPEN |
| **Owner** | Software Lead |
| **Target Date** | TBD |
| **Options** | (A) Start on TI Edge AI SDK with TDA4VM EVM, port to TDA4VL later; (B) Start on J722S EVM if available; (C) Start on AM62A Processor SDK |
| **Recommendation** | Option A (PRELIMINARY) |
| **Rationale** | TDA4VM SDK is most mature with best model zoo and ISP tuning tools. Software developed on TDA4VM can be scaled down to TDA4VL (same SDK family). J722S SDK is too new. |
| **Blocking** | Software development timeline, EVM procurement |
| **Dependencies** | OD-001, OD-002 (final SoC choices) |

### OD-010: Deep Learning Model Architecture for v0.5

| Field | Value |
|-------|-------|
| **ID** | OD-010 |
| **Subsystem** | AI / Perception |
| **Priority** | P2 - High |
| **Status** | OPEN |
| **Owner** | AI/ML Team |
| **Target Date** | TBD |
| **Options** | (A) TI reference models from model zoo; (B) Custom models trained and quantized for TI targets; (C) Third-party model license |
| **Recommendation** | Combination A + B (start with reference, customize) |
| **Rationale** | TI model zoo provides validated starting point. Custom training needed for OEM-specific requirements (detection classes, DMS features). |
| **Blocking** | Training data pipeline, compute resources for training |
| **Dependencies** | OD-001 (target TOPS determines model complexity budget) |

---

## 7. Thermal and Mechanical Decisions

### OD-011: Thermal Feasibility of TDA4VM in Windshield Mount

| Field | Value |
|-------|-------|
| **ID** | OD-011 |
| **Subsystem** | Thermal / Mechanical |
| **Priority** | P1 - Critical |
| **Status** | OPEN |
| **Owner** | Thermal Engineering |
| **Target Date** | TBD |
| **Question** | Can TDA4VM (10-15W TDP) be adequately cooled in a sealed windshield-mount housing with solar load? |
| **Analysis Required** | CFD simulation of enclosed module at 85C ambient + solar load, with aluminum spreader plate |
| **Fallback** | If thermal infeasible: (A) Power-limit TDA4VM via DVFS; (B) Use J722S instead; (C) Enlarge housing |
| **Blocking** | ADVIS Control v0.5 feasibility confirmation |
| **Dependencies** | OD-002, housing mechanical design |

### OD-012: Module Housing Dimensions and Bracket Design

| Field | Value |
|-------|-------|
| **ID** | OD-012 |
| **Subsystem** | Mechanical |
| **Priority** | P2 - High |
| **Status** | OPEN |
| **Owner** | Mechanical Engineering |
| **Target Date** | TBD |
| **Options** | (A) 60x40x25mm (aggressive compact); (B) 80x50x30mm (standard compact); (C) OEM-specific form factor |
| **Recommendation** | Option B for first prototype (PRELIMINARY) |
| **Rationale** | 80x50x30mm provides adequate PCB area for TDA4VM BGA, thermal spreader, and optical separation. Option A may be achievable with TDA4VL only. |
| **Blocking** | PCB outline, component placement, optical path design |
| **Dependencies** | OD-001, OD-002, OD-011 |

---

## 8. IR Illumination Decisions

### OD-013: IR LED Wavelength Selection

| Field | Value |
|-------|-------|
| **ID** | OD-013 |
| **Subsystem** | Optics / DMS |
| **Priority** | P2 - High |
| **Status** | OPEN |
| **Owner** | Optical Engineering |
| **Target Date** | TBD |
| **Options** | 850nm (visible faint red glow, higher sensor QE) vs. 940nm (invisible to human eye, lower sensor QE) |
| **Recommendation** | 940nm (PRELIMINARY) |
| **Rationale** | 940nm is invisible to occupants (no red glow distraction in windshield-mount module). Lower QE compensated by higher LED drive current or more LEDs. Most OEMs prefer invisible illumination for passenger vehicles. |
| **Blocking** | LED selection, driver circuit design, optical filter specification |
| **Dependencies** | OD-007, OD-008 (sensor NIR sensitivity at chosen wavelength) |

### OD-014: IR LED Drive Topology

| Field | Value |
|-------|-------|
| **ID** | OD-014 |
| **Subsystem** | Electrical / DMS |
| **Priority** | P3 - Medium |
| **Status** | OPEN |
| **Owner** | Electrical Engineering |
| **Target Date** | TBD |
| **Options** | (A) Constant-current LED driver IC (e.g., TPS92610-Q1); (B) Discrete MOSFET + sense resistor; (C) SoC GPIO direct drive (low-power LEDs only) |
| **Recommendation** | Option A (PRELIMINARY) |
| **Rationale** | Dedicated LED driver provides consistent illumination, thermal protection, and fault detection. Discrete approach saves cost but lacks diagnostics. |
| **Blocking** | BOM cost target, fault detection requirement from safety analysis |
| **Dependencies** | OD-013 (wavelength determines LED Vf and current) |

---

## 9. Signal Integrity and PCB Decisions

### OD-015: DMS Flex Cable Length and Type

| Field | Value |
|-------|-------|
| **ID** | OD-015 |
| **Subsystem** | Signal Integrity / Mechanical |
| **Priority** | P2 - High |
| **Status** | OPEN |
| **Owner** | SI Engineer / Mechanical |
| **Target Date** | TBD |
| **Options** | (A) 30mm rigid-flex (tight integration); (B) 50mm rigid-flex (nominal); (C) 80mm FPC (maximum flexibility) |
| **Recommendation** | 50mm rigid-flex (PRELIMINARY) |
| **Rationale** | 50mm provides adequate mechanical separation for optical baffle placement while maintaining good MIPI signal integrity margin (~2 dB margin at 1.5 Gbps). |
| **Blocking** | DMS PCBlet mechanical design, flex vendor selection |
| **Dependencies** | OD-012 (housing dimensions determine available flex routing path) |

### OD-016: PCB Stackup Definition

| Field | Value |
|-------|-------|
| **ID** | OD-016 |
| **Subsystem** | PCB Layout |
| **Priority** | P2 - High |
| **Status** | OPEN |
| **Owner** | Layout Engineering |
| **Target Date** | TBD |
| **Options** | (A) 6-layer (TDA4VL/AM62A only); (B) 8-layer (TDA4VM compatible); (C) 8-layer HDI (high density, smallest area) |
| **Recommendation** | 8-layer standard for prototype (PRELIMINARY) |
| **Rationale** | 8-layer supports both TDA4VL and TDA4VM BGA variants. HDI adds cost. 6-layer may be cost-reduced in production for Assist-only variant. |
| **Blocking** | PCB vendor selection, impedance calculations |
| **Dependencies** | OD-001, OD-002, OD-003 (single vs. dual PCB strategy) |

---

## 10. Production and Supply Chain Decisions

### OD-017: Sensor Dual-Source Strategy

| Field | Value |
|-------|-------|
| **ID** | OD-017 |
| **Subsystem** | Supply Chain |
| **Priority** | P3 - Medium |
| **Status** | OPEN |
| **Owner** | Procurement / Systems |
| **Target Date** | TBD |
| **Question** | Should the PCB footprint support pin-compatible alternate sensors for supply resilience? |
| **Options** | (A) Single-source optimized footprint; (B) Dual-source compatible footprint (if sensors share pinout); (C) Interposer PCBlet for sensor swap |
| **Recommendation** | Option B if pinout-compatible alternate exists (PRELIMINARY) |
| **Blocking** | Sensor module mechanical design |
| **Dependencies** | OD-004, OD-005, OD-007, OD-008 |

### OD-018: eMMC vs. UFS Storage Selection

| Field | Value |
|-------|-------|
| **ID** | OD-018 |
| **Subsystem** | Storage / Compute |
| **Priority** | P3 - Medium |
| **Status** | OPEN |
| **Owner** | Systems Engineering |
| **Target Date** | TBD |
| **Options** | (A) eMMC 5.1 (16/32GB, lower cost); (B) UFS 2.1 (higher throughput, slightly higher cost) |
| **Recommendation** | eMMC 5.1 (PRELIMINARY) |
| **Rationale** | eMMC sufficient for boot + model storage + event logging. UFS throughput not needed for v0.5 workload. Cost-down priority. |
| **Blocking** | Storage partition planning, boot time analysis |
| **Dependencies** | OD-001 (SoC storage interface support) |

---

## 11. Decision Priority Summary

| Priority | Count | IDs |
|----------|-------|-----|
| P1 - Critical (blocks major milestone) | 6 | OD-001, OD-002, OD-003, OD-007, OD-009, OD-011 |
| P2 - High (blocks detailed design) | 8 | OD-004, OD-005, OD-006, OD-008, OD-012, OD-013, OD-015, OD-016 |
| P3 - Medium (can be deferred to later phase) | 4 | OD-010, OD-014, OD-017, OD-018 |

---

## 12. Decision Dependencies Graph

```
OD-001 (SoC Assist) ----+----> OD-003 (Single/Dual PCB)
                         |
OD-002 (SoC Control) ---+----> OD-011 (Thermal feasibility)
                         |          |
                         |          v
                         +----> OD-012 (Housing dimensions)
                         |          |
                         |          v
                         +----> OD-016 (PCB stackup)
                         |
OD-004 (FWD sensor) ----+----> OD-006 (MIPI lane count)
OD-005 (FWD sensor Ctrl)+          |
                         |          v
OD-007 (DMS sensor) ----+----> OD-013 (IR wavelength) --> OD-014 (IR driver)
OD-008 (DMS sensor Ctrl)+          |
                                    v
                              OD-015 (DMS flex cable)

OD-009 (SDK selection) depends on OD-001, OD-002
OD-010 (DL models) depends on OD-001, OD-009
OD-017 (Dual-source) depends on OD-004, OD-005, OD-007, OD-008
OD-018 (Storage) depends on OD-001
```

---

## 13. Next Steps

1. Schedule SoC selection review meeting (resolve OD-001, OD-002)
2. Request TI samples: TDA4VL-Q1 EVM, TDA4VM SK (if not already available)
3. Request sensor evaluation kits: OX03C10, OX01N1B, IMX390
4. Initiate thermal simulation for windshield-mount module (OD-011)
5. Begin SDK evaluation on TDA4VM SK platform (OD-009)
6. Define housing envelope options with mechanical team (OD-012)
7. Confirm J722S availability timeline and SDK roadmap with TI FAE

---

## 14. Revision History

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| 0.1 | 2026-07 | Systems Engineering | Initial open decisions register for v0.5 compact module |

---

*PRELIMINARY - All recommendations subject to evaluation results and vendor confirmation*

*End of Document*
