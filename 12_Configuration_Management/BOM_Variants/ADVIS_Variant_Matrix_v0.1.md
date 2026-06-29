# ADVIS Variant Matrix v0.1

**Classification:** Confidential - Engineering Use Only  
**Version:** 0.1  
**Date:** June 2026

---

## 1. Purpose

This document defines the hardware configuration variants for the ADVIS platform across product tiers and hardware baselines. It specifies which components are populated, optional (DNI), or not applicable for each variant.

---

## 2. Population Legend

| Symbol | Meaning |
|--------|---------|
| POP | Populated (installed) |
| DNI | Do Not Install (footprint present, component not placed) |
| N/A | Not applicable (no footprint on this board variant) |
| OPT | Optional (customer/OEM selectable at order time) |

---

## 3. Variant Matrix

| Parameter | ADVIS Assist | ADVIS Control | ADVIS Fleet | ADVIS Fusion | A-sample Engineering Board (v0.4.4) | Compact Production Board (v0.5) |
|-----------|-------------|---------------|-------------|--------------|--------------------------------------|----------------------------------|
| **Camera Architecture** | Direct MIPI (forward + DMS) | Direct MIPI (forward + DMS) | Direct MIPI (forward + DMS) | Direct MIPI (forward + DMS) + radar interface | SerDes FPD-Link III via DS90UB954 (external cameras) | Direct MIPI CSI-2 (integrated cameras) |
| **SoC Class** | AM62A or TDA4VL (entry) | TDA4VL or TDA4VM (mid) | TDA4VL or TDA4VM (mid) | TDA4VM (high) | TDA4VM/AM68A (SOM) | TDA4VL / TDA4VM / AM62A (direct) |
| **Memory (DDR)** | 2 GB LPDDR4 | 4 GB LPDDR4 | 4 GB LPDDR4 | 4 GB LPDDR4X | 4 GB (SOM-provided) | 2 GB (entry) / 4 GB (mid/high) |
| **Storage (eMMC)** | 16 GB | 32 GB | 32 GB | 32 GB | 32 GB (SOM-provided) | 16 GB (entry) / 32 GB (mid/high) |
| **GNSS** | DNI | DNI | POP (NEO-M9N or equivalent) | POP | POP (NEO-M9N-00B) | OPT (DNI pads; POP for Fleet/Fusion) |
| **IMU** | DNI | DNI | POP (BMI088 or equivalent) | POP | POP (BMI088) | OPT (DNI pads; POP for Fleet/Fusion) |
| **IR Illumination** | POP (integrated) | POP (integrated) | POP (integrated) | POP (integrated) | POP (external daughterboard) | POP (integrated on DMS pod) |
| **Ethernet** | N/A | N/A | OPT (for gateway variant) | OPT | POP (debug header) | N/A |
| **USB** | N/A | N/A | N/A | N/A | POP (USB-C device mode) | N/A (test pads only) |
| **MicroSD** | N/A | N/A | N/A | N/A | POP (UHS-I slot) | N/A |
| **CAN/CAN-FD** | POP (TCAN1044AV-Q1) | POP (TCAN1044AV-Q1) | POP (TCAN1044AV-Q1) | POP (TCAN1044AV-Q1) | POP (TCAN1044AV-Q1) | POP (TCAN1044AV-Q1) |
| **Feature Scope** | FCW, LDW, TSR, PCW, DMS alerting | AEB/ACC/LKA request outputs, speed moderation, full DMS | Fleet safety, driver behavior scoring, event recording, geofence | Sensor fusion AEB/ACC/LKA, radar-camera fusion, blind-spot | Full engineering validation and development platform | Production cost-optimized platform |
| **DS90UB954** | N/A | N/A | N/A | N/A | POP | N/A |
| **UB953 (per camera)** | N/A | N/A | N/A | N/A | Assumed on remote camera modules | N/A |
| **FAKRA/HSD Connectors** | N/A | N/A | N/A | N/A | POP (2x) | N/A |
| **PoC Network** | N/A | N/A | N/A | N/A | POP | N/A |
| **Debug Headers** | N/A | N/A | N/A | N/A | POP (large multi-pin) | N/A (test pads only) |
| **Watchdog (TPS3431)** | POP | POP | POP | POP | POP | POP |
| **Supervisor (TPS3808G33)** | POP | POP | POP | POP | POP | POP |
| **12V Protection** | POP | POP | POP | POP | POP | POP |
| **Radar Interface** | N/A | N/A | N/A | POP (connector/SPI) | N/A | OPT (reserved footprint for Fusion) |
| **Hardware Population Notes** | Minimum BOM for cost-sensitive L1 ADAS | Same as Assist + full SoC capability for L2 request outputs | Adds GNSS + IMU for fleet positioning and route analysis | Full sensor complement including radar interface | All subsystems populated for maximum development flexibility | Cost-optimized; DNI pads for optional subsystems |
| **Cost Impact** | Lowest | Low-Mid | Mid (GNSS+IMU add cost) | Highest (radar + full memory + full SoC) | Highest (SOM premium + SerDes + all peripherals + debug) | Low (target 40-60% cost reduction vs. A-sample) |

---

## 4. Notes

### 4.1 Camera Sensor Candidates

| Camera | Tier | Candidates |
|--------|------|-----------|
| Forward (ADAS) | All production variants | IMX390 / OX03C10 / AR0233 class |
| DMS (cabin) | All production variants | OX01N1B / OX01H1B / RGB-IR / AR0144 class |

Final sensor selection is an open item that affects MIPI lane requirements and power rail specifications.

### 4.2 SoC Selection Impact

| SoC | AI Performance | CSI Ports | Power | Target Tier |
|-----|---------------|-----------|-------|-------------|
| AM62A | 2 TOPS (product headline) | 1 CSI-Rx | Low | Single-camera DMS-only, fleet-lite |
| TDA4VL | 4 TOPS (confirmed per product headline and H speed grade) | 2 CSI-Rx | Medium | Assist, Fleet |
| TDA4AL | 8 TOPS (no GPU, encode only, analytics-focused) | Per datasheet | Medium-High | Comparison candidate |
| TDA4VE | 8 TOPS (GPU, higher resources) | Per datasheet | Medium-High | Comparison candidate |
| TDA4VM | 8 TOPS (confirmed per product headline) | 4 CSI-Rx | Higher | Control, Fleet, Fusion |

### 4.3 Variant ID Mechanism

Each production board includes hardware variant identification:
- Board variant ID pins (resistor-coded)
- SoC ID EEPROM or ID resistor network
- Camera module ID read path (I2C)
- Calibration EEPROM for per-unit configuration

This allows firmware to auto-detect hardware configuration at boot time.

### 4.4 Safety Boundary (All Variants)

ADVIS does not directly actuate brake, steering, throttle or powertrain.

ADVIS Assist provides warning/advisory outputs.

ADVIS Control may generate perception-validated, safety-supervised actuation request messages over CAN/CAN-FD, depending on OEM integration.

Final actuator authority, arbitration and vehicle-level safety release remain with the OEM brake, EPS and powertrain ECUs.

---

*End of Document*
