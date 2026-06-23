# ADVIS Design Verification Test (DVT) Report Template

| Field | Value |
|-------|-------|
| Document ID | ADVIS-VT-DVT-[NNN] |
| Version | [X.Y] |
| Status | [Draft / Released] |
| Author | [Name] |
| Date | [YYYY-MM-DD] |
| Classification | CONFIDENTIAL |

---

## 1. Test Item Identification

| Parameter | Value |
|-----------|-------|
| Product name | ADVIS ECU |
| Hardware revision | [Rev X.Y] |
| PCB part number | [ADVIS-PCB-XXXX] |
| BOM revision | [BOM Rev X] |
| Firmware version | [vX.Y.Z] |
| Serial numbers tested | [List] |
| Build lot / date code | [Lot ID] |
| Number of samples | [N] |

## 2. Test Configuration

### 2.1 Test Setup Description

[Provide detailed description of test setup, including block diagram]

```
  [Power Supply] --> [DUT: ADVIS ECU] --> [CAN Bus Simulator]
                          |
                     [Camera Modules]
                          |
                     [Measurement Equipment]
```

### 2.2 Equipment List

| Equipment | Model | Serial # | Calibration Date | Cal Due |
|-----------|-------|----------|-----------------|---------|
| | | | | |
| | | | | |
| | | | | |

### 2.3 Environmental Conditions

| Parameter | Value |
|-----------|-------|
| Ambient temperature | [C] |
| Relative humidity | [%] |
| Barometric pressure | [hPa] |
| Test date(s) | [Start - End] |

### 2.4 Software/Configuration

| Item | Version/Setting |
|------|-----------------|
| SoM firmware | [version] |
| Camera firmware | [version] |
| Test script version | [version] |
| CAN database | [version] |

## 3. Test Results Summary

### 3.1 Overall Result

| Category | Total Tests | Pass | Fail | N/A | Pass Rate |
|----------|------------|------|------|-----|-----------|
| Power Integrity | | | | | |
| Signal Integrity | | | | | |
| EMC/EMI | | | | | |
| Environmental | | | | | |
| Functional | | | | | |
| Reliability | | | | | |
| **TOTAL** | | | | | |

### 3.2 Executive Summary

[One-paragraph summary of DVT results, key findings, and overall verdict]

## 4. Detailed Test Results

### 4.1 Power Integrity Results

| Test | Specification | Measured | Unit | Result |
|------|---------------|----------|------|--------|
| 5V_SYS accuracy | 5.0V +/- 2% | | V | |
| 5V_SYS ripple | < 50 mV pk-pk | | mV | |
| 3V3_IO accuracy | 3.3V +/- 3% | | V | |
| 3V3_IO ripple | < 30 mV pk-pk | | mV | |
| 1V8_CORE accuracy | 1.8V +/- 3% | | V | |
| 1V8_CORE ripple | < 20 mV pk-pk | | mV | |
| Load regulation (5V) | < 1.0% | | % | |
| Line regulation (5V) | < 0.5% | | % | |
| Power sequencing | Correct order | | - | |
| OCP trip (5V) | 7.0-9.0A | | A | |
| Transient recovery (5V) | < 50 us | | us | |
| Input range | 6V - 36V | | V | |
| Reverse polarity | No damage at -16V | | - | |

### 4.2 Signal Integrity Results

| Test | Specification | Measured | Unit | Result |
|------|---------------|----------|------|--------|
| CSI-2 eye height | >= 140 mV | | mV | |
| CSI-2 eye width | >= 0.35 UI | | UI | |
| FPD-Link BER | < 10^-12 | | - | |
| CAN V_diff (dominant) | 1.5 - 3.0V | | V | |
| CAN rise/fall time | < 40 ns | | ns | |
| USB eye height | >= 250 mV | | mV | |
| SPI error rate | 0 errors | | - | |

### 4.3 Functional Test Results

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| Power-on sequence | Correct order, < 50ms total | | |
| Forward camera lock | < 500 ms | | |
| DMS camera lock | < 500 ms | | |
| CAN heartbeat | 100 ms periodic | | |
| GNSS TTFF (cold) | < 30 s | | |
| IMU chip ID | ACC:0x1E, GYRO:0x0F | | |
| Watchdog timeout | Reset within 1.6s | | |
| USB enumeration | HS (480 Mbps) | | |
| IR LED control | Linear PWM response | | |

## 5. Pass/Fail Matrix

### 5.1 By Sample

| Test | Unit 1 | Unit 2 | Unit 3 | Unit 4 | Unit 5 |
|------|--------|--------|--------|--------|--------|
| Power integrity | | | | | |
| Signal integrity | | | | | |
| Functional | | | | | |
| Environmental | | | | | |
| EMC | | | | | |

### 5.2 By Temperature

| Test | -40C | 0C | 25C | 55C | 85C |
|------|------|-----|------|------|------|
| Power integrity | | | | | |
| Signal integrity | | | | | |
| Functional | | | | | |

## 6. Deviations and Non-Conformances

### 6.1 Deviation List

| ID | Test | Specification | Measured | Severity | Disposition |
|----|------|---------------|----------|----------|-------------|
| DEV-001 | | | | | |
| DEV-002 | | | | | |
| DEV-003 | | | | | |

### 6.2 Deviation Disposition Codes

| Code | Meaning |
|------|---------|
| ACCEPT | Use-as-is, within acceptable risk |
| REWORK | Correctable by rework/modification |
| REDESIGN | Requires PCB/schematic revision |
| RETEST | Additional testing required |
| WAIVE | Customer-approved waiver |

## 7. Corrective Actions

| ID | Related Deviation | Root Cause | Corrective Action | Owner | Target Date | Status |
|----|-------------------|------------|-------------------|-------|-------------|--------|
| CA-001 | | | | | | |
| CA-002 | | | | | | |

## 8. Test Evidence

### 8.1 Attached Files

| File Name | Description | Format |
|-----------|-------------|--------|
| [filename] | [description] | [PDF/PNG/CSV] |
| | | |

### 8.2 Oscilloscope Captures

[Reference to oscilloscope screenshot archive]

### 8.3 Measurement Data Files

[Reference to raw measurement data archive]

## 9. Conclusions and Recommendations

### 9.1 Overall Verdict

- [ ] **PASS** - All tests meet specification. Proceed to next phase.
- [ ] **CONDITIONAL PASS** - Minor deviations, acceptable with documented waivers.
- [ ] **FAIL** - Critical non-conformances require corrective action before release.

### 9.2 Recommendations

[List recommendations for next build, design improvements, or additional testing]

## 10. Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Test Engineer | | | |
| Hardware Lead | | | |
| Quality Engineer | | | |
| Program Manager | | | |

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| [X.Y] | [Date] | [Name] | [Description] |
