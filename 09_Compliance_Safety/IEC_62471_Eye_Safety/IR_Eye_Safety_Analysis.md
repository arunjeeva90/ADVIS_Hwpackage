# ADVIS IR Eye Safety Analysis (IEC 62471)

| Field | Value |
|-------|-------|
| Document ID | ADVIS-CS-IRS-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Optical Safety Team |
| Date | 2024-01-15 |
| Classification | CONFIDENTIAL |

---

## 1. Scope

This document presents the photobiological safety analysis for the infrared (IR) LED illumination system used in the ADVIS DMS (Driver Monitoring System) camera subsystem. The analysis follows IEC 62471:2006 (Photobiological safety of lamps and lamp systems) and classifies the emission risk group.

## 2. System Description

### 2.1 IR Illumination Configuration

| Parameter | Value |
|-----------|-------|
| Application | Driver face illumination for DMS camera |
| Wavelength | 940 nm (nominal) |
| LED type | IR LED array on daughterboard |
| Number of LEDs | [TBD - design dependent, typically 4-8] |
| Drive method | PWM-controlled via IR_LED_EN and IR_PWM signals |
| Beam pattern | Wide-angle (>= 60 deg half-angle) for uniform face coverage |
| Mounting distance to driver | 0.5 m - 1.0 m (typical windshield mount to driver) |
| Operating duty cycle | Variable (10% - 100% PWM) |
| Maximum continuous operation | During all driving conditions (nighttime DMS) |

### 2.2 Control Signals

| Signal | Function | Safety Role |
|--------|----------|-------------|
| IR_LED_EN | Master enable (active HIGH) | Disables all IR when LOW |
| IR_PWM | Intensity modulation | Limits average power |
| Thermal feedback | Over-temperature protection | Reduces/disables IR at thermal limit |

## 3. IEC 62471 Risk Group Classification

### 3.1 Applicable Hazards for IR (940 nm)

At 940 nm wavelength, the relevant photobiological hazards per IEC 62471 are:

| Hazard | Wavelength Range | Applicable to 940nm? | Assessment |
|--------|------------------|---------------------|------------|
| Actinic UV | 200 - 400 nm | No | Not applicable |
| Near-UV | 315 - 400 nm | No | Not applicable |
| Blue light (retinal) | 300 - 700 nm | No | Not applicable |
| Retinal thermal | 380 - 1400 nm | **Yes** | Must evaluate |
| IR-A corneal/lens | 780 - 1400 nm | **Yes** | Must evaluate |
| IR-B/C corneal | 780 - 3000 nm | **Yes** | Must evaluate |

### 3.2 Exposure Limits

Per IEC 62471, Table 6.2 (Infrared radiation hazard to the eye):

| Exposure Duration | Limit (E_IR) | Wavelength |
|-------------------|--------------|------------|
| t > 1000 s | 100 W/m^2 | 780 - 3000 nm |
| t <= 1000 s | 18000/t^(3/4) W/m^2 | 780 - 3000 nm |

For retinal thermal hazard (780 - 1400 nm):
- Depends on angular subtense of source and exposure duration
- For extended sources (LED array): limits are more relaxed

### 3.3 Measurement Conditions

Per IEC 62471, measurements for risk classification:

| Condition | Distance | Aperture |
|-----------|----------|----------|
| Exempt Group / RG1 | 200 mm from apparent source | 7 mm (pupil, worst case) |
| Risk Group 2 | 200 mm | 7 mm |
| Risk Group 3 | 200 mm | 7 mm |

**Note:** For the ADVIS application, the actual viewing distance is 500-1000 mm (windshield to driver), which provides additional safety margin beyond the 200 mm measurement condition.

### 3.4 Classification Target

| Risk Group | Meaning | ADVIS Target |
|------------|---------|--------------|
| **Exempt** | No photobiological hazard under any reasonable condition | **Primary target** |
| **Risk Group 1 (Low Risk)** | No hazard due to normal behavioral limitations (aversion) | **Acceptable alternative** |
| Risk Group 2 (Moderate Risk) | Potential hazard; requires administrative controls | Not acceptable for DMS |
| Risk Group 3 (High Risk) | Hazard even for momentary exposure | Not acceptable |

## 4. Radiometric Analysis

### 4.1 Worst-Case Calculation

**Assumptions (worst case):**
- All LEDs operating at 100% duty cycle (IR_PWM = 100%)
- Distance: 200 mm (IEC 62471 measurement distance, closer than actual use)
- Pupil diameter: 7 mm (dark-adapted, maximizes retinal exposure)
- No protective barrier between LEDs and driver

**Calculation Framework:**

```
Total radiant intensity: I_e = N_LED x I_LED [W/sr]
Irradiance at 200mm:    E = I_e / (0.2m)^2 [W/m^2]
Compare to limit:       E vs. 100 W/m^2 (continuous exposure limit)
```

**Design Budget:**

| Parameter | Budget (for Exempt classification) |
|-----------|-----------------------------------|
| Maximum irradiance at 200 mm | < 100 W/m^2 |
| Maximum irradiance at 500 mm (actual) | < 16 W/m^2 (inverse square) |
| Per-LED radiant intensity budget | < I_total / N_LED |

### 4.2 Typical 940nm DMS LED Parameters

| Parameter | Typical Range | Unit |
|-----------|--------------|------|
| Radiant intensity per LED | 20 - 100 | mW/sr |
| Total radiant flux per LED | 50 - 200 | mW |
| Half-angle | 30 - 60 | degrees |
| Forward current (max) | 100 - 500 | mA |
| Package | Surface mount, 3535 or 5050 | - |

### 4.3 Expected Classification Result

For a typical 940 nm DMS illuminator (4-8 LEDs, wide beam, 0.5-1.0m distance):
- **Expected classification: Exempt or Risk Group 1 (Low Risk)**
- This is consistent with commercially available DMS systems

## 5. Protective Measures

Regardless of classification, the following protective measures are implemented:

### 5.1 Engineering Controls

| Control | Implementation | Purpose |
|---------|----------------|---------|
| PWM duty limiting | Maximum PWM capped in firmware | Limits average optical power |
| Thermal derating | IR current reduced at high temperature | Prevents over-drive |
| Master enable | IR_LED_EN controlled by SoM | System-level on/off |
| Fault detection | Monitor LED current for open/short | Detect failure modes |
| Timeout watchdog | IR disabled if no SoM heartbeat | Prevent uncontrolled emission |

### 5.2 Inherent Safety Features

| Feature | Description |
|---------|-------------|
| 940 nm wavelength | Invisible to human eye; no discomfort/aversion response needed |
| Wide beam angle | Low irradiance density at any point |
| Distance (0.5-1.0 m) | Significant inverse-square-law reduction |
| Short exposure per frame | Pulsed operation reduces average exposure |

### 5.3 Administrative Controls (Production)

| Control | Requirement |
|---------|-------------|
| Eye safety label | Applied to product if RG1 or higher |
| User manual statement | IR emission notice per IEC 62471 |
| Service manual warning | Do not look directly at LEDs during bench test |
| Production test limit | Verify LED current does not exceed rated maximum |

## 6. Labeling Requirements

### 6.1 Per IEC 62471 and IEC 60825-1 (if applicable)

| Classification | Required Label | Label Content |
|----------------|----------------|---------------|
| Exempt | None required | Optional: "Contains IR LEDs" |
| Risk Group 1 | Caution label | "CAUTION: IR radiation emitted. Do not stare directly into beam." |
| Risk Group 2 | Warning label | Not acceptable for this application |

### 6.2 ADVIS Product Label (Proposed)

Even if classified as Exempt:
```
+------------------------------------------+
| Contains infrared LED emitters (940 nm)  |
| Class 1 LED product per IEC 62471       |
| Do not view directly with optical aids   |
+------------------------------------------+
```

## 7. Verification Testing

### 7.1 Measurements Required

| Measurement | Equipment | Standard |
|-------------|-----------|----------|
| Spectral irradiance at 200 mm | Spectroradiometer (780-1100 nm) | IEC 62471, Clause 6 |
| Radiant intensity (per LED and total) | Calibrated detector + integrating sphere | IEC 62471 |
| Beam profile (angular distribution) | Goniometer or far-field detector | IEC 62471 |
| PWM waveform (temporal) | Photodetector + oscilloscope | Internal verification |
| Thermal derating verification | IR power meter + thermal chamber | Internal verification |

### 7.2 Test Conditions

| Condition | Setting | Rationale |
|-----------|---------|-----------|
| Maximum current | All LEDs at rated max | Worst-case optical power |
| Maximum PWM | 100% duty cycle | Maximum average irradiance |
| Minimum distance | 200 mm | IEC 62471 measurement condition |
| Ambient temperature | 25C | Nominal measurement |
| Fresh LEDs (0 hours) | New production units | Maximum output (before aging) |

## 8. Compliance Statement

Based on preliminary analysis and comparison with similar commercial DMS systems:

- The ADVIS IR illumination system is expected to achieve **Exempt** or **Risk Group 1** classification per IEC 62471.
- Final classification requires laboratory measurement with calibrated equipment.
- The design includes multiple engineering controls to ensure safe operation even in single-fault conditions.
- No direct actuation hazard exists (IR failure = loss of DMS function, not vehicle control loss).

## 9. References

| Document | Relevance |
|----------|-----------|
| IEC 62471:2006 | Photobiological safety of lamps and lamp systems |
| IEC 62471:2006/AMD1:2008 | Amendment 1 |
| IEC TR 62471-2:2009 | Guidance on manufacturing requirements |
| IEC 60825-1:2014 | Safety of laser products (not directly applicable but referenced) |
| EU Directive 2006/25/EC | Workers' exposure to artificial optical radiation |

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2024-01-15 | Optical Safety Team | Initial draft |
