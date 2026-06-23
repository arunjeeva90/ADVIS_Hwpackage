# ADVIS High-Speed Routing Constraints

**Document ID:** ADVIS-PCB-HSRT-001  
**Version:** 0.1.0  
**Status:** Draft  
**Last Updated:** 2024-01-15

---

## 1. Purpose

This document defines routing constraints for all high-speed interfaces on the ADVIS ECU
carrier board. These constraints ensure signal integrity, EMC compliance, and reliable
operation across the automotive temperature range.

**Note:** This document defines constraint categories and target values. Exact routing
topology, layer transitions, and trace geometries are proprietary design implementation
details and are not disclosed here.

---

## 2. CSI-2 Interface (Camera Deserializer to SOM)

### 2.1 Interface Parameters

| Parameter | Value |
|-----------|-------|
| Configuration | 4 data lanes + 1 clock lane |
| Data Rate | Up to 2.5 Gbps per lane (CSI-2 v2.0) |
| Signaling | MIPI D-PHY differential |
| Target Impedance | 100 ohm differential |
| Reference Layer | GND1 (L2) |

### 2.2 Routing Constraints

| Constraint | Requirement | Notes |
|-----------|-------------|-------|
| Differential impedance | 100 ohm +/- 10% | Verified by TDR on test coupon |
| Intra-pair skew | < 0.15mm (within a diff pair) | P/N matched length |
| Inter-lane skew | < 0.5mm (between lanes) | All 4 data lanes matched to clock |
| Maximum trace length | Minimize (target < 50mm) | Shorter is better for jitter |
| Via transitions | Minimize (0-1 via pairs max) | Each via adds discontinuity |
| Guard spacing | >= 3x trace width from other signals | Crosstalk isolation |
| Reference plane | Continuous, unbroken GND beneath | No plane splits under diff pairs |
| AC coupling capacitors | Placed at transmitter end | Per MIPI Alliance routing guide |
| Termination | On-die (no external termination) | MIPI D-PHY self-terminated |

### 2.3 Keep-out Requirements

- No other signals routed parallel to CSI-2 pairs within isolation spacing
- No via stitching within the differential pair routing channel
- No power plane splits beneath the CSI-2 route path
- Ground plane must be continuous under entire CSI-2 path

---

## 3. FPD-Link III Interface (Camera to Deserializer)

### 3.1 Interface Parameters

| Parameter | Value |
|-----------|-------|
| Configuration | 2 input ports (Forward + DMS) |
| Data Rate | Up to 4.16 Gbps per port |
| Signaling | Differential, AC-coupled |
| Target Impedance | 100 ohm differential |
| Cable | Coaxial (external) |
| On-board | Connector to deserializer |

### 3.2 Routing Constraints

| Constraint | Requirement | Notes |
|-----------|-------------|-------|
| Differential impedance | 100 ohm +/- 10% | Matched to coax cable impedance |
| Trace length | Absolute minimum from connector to IC | Connector placement adjacent to deser |
| Connector ground return | Multiple ground vias at connector pad | Low-inductance return path |
| PoC bias network | Isolated from data path | High-frequency blocking required |
| ESD protection | At connector, before AC coupling | Fast-response TVS diodes |
| Reference plane | Continuous GND beneath entire path | No interruptions or splits |
| Via count | Zero (same-layer routing preferred) | Minimize impedance discontinuities |

### 3.3 Coax Connector Placement

- Coax connectors placed as close to DS90UB954-Q1 as physically possible
- Ground ring around connector footprint with via stitching
- No signal traces routed between connector and deserializer input pins

---

## 4. USB 2.0 Interface

### 4.1 Interface Parameters

| Parameter | Value |
|-----------|-------|
| Configuration | 1 port, device mode |
| Data Rate | 480 Mbps (High-Speed) |
| Signaling | Differential |
| Target Impedance | 90 ohm differential |
| Reference Layer | GND1 (L2) |

### 4.2 Routing Constraints

| Constraint | Requirement | Notes |
|-----------|-------------|-------|
| Differential impedance | 90 ohm +/- 10% | USB 2.0 specification |
| Intra-pair skew | < 0.15mm | Length-matched P/N |
| Maximum trace length | < 100mm recommended | Keep short for signal quality |
| Series resistors | 22 ohm at SOM end (if required) | Impedance matching |
| ESD protection | At USB-C connector | Before any components |
| Guard spacing | >= 2x trace width from other signals | Crosstalk prevention |
| Reference plane | Continuous GND beneath | No splits or voids |

### 4.3 USB-C Connector Notes

- CC1/CC2 resistors (5.1k) placed close to connector pins
- Shield ground through capacitor to CHASSIS_GND
- VBUS trace sized for maximum charging current (if applicable)

---

## 5. CAN-FD Interface

### 5.1 Interface Parameters

| Parameter | Value |
|-----------|-------|
| Configuration | 1 CAN-FD bus |
| Data Rate | Up to 5 Mbps (CAN-FD data phase) |
| Signaling | Differential (CAN_H/CAN_L) |
| Target Impedance | 120 ohm differential |
| Reference Layer | GND2 (L7) or local ground pour |

### 5.2 Routing Constraints

| Constraint | Requirement | Notes |
|-----------|-------------|-------|
| Differential impedance | 120 ohm +/- 10% | ISO 11898-2 specification |
| Intra-pair skew | < 1mm | Less critical than high-speed serial |
| Bus termination | 120 ohm split-term at board edge | Matched to bus characteristic impedance |
| Common-mode filter | At connector, before termination | EMC emission reduction |
| ESD protection | TVS at connector | Before any board traces |
| Isolation | Separated from high-speed digital | Prevent noise coupling |
| Guard traces | Ground guard on both sides | EMC containment |

### 5.3 CAN Layout Best Practices

- Transceiver (TCAN1044AV-Q1) placed close to vehicle connector
- Termination resistors at board edge (closest point to bus)
- CAN_H/CAN_L traces should not cross power supply switching nodes
- Common-mode choke oriented perpendicular to board edge

---

## 6. SPI Interface (BMI088 IMU)

### 6.1 Interface Parameters

| Parameter | Value |
|-----------|-------|
| Configuration | 4-wire SPI, dual chip-select |
| Clock Rate | Up to 10 MHz |
| Signaling | Single-ended, 3.3V CMOS |
| Target Impedance | 50 ohm (if > 50mm trace length) |

### 6.2 Routing Constraints

| Constraint | Requirement | Notes |
|-----------|-------------|-------|
| Clock integrity | Minimize stub length | Point-to-point preferred |
| Trace length matching | MISO/MOSI matched to +/- 5mm of CLK | Timing margin |
| Chip select routing | Independent traces, no shared stub | Dual-CS for accel/gyro |
| Decoupling | 100nF at BMI088 VDD pin | Within 2mm of pin |
| Ground return | Via adjacent to each signal via | Low-inductance return |

---

## 7. I2C Interface (DS90UB954 Configuration)

### 7.1 Routing Constraints

| Constraint | Requirement | Notes |
|-----------|-------------|-------|
| Pull-up resistors | Close to master (SOM end) | Single pull-up per line |
| Trace length | < 200mm total bus length | Capacitance budget |
| Bus capacitance | < 400pF total | I2C specification limit |
| Routing | Avoid parallel run with high-speed | Crosstalk sensitivity |
| Series resistors | Optional 33 ohm for ringing control | At slave end if needed |

---

## 8. General High-Speed Design Rules

### 8.1 Via Usage

| Rule | Requirement |
|------|-------------|
| Via stub length | Minimize via stubs on high-speed nets |
| Ground via proximity | Ground return via within 1mm of signal via |
| Via-in-pad | Only with via plugging (to avoid solder wicking) |
| Differential pair via | Transition as pair (both P and N same location) |

### 8.2 Return Path Continuity

| Rule | Requirement |
|------|-------------|
| Reference plane splits | Never route high-speed across a split |
| Layer transitions | Place ground via at layer change point |
| Plane void avoidance | No routing over areas without copper pour |
| Stitching via density | Every 10mm along board edge and around high-speed zones |

### 8.3 Crosstalk Prevention

| Rule | Requirement |
|------|-------------|
| 3W rule | Maintain 3x trace width center-to-center between sensitive pairs |
| Aggressor isolation | Power switching nodes separated from victim signals |
| Guard traces | Ground guard between CSI-2 and adjacent signals |
| Layer separation | High-speed signals not on adjacent inner layers |

---

## 9. Constraint Summary Table

| Interface | Z (ohm) | Skew | Max Length | Layer | Priority |
|-----------|---------|------|-----------|-------|----------|
| CSI-2 | 100 diff | 0.15mm | 50mm | L1 ref GND1 | Critical |
| FPD-Link III | 100 diff | N/A (point-to-point) | Minimum | L1 ref GND1 | Critical |
| USB 2.0 | 90 diff | 0.15mm | 100mm | L1 ref GND1 | High |
| CAN-FD | 120 diff | 1mm | N/A | L6/L8 ref GND2 | High |
| SPI (IMU) | 50 SE | 5mm | 100mm | L3/L6 | Medium |
| I2C | N/A | N/A | 200mm | L3/L6 | Low |

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1.0 | 2024-01-15 | -- | Initial high-speed routing constraints |
