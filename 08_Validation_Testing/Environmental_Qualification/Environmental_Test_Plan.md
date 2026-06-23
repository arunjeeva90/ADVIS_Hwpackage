# ADVIS Environmental Qualification Test Plan

| Field | Value |
|-------|-------|
| Document ID | ADVIS-VT-ENV-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Reliability & Qualification Team |
| Date | 2024-01-15 |
| Classification | CONFIDENTIAL |

---

## 1. Scope

This document defines the environmental qualification test plan for the ADVIS ECU per automotive standards. The ECU is designed for windshield-mount installation in passenger vehicles, rated for AEC-Q100 Grade 2 operating temperature range (-40C to +85C ambient).

## 2. Applicable Standards

| Standard | Scope | Application |
|----------|-------|-------------|
| ISO 16750-1 | General | Test conditions and definitions |
| ISO 16750-2 | Electrical loads | Supply voltage conditions |
| ISO 16750-3 | Mechanical loads | Vibration, shock |
| ISO 16750-4 | Climatic loads | Temperature, humidity |
| ISO 16750-5 | Chemical loads | Fluid resistance (if applicable) |
| AEC-Q100 Rev. J | IC qualification | Grade 2 (-40C to +105C junction) |
| AEC-Q200 Rev. D | Passive qualification | Operating temperature range |
| IEC 60068-2-x | Environmental testing | Test method reference |

## 3. Installation Category

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Mounting location | Windshield (behind rearview mirror) | DMS + forward camera position |
| ISO 16750 location class | Code 3A (passenger compartment, not directly heated) | Interior mount, indirect solar |
| Temperature range (ambient) | -40C to +85C | AEC-Q100 Grade 2 |
| Humidity exposure | Up to 95% RH (non-condensing in operation) | Cabin environment |
| Vibration severity | Moderate (passenger car, body-mounted) | Not engine-mounted |

## 4. Test Sample Requirements

| Test Group | Sample Size | Acceptance Criteria |
|------------|-------------|---------------------|
| Temperature cycling | 5 units (minimum) | 0/5 failures |
| High-temperature operating life | 5 units | 0/5 failures |
| Low-temperature operating | 3 units | 0/3 failures |
| Temperature-humidity bias | 5 units | 0/5 failures |
| Vibration (random) | 3 units | 0/3 failures |
| Vibration (sinusoidal) | 3 units | 0/3 failures |
| Mechanical shock | 3 units | 0/3 failures |
| Thermal shock | 3 units | 0/3 failures |
| Salt spray (if applicable) | 3 units | 0/3 failures (connector only) |

## 5. Test Procedures

### 5.1 Temperature Cycling (Powered)

**Reference:** IEC 60068-2-14 (Test Na), ISO 16750-4

**Parameters:**

| Parameter | Value |
|-----------|-------|
| Low temperature | -40C |
| High temperature | +85C |
| Dwell time at extremes | 30 minutes (minimum) |
| Transition rate | 5C/min (typical) |
| Number of cycles | 1000 |
| DUT state during test | Powered, operating (Mode A) |
| Monitoring | Continuous functional check |

**Functional Checks During Test:**
- CAN communication (heartbeat message every 100 ms)
- Camera stream integrity (frame counter, no corruption)
- Power rail monitoring (within specification)
- GNSS lock maintenance (when signal available)

**Pass/Fail Criteria:**
- All functions operational at temperature extremes
- No intermittent failures during transitions
- Post-test visual inspection: no solder cracks, delamination, or component damage
- Post-test electrical: all parameters within specification
- Microsection (2 units): no solder joint degradation beyond acceptable limits

### 5.2 High-Temperature Operating Life (HTOL)

**Reference:** AEC-Q100 Test A (JESD22-A108)

**Parameters:**

| Parameter | Value |
|-----------|-------|
| Temperature | +85C ambient (Grade 2) |
| Duration | 1000 hours |
| DUT state | Powered, maximum operating conditions |
| Power supply | 13.5V nominal |
| Readout intervals | 0h, 168h, 500h, 1000h |

**Measurements at Each Readout:**
- All power rail voltages (accuracy and ripple)
- Quiescent current consumption
- Camera image quality (SNR, uniformity)
- CAN transceiver parameters (V_dom, V_rec)
- IMU bias stability

**Pass/Fail Criteria:**
- Parameter drift: < 5% from initial measurement
- No functional failures
- No physical damage (visual inspection at 20x magnification)

### 5.3 Low-Temperature Operating

**Reference:** ISO 16750-4, IEC 60068-2-1 (Test Ab)

**Parameters:**

| Parameter | Value |
|-----------|-------|
| Temperature | -40C |
| Duration | 96 hours continuous |
| DUT state | Powered, full operation |
| Cold start test | Power-on at -40C from unpowered state |

**Cold Start Verification:**
1. Soak DUT at -40C for 4 hours (unpowered)
2. Apply power (13.5V)
3. Measure time to full operation (all subsystems ready)
4. Verify all functions within 30 seconds of power application

**Pass/Fail Criteria:**
- Full functionality at -40C
- Cold start to full operation: < 30 seconds
- Power sequencing correct at all temperatures
- No display artifacts, camera degradation, or communication errors

### 5.4 Temperature-Humidity Bias (THB)

**Reference:** AEC-Q100 Test B (JESD22-A101), ISO 16750-4

**Parameters:**

| Parameter | Value |
|-----------|-------|
| Temperature | +85C |
| Relative humidity | 85% RH |
| Duration | 1000 hours |
| DUT state | Powered, bias applied to all rails |
| Readout intervals | 0h, 168h, 500h, 1000h |

**Pass/Fail Criteria:**
- No corrosion on PCB traces or component leads
- Insulation resistance > 100 Mohm between adjacent nets
- No parameter drift > 5% from initial
- No delamination of PCB or conformal coating (if applied)
- Surface insulation resistance (SIR) per IPC-9201

### 5.5 Random Vibration

**Reference:** ISO 16750-3, IEC 60068-2-64

**Parameters (passenger car, body/instrument panel mount):**

| Parameter | Value |
|-----------|-------|
| Frequency range | 10 Hz - 2000 Hz |
| Overall G_rms | 3.1 G_rms (per ISO 16750-3, Table 12) |
| Duration | 8 hours per axis |
| Axes | 3 orthogonal axes (X, Y, Z) |
| DUT state | Powered, operating |

**PSD Profile (simplified):**

| Frequency (Hz) | PSD (G^2/Hz) |
|-----------------|--------------|
| 10 | 0.010 |
| 50 | 0.010 |
| 100 | 0.005 |
| 300 | 0.005 |
| 1000 | 0.001 |
| 2000 | 0.001 |

**Monitoring During Test:**
- CAN heartbeat (error counter)
- Camera frame continuity
- Accelerometer (BMI088) data vs. reference accelerometer

**Pass/Fail Criteria:**
- No intermittent failures during vibration
- No resonance-induced failures
- Post-test: all functions nominal
- Post-test: visual inspection (no loose components, cracked solder)
- Natural frequency of assembly > 200 Hz (confirmed by sweep)

### 5.6 Sinusoidal Vibration (Resonance Survey)

**Reference:** ISO 16750-3, IEC 60068-2-6

**Parameters:**

| Parameter | Value |
|-----------|-------|
| Frequency range | 10 Hz - 2000 Hz |
| Sweep rate | 1 octave/minute |
| Amplitude | 1.0 G (peak), 0-peak |
| Axes | 3 orthogonal |
| Purpose | Resonance identification |

**Follow-up:** If resonances found below 200 Hz, perform resonance dwell (10^6 cycles at each resonance).

### 5.7 Mechanical Shock

**Reference:** ISO 16750-3, IEC 60068-2-27

**Parameters:**

| Parameter | Value |
|-----------|-------|
| Pulse shape | Half-sine |
| Peak acceleration | 50 G |
| Duration | 6 ms |
| Number of shocks | 3 per direction, 6 directions (+/-X, +/-Y, +/-Z) |
| Total shocks | 18 |
| DUT state | Unpowered |

**Pass/Fail Criteria:**
- No structural damage
- Full functionality after test
- No solder joint failures (X-ray if BGA/QFN present)

### 5.8 Thermal Shock

**Reference:** IEC 60068-2-14 (Test Na), rapid transition

**Parameters:**

| Parameter | Value |
|-----------|-------|
| Low temperature | -40C |
| High temperature | +125C |
| Transfer time | < 30 seconds |
| Dwell time | 15 minutes at each extreme |
| Number of cycles | 500 |
| DUT state | Unpowered |

**Pass/Fail Criteria:**
- Post-test functional test: all parameters pass
- Visual/X-ray: no solder joint cracking
- Cross-section (destructive, 2 samples): acceptable intermetallic growth

### 5.9 Salt Spray (Connector Qualification)

**Reference:** IEC 60068-2-11, ISO 16750-5 (if exterior connector)

**Applicability:** Only if connector is exposed to road environment (e.g., chassis-side connector). For interior windshield mount, this test may be waived per engineering judgment.

**Parameters (if applicable):**

| Parameter | Value |
|-----------|-------|
| NaCl concentration | 5% |
| Temperature | 35C |
| Duration | 96 hours |
| Test specimen | Connector assembly only |

**Pass/Fail Criteria:**
- Contact resistance increase: < 5 mohm
- No corrosion affecting mating integrity
- Visual: no base metal corrosion

## 6. Test Sequence and Dependencies

```
  +-----------------+     +------------------+     +-------------------+
  | Initial         | --> | Group A:         | --> | Group B:          |
  | Characterization|     | Thermal          |     | Mechanical        |
  | (all parameters)|     | (TC, HTOL, THB)  |     | (Vib, Shock)      |
  +-----------------+     +------------------+     +-------------------+
                                                            |
                                                            v
                                                   +-------------------+
                                                   | Final             |
                                                   | Characterization  |
                                                   | (all parameters)  |
                                                   +-------------------+
```

## 7. Failure Analysis Procedure

If any sample fails during qualification:
1. Document failure mode and test conditions at failure
2. Perform failure analysis (visual, X-ray, cross-section, FTIR)
3. Identify root cause
4. Implement corrective action
5. Restart qualification from beginning with corrected design

## 8. Reporting

Qualification report shall include:
- Test configuration and photographs
- Sample traceability (serial numbers, build lot)
- Results summary (pass/fail matrix)
- Measurement data at each readout interval
- Failure analysis reports (if any)
- Comparison to initial characterization
- Qualification conclusion and sign-off

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2024-01-15 | Reliability & Qualification Team | Initial draft |
