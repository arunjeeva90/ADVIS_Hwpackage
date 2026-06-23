# ADVIS Automotive Standards Compliance

| Field | Value |
|-------|-------|
| Document ID | ADVIS-CS-STD-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Compliance & Safety Team |
| Date | 2024-01-15 |
| Classification | CONFIDENTIAL |

---

## 1. Scope

This document defines the automotive standards compliance approach for the ADVIS ECU. It covers functional safety classification, component qualification tracking, and environmental standards applicability. The ADVIS ECU is classified as a non-actuation observation and processing unit, which fundamentally shapes its safety classification.

## 2. Safety Boundary Definition

### 2.1 ADVIS Functional Scope

The ADVIS ECU performs the following functions:
- Forward-facing camera capture and processing (ADAS perception)
- Driver-facing camera capture and processing (DMS)
- Sensor fusion (camera + IMU + GNSS)
- Risk assessment and decision generation
- Communication of safety-supervised actuation REQUESTS to OEM controllers via CAN-FD

### 2.2 What ADVIS Does NOT Do

The ADVIS ECU does **NOT** directly actuate:
- Braking systems (ESC, AEB actuators)
- Steering systems (EPS motor)
- Throttle/powertrain control
- Restraint systems (airbags, seatbelts)
- Lighting control (headlamps, indicators)

### 2.3 Safety Architecture

```
  +-------------------+          CAN-FD           +-------------------+
  |    ADVIS ECU      |  --- Request Messages --> |  OEM Safety ECU   |
  | (Observation &    |                           | (ASIL-rated,      |
  |  Processing ONLY) |                           |  actuates vehicle) |
  +-------------------+                           +-------------------+
        |                                                  |
        | QM (no actuation)                                | ASIL-B/C/D
        |                                                  | (per function)
        v                                                  v
  Non-safety-critical                              Safety-critical
  output: requests,                                output: brake,
  warnings, logging                                steer, throttle
```

## 3. ISO 26262 Functional Safety

### 3.1 ASIL Classification

| Item | ADVIS Classification | Justification |
|------|---------------------|---------------|
| Overall ECU | **QM (Quality Management)** | Non-actuation; does not control safety-critical actuators |
| Forward camera subsystem | QM | Observation only; no direct vehicle control |
| DMS subsystem | QM | Monitoring only; alerts are advisory |
| CAN output messages | QM | Requests only; receiving ECU validates independently |
| Power supply | QM | Loss of power = loss of observation, not hazardous |
| Watchdog | QM | Ensures self-recovery; no safety-critical dependency |

### 3.2 ASIL Decomposition Rationale

The ADVIS ECU operates within a safety architecture where:

1. **The receiving OEM ECU is responsible for validating all actuation requests.** ADVIS requests are treated as advisory inputs by the OEM safety controller.

2. **Loss of ADVIS function results in loss of observation capability, not loss of vehicle control.** The vehicle remains safe without ADVIS (driver maintains responsibility).

3. **No single failure in ADVIS can lead to unintended vehicle actuation.** The communication protocol includes:
   - Message authentication (if OEM requires)
   - Timeout detection (receiver ignores stale messages)
   - Plausibility checks (receiver validates against own sensors)

4. **Per ISO 26262 Part 3, Clause 7:** The hazard analysis for ADVIS considers the worst-case failure effect as "loss of warning/advisory function," which maps to:
   - Severity: S1 (light injuries at most, since driver retains control)
   - Exposure: E4 (high probability of operating scenario)
   - Controllability: C1 (driver can maintain control without ADVIS)
   - ASIL result: **QM** (S1 + E4 + C1 = QM per Table 4)

### 3.3 ISO 26262 Compliance Activities (QM)

Even at QM classification, the following quality activities are performed:

| Activity | ISO 26262 Reference | ADVIS Implementation |
|----------|---------------------|----------------------|
| HARA (Hazard Analysis) | Part 3 | Documented, QM conclusion |
| Safety concept | Part 3, Clause 8 | Non-actuation boundary documented |
| Hardware design | Part 5 (informative for QM) | Follow best practices |
| FMEA | Part 5, Clause 7 (recommended) | Hardware FMEA performed |
| Testing | Part 5, Clause 10 | Full DVT per test plans |
| Safety manual | Part 8 (if element) | Interface constraints documented |

### 3.4 Interface Safety Requirements

Although ADVIS is QM, the OEM integration imposes interface requirements:

| Requirement | Implementation |
|-------------|----------------|
| Message alive counter | 4-bit rolling counter in CAN frame |
| Message CRC | CRC-8 over data payload |
| Timeout detection | OEM ECU ignores messages older than 200 ms |
| Plausibility range | Request values within physically possible range |
| Graceful degradation | ADVIS reports confidence level with each request |

## 4. AEC-Q100 Component Qualification

### 4.1 IC Qualification Requirements

All integrated circuits on the ADVIS ECU shall be AEC-Q100 qualified to the appropriate stress test grade:

| Grade | Temperature Range | Application |
|-------|-------------------|-------------|
| Grade 0 | -40C to +150C | Not required for ADVIS |
| **Grade 2** | **-40C to +105C** | **ADVIS target (cabin mount)** |
| Grade 3 | -40C to +85C | Minimum acceptable |

### 4.2 Critical IC Qualification Status

| Component | Part Number | AEC-Q100 Grade | Status |
|-----------|-------------|----------------|--------|
| Buck converter | LM61460-Q1 | Grade 1 (-40/+125C) | Qualified |
| Buck converter | TPS62130A-Q1 | Grade 1 | Qualified |
| LDO | TLV75518-Q1 | Grade 2 | Qualified |
| Supervisor | TPS3808G33-Q1 | Grade 1 | Qualified |
| Watchdog | TPS3431-Q1 | Grade 1 | Qualified |
| CAN transceiver | TCAN1044AV-Q1 | Grade 1 | Qualified |
| FPD-Link deser | DS90UB954-Q1 | Grade 2 | Qualified |
| GNSS module | NEO-M9N-00B | AEC-Q100 Grade 2 | Qualified |
| IMU | BMI088 | AEC-Q100 Grade 2 | Qualified |
| SoM (TDA4VM) | Phytec phyCORE | Grade 2 (SoC) | Qualified |
| PMOS (reverse prot.) | [TBD] | Grade 1 | [Verify] |

### 4.3 Qualification Tracking Process

1. **Design entry:** Verify AEC-Q100 qualification in component datasheet
2. **BOM review:** Flag any non-automotive-grade components
3. **Risk assessment:** Document justification for any exceptions
4. **Supplier confirmation:** Obtain qualification certificates from IC vendors
5. **Change notification:** Subscribe to PCN (Product Change Notifications)

## 5. AEC-Q200 Passive Component Qualification

### 5.1 Requirements

All passive components in critical paths shall be AEC-Q200 qualified:

| Component Type | Critical Application | AEC-Q200 Required |
|----------------|---------------------|-------------------|
| Ceramic capacitors (MLCC) | Power rail decoupling | Yes |
| Electrolytic capacitors | Bulk input filter | Yes |
| Inductors (power) | Buck converter | Yes |
| Resistors (precision) | Voltage dividers | Yes |
| Ferrite beads | EMC filtering | Yes |
| TVS diodes | Input protection | Yes |
| Fuse | Input overcurrent | Yes (AEC-Q200 or equivalent) |

### 5.2 Derating Policy

| Component | Operating Derating | Rationale |
|-----------|-------------------|-----------|
| MLCC (voltage) | <= 70% of rated voltage | Reliability derating |
| MLCC (temperature) | <= 80% of rated temp | Margin for hotspots |
| Resistors (power) | <= 60% of rated power | Thermal derating |
| Inductors (current) | <= 80% of I_sat | Prevent saturation |
| Electrolytic caps (voltage) | <= 80% of rated voltage | Lifetime extension |
| Electrolytic caps (temp) | Rated temp >= T_max + 20C | Lifetime margin |

## 6. ISO 16750 Environmental Compliance

### 6.1 Applicable Tests (Windshield Mount, Code 3A)

| Test | ISO 16750 Clause | Severity | ADVIS Applicability |
|------|------------------|----------|---------------------|
| Supply voltage (static) | Part 2, 4.2 | 6V - 16V | Full compliance |
| Supply voltage (dynamic) | Part 2, 4.3 | Load dump per OEM | Full compliance |
| Reverse polarity | Part 2, 4.7 | -16V, 60s | Full compliance |
| Superimposed AC | Part 2, 4.4 | OEM-specific | Full compliance |
| Slow voltage decrease | Part 2, 4.5 | Cranking profile | Full compliance |
| Temperature range | Part 4, 5.1 | -40C to +85C | Full compliance |
| Humidity (constant) | Part 4, 5.3 | 85C/85%RH, 240h | Full compliance |
| Humidity (cyclic) | Part 4, 5.4 | Per Figure 5 | Full compliance |
| Vibration (random) | Part 3, 4.1 | Body-mount profile | Full compliance |
| Mechanical shock | Part 3, 4.2 | 50G, 6ms | Full compliance |
| Free fall | Part 3, 4.3 | 1m (manufacturing handling) | Full compliance |

### 6.2 Extended OEM Requirements

OEMs may impose additional requirements beyond ISO 16750. Document and track these:

| OEM Requirement | Standard/Spec | ADVIS Compliance | Status |
|-----------------|---------------|-----------------|--------|
| [OEM-specific voltage] | [OEM spec number] | [TBD] | Pending |
| [OEM-specific EMC] | [OEM spec number] | [TBD] | Pending |
| [OEM-specific life] | [OEM spec number] | [TBD] | Pending |

## 7. Compliance Matrix Summary

| Standard | Applicability | Target Level | Status |
|----------|---------------|--------------|--------|
| ISO 26262 | Functional safety | QM | Classification complete |
| AEC-Q100 | IC qualification | Grade 2 | Component selection ongoing |
| AEC-Q200 | Passive qualification | Automotive grade | Component selection ongoing |
| ISO 16750 | Environmental | Code 3A (cabin) | Test plan defined |
| CISPR 25 | EMC emissions | Class 5 | Test plan defined |
| ISO 11452 | EMC immunity | Per clause | Test plan defined |
| ISO 10605 | ESD | +/-8kV contact | Test plan defined |
| ISO 7637-2 | Transients | Full pulse set | Test plan defined |
| IEC 62471 | IR eye safety | Exempt/RG1 target | Analysis pending |
| EU RoHS | Hazardous substances | Full compliance | BOM review pending |
| EU REACH | Chemical registration | SVHC compliant | Supplier data pending |

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2024-01-15 | Compliance & Safety Team | Initial draft |
