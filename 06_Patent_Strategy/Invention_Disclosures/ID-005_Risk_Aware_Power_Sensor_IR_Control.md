# Invention Disclosure: ID-005

## CONFIDENTIAL - INTERNAL DRAFT

---

## 1. Title

Risk-Aware Adaptive Power, Sensor, and IR Illumination Control for Dual-Camera ADAS/DMS Module

## 2. Date

June 2026

## 3. Inventors

[To be filled - engineering team members who contributed to this concept]

## 4. Status

DRAFT - Awaiting prior art search and patent attorney review

---

## 5. Problem Statement

A compact windshield-mounted camera module has strict thermal and power budgets. Running all subsystems at full performance at all times wastes power, generates excess heat, and reduces component lifetime. Key problems include:

- SoC running full AI inference continuously consumes maximum power even when road risk is low
- DMS IR illumination running continuously wastes power and contributes to thermal load
- Camera sensors operating at maximum frame rate and resolution at all times is unnecessary during low-risk driving
- No existing system dynamically adjusts hardware power states, sensor modes, and IR illumination based on real-time driving risk assessment
- Thermal throttling is reactive (degrades performance after overheating); a proactive risk-aware approach could prevent thermal events

## 6. Background / Prior Art Summary

### Existing Approaches

| Approach | Example | Limitation |
|----------|---------|------------|
| Fixed power states | Most ADAS cameras | Always full power; no adaptation |
| Simple day/night IR switching | Generic DMS | Binary IR on/off based on ambient light only |
| CPU frequency scaling (DVFS) | All modern SoCs | Based on compute load, not driving risk |
| Thermal throttling | All SoCs | Reactive; degrades performance after overheating |

### Gap in Prior Art

No known system:
1. Uses a real-time driving risk score to proactively control hardware power states
2. Modulates camera frame rate, SoC performance, and IR illumination together based on risk
3. Implements predictive thermal management driven by situational awareness rather than temperature alone
4. Ties power budget allocation to perception priority (more power to higher-risk subsystem)

## 7. Proposed Solution

A risk-aware adaptive control system that dynamically adjusts:

1. **SoC performance state:** AI inference frequency/precision scaled to risk level
2. **Camera sensor mode:** Frame rate and resolution adjusted per channel based on need
3. **IR illumination:** Duty cycle, intensity, and pattern adapted to driver monitoring need
4. **Power rail management:** Non-critical subsystems powered down during low-risk periods

### Operating Modes

| Risk Level | SoC State | Forward Camera | DMS Camera | IR LEDs | Power Budget |
|------------|-----------|---------------|------------|---------|--------------|
| Low (highway, clear, attentive driver) | Reduced clock | 15 fps, standard res | 10 fps | Low duty cycle | Minimum |
| Medium (urban, moderate traffic) | Nominal | 30 fps | 15 fps | Medium duty cycle | Nominal |
| High (hazard detected, driver inattentive) | Maximum | 30 fps, HDR | 30 fps | Maximum duty cycle | Maximum |
| Critical (imminent collision risk) | Maximum boost | 60 fps if capable | 30 fps | Continuous | Peak (time-limited) |

## 8. Key Novel Elements

1. **Risk-driven power allocation:** Driving risk score (from ID-001 fusion) directly controls hardware power states
2. **Coordinated multi-subsystem adaptation:** SoC, cameras, and IR adjust together as a system
3. **Predictive thermal management:** Risk-aware scheduling prevents thermal throttling by managing power proactively
4. **IR duty cycle modulation:** DMS IR intensity tracks actual driver monitoring need (not binary on/off)
5. **Safety floor guarantee:** Minimum perception capability maintained at all risk levels; adaptation is upward from floor, not downward from maximum

## 9. Technical Implementation Details

### Control Architecture

```
[Risk Coupling Engine (from ID-001)]
         |
    Risk Level Signal
         |
[Power/Sensor/IR Controller]
    |         |          |
    v         v          v
[SoC DVFS] [Camera Mode] [IR PWM]
    |         |          |
    v         v          v
[Thermal Monitor] <-- feedback loop
```

### Control Logic

- Risk level mapped to predefined hardware state combinations
- Transitions between states have controlled ramp rates (no abrupt power spikes)
- Thermal headroom measurement feeds into maximum allowable power state
- If thermal budget is exceeded even at current risk-demanded state, graceful degradation applies to lowest-priority subsystem first
- Safety floor: minimum frame rate and minimum AI capability always maintained regardless of thermal state

### IR Illumination Strategy

- Ambient light sensor determines baseline IR need (none in daylight, increasing at dusk/night)
- DMS risk level modulates duty cycle above baseline
- IR intensity increased when driver monitoring requires higher confidence (inattention detected)
- IR reduced when driver face is well-illuminated by ambient light or when DMS is in low-priority state
- Eye-safety limits enforced in hardware (cannot exceed IEC 62471 limits regardless of software request)

*Note: Specific control parameters, state transition thresholds, and thermal model coefficients are trade secrets.*

## 10. Advantages Over Prior Art

| Advantage | Benefit |
|-----------|---------|
| Proactive thermal management | Prevents performance-degrading thermal throttling |
| Reduced average power consumption | Extends component lifetime; reduces thermal load 20-40% |
| Risk-appropriate performance | Maximum capability available when needed most |
| Coordinated control | System-level optimization vs. per-component optimization |
| Safety floor maintained | Never drops below minimum safe perception capability |
| IR power reduction | Reduces eye-safety risk margin consumption; extends LED lifetime |

## 11. Alternative Embodiments

1. **Machine-learning power predictor:** Train model on driving patterns to predict upcoming risk and pre-stage hardware
2. **V2X-informed power scheduling:** Vehicle-to-infrastructure data provides advance warning of upcoming high-risk zones
3. **Multi-camera priority allocation:** In variants with more than two cameras, dynamically allocate power budget to highest-priority camera
4. **Battery-backed mode:** For parking surveillance, operate in ultra-low-power mode with minimal perception
5. **OEM-configurable risk-to-power mapping:** Allow OEM to customize the risk-to-power-state mapping via CAN configuration

## 12. Potential Claims

### Independent Claim 1 (Method)

A method of controlling power consumption in a vehicle camera module, comprising:
- determining a driving risk level based on forward-facing scene analysis and driver state analysis;
- selecting a power allocation profile from a plurality of profiles based on said driving risk level;
- adjusting a processing unit operating frequency according to said selected profile;
- adjusting a camera sensor frame rate according to said selected profile; and
- adjusting a near-infrared illumination duty cycle according to said selected profile;
- wherein a minimum perception capability is maintained at all risk levels.

### Independent Claim 2 (System)

A vehicle camera system comprising:
- a forward-facing camera;
- a cabin-facing camera;
- a near-infrared illumination source;
- a processing unit; and
- a power controller configured to:
  - receive a risk level signal from a perception pipeline;
  - adjust power states of said processing unit, said cameras, and said illumination source based on said risk level signal;
  - monitor thermal state; and
  - constrain power allocation to maintain thermal headroom while satisfying a minimum perception safety floor.

### Dependent Claims

3. The method of claim 1, further comprising predicting a future thermal state based on current power allocation and ambient conditions.
4. The method of claim 1, wherein said near-infrared illumination duty cycle is further modulated by ambient light measurement.
5. The system of claim 2, wherein said power controller implements controlled ramp rates between power states.
6. The method of claim 1, wherein said minimum perception capability comprises a minimum forward camera frame rate and a minimum driver monitoring update rate.

*Note: Final patent claim language must be reviewed by a patent attorney.*

## 13. Drawings / Figures Description

### Figure 1: Risk-Aware Power Control Architecture
- Block diagram showing risk engine input, power controller, and controlled subsystems

### Figure 2: Operating Mode State Diagram
- State transitions between Low/Medium/High/Critical power modes with transition conditions

### Figure 3: IR Duty Cycle Modulation
- Timing diagram showing IR PWM changes in response to risk level and ambient light

### Figure 4: Thermal Management Integration
- Feedback loop showing thermal measurement constraining power allocation

## 14. Commercial Value

- Competitive differentiator: intelligent power management reduces module thermal design requirements
- Enables compact windshield mount (lower average power reduces thermal spreader requirements)
- Extends component lifetime (reduced average junction temperature)
- Addresses OEM concern about power consumption of always-on camera modules
- Potential licensing to other ADAS/DMS module manufacturers

## 15. Filing Recommendation

**Recommendation: File Provisional Patent Application**

- Filing type: Provisional (US) to establish priority date
- Conversion: Non-provisional within 12 months
- International: PCT recommended
- Priority territories: US, EU, China, Japan, South Korea
- Urgency: Medium - power management innovation timeline allows 90-day filing window

## 16. Confidentiality Classification

| Element | Classification |
|---------|---------------|
| Risk-driven power concept | PATENT - Disclose in filing |
| Control architecture block diagram | PATENT - Disclose in filing |
| Operating mode definitions | PATENT - Disclose at abstract level |
| Specific state transition thresholds | TRADE SECRET - Never disclose |
| Thermal model coefficients | TRADE SECRET - Never disclose |
| IR duty cycle algorithm parameters | TRADE SECRET - Never disclose |
| DVFS frequency/voltage tables | TRADE SECRET - Never disclose |

## 17. Next Steps

- [ ] Complete prior art search (power management patents, adaptive ADAS systems)
- [ ] Verify no blocking patents from TI, Qualcomm, NVIDIA, Intel
- [ ] Develop formal patent drawings (4 figures minimum)
- [ ] Review with patent attorney for claim refinement
- [ ] Coordinate with ID-001 (risk fusion) for risk level input definition
- [ ] Prototype risk-aware power controller algorithm
- [ ] Prepare provisional application filing package

---

**Document Version:** 1.0  
**Last Updated:** June 2026  
**Classification:** CONFIDENTIAL - INTERNAL DRAFT  
**Witness Signature:** _________________ Date: _________  
**Witness Signature:** _________________ Date: _________
