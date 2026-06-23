# Invention Disclosure: ID-004

## 1. Title

Dual-Camera Mutual Self-Calibration Using Shared Vehicle Geometry

## 2. Date

January 2025

## 3. Inventors

[To be filled - engineering team members who contributed to this concept]

## 4. Status

DRAFT - Awaiting prior art search completion

---

## 5. Problem Statement

Automotive camera systems require accurate calibration to function correctly. In a dual-facing camera module (forward ADAS + cabin DMS), calibration faces unique challenges:

- **Manufacturing tolerance**: Camera mounting angles vary unit-to-unit during assembly, requiring per-unit calibration
- **Field drift**: Windshield-mounted modules experience thermal cycling, vibration, and adhesive creep that alter camera alignment over time
- **No external targets in-field**: Traditional calibration requires targets (checkerboards, patterns) that are unavailable during normal vehicle operation
- **Dual-camera complexity**: Two cameras facing opposite directions cannot see the same external target simultaneously for relative calibration
- **Service cost**: Dealership recalibration after windshield replacement costs $200-500 and requires specialized equipment

No existing commercially available system allows two opposing cameras in a single module to mutually calibrate each other without external targets during normal vehicle operation.

## 6. Background / Prior Art Summary

### Existing Approaches

| Approach | Example | Limitation |
|----------|---------|------------|
| Factory calibration only | Most ADAS cameras | No field drift correction; requires service for recalibration |
| Ego-motion auto-calibration | Mobileye, Continental | Single camera only; uses road features, not mutual |
| Target-based recalibration | Bosch DAS3000 service tool | Requires workshop visit, specialized targets, trained tech |
| Online lane-based calibration | Tesla Vision | Forward camera only; no DMS cross-calibration |

### Key Patents Reviewed

- Mobileye online calibration using road geometry (single forward camera)
- Bosch camera misalignment detection and correction
- Continental multi-camera surround-view calibration (using overlapping FOV)
- Valeo parking camera auto-calibration (using ground plane)

### Gap in Prior Art

No known system:
1. Uses shared physical reference features visible to both opposing cameras for mutual calibration
2. Exploits known vehicle interior geometry as calibration references
3. Enables two cameras facing opposite directions to cross-validate each other's alignment
4. Provides continuous in-field calibration without external targets or workshop visits

## 7. Proposed Solution

The ADVIS Dual-Camera Mutual Self-Calibration method comprises:

1. **Shared Reference Feature Identification**: Both cameras can observe certain shared physical features of the vehicle structure -- the cabin camera sees the windshield edge, A-pillar, sun visor, and rearview mirror from inside; the forward camera sees the hood edge, windshield wiper rest position, and bonnet contour from outside. The geometric relationship between these internal and external reference features is fixed and known.

2. **Vehicle Geometry Model**: A pre-programmed 3D model of the relevant vehicle interior/exterior geometry relationships, specific to the vehicle platform. This model defines the expected spatial relationship between features visible to each camera.

3. **Mutual Calibration Algorithm**: By comparing the observed position of reference features in each camera's image against the known vehicle geometry model, the system can independently estimate each camera's mounting orientation. Since both estimates reference the same physical structure, any inconsistency reveals calibration drift.

4. **Cross-Validation**: Each camera's self-calibration result is cross-checked against the other camera's result through the shared geometry model, providing redundancy and confidence metrics.

5. **Continuous Background Operation**: The calibration algorithm runs continuously in the background during normal driving, accumulating observations over time and applying corrections when confidence thresholds are met.

## 8. Key Novel Elements

1. **Mutual calibration of opposing cameras**: Two cameras facing opposite directions calibrate each other through shared vehicle geometry, without external targets
2. **Vehicle geometry as calibration reference**: Known dimensions of windshield, A-pillar, mirror, hood are used as fixed reference features
3. **Cross-validation through shared structure**: Both cameras reference the same physical structure (the vehicle), enabling mutual consistency checking
4. **Continuous in-field operation**: No workshop visit, no targets, no driver intervention required
5. **Self-diagnosing drift detection**: System detects when calibration has drifted beyond acceptable limits and can request service if self-correction fails

## 9. Technical Implementation Details

### Calibration Architecture

```
+------------------------------------------------------------------+
|               ADVIS Mutual Calibration System                     |
|                                                                  |
|  +---------------------+         +---------------------+         |
|  | FORWARD CAMERA      |         | CABIN CAMERA        |         |
|  | Observable Features: |         | Observable Features:|         |
|  | - Hood edge contour |         | - Windshield edge   |         |
|  | - Wiper rest line   |         | - A-pillar edge     |         |
|  | - Bonnet profile    |         | - Sun visor edge    |         |
|  | - Windshield edge   |         | - Rearview mirror   |         |
|  |   (from outside)    |         |   (from inside)     |         |
|  +----------+----------+         +----------+----------+         |
|             |                               |                    |
|             v                               v                    |
|  +----------+----------+         +----------+----------+         |
|  | FORWARD CAMERA      |         | CABIN CAMERA        |         |
|  | POSE ESTIMATION     |         | POSE ESTIMATION     |         |
|  |                     |         |                     |         |
|  | Estimate: pitch,    |         | Estimate: pitch,    |         |
|  | yaw, roll from      |         | yaw, roll from      |         |
|  | reference features  |         | reference features  |         |
|  +----------+----------+         +----------+----------+         |
|             |                               |                    |
|             +---------------+---------------+                    |
|                             |                                    |
|                             v                                    |
|              +--------------+--------------+                     |
|              | VEHICLE GEOMETRY MODEL      |                     |
|              |                             |                     |
|              | Known 3D relationships      |                     |
|              | between all reference       |                     |
|              | features (vehicle-specific) |                     |
|              +--------------+--------------+                     |
|                             |                                    |
|                             v                                    |
|              +--------------+--------------+                     |
|              | CROSS-VALIDATION ENGINE     |                     |
|              |                             |                     |
|              | Compare forward + cabin     |                     |
|              | pose estimates through      |                     |
|              | shared geometry model       |                     |
|              +--------------+--------------+                     |
|                             |                                    |
|                             v                                    |
|              +--------------+--------------+                     |
|              | CALIBRATION UPDATE          |                     |
|              |                             |                     |
|              | Apply correction when       |                     |
|              | confidence > threshold      |                     |
|              +-----------------------------+                     |
|                                                                  |
+------------------------------------------------------------------+
```

### Reference Feature Categories

| Feature Type | Forward Camera View | Cabin Camera View |
|-------------|--------------------|--------------------|
| Windshield boundary | Upper frame edge (exterior side) | All edges (interior side) |
| Vehicle structure | Hood edge, A-pillar (exterior) | A-pillar, headliner (interior) |
| Fixed accessories | Wiper rest position, antenna | Rearview mirror, sun visor |
| Horizon reference | Road horizon line | Dashboard horizon line |

### Calibration Process

1. **Feature extraction**: Each camera identifies known reference features in its field of view
2. **Pose estimation**: Each camera independently estimates its mounting pose (3 DOF: pitch, yaw, roll) from reference feature positions
3. **Geometry consistency check**: Both pose estimates are transformed through the vehicle geometry model to verify mutual consistency
4. **Drift detection**: If inconsistency exceeds threshold, system identifies which camera has drifted
5. **Correction application**: Calibration parameters updated in software (image rectification transforms)
6. **Confidence accumulation**: Multiple observations averaged over time for high-confidence corrections

### Operating Conditions

- **Daytime operation**: Uses natural lighting for feature detection
- **Nighttime operation**: Uses IR illumination for cabin features; forward features detected by streetlights or headlight reflection
- **Stationary vehicle**: Can calibrate during engine-on stationary periods
- **Moving vehicle**: Continuous calibration during normal driving

## 10. Advantages Over Prior Art

| Advantage | Benefit | vs. Competitors |
|-----------|---------|-----------------|
| No external targets needed | Zero-cost in-field calibration | Bosch requires workshop targets |
| Mutual cross-validation | Higher confidence than single-camera methods | Mobileye has single-camera auto-cal only |
| Continuous operation | Always calibrated, never drifted | Factory-only calibration degrades over time |
| Windshield replacement tolerance | Self-recalibrates after service | Competitors require $200-500 recalibration service |
| No driver intervention | Transparent background operation | Some systems require driver to park on flat surface |
| Dual-camera redundancy | Detects which camera drifted | Single-camera systems cannot self-diagnose |

## 11. Alternative Embodiments

1. **IMU-assisted calibration**: Use onboard IMU to measure gravity vector as additional reference for pitch estimation
2. **GNSS-horizon cross-reference**: Use GNSS position and map data to validate forward camera horizon estimate
3. **Pattern-on-housing calibration**: Embed small calibration patterns on the module housing visible to each camera at extreme FOV edges
4. **Thermal compensation model**: Pre-characterize thermal deformation of mount and apply predictive correction based on temperature sensor
5. **Multi-vehicle geometry library**: Pre-load geometry models for multiple vehicle platforms; auto-detect vehicle type during installation
6. **Peer-to-peer fleet calibration**: Share calibration state across fleet vehicles with the same module for statistical validation

## 12. Potential Claims

### Independent Claim 1 (Method)

A method of calibrating a dual-camera module mounted in a vehicle, comprising:
- capturing, by a first camera having a first field of view oriented in a first direction, image data containing at least one reference feature of the vehicle structure;
- capturing, by a second camera having a second field of view oriented in a substantially opposite direction from said first direction, image data containing at least one reference feature of the vehicle structure;
- estimating a mounting pose of said first camera based on observed positions of said at least one reference feature in said first camera image data and a stored vehicle geometry model;
- estimating a mounting pose of said second camera based on observed positions of said at least one reference feature in said second camera image data and said stored vehicle geometry model;
- cross-validating said first camera mounting pose and said second camera mounting pose through geometric relationships defined in said vehicle geometry model; and
- updating calibration parameters of at least one of said first and second cameras based on said cross-validation.

### Independent Claim 2 (System)

A self-calibrating dual-camera system for a vehicle, comprising:
- a first image sensor oriented to capture a scene external to the vehicle;
- a second image sensor oriented to capture a scene internal to the vehicle;
- a non-volatile memory storing a vehicle geometry model defining spatial relationships between reference features visible to said first and second image sensors;
- a processor configured to:
  - detect reference features of the vehicle structure in images from said first and second image sensors;
  - compute independent pose estimates for each image sensor using detected reference features and said vehicle geometry model;
  - determine calibration consistency between said independent pose estimates; and
  - apply calibration corrections when said consistency exceeds a confidence threshold;
- wherein said self-calibration operates without external calibration targets.

### Independent Claim 3 (Computer-Readable Medium)

A non-transitory computer-readable medium storing instructions that, when executed by a processor coupled to a forward-facing camera and a cabin-facing camera in a vehicle-mounted module, cause the processor to:
- identify vehicle structure features visible in forward-facing camera imagery;
- identify vehicle structure features visible in cabin-facing camera imagery;
- determine orientation of each camera relative to the vehicle based on known geometry of said vehicle structure features;
- cross-validate determined orientations of both cameras through a shared vehicle geometry model stored in memory; and
- update image processing calibration parameters when cross-validation indicates drift beyond a predetermined tolerance.

### Dependent Claims

4. The method of claim 1, wherein said reference features of the vehicle structure visible to said first camera include at least one of: a hood edge contour, a windshield wiper rest position, or an A-pillar edge as viewed from exterior.
5. The method of claim 1, wherein said reference features of the vehicle structure visible to said second camera include at least one of: a windshield edge, a rearview mirror contour, or a sun visor edge as viewed from interior.
6. The system of claim 2, further comprising an inertial measurement unit providing gravity vector reference for validating pitch calibration.
7. The method of claim 1, wherein said calibrating is performed continuously during normal vehicle operation without driver intervention.
8. The method of claim 1, further comprising detecting that calibration drift exceeds a self-correctable limit and generating a service notification.
9. The system of claim 2, wherein said vehicle geometry model is vehicle-platform-specific and selected during module installation.
10. The method of claim 1, wherein said estimating is performed using accumulated observations over a plurality of driving sessions to improve confidence.
11. The system of claim 2, wherein said calibration corrections are applied as image rectification transforms without physical camera repositioning.
12. The method of claim 1, further comprising operating said calibration in both daylight conditions using natural illumination and nighttime conditions using infrared illumination.

## 13. Drawings / Figures Description

### Figure 1: Dual-Camera Reference Feature Diagram
- Vehicle cross-section showing forward camera FOV and cabin camera FOV
- Reference features labeled in each camera's view
- Geometric relationship lines connecting shared reference structures

### Figure 2: Calibration Data Flow
- Block diagram showing feature extraction, pose estimation, cross-validation, and correction update pipeline
- Data flow arrows with intermediate outputs labeled

### Figure 3: Vehicle Geometry Model
- 3D wireframe of relevant vehicle structure (windshield, A-pillars, hood, mirror)
- Camera mounting positions indicated
- Known dimension annotations

### Figure 4: Drift Detection and Correction
- Timeline showing calibration state over vehicle lifetime
- Manufacturing calibration point, drift accumulation, detection threshold, correction event
- Comparison: with and without mutual calibration

### Figure 5: Cross-Validation Geometry
- Mathematical diagram showing how two independent pose estimates are compared through shared geometry
- Consistency metric computation illustrated

## 14. Commercial Value

### Market Opportunity

- Windshield replacement market generates significant recalibration revenue for dealers ($200-500 per event)
- Self-calibrating module eliminates this pain point, making product attractive to OEMs focused on ownership cost
- Regulatory trend toward lifetime calibration assurance for safety systems

### Revenue Model

| Revenue Stream | Estimated Value |
|---------------|-----------------|
| Premium pricing for self-calibrating module | $5-15 per unit premium |
| Elimination of calibration service requirement | OEM cost avoidance value |
| Licensing calibration algorithm | $500K-2M per licensee |

### Competitive Advantage

- No competitor offers mutual cross-calibration for opposing cameras
- Significant patent blocking potential for dual-camera self-calibration field
- Reduces total cost of ownership (no recalibration visits)

## 15. Filing Recommendation

**Recommendation: File Provisional Patent Application within 90 days**

- **Filing type**: Provisional (US) for priority date
- **Conversion**: Non-provisional within 12 months
- **International**: PCT application recommended
- **Priority territories**: US, EU (Germany), China, Japan, South Korea
- **Urgency**: Medium-High - as dual-camera modules become more common, others will inevitably explore mutual calibration
- **Continuation opportunity**: Vehicle geometry model generation methods could be a separate continuation

## 16. Confidentiality Classification

| Element | Classification |
|---------|---------------|
| General mutual calibration concept | PATENT - Public upon filing |
| Reference feature types and geometry model approach | PATENT - Public upon filing |
| Specific feature detection algorithm parameters | TRADE SECRET - Never disclose |
| Calibration threshold values (when to correct) | TRADE SECRET - Never disclose |
| Confidence accumulation parameters | TRADE SECRET - Never disclose |
| Vehicle-specific geometry model data | TRADE SECRET - OEM-specific, under NDA |
| Drift rate characterization data | TRADE SECRET - Manufacturing know-how |

## 17. Next Steps

- [ ] Complete prior art search (focus on automotive camera calibration patents)
- [ ] Survey existing auto-calibration literature (academic + patent)
- [ ] Prototype mutual calibration algorithm in simulation environment
- [ ] Identify minimum viable set of reference features for robust calibration
- [ ] Validate concept with real camera module in lab vehicle
- [ ] Review with patent attorney for claim scope
- [ ] Prepare provisional application filing package
- [ ] Coordinate with ID-001 (platform) for integration architecture
- [ ] Budget allocation: provisional filing ($3K-5K)

---

**Document Version:** 1.0  
**Last Updated:** 2025-01  
**Classification:** CONFIDENTIAL - Attorney-Client Privilege  
**Witness Signature:** _________________ Date: _________  
**Witness Signature:** _________________ Date: _________
