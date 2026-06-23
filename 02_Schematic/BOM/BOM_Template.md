# ADVIS Bill of Materials Template

**Document ID:** ADVIS-BOM-TPL-001  
**Version:** 0.1.0 (Seed BOM)  
**Status:** Pre-production  
**Last Updated:** 2024-01-15

---

## 1. BOM Structure

The production BOM follows the columns defined below. All components must carry AEC-Q100
(ICs) or AEC-Q200 (passives) qualification for automotive deployment.

### Column Definitions

| Column | Description |
|--------|-------------|
| RefDes | Reference designator(s) on schematic |
| Value | Component value or part description |
| Part Number | Manufacturer part number (MPN) |
| Manufacturer | Component manufacturer |
| Package | Package type and size (e.g., QFN-48, 0402) |
| Tolerance | Value tolerance (e.g., 1%, 5%, 10%) |
| Voltage Rating | Maximum voltage rating |
| AEC-Q | AEC qualification level (Q100, Q200, or N/A) |
| Alternate PN | Approved second-source part number |
| DNI | Do Not Install flag (Y/N) |
| Tier Variant | Which product tier uses this part (All, Mid+High, High only) |
| Notes | Special handling, placement, or sourcing notes |

---

## 2. Seed BOM - Key Components

### 2.1 Power Path

| RefDes | Value | Part Number | Manufacturer | Package | Tolerance | Voltage Rating | AEC-Q | Alternate PN | DNI | Tier Variant | Notes |
|--------|-------|-------------|--------------|---------|-----------|----------------|-------|--------------|-----|--------------|-------|
| F1 | 5A Automotive Fuse | TBD | TBD | Blade mini | -- | 32V | Q200 | -- | N | All | Slow-blow rated |
| D1 | TVS Diode | TBD | TBD | SMB | -- | 24V standoff | Q100 | -- | N | All | Bidirectional, ISO 7637 |
| Q1 | P-ch MOSFET 80V | TBD | TBD | DPAK | -- | 80V | Q100 | -- | N | All | Reverse polarity protection |
| U1 | 6A Buck 5V | LM61460-Q1 | Texas Instruments | HTSSOP-16 | -- | 36V input | Q100 | -- | N | All | 5V_SYS primary rail |
| U2 | 2A Buck 3.3V | TPS62130A-Q1 | Texas Instruments | QFN-16 | -- | 17V input | Q100 | -- | N | All | 3.3V rail |
| U3 | 500mA LDO 1.8V | TLV75518-Q1 | Texas Instruments | SOT-23-5 | -- | 5.5V input | Q100 | -- | N | All | 1.8V rail |

### 2.2 Supervision and Watchdog

| RefDes | Value | Part Number | Manufacturer | Package | Tolerance | Voltage Rating | AEC-Q | Alternate PN | DNI | Tier Variant | Notes |
|--------|-------|-------------|--------------|---------|-----------|----------------|-------|--------------|-----|--------------|-------|
| U4 | Voltage Supervisor | TPS3808G33-Q1 | Texas Instruments | SOT-23-6 | -- | 6.5V | Q100 | -- | N | All | Monitors 3V3_IO rail |
| U5 | Window Watchdog | TPS3431-Q1 | Texas Instruments | SOT-23-6 | -- | 6.5V | Q100 | -- | N | All | Disabled during boot |

### 2.3 Camera Interface

| RefDes | Value | Part Number | Manufacturer | Package | Tolerance | Voltage Rating | AEC-Q | Alternate PN | DNI | Tier Variant | Notes |
|--------|-------|-------------|--------------|---------|-----------|----------------|-------|--------------|-----|--------------|-------|
| U6 | Dual FPD-Link III Deser | DS90UB954-Q1 | Texas Instruments | QFP-64 | -- | 3.6V I/O | Q100 | -- | N | All | VC0=Forward, VC1=DMS |

### 2.4 Communication Interfaces

| RefDes | Value | Part Number | Manufacturer | Package | Tolerance | Voltage Rating | AEC-Q | Alternate PN | DNI | Tier Variant | Notes |
|--------|-------|-------------|--------------|---------|-----------|----------------|-------|--------------|-----|--------------|-------|
| U7 | CAN-FD Transceiver | TCAN1044AV-Q1 | Texas Instruments | SOIC-8 | -- | 5.5V | Q100 | -- | N | All | Normal mode default |
| U8 | GNSS Receiver | NEO-M9N-00B | u-blox | LCC-24 | -- | 3.6V | Q100 | -- | N | Mid+High | Multi-constellation |

### 2.5 Sensors

| RefDes | Value | Part Number | Manufacturer | Package | Tolerance | Voltage Rating | AEC-Q | Alternate PN | DNI | Tier Variant | Notes |
|--------|-------|-------------|--------------|---------|-----------|----------------|-------|--------------|-----|--------------|-------|
| U9 | 6-axis IMU | BMI088 | Bosch Sensortec | LGA-16 | -- | 3.6V | Q100 | -- | N | Mid+High | Dual SPI CS (accel+gyro) |

### 2.6 Connectors

| RefDes | Value | Part Number | Manufacturer | Package | Tolerance | Voltage Rating | AEC-Q | Alternate PN | DNI | Tier Variant | Notes |
|--------|-------|-------------|--------------|---------|-----------|----------------|-------|--------------|-----|--------------|-------|
| J1 | Vehicle Connector | TBD | TBD | TBD | -- | -- | Q200 | -- | N | All | J100 vehicle harness |
| J2 | Forward Camera Coax | TBD | TBD | FAKRA/HSD | -- | -- | Q200 | -- | N | All | FPD-Link III input |
| J3 | DMS Camera Coax | TBD | TBD | FAKRA/HSD | -- | -- | Q200 | -- | N | All | FPD-Link III input |
| J4 | USB-C | TBD | TBD | USB-C | -- | 20V | Q200 | -- | N | All | Device mode, 5.1k CC |
| J5 | SOM Connector | TBD | TBD | Board-to-board | -- | -- | Q200 | -- | N | All | High-density interface |
| J6 | IR Daughterboard | TBD | TBD | 8-pin header | -- | -- | Q200 | -- | N | Mid+High | J800 IR interface |
| J7 | GNSS Antenna | TBD | TBD | SMA/U.FL | -- | -- | Q200 | -- | N | Mid+High | RF antenna feed |

---

## 3. Passive Component Guidelines

| Category | Preferred Package | Voltage Derating | Temp Rating | AEC-Q |
|----------|-------------------|------------------|-------------|-------|
| Bulk Capacitor (>10uF) | 0805/1206 | 50% min | X7R/-55 to +125C | Q200 |
| Decoupling (100nF) | 0402 | 2x operating | X7R/-55 to +125C | Q200 |
| Feedback Resistor | 0402 | -- | 1% thin film | Q200 |
| General Resistor | 0402 | -- | 5% thick film | Q200 |
| Power Inductor | Per datasheet | 30% Isat margin | -40 to +125C | Q200 |

---

## 4. DNI Strategy

Components marked DNI are placed on PCB but not assembled. This enables:
- Product tier differentiation (Entry tier omits GNSS, IMU, IR)
- Debug features not needed in production
- Future feature enablement without PCB respin

### Tier-based DNI Matrix

| Component | Entry | Mid | High |
|-----------|-------|-----|------|
| GNSS (NEO-M9N) | DNI | Install | Install |
| IMU (BMI088) | DNI | Install | Install |
| IR Daughterboard Header | DNI | Install | Install |
| USB Debug Connector | Install | Install | Install |
| CAN Transceiver | Install | Install | Install |
| Camera Deserializer | Install | Install | Install |

---

## 5. Approved Vendor List (AVL)

| Manufacturer | Categories | Qualification |
|--------------|-----------|---------------|
| Texas Instruments | Power, Interface, Supervisors | AEC-Q100 |
| u-blox | GNSS receivers | AEC-Q100 |
| Bosch Sensortec | MEMS sensors | AEC-Q100 |
| TBD (Connector) | Automotive connectors | AEC-Q200 |
| TBD (Passive) | Resistors, Capacitors, Inductors | AEC-Q200 |

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1.0 | 2024-01-15 | -- | Initial seed BOM with key active components |
