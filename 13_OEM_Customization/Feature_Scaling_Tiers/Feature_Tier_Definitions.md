# ADVIS Feature Scaling Tier Definitions

## 1. Overview

The ADVIS platform defines three hardware scaling tiers that enable product variants from basic fleet DMS through to full surround-view sensor fusion. Each tier represents a distinct capability level, cost point, and thermal envelope.

---

## 2. Entry Tier

### 2.1 Summary

| Attribute | Specification |
|-----------|--------------|
| **Target Use Case** | Single-camera DMS, basic fleet monitoring |
| **SoC** | TI AM62A |
| **AI Performance** | <1 TOPS |
| **Camera Count** | 1 (DMS only) |
| **Sensor Set** | DMS camera, CAN monitor |
| **Target BOM Cost** | Lowest tier |
| **Power Envelope** | <5W total system |
| **Thermal Solution** | Passive (no heatsink required at typical ambient) |
| **Form Factor** | Ultra-compact (<60x60mm PCB) |

### 2.2 Feature Set

| Feature | Status |
|---------|--------|
| Drowsiness detection | Included |
| Distraction detection | Included |
| Phone use detection | Included |
| Driver identification | Optional |
| CAN bus monitoring (read-only) | Included |
| USB diagnostics | Included |
| MicroSD logging | Included |
| GNSS positioning | Optional (populate/depopulate) |
| Forward ADAS | Not available |
| IMU fusion | Not available |
| Actuation requests | Not available |

### 2.3 Compute Requirements

| Resource | Utilization |
|----------|-------------|
| CPU (A53) | ~40% (DMS pipeline + Linux OS) |
| AI accelerator | ~60% (DMS inference @ 30fps) |
| Memory | 1GB LPDDR4 sufficient |
| Storage | 4GB eMMC + MicroSD |
| CSI-2 bandwidth | 1 lane sufficient (2MP @ 30fps) |

### 2.4 Target Applications

- Fleet driver monitoring (regulatory compliance)
- Insurance telematics with driver behavior
- Basic ride-share driver monitoring
- Commercial vehicle fatigue detection
- Mining/construction equipment operator monitoring

---

## 3. Mid Tier (Current v0.4.4 Baseline)

### 3.1 Summary

| Attribute | Specification |
|-----------|--------------|
| **Target Use Case** | Dual-camera ADAS + DMS, full safety advisory |
| **SoC** | TI AM68A / TDA4VM |
| **AI Performance** | 8 TOPS |
| **Camera Count** | 2 (Forward + DMS) |
| **Sensor Set** | Forward camera, DMS camera, GNSS, IMU, CAN |
| **Target BOM Cost** | Baseline (reference) |
| **Power Envelope** | 10-15W typical, 20W maximum |
| **Thermal Solution** | Passive (heatsink, natural convection) |
| **Form Factor** | Standard automotive module (~100x80mm PCB) |

### 3.2 Feature Set

| Feature | Status |
|---------|--------|
| All Entry tier features | Included |
| Forward Collision Warning (FCW) | Included |
| Lane Departure Warning (LDW) | Included |
| Traffic Sign Recognition (TSR) | Included |
| Pedestrian/Cyclist Warning (PCW) | Included |
| Headway monitoring | Included |
| AEB request output | Included (ADVIS Control) |
| ACC request output | Included (ADVIS Control) |
| LKA request output | Included (ADVIS Control) |
| GNSS positioning + timing | Included |
| IMU (6-axis) fusion | Included |
| Dead reckoning navigation | Included |
| IR illumination control | Included |
| Driver-aware speed moderation | Included (ADVIS Control) |

### 3.3 Compute Requirements

| Resource | Utilization |
|----------|-------------|
| CPU (2x A72) | ~60% (dual pipeline + fusion + Linux) |
| AI accelerator (C7x+MMA) | ~75% (ADAS + DMS concurrent inference) |
| Safety MCU (R5F) | ~30% (watchdog management, CAN arbitration) |
| Memory | 2-4GB LPDDR4 |
| Storage | 16GB eMMC + MicroSD |
| CSI-2 bandwidth | 4 lanes (2x 2MP @ 30fps, VC multiplexed) |

### 3.4 Target Applications

- OEM ADAS Level 1 / Level 2 (Euro NCAP compliant)
- OEM driver monitoring (EU GSR2 compliance)
- Fleet safety with full ADAS advisory
- Advanced insurance telematics
- Ride-share/taxi safety platform

---

## 4. High Tier

### 4.1 Summary

| Attribute | Specification |
|-----------|--------------|
| **Target Use Case** | Multi-camera surround view + sensor fusion |
| **SoC** | TI TDA4VH |
| **AI Performance** | 32 TOPS |
| **Camera Count** | 4-8 (Forward + DMS + Side + Rear) |
| **Sensor Set** | Multi-camera, GNSS, IMU, radar input, Ethernet |
| **Target BOM Cost** | Premium tier |
| **Power Envelope** | 20-30W typical, 35W maximum |
| **Thermal Solution** | Active (forced-air or TEC assisted) |
| **Form Factor** | Extended automotive module (~120x100mm PCB) |

### 4.2 Feature Set

| Feature | Status |
|---------|--------|
| All Mid tier features | Included |
| Multi-camera (4-8) input | Included |
| Surround-view perception | Included |
| Radar data fusion | Included |
| Blind-spot detection | Included |
| Moving-off detection | Included |
| Rear cross-traffic warning | Included |
| Enhanced AEB (pedestrian, cyclist) | Included |
| Automotive Ethernet output | Included |
| Multi-CAN interface (2+ channels) | Included |
| V2X readiness | Prepared (interface available) |
| High-speed data recording | Included |

### 4.3 Compute Requirements

| Resource | Utilization |
|----------|-------------|
| CPU (4x A72) | ~70% (multi-pipeline + fusion + planning) |
| AI accelerator (C7x+MMA, enhanced) | ~80% (4+ concurrent DNNs) |
| Safety MCU (R5F, dual) | ~50% (actuator arbitration, sensor monitoring) |
| Memory | 4-8GB LPDDR4x |
| Storage | 32GB eMMC + MicroSD |
| CSI-2 bandwidth | 8+ lanes (multiple deserializers) |
| Ethernet bandwidth | 100Mbps (sensor data streaming) |

### 4.4 Target Applications

- Premium OEM Level 2+ systems
- Autonomous driving development platforms
- High-end fleet safety (construction, mining)
- Robotaxi safety monitoring
- Sensor fusion research and development

---

## 5. Tier Comparison Summary

| Attribute | Entry | Mid | High |
|-----------|-------|-----|------|
| SoC | AM62A | AM68A/TDA4VM | TDA4VH |
| TOPS | <1 | 8 | 32 |
| Cameras | 1 | 2 | 4-8 |
| Power | <5W | 10-15W | 20-30W |
| Cooling | None/passive | Passive heatsink | Active fan/TEC |
| CAN channels | 1 | 1 | 2+ |
| Ethernet | No | No | Yes |
| GNSS | Optional | Yes | Yes |
| IMU | No | Yes | Yes |
| Radar | No | No | Yes |
| BOM Relative | 0.5x | 1.0x (baseline) | 1.8x |

---

## 6. Migration Paths

### 6.1 Entry to Mid Upgrade

- Replace SOM module (AM62A to AM68A)
- Populate forward camera port components
- Populate GNSS and IMU components
- Populate IR interface
- Update firmware configuration profile
- No PCB redesign required

### 6.2 Mid to High Upgrade

- Replace SOM module (AM68A to TDA4VH)
- Add secondary deserializer and camera ports
- Add secondary CAN transceiver
- Add Ethernet PHY
- Install active cooling solution
- Larger enclosure may be required
- Carrier PCB revision may be needed (additional routing)

### 6.3 Software Portability

All ADVIS tiers share:
- Common Linux BSP foundation (TI Processor SDK)
- TIDL runtime for AI inference (models portable across tiers)
- Common HAL (Hardware Abstraction Layer) for peripherals
- Same configuration management system
- Over-the-air update infrastructure

---

*ADVIS Hardware Platform - OEM Customization*
