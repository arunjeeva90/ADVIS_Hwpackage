# ADVIS Hardware Package (ADVIS_Hwpackage)

## Project: ADVIS - Adaptive Driver & Vehicle Intelligence System

**Version:** v0.4.4  
**Status:** A-sample production-intent architecture and schematic capture baseline

---

## What Is This Repository?

This repository is the complete hardware IP package for the ADVIS dual-camera ADAS + DMS vehicle ECU platform. It contains architecture definitions, schematic capture assets, firmware abstraction layers, interface control documents, patent/IP strategy, validation plans, and OEM customization frameworks.

---

## Platform Overview

The ADVIS ECU is a vehicle-mounted edge compute unit that:

- Receives two camera streams (Forward + DMS) via FPD-Link III
- Processes perception and monitoring workloads on a TDA4VM/AM68A-class SOM
- Monitors/logs CAN-FD traffic
- Fuses GNSS + IMU data for positioning and motion context
- Exposes engineering/service interfaces (UART, USB, microSD)
- Supports external IR illumination for DMS

**Safety boundary:** This is an observation/processing/logging ECU. It does NOT perform actuation (brake, steering, throttle, powertrain). ADVIS generates safety-supervised actuation REQUESTS to OEM vehicle controllers only.

---

## Product Family

| Product | Sensor Set | Feature Scope |
|---------|-----------|---------------|
| ADVIS Assist | Forward camera + DMS camera | FCW, LDW, TSR, PCW, DMS |
| ADVIS Control | Same two-camera hardware | AEB, ACC, LKA request outputs, driver-aware speed moderation |
| ADVIS Fusion | Camera + DMS + radar | Sensor fusion, enhanced AEB/ACC/LKA, blind-spot/moving-off support |
| ADVIS Fleet | Camera + DMS, later radar optional | Fleet safety, driver behavior, event logging |

All product tiers share a common carrier board. Tier differentiation is achieved through SoM selection and firmware feature licensing.

---

## Repository Structure

```
ADVIS_Hwpackage/
|
|-- 01_Architecture/          Architecture definitions, block diagrams, platform spec
|-- 02_Schematic/             Schematic sheets, symbols, BOM, netlists
|-- 03_PCB_Layout/            Stackup, placement, routing, gerbers, DFM
|-- 04_Firmware_HAL/          Hardware abstraction layer, drivers, device trees
|-- 05_Interface_Control_Documents/  ICDs for all subsystem boundaries
|-- 06_Patent_Strategy/       Invention disclosures, claims, prior art, filings
|-- 07_IP_Protection/         Trade secrets, licensing, competitive analysis
|-- 08_Validation_Testing/    PI, SI, EMC, environmental, DVT
|-- 09_Compliance_Safety/     Automotive standards, eye safety, FMEA
|-- 10_Manufacturing/         Assembly, test fixtures, production BOM
|-- 11_Documentation/         Handoff docs, design reviews, change log
|-- 12_Configuration_Management/  Version control, ECO tracking, BOM variants
|-- 13_OEM_Customization/     Variant matrix, SoC options, feature tiers
```

---

## Key Hardware Stack

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

---

## Current Status

- **Architecture:** LOCKED
- **Schematic skeleton capture:** CAN BEGIN
- **ERC-clean schematic:** BLOCKED (pending SOM pinout, camera ICD, PoC values)
- **PCB layout release:** BLOCKED

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| v0.4.4 | 2026-06 | Architecture lock, initial document population |
| v0.4.3 | 2026-05 | Platform modularity concept finalized |
| v0.4.2 | 2026-04 | ICD signal lists defined |
| v0.4.1 | 2026-03 | Component selection baseline |
| v0.4.0 | 2026-02 | Repository structure created |

---

## Confidentiality

This repository contains proprietary hardware IP. All contents are confidential and subject to applicable NDA terms.
