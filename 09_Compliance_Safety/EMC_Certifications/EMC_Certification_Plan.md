# ADVIS EMC Certification Plan

| Field | Value |
|-------|-------|
| Document ID | ADVIS-CS-EMC-001 |
| Version | 0.1 |
| Status | Draft |
| Author | EMC & Compliance Team |
| Date | 2024-01-15 |
| Classification | CONFIDENTIAL |

---

## 1. Scope

This document defines the EMC certification roadmap for the ADVIS ECU, from pre-compliance testing through formal certification. The target performance level is CISPR 25 Class 5 for all emission tests and full compliance with ISO 11452 immunity requirements.

## 2. Certification Objectives

| Objective | Standard | Target Level |
|-----------|----------|--------------|
| Conducted emissions (voltage) | CISPR 25 | Class 5 |
| Conducted emissions (current) | CISPR 25 | Class 5 |
| Radiated emissions | CISPR 25 | Class 5 |
| Radiated immunity | ISO 11452-2 | 100 V/m (30-1000 MHz) |
| Bulk current injection | ISO 11452-4 | 200 mA |
| ESD | ISO 10605 | +/- 8 kV contact, +/- 15 kV air |
| Transient immunity | ISO 7637-2 | All pulse types |

## 3. Pre-Compliance Testing Strategy

### 3.1 Internal Pre-Compliance Lab Requirements

| Equipment | Purpose | Minimum Specification |
|-----------|---------|----------------------|
| EMI receiver (or spectrum analyzer) | Emissions measurement | 9 kHz - 3 GHz, CISPR detectors |
| Near-field probe set | Source identification | H-field: 5-30 mm, E-field |
| LISN (pair) | Conducted emissions | 50uH/50-ohm, CISPR 25 |
| Shielded enclosure or absorber tiles | Ambient noise reduction | > 40 dB isolation at 100 MHz |
| ESD simulator | ESD pre-test | +/- 15 kV, ISO 10605 waveform |
| Current injection probe | BCI pre-test | 1-400 MHz |

### 3.2 Pre-Compliance Test Schedule

| Phase | Activity | Timing (vs. DVT) | Decision Gate |
|-------|----------|-------------------|---------------|
| PC-1 | Near-field scan (bare board) | DVT - 8 weeks | Identify hot spots |
| PC-2 | Conducted emissions (LISN scan) | DVT - 6 weeks | Verify filter effectiveness |
| PC-3 | Radiated pre-scan (open area or shielded room) | DVT - 4 weeks | Estimate margin to limits |
| PC-4 | ESD pre-test | DVT - 4 weeks | Verify protection circuits |
| PC-5 | Design fixes (if needed) | DVT - 3 weeks | Implement countermeasures |
| PC-6 | Re-test after fixes | DVT - 2 weeks | Confirm compliance |

### 3.3 Pre-Compliance Pass Criteria

| Test | Target | Margin Requirement |
|------|--------|--------------------|
| Conducted emissions | Class 5 limits | >= 6 dB margin |
| Radiated emissions | Class 5 limits | >= 6 dB margin |
| ESD | Full pass at rated level | No degradation |
| BCI | Full pass at rated level | No loss of function |

## 4. Formal Certification Lab Selection

### 4.1 Lab Requirements

| Criterion | Requirement |
|-----------|-------------|
| Accreditation | ISO/IEC 17025 |
| Automotive EMC scope | CISPR 25, ISO 11452, ISO 10605, ISO 7637 |
| Chamber type | ALSE (Absorber-Lined Shielded Enclosure) or SAC |
| Equipment calibration | Current (within 12 months) |
| Automotive experience | Demonstrated Tier-1 / OEM test history |
| Location preference | Within shipping distance for DUT support |
| Report acceptance | Recognized by target OEM(s) |

### 4.2 Candidate Labs (Examples)

| Lab | Location | Accreditation | Specialization |
|-----|----------|---------------|----------------|
| [Lab A] | [Location] | ISO 17025 | Automotive EMC |
| [Lab B] | [Location] | ISO 17025 | Component + system |
| [Lab C] | [Location] | ISO 17025 | Full vehicle + component |

*Note: Final lab selection based on OEM acceptance, schedule availability, and cost.*

## 5. Test Standard Matrix

### 5.1 Emissions Tests

| Test | Standard | Clause | Frequency | DUT Mode |
|------|----------|--------|-----------|----------|
| CE - Voltage method | CISPR 25 | 6.3 | 150 kHz - 108 MHz | Mode A, C, D |
| CE - Current method | CISPR 25 | 6.4 | 150 kHz - 200 MHz | Mode A, C, D |
| RE - ALSE | CISPR 25 | 6.5 | 150 kHz - 2.5 GHz | Mode A, C, D |
| RE - TEM cell (optional) | CISPR 25 | 6.6 | 150 kHz - 200 MHz | Mode A |

### 5.2 Immunity Tests

| Test | Standard | Clause | Range | Level |
|------|----------|--------|-------|-------|
| Radiated immunity | ISO 11452-2 | 6 | 30 - 2000 MHz | 100 V/m |
| BCI | ISO 11452-4 | 6 | 1 - 400 MHz | 200 mA |
| Stripline (optional) | ISO 11452-5 | 6 | 10 kHz - 400 MHz | Per OEM |
| ESD (contact direct) | ISO 10605 | 7 | - | +/- 4 kV |
| ESD (contact indirect) | ISO 10605 | 7 | - | +/- 8 kV |
| ESD (air direct) | ISO 10605 | 7 | - | +/- 8 kV |
| ESD (air indirect) | ISO 10605 | 7 | - | +/- 15 kV |
| Transient pulse 1 | ISO 7637-2 | 4.2 | - | Per Table 1 |
| Transient pulse 2a/2b | ISO 7637-2 | 4.3 | - | Per Table 2 |
| Transient pulse 3a/3b | ISO 7637-2 | 4.4 | - | Per Table 3 |
| Transient pulse 4 | ISO 7637-2 | 4.5 | - | Per Table 4 |
| Transient pulse 5a/5b | ISO 7637-2 | 4.6 | - | Per Table 5 |

### 5.3 Performance Criteria During Immunity

| Level | Definition | ADVIS Requirement |
|-------|------------|-------------------|
| A | Normal performance during and after | Required for RI, BCI |
| B | Temporary degradation, self-recovery | Acceptable for ESD (direct) |
| C | Temporary degradation, operator reset | Not acceptable |
| D | Permanent damage | Not acceptable |

## 6. DUT Operating Modes for Certification

| Mode ID | Description | Current Draw | Active Interfaces |
|---------|-------------|--------------|-------------------|
| Mode A | Full operation | Maximum | All cameras, CAN, GNSS, IMU, IR |
| Mode B | Low-power standby | Minimum | CAN listen-only |
| Mode C | DMS + IR active | High | DMS camera, IR LEDs, CAN |
| Mode D | Stress mode | Maximum possible | All at max throughput |

All emission tests performed in Mode A (highest emission) and Mode C (IR LEDs active).
Immunity tests performed in Mode A (most susceptible functions active).

## 7. Certification Timeline

| Milestone | Target Date (relative) | Dependencies |
|-----------|----------------------|--------------|
| Pre-compliance equipment ready | T - 12 weeks | Lab setup |
| A-sample PCBs available | T - 10 weeks | PCB fabrication |
| Pre-compliance round 1 (PC-1,2) | T - 8 weeks | A-samples |
| Design fixes (if needed) | T - 6 weeks | PC results |
| Pre-compliance round 2 (PC-3,4,5,6) | T - 4 weeks | Fixed samples |
| Formal lab booking confirmed | T - 4 weeks | Lab availability |
| DVT samples shipped to lab | T - 2 weeks | DVT build complete |
| Formal testing begins | T (test week) | All ready |
| Formal testing complete | T + 2 weeks | 2-week test window |
| Draft report received | T + 4 weeks | Lab turnaround |
| Final report / certificate | T + 6 weeks | Review and sign-off |

*T = formal certification test start date, aligned with DVT schedule.*

## 8. Risk Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Switching converter harmonics exceed limits | Medium | High | Spread-spectrum clocking, input filter optimization |
| FPD-Link cable radiation | Medium | Medium | Shielded cables, ferrite beads |
| IR LED PWM emissions | Low | Medium | Slew rate control, LC filtering |
| ESD failure on USB-C | Medium | Medium | TVS selection, layout optimization |
| CAN transient failure | Low | High | TCAN1044AV-Q1 has built-in protection |
| GNSS desense from self-emission | Medium | Medium | Frequency planning, shielding |

## 9. Documentation Deliverables

| Document | Owner | Timing |
|----------|-------|--------|
| Pre-compliance test report (internal) | EMC Engineer | Before formal test |
| EMC test plan (for lab) | EMC Engineer | With DUT shipment |
| Formal EMC test report | Certification lab | Post-test |
| EMC compliance certificate | Certification lab | Post-report |
| OEM compliance declaration | Quality Manager | For customer submission |

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2024-01-15 | EMC & Compliance Team | Initial draft |
