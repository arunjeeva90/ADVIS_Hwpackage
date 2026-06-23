# ADVIS Test Fixture Requirements

| Field | Value |
|-------|-------|
| Document ID | ADVIS-MFG-TF-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Test Engineering Team |
| Date | 2024-01-15 |
| Classification | CONFIDENTIAL |

---

## 1. Scope

This document defines the requirements for In-Circuit Test (ICT) and Functional Test fixtures for the ADVIS ECU production line. Fixtures are designed for high-volume manufacturing with targets for test time, coverage, and reliability.

## 2. Test Strategy Overview

```
  PCB Assembly --> [ICT] --> [Functional Test] --> [HASS Screen] --> [Final QC]
                     |              |
                     v              v
              Detect mfg      Verify system
              defects:        functionality:
              - Opens         - Power rails
              - Shorts        - Camera init
              - Wrong value   - CAN comms
              - Missing       - Sensor read
```

## 3. In-Circuit Test (ICT) Fixture

### 3.1 ICT Fixture Specifications

| Parameter | Requirement |
|-----------|-------------|
| Fixture type | Bed-of-nails (vacuum actuated) |
| Probe count | [TBD - estimate 200-400 probes] |
| Probe type | Spring-loaded, spear-tip (0.64mm standard) |
| Board interface | Bottom-side probing (primary), top-side probing (limited) |
| Actuation | Pneumatic vacuum (minimum 5 psi differential) |
| Alignment | Pin-guided with board tooling holes |
| Test platform | Keysight i3070 / Teradyne TestStation (or equivalent) |
| Cycle time target | < 30 seconds (including load/unload) |

### 3.2 Test Point Access Map

| Net Category | Required Access | Test Point Type | Min Pad Size |
|--------------|----------------|-----------------|--------------|
| Power rails (5V, 3.3V, 1.8V, GND) | Mandatory | Dedicated test via (bottom) | 1.0 mm |
| High-value passives (> 1k ohm) | Mandatory | Component pad access | 0.8 mm |
| IC power pins (VCC, GND) | Mandatory | Via or pad | 0.8 mm |
| Critical signal nets | Recommended | Test via | 0.8 mm |
| I2C bus (SDA, SCL) | Mandatory | Test pad | 1.0 mm |
| SPI bus (SCLK, MOSI, MISO, CS) | Mandatory | Test pad | 1.0 mm |
| CAN bus (CANH, CANL) | Mandatory | Connector pin | N/A (via connector) |
| Reset signals | Mandatory | Test via | 0.8 mm |
| JTAG/Debug (if accessible) | Recommended | Test header pad | 1.0 mm |

### 3.3 ICT Coverage Targets

| Test Type | Coverage Target | Method |
|-----------|----------------|--------|
| Short circuit detection | >= 99% of adjacent nets | Shorts measurement |
| Open circuit detection | >= 95% of solder joints | Opens measurement |
| Passive components (R, C, L) | >= 90% of BOM line items | In-circuit measurement |
| IC presence/orientation | >= 95% of ICs | Pin measurement / boundary scan |
| Voltage regulator basic function | All power ICs | Powered test (apply input, measure output) |
| Boundary scan (JTAG) | If available on SoM | IEEE 1149.1 |

### 3.4 ICT Pass/Fail Criteria

| Measurement | Tolerance | Fail Action |
|-------------|-----------|-------------|
| Resistors | +/- 5% (or per BOM tolerance) | Reject, repair |
| Capacitors | +/- 20% (or per BOM tolerance) | Reject, repair |
| Inductors | +/- 20% | Reject, repair |
| Diode forward voltage | +/- 100 mV of nominal | Reject |
| Short circuit resistance | > 10 kohm between non-connected nets | If < 10 kohm: flag |
| Open circuit | < 100 ohm for connected nets | If > 100 ohm: flag |
| Power rail (basic) | Within +/- 5% of nominal | Reject |

## 4. Functional Test Fixture

### 4.1 Functional Test Fixture Specifications

| Parameter | Requirement |
|-----------|-------------|
| Fixture type | Custom test jig with DUT interface |
| Power supply | Programmable 0-40V, 10A (simulate vehicle battery) |
| CAN interface | CAN-FD capable (500kbps/5Mbps) |
| Camera simulation | Test pattern generator or reference camera |
| GNSS simulation | Optional (or antenna with known position) |
| USB interface | USB 2.0 host for enumeration test |
| Measurement | DMM for voltages, oscilloscope for waveforms |
| Control interface | PC-based (LabVIEW, Python, or custom) |
| Cycle time target | < 120 seconds (full functional test) |

### 4.2 Functional Test Sequence

| Step | Test | Duration | Stimulus | Expected Response |
|------|------|----------|----------|-------------------|
| 1 | Apply power (13.5V) | 5s | 13.5V input | No smoke, current < limit |
| 2 | Power rail verification | 5s | Measure TP3, TP4, TP5 | 5V +/-2%, 3.3V +/-3%, 1.8V +/-3% |
| 3 | Power sequencing check | 5s | Monitor PG signals | Correct sequence |
| 4 | SoM boot | 30s | Wait for SOM_BOOT_OK | HIGH within 30s |
| 5 | Watchdog enable | 2s | Monitor WDI | Toggling after boot |
| 6 | CAN communication | 5s | Send/receive CAN frames | Correct decode, no errors |
| 7 | I2C bus scan | 3s | SoM scans I2C devices | DS90UB954, other ICs respond |
| 8 | Camera initialization | 10s | Connect test camera (or pattern) | Lock indicator, frame output |
| 9 | IMU readout | 3s | Read BMI088 registers | Chip ID correct, data valid |
| 10 | GNSS UART check | 5s | Monitor NMEA output | Valid NMEA sentences received |
| 11 | USB enumeration | 5s | Connect USB host | Device enumerates at HS |
| 12 | IR LED test | 5s | Enable IR, measure | Current within spec |
| 13 | Current consumption | 5s | Measure input current | Within expected range |
| 14 | Thermal check | 2s | Read temperature sensor | Reasonable value (15-35C) |
| 15 | Power down | 3s | Remove input power | Graceful shutdown |
| | **Total** | **~90s** | | |

### 4.3 Functional Test Pass/Fail Criteria

| Test | Pass Criteria | Fail Action |
|------|---------------|-------------|
| 5V rail | 4.90V - 5.10V | Reject |
| 3.3V rail | 3.201V - 3.399V | Reject |
| 1.8V rail | 1.746V - 1.854V | Reject |
| Boot time | < 30 seconds | Reject (investigate) |
| CAN TX/RX | Zero error frames in 100 messages | Reject |
| Camera lock | Lock within 5 seconds | Reject |
| IMU chip ID | ACC=0x1E, GYRO=0x0F | Reject |
| GNSS NMEA | Valid GGA sentence within 5s of UART active | Reject |
| USB enum | Device descriptor readable | Reject |
| IR LED current | Within +/- 15% of nominal | Reject |
| Input current (idle) | < [TBD] mA | Reject |
| Input current (active) | [TBD] - [TBD] mA | Reject if out of range |

## 5. Test Fixture Design Requirements

### 5.1 Mechanical Requirements

| Parameter | Specification |
|-----------|---------------|
| DUT retention | Vacuum hold-down or mechanical clamp |
| Connector mating | Auto-mate (pneumatic) for power, CAN |
| Camera interface | Pogo-pin or flex cable adapter |
| Operator interface | Single button start, pass/fail indicator (LED) |
| ESD protection | All operator-accessible surfaces grounded |
| Fixture lifetime | >= 100,000 insertions before maintenance |
| Probe replacement | Tool-free probe change (spring-loaded modules) |

### 5.2 Safety Requirements

| Requirement | Implementation |
|-------------|----------------|
| Operator safety | Guarded moving parts; interlock on access door |
| ESD | Ionized air + wrist strap monitor |
| Voltage (< 50V) | SELV classification, no touch hazard |
| Emergency stop | Red mushroom button, cuts power to DUT |
| Pinch points | None accessible during operation |

### 5.3 Calibration Requirements

| Item | Calibration Interval | Method |
|------|---------------------|--------|
| DMM (voltage measurement) | 12 months | Traceable to national standard |
| Current measurement | 12 months | Calibrated shunt |
| CAN interface timing | 12 months | Reference CAN node |
| Power supply (voltage, current) | 12 months | Traceable DMM |
| Oscilloscope (if used) | 12 months | Calibration signal source |

## 6. Test Programming Interface

### 6.1 DUT Programming Requirements

| Operation | Interface | Tool |
|-----------|-----------|------|
| SoM firmware flash | USB/UART (boot mode) | Custom flasher script |
| Calibration data write | CAN (UDS protocol) | CAN flasher |
| Serial number programming | CAN / I2C | Fixture software |
| MAC address programming | SoM-specific | Per SoM vendor process |
| Production configuration | CAN / UART | Fixture software |

### 6.2 Software Architecture

```
  +-------------------+
  | Test Executive     | (LabVIEW / Python / TestStand)
  | (Sequence Control) |
  +--------+----------+
           |
  +--------+----------+
  |  Instrument       | (VISA / SCPI / Socket)
  |  Drivers          |
  +---+------+------+-+
      |      |      |
  +---+--+ +-+----+ +----+--+
  | DMM  | | CAN  | | Power |
  |      | | I/F  | | Supply|
  +------+ +------+ +-------+
```

## 7. Data Collection and Reporting

### 7.1 Data Logged Per Unit

| Data | Format | Purpose |
|------|--------|---------|
| Serial number | String | Unit identification |
| Test date/time | ISO 8601 | Traceability |
| Operator ID | String | Accountability |
| Fixture ID | String | Fixture correlation |
| All measurements (numeric) | Float + unit | Trend analysis, SPC |
| Pass/fail per step | Boolean | Yield calculation |
| Overall result | Pass/Fail | Release decision |
| Test duration | Seconds | Throughput tracking |
| Failure codes (if fail) | Codified | Pareto analysis |

### 7.2 Data Retention

| Data Type | Retention Period | Storage |
|-----------|-----------------|---------|
| Individual unit records | 15 years (vehicle lifetime) | MES database + backup |
| SPC charts | 5 years | Quality system |
| Calibration records | 10 years | Quality system |
| Fixture maintenance logs | Fixture lifetime + 5 years | Maintenance system |

## 8. Fixture Maintenance

| Activity | Frequency | Performed By |
|----------|-----------|--------------|
| Probe continuity check | Daily (start of shift) | Operator |
| Probe replacement (worn) | Per probe cycle count or failure | Technician |
| Connector inspection | Weekly | Technician |
| Pneumatic system check | Monthly | Maintenance |
| Full calibration | Per calibration schedule | Metrology |
| Software/firmware update | As released (controlled) | Test Engineer |

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2024-01-15 | Test Engineering Team | Initial draft |
