# ADVIS EMC Test Plan

| Field | Value |
|-------|-------|
| Document ID | ADVIS-VT-EMC-001 |
| Version | 0.1 |
| Status | Draft |
| Author | EMC & Compliance Team |
| Date | 2024-01-15 |
| Classification | CONFIDENTIAL |

---

## 1. Scope

This document defines the electromagnetic compatibility (EMC) test plan for the ADVIS ECU. The plan covers conducted emissions, radiated emissions, and immunity testing per CISPR 25 and ISO 11452 series standards. The target performance level is CISPR 25 Class 5 for all emission tests.

## 2. Applicable Standards

| Standard | Edition | Scope |
|----------|---------|-------|
| CISPR 25 (Ed. 4) | 2016 | Vehicle EMC - Emissions |
| ISO 11452-1 | 2015 | EMC Immunity - General |
| ISO 11452-2 | 2019 | Radiated immunity (absorber-lined chamber) |
| ISO 11452-4 | 2011 | Bulk current injection (BCI) |
| ISO 11452-8 | 2015 | Immunity to magnetic fields |
| ISO 10605 | 2008 / AMD1:2014 | ESD testing |
| ISO 7637-2 | 2011 | Electrical transients |
| OEM-specific | TBD | Customer EMC specifications |

## 3. Target Performance Level

| Test Category | Standard | Target Level |
|---------------|----------|--------------|
| Conducted emissions (voltage method) | CISPR 25, Class 5 | Most stringent |
| Conducted emissions (current method) | CISPR 25, Class 5 | Most stringent |
| Radiated emissions (ALSE) | CISPR 25, Class 5 | Most stringent |
| Radiated immunity | ISO 11452-2 | 100 V/m (30-1000 MHz) |
| Bulk current injection | ISO 11452-4 | 200 mA (1-400 MHz) |
| ESD (contact) | ISO 10605 | +/- 8 kV |
| ESD (air) | ISO 10605 | +/- 15 kV |

## 4. Equipment Required

| Equipment | Specification | Purpose |
|-----------|---------------|---------|
| EMI Receiver | CISPR 16-1-1 compliant, 9 kHz - 6 GHz | Emissions measurement |
| LISN (2x) | 50uH/50-ohm, CISPR 25 type | Conducted emissions |
| Anechoic Chamber | >= 3m semi-anechoic (ALSE) | Radiated emissions/immunity |
| Biconical Antenna | 30 MHz - 300 MHz | Low-frequency emissions |
| Log-Periodic Antenna | 300 MHz - 1 GHz | Mid-frequency emissions |
| Horn Antenna | 1 GHz - 6 GHz | High-frequency emissions |
| RF Signal Generator | 100 kHz - 3 GHz, 200W amp | Immunity source |
| BCI Clamp | 1 MHz - 400 MHz | Bulk current injection |
| ESD Gun | ISO 10605 compliant, +/- 25 kV | ESD testing |
| Current Probe | CISPR 25 type, 150 kHz - 200 MHz | Current method CE |
| Ground Plane | 2m x 1m minimum (copper) | Reference ground |
| 12V Battery Simulator | Automotive LISN integrated | Supply simulation |

## 5. Device Under Test (DUT) Configuration

### Operating Modes for EMC Testing

| Mode | Description | Active Subsystems |
|------|-------------|-------------------|
| Mode A | Full operation | All systems active, cameras streaming, CAN active |
| Mode B | Standby | Power on, SoM in low-power, CAN listen-only |
| Mode C | DMS active | IR LEDs on, DMS camera streaming, ADAS idle |
| Mode D | Full load | Maximum current draw, all interfaces active |

### Harness Configuration
- Power harness: 1700 mm +/- 50 mm (per CISPR 25)
- CAN bus harness: 2000 mm with 120-ohm termination
- Camera cables: Representative length (per vehicle installation)
- USB cable: 1000 mm (if connected during test)
- All harnesses routed 50 mm above ground plane

## 6. Conducted Emissions Tests

### 6.1 Voltage Method (CISPR 25, Clause 6.3)

**Frequency Range:** 150 kHz - 108 MHz

**Setup:**
```
  Battery    LISN    DUT Harness (1.7m)    DUT
  Simulator--[50uH]--========================--[ADVIS ECU]
                |                                    |
            [EMI Rx]                          [Ground Plane]
```

**Procedure:**
1. Install DUT on ground plane with 50 mm standoff
2. Route power harness per CISPR 25 Figure 3
3. Connect LISN to power supply line and return line
4. Set EMI receiver to peak detector, RBW per CISPR 16-1-1
5. Perform scan: 150 kHz - 108 MHz
6. Record peak and average/quasi-peak readings

**CISPR 25 Class 5 Limits (Voltage Method):**

| Frequency Range | Peak Limit (dBuV) | Quasi-Peak Limit (dBuV) | Average Limit (dBuV) |
|-----------------|--------------------|-----------------------|---------------------|
| 150 kHz - 300 kHz | 44 | 34 | 24 |
| 300 kHz - 530 kHz | 38 | 28 | 18 |
| 530 kHz - 1.8 MHz | 43 | 33 | 23 |
| 1.8 MHz - 5.9 MHz | 36 | 26 | 16 |
| 5.9 MHz - 6.2 MHz | 26 | 16 | 6 |
| 6.2 MHz - 30 MHz | 34 | 24 | 14 |
| 30 MHz - 54 MHz | 34 | 24 | 14 |
| 54 MHz - 108 MHz | 34 | 24 | 14 |

### 6.2 Current Probe Method (CISPR 25, Clause 6.4)

**Frequency Range:** 150 kHz - 200 MHz

**Setup:** Same as voltage method, with current probe clamped around harness at 50 mm from DUT connector.

**CISPR 25 Class 5 Limits (Current Method):**

| Frequency Range | Peak Limit (dBuA) | Quasi-Peak Limit (dBuA) | Average Limit (dBuA) |
|-----------------|--------------------|-----------------------|---------------------|
| 150 kHz - 1.8 MHz | 10 | 0 | -10 |
| 1.8 MHz - 30 MHz | 6 | -4 | -14 |
| 30 MHz - 108 MHz | 2 | -8 | -18 |
| 108 MHz - 200 MHz | 2 | -8 | -18 |

## 7. Radiated Emissions Tests

### 7.1 ALSE Method (CISPR 25, Clause 6.5)

**Frequency Range:** 150 kHz - 2.5 GHz

**Setup:**
- Antenna distance: 1 m from DUT harness
- Antenna positions: Per CISPR 25 Figure 6 (top, side)
- Antenna polarization: Vertical and horizontal
- DUT operating mode: Mode A (full operation) and Mode C (IR LEDs active)

**CISPR 25 Class 5 Limits (Radiated, 1m):**

| Frequency Range | Peak Limit (dBuV/m) | Quasi-Peak Limit (dBuV/m) | Average Limit (dBuV/m) |
|-----------------|----------------------|--------------------------|------------------------|
| 150 kHz - 1.8 MHz | 32 | 22 | 12 |
| 1.8 MHz - 30 MHz | 22 | 12 | 2 |
| 30 MHz - 54 MHz | 32 | 22 | 12 |
| 54 MHz - 108 MHz | 28 | 18 | 8 |
| 108 MHz - 500 MHz | 24 | 14 | 4 |
| 500 MHz - 960 MHz | 30 | 20 | 10 |
| 960 MHz - 2500 MHz | 36 | 26 | 16 |

## 8. Immunity Tests

### 8.1 Radiated Immunity (ISO 11452-2)

**Frequency Range:** 30 MHz - 2000 MHz

**Test Levels:**

| Frequency Range | Field Strength | Modulation |
|-----------------|----------------|------------|
| 30 MHz - 1000 MHz | 100 V/m | AM, 80%, 1 kHz |
| 1000 MHz - 2000 MHz | 60 V/m | AM, 80%, 1 kHz |

**Performance Criteria:**
- Level A: Normal operation during and after exposure
- Acceptable: No loss of CAN communication, camera streaming, or GNSS lock
- Pass condition: All functions maintain Level A performance

### 8.2 Bulk Current Injection (ISO 11452-4)

**Frequency Range:** 1 MHz - 400 MHz

**Test Levels:**

| Frequency Range | Injected Current | Modulation |
|-----------------|-----------------|------------|
| 1 MHz - 400 MHz | 200 mA | AM, 80%, 1 kHz |

**Harnesses Tested:**
- Power supply harness
- CAN bus harness
- Camera FPD-Link cables (each)

**Performance Criteria:** Level A (normal operation)

### 8.3 ESD Testing (ISO 10605)

**Test Levels:**

| Discharge Method | Voltage | Polarity | Discharges |
|-----------------|---------|----------|------------|
| Contact (direct) | +/- 4 kV | Both | 3 per point |
| Contact (indirect) | +/- 8 kV | Both | 3 per point |
| Air (direct) | +/- 8 kV | Both | 3 per point |
| Air (indirect) | +/- 15 kV | Both | 3 per point |

**Discharge Points:**
- USB-C connector shell
- CAN connector pins
- Camera connector shell
- Mounting hardware
- Exposed enclosure surfaces
- Connector seams

**Performance Criteria:**
- Level A for indirect discharge
- Level B for direct discharge (temporary loss acceptable, self-recovery required)
- No permanent damage at any test level

## 9. Pre-Compliance Test Procedures

### 9.1 Desktop Pre-Scan

Before formal lab testing, perform the following pre-compliance checks:

1. **Near-field probe scan:** Use H-field and E-field near-field probes to identify emission sources on PCB
2. **LISN pre-scan:** Quick conducted emissions scan at engineering lab
3. **Current probe survey:** Identify common-mode currents on cables
4. **Switching frequency harmonics:** Verify LM61460 (2.1 MHz) and TPS62130A (2.5 MHz) harmonics meet limits with adequate margin

### 9.2 Pre-Compliance Pass Criteria

| Parameter | Pre-Compliance Target | Margin to Class 5 |
|-----------|----------------------|-------------------|
| Conducted emissions | 6 dB below Class 5 limit | >= 6 dB |
| Radiated emissions | 6 dB below Class 5 limit | >= 6 dB |
| ESD survival | Full compliance | No margin reduction |

## 10. EMC Design Features (Verification Points)

The following design features shall be verified during EMC testing:

| Feature | Verification Method |
|---------|-------------------|
| Input filter (LC) | Conducted emissions at switching frequency |
| TVS clamping | ESD recovery, no latch-up |
| Shield continuity (if enclosed) | Radiated emissions comparison (with/without) |
| Ground plane integrity | Near-field probe scan |
| Ferrite beads (camera cables) | CM current reduction on FPD-Link |
| Spread-spectrum clocking | Narrowband emission reduction (if enabled) |

## 11. Reporting

EMC test reports shall include:
- Test configuration photographs
- Ambient (noise floor) measurements
- Full frequency scan plots with limit lines overlaid
- Margin table (dB below limit at each frequency band)
- Any non-compliance and corrective actions taken
- Pre/post-fix comparison data

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2024-01-15 | EMC & Compliance Team | Initial draft |
