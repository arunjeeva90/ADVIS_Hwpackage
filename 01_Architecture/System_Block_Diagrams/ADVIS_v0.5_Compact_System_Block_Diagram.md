# ADVIS v0.5 Compact System Block Diagram

**Classification:** CONFIDENTIAL - ENGINEERING USE ONLY  
**Status:** PRELIMINARY - Subject to vendor/datasheet confirmation  
**Version:** v0.1 - June 2026  
**Document ID:** ARCH-SBD-002

---

## 1. Overview

This document presents the top-level system block diagram for the ADVIS v0.5 Compact windshield-mounted module. The v0.5 architecture eliminates the SerDes subsystem and SOM module, using direct MIPI CSI-2 connections and on-board SoC placement for production cost-down.

**Safety boundary:** ADVIS does not directly actuate brake, steering, throttle or powertrain. ADVIS Assist provides warning/advisory outputs. ADVIS Control may generate perception-validated, safety-supervised actuation request messages over CAN/CAN-FD, depending on OEM integration. Final actuator authority, arbitration and vehicle-level safety release remain with the OEM brake, EPS and powertrain ECUs.

---

## 2. System Block Diagram

```
                        VEHICLE HARNESS (J100)
    ==============================================================
    | 12V_BAT | GND_RET | CAN_H | CAN_L | IGN | WAKE | SHLD    |
    ==============================================================
         |        |        |    |     |      |              |
         v        v        |    |     |      |              |
    +--------+  +----+     |    |     |      |              |
    | FUSE   |  |PGND|     |    |     |      |              |
    | 3A     |  | IN |     |    |     |      |              |
    +--------+  +----+     |    |     |      |              |
         |        |        |    |     |      |              |
         v        |        |    |     |      |              |
    +--------+    |        |    |     |      |              |
    | TVS    |    |        |    |     |      |              |
    | Clamp  |    |        |    |     |      |              |
    +--------+    |        |    |     |      |              |
         |        |        |    |     |      |              |
         v        |        |    |     |      |              |
    +---------+   |        |    |     |      |              |
    | PMOS    |   |        |    |     |      |              |
    | Rev-Pol |   |        |    |     |      |              |
    | (80V)   |   |        |    |     |      |              |
    +---------+   |        |    |     |      |              |
         |        |        |    |     |      |              |
         v        v        v    v     v      v              v
    +================================================================+
    |               ADVIS v0.5 COMPACT MODULE PCB                    |
    |                                                                 |
    |  +-----------------------+    +----------------------------+   |
    |  | POWER SUBSYSTEM       |    | VEHICLE COMM SUBSYSTEM     |   |
    |  |                       |    |                            |   |
    |  | LM61460-Q1  (12V->5V) |    | TCAN1044AV-Q1             |   |
    |  | TPS62130A-Q1(5V->3.3V)|    |   CAN-FD PHY              |   |
    |  | TLV75518-Q1 (3.3->1.8)|    |   (Normal Mode)           |   |
    |  | Sensor LDOs (1.2/2.8V)|    | 120ohm Split Term (DNI)   |   |
    |  | TPS3808 (SUPV)        |    +----------------------------+   |
    |  | TPS3431 (WDG)         |                                     |
    |  +-----------------------+    +----------------------------+   |
    |                               | IR ILLUMINATION SUBSYSTEM  |   |
    |                               |                            |   |
    |  +-----------------------+    | IR LED Array (850nm/940nm) |   |
    |  | FORWARD CAMERA (MIPI) |    | LED Driver IC              |   |
    |  |                       |    | IR_EN (GPIO from SoC)      |   |
    |  | Image Sensor           |    | IR_FAULT_N (feedback)      |   |
    |  | (IMX390/OX03C10/AR0233)|    +----------------------------+   |
    |  |                       |                                     |
    |  | CSI-2 2-lane or 4-lane|    +----------------------------+   |
    |  | Direct to SoC Port 0  |    | OPTIONAL SUBSYSTEMS (DNI)  |   |
    |  | I2C Config (400kHz)   |    |                            |   |
    |  | Lens + IR-cut filter  |    | GNSS: NEO-M9N (UART+PPS)  |   |
    |  +-----------------------+    | IMU: BMI088 (SPI)          |   |
    |                               | Radar I/F: Reserved pads   |   |
    |  +-----------------------+    +----------------------------+   |
    |  | DMS CAMERA (MIPI)     |                                     |
    |  |                       |    +----------------------------+   |
    |  | Image Sensor           |    | DEBUG / TEST (Pads Only)   |   |
    |  | (OX01N1B/OX01H1B/     |    |                            |   |
    |  |  AR0144/RGB-IR)       |    | UART Console (test pads)   |   |
    |  |                       |    | JTAG/SWD (test pads)       |   |
    |  | CSI-2 2-lane          |    | Board ID resistors         |   |
    |  | Direct to SoC Port 1  |    | SoC ID EEPROM footprint   |   |
    |  | I2C Config (400kHz)   |    +----------------------------+   |
    |  | ~5cm Flex/Rigid-Flex  |                                     |
    |  | NIR-pass filter       |                                     |
    |  +-----------------------+                                     |
    |                                                                 |
    |  +==========================================================+  |
    |  |              SoC (DIRECT MOUNT ON PCB)                    |  |
    |  |       TDA4VL-Q1 / TDA4VM-Q1 / AM62A / J722S              |  |
    |  |                                                           |  |
    |  |  +--------+  +-------+  +------+  +-------+  +-------+  |  |
    |  |  |CSI-2   |  |CSI-2  |  | MCAN |  |UART x2|  |GPIO   |  |  |
    |  |  |Port 0  |  |Port 1 |  | FD   |  |(debug |  |(IR_EN |  |  |
    |  |  |(FWD)   |  |(DMS)  |  |      |  | +opt  |  | WDI   |  |  |
    |  |  |2/4-lane|  |2-lane |  |      |  | GNSS) |  | BOOT  |  |  |
    |  |  +--------+  +-------+  +------+  +-------+  | _OK)  |  |  |
    |  |                                               +-------+  |  |
    |  |  +--------+  +-------+  +------+  +-------+             |  |
    |  |  |ISP/VPAC|  |C7x DSP|  | MMA  |  |ARM    |             |  |
    |  |  |(Image  |  |(Vision|  |(Deep |  |Cortex |             |  |
    |  |  | Proc)  |  | Algos)|  |Learn)|  |A53/A72|             |  |
    |  |  +--------+  +-------+  +------+  +-------+             |  |
    |  |                                                           |  |
    |  |  +--------+  +------------------+  +-----------------+   |  |
    |  |  |I2C x2  |  | LPDDR4/4X        |  | eMMC            |   |  |
    |  |  |(Sensor |  | 2GB (Assist)     |  | 16GB (Assist)   |   |  |
    |  |  | Config)|  | 4GB (Control)    |  | 32GB (Control)  |   |  |
    |  |  +--------+  +------------------+  +-----------------+   |  |
    |  |                                                           |  |
    |  +==========================================================+  |
    |                                                                 |
    +================================================================+
```

---

## 3. Signal Interconnections Summary

| Source | Destination | Interface | Signals | Data Rate |
|--------|-------------|-----------|---------|-----------|
| Forward Camera Sensor | SoC CSI-2 Port 0 | Direct MIPI CSI-2 | 2 or 4 data + 1 clk lane | up to 2.5 Gbps/lane |
| DMS Camera Sensor | SoC CSI-2 Port 1 | Direct MIPI CSI-2 | 2 data + 1 clk lane | up to 2.5 Gbps/lane |
| SoC | Forward Sensor | I2C | SCL, SDA | 400 kHz |
| SoC | DMS Sensor | I2C | SCL, SDA | 400 kHz |
| SoC | TCAN1044AV-Q1 | CAN-FD | TXD, RXD | up to 5 Mbps |
| TCAN1044AV-Q1 | Vehicle (J100) | CAN Bus | CAN_H, CAN_L | up to 5 Mbps |
| SoC | IR LED Driver | GPIO | IR_EN, IR_PWM | Logic level |
| IR LED Driver | SoC | GPIO | IR_FAULT_N | Active-low |
| TPS3431 WDG | SoC | GPIO | WDI (kick input) | Pulse |
| SoC | TPS3431 | GPIO | BOOT_OK (gate enable) | Logic level |
| TPS3808 | SoC | Open-drain | RESET_N | Active-low |
| SoC | LPDDR4/4X | DDR | 16/32-bit bus | 3200 MT/s |
| SoC | eMMC | eMMC 5.1 | 8-bit data + CLK | HS400 |
| SoC | GNSS (opt) | UART | TX, RX | 115200 baud |
| GNSS (opt) | SoC | GPIO | PPS | 1 Hz pulse |
| SoC | IMU (opt) | SPI | SCLK, MOSI, MISO, CS | 10 MHz |
| SoC | Debug pads | UART | TX, RX | 115200 baud |

---

## 4. Key Differences vs. v0.4.4 Block Diagram

| Aspect | v0.4.4 (SerDes/SOM) | v0.5 (Compact Direct-MIPI) |
|--------|---------------------|----------------------------|
| Camera connection | FPD-Link III via DS90UB954 | Direct MIPI CSI-2 on-board |
| Compute module | SOM (e.g., phyCORE) | SoC direct-mounted on PCB |
| GNSS/IMU | Always populated | DNI pads (Fleet/Fusion variant only) |
| USB-C | Present (J300) | Removed (test pads for debug) |
| microSD | Present (J400) | Removed (eMMC only) |
| IR illumination | Via J800 daughterboard | Integrated on carrier PCB |
| Debug interface | Header (J500) | Test pads (pogo-pin fixture) |
| Camera connectors | FAKRA coaxial (J200, J201) | None (direct PCB-mount sensors) |
| Board size | Standard carrier for SOM | Compact (windshield-mount) |

---

## 5. Power Domain Mapping

### 5.1 Power Rails

| Rail | Voltage | Source | Loads |
|------|---------|--------|-------|
| 12V_BAT | 8-16V (nom 12V) | Vehicle battery via J100 | Protection stage input |
| 5V_SYS | 5.0V +/- 3% | LM61460-Q1 | SoC core PMIC input, IR LED driver |
| 3V3_IO | 3.3V +/- 3% | TPS62130A-Q1 | CAN PHY, sensor I/O, optional GNSS/IMU |
| 1V8_IO | 1.8V +/- 3% | TLV75518-Q1 | SoC I/O, DDR VDD1 |
| VDD_CORE | 0.75-0.85V | SoC PMIC (internal) | SoC core logic |
| VDDA_SENSOR | 2.8V (typ) | Dedicated LDO | Image sensor analog supply |
| VDDIO_SENSOR | 1.8V | Shared from 1V8_IO or LDO | Image sensor digital I/O |
| VDD_DDR | 1.1V | SoC PMIC or LDO | LPDDR4/4X |

### 5.2 Power Budget Targets by Product Tier

**Note:** Power values in ADVIS tier tables are module design targets, not official SoC power consumption values. Actual SoC power consumption requires per-use-case characterization from TI datasheet power tables or TI power estimation tools.

| Tier | SoC | Module Power Target (Typical) | Module Power (Absolute Max) | Thermal Strategy |
|------|-----|-------------------------------|-----------------------------|--------------------|
| ADVIS Assist | TDA4VL-Q1 | Less than 6W | Less than 8W | Standard compact thermal spreader |
| ADVIS Control | TDA4VM-Q1 | Less than 14W | Less than 18W | Large thermal spreader, DVFS management |
| Single-Camera (if applicable) | AM62A7 | Less than 5W | Less than 7W | Minimal thermal challenge |

*Note: SoC power figures are preliminary estimates based on TI product page power class descriptions. Final values require per-use-case characterization from TI datasheet power tables.*

---

## 6. Connector Reference

| Connector | Function | Type |
|-----------|----------|------|
| J100 | Vehicle harness (power, CAN, ignition, wake) | Automotive sealed (compact) |
| FPC-FWD | Forward camera sensor flex (if not rigid-mount) | 0.3mm pitch FPC |
| FPC-DMS | DMS camera sensor flex (~5cm rigid-flex) | 0.3mm pitch FPC |
| TP-UART | Debug UART access | Test pads (pogo-pin) |
| TP-JTAG | JTAG/SWD programming | Test pads (pogo-pin) |

---

## 7. Design Constraints

- All vehicle-facing signals must pass through ESD protection (minimum IEC 61000-4-2 Level 4)
- CAN bus must tolerate +/-58V fault per ISO 11898-2
- Direct MIPI CSI-2 traces must be length-matched within 0.5mm intra-pair, 2mm inter-pair
- DMS flex cable must maintain MIPI D-PHY differential impedance per final stackup/SI review (preliminary planning range: 90-100 ohm differential)
- Ground domains: single digital ground plane (no analog ground split on compact PCB)
- Total module power budget: target less than 8W at nominal for Assist tier (TDA4VL-Q1); target less than 15W for Control tier (TDA4VM-Q1); these are module design targets, not official SoC power consumption values; final values pending SoC datasheet power characterization
- Watchdog disabled during boot (BOOT_OK gates enable)
- SoC thermal pad must have direct thermal path to aluminum rear plate
- Optical baffle required between forward and DMS light paths

---

## 8. Thermal Architecture

```
    +-------------------+
    |  Windshield Glass |   (Solar load from exterior)
    +-------------------+
            |
    +-------------------+
    | Plastic Housing   |   (IR filter windows for cameras)
    | (Front Shell)     |
    +-------------------+
            |
    +---[PCB Assembly]--+
    |  FWD Sensor  |  DMS Sensor (via flex)
    |       |
    |  SoC + DDR + eMMC
    |       |
    |  Thermal Pad / TIM
    +-------------------+
            |
    +-------------------+
    | Aluminum Rear     |   (Thermal spreader + structural)
    | Plate / Bracket   |
    +-------------------+
            |
    +-------------------+
    | Adhesive Mount    |   (Thermal isolation from glass)
    +-------------------+
```

- SoC TDP target: TBD pending datasheet confirmation; preliminary estimate 3-5W class (TDA4VL) or 10-15W class (TDA4VM)
- Thermal spreader area: minimum 2x SoC package footprint
- TIM: graphite sheet or thermal pad (0.5-1.0 mm)
- Ambient operating range: -40C to +85C (junction max per SoC datasheet: 125C for TDA4VL, 105C for TDA4VM)

---

## 9. Visual Concept References

Conceptual 3D visualizations of this module are available for architecture communication:

- [Compact Board 3D View (isometric)](../Visual_Concepts/ADVIS_v0.5_Compact_Board_3D_View.svg) - Component placement and signal paths
- [Compact Module Exploded View](../Visual_Concepts/ADVIS_v0.5_Compact_Module_Exploded_View.svg) - Assembly stack and mechanical layers
- [3D View Description Document](../Visual_Concepts/ADVIS_v0.5_Compact_Board_3D_View.md) - Detailed element descriptions

These are conceptual visualizations only - not production layout, not mechanical CAD release.

---

## 10. Revision History

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| 0.1 | 2026-06 | Architecture Team | Initial PRELIMINARY release for v0.5 compact module |

---

*PRELIMINARY - All values subject to datasheet/vendor confirmation*

*End of Document*
