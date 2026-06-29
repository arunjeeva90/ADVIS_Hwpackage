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

Common carrier-board reuse applies primarily to the v0.4.4 SOM-based A-sample architecture, where compute variation can be handled through the SoM. For the v0.5 compact direct-SoC architecture, product tiers aim to share common mechanical, optical, connector, software and calibration architecture. PCB commonality depends on SoC pinout, power-tree, DDR, thermal and cost feasibility. Tier differentiation is achieved through SoC selection, sensor population, firmware feature licensing and OEM integration scope.

---

## Repository Structure

> **Note:** This repository is currently architecture-definition focused. Schematic/PCB/manufacturing folders may contain placeholders until corresponding engineering phases begin.

### 01_Architecture/
- **Purpose:** Top-level system architecture definitions, design decisions, and hardware baselines
- **Contains:** System block diagrams, signal flow diagrams, power tree, ground domains, thermal strategy, mechanical envelope, SoC variant analysis, modular platform definition, visual concept assets, and locked baseline documents
- **Used by:** Systems Engineering, Hardware Architecture, Mechanical Engineering, Thermal Engineering
- **Output:** Architecture baselines (v0.4.4, v0.5), SoC selection decisions, board-level signal/power topology

### 02_Schematic/
- **Purpose:** Schematic capture assets, component libraries, and electrical design verification
- **Contains:** Schematic sheets (hierarchical), BOM management, ERC reports and waiver policies, net lists, symbols, review checklists
- **Used by:** Electrical Engineering, Schematic Capture, Component Engineering
- **Output:** Verified schematic netlists, production BOM, ERC-clean design release

### 03_PCB_Layout/
- **Purpose:** PCB physical design, manufacturing data, and design-for-manufacturing validation
- **Contains:** Stackup definitions, component placement strategy, routing constraints (high-speed rules), Gerber outputs, assembly drawings, DFM reports
- **Used by:** Layout Engineering, Signal Integrity, Manufacturing Engineering
- **Output:** Gerber release package, assembly drawings, DFM-validated board design

### 04_Firmware_HAL/
- **Purpose:** Hardware abstraction layer definitions, device tree overlays, and low-level driver interfaces
- **Contains:** HAL API definitions, peripheral driver specifications, boot sequence, device tree templates
- **Used by:** Firmware Engineering, BSP/SDK Team, Software Integration
- **Output:** HAL interface contracts, device tree configurations, driver specifications for software team

### 05_Interface_Control_Documents/
- **Purpose:** Formal interface definitions between all subsystem boundaries
- **Contains:** Signal lists, timing diagrams, protocol specifications, connector pinouts, voltage/current specs
- **Used by:** All engineering disciplines (hardware/firmware/software), System Integration, Test Engineering
- **Output:** ICD releases that define the contract between hardware subsystems and external interfaces

### 06_Patent_Strategy/
- **Purpose:** Invention disclosure tracking, patent claim drafts, and prior art analysis
- **Contains:** Invention disclosures, claim drafts and guidelines, prior art searches, freedom-to-operate analysis
- **Used by:** Systems Engineering, Patent Counsel, IP Management
- **Output:** Patent filing decisions, FTO risk assessments, claim language for filings

### 07_IP_Protection/
- **Purpose:** Trade secret identification, licensing strategy, and competitive positioning
- **Contains:** Trade secret registers, licensing frameworks, competitive analysis, IP protection policies
- **Used by:** IP Management, Legal, Business Development
- **Output:** IP protection policies, licensing terms, competitive differentiation documentation

### 08_Validation_Testing/
- **Purpose:** Hardware validation plans, test procedures, and results tracking
- **Contains:** Power integrity (PI), signal integrity (SI), EMC/EMI, environmental testing, DVT plans, DVP&R matrices
- **Used by:** Validation Engineering, Test Engineering, Signal Integrity, EMC Lab
- **Output:** Test reports, pass/fail matrices, compliance evidence, design validation closure

### 09_Compliance_Safety/
- **Purpose:** Automotive standards compliance, functional safety, and regulatory requirements
- **Contains:** ISO 26262 work products, FMEA documents, eye safety analysis (IR), ASIL decomposition, regulatory mapping
- **Used by:** Safety Engineering, Compliance, Systems Engineering, Quality
- **Output:** Safety cases, FMEA reports, compliance matrices, ASIL allocation documents

### 10_Manufacturing/
- **Purpose:** Production readiness, assembly processes, test fixtures, and cost management
- **Contains:** Assembly process definitions, test fixture specifications, production BOM, yield tracking, production costing
- **Used by:** Manufacturing Engineering, Production, Quality, Procurement
- **Output:** Assembly instructions, test fixture designs, production cost models, yield baselines

### 11_Documentation/
- **Purpose:** Engineering documentation, design reviews, handoff packages, and technical notes
- **Contains:** Handoff documents, design review records, change log, technical notes (open decisions, verification rules, part selection)
- **Used by:** All engineering disciplines, Program Management, Quality
- **Output:** Design review approvals, handoff packages for downstream phases, technical decision records

### 12_Configuration_Management/
- **Purpose:** Version control, engineering change order (ECO) tracking, and BOM variant management
- **Contains:** ECO log, BOM variant definitions, version tagging policy, configuration baselines
- **Used by:** Configuration Management, Program Management, Quality, Procurement
- **Output:** ECO approvals, variant matrices, release baselines

### 13_OEM_Customization/
- **Purpose:** Customer-facing variant definitions, feature tier scaling, and SoC option packages
- **Contains:** Feature tier definitions (Entry/Assist/Control/High), SoC option packages guide, OEM-specific variant configurations
- **Used by:** Sales Engineering, Systems Engineering, Program Management, OEM Integration
- **Output:** OEM-ready variant specifications, feature/cost trade-off guides, customization options

---

## Visual Concept Assets

Conceptual visualizations of the v0.5 Compact Module are available for architecture communication:

- [Compact Board 3D View (description)](01_Architecture/Visual_Concepts/ADVIS_v0.5_Compact_Board_3D_View.md)
- [Compact Board 3D View (SVG)](01_Architecture/Visual_Concepts/ADVIS_v0.5_Compact_Board_3D_View.svg)
- [Compact Module Exploded View (SVG)](01_Architecture/Visual_Concepts/ADVIS_v0.5_Compact_Module_Exploded_View.svg)

These are conceptual visualizations only - not production layout, not mechanical CAD release.

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

### SoC Position Summary (v0.5)

| SoC | AI Performance | Target Tier | Notes |
|-----|---------------|-------------|-------|
| AM62A7-Q1 | 2 TOPS | Single-camera DMS, fleet-lite | Single CSI-2 RX port |
| TDA4VL-Q1 | 4 TOPS | Assist, Fleet (dual-camera) | H speed grade: A72 at 1200 MHz, C7x at 500 MHz |
| TDA4AL-Q1 | 8 TOPS | Comparison candidate | No GPU, encode only, analytics-focused |
| TDA4VE-Q1 | 8 TOPS | Comparison candidate | GPU, higher resources |
| TDA4VM-Q1 | 8 TOPS | Control | J721E platform, A72 at 2.0 GHz |

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
| v0.5.0 | 2026-06 | Compact direct-MIPI architecture definition started |
| v0.4.4 | 2026-06 | Architecture lock, initial document population |
| v0.4.3 | 2026-05 | Platform modularity concept finalized |
| v0.4.2 | 2026-04 | ICD signal lists defined |
| v0.4.1 | 2026-03 | Component selection baseline |
| v0.4.0 | 2026-02 | Repository structure created |

---

## Confidentiality

This repository contains proprietary hardware IP. All contents are confidential and subject to applicable NDA terms.
