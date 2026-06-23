# Invention Disclosure: ID-003

## 1. Title

Risk-Coupled ADAS+DMS Decision Fusion

## 2. Date

January 2025

## 3. Inventors

[To be filled - engineering team members who contributed to this concept]

## 4. Status

DRAFT - Awaiting prior art search completion

---

## 5. Problem Statement

Current advanced driver assistance systems (ADAS) and driver monitoring systems (DMS) operate as independent subsystems with minimal cross-coupling. This architectural separation creates critical safety gaps:

- **Decoupled risk assessment**: ADAS evaluates road risk independently of driver attention state, leading to either excessive false warnings (driver is attentive) or insufficient warnings (driver is inattentive)
- **Binary driver state**: DMS systems typically classify driver state as attentive/inattentive without considering the actual external risk level, leading to unnecessary alerts during low-risk driving
- **Fixed warning thresholds**: Alert thresholds remain static regardless of the combined risk picture (driver state + road conditions + vehicle dynamics)
- **Missed risk multiplication**: When a distracted driver faces a high-risk road scenario, the combined danger is multiplicative, not additive, but no existing system models this coupling

No commercially available system dynamically couples driver attention state with ADAS perception risk to produce a unified, risk-proportional response.

## 6. Background / Prior Art Summary

### Existing Approaches

| Approach | Example | Limitation |
|----------|---------|------------|
| Independent ADAS + DMS | Mobileye + Seeing Machines | No cross-coupling; separate alert logic |
| Simple DMS gating | Euro NCAP 2026 requirements | Binary gate: attentive/inattentive only |
| Tiered warnings | BMW/Mercedes DMS | Fixed tiers; no continuous risk coupling |
| Aftermarket driver scoring | Nauto, Lytx | Fleet telematics; not real-time actuation-ready |

### Key Patents Reviewed

- Seeing Machines patents on gaze detection and distraction classification
- Mobileye patents on time-to-collision computation
- Toyota patents on driver state estimation
- GM Super Cruise attention monitoring system

### Gap in Prior Art

No known system:
1. Computes a continuous coupled risk metric from both driver attention AND external scene risk
2. Uses the coupled metric to dynamically modulate ADAS intervention thresholds
3. Generates graded actuation requests proportional to the coupled risk level
4. Maintains safety boundary (requests only, not direct actuation)

## 7. Proposed Solution

The ADVIS Risk-Coupled Decision Fusion method comprises:

1. **Driver Attention Model**: Continuous assessment of driver attention level (gaze direction, eye closure, head pose, micro-saccade patterns) producing a normalized attention score

2. **Scene Risk Model**: Continuous assessment of forward scene risk (time-to-collision, lane departure risk, object density, road geometry complexity) producing a normalized risk score

3. **Risk Coupling Function**: A mathematical coupling function that combines driver attention score and scene risk score into a unified coupled-risk metric, where the coupling is multiplicative (low attention + high risk = very high coupled risk)

4. **Adaptive Threshold Modulation**: Warning and actuation request thresholds that dynamically adjust based on the coupled-risk metric, providing earlier and more aggressive intervention when coupled risk is high

5. **Graded Actuation Requests**: The system generates safety-supervised actuation requests to OEM vehicle ECUs with intensity proportional to the coupled-risk metric. The ADVIS system does NOT directly actuate - final authority remains with OEM vehicle controllers.

## 8. Key Novel Elements

1. **Continuous coupled-risk metric**: Not binary (attentive/inattentive) but a continuous function of both driver state and scene risk
2. **Multiplicative risk coupling**: Recognition that combined risk is multiplicative, not additive (distracted driver + high scene risk = exponentially higher danger)
3. **Dynamic threshold modulation**: ADAS intervention thresholds shift continuously based on coupled risk, not fixed per-feature thresholds
4. **Proportional actuation requests**: Request intensity scales with coupled risk (gentle request at low coupling, urgent request at high coupling)
5. **Single-SoC fusion**: Both ADAS and DMS perception run on the same processor, enabling zero-latency cross-domain data sharing for risk coupling

## 9. Technical Implementation Details

### System Architecture

```
+------------------------------------------------------------------+
|                    ADVIS Decision Fusion Engine                    |
|                                                                  |
|  +---------------------+         +---------------------+         |
|  | FORWARD CAMERA      |         | CABIN CAMERA        |         |
|  | (ADAS Perception)   |         | (DMS Monitoring)    |         |
|  |                     |         |                     |         |
|  | - Object detection  |         | - Face detection    |         |
|  | - Lane detection    |         | - Gaze estimation   |         |
|  | - Free space        |         | - Eye closure       |         |
|  | - Scene parsing     |         | - Head pose         |         |
|  +----------+----------+         +----------+----------+         |
|             |                               |                    |
|             v                               v                    |
|  +----------+----------+         +----------+----------+         |
|  | SCENE RISK MODEL    |         | DRIVER ATTENTION    |         |
|  |                     |         | MODEL               |         |
|  | Output: R_scene     |         | Output: A_driver    |         |
|  | (0.0 to 1.0)        |         | (0.0 to 1.0)        |         |
|  +----------+----------+         +----------+----------+         |
|             |                               |                    |
|             +---------------+---------------+                    |
|                             |                                    |
|                             v                                    |
|              +--------------+--------------+                     |
|              | RISK COUPLING FUNCTION      |                     |
|              |                             |                     |
|              | C_risk = f(R_scene, A_driver)|                     |
|              | (Multiplicative coupling)    |                     |
|              +--------------+--------------+                     |
|                             |                                    |
|                             v                                    |
|              +--------------+--------------+                     |
|              | THRESHOLD MODULATION        |                     |
|              |                             |                     |
|              | Adjust warning/request      |                     |
|              | thresholds based on C_risk  |                     |
|              +--------------+--------------+                     |
|                             |                                    |
|                             v                                    |
|              +--------------+--------------+                     |
|              | ACTUATION REQUEST           |                     |
|              | GENERATOR                   |                     |
|              |                             |                     |
|              | Graded requests to OEM ECU  |                     |
|              | (NOT direct actuation)      |                     |
|              +-----------------------------+                     |
|                                                                  |
+------------------------------------------------------------------+
         |
         | CAN-FD: Safety-supervised actuation REQUESTS
         v
+------------------------------------------------------------------+
|              OEM VEHICLE ECU (Final Actuator Authority)           |
+------------------------------------------------------------------+
```

### Risk Coupling Function

The coupled risk metric is computed as:

```
C_risk = R_scene * (1 - A_driver)^alpha

Where:
  R_scene   = Scene risk score [0.0 = no risk, 1.0 = imminent collision]
  A_driver  = Driver attention score [0.0 = fully inattentive, 1.0 = fully attentive]
  alpha     = Coupling exponent (controls sensitivity to inattention)
  C_risk    = Coupled risk metric [0.0 = minimal, 1.0 = maximum]
```

- When driver is fully attentive (A=1.0): C_risk = 0 regardless of scene risk (driver can handle)
- When driver is inattentive (A=0.0): C_risk = R_scene (full scene risk passes through)
- Partial attention: proportional coupling with exponential sensitivity

### Threshold Modulation

```
Threshold_warning  = Base_threshold * (1 - C_risk * gain_warning)
Threshold_request  = Base_threshold * (1 - C_risk * gain_request)
```

- Higher coupled risk lowers the intervention threshold (earlier intervention)
- Separate gain factors for warnings (visual/audio) vs. actuation requests
- Base thresholds calibrated per ADAS feature (FCW, LDW, etc.)

### Actuation Request Protocol

- Requests sent to OEM vehicle ECU via CAN-FD with specified message format
- Request includes: feature ID, urgency level (0-7), requested action type, confidence score
- OEM ECU has final authority to execute, modify, or reject any request
- ADVIS never directly controls brakes, steering, or throttle

## 10. Advantages Over Prior Art

| Advantage | Benefit | vs. Competitors |
|-----------|---------|-----------------|
| Continuous coupled metric | Eliminates binary attentive/inattentive gap | Seeing Machines uses discrete states |
| Multiplicative coupling | Captures true combined danger level | No competitor models multiplicative risk |
| Dynamic thresholds | Reduces false warnings while improving safety | Fixed thresholds = over/under-alerting |
| Proportional requests | Smoother driver experience | Competitors use binary on/off alerts |
| Single-SoC fusion | Zero-latency cross-domain data | Separate ECUs have communication latency |
| Safety boundary compliance | Generates requests only | Maintains clear OEM responsibility |

## 11. Alternative Embodiments

1. **Bayesian risk fusion**: Replace deterministic coupling function with Bayesian probabilistic model
2. **Learned coupling function**: Train the coupling exponent using naturalistic driving data
3. **Multi-sensor extension**: Incorporate vehicle dynamics (speed, steering rate) as additional coupling inputs
4. **Predictive coupling**: Use trajectory prediction to assess future coupled risk (look-ahead coupling)
5. **Driver-personalized profiles**: Adapt coupling parameters to individual driver behavior patterns over time
6. **V2X enhanced coupling**: Incorporate vehicle-to-everything communication data into scene risk model
7. **Fatigue progression model**: Extend driver attention model to predict attention degradation trends

## 12. Potential Claims

### Independent Claim 1 (Method)

A method of generating safety-supervised actuation requests in an automotive vision system, comprising:
- receiving image data from a forward-facing camera and processing said image data to generate a scene risk score representing a level of external driving risk;
- receiving image data from a cabin-facing camera and processing said image data to generate a driver attention score representing a level of driver engagement;
- computing a coupled risk metric by applying a coupling function to said scene risk score and said driver attention score, wherein said coupling function produces a higher coupled risk metric when both scene risk is elevated and driver attention is reduced;
- modulating at least one intervention threshold based on said coupled risk metric; and
- generating an actuation request to a vehicle electronic control unit when said coupled risk metric exceeds said modulated intervention threshold;
- wherein said actuation request is a safety-supervised request and final actuator authority remains with said vehicle electronic control unit.

### Independent Claim 2 (System)

A dual-camera automotive safety system, comprising:
- a forward-facing camera for capturing road scene imagery;
- a cabin-facing camera for capturing driver imagery;
- a processor configured to execute:
  - a scene risk model that outputs a continuous scene risk score from said road scene imagery;
  - a driver attention model that outputs a continuous driver attention score from said driver imagery;
  - a risk coupling module that computes a coupled risk metric as a function of both said scene risk score and said driver attention score; and
  - a request generator that produces graded actuation requests to a vehicle control system based on said coupled risk metric;
- wherein said coupled risk metric increases when scene risk increases and driver attention decreases simultaneously.

### Independent Claim 3 (Computer-Readable Medium)

A non-transitory computer-readable medium storing instructions that, when executed by a processor in a vehicle camera module, cause the processor to:
- compute a scene risk score from forward-facing camera data;
- compute a driver attention score from cabin-facing camera data;
- determine a coupled risk value by applying a multiplicative coupling function to said scene risk score and a complement of said driver attention score;
- adjust intervention thresholds for at least one advanced driver assistance feature based on said coupled risk value; and
- transmit graded actuation requests to a separate vehicle electronic control unit over a vehicle communication bus when said adjusted intervention thresholds are exceeded.

### Dependent Claims

4. The method of claim 1, wherein said coupling function is multiplicative such that the coupled risk metric equals the scene risk score multiplied by a decreasing function of the driver attention score.
5. The method of claim 1, wherein said modulating comprises lowering said intervention threshold as said coupled risk metric increases.
6. The system of claim 2, wherein said processor is a single system-on-chip processing both forward-facing and cabin-facing image data.
7. The method of claim 1, further comprising generating a plurality of actuation requests with urgency levels proportional to said coupled risk metric.
8. The system of claim 2, wherein said vehicle communication bus is CAN-FD.
9. The method of claim 1, wherein said driver attention score is derived from at least two of: gaze direction, eye closure state, and head pose orientation.
10. The method of claim 1, wherein said scene risk score is derived from at least one of: time-to-collision, lane departure proximity, and object density in forward path.
11. The system of claim 2, further comprising a safety watchdog that monitors processor health and disables actuation requests if processor malfunction is detected.
12. The method of claim 1, further comprising adapting parameters of said coupling function based on vehicle speed.
13. The method of claim 1, wherein said actuation request includes a confidence score indicating reliability of the underlying perception data.

## 13. Drawings / Figures Description

### Figure 1: System Architecture Block Diagram
- Shows dual-camera inputs flowing through perception models to risk coupling engine
- Illustrates separation between ADVIS request generation and OEM actuation authority
- Labels all data flows and interfaces

### Figure 2: Risk Coupling Function Visualization
- 3D surface plot showing coupled risk as function of scene risk (x-axis) and driver attention (y-axis)
- Color gradient indicating coupled risk intensity
- Annotated operating regions (safe, cautious, critical)

### Figure 3: Threshold Modulation Diagram
- Timeline showing how intervention thresholds shift with changing coupled risk
- Example scenario: driver looks away while approaching slow vehicle
- Comparison with fixed-threshold system response

### Figure 4: Actuation Request Protocol
- CAN-FD message format for actuation requests
- Request escalation ladder (advisory -> warning -> urgent request)
- OEM ECU decision authority boundary clearly marked

### Figure 5: Decision Fusion Timing Diagram
- Shows temporal relationship between: scene risk change, attention change, coupled metric update, threshold modulation, request generation
- Demonstrates low-latency single-SoC advantage

## 14. Commercial Value

### Market Opportunity

- Euro NCAP 2026 mandates DMS presence and "adequate response" to distraction
- UNECE regulation (UN R167) requires DMS for automated driving systems
- No existing regulation specifies coupled risk assessment (opportunity to establish standard)
- Combined ADAS+DMS decision fusion is a key differentiator for OEM bids

### Revenue Model

| Revenue Stream | Estimated Value |
|---------------|-----------------|
| Per-unit software license (includes fusion algorithm) | $3-8 per unit |
| OEM integration engineering | $200K-500K per program |
| Algorithm licensing to other Tier-1s | $1M-5M per licensee |

### Competitive Advantage

- First-to-file on coupled risk assessment creates blocking patent position
- OEMs can claim "intelligent driver awareness" in marketing
- Regulatory trend toward integrated DMS+ADAS creates growing market

## 15. Filing Recommendation

**Recommendation: File Provisional Patent Application IMMEDIATELY (highest priority)**

- **Filing type**: Provisional (US) to establish earliest possible priority date
- **Conversion**: Non-provisional within 12 months with expanded claims
- **International**: PCT application - this is a global automotive technology
- **Priority territories**: US, EU (Germany, France), China, Japan, South Korea, India
- **Urgency**: CRITICAL - This is the most novel and commercially valuable of the 5 filings. Competitors are moving toward integrated systems.
- **Note**: This is filing priority #1 among the ADVIS patent portfolio

## 16. Confidentiality Classification

| Element | Classification |
|---------|---------------|
| General coupled-risk concept | PATENT - Public upon filing |
| Coupling function architecture | PATENT - Public upon filing |
| Specific coupling exponent (alpha) values | TRADE SECRET - Never disclose |
| Calibration thresholds for production | TRADE SECRET - Never disclose |
| Training dataset details (Indian road data) | TRADE SECRET - Never disclose |
| Model tuning parameters | TRADE SECRET - Never disclose |
| Perception model architecture details | TRADE SECRET - Where novel, file separately |
| CAN message format for requests | PATENT - General format only |

## 17. Next Steps

- [ ] File provisional application IMMEDIATELY (priority #1)
- [ ] Complete comprehensive prior art search (Seeing Machines, Mobileye, Toyota, GM patents)
- [ ] Develop formal patent drawings (5 figures minimum)
- [ ] Prepare demonstration video showing coupled risk concept
- [ ] Coordinate with ID-005 (Risk-Aware Power Control) for cross-referencing
- [ ] Review with patent attorney for claim scope optimization
- [ ] Identify continuation application opportunities (additional coupling methods)
- [ ] Budget allocation: provisional filing ($3K-5K) + international PCT ($15K-25K)
- [ ] Confirm safety boundary language satisfies regulatory review

---

**Document Version:** 1.0  
**Last Updated:** 2025-01  
**Classification:** CONFIDENTIAL - Attorney-Client Privilege  
**Witness Signature:** _________________ Date: _________  
**Witness Signature:** _________________ Date: _________
