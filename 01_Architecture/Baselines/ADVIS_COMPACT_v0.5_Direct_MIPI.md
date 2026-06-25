# ADVIS v0.5 Compact Direct-MIPI Production-Cost-Down Module

**Classification:** Confidential - Engineering Use Only  
**Status:** Architecture Definition In Progress  
**Date:** July 2026

---

## 1. Purpose

The ADVIS v0.5 Compact Module is the production-cost-down architecture for a windshield-mounted dual-facing ADAS + DMS smart camera module. It is designed for high-volume OEM deployment with minimum bill-of-materials cost while maintaining full perception and safety-supervisor functionality.

---

## 2. Product Form Factor

- **Form:** Compact windshield-mounted module
- **Mounting:** Adhesive/bracket mount behind rearview mirror area or upper windshield
- **Cameras:** Two integrated cameras (forward road-facing + cabin-facing DMS)
- **Appearance:** Sleek, compact, OEM-grade finish suitable for passenger car interior

---

## 3. Architecture Overview

### 3.1 Camera Architecture

| Camera | Direction | Connection | Default |
|--------|-----------|-----------|---------|
| Forward road-facing | Outward through windshield toward road | Direct MIPI CSI-2 | Yes |
| Cabin-facing DMS | Inward toward driver/cabin | Direct MIPI CSI-2 (short flex or rigid-flex, approx. 5 cm) | Yes |

- **Direct MIPI CSI-2 is the default camera connection method**
- SerDes (DS90UB954, UB953, FPD-Link) is removed by default
- FPD-Link remains an optional add-back for remote-camera OEM variants only
- No FAKRA/HSD connectors by default
- No Power-over-Coax (PoC) network by default

### 3.2 DMS Camera Connection

- DMS camera may be offset by approximately 5 cm from the main PCB using a short flex or rigid-flex cable
- This allows the DMS camera to face the cabin while the forward camera faces through the windshield
- Flex connector carries MIPI CSI-2 data lanes, I2C control, reset, clock, and power

### 3.3 Compute

- **Shared SoC:** Single TDA4VL / TDA4VM / AM62A-class processor (direct mount or SiP)
- **Shared memory:** LPDDR4/LPDDR4X (2 GB minimum for entry tier, 4 GB for higher tiers)
- **Shared storage:** eMMC (16 GB minimum for entry tier, 32 GB for higher tiers)
- No SOM module - SoC is placed directly on carrier PCB (or as SiP) for cost reduction

### 3.4 Power Tree

- **Shared power:** 12V input with automotive protection (fuse, TVS, reverse polarity MOSFET)
- 12V to 5V buck converter (LM61460-Q1 class)
- 5V to 3.3V buck converter (TPS62130A-Q1 class)
- 3.3V to 1.8V LDO (TLV75518-Q1 class)
- Sensor-specific rails derived from 3.3V or 1.8V as required by selected imagers

### 3.5 Safety Supervisor

- **Shared watchdog:** TPS3431-Q1 (boot-gated, independent timeout)
- **Shared reset supervisor:** TPS3808G33-Q1 (monitors 3.3V rail)
- Same proven power-on/power-off sequence topology as v0.4.4

### 3.6 Vehicle Interface

- **CAN-FD:** TCAN1044AV-Q1 (shared bus interface, up to 5 Mbps)
- Supports advisory messages (ADVIS Assist) and actuation request messages (ADVIS Control)
- 120 ohm termination option (DNI for mid-bus nodes)

### 3.7 IR Illumination

- Integrated IR LED(s) for DMS NIR illumination (no external daughterboard connector)
- IR_EN control from SoC GPIO, synchronized to DMS frame capture
- IR_FAULT_N feedback for LED string health monitoring
- IR window with optical filter integrated into housing

---

## 4. Items Removed by Default (vs. v0.4.4)

| Item | Reason for Removal | Add-back Condition |
|------|-------------------|-------------------|
| DS90UB954-Q1 deserializer | Cameras are co-located, no long cable needed | Remote-camera OEM variant |
| UB953 serializers | No remote cameras by default | Remote-camera OEM variant |
| FAKRA/HSD connectors | No coaxial camera links by default | Remote-camera OEM variant |
| PoC inductors/filters | No power-over-coax needed | Remote-camera OEM variant |
| microSD card slot | eMMC sufficient for production | Never (debug via test pads) |
| USB-C connector | Not needed in production module | Never (UART via test pads) |
| Ethernet | Not needed for windshield module | Fleet gateway variant |
| Large debug headers | Board area reduction | Never (test pads instead) |
| SOM module connector | Direct SoC placement for cost | Never in compact form |

---

## 5. Items Retained from v0.4.4

| Item | Reason |
|------|--------|
| 12V input protection (fuse, TVS, PMOS) | Automotive electrical environment |
| CAN-FD transceiver (TCAN1044AV-Q1) | Vehicle communication required |
| Watchdog (TPS3431-Q1) | Safety supervisor, boot-gated |
| Reset supervisor (TPS3808G33-Q1) | Rail monitoring, POR generation |
| Power tree topology (5V/3.3V/1.8V) | Proven, validated in v0.4.4 |
| ESD protection on all external pins | Automotive ESD requirements |
| EMC filtering on power input | Automotive EMC requirements |
| Sensor power rails | Required for image sensors |
| IR LED control | DMS NIR illumination |

---

## 6. Optional Population (Variant-Dependent)

| Item | Variant | Notes |
|------|---------|-------|
| GNSS (NEO-M9N or equivalent) | Fleet / Fusion | DNI pads for non-fleet variants |
| IMU (BMI088 or equivalent) | Fleet / Fusion | DNI pads for non-fleet variants |
| SerDes add-back (DS90UB954) | Remote camera OEM variant | Separate PCB revision or mezzanine |
| Additional memory/storage | Higher tiers | BOM variant |
| Radar interface connector | Fusion variant | Reserved footprint |

---

## 7. Optical and Mechanical Architecture

### 7.1 Optical Path Separation

- Forward camera optical path: outward through windshield toward road scene
- DMS camera optical path: inward toward driver/cabin
- **Optical baffle** between forward and DMS paths to prevent:
  - IR leakage from DMS illuminator into forward camera
  - NIR reflection contamination
  - Stray light cross-talk
- Road-facing and cabin-facing optical axes are physically separated

### 7.2 Thermal Management

- Compact thermal spreader behind SoC area (aluminum or copper)
- Thermal path from SoC die to spreader via thermal pad/TIM
- Housing design allows limited convective cooling
- Thermal budget constrained by windshield-mount environment (solar load, enclosed air)

### 7.3 Housing Concept

- Plastic + aluminum hybrid housing
- Aluminum rear plate doubles as thermal spreader and structural element
- Plastic front/surround provides optical windows and IR filter mounting
- Windshield bracket attachment mechanism (adhesive pad + mechanical clip)
- Service cover or access panel for production test/calibration
- Sleek, compact OEM-grade appearance

---

## 8. Production Debug Strategy

- **No large debug headers** - replaced by test pads and service pads
- UART console available via fine-pitch test pads (pogo-pin accessible in fixture)
- JTAG/SWD available via test pads for factory programming
- CAN-FD connector remains (vehicle interface, also used for diagnostics)
- Board variant ID pins for production tester identification
- SoC ID EEPROM or ID resistor network for configuration readback
- Camera module ID read path via I2C

---

## 9. Design Constraints for v0.5

### 9.1 Cost-Down Principles

- No expensive flexibility unless explicitly marked optional/DNI
- No high-speed lane crossbar by default
- No runtime programmable PoC by default
- No multi-camera expansion beyond two cameras by default
- No universal support for every SoC on first PCB revision
- No heavy modular mezzanine system

### 9.2 Reserved Hooks (Low-Cost Provisions)

- SoC ID EEPROM or ID resistor network footprint
- Board variant ID pins
- Camera module ID read path (I2C)
- Calibration EEPROM / secure memory footprint
- DMS pod presence detect signal
- Optional level-shifter footprints (DNI)
- Strap resistor matrix footprints for configuration
- Production test pads on all critical nets

---

## 10. Open Items

| # | Item | Owner | Status |
|---|------|-------|--------|
| 1 | Final forward camera sensor selection | Systems | Open |
| 2 | Final DMS camera sensor selection | Systems | Open |
| 3 | SoC selection for compact board (TDA4VL/TDA4VM/AM62A) | Systems | Open |
| 4 | MIPI lane count per sensor | Systems/SoC | Open |
| 5 | SoC CSI port availability and mapping | SoC Lead | Open |
| 6 | DMS flex connector length and part number | Mechanical | Open |
| 7 | Optical baffle material and placement | Optical/Mech | Open |
| 8 | Thermal spreader material and size | Thermal | Open |
| 9 | Housing 3D model and bracket design | Mechanical | Open |
| 10 | PCB stackup for compact form factor | Layout | Open |
| 11 | Production test pad placement plan | Test/DFT | Open |
| 12 | IR LED selection and drive circuit | Electrical | Open |
| 13 | Image sensor power sequencing definition | Power | Open |
| 14 | Direct-MIPI signal integrity budget | SI Engineer | Open |
| 15 | Windshield mount thermal analysis | Thermal | Open |

---

## 11. Safety Boundary

ADVIS does not directly actuate brake, steering, throttle or powertrain.

ADVIS Assist provides warning/advisory outputs.

ADVIS Control may generate perception-validated, safety-supervised actuation request messages over CAN/CAN-FD, depending on OEM integration.

Final actuator authority, arbitration and vehicle-level safety release remain with the OEM brake, EPS and powertrain ECUs.

---

*End of Document*
