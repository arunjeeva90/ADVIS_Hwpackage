# ADVIS Design Verification Plan and Report (DVP&R) v0.1

**Classification:** Confidential - Engineering Use Only  
**Version:** 0.1  
**Date:** July 2026  
**Applies to:** ADVIS v0.5 Compact Module and v0.4.4 A-sample (where noted)

---

## 1. Purpose

This document is the initial DVP&R for the ADVIS hardware platform. It defines the validation tests required to verify that the hardware design meets its requirements. Each row specifies the test, method, acceptance criteria, and applicable standard.

---

## 2. Status Legend

| Status | Meaning |
|--------|---------|
| Not Started | Test not yet executed |
| In Progress | Test underway |
| Pass | Met acceptance criteria |
| Fail | Did not meet criteria (requires corrective action) |
| Waived | Accepted deviation with documented rationale |
| N/A | Not applicable to this variant |

---

## 3. Validation Test Matrix

| Test ID | Requirement | Method | Sample Size | Acceptance Criteria | Standard/Reference | Status | Notes |
|---------|-------------|--------|-------------|--------------------|--------------------|--------|-------|
| DVT-001 | 12V input operating range | Bench power supply sweep, 9V to 16V continuous | 5 units | All rails within spec across full input range; no resets, no oscillation | ISO 16750-2 | Not Started | Verify at -40C, +25C, +85C |
| DVT-002 | Load dump survival | ISO 7637-2 Pulse 5b applied to VIN | 3 units | No permanent damage; system recovers after event | ISO 7637-2 | Not Started | TVS clamping verification |
| DVT-003 | Reverse polarity | -16V applied to VIN for 60 seconds | 3 units | No current flow; no damage; system operates normally after correct polarity restored | ISO 16750-2 | Not Started | PMOS protection verification |
| DVT-004 | Cold crank | Input voltage dip to 3.5V for 15ms per cranking profile | 3 units | System recovers without manual intervention after voltage returns to normal | ISO 16750-2 | Not Started | Verify supervisor holds reset during cranking |
| DVT-005 | 5V rail accuracy | Load sweep 0-6A, measure 5V_SYS | 5 units | 5.0V +/- 3% (4.85V to 5.15V) across load and temperature | Internal | Not Started | LM61460-Q1 output |
| DVT-006 | 3V3 rail accuracy | Load sweep 0-3A, measure 3V3_IO | 5 units | 3.3V +/- 2% (3.234V to 3.366V) across load and temperature | Internal | Not Started | TPS62130A-Q1 output |
| DVT-007 | 1V8 rail accuracy | Load sweep 0-500mA, measure 1V8_AUX | 5 units | 1.8V +/- 2% (1.764V to 1.836V) across load and temperature | Internal | Not Started | TLV75518-Q1 output |
| DVT-008 | Watchdog boot behavior | Power-on without firmware kicking WDI | 3 units | Watchdog remains disabled until SOM_BOOT_OK asserted; no spurious resets during boot | Internal | Not Started | TPS3431-Q1 enable gating |
| DVT-009 | Watchdog runtime timeout | Stop WDI toggle during normal operation | 3 units | System reset asserted within specified timeout window (1.0s to 2.2s typical) | Internal | Not Started | Timeout set by CT pin capacitor |
| DVT-010 | CAN-FD physical layer | CAN bus connected to reference node; bit rate sweep | 5 units | Dominant/recessive levels within CAN-FD spec; no bit errors at 5 Mbps | ISO 11898-2 | Not Started | TCAN1044AV-Q1 characterization |
| DVT-011 | CAN message timing | Transmit and receive CAN-FD frames at max rate | 3 units | Zero frame loss over 1M frames; latency within spec | ISO 11898-1 | Not Started | Verify with automotive CAN analyzer |
| DVT-012 | Direct-MIPI camera link (v0.5) | Connect sensor evaluation board; capture frames | 3 units | Error-free frame capture at target resolution and frame rate; no CRC errors | MIPI CSI-2 spec | Not Started | Applies to v0.5 only; verify both cameras |
| DVT-013 | Forward camera image quality | Capture test chart images; analyze MTF, SNR, dynamic range | 3 units | MTF > 0.3 at Nyquist; SNR > 36 dB at 1 lux; HDR > 120 dB | Internal / sensor datasheet | Not Started | Test with selected forward sensor |
| DVT-014 | DMS camera image quality | Capture face images under NIR illumination; analyze SNR and uniformity | 3 units | Face detectable at 1m distance; SNR > 30 dB under 940nm illumination; uniform illumination +/- 20% | Internal / sensor datasheet | Not Started | Test with selected DMS sensor + IR LEDs |
| DVT-015 | DMS NIR illumination | Measure 940nm LED output power and uniformity at driver position | 3 units | Sufficient illumination for face detection across driver position range; uniform within +/- 20% | Internal | Not Started | Measure with NIR power meter |
| DVT-016 | IR eye-safety pre-check | Measure irradiance at accessible distance per IEC 62471 | 3 units | Below exempt or risk group 1 limit for prolonged exposure | IEC 62471 | Not Started | Must pass before any human subject testing |
| DVT-017 | Optical baffle / IR leakage | Activate DMS IR LEDs; measure NIR signal at forward camera sensor | 3 units | IR leakage into forward camera below detectable threshold (< 1 LSB contribution) | Internal | Not Started | Verify baffle effectiveness |
| DVT-018 | Windshield solar thermal test | Mount module on windshield; expose to 1000 W/m2 solar lamp | 3 units | SoC junction temp below max rated; no thermal shutdown during 8h exposure | Custom (solar simulation) | Not Started | Simulates worst-case summer sun |
| DVT-019 | Vibration | Random and sinusoidal per ISO 16750-3 passenger car profile | 5 units | No mechanical failure; no intermittent connections; functional after test | ISO 16750-3 | Not Started | Mount per intended vehicle location |
| DVT-020 | Humidity | 85C / 85% RH for 1000 hours | 3 units | No corrosion; no parameter drift beyond spec; functional after test | ISO 16750-4 | Not Started | Conformal coating effectiveness |
| DVT-021 | EMC pre-scan | Radiated emissions scan 30 MHz to 6 GHz | 3 units | Below CISPR 25 Class 5 limits with margin | CISPR 25 | Not Started | Identify problem frequencies before full compliance |
| DVT-022 | ESD | IEC 61000-4-2 contact and air discharge to all accessible pins/surfaces | 3 units | Level 4 (8kV contact, 15kV air); no damage, no reset | IEC 61000-4-2 | Not Started | Test all connector pins and housing surfaces |
| DVT-023 | Calibration drift detection | Mount on vibration fixture; run calibration check after each session | 3 units | System detects misalignment > 0.5 deg and flags error | Internal | Not Started | Software-assisted detection via image analysis |
| DVT-024 | Camera blocked detection (forward) | Cover forward camera during operation | 3 units | System detects blocked condition within 1 second; reports via CAN | Internal | Not Started | Test with opaque and translucent covers |
| DVT-025 | DMS blocked detection | Cover DMS camera during operation | 3 units | System detects blocked condition within 1 second; reports via CAN | Internal | Not Started | Test with opaque and translucent covers |
| DVT-026 | Factory EOL calibration | Run production calibration sequence via test fixture | 10 units | Calibration completes within target cycle time (< 60s); parameters stored in NVM | Internal | Not Started | Validate fixture interface and calibration algorithm |
| DVT-027 | Production test pads | Verify all test pads accessible with pogo-pin fixture | 5 units | All designated test points make reliable contact; pass electrical continuity | Internal | Not Started | Fixture design must accommodate housing service cover |

---

## 4. Test Equipment Requirements

| Equipment | Purpose | Applicable Tests |
|-----------|---------|-----------------|
| Programmable DC power supply (0-40V, 10A) | Input voltage sweep, load dump simulation | DVT-001 through DVT-004 |
| Electronic load (0-10A per channel) | Rail load testing | DVT-005 through DVT-007 |
| Oscilloscope (1 GHz+, 4 channel) | Waveform capture, timing measurement | DVT-008, DVT-009, DVT-012 |
| CAN-FD analyzer/interface | Bus traffic generation and monitoring | DVT-010, DVT-011 |
| Image quality test bench (test chart, controlled lighting) | Camera characterization | DVT-013, DVT-014 |
| NIR power meter and radiometer | IR output and eye safety measurement | DVT-015, DVT-016 |
| Solar simulation lamp (1000 W/m2) | Thermal qualification | DVT-018 |
| Vibration table (3-axis) | Mechanical qualification | DVT-019 |
| Environmental chamber (-40 to +125C, humidity) | Temperature and humidity testing | DVT-001, DVT-020 |
| EMC pre-compliance scanner | Radiated emissions | DVT-021 |
| ESD simulator (contact + air) | ESD immunity | DVT-022 |
| Production test fixture (pogo-pin) | Manufacturing test validation | DVT-026, DVT-027 |

---

## 5. Test Sequence and Dependencies

```
Phase 1 - Bench/Electrical (can start at PCB power-on):
  DVT-001 -> DVT-002 -> DVT-003 -> DVT-004
  DVT-005, DVT-006, DVT-007 (parallel)
  DVT-008, DVT-009
  DVT-010, DVT-011

Phase 2 - Camera/Optical (requires sensor integration):
  DVT-012 -> DVT-013 -> DVT-014
  DVT-015 -> DVT-016
  DVT-017

Phase 3 - Environmental/Mechanical (requires fully assembled units):
  DVT-018
  DVT-019
  DVT-020
  DVT-021, DVT-022

Phase 4 - System/Production (requires firmware maturity):
  DVT-023, DVT-024, DVT-025
  DVT-026, DVT-027
```

---

## 6. Applicable Standards

| Standard | Title | Applicable Tests |
|----------|-------|-----------------|
| ISO 16750-2 | Electrical loads | DVT-001, DVT-003, DVT-004 |
| ISO 16750-3 | Mechanical loads | DVT-019 |
| ISO 16750-4 | Climatic loads | DVT-018, DVT-020 |
| ISO 7637-2 | Electrical transients | DVT-002 |
| ISO 11898-1/2 | CAN physical layer | DVT-010, DVT-011 |
| IEC 61000-4-2 | ESD immunity | DVT-022 |
| IEC 62471 | Photobiological safety | DVT-016 |
| CISPR 25 | Vehicle EMC | DVT-021 |
| MIPI CSI-2 | Camera serial interface | DVT-012 |

---

*End of Document*
