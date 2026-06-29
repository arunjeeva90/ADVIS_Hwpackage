# Invention Disclosure: ID-001

## CONFIDENTIAL - INTERNAL DRAFT

---

## 1. Title

Risk-Coupled ADAS/DMS Decision Fusion Architecture

## 2. Date

June 2026

## 3. Inventors

[To be filled - engineering team members who contributed to this concept]

## 4. Status

DRAFT - Awaiting prior art search and patent attorney review

---

## 5. Problem Statement

Current ADAS and DMS systems operate as separate, loosely coupled modules. Forward-facing ADAS cameras detect road hazards, while cabin-facing DMS cameras monitor driver state, but these two information streams are not fused at the decision level in a risk-weighted manner. This creates several problems:

- ADAS may issue collision warnings without considering whether the driver is already attentive and actively responding
- DMS may flag driver inattention without correlating it to the actual forward road risk level
- The system cannot modulate its intervention urgency based on the combined risk state
- OEM controllers receive independent, potentially conflicting advisory messages from separate systems
- No single risk metric captures both "external threat severity" and "driver readiness to respond"

Existing systems either treat ADAS and DMS as independent advisory channels or combine them only at the human-machine interface (HMI) level rather than at the perception/decision level.

## 6. Background / Prior Art Summary

### Existing Approaches

| Approach | Example | Limitation |
|----------|---------|------------|
| Independent ADAS + DMS | Bosch + Smart Eye separate modules | No risk coupling at decision level |
| HMI-level fusion | Euro NCAP DMS + FCW escalation | Only affects warning loudness, not decision logic |
| Single-sensor distraction scaling | Mobileye attention proxy from gaze direction | No cabin camera; relies on forward behavior only |
| Rule-based escalation | OEM-specific escalation tables | Static rules; no real-time risk weighting |

### Gap in Prior Art

No known system performs real-time bidirectional risk coupling where:
1. Forward scene risk modulates the DMS attention threshold (lower threshold when road risk is high)
2. Driver inattention state modulates the urgency and type of ADAS actuation request
3. A single fused risk metric drives the CAN actuation request message priority

## 7. Proposed Solution

A dual-camera smart camera module that performs risk-coupled decision fusion:

1. **Forward perception pipeline** generates a scene risk score (threat proximity, time-to-collision, obstacle classification, road departure risk)
2. **DMS perception pipeline** generates a driver readiness score (gaze direction, eye openness, head pose, response latency estimate)
3. **Risk coupling engine** fuses both scores into a combined risk state that determines:
   - Whether to issue an actuation request vs. a warning-only advisory
   - The urgency level of the CAN message sent to OEM controllers
   - Whether to increase DMS sampling rate when road risk is elevated
   - Whether to reduce ADAS sensitivity when driver is clearly attentive and responding

4. **Output:** Safety-supervised actuation request messages over CAN/CAN-FD with risk-weighted priority

## 8. Key Novel Elements

1. **Bidirectional risk coupling:** Forward risk modulates DMS thresholds; DMS state modulates ADAS response
2. **Single fused risk metric:** Combines external threat and driver readiness into one decision variable
3. **Adaptive threshold modulation:** DMS attention threshold tightens when forward scene risk increases
4. **Risk-weighted actuation request:** CAN message priority/urgency driven by fused risk state
5. **Single-module implementation:** Both cameras and fusion engine in one compact unit, reducing latency

## 9. Technical Implementation Details

### Architecture

```
Forward Camera --> [ADAS Perception] --> Scene Risk Score
                                              |
                                    [Risk Coupling Engine] --> Fused Risk State --> CAN Actuation Request
                                              |
DMS Camera -----> [DMS Perception] ---> Driver Readiness Score
```

### Risk Coupling Logic

- When scene risk is HIGH and driver readiness is LOW: maximum urgency actuation request
- When scene risk is HIGH and driver readiness is HIGH: moderate advisory (driver is responding)
- When scene risk is LOW and driver readiness is LOW: DMS-only drowsiness/distraction alert
- When scene risk is LOW and driver readiness is HIGH: no intervention

### Adaptive Threshold Behavior

- Forward risk elevation triggers DMS pipeline to increase frame rate and tighten attention thresholds
- Confirmed driver attentiveness allows ADAS pipeline to use slightly relaxed intervention thresholds (reducing false positives)
- Both adaptations are bounded by safety floor values that cannot be relaxed beyond defined limits

*Note: Specific threshold values, model weights, and calibration parameters are trade secrets and are not disclosed in this document.*

## 10. Advantages Over Prior Art

| Advantage | Benefit |
|-----------|---------|
| Bidirectional coupling | Smarter intervention decisions vs. independent systems |
| Reduced false positives | Attentive driver does not receive unnecessary warnings |
| Reduced missed events | Inattentive driver gets earlier/stronger intervention |
| Single CAN message priority | OEM controller receives one coherent risk signal |
| Single module | Lower latency than multi-ECU fusion; lower system cost |

## 11. Alternative Embodiments

1. **Cloud-assisted risk model:** Upload anonymized risk coupling statistics for fleet-level threshold optimization
2. **Multi-occupant awareness:** Extend DMS to detect passenger state for ride-share/taxi safety applications
3. **Radar-augmented risk:** Add radar input to scene risk score for enhanced time-to-collision estimation
4. **V2X risk input:** Incorporate vehicle-to-everything communication data as additional risk input
5. **Configurable risk policy:** OEM-programmable risk coupling parameters via CAN configuration message

## 12. Potential Claims

### Independent Claim 1 (System)

A vehicle safety system comprising:
- a forward-facing camera configured to capture road scene imagery;
- a cabin-facing camera configured to capture driver state imagery;
- a processing unit configured to:
  - generate a scene risk score from said road scene imagery;
  - generate a driver readiness score from said driver state imagery;
  - fuse said scene risk score and said driver readiness score into a combined risk state; and
  - generate an actuation request message with an urgency level determined by said combined risk state;
- a vehicle communication interface configured to transmit said actuation request message to a vehicle controller.

### Independent Claim 2 (Method)

A method of generating risk-weighted vehicle safety requests, comprising:
- capturing road scene imagery from a forward-facing camera;
- capturing driver state imagery from a cabin-facing camera;
- computing a scene risk score indicative of external threat severity;
- computing a driver readiness score indicative of driver capacity to respond;
- fusing said scene risk score and said driver readiness score according to a risk coupling function;
- modulating an actuation request urgency based on said fused risk state; and
- transmitting said actuation request to a vehicle controller via a vehicle communication bus.

### Dependent Claims

3. The system of claim 1, wherein said processing unit adaptively modulates a driver attention threshold based on said scene risk score.
4. The system of claim 1, wherein said processing unit reduces actuation request urgency when said driver readiness score exceeds a defined attentiveness threshold.
5. The method of claim 2, further comprising increasing a DMS camera frame rate when said scene risk score exceeds a risk elevation threshold.
6. The system of claim 1, wherein said forward-facing camera and said cabin-facing camera are housed in a single compact module mounted to a vehicle windshield.

*Note: Final patent claim language must be reviewed by a patent attorney.*

## 13. Drawings / Figures Description

### Figure 1: Risk Coupling Architecture
- Block diagram showing forward camera, DMS camera, perception pipelines, risk coupling engine, and CAN output
- Arrows showing bidirectional threshold modulation

### Figure 2: Risk State Matrix
- 2D matrix showing action/output for each combination of scene risk level and driver readiness level

### Figure 3: Adaptive Threshold Modulation
- Timing diagram showing DMS threshold adjustment in response to forward risk elevation

### Figure 4: CAN Message Priority Mapping
- Diagram showing how fused risk state maps to CAN message priority/urgency field

## 14. Commercial Value

- Differentiator for Euro NCAP 2026+ ADAS + DMS combined assessment
- Enables single-module replacement of separate ADAS + DMS ECUs (cost reduction for OEM)
- Potential licensing to Tier-1 suppliers lacking integrated ADAS+DMS fusion capability
- Addresses regulatory trend toward combined driver monitoring + collision avoidance

## 15. Filing Recommendation

**Recommendation: File Provisional Patent Application**

- Filing type: Provisional (US) to establish priority date
- Conversion: Non-provisional within 12 months
- International: PCT recommended (global automotive market)
- Priority territories: US, EU (Germany), China, Japan, South Korea
- Urgency: High - Euro NCAP 2026 timeline drives competitor development

## 16. Confidentiality Classification

| Element | Classification |
|---------|---------------|
| Risk coupling concept and architecture | PATENT - Disclose in filing |
| Block diagram and data flow | PATENT - Disclose in filing |
| Specific threshold values and calibration | TRADE SECRET - Never disclose |
| Model architecture and weights | TRADE SECRET - Never disclose |
| Training data and datasets | TRADE SECRET - Never disclose |
| Exact risk score computation method | TRADE SECRET - Never disclose |
| CAN message format details | TRADE SECRET - Never disclose |

## 17. Next Steps

- [ ] Complete prior art search (USPTO, EPO, WIPO, SAE papers)
- [ ] Confirm no blocking patents from Mobileye, Bosch, Continental, Seeing Machines
- [ ] Develop formal patent drawings (minimum 4 figures)
- [ ] Review with patent attorney for claim refinement
- [ ] Coordinate with ID-005 (Risk-Aware Power/Sensor/IR Control) for cross-reference
- [ ] Prepare provisional application filing package
- [ ] Budget allocation for filing

---

**Document Version:** 1.0  
**Last Updated:** June 2026  
**Classification:** CONFIDENTIAL - INTERNAL DRAFT  
**Witness Signature:** _________________ Date: _________  
**Witness Signature:** _________________ Date: _________
