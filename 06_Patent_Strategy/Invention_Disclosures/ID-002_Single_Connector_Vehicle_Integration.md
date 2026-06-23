# Invention Disclosure: ID-002

## 1. Title

Compact Dual-Facing Windshield Module with Integrated Thermal/EMC Stack

## 2. Date

January 2025

## 3. Inventors

[To be filled - engineering team members who contributed to this concept]

## 4. Status

DRAFT - Awaiting prior art search completion

---

## 5. Problem Statement

Automotive vision systems that combine forward-facing ADAS and cabin-facing DMS functionality face severe physical constraints when mounted on the windshield:

- **Thermal challenge**: High-performance SoCs generate 5-15W in a sealed enclosure with limited convective cooling, positioned behind glass that acts as a thermal insulator
- **EMC challenge**: High-speed camera deserializers, SoC digital logic, and CAN-FD transceivers generate broadband EMI that must be contained within millimeters of sensitive RF receivers (GNSS) and camera sensor analog front-ends
- **Form factor constraint**: Windshield-mount modules must be compact enough to fit behind the rearview mirror without obstructing driver vision or triggering regulatory visibility concerns
- **Dual-facing optical challenge**: Forward and cabin cameras require opposing optical paths within a single compact housing

No existing commercially available module solves all four constraints simultaneously in a single windshield-mounted package.

## 6. Background / Prior Art Summary

### Existing Approaches

| Approach | Example | Limitation |
|----------|---------|------------|
| Separate ADAS + DMS modules | Mobileye + Seeing Machines | Two mounting points, two harnesses, higher cost |
| Large dashboard-mounted units | Continental MFC500 | Too large for windshield; not dual-facing |
| Aftermarket DMS dongles | Various | No ADAS integration; consumer-grade thermal |
| IP camera form factors | Axis, Bosch Security | Not automotive-qualified; no EMC compliance |

### Key Patents Reviewed

- Mobileye windshield camera housing patents (single-facing only)
- Bosch camera module thermal management (large format, not compact dual-facing)
- Continental camera EMC shielding (standard approaches, not integrated stack)
- Gentex mirror-integrated camera concepts (mirror-mounted, different constraints)

### Gap in Prior Art

No known design combines:
1. Dual opposing optical paths (forward + cabin) in a single compact windshield housing
2. Integrated thermal management stack optimized for windshield mounting thermal constraints
3. EMC containment architecture that isolates high-speed digital from sensitive analog within millimeters
4. Automotive-qualified (-40C to +105C) operation in a package small enough for windshield concealment

## 7. Proposed Solution

The ADVIS Compact Dual-Facing Windshield Module comprises:

1. **Dual-Optical-Path Housing**: A single compact enclosure with opposing optical apertures - one facing forward through the windshield for ADAS perception, one facing the cabin for DMS monitoring

2. **Integrated Thermal Stack**: A layered thermal management architecture that conducts heat from the SoC through a structured thermal path to an external dissipation surface, optimized for the limited airflow available in windshield-mount position

3. **EMC Containment Architecture**: A compartmentalized internal structure that provides electromagnetic isolation between high-speed digital domains (SoC, deserializer), sensitive analog domains (camera sensors, GNSS), and vehicle interface domains (CAN-FD)

4. **Compact Form Factor**: Overall dimensions designed to fit within the shadow zone behind a standard automotive rearview mirror, complying with forward visibility regulations

5. **Structural Integration**: The thermal and EMC elements serve dual structural purposes, reducing part count while providing both thermal conductivity and electromagnetic shielding

## 8. Key Novel Elements

1. **Dual-optical-path windshield housing**: Single compact module with opposing camera apertures, eliminating need for two separate mounted units
2. **Integrated thermal/structural/EMC stack**: Layered internal architecture where thermal spreaders, EMC shields, and structural elements are combined into a unified multi-function stack
3. **Windshield-optimized thermal path**: Thermal design specifically engineered for the unique constraints of windshield mounting (glass thermal barrier, limited convection, solar loading)
4. **Compartmentalized EMC zones**: Internal partitioning that achieves EMC compliance without external shielding cans or gaskets that would increase module volume
5. **Mirror-shadow form factor**: Physical dimensions and mounting geometry designed to utilize the aerodynamic and visual shadow of the rearview mirror

## 9. Technical Implementation Details

### Module Architecture

```
+--------------------------------------------------+
|          ADVIS Windshield Module (Top View)       |
|                                                  |
|  +--------------------+  +--------------------+  |
|  | FORWARD CAMERA     |  | CABIN CAMERA       |  |
|  | (ADAS Perception)  |  | (DMS Monitoring)   |  |
|  |                    |  |                    |  |
|  |  Lens + Sensor     |  |  Lens + Sensor     |  |
|  |  + IR-cut filter   |  |  + IR-pass filter  |  |
|  +--------------------+  +--------------------+  |
|              |                    |               |
|  +-----------v--------------------v-----------+  |
|  |         Processing + Interface Layer        |  |
|  |  Deserializer | SoC Module | CAN-FD | GNSS |  |
|  +------------------------------------------------+
|  |         Thermal/EMC Stack Layer             |  |
|  |  Thermal spreader | EMC partition | Ground  |  |
|  +------------------------------------------------+
|                                                  |
+--------------------------------------------------+
```

### Thermal Management Stack

```
Cross-Section (Side View):

  [Windshield Glass]
       |
  [Adhesive Mount Pad]
       |
  [Module Housing - Top Shell]
       |
  [Camera Sensors + Optics]
       |
  [Processing Layer (SoC, Deser)]
       |
  [Thermal Interface Material]
       |
  [Thermal Spreader Plate]  <-- Conducts heat laterally
       |
  [EMC/Structural Partition]
       |
  [External Dissipation Surface]
       |
  [Cabin Air (natural convection)]
```

- Heat flows from SoC downward through thermal interface material to spreader plate
- Spreader distributes heat laterally to maximize surface area exposed to cabin air
- Module orientation places thermal dissipation surface facing downward into cabin airflow
- No active cooling (fan-less) for reliability and acoustic requirements

### EMC Compartmentalization

```
+-----------------------------------------------------------+
|  Zone A: High-Speed Digital     | Zone B: Analog/Sensor   |
|  - SoC + DDR memory            | - Camera sensor AFE     |
|  - Deserializer HSDI           | - GNSS RF front-end     |
|  - USB 2.0 interface           | - IMU analog circuits   |
|                                |                         |
|  [EMC Partition Wall]          | [EMC Partition Wall]    |
|-------------------------------|--------------------------|
|  Zone C: Vehicle Interface     | Zone D: Power            |
|  - CAN-FD transceiver         | - DC-DC converters      |
|  - Connector interface         | - LDO regulators        |
|  - Wake/sleep logic           | - Input protection      |
+-----------------------------------------------------------+
```

### Mechanical Envelope

- Target dimensions: approximately 80mm x 50mm x 30mm (L x W x H)
- Weight target: less than 150g including optics
- Mounting: automotive-grade adhesive pad to windshield inner surface
- IP rating: IP52 minimum (dust protected, drip proof)
- Operating temperature: -40C to +85C ambient, +105C SoC junction

## 10. Advantages Over Prior Art

| Advantage | Benefit | vs. Competitors |
|-----------|---------|-----------------|
| Single dual-facing module | Eliminates second ECU and harness | Competitors need separate ADAS + DMS units |
| Integrated thermal/EMC stack | Fewer parts, smaller package | Traditional designs use separate thermal and EMC solutions |
| Windshield-optimized thermal | Reliable operation without fan | Large modules require active cooling or dashboard mount |
| Mirror-shadow mounting | Invisible to driver, regulation compliant | Larger modules obstruct vision or require dashboard cutout |
| Combined structural elements | Lower BOM cost, lighter weight | Competitors use discrete shields, spreaders, brackets |
| Automotive-qualified compact package | Direct OEM integration | Aftermarket solutions lack automotive qualification |

## 11. Alternative Embodiments

1. **Active thermal assist**: Optional thermoelectric cooler (TEC) for extreme ambient conditions (desert climates)
2. **Windshield-conductive thermal path**: Use windshield glass itself as a thermal spreader by thermally coupling the module to a larger glass area
3. **Modular optical cassette**: Replaceable camera/lens assemblies for field upgrade of sensor resolution
4. **Split-module architecture**: Two smaller linked housings (one forward, one cabin) connected by a thin bridge
5. **Integrated rearview mirror housing**: Module built directly into the rearview mirror housing assembly
6. **Phase-change thermal material**: Use phase-change material for thermal buffering during high-compute burst operations

## 12. Potential Claims

### Independent Claim 1 (Apparatus)

A compact camera module for mounting on an interior surface of a vehicle windshield, comprising:
- a housing having a first optical aperture oriented toward the exterior of the vehicle for receiving a forward scene and a second optical aperture oriented toward the interior of the vehicle for receiving a cabin scene;
- a first image sensor positioned to receive light through said first optical aperture;
- a second image sensor positioned to receive light through said second optical aperture;
- a processing module disposed within said housing and configured to receive and process image data from both said first and second image sensors;
- a thermal management stack disposed within said housing, comprising at least a thermal spreader element configured to conduct heat from said processing module to a dissipation surface of said housing; and
- an electromagnetic compatibility structure comprising at least one internal partition separating a high-speed digital domain containing said processing module from an analog domain containing said image sensors.

### Independent Claim 2 (Method of Thermal Management)

A method of managing thermal energy in a windshield-mounted dual-camera automotive module, comprising:
- generating heat by processing image data from a forward-facing camera and a cabin-facing camera within a sealed compact housing mounted to vehicle windshield glass;
- conducting said heat from a processing element through a thermal interface to a thermal spreader element;
- distributing said heat laterally across said thermal spreader to increase effective dissipation area;
- radiating and convecting said distributed heat from an external surface of said housing into cabin air;
- wherein said thermal management is accomplished without active cooling elements and within a housing envelope that fits within a shadow zone of a vehicle rearview mirror.

### Independent Claim 3 (EMC Architecture)

An electromagnetic compatibility architecture for a compact automotive camera module, comprising:
- a housing containing a plurality of electronic subsystems including at least a high-speed digital processing subsystem and an analog imaging subsystem;
- at least one internal electromagnetic partition disposed between said high-speed digital processing subsystem and said analog imaging subsystem;
- wherein said electromagnetic partition simultaneously serves as a structural support element and a thermal conduction path;
- wherein said housing is dimensioned for mounting on a vehicle windshield interior surface in a region obscured by a rearview mirror.

### Dependent Claims

4. The module of claim 1, wherein said thermal management stack and said electromagnetic compatibility structure share at least one common structural element.
5. The module of claim 1, wherein said housing dimensions do not exceed 100mm in any axis.
6. The module of claim 1, further comprising an infrared illumination source oriented toward said second optical aperture for cabin monitoring in low-light conditions.
7. The method of claim 2, further comprising modulating processing load to maintain junction temperature below a thermal threshold.
8. The module of claim 1, further comprising a vehicle communication interface (CAN-FD) disposed within an electromagnetically isolated zone of said housing.
9. The module of claim 1, wherein said housing is attached to said windshield via an automotive-grade adhesive pad.
10. The architecture of claim 3, wherein said housing contains at least four electromagnetically isolated zones.
11. The module of claim 1, further comprising a global navigation satellite system receiver with antenna, isolated from said high-speed digital domain by said electromagnetic compatibility structure.
12. The module of claim 1, qualified for automotive operation over -40C to +105C temperature range.

## 13. Drawings / Figures Description

### Figure 1: Module External View
- Isometric rendering showing compact housing with two opposing lens apertures
- Mounting surface (adhesive pad) visible on top face
- Vehicle connector on rear face
- Dimensional annotations

### Figure 2: Exploded Assembly View
- All internal layers separated: top shell, camera modules, processing board, thermal stack, EMC partitions, bottom shell
- Assembly order indicated

### Figure 3: Thermal Stack Cross-Section
- Detailed cross-section showing heat flow path from SoC to external surface
- Temperature gradient annotations at each layer interface
- Thermal resistance chain diagram

### Figure 4: EMC Zone Layout (Top View)
- Four-zone compartmentalization shown from above
- Partition wall locations and grounding points
- Signal routing channels between zones

### Figure 5: Vehicle Installation Context
- Module shown mounted on windshield behind rearview mirror
- Forward and cabin optical paths illustrated with field-of-view cones
- Dimensional relationship to mirror shadow zone

## 14. Commercial Value

### Market Opportunity

- Combined ADAS+DMS windshield module market emerging as Euro NCAP 2026 mandates DMS
- OEMs seeking single-module solutions to reduce integration cost and complexity
- Estimated 15M+ vehicles/year requiring combined ADAS+DMS by 2028

### Revenue Model

| Revenue Stream | Estimated Value |
|---------------|-----------------|
| Module supply (per unit) | $80-150 per module |
| Design license to Tier-1 | $1M-3M per licensee |
| Thermal/EMC IP license | $200K-500K per application |

### Cost Advantage

- Single module vs. dual separate modules: $30-50 per vehicle saving for OEM
- Reduced harness complexity: $10-15 per vehicle saving
- Single mounting operation vs. dual: labor saving at assembly

## 15. Filing Recommendation

**Recommendation: File Provisional Patent Application within 90 days**

- **Filing type**: Provisional (US) for priority date
- **Conversion**: Non-provisional within 12 months
- **Design patent**: Separate design patent application for module external appearance
- **International**: PCT filing recommended (global automotive market)
- **Priority territories**: US, EU (Germany), China, Japan, South Korea
- **Urgency**: High - physical form factor innovations are easily visible to competitors once products ship

## 16. Confidentiality Classification

| Element | Classification |
|---------|---------------|
| General concept (dual-facing windshield module) | PATENT - Public upon filing |
| Thermal/EMC stack architecture | PATENT - Public upon filing |
| Exact thermal interface material selection | TRADE SECRET - Never disclose |
| Specific PCB stackup and layer assignment | TRADE SECRET - Never disclose |
| EMI mitigation recipes (filter values, trace geometry) | TRADE SECRET - Never disclose |
| Exact mechanical dimensions and tolerances | PATENT - General ranges only |
| Mounting adhesive specification | TRADE SECRET - Never disclose |

## 17. Next Steps

- [ ] Complete prior art search focused on windshield-mount camera thermal patents
- [ ] Survey competitor module dimensions (Mobileye EyeQ6, Continental MFC, Bosch MPC3)
- [ ] Thermal simulation: validate spreader concept meets junction temperature targets
- [ ] EMC simulation: confirm partition effectiveness at relevant frequencies
- [ ] Prepare design patent application for external form factor
- [ ] Coordinate with mechanical engineering for prototype housing
- [ ] Review with patent attorney for claim scope optimization
- [ ] Budget allocation: provisional filing ($3K-5K) + design patent ($2K-3K)

---

**Document Version:** 2.0  
**Last Updated:** 2025-01  
**Classification:** CONFIDENTIAL - Attorney-Client Privilege  
**Witness Signature:** _________________ Date: _________  
**Witness Signature:** _________________ Date: _________
