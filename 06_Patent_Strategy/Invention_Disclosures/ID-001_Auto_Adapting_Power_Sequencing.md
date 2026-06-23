# Invention Disclosure: ID-001

## 1. Title

SoC-Adaptive Dual-Vision Smart Camera Platform

## 2. Date

January 2025

## 3. Inventors

[To be filled - engineering team members who contributed to this concept]

## 4. Status

DRAFT - Awaiting prior art search completion

---

## 5. Problem Statement

Current automotive ADAS and DMS camera systems are built as fixed-function designs that couple the processing module (SoC) to the carrier/interface board. When an OEM requires a different SoC variant (for cost, performance, or supply chain reasons), the entire camera module must be redesigned. This creates several critical problems:

- **High NRE cost**: Each SoC change triggers full carrier board redesign (schematic, layout, validation)
- **Extended time-to-market**: 12-18 months per SoC variant carrier redesign cycle
- **Supply chain fragility**: Single-source SoC dependency creates production risk
- **Tier differentiation difficulty**: Entry, mid, and high-tier products cannot share common hardware
- **Dual-vision integration gap**: No existing platform supports both forward-facing ADAS and cabin-facing DMS cameras on a single adaptive carrier

No commercially available platform allows a single carrier board to support multiple SoC families while simultaneously integrating dual-camera (forward ADAS + cabin DMS) functionality.

## 6. Background / Prior Art Summary

### Existing Approaches

| Approach | Example | Limitation |
|----------|---------|------------|
| Fixed SoC designs | Mobileye EyeQ, Bosch MPC | Tied to single SoC; redesign required for variant |
| NVIDIA compute modules | Jetson AGX/Orin | Not automotive-qualified; single SoC family only |
| COM Express modules | Various | Not designed for automotive environment; no camera integration |
| Qualcomm Ride Platform | SA8295P | Vertically integrated; no multi-SoC carrier concept |

### Key Patents Reviewed

- TI power sequencing patents (fixed sequence controllers)
- NVIDIA Jetson carrier board architecture (consumer/industrial, not automotive)
- Intel/Mobileye integrated vision processor packages
- Various COM Express module connector standards (PICMG)

### Gap in Prior Art

No known system combines:
1. A single automotive-qualified carrier supporting multiple SoC module variants
2. Hardware-autonomous SoM identity detection and power profile adaptation
3. Integrated dual-camera (ADAS + DMS) interface on the same adaptive carrier
4. Software-defined tier scaling from a common hardware base

## 7. Proposed Solution

The ADVIS SoC-Adaptive Dual-Vision Smart Camera Platform comprises:

1. **Universal Carrier Board**: A single automotive-qualified carrier PCB designed to host interchangeable System-on-Module (SoM) blades from different SoC families (e.g., TDA4VM class, AM68A class, and future variants)

2. **SoM Identity Detection**: Hardware-level module identification that operates before any software executes, detecting the installed SoM type via encoded identification signals

3. **Adaptive Power Sequencing**: Power management system that reads the SoM power profile requirements and configures regulator enable sequencing, timing delays, and rail validation without firmware intervention

4. **Dual-Camera Interface Architecture**: Integrated deserializer and CSI-2 routing that supports both forward-facing ADAS camera and cabin-facing DMS camera through a common interface layer

5. **Software-Defined Tier Scaling**: The same hardware platform supports multiple ADAS capability tiers (Assist, Control, Fleet, Fusion) through software configuration rather than hardware changes

## 8. Key Novel Elements

1. **Single carrier, multiple SoC families**: One automotive PCB design accommodates different SoC processing modules without hardware modification
2. **Hardware-autonomous SoM detection**: Identity resolution occurs at the hardware level before boot, enabling correct power sequencing without firmware dependency
3. **Adaptive power profile switching**: The power subsystem reconfigures itself (enable sequence, timing, rail validation) based on detected module identity
4. **Dual-vision on adaptive platform**: Both ADAS and DMS camera interfaces are integrated on the same SoC-adaptive carrier
5. **Fail-safe default behavior**: If SoM identity cannot be resolved, the system defaults to the most conservative power sequencing profile, preventing hardware damage

## 9. Technical Implementation Details

### Architecture Overview

```
+----------------------------------------------------------+
|              ADVIS Universal Carrier Board                |
|                                                          |
|  +-----------+    +------------------+    +-----------+  |
|  | SoM       |    | Power Management |    | Camera    |  |
|  | Interface |    | (Adaptive)       |    | Interface |  |
|  | Connector |    |                  |    |           |  |
|  |           |    | - ID Detection   |    | - ADAS    |  |
|  | - ID pins |    | - Seq. Logic     |    |   Deser   |  |
|  | - Power   |    | - Rail Monitor   |    | - DMS     |  |
|  | - Data    |    | - Fault Protect  |    |   Deser   |  |
|  +-----------+    +------------------+    +-----------+  |
|         |                  |                     |        |
|  +------v------------------v---------------------v-----+ |
|  |           Common Carrier Infrastructure             | |
|  |  CAN-FD | GNSS | IMU | Watchdog | USB | IR LED     | |
|  +---------------------------------------------------------+
|                                                          |
+----------------------------------------------------------+
```

### SoM Detection Mechanism

- Module identification encoded on dedicated interface pins at the SoM connector
- Detection circuitry reads identification state during initial power application
- Identification result selects the corresponding power sequencing profile from hardware logic
- No microcontroller or firmware required for the detection and sequencing process

### Adaptive Power Sequencing

- Power sequencing controller with multiple profile configurations stored in hardware
- Enable chain ordering, timing delays, and power-good validation adapted per profile
- Protection mechanisms active regardless of selected profile (over-current, over-voltage, thermal)
- Graceful degradation: if any rail fails sequencing validation, subsequent rails are held off

### Dual-Camera Interface

- Forward-facing camera: deserializer receives ADAS perception data via coaxial link
- Cabin-facing camera: deserializer receives DMS data via coaxial or direct MIPI link
- Both camera data streams routed to the SoM via standard CSI-2 interface
- Camera interface operates independently of SoM variant (common electrical interface)

## 10. Advantages Over Prior Art

| Advantage | Benefit | vs. Competitors |
|-----------|---------|-----------------|
| Single carrier design | 60-70% NRE reduction for SoC variants | Mobileye, Continental require full redesign |
| Hardware-autonomous detection | Zero-firmware boot dependency | NVIDIA Jetson requires SW-based detection |
| Multi-SoC support | Supply chain resilience | All competitors tied to single SoC |
| Dual-vision integration | Single module replaces two ECUs | Competitors use separate ADAS + DMS modules |
| Software-defined tiers | One BOM for multiple product tiers | Competitors need different HW per tier |
| Automotive-qualified design | Direct vehicle integration | COM Express not automotive-grade |

## 11. Alternative Embodiments

1. **FPGA-based sequencing**: Replace hardware logic with a small FPGA for maximum flexibility in profile configuration
2. **I2C EEPROM identification**: Use serial EEPROM on SoM for richer identity data (version, power map, thermal limits)
3. **Resistor-coded identification**: Simpler approach using resistor divider networks for SoM identification
4. **Triple-camera variant**: Extend to three cameras (forward, cabin, surround/parking) on the same adaptive carrier
5. **Stacked module architecture**: Vertical SoM mounting for ultra-compact form factors
6. **Wireless SoM identification**: NFC tag on SoM read during manufacturing/service for configuration logging

## 12. Potential Claims

### Independent Claim 1 (System)

A smart camera platform for an automotive vehicle, comprising:
- a carrier printed circuit board configured for mounting within a vehicle;
- a module connector interface configured to receive any one of a plurality of system-on-module (SoM) variants, each SoM variant comprising a different system-on-chip processor;
- an identification detection circuit coupled to said module connector interface, configured to determine an identity of an installed SoM variant based on electrical signals present at said module connector interface upon power application;
- an adaptive power sequencing circuit responsive to said identification detection circuit, configured to select from a plurality of power sequencing profiles corresponding to said plurality of SoM variants and to energize power rails in an order and timing determined by the selected profile;
- a first camera interface configured to receive image data from a forward-facing perception camera; and
- a second camera interface configured to receive image data from a cabin-facing driver monitoring camera;
- wherein said first and second camera interfaces route received image data to the installed SoM variant via a common data bus interface.

### Independent Claim 2 (Method)

A method of operating an adaptive camera platform in an automotive vehicle, comprising:
- detecting, by hardware circuitry and without firmware execution, an identity of a processing module installed on a carrier board;
- selecting, responsive to said detected identity, a power sequencing profile from among a plurality of stored profiles;
- energizing power rails of said carrier board according to said selected power sequencing profile;
- receiving forward-facing image data from an advanced driver assistance camera via a first deserializer;
- receiving cabin-facing image data from a driver monitoring camera via a second deserializer; and
- routing said forward-facing image data and said cabin-facing image data to said processing module via a common serial interface.

### Independent Claim 3 (Computer-Readable Medium / Configuration)

A hardware configuration stored in a non-volatile manner on an automotive camera carrier board, the configuration comprising:
- a plurality of power sequencing profiles, each profile specifying rail enable ordering, timing constraints, and power-good validation criteria for a corresponding system-on-module variant;
- an identity mapping associating electrical identification states with said plurality of profiles; and
- a fail-safe default profile specifying the most conservative sequencing among said plurality of profiles;
- wherein said configuration is readable by power sequencing hardware to autonomously configure power delivery without software intervention.

### Dependent Claims

4. The platform of claim 1, wherein said identification detection circuit operates without a microcontroller.
5. The platform of claim 1, further comprising a safety watchdog circuit that validates power sequencing completion before enabling peripheral subsystems.
6. The platform of claim 1, wherein said plurality of SoM variants span at least two different SoC product families from different semiconductor vendors.
7. The method of claim 2, further comprising defaulting to a most conservative power sequencing profile if said identity detection fails.
8. The method of claim 2, wherein said common serial interface is a MIPI CSI-2 interface.
9. The platform of claim 1, further comprising a vehicle communication interface (CAN-FD) common to all SoM variants.
10. The platform of claim 1, wherein said carrier board meets automotive temperature range (-40C to +105C) qualification.
11. The method of claim 2, further comprising scaling ADAS processing capability through software configuration without changing hardware.
12. The platform of claim 1, wherein said adaptive power sequencing circuit provides fault protection independent of the selected sequencing profile.

## 13. Drawings / Figures Description

### Figure 1: System Architecture Block Diagram
- Shows universal carrier board with SoM connector, power management block, dual camera interfaces
- Indicates interchangeable SoM modules (Variant A, B, C) docking to the same carrier
- Labels all major subsystems and signal paths

### Figure 2: SoM Identity Detection Flow
- Flowchart showing: Power applied -> Read ID pins -> Decode identity -> Select profile -> Execute sequence
- Includes fail-safe path for unrecognized identity
- Shows timing relationships

### Figure 3: Power Sequencing Profiles
- Timing diagram showing different rail enable sequences for 3 SoC variants
- Indicates power-good validation checkpoints
- Shows fault protection intervention points

### Figure 4: Dual-Camera Data Path
- Signal flow from ADAS camera through deserializer to SoM
- Signal flow from DMS camera through deserializer to SoM
- Common CSI-2 bus routing to processing module

### Figure 5: Platform Tier Scaling
- Diagram showing single hardware platform mapped to Assist, Control, Fleet, Fusion tiers
- Software-defined feature enablement without hardware changes

## 14. Commercial Value

### Market Opportunity

- Global ADAS camera module market: $8.5B by 2027 (growing 15% CAGR)
- DMS market driven by Euro NCAP 2026 and US regulations: $2.1B by 2027
- Combined ADAS+DMS module opportunity eliminates need for two separate ECUs

### Revenue Model

| Revenue Stream | Estimated Value |
|---------------|-----------------|
| Platform license (per unit) | $2-5 per unit royalty |
| Design license (one-time) | $500K-2M per OEM |
| SoM certification program | $50K-100K per SoC vendor |
| Engineering services | Time and materials |

### Cost Advantage

- Single carrier design vs. per-SoC designs: 60-70% NRE reduction
- Dual-vision integration: eliminates separate DMS ECU ($20-40 cost saving per vehicle)
- Supply chain flexibility: reduces single-source SoC risk premium

## 15. Filing Recommendation

**Recommendation: File Provisional Patent Application within 90 days**

- **Filing type**: Provisional (US) initially to establish priority date
- **Conversion**: Non-provisional within 12 months
- **International**: PCT application recommended given global automotive market
- **Priority territories**: US, EU (Germany), China, Japan, South Korea, India
- **Urgency**: High - competitors may develop similar adaptive platform concepts as multi-SoC strategies become more common

## 16. Confidentiality Classification

| Element | Classification |
|---------|---------------|
| General concept (adaptive SoC platform) | PATENT - Public upon filing |
| Block diagrams and architecture | PATENT - Public upon filing |
| Exact carrier pinout specification | TRADE SECRET - Never disclose |
| PCB routing rules and layer assignment | TRADE SECRET - Never disclose |
| Specific power sequencing timing values | TRADE SECRET - Never disclose |
| Calibration thresholds and parameters | TRADE SECRET - Never disclose |
| SoM detection algorithm details | PATENT - Architecture level only |

## 17. Next Steps

- [ ] Complete comprehensive prior art search (USPTO, EPO, WIPO)
- [ ] Confirm no blocking patents from TI, NXP, Qualcomm, Renesas
- [ ] Develop formal patent drawings (5 figures minimum)
- [ ] Review with patent attorney for claim refinement
- [ ] Prepare provisional application filing package
- [ ] Identify potential continuation applications (divisional claims)
- [ ] Coordinate with ID-003, ID-004, ID-005 for cross-referencing claims
- [ ] Budget allocation: provisional filing ($3K-5K estimated)

---

**Document Version:** 2.0  
**Last Updated:** 2025-01  
**Classification:** CONFIDENTIAL - Attorney-Client Privilege  
**Witness Signature:** _________________ Date: _________  
**Witness Signature:** _________________ Date: _________
