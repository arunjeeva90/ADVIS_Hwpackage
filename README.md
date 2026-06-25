# ADVIS Hardware Package (ADVIS_Hwpackage)

## Project: ADVIS - Adaptive Driver & Vehicle Intelligence System

**Version:** v0.5 (architecture definition)  
**Status:** Dual-baseline repository: A-sample validation + compact production-cost-down module

---

## What Is This Repository?

This repository is the complete hardware IP package for the ADVIS dual-camera ADAS + DMS vehicle platform. It contains architecture definitions, schematic capture assets, firmware abstraction layers, interface control documents, patent/IP strategy, validation plans, and OEM customization frameworks.

This repository contains two hardware baselines:

1. **ADVIS v0.4.4** - A-sample SerDes/SOM validation platform
2. **ADVIS v0.5** - Compact direct-MIPI production-cost-down module

---

## Hardware Baselines

### ADVIS_A_SAMPLE_v0.4.4_SerDes_SOM

| Field | Detail |
|-------|--------|
| **Purpose** | Engineering validation, TI EVM/SDK bring-up, external camera experiments, FPD-Link validation, debug-heavy A-sample board |
| **Architecture** | SOM + DS90UB954 + FPD-Link camera inputs + GNSS + IMU + USB/debug/microSD |
| **Status** | Architecture locked as A-sample schematic capture baseline |
| **PCB Release** | Blocked until implementation-closure items are completed |

This baseline is documented in the consolidated handoff document at `11_Documentation/Handoff_Documents/IND-VIAS_ECU_v0.4.4_Consolidated_Handoff.md` and its architecture baseline at `01_Architecture/Baselines/ADVIS_A_SAMPLE_v0.4.4_SerDes_SOM.md`.

### ADVIS_COMPACT_v0.5_Direct_MIPI

| Field | Detail |
|-------|--------|
| **Purpose** | Compact production cost-down windshield module |
| **Architecture** | Integrated road-facing camera + cabin-facing DMS camera + direct MIPI CSI-2 + one shared SoC + shared power + shared safety supervisor |
| **Removes by Default** | DS90UB954, UB953, FAKRA/HSD, PoC, microSD, Ethernet, large debug headers |
| **Keeps** | 12V protection, CAN-FD, watchdog, reset supervisor, sensor rails, IR control, ESD/EMC protection |
| **Status** | Architecture definition in progress |

This baseline is defined at `01_Architecture/Baselines/ADVIS_COMPACT_v0.5_Direct_MIPI.md`.

---

## Safety Boundary

ADVIS does not directly actuate brake, steering, throttle or powertrain.

- **ADVIS Assist** provides warning/advisory outputs.
- **ADVIS Control** may generate perception-validated, safety-supervised actuation request messages over CAN/CAN-FD, depending on OEM integration.

Final actuator authority, arbitration and vehicle-level safety release remain with the OEM brake, EPS and powertrain ECUs.

ADVIS does not claim:
- Direct brake actuation
- Direct steering actuation
- Direct throttle actuation
- ASIL-C or ASIL-D system-level compliance

---

## Platform Overview

The ADVIS platform is a vehicle-mounted edge compute unit that:

- Receives two camera streams (Forward + DMS)
- Processes perception and monitoring workloads on a TDA4VM/TDA4VL/AM62A-class SoC
- Monitors/logs CAN-FD traffic
- Fuses GNSS + IMU data for positioning and motion context (optional per variant)
- Supports IR illumination for DMS
- Generates safety-supervised actuation REQUESTS to OEM vehicle controllers

Camera connection method depends on hardware baseline:
- **v0.4.4**: FPD-Link III via DS90UB954-Q1 (external/remote cameras)
- **v0.5**: Direct MIPI CSI-2 (integrated cameras in windshield module)

---

## Product Family

| Product | Sensor Set | Feature Scope |
|---------|-----------|---------------|
| ADVIS Assist | Forward camera + DMS camera | FCW, LDW, TSR, PCW, DMS |
| ADVIS Control | Same two-camera hardware | AEB, ACC, LKA request outputs, driver-aware speed moderation |
| ADVIS Fusion | Camera + DMS + radar | Sensor fusion, enhanced AEB/ACC/LKA, blind-spot/moving-off support |
| ADVIS Fleet | Camera + DMS, later radar optional | Fleet safety, driver behavior, event logging |

All product tiers share a common carrier board. Tier differentiation is achieved through SoC selection and firmware feature licensing.

---

## Repository Structure

```
ADVIS_Hwpackage/
|
|-- 01_Architecture/          Architecture definitions, block diagrams, baselines
|-- 02_Schematic/             Schematic sheets, symbols, BOM, netlists
|-- 03_PCB_Layout/            Stackup, placement, routing, gerbers, DFM
|-- 04_Firmware_HAL/          Hardware abstraction layer, drivers, device trees
|-- 05_Interface_Control_Documents/  ICDs for all subsystem boundaries
|-- 06_Patent_Strategy/       Invention disclosures, claims, prior art, filings
|-- 07_IP_Protection/         Trade secrets, licensing, competitive analysis
|-- 08_Validation_Testing/    PI, SI, EMC, environmental, DVT, DVP&R
|-- 09_Compliance_Safety/     Automotive standards, eye safety, FMEA
|-- 10_Manufacturing/         Assembly, test fixtures, production BOM
|-- 11_Documentation/         Handoff docs, design reviews, change log
|-- 12_Configuration_Management/  Version control, ECO tracking, BOM variants
|-- 13_OEM_Customization/     Variant matrix, SoC options, feature tiers
```

---

## Key Hardware Stack (v0.4.4 A-sample)

| Function | Component |
|----------|-----------|
| Compute SOM | TDA4VM / AM68A-class (Phytec phyCORE baseline) |
| Deserializer | DS90UB954-Q1 |
| 5V Buck | LM61460-Q1 class, 6A |
| 3.3V Buck | TPS62130A-Q1 class |
| 1.8V LDO | TLV75518-Q1 class |
| Supervisor | TPS3808G33-Q1 class |
| Watchdog | TPS3431-Q1 |
| CAN-FD | TCAN1044AV-Q1 |
| GNSS | u-blox NEO-M9N-00B |
| IMU | Bosch BMI088 |

## Key Hardware Stack (v0.5 Compact)

| Function | Component |
|----------|-----------|
| SoC (direct mount or SiP) | TDA4VL / TDA4VM / AM62A class |
| Forward Camera | IMX390 / OX03C10 / AR0233 class (direct MIPI) |
| DMS Camera | OX01N1B / OX01H1B / RGB-IR / AR0144 class (direct MIPI) |
| 5V Buck | LM61460-Q1 class |
| 3.3V Buck | TPS62130A-Q1 class |
| 1.8V LDO | TLV75518-Q1 class |
| Supervisor | TPS3808G33-Q1 class |
| Watchdog | TPS3431-Q1 |
| CAN-FD | TCAN1044AV-Q1 |

---

## Current Status

| Baseline | Architecture | Schematic | PCB |
|----------|-------------|-----------|-----|
| v0.4.4 A-sample | LOCKED | Can begin (blocked items remain) | BLOCKED |
| v0.5 Compact | Definition in progress | Not started | Not started |

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| v0.5.0 | 2026-07 | Compact direct-MIPI architecture definition started |
| v0.4.4 | 2026-06 | Architecture lock, initial document population |
| v0.4.3 | 2026-05 | Platform modularity concept finalized |
| v0.4.2 | 2026-04 | ICD signal lists defined |
| v0.4.1 | 2026-03 | Component selection baseline |
| v0.4.0 | 2026-02 | Repository structure created |

---

## Confidentiality

This repository contains proprietary hardware IP. All contents are confidential and subject to applicable NDA terms.
