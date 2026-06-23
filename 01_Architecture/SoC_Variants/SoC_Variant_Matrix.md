# ADVIS SoC Variant Compatibility Matrix

## Version
v1.0 - June 2026

## Document ID
ARCH-SOC-001

---

## 1. Overview

This document defines the SoC compatibility matrix for the ADVIS platform. The modular carrier-to-SoM architecture allows multiple SoC options to be supported without carrier board redesign. Each SoC variant maps to one or more ADVIS product tiers.

---

## 2. SoC Compatibility Matrix

| Parameter | AM62A | AM68A / TDA4VM | TDA4VH | SA8295P |
|-----------|-------|----------------|--------|---------|
| **Vendor** | Texas Instruments | Texas Instruments | Texas Instruments | Qualcomm |
| **Process** | 16nm | 7nm | 7nm | 5nm |
| **CPU cores** | 4x A53 | 2x A72 + 4x A53 | 2x A72 + 4x A53 | 8x Kryo Gold |
| **AI accelerator** | 2 TOPS (DLA) | 8 TOPS (C7x + MMA) | 32 TOPS (C7x + MMA) | 30+ TOPS (Hexagon) |
| **CSI-2 inputs** | 1x 4-lane | 2x 4-lane | 4x 4-lane | 4x 4-lane |
| **Camera support** | 2 cameras | 4 cameras | 8 cameras | 8+ cameras |
| **DDR** | LPDDR4, 16GB max | LPDDR4, 16GB max | LPDDR4x, 32GB max | LPDDR5, 32GB max |
| **CAN interfaces** | 2x MCAN | 3x MCAN | 3x MCAN | 2x CAN-FD (via QUP) |
| **USB** | USB 2.0 | USB 3.0 + 2.0 | USB 3.0 + 2.0 | USB 3.1 |
| **Ethernet** | 1x RGMII | 2x RGMII | 2x RGMII | 1x RGMII |
| **Typical power** | 3W | 5W | 10W | 12W |
| **Max TDP** | 5W | 8W | 15W | 20W |
| **Operating temp** | -40 to +125C Tj | -40 to +125C Tj | -40 to +125C Tj | -40 to +125C Tj |
| **ADVIS tier** | Assist, Fleet | Control | Fusion | Fusion (premium) |

---

## 3. Carrier Compatibility Assessment

| Feature Required | AM62A | AM68A/TDA4VM | TDA4VH | SA8295P |
|-----------------|-------|--------------|--------|---------|
| 4-lane CSI-2 Rx | Yes | Yes | Yes | Yes |
| I2C master (camera cfg) | Yes | Yes | Yes | Yes |
| SPI master (IMU) | Yes | Yes | Yes | Yes |
| UART (GNSS) | Yes | Yes | Yes | Yes |
| UART (Debug) | Yes | Yes | Yes | Yes |
| CAN-FD controller | Yes | Yes | Yes | Yes |
| USB 2.0 device | Yes | Yes | Yes | Yes |
| SD/MMC | Yes | Yes | Yes | Yes |
| GPIO (WDG, IR, CAN_STB) | Yes | Yes | Yes | Yes |
| 5V input acceptance | Via PMIC | Via PMIC | Via PMIC | Via PMIC |
| **Carrier compatible** | **YES** | **YES** | **YES** | **YES*** |

*SA8295P requires adapter board or alternate SoM connector due to different form factor.

---

## 4. Product Tier to SoC Mapping

| Product Tier | Primary SoC | Alternate SoC | Rationale |
|-------------|-------------|---------------|-----------|
| ADVIS Assist | AM62A | AM68A (downclocked) | 2 TOPS sufficient for FCW+LDW+DMS |
| ADVIS Control | AM68A / TDA4VM | TDA4VH (future) | 8 TOPS for AEB/ACC/LKA requests |
| ADVIS Fusion | TDA4VH | SA8295P | 32 TOPS for radar fusion + enhanced perception |
| ADVIS Fleet | AM62A | AM68A | Focus on logging, not heavy compute |

---

## 5. SoM Module Options

| SoM Vendor | Module | SoC | Form Factor | Status |
|------------|--------|-----|-------------|--------|
| Phytec | phyCORE-AM68A | AM68A/TDA4VM | SODIMM-style | Baseline reference |
| Phytec | phyCORE-AM62A | AM62A | SODIMM-style | Evaluation pending |
| TI | SK-TDA4VM (eval) | TDA4VM | Dev board | Reference only |
| Custom | ADVIS-SoM-V1 | TDA4VH | Custom B2B | Future development |

---

## 6. Performance Comparison for ADVIS Workloads

| Workload | AM62A | AM68A/TDA4VM | TDA4VH | SA8295P |
|----------|-------|--------------|--------|---------|
| Forward camera object detection (30fps) | Marginal | Comfortable | Excess | Excess |
| DMS face/gaze tracking (30fps) | OK | Comfortable | Excess | Excess |
| LDW lane marking detection | OK | Comfortable | Excess | Excess |
| AEB time-to-collision compute | Insufficient | OK | Comfortable | Comfortable |
| Radar point cloud fusion | N/A | Marginal | Comfortable | Comfortable |
| Multi-camera surround view | N/A | N/A | OK | Comfortable |
| CAN bus logging (100% bus load) | OK | OK | OK | OK |
| GNSS + IMU sensor fusion | OK | OK | OK | OK |

---

## 7. Power and Thermal Impact

| SoC | Carrier Thermal Design | Additional Cooling | Power Budget from 5V_SYS |
|-----|----------------------|-------------------|--------------------------|
| AM62A | Standard thermal pad | None required | 2A from 5V_SYS (via PMIC) |
| AM68A/TDA4VM | Enhanced thermal pad | Small heatsink | 3.5A from 5V_SYS (via PMIC) |
| TDA4VH | Large heatsink required | Thermal gap filler to lid | 5A from 5V_SYS (via PMIC) |
| SA8295P | Active or large passive | Possible carrier redesign | May exceed 6A budget |

---

## 8. Migration Path

```
Phase 1 (2026)          Phase 2 (2027)         Phase 3 (2028)
+-----------+           +------------+          +------------+
| AM62A     |           | TDA4VH     |          | Next-gen   |
| AM68A     |           | SA8295P    |          | SoC (TBD)  |
| (Baseline)|           | (Extended) |          | (Future)   |
+-----------+           +------------+          +------------+
     |                       |                       |
     | Same carrier          | Same carrier          | Carrier v2
     | board v1.0            | board v1.0            | (if needed)
     |                       | (adapter for SA8295)  |
```

---

## 9. SoC Selection Criteria

When evaluating new SoC candidates for ADVIS carrier compatibility:

1. Must support 4-lane MIPI CSI-2 receive (minimum 1 port)
2. Must have CAN-FD controller (minimum 1 channel)
3. Must support SPI master at 10 MHz (for IMU)
4. Must provide 2 UART channels (GNSS + debug)
5. Must accept 5V or 3.3V power input (via on-module PMIC)
6. Must operate across -40C to +85C ambient
7. Must be available in automotive-qualified grade (AEC-Q100)
8. Module form factor must fit within SoM connector zone on carrier

---

## 10. Revision History

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| 1.0 | 2026-06 | Architecture Team | Initial release |
