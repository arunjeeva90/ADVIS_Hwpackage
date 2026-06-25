# ADVIS v0.4.4 A-Sample SerDes/SOM Validation Platform

**Classification:** Confidential - Engineering Use Only  
**Status:** Architecture LOCKED  
**Date:** June 2026

---

## 1. Purpose

The ADVIS v0.4.4 A-sample is an engineering validation platform designed for:

- TI EVM and SDK bring-up with TDA4VM/AM68A-class SOM
- External/remote camera validation using FPD-Link III
- DS90UB954-Q1 deserializer characterization and integration
- Full-featured debug environment (USB-C, UART, microSD, Ethernet headers)
- Peripheral subsystem validation (GNSS, IMU, CAN-FD, watchdog, power tree)
- Software and algorithm development with maximum observability
- A-sample customer demonstrations and OEM evaluation

This platform prioritizes engineering flexibility over production cost optimization.

---

## 2. Architecture Overview

### 2.1 Compute

- **SOM-based compute:** Phytec phyCORE-AM68A (TDA4VM-class) system-on-module
- SOM provides CPU, GPU, AI accelerator, DDR memory, eMMC storage
- SOM connector carries CSI-2, SPI, I2C, UART, CAN, USB, SD/MMC, GPIO

### 2.2 Camera Subsystem

- **DS90UB954-Q1 deserializer** aggregates two FPD-Link III camera inputs
- Port 0 (RX0): Forward-facing ADAS camera via coaxial cable (up to 15m)
- Port 1 (RX1): Cabin-facing DMS camera via coaxial cable (up to 15m)
- Remote camera modules use UB953-class serializers
- Power-over-Coax (PoC) supplies remote serializer modules through the same coax link
- 4-lane MIPI CSI-2 output from DS90UB954 to SOM (VC0 = Forward, VC1 = DMS)

### 2.3 Sensor Subsystem

- **GNSS:** u-blox NEO-M9N-00B, concurrent multi-GNSS, UART + I2C interface, 1PPS output
- **IMU:** Bosch BMI088, 6-axis (accelerometer + gyroscope), SPI interface, dual chip-select
- Active GNSS antenna support with bias-T and ESD protection

### 2.4 Vehicle Interface

- **CAN-FD:** TCAN1044AV-Q1, up to 5 Mbps, 120 ohm termination (DNI option)
- Advisory/logging mode by default
- Actuation request output capability depending on product tier and OEM integration

### 2.5 Power Tree

```
Vehicle 12V --> [Fuse] --> [TVS] --> [PMOS Reverse Polarity]
  --> LM61460-Q1 (12V to 5V, 6A)
    --> TPS62130A-Q1 (5V to 3.3V, 3A)
      --> TLV75518-Q1 (3.3V to 1.8V, 500mA)
  --> TPS3808G33-Q1 (supervisor, monitors 3.3V)
  --> TPS3431-Q1 (watchdog, boot-gated enable)
```

### 2.6 Debug and Service Interfaces

- USB-C device mode (firmware update, data offload)
- UART debug console (115200 baud, 3.3V, 1.27mm header)
- MicroSD card slot (UHS-I, removable storage for logs)
- Optional Ethernet header (debug/development)
- Large debug headers for logic analyzer/scope probing

### 2.7 IR Illumination

- External IR daughterboard connector (5V_IR, IR_EN, IR_FAULT_N, GND)
- Load-switch controlled, 2W max power budget
- Synchronized to DMS frame capture via SOM GPIO

---

## 3. Why This Platform Is Useful

| Use Case | Benefit |
|----------|---------|
| TI SDK integration | Full EVM-equivalent bring-up with automotive peripherals |
| Camera algorithm development | Real FPD-Link camera feeds at realistic cable lengths |
| Power/thermal characterization | All rails instrumented with test points |
| CAN-FD integration testing | Real transceiver on real bus |
| GNSS/IMU sensor fusion | Full sensor complement for positioning algorithms |
| A-sample OEM evaluation | Demonstrates complete feature set |
| Remote/external camera variants | Validates long-cable FPD-Link scenarios |
| Debug-intensive development | Maximum signal observability |

---

## 4. Why This Is Not the Lowest-Cost Production Design

| Factor | Impact |
|--------|--------|
| DS90UB954-Q1 deserializer | Adds cost when cameras are co-located in same module |
| UB953 serializers on camera modules | Additional cost per camera end |
| FAKRA/HSD coaxial connectors | Expensive automotive RF connectors |
| PoC inductors and filters | Not needed when cameras are on same PCB/flex |
| SOM module form factor | Higher cost vs. direct SoC placement |
| microSD slot | Not needed in production (eMMC sufficient) |
| USB-C connector and protection | Debug convenience, not production requirement |
| Ethernet header | Development tool, not production requirement |
| Large debug headers | Engineering tool, adds board area |
| Full GNSS + active antenna path | Not required for all product tiers |
| Full 6-axis IMU | Not required for all product tiers |
| Oversized PCB for debug access | Board area premium |

The compact production-cost-down architecture (v0.5) eliminates these items by integrating cameras directly into the windshield module with direct MIPI CSI-2 connections.

---

## 5. Current Blocked Items Before PCB Release

### 5.1 Critical Path

| # | Item | Owner | Status |
|---|------|-------|--------|
| 1 | Final PCB stackup selection (8 vs 10 layer) | Layout Lead | Open |
| 2 | SI simulation for CSI-2 lanes (1.6 Gbps) | SI Engineer | Open |
| 3 | Thermal simulation (SOM + DS90UB954 + buck) | Thermal Lead | Open |
| 4 | Connector vendor selection and 3D model | Mechanical | Open |
| 5 | EMC pre-compliance plan | EMC Engineer | Open |

### 5.2 Desirable Before Release

| # | Item | Owner | Status |
|---|------|-------|--------|
| 6 | GNSS antenna placement study | RF Engineer | Open |
| 7 | Power integrity simulation | PI Engineer | Open |
| 8 | Conformal coating specification | Manufacturing | Open |
| 9 | Production test point placement plan | Test Engineer | Open |
| 10 | Second-source component identification | Procurement | Open |

---

## 6. Relationship to v0.5 Compact Module

The v0.4.4 A-sample and v0.5 compact module serve different purposes:

- v0.4.4 is the development/validation workhorse with maximum flexibility
- v0.5 is the production-cost-optimized compact module for OEM deployment
- Learnings from v0.4.4 power tree, watchdog, CAN-FD, and firmware directly carry forward to v0.5
- v0.4.4 remains valid for remote-camera OEM variants where FPD-Link is still required

---

*End of Document*
