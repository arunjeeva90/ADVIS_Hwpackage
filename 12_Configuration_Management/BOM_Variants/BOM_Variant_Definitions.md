# ADVIS BOM Variant Definitions

## 1. Overview

The ADVIS v0.4.4 carrier PCB supports multiple product configurations through BOM variants. In the SOM-based architecture, a single carrier PCB design accommodates Entry, Mid, and High tier products by populating or depopulating specific components and changing strap resistor values, because the SoC resides on the interchangeable SoM. For the v0.5 direct-SoC architecture, PCB commonality across SoC variants is subject to pinout compatibility analysis (see OD-003).

## 2. Variant Summary

| Variant | SoC Tier | Cameras | GNSS | IMU | CAN | IR | Target Cost Tier |
|---------|----------|---------|------|-----|-----|----|-----------------|
| ADVIS-E (Entry) | AM62A | 1 (DMS only) | Optional | No | Yes | No | Lowest |
| ADVIS-M (Mid) | AM68A/TDA4VM | 2 (Fwd + DMS) | Yes | Yes | Yes | Yes | Baseline |
| ADVIS-H (High) | TDA4VH | 2-4+ | Yes | Yes | Yes (multi) | Yes | Premium |

---

## 3. Entry Tier (ADVIS-E)

### 3.1 Configuration

| Subsystem | Status | Notes |
|-----------|--------|-------|
| SOM | AM62A-based module | Lower-cost, single-camera capable |
| DS90UB954 Port 0 | DNI | Forward camera not connected |
| DS90UB954 Port 1 | Populated | DMS camera via FPD-Link III |
| DS90UB954 (alt) | DNI entire IC | Direct MIPI option for cost-down |
| LM61460-Q1 | Populated | Reduced current draw (~2A typical) |
| TPS62130A-Q1 | Populated | Standard 3.3V rail |
| TLV75518-Q1 | Populated | Standard 1.8V rail |
| TCAN1044AV-Q1 | Populated | CAN monitoring (read-only use) |
| NEO-M9N-00B | DNI | GNSS not required for basic DMS |
| BMI088 | DNI | IMU not required for basic DMS |
| GNSS antenna bias-T | DNI | Not populated when GNSS DNI |
| IR connector | DNI | IR illumination optional |
| USB-C | Populated | Firmware update, diagnostics |
| MicroSD | Populated | Log storage |
| CAN termination (120R) | DNI | Mid-bus node default |

### 3.2 DNI Designators (Entry)

```
DNI List (Entry Tier):
  U2 (DS90UB954) - when using direct MIPI
  U9 (NEO-M9N-00B) - GNSS receiver
  U10 (BMI088) - IMU
  R_PORT0_TERM - FPD-Link Port 0 termination
  C_GNSS_* - GNSS decoupling capacitors
  L_GNSS - GNSS RF choke
  C_IMU_* - IMU decoupling capacitors
  J_IR - IR daughterboard connector
  J_GNSS_ANT - GNSS antenna connector
```

### 3.3 Strap Changes (Entry)

| Strap | Entry Value | Purpose |
|-------|-------------|---------|
| SOM Boot Mode | SD card | Development/fleet update |
| DS90UB954 mode | Single-port (if populated) | Only VC1 active |

---

## 4. Mid Tier (ADVIS-M) - Current v0.4.4 Baseline

### 4.1 Configuration

| Subsystem | Status | Notes |
|-----------|--------|-------|
| SOM | AM68A/TDA4VM (Phytec phyCORE) | Full dual-camera AI capability |
| DS90UB954 Port 0 | Populated | Forward camera (VC0) |
| DS90UB954 Port 1 | Populated | DMS camera (VC1) |
| LM61460-Q1 | Populated | Full 6A capability |
| TPS62130A-Q1 | Populated | Full 3A capability |
| TLV75518-Q1 | Populated | Standard 1.8V |
| TCAN1044AV-Q1 | Populated | CAN-FD monitoring |
| NEO-M9N-00B | Populated | Multi-constellation GNSS |
| BMI088 | Populated | 6-axis IMU |
| GNSS antenna bias-T | Populated | Active antenna support |
| IR connector | Populated | DMS IR illumination |
| USB-C | Populated | Diagnostics, firmware update |
| MicroSD | Populated | Log storage, update media |
| CAN termination (120R) | DNI | Mid-bus node (default) |

### 4.2 DNI Designators (Mid)

```
DNI List (Mid Tier):
  R_CAN_TERM (120R) - Only if mid-bus node
  [All other components populated]
```

### 4.3 Strap Settings (Mid)

| Strap | Mid Value | Purpose |
|-------|-----------|---------|
| SOM Boot Mode | eMMC primary, SD fallback | Production boot |
| DS90UB954 Address | 0x30 (default) | I2C address |
| CAN STB | LOW | Normal Mode |
| Watchdog EN | GPIO controlled | SOM_BOOT_OK gating |

---

## 5. High Tier (ADVIS-H)

### 5.1 Configuration

| Subsystem | Status | Notes |
|-----------|--------|-------|
| SOM | TDA4VH-based module | Multi-camera, high AI performance |
| DS90UB954 Port 0 | Populated | Forward camera (VC0) |
| DS90UB954 Port 1 | Populated | DMS camera (VC1) |
| Additional DeSerializer | Populated (future) | Additional camera ports (side/rear) |
| LM61460-Q1 | Populated | Higher average current draw |
| TPS62130A-Q1 | Populated | Higher average current draw |
| TLV75518-Q1 | Populated | Standard |
| TCAN1044AV-Q1 (x2) | Populated | Dual CAN channels |
| NEO-M9N-00B | Populated | Multi-constellation + dead reckoning |
| BMI088 | Populated | Vehicle dynamics input |
| GNSS antenna bias-T | Populated | Active antenna |
| IR connector | Populated | Enhanced IR (higher power) |
| USB-C | Populated | High-speed data offload |
| MicroSD | Populated | Extended logging capacity |
| CAN termination (120R) | Populated | End-node configuration |
| Ethernet PHY | Populated (future) | Automotive Ethernet (100BASE-T1) |

### 5.2 Additional Components (High Only)

```
High-Tier Additional:
  U11 - Second CAN transceiver (TCAN1044AV-Q1)
  U12 - Ethernet PHY (future, DP83TC811S-Q1)
  U13 - Additional deserializer (future, DS90UB954-Q1 or DS90UB960-Q1)
  J_ETH - Automotive Ethernet connector
  Active cooling connector (fan header or TEC interface)
```

### 5.3 Strap Settings (High)

| Strap | High Value | Purpose |
|-------|-----------|---------|
| SOM Boot Mode | eMMC primary | Fast production boot |
| DS90UB954 Address | 0x30 | Primary deserializer |
| Additional DeSerializer Address | 0x36 | Secondary (non-conflicting) |
| CAN termination | Populated (120R) | End-node for primary CAN |
| Thermal management | Active | Fan/TEC enable |

---

## 6. Cost Impact Summary

| Component | Entry (DNI saves) | Mid (baseline) | High (additional cost) |
|-----------|-------------------|----------------|----------------------|
| DS90UB954-Q1 | -$4.50 (if DNI) | $0 (included) | $0 |
| NEO-M9N-00B | -$8.00 | $0 (included) | $0 |
| BMI088 | -$5.00 | $0 (included) | $0 |
| IR connector + components | -$1.50 | $0 (included) | $0 |
| GNSS antenna circuit | -$2.00 | $0 (included) | $0 |
| Second CAN transceiver | N/A | N/A | +$2.50 |
| Ethernet PHY | N/A | N/A | +$6.00 |
| Additional deserializer | N/A | N/A | +$5.00 |
| Active cooling | N/A | N/A | +$4.00 |
| **Net vs Mid Baseline** | **-$21.00** | **$0** | **+$17.50** |

*Costs are approximate at 10k unit volume. Actual costs depend on vendor negotiations and volume.*

## 7. Variant Validation Matrix

| Test | Entry | Mid | High |
|------|-------|-----|------|
| Power-on / rail sequencing | Required | Required | Required |
| Single camera (DMS) streaming | Required | Required | Required |
| Dual camera streaming | N/A | Required | Required |
| CAN bus communication | Required | Required | Required |
| GNSS position fix | N/A | Required | Required |
| IMU data acquisition | N/A | Required | Required |
| IR illumination control | N/A | Required | Required |
| USB data transfer | Required | Required | Required |
| MicroSD read/write | Required | Required | Required |
| Multi-CAN operation | N/A | N/A | Required |
| Ethernet connectivity | N/A | N/A | Required (future) |
| Thermal under load | Required | Required | Required (active) |

---

*ADVIS Hardware Platform - Configuration Management*
