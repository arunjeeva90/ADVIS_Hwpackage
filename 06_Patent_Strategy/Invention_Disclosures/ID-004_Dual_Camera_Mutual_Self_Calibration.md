# Invention Disclosure: ID-004

## CONFIDENTIAL - INTERNAL DRAFT

---

## 1. Title

Dual-Camera Mutual Self-Calibration for Windshield-Mounted ADAS/DMS Module

## 2. Date

June 2026

## 3. Inventors

[To be filled - engineering team members who contributed to this concept]

## 4. Status

DRAFT - Awaiting prior art search and patent attorney review

---

## 5. Problem Statement

A windshield-mounted camera module is subject to thermal expansion, mechanical vibration, and potential bracket movement over vehicle lifetime. If the cameras shift even slightly relative to the vehicle coordinate frame, ADAS perception accuracy degrades (e.g., incorrect object distance estimation, lane departure detection errors). Key problems include:

- Traditional calibration requires a service visit with special targets/patterns
- Single-camera self-calibration uses vanishing points or lane markings but cannot detect pure translational shifts
- A dual-camera module (forward + DMS) has an additional opportunity: the geometric relationship between the two cameras can serve as a reference if exploited correctly
- No existing system uses DMS camera observations as a cross-reference to validate or correct forward camera calibration, or vice versa
- Vibration-induced micro-shifts accumulate over time but may be too small for single-frame detection

## 6. Background / Prior Art Summary

### Existing Approaches

| Approach | Example | Limitation |
|----------|---------|------------|
| Factory calibration only | Most production ADAS cameras | No drift correction during vehicle life |
| Vanishing point recalibration | Mobileye, Tesla | Requires structured road features; cannot detect translation |
| Multi-camera cross-calibration | Surround view systems | Uses overlapping FOV; not applicable to opposing cameras |
| Service-bay target calibration | OEM service procedures | Requires dealer visit; expensive and inconvenient |

### Gap in Prior Art

No known system uses:
1. Two cameras with opposing fields of view (forward vs. cabin) for mutual calibration reference
2. Known vehicle interior geometry (steering wheel, dashboard, A-pillar) as DMS-derived reference features for cross-validating forward camera mounting angle
3. Combined forward scene statistics + cabin geometry statistics to detect calibration drift without overlapping FOV

## 7. Proposed Solution

A mutual self-calibration method for a dual-facing camera module:

1. **Forward camera self-check:** Monitors vanishing point position, horizon line, lane geometry statistics to detect angular drift
2. **DMS camera self-check:** Monitors known vehicle interior landmarks (steering wheel position, dashboard edge, A-pillar angle) to detect DMS mounting angle change
3. **Mutual cross-validation:** Because both cameras are rigidly mounted in the same housing, any detected drift in one camera implies equal drift for the other:
   - If DMS detects housing has pitched down (steering wheel appears higher in frame), forward camera has also pitched down
   - If forward camera detects horizon drift, DMS should observe corresponding shift in cabin landmarks
4. **Calibration confidence metric:** Fuses self-check and cross-check results into a confidence score
5. **Alert or correction:** If drift exceeds threshold, system flags calibration degradation via CAN diagnostic message; optionally applies software correction factor within safe bounds

## 8. Key Novel Elements

1. **Opposing-camera mutual calibration:** Two cameras with non-overlapping FOV validate each other through rigid housing assumption
2. **Cabin geometry as calibration reference:** Vehicle interior landmarks serve as angular reference for DMS camera (and indirectly for forward camera)
3. **Cross-axis drift detection:** DMS detects pitch/yaw drift that forward self-calibration alone cannot isolate from road geometry changes
4. **Confidence fusion:** Combined self-check + cross-check provides higher confidence than either alone
5. **No external targets required:** Self-calibration operates during normal driving without special service equipment

## 9. Technical Implementation Details

### Architecture

```
Forward Camera --> [Feature Extraction] --> Vanishing Point, Horizon, Lane Stats
                                                      |
                                            [Calibration Fusion Engine]
                                                      |
DMS Camera -----> [Feature Extraction] --> Cabin Landmarks, Head Position Baseline
                                                      |
                                            [Drift Detection + Confidence Score]
                                                      |
                                            [CAN Alert / Software Correction]
```

### Mutual Validation Logic

- Housing rigid body assumption: both cameras share same mount, same drift
- Forward pitch drift detected by horizon shift correlates with DMS seeing cabin landmarks shift in opposite direction
- Yaw drift detected by vanishing point horizontal shift correlates with DMS seeing steering wheel/dashboard shift
- Time-averaged statistics (not single-frame) to reject noise and transient vibration
- Drift detection threshold set conservatively to avoid false alarms

### Correction Strategy

- Primary: Flag calibration degradation to driver/fleet via CAN diagnostic
- Secondary: Apply bounded software angular correction (within safe range, e.g., +/- 1 degree)
- Beyond safe correction range: require service-bay recalibration
- Correction never applied to safety-critical ADAS decisions without confidence exceeding threshold

*Note: Specific threshold values, feature extraction algorithms, and fusion logic parameters are trade secrets and are not disclosed.*

## 10. Advantages Over Prior Art

| Advantage | Benefit |
|-----------|---------|
| No service-bay visit needed | Reduces vehicle lifetime calibration cost |
| Continuous monitoring | Detects drift before it causes ADAS degradation |
| Cross-validation | Higher confidence than single-camera self-calibration |
| No overlapping FOV required | Works with opposing (forward + cabin) cameras |
| Leverages existing hardware | No additional sensors; uses cameras already present |
| Bounded correction | Maintains safety margin; escalates to service when needed |

## 11. Alternative Embodiments

1. **IMU-assisted drift detection:** Fuse IMU measurements to distinguish between road slope changes and actual camera drift
2. **GNSS-map correlation:** Use GNSS position + map data to validate forward camera horizon/vanishing point expectations
3. **Temperature-compensated model:** Predict expected thermal drift based on housing temperature and compensate proactively
4. **Fleet learning:** Aggregate calibration drift statistics across fleet to identify systematic mounting issues
5. **Parking-mode calibration:** Use known parking structure geometry (flat floor, straight walls) during parked state

## 12. Potential Claims

### Independent Claim 1 (Method)

A method of detecting calibration drift in a dual-camera vehicle module, comprising:
- capturing imagery from a forward-facing camera and a cabin-facing camera housed in a common rigid enclosure;
- extracting geometric reference features from said forward-facing imagery indicative of forward camera angular orientation;
- extracting geometric reference features from said cabin-facing imagery indicative of cabin camera angular orientation;
- comparing changes in said forward reference features to changes in said cabin reference features based on a rigid-body coupling constraint; and
- determining a calibration confidence metric based on consistency between said forward and said cabin angular orientation estimates.

### Independent Claim 2 (System)

A vehicle camera system comprising:
- a housing rigidly mounting a first image sensor facing a road scene and a second image sensor facing a vehicle cabin;
- a processor configured to:
  - determine an angular orientation estimate of said first image sensor based on road scene features;
  - determine an angular orientation estimate of said second image sensor based on vehicle cabin features;
  - evaluate consistency between said first and second orientation estimates based on a rigid mounting assumption; and
  - generate a calibration status signal indicating whether said camera system remains within calibration tolerance.

### Dependent Claims

3. The method of claim 1, further comprising applying a bounded angular correction to image processing when drift is within a safe correction range.
4. The method of claim 1, further comprising transmitting a service alert via a vehicle communication bus when drift exceeds a correction threshold.
5. The system of claim 2, wherein said vehicle cabin features include at least one of: steering wheel position, dashboard edge, A-pillar angle, or headliner edge.
6. The method of claim 1, wherein said determining is performed on time-averaged statistics accumulated over multiple driving sessions.

*Note: Final patent claim language must be reviewed by a patent attorney.*

## 13. Drawings / Figures Description

### Figure 1: Dual-Camera Mutual Calibration Architecture
- Block diagram showing both cameras, feature extraction, fusion engine, and output

### Figure 2: Rigid Housing Drift Model
- Diagram showing how housing pitch/yaw affects both camera views simultaneously

### Figure 3: Feature Reference Points
- Forward camera: vanishing point, horizon line, lane markers
- DMS camera: steering wheel, dashboard edge, A-pillar, headliner

### Figure 4: Drift Detection and Correction Flow
- Decision flowchart: detect, validate, correct or escalate

## 14. Commercial Value

- Addresses growing regulatory and Euro NCAP requirement for calibration monitoring
- Reduces OEM warranty cost (fewer service visits for recalibration)
- Differentiator vs. competitors who require manual recalibration
- Enhances ADAS reliability over vehicle lifetime
- Potential licensing to other ADAS module suppliers

## 15. Filing Recommendation

**Recommendation: File Provisional Patent Application**

- Filing type: Provisional (US) to establish priority date
- Conversion: Non-provisional within 12 months
- International: PCT recommended
- Priority territories: US, EU, China, Japan, South Korea
- Urgency: Medium-High - calibration maintenance is an emerging competitive focus area

## 16. Confidentiality Classification

| Element | Classification |
|---------|---------------|
| Mutual calibration concept | PATENT - Disclose in filing |
| Rigid-body coupling principle | PATENT - Disclose in filing |
| Feature extraction algorithm details | TRADE SECRET - Never disclose |
| Specific threshold values | TRADE SECRET - Never disclose |
| Correction function parameters | TRADE SECRET - Never disclose |
| Training data for landmark detection | TRADE SECRET - Never disclose |

## 17. Next Steps

- [ ] Complete prior art search (calibration patents, camera alignment IP)
- [ ] Verify no blocking patents from Mobileye, Bosch, Valeo, Magna
- [ ] Develop formal patent drawings (4 figures minimum)
- [ ] Review with patent attorney for claim refinement
- [ ] Coordinate with ID-003 (compact module) for rigid housing reference
- [ ] Prototype calibration drift detection algorithm
- [ ] Prepare provisional application filing package

---

**Document Version:** 1.0  
**Last Updated:** June 2026  
**Classification:** CONFIDENTIAL - INTERNAL DRAFT  
**Witness Signature:** _________________ Date: _________  
**Witness Signature:** _________________ Date: _________
