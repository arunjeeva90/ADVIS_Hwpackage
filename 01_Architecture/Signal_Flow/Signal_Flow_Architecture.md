# ADVIS Signal Flow Architecture

## Version
v1.0 - June 2026

## Document ID
ARCH-SIG-001

---

## 1. Overview

This document defines the signal flow architecture for the ADVIS ECU platform. It covers all inter-subsystem signal paths, their protocols, electrical characteristics, impedance targets, and routing requirements.

**Safety boundary:** ADVIS does not directly actuate brake, steering, throttle or powertrain. ADVIS Assist provides warning/advisory outputs. ADVIS Control may generate perception-validated, safety-supervised actuation request messages over CAN/CAN-FD, depending on OEM integration. Final actuator authority, arbitration and vehicle-level safety release remain with the OEM brake, EPS and powertrain ECUs.

---

## 2. Signal Flow Block Diagram

```
+--------+    FPD-Link III     +-----------+    CSI-2 4-Lane    +--------+
| FWD    |---(Coax, PoC)----->| DS90UB954 |----(MIPI D-PHY)--->|  SoM   |
| Camera |    RX0, VC0        | -Q1       |    CLK + D[3:0]    |        |
+--------+                    |           |                     |        |
                              | Dual Deser|    I2C Config       |        |
+--------+    FPD-Link III    |           |<---(SCL/SDA)--------|        |
| DMS    |---(Coax, PoC)----->|           |    400 kHz          |        |
| Camera |    RX1, VC1        +-----------+                     |        |
+--------+                                                      |        |
                                                                |        |
+--------+    UART             +--------+                       |        |
| NEO-   |<---(TX/RX)-------->|  SoM   |                       |        |
| M9N    |    115200 baud      |        |                       |        |
| GNSS   |----(PPS)---------->|        |                       |        |
+--------+    1Hz pulse        |        |                       |        |
                               |        |                       |        |
+--------+    SPI (Dual CS)    |        |                       |        |
| BMI088 |<---(SCLK/MOSI/     |        |                       |        |
| IMU    |    MISO/CS_A/CS_G)->|        |                       |        |
|        |----(INT_A)--------->|        |                       |        |
|        |----(INT_G)--------->|        |                       |        |
+--------+    10 MHz           +--------+                       |        |
                                                                |        |
+----------+   CAN-FD          +--------+                       |        |
| TCAN1044 |<--(TXD/RXD)------|  SoM   |                       |        |
| AV-Q1    |   Logic-level     |  CAN   |                       |        |
|          |                   |  Ctrl  |                       |        |
|          |===(CAN_H/CAN_L)==>| Vehicle|                       |        |
+----------+   Diff pair       +--------+                       |        |
                                                                |        |
+--------+    USB 2.0          +--------+                       |        |
| USB-C  |<---(D+/D-)-------->|  SoM   |                       |        |
| Conn   |    480 Mbps         |  USB   |                       |        |
+--------+                     +--------+                       +--------+
```

---

## 3. Camera Signal Path (FPD-Link III)

### 3.1 Physical Layer

| Parameter | Specification |
|-----------|---------------|
| Interface standard | TI FPD-Link III (DS90UB953 serializer to DS90UB954 deserializer) |
| Cable type | 50-ohm coaxial, automotive-grade shielded |
| Cable length | Maximum 15m (typical installation: 0.5m to 3m) |
| Data rate | Up to 1.6 Gbps per link |
| Power over Coax (PoC) | Carrier sources PoC voltage through DS90UB954 back-channel |
| Virtual channels | VC0 = Forward camera (RX0), VC1 = DMS camera (RX1) |
| Connector | FAKRA coaxial (Z-code or custom) |

### 3.2 CSI-2 Output (Deserializer to SoM)

| Parameter | Specification |
|-----------|---------------|
| Interface standard | MIPI CSI-2, D-PHY v1.2+ |
| Lane count | 4 data lanes + 1 clock lane |
| Lane data rate | Up to 1.5 Gbps per lane |
| Aggregate bandwidth | Up to 6 Gbps |
| Impedance | 100 ohm differential |
| Trace length matching | Within 0.5mm intra-pair, within 2mm inter-pair |
| AC coupling | 100nF capacitors on each lane (placed at receiver) |
| Signal routing | Must not cross ground plane splits |

### 3.3 I2C Configuration Path

| Parameter | Specification |
|-----------|---------------|
| Bus speed | 400 kHz (Fast Mode) |
| Pull-up resistors | 2.2k ohm to 3V3_IO |
| Address | DS90UB954 default 0x3D (7-bit) |
| Usage | Camera initialization, register programming, status readback |

---

## 4. GNSS Signal Path (UART)

| Parameter | Specification |
|-----------|---------------|
| Interface | UART (TTL-level, 3.3V) |
| Baud rate | 115200 bps (default), configurable to 921600 |
| Data format | 8N1 |
| Signals | TX (SoM to GNSS), RX (GNSS to SoM), PPS (GNSS to SoM GPIO) |
| PPS characteristics | 1 Hz, 100ms pulse width, rising-edge aligned to UTC second |
| GNSS antenna | Active, fed through J100 connector (DC bias through connector) |
| Protocol | UBX binary + NMEA ASCII (configurable) |

---

## 5. IMU Signal Path (SPI)

| Parameter | Specification |
|-----------|---------------|
| Interface | SPI Mode 0 (CPOL=0, CPHA=0) |
| Clock frequency | 10 MHz maximum |
| Chip selects | CS_ACCEL (accelerometer), CS_GYRO (gyroscope) |
| Data width | 8-bit SPI frames |
| Interrupts | INT_ACCEL (data ready), INT_GYRO (data ready) |
| Interrupt polarity | Active high, push-pull |
| SPI bus topology | Point-to-point (SoM is sole master) |
| BMI088 supply | 1.8V (VDD and VDDIO) |

### IMU Routing Considerations

- SPI clock trace must be guarded (ground on both sides)
- Keep SPI trace length under 50mm
- Interrupt lines require ESD protection if routed near board edge
- IMU placed away from vibration-inducing components (inductors, fans)

---

## 6. CAN-FD Signal Path

### 6.1 Logic Side (SoM to PHY)

| Parameter | Specification |
|-----------|---------------|
| Signals | TXD (SoM to PHY), RXD (PHY to SoM) |
| Voltage levels | 3.3V CMOS or 5V tolerant (PHY accepts both) |
| Pull-up | TXD has internal/external pull-up to recessive state |
| Standby control | CAN_STB GPIO from SoM (active-low to enter standby) |
| Default mode | Normal mode (STB pin pulled high) |

### 6.2 Bus Side (PHY to Vehicle)

| Parameter | Specification |
|-----------|---------------|
| Standard | ISO 11898-2 (CAN-FD physical layer) |
| Data rate | Arbitration: 500 kbps, Data phase: up to 5 Mbps |
| Signals | CAN_H, CAN_L (differential pair) |
| Termination | 120-ohm split termination (60 ohm + 60 ohm with 4.7nF to GND) |
| Common-mode range | -2V to +7V |
| Fault tolerance | +/-58V on bus pins |
| ESD protection | IEC 61000-4-2 Level 4 (contact +/-8kV) |
| Connector | Via J100 vehicle connector |

---

## 7. USB Signal Path

| Parameter | Specification |
|-----------|---------------|
| Interface | USB 2.0 (High-Speed, 480 Mbps) |
| Mode | Device mode (ADVIS acts as USB device to host tool) |
| Connector | USB-C receptacle (J300) |
| CC pull-downs | 5.1k ohm on each CC pin (device role advertisement) |
| ESD protection | Dedicated USB ESD array on D+/D- and CC/VBUS |
| Impedance | 90 ohm differential (D+/D-) |
| Cable length | Standard USB: up to 5m |
| Purpose | Engineering/service port (firmware update, log download, debug) |

---

## 8. IR Daughterboard Signal Path

| Parameter | Specification |
|-----------|---------------|
| Connector | J800 (8-pin board-to-board) |
| Power | 5V_SYS pass-through, current limited |
| IR_LED_EN | GPIO from SoM, active-high, enables IR LED driver |
| IR_PWM | PWM signal from SoM, controls IR LED intensity |
| FAULT_N | Open-drain output from IR board, active-low on fault |
| Ground | BOARD_GND |
| Shield | Connected to CHASSIS_GND through connector shell |

---

## 9. Debug UART Signal Path

| Parameter | Specification |
|-----------|---------------|
| Interface | UART (TTL 3.3V) |
| Baud rate | 115200 bps (boot console), configurable |
| Connector | J500 (1.27mm pin header) |
| Signals | TX, RX, GND |
| Purpose | Boot log, kernel console, factory diagnostics |

---

## 10. Signal Impedance Summary

| Signal | Impedance Target | Tolerance | Routing Type |
|--------|-----------------|-----------|--------------|
| FPD-Link III (coax) | 50 ohm single-ended | +/- 10% | Controlled impedance coax |
| CSI-2 (PCB) | 100 ohm differential | +/- 10% | Diff pair, length matched |
| USB 2.0 (PCB) | 90 ohm differential | +/- 10% | Diff pair |
| CAN bus (PCB) | 120 ohm differential | +/- 10% | Diff pair to connector |
| SPI | 50 ohm single-ended | +/- 15% | Standard trace (short) |
| UART | No controlled impedance | N/A | Standard trace |
| I2C | No controlled impedance | N/A | Standard trace with pull-ups |

---

## 11. Signal Integrity Constraints

| Constraint | Requirement |
|------------|-------------|
| CSI-2 intra-pair skew | < 0.5mm (trace length difference) |
| CSI-2 inter-pair skew | < 2mm |
| USB intra-pair skew | < 0.15mm |
| No ground plane splits under high-speed signals | All CSI-2, USB, CAN |
| Via count on high-speed paths | Minimize (2 max per signal) |
| Component placement (ESD) | < 5mm from connector pin |
| Decoupling capacitors | < 3mm from power pins |

---

## 12. Revision History

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| 1.0 | 2026-06 | Signal Integrity Team | Initial release |
