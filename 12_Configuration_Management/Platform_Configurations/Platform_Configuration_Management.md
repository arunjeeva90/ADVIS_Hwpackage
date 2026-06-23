# ADVIS Platform Configuration Management

## 1. Overview

This document defines how hardware configurations map to firmware profiles, how the configuration database is structured, and how variant validation is managed across the ADVIS product family.

## 2. Hardware-to-Firmware Mapping

### 2.1 Configuration Detection

The firmware detects the hardware variant at boot time through a combination of:

| Method | What It Detects | Example |
|--------|----------------|---------|
| SOM identification | SoC type (AM62A / AM68A / TDA4VH) | Device tree selection |
| I2C bus scan | Populated peripherals | GNSS present (0x42 responds) |
| GPIO strap reading | Board variant ID | 2-bit variant code |
| EEPROM content | Board serial, revision, configuration | Manufacturing data |

### 2.2 Configuration Profiles

| Profile ID | Hardware Variant | Firmware Features Enabled |
|------------|-----------------|--------------------------|
| CFG-ENTRY-DMS | ADVIS-E, AM62A, DMS only | DMS inference, CAN logging, USB diagnostics |
| CFG-MID-ADAS | ADVIS-M, AM68A, dual camera | Full ADAS+DMS, GNSS+IMU fusion, CAN advisory |
| CFG-MID-FLEET | ADVIS-M, AM68A, fleet config | DMS + driver behavior, event logging, fleet reporting |
| CFG-HIGH-FUSION | ADVIS-H, TDA4VH, multi-sensor | Surround perception, sensor fusion, multi-CAN |

### 2.3 Feature Enable Matrix

| Feature | CFG-ENTRY-DMS | CFG-MID-ADAS | CFG-MID-FLEET | CFG-HIGH-FUSION |
|---------|---------------|--------------|---------------|-----------------|
| DMS inference | Enabled | Enabled | Enabled | Enabled |
| Forward camera ADAS | Disabled | Enabled | Disabled | Enabled |
| FCW/LDW/TSR | Disabled | Enabled | Disabled | Enabled |
| GNSS positioning | Disabled | Enabled | Enabled | Enabled |
| IMU fusion | Disabled | Enabled | Disabled | Enabled |
| Dead reckoning | Disabled | Enabled | Disabled | Enabled |
| CAN monitoring | Read-only | Advisory | Logging | Full |
| Actuation requests | Disabled | Enabled | Disabled | Enabled |
| Fleet reporting | Disabled | Disabled | Enabled | Optional |
| Driver behavior scoring | Disabled | Disabled | Enabled | Optional |
| Multi-camera fusion | Disabled | Disabled | Disabled | Enabled |
| Radar fusion | Disabled | Disabled | Disabled | Enabled |
| IR illumination | Disabled | Enabled | Enabled | Enabled |
| Ethernet streaming | Disabled | Disabled | Disabled | Enabled |

## 3. Configuration Database Structure

### 3.1 Board Identity Block (EEPROM)

```
Offset  Size  Field
0x00    4     Magic number (0xADV1)
0x04    2     Board revision (major.minor)
0x06    2     Variant code (Entry=0x01, Mid=0x02, High=0x03)
0x08    4     Manufacturing date (Unix timestamp)
0x0C    16    Serial number (ASCII)
0x1C    4     Configuration profile ID
0x20    4     Calibration date (Unix timestamp)
0x24    2     Hardware feature flags (bitfield)
0x26    2     CRC16 (over 0x00-0x25)
```

### 3.2 Hardware Feature Flags

| Bit | Feature | Set=Present |
|-----|---------|-------------|
| 0 | Forward camera port populated | 1=Yes |
| 1 | DMS camera port populated | 1=Yes |
| 2 | GNSS receiver populated | 1=Yes |
| 3 | IMU populated | 1=Yes |
| 4 | IR interface populated | 1=Yes |
| 5 | Second CAN channel populated | 1=Yes |
| 6 | Ethernet PHY populated | 1=Yes |
| 7 | Active cooling present | 1=Yes |
| 8-15 | Reserved | 0 |

### 3.3 Runtime Configuration Files

```
/etc/advis/
  |- platform.conf          # Auto-detected hardware configuration
  |- features.conf          # Enabled feature set (from profile)
  |- calibration/
  |    |- camera_fwd.cal    # Forward camera intrinsics (if present)
  |    |- camera_dms.cal    # DMS camera intrinsics
  |    |- imu.cal           # IMU bias/alignment (if present)
  |- network/
  |    |- can0.conf         # CAN bus configuration
  |    |- can1.conf         # Secondary CAN (if present)
  |- models/
       |- dms_model.bin     # DMS neural network model
       |- adas_model.bin    # ADAS neural network model (if enabled)
```

## 4. Variant Validation Process

### 4.1 Manufacturing Test Coverage

| Test Stage | Entry | Mid | High | Method |
|------------|-------|-----|------|--------|
| Power rail verification | All rails | All rails | All rails | Automated probe |
| ICT (In-Circuit Test) | Yes | Yes | Yes | Flying probe / bed-of-nails |
| Functional boot test | Yes | Yes | Yes | Automated test script |
| Camera stream test | DMS only | Both cameras | All cameras | Pattern generator |
| CAN loopback | Single channel | Single channel | Both channels | Internal loopback |
| GNSS sensitivity | Skip | Yes | Yes | RF signal generator |
| IMU self-test | Skip | Yes | Yes | BMI088 built-in self-test |
| Thermal stress | Abbreviated | Full | Full (with cooling) | Temperature chamber |
| Vibration screening | Abbreviated | Full | Full | Shaker table |

### 4.2 Validation Matrix by Product Variant

| Validation Test | ADVIS Assist | ADVIS Control | ADVIS Fleet | ADVIS Fusion |
|-----------------|-------------|---------------|-------------|--------------|
| DMS accuracy | Required | Required | Required | Required |
| Forward ADAS accuracy | Required | Required | N/A | Required |
| FCW response time | Required | Required | N/A | Required |
| LDW accuracy | Required | Required | N/A | Required |
| AEB request timing | N/A | Required | N/A | Required |
| ACC request stability | N/A | Required | N/A | Required |
| GNSS position accuracy | Required | Required | Required | Required |
| IMU drift characterization | Required | Required | N/A | Required |
| CAN message timing | Required | Required | Required | Required |
| Fleet event logging | N/A | N/A | Required | Optional |
| Driver scoring accuracy | N/A | N/A | Required | Optional |
| Sensor fusion latency | N/A | N/A | N/A | Required |
| Multi-camera sync | N/A | N/A | N/A | Required |

## 5. Configuration Change Control

### 5.1 When Configuration Changes Require ECO

| Change | ECO Required? |
|--------|--------------|
| New feature flag definition | Yes |
| Profile feature enable/disable | Yes |
| EEPROM format change | Yes |
| Calibration parameter range change | Yes |
| New configuration file addition | No (if additive) |
| Model file update | No (firmware update process) |

### 5.2 Configuration Audit

Quarterly configuration audits verify:
- All production units have valid EEPROM data
- Feature flags match physical BOM for sampled units
- Calibration dates are within validity period
- Firmware versions match configuration profile requirements

---

*ADVIS Hardware Platform - Configuration Management*
