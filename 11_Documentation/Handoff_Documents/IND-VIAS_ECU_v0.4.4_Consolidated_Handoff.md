# ADVIS ECU v0.4.4 Consolidated Hardware Handoff Document

> **Note:** This document describes the ADVIS v0.4.4 A-sample SerDes/SOM validation baseline. It is not the compact v0.5 direct-MIPI production-cost-down architecture. The compact module is defined separately under `01_Architecture/Baselines/ADVIS_COMPACT_v0.5_Direct_MIPI.md`.

## 1. Document Status

| Field | Value |
|-------|-------|
| **Project** | ADVIS (Adaptive Driver & Vehicle Intelligence System) ADAS + DMS ECU |
| **Version** | v0.4.4 |
| **Status** | A-sample production-intent architecture and schematic capture baseline |
| **Architecture** | LOCKED |
| **Date** | June 2026 |
| **Classification** | Confidential - Engineering Use Only |

**Schematic skeleton capture:** Can begin immediately  
**ERC-clean schematic / final BOM / PCB layout release:** Blocked until implementation-closure items are completed

This document consolidates the complete current hardware definition into one place: what is being built, the target architecture, the selected major components, the power tree, the interfaces, the default strap states, the connector intent, the net and signal map, and the remaining implementation-closure items that must be finished before final PCB release.

---

## 2. What Is Being Built

The ADVIS ECU is a vehicle-mounted ADAS + DMS edge compute unit intended to receive two camera streams, run perception and monitoring workloads on a TDA4VM/AM68A-class SOM, log or observe CAN-FD traffic, receive GNSS and IMU data, and expose engineering/service interfaces such as UART, USB, and removable storage.

### 2.1 Functional Scope

| Function | Implementation |
|----------|---------------|
| Forward camera input | FPD-Link III via DS90UB954-Q1 VC0 |
| DMS camera input | FPD-Link III via DS90UB954-Q1 VC1 |
| Camera aggregation | Single deserializer hub, dual virtual channel to CSI-2 |
| GNSS position/time | u-blox NEO-M9N-00B, concurrent multi-GNSS |
| IMU motion sensing | Bosch BMI088, SPI interface, dual chip-select |
| CAN-FD monitoring | TCAN1044AV-Q1 transceiver, advisory/logging mode |
| Service/debug | UART console, USB-C device mode, microSD slot |
| IR illumination | External IR daughterboard connector for DMS |

### 2.2 Explicit Non-Scope / Safety Boundary

This ECU does NOT provide:

- Direct brake actuation
- Direct steering actuation
- Direct throttle actuation
- Direct powertrain actuation
- ASIL-C or ASIL-D system-level compliance

ADVIS does not directly actuate brake, steering, throttle or powertrain.

ADVIS Assist provides warning/advisory outputs.

ADVIS Control may generate perception-validated, safety-supervised actuation request messages over CAN/CAN-FD, depending on OEM integration.

Final actuator authority, arbitration and vehicle-level safety release remain with the OEM brake, EPS and powertrain ECUs.

### 2.3 Product Family Context

| Product | Sensor Set | Feature Scope |
|---------|-----------|---------------|
| ADVIS Assist | Forward + DMS camera | FCW, LDW, TSR, PCW, DMS |
| ADVIS Control | Forward + DMS camera | AEB, ACC, LKA request outputs, driver-aware speed moderation |
| ADVIS Fusion | Camera + DMS + radar | Sensor fusion, enhanced AEB/ACC/LKA, blind-spot/moving-off |
| ADVIS Fleet | Camera + DMS (later radar) | Fleet safety, driver behavior, event logging |

---

## 3. Architecture Lock Statement

ADVIS ECU v0.4.4 is locked as the A-sample production-intent architecture and schematic capture baseline. Changes to locked items require a formal ECO (Engineering Change Order) with impact assessment and multi-stakeholder approval.

### 3.1 Locked Items

- Power tree topology and voltage rails
- SOM interface assignment (CSI-2 lanes, SPI bus, I2C addresses)
- Connector pinout intent (pending final mechanical validation)
- Ground domain strategy
- Camera aggregation architecture (single DS90UB954-Q1)
- Component selections for all critical-path ICs

### 3.2 Not Yet Locked (Implementation-Closure)

- Exact passive component values (decoupling caps, filter networks)
- PCB stackup layer count (8 vs 10 layer pending SI analysis)
- EMI filter component selection
- Mechanical enclosure final dimensions

---

## 4. Complete Component List

### 4.1 Active Components

| RefDes | Component | Manufacturer | Part Number | Function |
|--------|-----------|-------------|-------------|----------|
| U1 | SOM Module | Phytec | phyCORE-AM68A (TDA4VM) | Main compute, AI inference |
| U2 | FPD-Link III DeSerializer | Texas Instruments | DS90UB954-Q1 | Dual camera aggregation |
| U3 | Buck Converter (12V to 5V) | Texas Instruments | LM61460-Q1 | Primary 5V_SYS rail, 6A |
| U4 | Buck Converter (5V to 3.3V) | Texas Instruments | TPS62130A-Q1 | 3.3V rail generation |
| U5 | LDO (3.3V to 1.8V) | Texas Instruments | TLV75518-Q1 | 1.8V rail generation |
| U6 | Voltage Supervisor | Texas Instruments | TPS3808G33-Q1 | 3V3_IO monitoring, reset gen |
| U7 | Watchdog Timer | Texas Instruments | TPS3431-Q1 | Independent watchdog |
| U8 | CAN-FD Transceiver | Texas Instruments | TCAN1044AV-Q1 | CAN bus interface |
| U9 | GNSS Receiver | u-blox | NEO-M9N-00B | Multi-constellation GNSS |
| U10 | IMU (Accel + Gyro) | Bosch | BMI088 | 6-axis inertial sensing |
| Q1 | Reverse-Polarity PMOS | Various | 80V P-channel MOSFET | Input protection |
| D1 | TVS Diode | Various | Bidirectional TVS, 15V Vr | Transient protection |
| F1 | Automotive Fuse | Various | 5A blade fuse | Overcurrent protection |

### 4.2 Passive and Support Components

| RefDes | Component | Value | Function |
|--------|-----------|-------|----------|
| R_CAN_TERM | CAN Termination | 120 ohm (DNI option) | Bus termination |
| R_TXD_PU | TXD Pull-up | 10k to 3V3_CAN | Recessive state bias |
| C_IN | Input Bulk Cap | 100uF/50V electrolytic | Input energy storage |
| C_5V | 5V Rail Decoupling | 22uF + 100nF ceramic | Rail stability |
| C_3V3 | 3.3V Rail Decoupling | 10uF + 100nF ceramic | Rail stability |
| C_1V8 | 1.8V Rail Decoupling | 4.7uF + 100nF ceramic | Rail stability |
| L_GNSS | GNSS RF Choke | Ferrite bead | RF isolation |
| R_WDI | Watchdog Kick Pull-up | 100k to 3V3_IO | Default safe state |

---

## 5. Power Tree Architecture

### 5.1 Power Flow Diagram

```
Vehicle 12V Battery
       |
    [F1: 5A Fuse]
       |
    [D1: TVS Diode - bidirectional, Vr=15V]
       |
    [Q1: 80V PMOS - Reverse Polarity Protection]
       |
  VIN_PROTECTED (~11.5-14.5V typical)
       |
       +--[U3: LM61460-Q1, 6A Buck]---> 5V_SYS (5.0V, 6A max)
       |                                      |
       |                 +--------------------+--------------------+
       |                 |                    |                    |
       |    [U4: TPS62130A-Q1]     (Direct to SOM)    (Direct to USB)
       |           |                          
       |      3V3_IO (3.3V, 3A max)          
       |           |                          
       |           +--[U5: TLV75518-Q1]---> 1V8_AUX (1.8V, 500mA)
       |           |
       |           +---> U6 TPS3808G33 (supervisor input)
       |           +---> U7 TPS3431 (watchdog VCC)
       |           +---> U8 TCAN1044AV (CAN VCC)
       |           +---> U9 NEO-M9N (GNSS VCC)
       |           +---> U10 BMI088 (IMU VDD)
       |
  5V_SYS---> SOM 5V input
  5V_SYS---> DS90UB954-Q1 VCC
  5V_SYS---> USB VBUS (via switch/fuse)
```

### 5.2 Rail Specifications

| Rail Name | Nominal | Tolerance | Max Current | Source | Load |
|-----------|---------|-----------|-------------|--------|------|
| VIN_RAW | 9-16V (27V crank) | Automotive | 5A fuse | Vehicle | Protection circuit |
| VIN_PROTECTED | ~VIN - 0.3V | - | 5A | PMOS output | LM61460 input |
| 5V_SYS | 5.0V | +/-3% | 6A | LM61460-Q1 | SOM, DS90UB954, USB |
| 3V3_IO | 3.3V | +/-2% | 3A | TPS62130A-Q1 | Peripherals, logic |
| 1V8_AUX | 1.8V | +/-2% | 500mA | TLV75518-Q1 | Level shifters, misc |

### 5.3 Power Sequencing

```
Power-On Sequence:
  1. VIN applied (key-on or permanent power)
  2. PMOS conducts (VIN_PROTECTED present)
  3. LM61460 starts -> 5V_SYS rises (EN tied to VIN via divider)
  4. TPS62130A starts -> 3V3_IO rises (EN from 5V_SYS PG)
  5. TLV75518 starts -> 1V8_AUX rises (EN from 3V3_IO PG)
  6. TPS3808G33 asserts RESET_N low until 3V3_IO stable
  7. RESET_N released -> SOM begins boot
  8. SOM asserts SOM_BOOT_OK -> TPS3431 watchdog enabled
  9. Firmware begins periodic watchdog kicks (WDI toggle)

Power-Off Sequence (reverse):
  1. VIN removed or supervisor trip
  2. Watchdog timeout -> system reset (if SOM hangs)
  3. Rails decay in reverse order (1V8 -> 3V3 -> 5V)
```

---

## 6. Ground Domain Architecture

### 6.1 Ground Domains

| Domain | Symbol | Connected Circuits | Return Path |
|--------|--------|-------------------|-------------|
| Power Ground | PGND | Buck converters, input protection, bulk caps | Chassis via connector |
| Digital Ground | DGND | SOM, deserializer, CAN, USB | Star-point to PGND |
| Analog/RF Ground | AGND | GNSS RF, IMU, antenna bias | Star-point to DGND |

### 6.2 Star-Point Topology

```
         CHASSIS (connector shell)
              |
         [Single-point bond]
              |
            PGND -------- Power stage, input caps, TVS
              |
         [Star-point A]
              |
            DGND -------- SOM, DS90UB954, CAN, USB, watchdog
              |
         [Star-point B]
              |
            AGND -------- NEO-M9N RF, BMI088, antenna
```

### 6.3 Design Rules

- PGND copper pour under power components, separate from DGND pour
- DGND and PGND connect at ONE defined star point near input connector
- AGND connects to DGND at ONE point near the GNSS/IMU region
- No digital traces cross AGND pour boundaries
- Minimum 50mil keepout between AGND and DGND boundaries

---

## 7. Camera Subsystem

### 7.1 DS90UB954-Q1 Configuration

| Parameter | Value |
|-----------|-------|
| Part Number | DS90UB954-Q1RGERQ1 |
| Mode | Dual FPD-Link III Deserializer |
| Port 0 (RX0) | Forward Camera (VC0) |
| Port 1 (RX1) | DMS Camera (VC1) |
| CSI-2 Output | 4-lane to SOM CSI-2 Rx port |
| I2C Address | 0x30 (default, configurable via strap) |
| Power | 5V_SYS (internal LDOs) |
| PoC | Power-over-Coax to remote serializers |

### 7.2 Camera Channel Mapping

```
Forward Camera Module          DMS Camera Module
  [Serializer UB953]             [Serializer UB953]
        |                              |
  FPD-Link III Coax              FPD-Link III Coax
  (up to 15m)                    (up to 15m)
        |                              |
  +-----+------------------------------+-----+
  |  RX0/PORT0              RX1/PORT1         |
  |                                           |
  |            DS90UB954-Q1                   |
  |                                           |
  |      CSI-2 TX (4-lane, up to 1.6Gbps/ln) |
  +-------------------------------------------+
        |
   SOM CSI-2 Rx Port
   (VC0 = Forward, VC1 = DMS)
```

### 7.3 FPD-Link III Specifications

| Parameter | Specification |
|-----------|--------------|
| Data Rate | Up to 2.5 Gbps per link |
| Cable Type | Coaxial or STP, automotive grade |
| Max Cable Length | 15m (typical automotive) |
| PoC Voltage | 9-18V (through same coax) |
| Video Format | RAW10/12, YUV422 |
| Bidirectional Control | I2C back-channel (100kbps) |

---

## 8. CAN-FD Subsystem

### 8.1 TCAN1044AV-Q1 Configuration

| Parameter | Value |
|-----------|-------|
| Mode | Normal Mode (default) |
| VCC | 3V3_IO |
| VIO | 3V3_IO (same as VCC for 3.3V logic) |
| STB pin | Tied LOW (Normal Mode) |
| TXD Pull-up | 10k to 3V3_CAN (recessive default) |
| Bus Termination | 120 ohm (DNI for mid-bus nodes) |

### 8.2 CAN Bus Interface

```
SOM CAN_TX ---[3.3V]---> TCAN1044AV TXD
SOM CAN_RX <----------- TCAN1044AV RXD
                              |
                         CANH ---+--- [120R DNI] ---+--- CANH (connector)
                         CANL ---+--- [120R DNI] ---+--- CANL (connector)
                              |
                         STB = LOW (Normal Mode)
                         WAKE (optional, to SOM GPIO)
```

### 8.3 Operational Notes

- Default operation: Normal Mode (STB=LOW)
- TXD has external 10k pull-up ensuring recessive state if SOM tri-states
- CAN termination resistor is DNI (Do Not Install) for mid-bus applications
- Wake pattern detection available for partial networking (future use)
- Bus speed: up to 5 Mbps CAN-FD, 1 Mbps classic CAN

---

## 9. GNSS Subsystem

### 9.1 NEO-M9N-00B Configuration

| Parameter | Value |
|-----------|-------|
| Interface | UART (primary), I2C (secondary) |
| VCC | 3V3_IO |
| Antenna | Active antenna via SMA or u.FL |
| Antenna Bias | 3.3V bias-T through RF choke + DC block |
| PPS Output | 1PPS to SOM GPIO (time sync) |
| Backup Battery | Optional CR1220 for hot-start |
| Update Rate | Up to 25Hz (configurable) |
| Constellations | GPS + GLONASS + Galileo + BeiDou (concurrent) |

### 9.2 GNSS RF Path

```
Active Antenna
      |
  [SMA/u.FL Connector]
      |
  [ESD Protection]
      |
  [Bias-T: 3V3 via RF choke + DC blocking cap]
      |
  [SAW Filter (optional, improves interference rejection)]
      |
  NEO-M9N-00B RF_IN
```

---

## 10. IMU Subsystem

### 10.1 BMI088 Configuration

| Parameter | Value |
|-----------|-------|
| Interface | SPI (primary) |
| Accelerometer CS | SPI_CS0 (SOM GPIO) |
| Gyroscope CS | SPI_CS1 (SOM GPIO) |
| VDD | 3V3_IO |
| VDDIO | 1V8_AUX (I/O voltage) |
| INT1 (Accel) | To SOM GPIO (data-ready) |
| INT3 (Gyro) | To SOM GPIO (data-ready) |
| SPI Clock | Up to 10 MHz |
| Accel Range | +/-24g (configurable) |
| Gyro Range | +/-2000 deg/s (configurable) |

### 10.2 SPI Bus Architecture

```
SOM SPI Master
  |
  +--- SCLK ---------> BMI088 SCLK
  +--- MOSI ---------> BMI088 SDI
  +--- MISO <--------- BMI088 SDO
  +--- CS0  ---------> BMI088 CSB1 (Accelerometer)
  +--- CS1  ---------> BMI088 CSB2 (Gyroscope)
```

---

## 11. Reset and Watchdog Topology

### 11.1 Reset Architecture

```
                    TPS3808G33-Q1 (U6)
                         |
                    VDD = 3V3_IO
                    SENSE = 3V3_IO (monitors this rail)
                    Threshold = 3.08V (93% of 3.3V)
                         |
                    RESET_N (open-drain, active-low)
                         |
                    +----+----+
                    |         |
               SOM nRESET   DS90UB954 PDB
                              (power-down bar)
```

### 11.2 Watchdog Architecture

```
                    TPS3431-Q1 (U7)
                         |
                    VCC = 3V3_IO
                    EN = SOM_BOOT_OK (GPIO, active-high)
                         |
                    WDI <--- SOM GPIO (periodic toggle)
                    RESET_N ---> OR with supervisor RESET_N
                         |
                    Timeout: configurable via CT pin cap
                    Default: ~1.6s (typ)

Boot Behavior:
  - EN = LOW during boot (watchdog DISABLED)
  - SOM completes boot, firmware asserts SOM_BOOT_OK = HIGH
  - Watchdog starts; firmware must kick WDI periodically
  - If WDI not toggled within timeout -> RESET_N asserted
```

### 11.3 Reset Priority

| Source | Condition | Effect |
|--------|-----------|--------|
| TPS3808G33 | 3V3_IO < 3.08V | Assert RESET_N (all digital) |
| TPS3431 | WDI timeout | Assert RESET_N (all digital) |
| Manual | Test point / debug header | Assert RESET_N (all digital) |
| SOM internal | Software reset | SOM-only reset |

---

## 12. USB and Debug Interfaces

### 12.1 USB-C Device Mode

| Parameter | Value |
|-----------|-------|
| Connector | USB-C receptacle |
| Mode | Device (UFP) only |
| CC Pull-downs | 5.1k on each CC pin (device identification) |
| Data Lines | USB 2.0 D+/D- to SOM |
| VBUS | Not sourced (device mode) |
| Use Case | Firmware update, data offload, diagnostics |

### 12.2 UART Debug Console

| Parameter | Value |
|-----------|-------|
| Interface | 3.3V UART (TX, RX, GND) |
| Baud Rate | 115200 (default boot console) |
| Connector | 3-pin header (1.27mm pitch) |
| Level | 3.3V LVCMOS (no RS-232 driver) |
| Use Case | Boot log, Linux console, field diagnostics |

### 12.3 MicroSD Card Slot

| Parameter | Value |
|-----------|-------|
| Interface | SD 3.0 (UHS-I capable) |
| Voltage | 3.3V signaling |
| Use Case | Removable storage for logs, firmware update media |
| Card Detect | Mechanical switch (active-low to SOM GPIO) |

---

## 13. IR Daughterboard Interface

### 13.1 Connector Definition

| Pin | Signal | Direction | Description |
|-----|--------|-----------|-------------|
| 1 | 5V_IR | OUT | 5V supply for IR LEDs (from 5V_SYS via load switch) |
| 2 | IR_EN | OUT | Enable signal from SOM GPIO (active-high) |
| 3 | IR_FAULT_N | IN | Overcurrent/thermal fault feedback (active-low) |
| 4 | GND | - | Power/signal return |

### 13.2 IR Control Logic

- IR_EN driven by SOM GPIO (synchronized to DMS frame capture)
- 5V_IR provided through dedicated load switch with current limit
- IR_FAULT_N monitored by SOM for LED string failure detection
- Maximum IR power budget: 2W (400mA at 5V)

---

## 14. External Connector Definitions

### 14.1 Main Vehicle Connector (Intent)

| Pin | Signal | Description |
|-----|--------|-------------|
| 1 | VIN+ | Vehicle 12V power input |
| 2 | GND | Power and chassis ground |
| 3 | CANH | CAN-FD bus high |
| 4 | CANL | CAN-FD bus low |
| 5 | FPD0+ | FPD-Link III Port 0 (Forward camera) |
| 6 | FPD0- | FPD-Link III Port 0 shield/return |
| 7 | FPD1+ | FPD-Link III Port 1 (DMS camera) |
| 8 | FPD1- | FPD-Link III Port 1 shield/return |
| 9 | GNSS_ANT | GNSS antenna RF |
| 10 | GNSS_GND | GNSS antenna ground |

*Note: Final pin assignment pending mechanical envelope and connector vendor selection.*

### 14.2 Service/Debug Connector

| Pin | Signal | Description |
|-----|--------|-------------|
| 1 | USB_D+ | USB 2.0 data positive |
| 2 | USB_D- | USB 2.0 data negative |
| 3 | UART_TX | Debug console transmit (from ECU) |
| 4 | UART_RX | Debug console receive (to ECU) |
| 5 | GND | Signal ground |

---

## 15. SOM Signal Map

### 15.1 Key SOM Interface Assignments

| SOM Interface | Connected To | Notes |
|---------------|-------------|-------|
| CSI-2 Rx (4-lane) | DS90UB954-Q1 CSI TX | Camera data input |
| I2C Bus 0 | DS90UB954-Q1 (0x30) | DeSerializer config |
| I2C Bus 1 | NEO-M9N (0x42) | GNSS secondary interface |
| SPI Bus 0 | BMI088 (CS0=Accel, CS1=Gyro) | IMU data |
| UART 0 | Debug connector | Linux console |
| UART 1 | NEO-M9N | GNSS NMEA/UBX data |
| CAN-FD 0 | TCAN1044AV-Q1 | Vehicle CAN bus |
| USB 2.0 | USB-C connector | Device mode |
| SD/MMC | MicroSD slot | Removable storage |
| GPIO_A | SOM_BOOT_OK | Watchdog enable |
| GPIO_B | WDI | Watchdog kick |
| GPIO_C | RESET_N (input) | System reset |
| GPIO_D | IR_EN | IR daughterboard enable |
| GPIO_E | IR_FAULT_N (input) | IR fault feedback |
| GPIO_F | PPS (input) | GNSS 1PPS time sync |
| GPIO_G | IMU_INT1 (input) | Accel data-ready |
| GPIO_H | IMU_INT3 (input) | Gyro data-ready |
| GPIO_I | SD_CD_N (input) | MicroSD card detect |

---

## 16. Default Strap States

| Signal | Default State | Purpose | Change Method |
|--------|---------------|---------|---------------|
| DS90UB954 ADDR[1:0] | 00 | I2C address = 0x30 | Strap resistors |
| TCAN1044 STB | LOW | Normal Mode | Strap to GND |
| CAN Termination | DNI (open) | Mid-bus node | Populate 120R |
| SOM Boot Mode | SD/eMMC | Primary boot from eMMC | Strap resistors |
| Watchdog EN | LOW at POR | Disabled until firmware ready | SOM GPIO |

---

## 17. Open Items Blocking PCB Release

### 17.1 Critical Path Items

| # | Item | Owner | Status | Impact |
|---|------|-------|--------|--------|
| 1 | Final PCB stackup selection (8 vs 10 layer) | Layout Lead | Open | Impedance control, cost |
| 2 | SI simulation for CSI-2 lanes (1.6Gbps) | SI Engineer | Open | Trace routing rules |
| 3 | Thermal simulation (SOM + DS90UB954 + buck) | Thermal Lead | Open | Heatsink/airflow requirements |
| 4 | Connector vendor selection and 3D model | Mechanical | Open | PCB footprint, panel cutouts |
| 5 | EMC pre-compliance plan | EMC Engineer | Open | Filter component selection |

### 17.2 Desirable Before Release

| # | Item | Owner | Status | Impact |
|---|------|-------|--------|--------|
| 6 | GNSS antenna placement study | RF Engineer | Open | Sensitivity, multipath |
| 7 | Power integrity simulation | PI Engineer | Open | Decoupling optimization |
| 8 | Conformal coating specification | Manufacturing | Open | Environmental protection |
| 9 | Production test point placement plan | Test Engineer | Open | ICT/FCT coverage |
| 10 | Second-source component identification | Procurement | Open | Supply chain risk |

---

## 18. Design Constraints and Rules

### 18.1 Electrical Constraints

| Parameter | Requirement |
|-----------|-------------|
| Input voltage range | 9V to 16V continuous, 27V cranking (100ms) |
| Reverse polarity | Survive indefinite reverse up to -16V |
| Load dump | ISO 7637-2 pulse 5b (survive) |
| ESD (connector pins) | IEC 61000-4-2 Level 4 (8kV contact, 15kV air) |
| Operating temperature | -40C to +85C (junction limit per component) |
| Storage temperature | -40C to +125C |
| Total power budget | <25W at maximum load (all peripherals active) |

### 18.2 Mechanical Constraints

| Parameter | Requirement |
|-----------|-------------|
| PCB dimensions | TBD (pending enclosure selection) |
| Mounting | M3 standoffs, minimum 4 points |
| Connector access | Single-side preferred (vehicle harness routing) |
| Vibration | ISO 16750-3 (passenger car, engine-mounted) |
| IP rating | IP54 minimum (with sealed connectors) |

---

## 19. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| v0.4.4 | June 2026 | Hardware Team | Architecture lock, A-sample baseline |
| v0.4.0 | May 2026 | Hardware Team | Near-final architecture, safety boundary |
| v0.3.5 | April 2026 | Hardware Team | Interface definitions, ground strategy |
| v0.3.0 | March 2026 | Hardware Team | Component selections finalized |
| v0.2.0 | February 2026 | Hardware Team | Architecture exploration |
| v0.1.0 | January 2026 | Hardware Team | Initial concept |

---

*End of Consolidated Handoff Document*
