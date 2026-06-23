# ADVIS Reliability Test Plan

| Field | Value |
|-------|-------|
| Document ID | ADVIS-VT-REL-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Reliability Engineering Team |
| Date | 2024-01-15 |
| Classification | CONFIDENTIAL |

---

## 1. Scope

This document defines the reliability test plan for the ADVIS ECU, including Highly Accelerated Life Testing (HALT), Highly Accelerated Stress Screening (HASS), accelerated life testing (ALT), and MTBF prediction methodology. The plan ensures the ADVIS ECU meets automotive reliability targets for the intended 15-year / 300,000 km vehicle lifetime.

## 2. Reliability Targets

| Parameter | Target | Basis |
|-----------|--------|-------|
| Design life | 15 years / 300,000 km | OEM vehicle lifetime requirement |
| Operating hours | 6,000 hours (typical) | 400 hrs/year average use |
| MTBF (predicted) | >= 50,000 hours | MIL-HDBK-217F / Telcordia SR-332 |
| Field failure rate (warranty) | < 100 ppm/year | OEM warranty cost target |
| Infant mortality screen | HASS (production) | Remove latent defects |
| Useful life failures | Random, < 50 FIT per function | Exponential distribution |

## 3. HALT (Highly Accelerated Life Testing)

### 3.1 Purpose

HALT identifies design weaknesses and margins beyond the specification limits. It is NOT a pass/fail test but a tool to find and fix weaknesses during development.

### 3.2 HALT Profile

| Stage | Parameter | Start | Step | Hold | Monitor |
|-------|-----------|-------|------|------|---------|
| Cold step stress | Temperature | +25C | -10C steps | 10 min/step | Full function |
| | | Continue until | Failure or -80C | | |
| Hot step stress | Temperature | +25C | +10C steps | 10 min/step | Full function |
| | | Continue until | Failure or +130C | | |
| Vibration step | Random vib | 5 Grms | +5 Grms steps | 10 min/step | Full function |
| | | Continue until | Failure or 60 Grms | | |
| Combined (cold + vib) | Temp + Vib | -40C, 10 Grms | Increase both | 10 min/step | Full function |
| Combined (hot + vib) | Temp + Vib | +85C, 10 Grms | Increase both | 10 min/step | Full function |
| Rapid thermal transition | -60C to +120C | 60C/min | 20 cycles | - | Post-cycle check |

### 3.3 HALT Monitoring

During each HALT step, monitor:
- All power rails (voltage, current)
- CAN communication (heartbeat)
- Camera streaming (frame counter)
- IMU output (compare to reference)
- GNSS (if signal available)

### 3.4 HALT Exit Criteria

| Outcome | Action |
|---------|--------|
| Operating margin > 20C beyond spec on both extremes | Adequate margin |
| Operating margin < 20C beyond spec | Investigate, potential design change |
| Destruct limit found | Document, assess against margin requirements |
| Intermittent failures observed | Root cause, corrective action required |

### 3.5 HALT Sample Size

- Minimum 5 units from prototype build
- 2 additional units designated for destructive analysis post-HALT

## 4. HASS (Highly Accelerated Stress Screening)

### 4.1 Purpose

HASS is applied to production units to precipitate latent defects (infant mortality) that would otherwise cause early field failures.

### 4.2 HASS Profile (Production Screen)

| Parameter | Value | Duration |
|-----------|-------|----------|
| Temperature range | -30C to +80C (within HALT operating limits) | 20 cycles |
| Transition rate | >= 40C/min | - |
| Dwell time at extremes | 5 minutes | - |
| Vibration (combined) | 10 Grms random | During thermal transitions |
| Power cycling | 5 cycles (off/on during dwell) | At each extreme |
| Total screen time | < 4 hours | Production throughput target |

### 4.3 HASS Monitoring

- Power-on self-test (POST) at each power cycle
- CAN communication check
- Camera initialization check
- All tests must pass within 10 seconds of power application

### 4.4 HASS Effectiveness

Track the following metrics to validate HASS effectiveness:

| Metric | Target |
|--------|--------|
| Detection rate (known defects) | >= 95% |
| False failure rate | < 2% |
| Remaining useful life consumption | < 5% of design life |

## 5. Accelerated Life Testing (ALT)

### 5.1 Methodology

Use acceleration factors based on Arrhenius model (temperature) and inverse power law (vibration/voltage) to predict useful life from accelerated test data.

### 5.2 ALT Test Conditions

| Stress Factor | Use Condition | Accelerated Condition | Acceleration Factor |
|---------------|---------------|----------------------|---------------------|
| Temperature | 50C avg (cabin) | 100C continuous | ~16x (Ea=0.7eV) |
| Thermal cycling | 1 cycle/day (-20C to +60C) | 12 cycles/day (-40C to +100C) | ~48x |
| Vibration | 0.5 Grms road | 3 Grms continuous | ~36x (n=2) |
| Voltage | 13.5V nominal | 16V continuous | ~2x |

### 5.3 ALT Duration and Sample Size

| Test | Duration | Samples | Equivalent Field Life |
|------|----------|---------|----------------------|
| HTOL (100C, powered) | 2000 hours | 10 | 32,000 hours (~5 years) |
| Thermal cycling (accelerated) | 5000 cycles | 5 | 15 years |
| Vibration endurance | 500 hours | 5 | 15 years |
| Combined stress | 1000 hours | 5 | 15 years |

### 5.4 Weibull Analysis

Failure data shall be analyzed using Weibull distribution:
- Plot failures on Weibull probability paper
- Determine shape parameter (beta) and characteristic life (eta)
- Extrapolate to field conditions using acceleration factors
- Report B1 life (1% failure) and B10 life (10% failure) at field conditions

## 6. MTBF Prediction

### 6.1 Prediction Methodology

| Method | Application | Tool |
|--------|-------------|------|
| MIL-HDBK-217F (Parts Count) | Initial estimate during design | Relex / BQR |
| Telcordia SR-332 (Method I) | Refined prediction | Relex / BQR |
| IEC 62380 | European OEM requirement (if applicable) | RAM Commander |
| Field data feedback | Post-launch correction | In-house database |

### 6.2 Environmental Factors

| Parameter | Value | Basis |
|-----------|-------|-------|
| Environment category | Ground, Mobile (GM) | Vehicle installation |
| Ambient temperature (average) | 50C | Cabin near windshield |
| Temperature cycling (delta) | 60C | Daily range |
| Duty cycle | 40% | Average vehicle on-time |
| Quality factor (pi_Q) | 1.0 | AEC-Q100/Q200 components |

### 6.3 MTBF Allocation (by Subsystem)

| Subsystem | Component Count | Allocated MTBF | FIT Budget |
|-----------|-----------------|----------------|------------|
| Power supply | ~30 | >= 200,000 hrs | 5,000 |
| SoM + processor | ~1 (module) | >= 150,000 hrs | 6,667 |
| Camera deserializer | ~10 | >= 300,000 hrs | 3,333 |
| CAN transceiver | ~5 | >= 500,000 hrs | 2,000 |
| GNSS module | ~1 | >= 400,000 hrs | 2,500 |
| IMU (BMI088) | ~1 | >= 500,000 hrs | 2,000 |
| Watchdog/supervisor | ~5 | >= 1,000,000 hrs | 1,000 |
| Passive components | ~200 | >= 500,000 hrs | 2,000 |
| Connectors | ~5 | >= 300,000 hrs | 3,333 |
| PCB (board-level) | 1 | >= 1,000,000 hrs | 1,000 |
| **System Total** | ~260 | **>= 50,000 hrs** | **<= 20,000** |

Note: 1 FIT = 1 failure per 10^9 hours. MTBF = 10^9 / FIT_total.

## 7. Field Failure Rate Targets

| Period | Target (ppm/year) | Monitoring Method |
|--------|-------------------|--------------------|
| Warranty (0-3 years) | < 100 | Warranty claims database |
| Extended (3-10 years) | < 200 | Field return analysis |
| End of life (10-15 years) | < 500 (wearout onset) | Customer feedback |

## 8. Reliability Growth

### 8.1 Growth Model

Use Duane/AMSAA model to track reliability improvement across development phases:

| Phase | Sample | MTBF Target | Growth Rate |
|-------|--------|-------------|-------------|
| A-sample (prototype) | 10 units | >= 20,000 hrs | - |
| B-sample (pre-production) | 25 units | >= 35,000 hrs | 0.3 |
| C-sample (production intent) | 50 units | >= 50,000 hrs | 0.3 |
| SOP (start of production) | 100% screen | >= 50,000 hrs (demonstrated) | - |

### 8.2 Corrective Action Effectiveness

Track failure mode recurrence after corrective actions:
- First-time fix rate target: >= 80%
- Repeat failure tolerance: 0 (must root-cause all repeats)

## 9. Reporting

Reliability reports shall include:
- HALT summary (margins found, failures corrected)
- ALT Weibull plots and life predictions
- MTBF prediction report (comparison across methods)
- HASS effectiveness data (detection rates)
- Field failure tracking (once in production)
- Reliability growth chart

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2024-01-15 | Reliability Engineering Team | Initial draft |
