# ADVIS Product Variant Matrix

## 1. Overview

This matrix maps every hardware subsystem, feature, and capability against the four ADVIS product variants. Use this document to understand what is included, optional, or excluded in each product configuration.

## 2. Product Variant Summary

| Attribute | ADVIS Assist | ADVIS Control | ADVIS Fleet | ADVIS Fusion |
|-----------|-------------|---------------|-------------|--------------|
| **Phase** | Phase 1 | Phase 1 | Parallel (commercial) | Phase 2 (future) |
| **Target Market** | OEM L1/L2 | OEM L2/L2+ | Fleet/aftermarket | OEM premium |
| **Sensor Set** | Forward + DMS | Forward + DMS | Forward + DMS (later radar) | Camera + DMS + radar |
| **SoC Tier** | Mid (AM68A/TDA4VM) | Mid (AM68A/TDA4VM) | Mid (AM68A/TDA4VM) | High (TDA4VH) |
| **Safety Level** | QM (observation) | QM (request output) | QM (logging) | QM (request output) |
| **Cost Tier** | Standard | Standard | Standard | Premium |

---

## 3. Hardware Subsystem Matrix

| Subsystem / Component | ADVIS Assist | ADVIS Control | ADVIS Fleet | ADVIS Fusion |
|-----------------------|:---:|:---:|:---:|:---:|
| **Compute** | | | | |
| AM68A/TDA4VM SOM | YES | YES | YES | - |
| TDA4VH SOM | - | - | - | YES |
| AI accelerator (8 TOPS) | YES | YES | YES | - |
| AI accelerator (32 TOPS) | - | - | - | YES |
| **Camera Interface** | | | | |
| DS90UB954-Q1 (primary) | YES | YES | YES | YES |
| DS90UB954-Q1 (secondary) | - | - | - | YES |
| FPD-Link III Port 0 (Forward) | YES | YES | YES | YES |
| FPD-Link III Port 1 (DMS) | YES | YES | YES | YES |
| FPD-Link III Port 2-3 (Side/Rear) | - | - | - | YES |
| PoC (Power over Coax) | YES | YES | YES | YES |
| **Power** | | | | |
| LM61460-Q1 (5V buck) | YES | YES | YES | YES |
| TPS62130A-Q1 (3.3V buck) | YES | YES | YES | YES |
| TLV75518-Q1 (1.8V LDO) | YES | YES | YES | YES |
| 80V PMOS protection | YES | YES | YES | YES |
| TVS + fuse input protection | YES | YES | YES | YES |
| Active cooling support | - | - | - | YES |
| **Supervision / Safety** | | | | |
| TPS3808G33-Q1 (supervisor) | YES | YES | YES | YES |
| TPS3431-Q1 (watchdog) | YES | YES | YES | YES |
| SOM_BOOT_OK handshake | YES | YES | YES | YES |
| **CAN Interface** | | | | |
| TCAN1044AV-Q1 (primary) | YES | YES | YES | YES |
| TCAN1044AV-Q1 (secondary) | - | - | - | YES |
| CAN termination (120R DNI) | OPT | OPT | OPT | YES |
| Wake pattern detection | - | OPT | - | OPT |
| **Navigation / Inertial** | | | | |
| NEO-M9N-00B (GNSS) | YES | YES | YES | YES |
| GNSS active antenna bias | YES | YES | YES | YES |
| 1PPS timing output | YES | YES | YES | YES |
| BMI088 (IMU) | YES | YES | - | YES |
| Dead reckoning fusion | YES | YES | - | YES |
| **Connectivity** | | | | |
| USB-C (device mode) | YES | YES | YES | YES |
| UART debug console | YES | YES | YES | YES |
| MicroSD slot | YES | YES | YES | YES |
| Automotive Ethernet (100BASE-T1) | - | - | - | YES |
| **IR Illumination** | | | | |
| IR daughterboard connector | YES | YES | YES | YES |
| IR_EN control | YES | YES | YES | YES |
| IR_FAULT_N monitoring | YES | YES | YES | YES |
| **Radar Interface** | | | | |
| Radar data input (CAN/SPI) | - | - | OPT (Phase 2) | YES |
| Radar object fusion | - | - | - | YES |

Legend: **YES** = Included, **OPT** = Optional/configurable, **-** = Not included

---

## 4. Feature / Function Matrix

| Feature | ADVIS Assist | ADVIS Control | ADVIS Fleet | ADVIS Fusion |
|---------|:---:|:---:|:---:|:---:|
| **Forward Camera ADAS** | | | | |
| Forward Collision Warning (FCW) | YES | YES | - | YES |
| Lane Departure Warning (LDW) | YES | YES | - | YES |
| Traffic Sign Recognition (TSR) | YES | YES | - | YES |
| Pedestrian/Cyclist Warning (PCW) | YES | YES | - | YES |
| Headway monitoring | YES | YES | - | YES |
| **Active Safety Requests** | | | | |
| AEB request output | - | YES | - | YES |
| ACC request output | - | YES | - | YES |
| LKA request output | - | YES | - | YES |
| Speed moderation request | - | YES | - | YES |
| **Driver Monitoring (DMS)** | | | | |
| Drowsiness detection | YES | YES | YES | YES |
| Distraction detection | YES | YES | YES | YES |
| Phone use detection | YES | YES | YES | YES |
| Seatbelt detection | OPT | OPT | YES | OPT |
| Driver identification | - | - | YES | - |
| Driver-aware speed moderation | - | YES | - | YES |
| **Fleet Features** | | | | |
| Driver behavior scoring | - | - | YES | - |
| Event recording (video clips) | - | - | YES | OPT |
| Trip logging | - | - | YES | - |
| Fleet reporting interface | - | - | YES | - |
| Harsh braking/acceleration detection | - | - | YES | - |
| **Sensor Fusion** | | | | |
| Camera + IMU fusion | YES | YES | - | YES |
| Camera + GNSS fusion | YES | YES | YES | YES |
| Camera + radar fusion | - | - | - | YES |
| Blind-spot detection | - | - | - | YES |
| Moving-off detection | - | - | - | YES |
| 360-degree perception | - | - | - | YES |
| **System Features** | | | | |
| OTA firmware update | YES | YES | YES | YES |
| Diagnostic interface (UDS) | YES | YES | YES | YES |
| Event data recorder | OPT | YES | YES | YES |
| CAN bus logging | YES | YES | YES | YES |
| GNSS dead reckoning | YES | YES | - | YES |

Legend: **YES** = Standard, **OPT** = Optional, **-** = Not available

---

## 5. Interface Requirements by Variant

| Interface | ADVIS Assist | ADVIS Control | ADVIS Fleet | ADVIS Fusion |
|-----------|-------------|---------------|-------------|--------------|
| Vehicle CAN (input) | 1 channel, monitor | 1 channel, bidirectional | 1 channel, monitor | 2 channels, bidirectional |
| Actuation CAN (output) | - | Shared on CAN0 | - | Dedicated CAN1 |
| Camera coax (FPD-Link) | 2 cables | 2 cables | 2 cables | 4+ cables |
| GNSS antenna | 1x active | 1x active | 1x active | 1x active |
| Power input | 12V, <2A typical | 12V, <2A typical | 12V, <2A typical | 12V, <3A typical |
| USB (service) | 1x USB-C | 1x USB-C | 1x USB-C | 1x USB-C |
| Ethernet | - | - | - | 1x 100BASE-T1 |
| IR interface | 4-pin connector | 4-pin connector | 4-pin connector | 4-pin connector |

---

## 6. Certification Requirements by Variant

| Certification | ADVIS Assist | ADVIS Control | ADVIS Fleet | ADVIS Fusion |
|---------------|:---:|:---:|:---:|:---:|
| AEC-Q100 (component level) | YES | YES | YES | YES |
| ISO 16750 (environmental) | YES | YES | YES | YES |
| CISPR 25 Class 5 (EMC) | YES | YES | YES | YES |
| ISO 11452 (immunity) | YES | YES | YES | YES |
| ISO 26262 (functional safety) | QM | ASIL-B(D) system | QM | ASIL-B(D) system |
| Euro NCAP protocol | YES | YES | - | YES |
| E-Mark (ECE R10) | YES | YES | YES | YES |
| UN R130 (LDWS) | YES | YES | - | YES |
| UN R131 (AEBS) | - | YES | - | YES |
| FCC/CE (radio) | YES | YES | YES | YES |

*Note: ASIL-B(D) denotes hardware at QM with ASIL-B system-level decomposition, where ADVIS provides the request and OEM provides the ASIL-rated actuator.*

---

## 7. Thermal and Mechanical by Variant

| Parameter | ADVIS Assist | ADVIS Control | ADVIS Fleet | ADVIS Fusion |
|-----------|-------------|---------------|-------------|--------------|
| Typical power dissipation | 12W | 14W | 10W | 22W |
| Maximum power dissipation | 18W | 20W | 15W | 30W |
| Cooling method | Passive (heatsink) | Passive (heatsink) | Passive (heatsink) | Active (fan/TEC) |
| Operating temp range | -40 to +85C | -40 to +85C | -40 to +85C | -40 to +85C |
| Enclosure size | Standard | Standard | Standard | Extended |
| Weight target | <300g | <300g | <300g | <500g |
| Mounting | 4x M3 | 4x M3 | 4x M3 | 6x M3 |

---

*ADVIS Hardware Platform - OEM Customization*
