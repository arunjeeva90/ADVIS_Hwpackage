# ADVIS v0.5 Direct MIPI CSI-2 Signal Flow

**Classification:** CONFIDENTIAL - ENGINEERING USE ONLY  
**Status:** PRELIMINARY - Subject to vendor/datasheet confirmation  
**Version:** v0.1 - June 2026  
**Document ID:** ARCH-SIG-002

---

## 1. Overview

This document defines the signal flow architecture for the ADVIS v0.5 Compact Module. The v0.5 architecture uses direct MIPI CSI-2 connections from image sensors to the SoC, eliminating the FPD-Link III SerDes subsystem present in v0.4.4. This significantly reduces BOM cost, board area, and signal path complexity.

**Safety boundary:** ADVIS does not directly actuate brake, steering, throttle or powertrain. ADVIS Assist provides warning/advisory outputs. ADVIS Control may generate perception-validated, safety-supervised actuation request messages over CAN/CAN-FD, depending on OEM integration. Final actuator authority, arbitration and vehicle-level safety release remain with the OEM brake, EPS and powertrain ECUs.

---

## 2. Signal Flow Block Diagram

```
+==================+     Direct MIPI CSI-2       +===================+
| FORWARD CAMERA   |     (PCB traces or short    |                   |
| SENSOR MODULE    |      FPC)                   |   SoC             |
|                  |                              |   (TDA4VL/TDA4VM/ |
| [Image Sensor]   |=====[CSI-2 Port 0]==========|    AM62A/J722S)   |
| IMX390/OX03C10/  |  CLK_P/N + D0_P/N...D3_P/N |                   |
| AR0233/AR0234    |  (2-lane or 4-lane)         |  [ISP/VPAC]       |
|                  |                              |  [C7x DSP]       |
| [I2C Slave]      |<----[I2C Bus 0]-------------|  [MMA (if avail)] |
| (Sensor Config)  |  SCL0 + SDA0 (400kHz)       |  [ARM Cortex]    |
|                  |                              |                   |
| [XCLK Input]     |<----[MCLK0]-----------------|  [Clock Gen]     |
| (24/27 MHz ref)  |  (SoC timer or oscillator)  |                   |
|                  |                              |                   |
| [RESET_N]        |<----[GPIO_FWD_RST_N]--------|  [GPIO]          |
| [PWDN]           |<----[GPIO_FWD_PWDN]---------|                   |
+==================+                              |                   |
                                                  |                   |
+==================+     Direct MIPI CSI-2       |                   |
| DMS CAMERA       |     (~5cm flex/rigid-flex)   |                   |
| SENSOR MODULE    |                              |                   |
|                  |=====[CSI-2 Port 1]==========|                   |
| [Image Sensor]   |  CLK_P/N + D0_P/N + D1_P/N |                   |
| OX01N1B/OX01H1B/ |  (2-lane)                   |                   |
| AR0144/RGB-IR    |                              |                   |
|                  |                              |                   |
| [I2C Slave]      |<----[I2C Bus 1]-------------|                   |
| (Sensor Config)  |  SCL1 + SDA1 (400kHz)       |                   |
|                  |                              |                   |
| [XCLK Input]     |<----[MCLK1]-----------------|                   |
| (24/27 MHz ref)  |                              |                   |
|                  |                              |                   |
| [RESET_N]        |<----[GPIO_DMS_RST_N]--------|                   |
| [PWDN]           |<----[GPIO_DMS_PWDN]---------|                   |
+==================+                              +===================+
                                                         |    |
                         +-------------------------------+    |
                         |                                    |
                         v                                    v
               +------------------+                 +------------------+
               | CAN-FD SUBSYSTEM |                 | SAFETY SUBSYSTEM |
               |                  |                 |                  |
               | SoC MCAN ------->| TXD             | TPS3431 WDG     |
               | SoC MCAN <-------| RXD             |  WDI <--- SoC   |
               |                  |                 |  BOOT_OK <-- SoC |
               | TCAN1044AV-Q1   |                 |  RST_OUT --> SoC |
               |  CAN_H =====> J100               |                  |
               |  CAN_L =====> J100               | TPS3808 SUPV    |
               +------------------+                 |  RESET_N --> SoC |
                                                    +------------------+
```

---

## 3. Forward Camera MIPI CSI-2 Signal Path

### 3.1 Physical Layer Specification

| Parameter | Specification |
|-----------|---------------|
| Interface standard | MIPI CSI-2, D-PHY v1.2+ |
| Lane configuration | 2-lane (entry) or 4-lane (full bandwidth) |
| Data rate per lane | Up to 2.5 Gbps (D-PHY v1.2) |
| Aggregate bandwidth (4-lane) | Up to 10 Gbps |
| Aggregate bandwidth (2-lane) | Up to 5 Gbps |
| Impedance | MIPI D-PHY differential impedance target: TBD by selected SoC datasheet, selected sensor datasheet, connector/flex design and PCB stackup. Preliminary planning range: 90-100 ohm differential. Final value to be locked after stackup and SI review. |
| Signal levels | LP: 0-1.2V; HS: 100-300 mV differential |
| Trace routing | Sensor to SoC, PCB traces (no cable) |
| Maximum trace length | 50mm recommended (PCB) |
| AC coupling | Not required for direct PCB connection (sensor to SoC on same board) |

### 3.2 Routing Constraints (Forward Camera)

| Constraint | Requirement |
|------------|-------------|
| Intra-pair skew (P vs N within one lane) | Less than 0.2mm |
| Inter-lane skew (lane-to-lane) | Less than 1.5mm |
| Clock-to-data skew | Less than 1.0mm |
| Differential pair spacing | Minimum 3x trace width (isolation) |
| Ground reference | Continuous ground plane, no splits under MIPI |
| Via count | 0 preferred; maximum 1 via pair per lane |
| Guard traces | Recommended between MIPI lanes and other high-speed signals |
| Keepout from power inductors | Minimum 3mm from switching nodes |
| Trace width / spacing (90-100 ohm range) | Per stackup calculation (typ. 3.5/4.5 mil on 4-mil dielectric) |

### 3.3 Forward Camera Connector (if not rigid-mount)

| Parameter | Specification |
|-----------|---------------|
| Connector type | 0.3mm pitch FPC connector (24-40 pin) |
| FPC length | Less than 20mm (forward camera on same side as SoC) |
| FPC impedance | MIPI D-PHY differential impedance target: TBD by selected SoC datasheet, selected sensor datasheet, connector/flex design and PCB stackup. Preliminary planning range: 90-100 ohm differential. Final value to be locked after stackup and SI review. |
| FPC layer count | 2-layer minimum (signal + ground reference) |

---

## 4. DMS Camera MIPI CSI-2 Signal Path

### 4.1 Physical Layer Specification

| Parameter | Specification |
|-----------|---------------|
| Interface standard | MIPI CSI-2, D-PHY v1.2+ |
| Lane configuration | 2-lane (1MP DMS sensor is bandwidth-adequate at 2-lane) |
| Data rate per lane | Up to 1.5 Gbps (typical for 1MP @ 30fps RAW10) |
| Aggregate bandwidth (2-lane) | Up to 3 Gbps (sufficient for 1MP RAW10 @ 30fps) |
| Impedance | MIPI D-PHY differential impedance target: TBD by selected SoC datasheet, selected sensor datasheet, connector/flex design and PCB stackup. Preliminary planning range: 90-100 ohm differential. Final value to be locked after stackup and SI review. |
| Connection method | ~5cm rigid-flex or flex cable |
| Maximum flex length | 50mm (target); 80mm absolute maximum |

### 4.2 DMS Flex Cable Specification

| Parameter | Specification |
|-----------|---------------|
| Cable type | Rigid-flex (preferred) or controlled-impedance FPC |
| Layer count | 4-layer rigid-flex (Sig-Gnd-Gnd-Sig) or 2-layer FPC |
| Impedance control | MIPI D-PHY differential impedance target: TBD by selected SoC datasheet, selected sensor datasheet, connector/flex design and PCB stackup. Preliminary planning range: 90-100 ohm differential. Final value to be locked after stackup and SI review. |
| Signals carried | CSI-2 CLK (P/N), D0 (P/N), D1 (P/N), I2C (SCL, SDA), XCLK, RST_N, PWDN, VDD_SENSOR, VDDIO, GND |
| Total conductors | ~20 conductors minimum |
| Connector (PCB side) | 0.3mm pitch FPC ZIF connector or board-to-board |
| Connector (DMS side) | Soldered to DMS sensor PCBlet or direct bond |
| Bend radius | Minimum 1mm for single bend |
| Flex cycles | 0 (static installation, no repeated flexing) |
| Shielding | Ground plane layer provides EMI shielding |

### 4.3 Routing Constraints (DMS Camera)

| Constraint | Requirement |
|------------|-------------|
| Intra-pair skew (on flex) | Less than 0.5mm |
| Inter-lane skew (on flex) | Less than 2.0mm |
| Flex impedance tolerance | +/- 15% (relaxed vs. rigid PCB) |
| Ground continuity | Unbroken ground reference through flex transition |
| Connector transition | Length-compensate at connector pads |
| ESD protection | TVS on MIPI lanes at connector boundary (if connector used) |

---

## 5. I2C Camera Configuration Paths

### 5.1 I2C Bus 0 (Forward Camera)

| Parameter | Specification |
|-----------|---------------|
| Bus speed | 400 kHz (Fast Mode) |
| Pull-up resistors | 2.2k ohm to VDDIO_SENSOR (1.8V) |
| Sensor I2C address | Per sensor datasheet (7-bit, configurable via strap pins) |
| Bus loading | Single device (sensor only) |
| Trace length | Less than 30mm (on-board) |
| Usage | Sensor register programming, mode configuration, status readback |

### 5.2 I2C Bus 1 (DMS Camera)

| Parameter | Specification |
|-----------|---------------|
| Bus speed | 400 kHz (Fast Mode) |
| Pull-up resistors | 2.2k ohm to VDDIO_SENSOR (1.8V), on DMS PCBlet |
| Sensor I2C address | Per sensor datasheet (must differ from FWD if shared bus fallback) |
| Bus loading | Single device (sensor only) |
| Trace length | Less than 80mm total (PCB + flex) |
| Usage | Sensor register programming, DMS mode config, NIR sync setup |

---

## 6. Camera Clock (XCLK/MCLK) Paths

| Parameter | MCLK0 (Forward) | MCLK1 (DMS) |
|-----------|-----------------|--------------|
| Source | SoC timer output or external oscillator | SoC timer output or external oscillator |
| Frequency | 24 MHz or 27 MHz (sensor-dependent) | 24 MHz or 27 MHz (sensor-dependent) |
| Signal type | Single-ended LVCMOS | Single-ended LVCMOS |
| Drive strength | 4-8 mA | 4-8 mA |
| Trace impedance | 50 ohm single-ended (if length over 20mm) | 50 ohm single-ended (on flex) |
| Series termination | 33 ohm at source (if needed for SI) | 33 ohm at source |
| Jitter requirement | Less than 100 ps RMS | Less than 100 ps RMS |

---

## 7. Camera Control GPIO Paths

| Signal | Direction | Logic Level | Purpose |
|--------|-----------|-------------|---------|
| GPIO_FWD_RST_N | SoC to FWD sensor | 1.8V, active-low | Forward sensor hardware reset |
| GPIO_FWD_PWDN | SoC to FWD sensor | 1.8V, active-high | Forward sensor power-down |
| GPIO_DMS_RST_N | SoC to DMS sensor | 1.8V, active-low | DMS sensor hardware reset |
| GPIO_DMS_PWDN | SoC to DMS sensor | 1.8V, active-high | DMS sensor power-down |
| IR_EN | SoC to IR LED driver | 3.3V, active-high | Enable IR illumination (sync to DMS frame) |
| IR_FAULT_N | IR driver to SoC | 3.3V, active-low open-drain | IR LED fault indication |

---

## 8. CAN-FD Signal Path

### 8.1 Logic Side (SoC to PHY)

| Parameter | Specification |
|-----------|---------------|
| Signals | TXD (SoC to PHY), RXD (PHY to SoC) |
| Voltage levels | 3.3V CMOS |
| SoC interface | MCAN controller (integrated in SoC) |
| Pull-up | TXD internal pull-up to recessive |
| Standby control | CAN_STB GPIO from SoC (active-low for standby) |

### 8.2 Bus Side (PHY to Vehicle)

| Parameter | Specification |
|-----------|---------------|
| Standard | ISO 11898-2 (CAN-FD physical layer) |
| Data rate | Arbitration: 500 kbps, Data phase: up to 5 Mbps |
| Signals | CAN_H, CAN_L (differential pair) |
| Termination | 120 ohm split termination (60 + 60 ohm with 4.7nF to GND), DNI option |
| ESD protection | IEC 61000-4-2 Level 4 (contact +/-8kV) |
| Connector | Via J100 vehicle harness |
| Common-mode choke | Optional, for EMC margin |

---

## 9. Safety Supervisor Signal Paths

| Signal | Source | Destination | Description |
|--------|--------|-------------|-------------|
| WDI | SoC GPIO | TPS3431 WDI pin | Watchdog kick pulse (periodic toggle) |
| BOOT_OK | SoC GPIO | TPS3431 enable gate | Gates watchdog start until boot complete |
| WDG_RST_N | TPS3431 RESET output | SoC reset input | Watchdog timeout triggers system reset |
| POR_RST_N | TPS3808 RESET_N | SoC reset input | Power-on reset, 3.3V rail monitor |
| RESET_N (combined) | Wired-OR of WDG + POR | SoC PORz input | Combined reset (open-drain, pull-up to VDD) |

---

## 10. IR Illumination Signal Path

| Parameter | Specification |
|-----------|---------------|
| IR LED wavelength | 850nm or 940nm (TBD per sensor selection) |
| LED count | 2-4 LEDs (per illumination coverage requirement) |
| Driver IC | Constant-current LED driver (TBD part number) |
| Enable signal | IR_EN (SoC GPIO, 3.3V logic, active-high) |
| PWM dimming | IR_PWM (SoC timer output, 3.3V, 1-100 kHz) |
| Fault feedback | IR_FAULT_N (open-drain, active-low, pulled up to 3.3V) |
| Synchronization | IR_EN toggled in phase with DMS frame exposure (strobe mode) |
| Power supply | Fed from 5V_SYS via LED driver |
| Typical LED current | 100-500 mA per LED (pulsed, duty-cycle limited) |
| Thermal consideration | LEDs mounted near DMS optical window, thermally coupled to housing |

---

## 11. Optional Subsystem Signal Paths (DNI by Default)

### 11.1 GNSS (Fleet/Fusion Variant Only)

| Parameter | Specification |
|-----------|---------------|
| Device | u-blox NEO-M9N or equivalent |
| Interface | UART (TX, RX) + PPS (GPIO) |
| Baud rate | 115200 bps default |
| PPS | 1 Hz, rising-edge aligned to UTC second |
| Antenna | Active patch antenna (integrated in housing or external via U.FL) |
| Population | DNI footprint; populated for Fleet/Fusion variants |

### 11.2 IMU (Fleet/Fusion Variant Only)

| Parameter | Specification |
|-----------|---------------|
| Device | Bosch BMI088 or equivalent |
| Interface | SPI (Mode 0, 10 MHz, dual chip-select) |
| Interrupts | INT_ACCEL, INT_GYRO (active-high to SoC GPIO) |
| Supply | 1.8V |
| Population | DNI footprint; populated for Fleet/Fusion variants |

---

## 12. Signal Integrity Budget (Direct MIPI)

### 12.1 Eye Diagram Budget (PRELIMINARY)

| Loss Contributor | Forward Camera (PCB) | DMS Camera (Flex) |
|------------------|---------------------|-------------------|
| PCB trace loss (FR4, 30mm) | ~0.5 dB | ~0.3 dB (PCB portion) |
| Flex cable loss (50mm) | N/A | ~1.0-1.5 dB |
| Connector loss (FPC ZIF) | ~0.2 dB (if used) | ~0.3 dB |
| Via transition | ~0.1 dB | ~0.2 dB |
| **Total insertion loss** | **~0.5-0.8 dB** | **~1.8-2.3 dB** |
| D-PHY budget available | ~4 dB (at 1.5 Gbps) | ~4 dB (at 1.5 Gbps) |
| **Margin** | **~3.2-3.5 dB** | **~1.7-2.2 dB** |

### 12.2 Crosstalk Mitigation

- Minimum 3x trace width spacing between adjacent MIPI differential pairs
- Ground guard traces between MIPI lanes and other high-speed signals (clock generators, switching regulators)
- No parallel routing of MIPI lanes alongside IR_PWM or switching node traces
- DMS flex cable ground plane provides inherent shielding

---

## 13. Signal Impedance Summary

| Signal | Impedance Target | Tolerance | Routing Type |
|--------|-----------------|-----------|--------------|
| MIPI CSI-2 (PCB) | TBD (preliminary planning range: 90-100 ohm differential) | TBD after stackup/SI review | Diff pair, length matched |
| MIPI CSI-2 (flex) | TBD (preliminary planning range: 90-100 ohm differential) | TBD after stackup/SI review | Controlled impedance flex |
| CAN bus (PCB) | 120 ohm differential | +/- 10% | Diff pair to connector |
| XCLK/MCLK | 50 ohm single-ended | +/- 15% | Controlled (if over 20mm) |
| I2C | No controlled impedance | N/A | Standard trace with pull-ups |
| GPIO | No controlled impedance | N/A | Standard trace |
| SPI (optional IMU) | 50 ohm single-ended | +/- 15% | Standard trace (short) |

---

## 14. Comparison: v0.4.4 vs v0.5 Signal Flow

| Aspect | v0.4.4 (SerDes Architecture) | v0.5 (Direct MIPI) |
|--------|------------------------------|---------------------|
| Camera-to-SoC hops | Sensor -> UB953 -> Coax -> UB954 -> CSI-2 -> SoM | Sensor -> CSI-2 -> SoC (direct) |
| Total latency (camera path) | ~2-3 frames additional SerDes latency | Near-zero additional latency |
| Signal path components | Serializer, cable, deserializer, level shifters | Direct trace or short flex only |
| BOM cost (camera interface) | High (UB953 x2 + UB954 + connectors + cables) | Very low (traces + flex connector) |
| Maximum camera distance | 15m (coaxial cable) | ~80mm (flex cable maximum) |
| Failure modes | Cable disconnect, PoC fault, SerDes lock loss | Flex fatigue (static mount mitigates) |
| EMC sensitivity | Low (SerDes is robust over cable) | Moderate (MIPI traces need careful layout) |
| I2C back-channel | Via SerDes I2C pass-through | Direct I2C bus (simpler, faster) |
| Debug / probe points | Accessible at cable connectors | Test pads on PCB only |

---

## 15. Power Sequencing for Camera Sensors

| Step | Action | Timing |
|------|--------|--------|
| 1 | Assert sensor PWDN (active-high) | Hold during power-up |
| 2 | Enable VDDA (analog supply, 2.8V) | t = 0 |
| 3 | Enable VDDIO (digital I/O, 1.8V) | t = 0 + 1ms |
| 4 | Enable VDDD (digital core, 1.2V if separate) | t = 0 + 2ms |
| 5 | Release PWDN (de-assert) | t = 0 + 5ms |
| 6 | Assert RESET_N (active-low pulse, 1ms) then release | t = 0 + 10ms |
| 7 | Wait for sensor internal PLL lock | t = 0 + 20ms (typical) |
| 8 | Begin I2C configuration | t = 0 + 25ms |
| 9 | Start MIPI streaming | After I2C config complete |

Note: Exact timing per sensor datasheet. Both cameras may be sequenced in parallel if on independent power domains, or sequentially if sharing rails.

---

## 16. Revision History

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| 0.1 | 2026-06 | Signal Integrity Team | Initial PRELIMINARY release for v0.5 direct-MIPI architecture |

---

*PRELIMINARY - All values subject to datasheet/vendor confirmation*

*End of Document*
