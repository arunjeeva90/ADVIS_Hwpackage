# Invention Disclosure: ID-003

## CONFIDENTIAL - INTERNAL DRAFT

---

## 1. Title

Compact Dual-Facing Windshield-Mounted Camera Module with Integrated Optical Isolation

## 2. Date

June 2026

## 3. Inventors

[To be filled - engineering team members who contributed to this concept]

## 4. Status

DRAFT - Awaiting prior art search and patent attorney review

---

## 5. Problem Statement

Automotive ADAS and DMS cameras are typically implemented as separate modules mounted in different vehicle locations. Combining both into a single windshield-mounted unit creates optical, thermal, and mechanical challenges that existing designs do not solve:

- Forward-facing and cabin-facing cameras share a confined housing, creating optical cross-talk risk
- NIR illumination for DMS can reflect off the windshield back into the forward camera
- Compact windshield mounting limits thermal dissipation (solar load + SoC heat)
- No existing compact module integrates both ADAS and DMS with adequate optical isolation in a form factor acceptable for OEM windshield mounting
- Existing dual-camera solutions are either too large, too expensive, or lack proper IR cross-talk prevention

## 6. Background / Prior Art Summary

### Existing Approaches

| Approach | Example | Limitation |
|----------|---------|------------|
| Separate ADAS + DMS modules | Bosch MPC + Smart Eye | Two mounting locations; two ECUs; higher cost |
| Rearview mirror integrated | Gentex + camera | Limited to simple cameras; no AI processing |
| Windshield-mount ADAS only | Mobileye EyeQ, DENSO | Forward only; no DMS integration |
| Large multi-camera modules | Continental surround view | Too large for windshield mount; not dual-facing |

### Gap in Prior Art

No known compact windshield-mounted module combines:
1. Forward road-facing ADAS camera and cabin-facing DMS camera in one housing
2. Integrated optical baffle preventing IR cross-contamination
3. Thermal management suitable for windshield-mount solar exposure
4. Form factor acceptable as OEM-grade interior component
5. Direct MIPI camera connection for cost optimization

## 7. Proposed Solution

A compact dual-facing windshield-mounted camera module comprising:

1. **Dual optical paths:** Forward camera faces through windshield; DMS camera faces inward toward cabin
2. **Integrated optical baffle:** Physical barrier between optical paths preventing NIR cross-talk
3. **IR window and filter:** Dedicated IR-pass window for DMS illumination, blocking visible light
4. **Compact thermal spreader:** Aluminum structure behind SoC, integrated into housing rear plate
5. **DMS pod offset:** DMS camera assembly offset via short rigid-flex, enabling optimal driver face angle
6. **OEM-grade housing:** Plastic + aluminum hybrid with concealed fasteners and sleek appearance
7. **Windshield bracket:** Adhesive + mechanical clip mounting system with coarse alignment

## 8. Key Novel Elements

1. **Integrated optical isolation in compact housing:** Baffle geometry prevents IR leakage between forward and cabin paths within minimal volume
2. **DMS pod with flex offset:** Camera pod extends from main housing via rigid-flex, allowing independent optical axis orientation
3. **Thermal spreader integrated into structural housing:** Rear aluminum plate serves both thermal and mechanical functions
4. **Windshield-mount form factor with full AI SoC:** Computing capability of a full ADAS+DMS system in compact windshield package
5. **IR reflection control:** Housing geometry and coatings prevent NIR from DMS bouncing off windshield into forward camera path

## 9. Technical Implementation Details

### Module Cross-Section

```
    [Windshield Glass]
          |
    [Forward Optical Window]  |  [Optical Baffle]  |  [DMS IR Window]
          |                   |                     |
    [Forward Camera]          |                     [DMS Camera + IR LEDs]
          |                   |                     |
    [Main PCB: SoC, Power, CAN, Watchdog]     [Flex Cable ~5cm]
          |
    [Thermal Spreader / Aluminum Rear Plate]
          |
    [Windshield Bracket]
```

### Optical Isolation Design

- Opaque baffle wall between forward and DMS optical chambers
- Baffle extends from PCB level to housing outer surface
- Matte black finish on all internal surfaces (minimize reflections at 850-940 nm)
- IR window positioned to direct DMS illumination toward cabin only
- Anti-reflection coating on windshield-facing surface of forward window

### DMS Pod Offset

- DMS camera + IR LEDs mounted on small sub-PCB
- Connected to main PCB via 50 mm rigid-flex cable
- Rigid-flex carries MIPI data, I2C, power, reset, IR control
- Pod angle optimized for driver face coverage from windshield mounting position

### Thermal Architecture

- SoC thermal pad connected to aluminum rear plate via TIM
- Aluminum plate area larger than SoC package (spreading effect)
- Housing design allows limited convective air flow over rear plate
- IR-reflective coating on forward-facing housing surfaces to reduce solar absorption
- Thermal shutdown protection as final safety mechanism

*Note: Exact mechanical dimensions, baffle geometry, and coating specifications are trade secrets.*

## 10. Advantages Over Prior Art

| Advantage | Benefit |
|-----------|---------|
| Single compact module | Replaces two separate ECUs; single harness connection |
| Integrated optical isolation | Prevents IR cross-talk without external shielding |
| DMS pod flexibility | Optimal cabin viewing angle independent of forward camera axis |
| OEM-grade appearance | Acceptable for premium vehicle interior |
| Windshield-mount thermal design | Operates in solar-exposed location |
| Cost-optimized | Direct MIPI, no SerDes overhead for co-located cameras |

## 11. Alternative Embodiments

1. **Rotating DMS pod:** Motorized DMS pod that adjusts angle for different driver heights
2. **Dual-wavelength IR:** Combined 850 nm + 940 nm illumination for different DMS modes
3. **Liquid lens DMS:** Electrically tunable focus for different driver distances
4. **Integrated display:** Small status display on cabin-facing surface
5. **Removable forward camera module:** Field-swappable forward camera for different FOV options
6. **Active thermal management:** Micro-fan or Peltier element for extreme thermal environments

## 12. Potential Claims

### Independent Claim 1 (Apparatus)

A compact camera module for mounting on a vehicle windshield, comprising:
- a housing having a first optical aperture facing toward a road scene through said windshield and a second optical aperture facing toward a vehicle cabin;
- a first image sensor positioned to receive light through said first optical aperture;
- a second image sensor positioned to receive light through said second optical aperture;
- an optical baffle disposed within said housing between said first and second optical apertures, configured to prevent electromagnetic radiation from passing between a first optical path and a second optical path;
- a near-infrared illumination source positioned adjacent to said second optical aperture, configured to illuminate a driver face; and
- a processing unit configured to receive image data from both said first and second image sensors and to generate vehicle safety messages.

### Independent Claim 2 (Method)

A method of manufacturing a dual-facing vehicle camera module, comprising:
- forming a housing with opposing optical apertures;
- installing an optical baffle between said apertures;
- mounting a first image sensor aligned with a windshield-facing aperture;
- mounting a second image sensor aligned with a cabin-facing aperture, offset from the main circuit board by a flexible circuit;
- positioning a thermal spreader in thermal contact with a processing device; and
- integrating said thermal spreader into a structural element of said housing.

### Dependent Claims

3. The module of claim 1, wherein said second image sensor is mounted on a sub-assembly connected to a main circuit board by a rigid-flex cable.
4. The module of claim 1, wherein said optical baffle includes a matte surface treatment having reflectance below a defined threshold at near-infrared wavelengths.
5. The module of claim 1, further comprising a windshield bracket providing coarse angular alignment of said module relative to a vehicle coordinate frame.
6. The module of claim 1, wherein said housing comprises a rear aluminum plate serving as both structural support and thermal spreader.

*Note: Final patent claim language must be reviewed by a patent attorney.*

## 13. Drawings / Figures Description

### Figure 1: Module Exploded View
- Housing components, baffle, cameras, PCB, thermal spreader, bracket

### Figure 2: Optical Path Cross-Section
- Forward and DMS light paths shown with baffle isolation

### Figure 3: DMS Pod and Flex Assembly
- Sub-PCB, flex cable, pod housing, IR window detail

### Figure 4: Thermal Path Diagram
- SoC to TIM to aluminum plate to ambient convection

### Figure 5: Vehicle Installation View
- Module mounted behind rearview mirror, windshield bracket detail

## 14. Commercial Value

- Design patent potential: Distinctive module appearance, DMS pod shape, IR window styling
- Utility patent: Optical isolation architecture, thermal integration, flex-offset DMS concept
- Market differentiator for OEMs seeking compact single-module ADAS+DMS solution
- Production cost advantage over dual-module (separate ADAS + DMS) approaches
- Addresses Euro NCAP 2026+ combined assessment requirement with minimal packaging impact

## 15. Filing Recommendation

**Recommendation: File Both Utility and Design Patent Applications**

- Utility patent: Optical isolation, thermal integration, DMS offset architecture
- Design patent: Module housing shape, DMS pod appearance, IR window styling, bracket
- Filing type: Provisional (US) for utility; Design application (US + Hague) for design
- Priority territories: US, EU, China, Japan, South Korea
- Urgency: High - compact ADAS+DMS modules are an active area of competitor development

## 16. Confidentiality Classification

| Element | Classification |
|---------|---------------|
| Dual-facing module concept | PATENT - Disclose in filing |
| Optical baffle architecture | PATENT - Disclose in filing |
| DMS pod offset concept | PATENT - Disclose in filing |
| Housing external appearance | DESIGN PATENT - Disclose in design filing |
| Exact mechanical dimensions | TRADE SECRET - Never disclose |
| Baffle coating formulation | TRADE SECRET - Never disclose |
| Thermal simulation results | TRADE SECRET - Never disclose |
| Manufacturing process details | TRADE SECRET - Never disclose |

## 17. Next Steps

- [ ] Complete prior art search (camera module patents, windshield-mount designs)
- [ ] Engage industrial designer for housing concept renderings
- [ ] Prepare design patent drawings (6-8 views per MPEP 1503.02)
- [ ] Review utility claims with patent attorney
- [ ] Coordinate with ID-001 (risk fusion) for single-module claims
- [ ] Prepare provisional application filing package
- [ ] Obtain 3D CAD model for patent drawings

---

**Document Version:** 1.0  
**Last Updated:** June 2026  
**Classification:** CONFIDENTIAL - INTERNAL DRAFT  
**Witness Signature:** _________________ Date: _________  
**Witness Signature:** _________________ Date: _________
