# ADVIS System Block Diagram

## Version
v1.0 - June 2026

## Document ID
ARCH-SBD-001

---

## 1. Overview

This document presents the top-level system block diagram for the ADVIS ECU platform. The diagram shows all major subsystems, their interconnections, signal types, and bus widths.

**Safety boundary:** ADVIS does not directly actuate brake, steering, throttle or powertrain. ADVIS Assist provides warning/advisory outputs. ADVIS Control may generate perception-validated, safety-supervised actuation request messages over CAN/CAN-FD, depending on OEM integration. Final actuator authority, arbitration and vehicle-level safety release remain with the OEM brake, EPS and powertrain ECUs.

---

## 2. System Block Diagram

```
                           VEHICLE HARNESS (J100)
    =====================================================================
    | 12V_BAT | GND_RET | CAN_H | CAN_L | IGN | WAKE | GNSS_ANT | SHLD |
    =====================================================================
         |        |        |    |     |      |       |         |
         v        v        |    |     |      |       |         |
    +--------+  +----+     |    |     |      |       |         |
    | FUSE   |  |PGND|     |    |     |      |       |         |
    | 5A     |  | IN |     |    |     |      |       |         |
    +--------+  +----+     |    |     |      |       |         |
         |        |        |    |     |      |       |         |
         v        |        |    |     |      |       |         |
    +--------+    |        |    |     |      |       |         |
    | TVS    |    |        |    |     |      |       |         |
    | Clamp  |    |        |    |     |      |       |         |
    +--------+    |        |    |     |      |       |         |
         |        |        |    |     |      |       |         |
         v        |        |    |     |      |       |         |
    +---------+   |        |    |     |      |       |         |
    | PMOS    |   |        |    |     |      |       |         |
    | Rev-Pol |   |        |    |     |      |       |         |
    | (80V)   |   |        |    |     |      |       |         |
    +---------+   |        |    |     |      |       |         |
         |        |        |    |     |      |       |         |
         v        v        v    v     v      v       v         v
    +================================================================+
    |                    ADVIS CARRIER BOARD                          |
    |                                                                 |
    |  +------------------+     +------------------+                  |
    |  | POWER SUBSYSTEM  |     | COMM SUBSYSTEM   |                  |
    |  |                  |     |                  |                  |
    |  | LM61460-Q1 (5V)  |     | TCAN1044AV-Q1   |                  |
    |  | TPS62130A (3.3V) |     |   CAN-FD PHY    |                  |
    |  | TLV75518 (1.8V)  |     | (Normal Mode)   |                  |
    |  | TPS3808 (SUPV)   |     +------------------+                  |
    |  | TPS3431 (WDG)    |                                          |
    |  +------------------+     +------------------+                  |
    |                           | GNSS SUBSYSTEM   |                  |
    |  +------------------+     |                  |                  |
    |  | CAMERA SUBSYSTEM |     | u-blox NEO-M9N   |                  |
    |  |                  |     | (UART + PPS)     |                  |
    |  | DS90UB954-Q1     |     +------------------+                  |
    |  | Dual FPD-Link III|                                          |
    |  | VC0=FWD, VC1=DMS |     +------------------+                  |
    |  +------------------+     | IMU SUBSYSTEM    |                  |
    |                           |                  |                  |
    |  +------------------+     | Bosch BMI088     |                  |
    |  | USB SUBSYSTEM    |     | (SPI, Dual CS)   |                  |
    |  |                  |     +------------------+                  |
    |  | USB-C Device     |                                          |
    |  | 5.1k CC pulldown |     +------------------+                  |
    |  +------------------+     | IR SUBSYSTEM     |                  |
    |                           |                  |                  |
    |                           | J800 Connector   |                  |
    |                           | (8-pin IR Board) |                  |
    |                           +------------------+                  |
    |                                                                 |
    |  +=========================================================+   |
    |  |               SoM MODULE (TDA4VM/AM68A)                 |   |
    |  |                                                         |   |
    |  |  [CSI-2 4L Rx] [I2C] [SPI] [UART x2] [CAN] [USB]     |   |
    |  |  [GPIO] [SD/MMC] [DDR] [eMMC] [AI Accelerator]        |   |
    |  |                                                         |   |
    |  +=========================================================+   |
    |                                                                 |
    +================================================================+
```

---

## 3. Signal Interconnections Summary

| Source | Destination | Interface | Signals | Data Rate |
|--------|------------|-----------|---------|-----------|
| Forward Camera | DS90UB954 RX0 | FPD-Link III | Coax (PoC) | up to 1.6 Gbps |
| DMS Camera | DS90UB954 RX1 | FPD-Link III | Coax (PoC) | up to 1.6 Gbps |
| DS90UB954 | SoM CSI-2 | MIPI CSI-2 | 4 data + 1 clk | up to 6 Gbps total |
| SoM | DS90UB954 | I2C | SCL, SDA | 400 kHz |
| SoM | BMI088 Accel | SPI | SCLK, MOSI, MISO, CS_A | 10 MHz |
| SoM | BMI088 Gyro | SPI | SCLK, MOSI, MISO, CS_G | 10 MHz |
| SoM | NEO-M9N | UART | TX, RX | 115200 baud |
| SoM | TCAN1044AV | CAN-FD | TXD, RXD | up to 5 Mbps |
| SoM | USB-C | USB 2.0 | D+, D- | 480 Mbps |
| SoM | microSD | SD 4-bit | CLK, CMD, DAT[3:0] | 50 MHz |
| SoM | IR Board (J800) | GPIO | IR_LED_EN, IR_PWM | Logic level |
| TPS3431 | SoM | GPIO | WDI (input to WDG) | Pulse |
| SoM | TPS3431 | GPIO | SOM_BOOT_OK | Logic level |
| TPS3808 | SoM | Open-drain | RESET_N | Active-low |
| NEO-M9N | SoM | GPIO | PPS | 1 Hz pulse |
| BMI088 | SoM | GPIO | INT_A, INT_G | Active-high |
| Vehicle | TCAN1044AV | Diff pair | CAN_H, CAN_L | up to 5 Mbps |

---

## 4. Connector Reference

| Connector | Function | Type |
|-----------|----------|------|
| J100 | Vehicle harness (power, CAN, ignition, wake, GNSS ant) | Automotive sealed |
| J200 | Forward camera FPD-Link III input | FAKRA coax |
| J201 | DMS camera FPD-Link III input | FAKRA coax |
| J300 | USB-C device port (engineering/service) | USB-C receptacle |
| J400 | microSD slot | Push-push card cage |
| J500 | Debug UART header | 1.27mm pin header |
| J800 | IR daughterboard | 8-pin board-to-board |
| J900 | SoM connector | High-density board-to-board |

---

## 5. Power Domain Mapping

| Rail | Voltage | Source | Loads |
|------|---------|--------|-------|
| 12V_BAT | 8-16V (nom 12V) | Vehicle battery | Protection stage input |
| 5V_SYS | 5.0V +/- 3% | LM61460-Q1 | SoM (PMIC input), USB VBUS option |
| 3V3_IO | 3.3V +/- 3% | TPS62130A-Q1 | DS90UB954, TCAN1044AV, NEO-M9N, level shifters |
| 1V8_IO | 1.8V +/- 3% | TLV75518-Q1 | BMI088, I/O level translation |

---

## 6. Design Constraints

- All vehicle-facing signals must pass through ESD protection (minimum IEC 61000-4-2 Level 4)
- CAN bus must tolerate +/-58V fault per ISO 11898-2
- FPD-Link III cables must maintain 100 ohm differential impedance
- CSI-2 traces must be length-matched to within 0.5mm per pair
- Ground domains must not mix (see Ground Domain Architecture document)
- Watchdog must be disabled during boot (SOM_BOOT_OK gates enable)

---

## 7. Revision History

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| 1.0 | 2026-06 | Architecture Team | Initial release |
