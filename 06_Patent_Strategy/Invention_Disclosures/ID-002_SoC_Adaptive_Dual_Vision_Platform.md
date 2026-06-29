# Invention Disclosure: ID-002

## CONFIDENTIAL - INTERNAL DRAFT

---

## 1. Title

SoC-Adaptive Dual-Vision Smart Camera Platform

## 2. Date

June 2026

## 3. Inventors

[To be filled - engineering team members who contributed to this concept]

## 4. Status

DRAFT - Awaiting prior art search and patent attorney review

---

## 5. Problem Statement

Automotive ADAS camera platforms are designed around a specific SoC, creating inflexible hardware that cannot adapt when OEMs require different processing capability, cost points, or supply chain alternatives. Key problems include:

- Each SoC change triggers a full carrier board redesign (12-18 month cycle)
- Single-source SoC dependency creates production risk
- Entry, mid, and high-tier products cannot share a common PCB platform
- No commercially available automotive camera platform supports multiple SoC families on a single carrier while integrating dual-camera (ADAS + DMS) functionality

## 6. Background / Prior Art Summary

### Existing Approaches

| Approach | Example | Limitation |
|----------|---------|------------|
| Fixed SoC camera designs | Mobileye EyeQ, Bosch MPC | Tied to single SoC; full redesign per variant |
| NVIDIA Jetson modules | AGX Orin | Single SoC family; not automotive-qualified carrier |
| COM Express modules | Various | Not automotive-grade; no integrated camera interface |
| TI EVM platforms | TDA4x EVM | Development tool only; not production-intent |

### Gap in Prior Art

No known system combines:
1. A single automotive-qualified carrier supporting multiple SoC module variants
2. Hardware-autonomous SoM/SiP identity detection and power profile adaptation
3. Integrated dual-camera (ADAS forward + DMS cabin) interface on the same adaptive platform
4. Software-defined product tier scaling from common hardware

## 7. Proposed Solution

The ADVIS SoC-Adaptive Dual-Vision Platform comprises:

1. **Adaptive Carrier Board:** Single automotive-qualified PCB designed to host different SoC configurations (SOM blade, SiP, or direct-mount variants from TDA4VL, TDA4VM, AM62A families)
2. **Hardware Identity Detection:** Module identification mechanism that operates before boot, detecting installed SoC variant via encoded identification signals (resistor network, EEPROM, or pin coding)
3. **Adaptive Power Sequencing:** Power management that reads the SoC identity and configures rail enable ordering, timing, and validation without firmware intervention
4. **Dual-Camera Interface:** Integrated forward + DMS camera interfaces (direct MIPI CSI-2) that operate identically regardless of installed SoC variant
5. **Tier Scaling:** Same hardware supports Assist, Control, Fleet, and Fusion product tiers through software/firmware differentiation

## 8. Key Novel Elements

1. **Single carrier, multiple SoC families:** One automotive PCB accommodates different SoC processing modules
2. **Hardware-autonomous identity detection:** Identity resolved before boot; no firmware dependency
3. **Adaptive power profile:** Power subsystem self-configures based on detected module identity
4. **Dual-vision integration on adaptive platform:** Both ADAS and DMS cameras on the same SoC-flexible carrier
5. **Fail-safe default:** Unrecognized SoC identity defaults to most conservative power profile

## 9. Technical Implementation Details

### Architecture Overview

```
+--------------------------------------------------+
|         ADVIS Adaptive Carrier Board             |
|                                                  |
|  [SoC Interface]  [Power Management]  [Camera]   |
|   - ID detection   - Profile select   - MIPI Rx  |
|   - Power pins     - Seq. logic       - Forward  |
|   - CSI-2 data     - Rail monitor     - DMS      |
|                                                  |
|  [Common Infrastructure]                         |
|   CAN-FD | Watchdog | IR | ESD | Power input    |
+--------------------------------------------------+
```

### Identity Detection Mechanism

- Dedicated ID pins at SoC interface read during initial power application
- Resistor-coded or EEPROM-based identification
- Detection result selects power sequencing profile from hardware logic
- No microcontroller or firmware required for detection process

### Adaptive Power Sequencing

- Multiple power profiles stored in hardware configuration
- Each profile specifies enable ordering, timing delays, power-good criteria
- Protection mechanisms (OCP, OVP, thermal) active regardless of profile
- Graceful hold-off if any rail fails validation

### Dual-Camera Interface

- Forward camera: MIPI CSI-2 lanes routed to SoC CSI-Rx port 0
- DMS camera: MIPI CSI-2 lanes routed to SoC CSI-Rx port 1
- Interface electrically identical for all supported SoC variants
- Camera subsystem operates independently of SoC selection

*Note: Exact pinout, routing rules, and timing parameters are trade secrets and are not disclosed.*

## 10. Advantages Over Prior Art

| Advantage | Benefit |
|-----------|---------|
| Single carrier design | 60-70% NRE reduction for SoC variants |
| Hardware-autonomous detection | Zero firmware boot dependency for power safety |
| Multi-SoC support | Supply chain resilience; no single-source lock-in |
| Dual-vision integration | Single module replaces separate ADAS + DMS ECUs |
| Software-defined tiers | One BOM supports multiple product tiers |
| Automotive qualification | Direct vehicle deployment; not consumer-grade |

## 11. Alternative Embodiments

1. **FPGA-based sequencing:** Small FPGA replaces hardware logic for maximum profile flexibility
2. **NFC-tagged SoM:** NFC tag on module for manufacturing/service configuration logging
3. **Triple-camera extension:** Add surround/parking camera on same adaptive carrier
4. **Stacked module format:** Vertical SoC mounting for ultra-compact form factors
5. **Carrier-within-carrier:** Common base board with SoC-specific interposer daughter card

## 12. Potential Claims

### Independent Claim 1 (System)

A smart camera platform for an automotive vehicle, comprising:
- a carrier printed circuit board;
- a processing module interface configured to receive any one of a plurality of system-on-chip variants;
- an identification circuit configured to determine an identity of an installed processing variant upon power application without firmware execution;
- a power sequencing circuit responsive to said identification circuit, configured to select a power profile and energize power rails accordingly;
- a first camera interface receiving forward-facing image data via MIPI CSI-2; and
- a second camera interface receiving cabin-facing image data via MIPI CSI-2;
- wherein both camera interfaces route data to the installed processing variant via a common serial bus.

### Independent Claim 2 (Method)

A method of operating an adaptive camera platform, comprising:
- detecting, by hardware circuitry without firmware, an identity of a processing module;
- selecting a power sequencing profile from among stored profiles;
- energizing rails according to said profile;
- receiving forward-facing image data from a first camera; and
- receiving cabin-facing image data from a second camera;
- routing both image streams to said processing module.

### Dependent Claims

3. The platform of claim 1, wherein said identification circuit uses a resistor-coded network.
4. The platform of claim 1, further comprising a safety watchdog that validates sequencing completion.
5. The platform of claim 1, wherein said plurality of system-on-chip variants span at least two different product families.
6. The method of claim 2, further comprising defaulting to the most conservative profile if identity detection fails.

*Note: Final patent claim language must be reviewed by a patent attorney.*

## 13. Drawings / Figures Description

### Figure 1: Adaptive Platform Block Diagram
- Carrier board with interchangeable SoC module options shown

### Figure 2: Identity Detection Flow
- Flowchart: power applied, read ID, decode, select profile, execute sequence, fail-safe path

### Figure 3: Power Sequencing Profiles
- Timing diagrams for different SoC variants showing rail enable sequences

### Figure 4: Dual-Camera Data Path
- Signal flow from forward and DMS cameras through MIPI to SoC

## 14. Commercial Value

- Platform license revenue: $2-5 per unit royalty potential
- Design license: $500K-2M per OEM engagement
- Addresses $10B+ combined ADAS + DMS camera market
- Reduces OEM NRE for SoC changes by 60-70%
- Enables supply chain flexibility (critical post-2021 shortage experience)

## 15. Filing Recommendation

**Recommendation: File Provisional Patent Application**

- Filing type: Provisional (US) to establish priority date
- Conversion: Non-provisional within 12 months
- International: PCT recommended
- Priority territories: US, EU, China, Japan, South Korea
- Urgency: High - multi-SoC platform concept is increasingly valuable as SoC market fragments

## 16. Confidentiality Classification

| Element | Classification |
|---------|---------------|
| Adaptive platform concept | PATENT - Disclose in filing |
| Block-level architecture | PATENT - Disclose in filing |
| Exact carrier pinout | TRADE SECRET - Never disclose |
| PCB routing and layer assignment | TRADE SECRET - Never disclose |
| Power sequencing timing values | TRADE SECRET - Never disclose |
| SoM detection circuit detail | PATENT - Architecture level only |

## 17. Next Steps

- [ ] Complete prior art search (USPTO, EPO, WIPO)
- [ ] Verify no blocking patents from TI, NXP, Qualcomm, Renesas
- [ ] Develop formal patent drawings (minimum 4 figures)
- [ ] Review with patent attorney for claim refinement
- [ ] Prepare provisional application filing package
- [ ] Cross-reference with ID-003 (compact module) and ID-005 (power control)

---

**Document Version:** 1.0  
**Last Updated:** June 2026  
**Classification:** CONFIDENTIAL - INTERNAL DRAFT  
**Witness Signature:** _________________ Date: _________  
**Witness Signature:** _________________ Date: _________
