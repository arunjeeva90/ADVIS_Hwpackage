# ADVIS Schematic Sheet Hierarchy

**Document ID:** ADVIS-SCH-HIER-001  
**Version:** 0.1.0  
**Status:** Draft  
**Last Updated:** 2024-01-15

---

## 1. Overview

The ADVIS ECU carrier board schematic is organized into 12 hierarchical sheets.
This decomposition aligns with the architectural subsystems and enables independent
review and modification of each functional block.

```
+---------------------------+
|  Sheet 1: Top/Integration |
+---------------------------+
    |   |   |   |   |   |   |   |   |   |   |
    v   v   v   v   v   v   v   v   v   v   v
  [S2] [S3] [S4] [S5] [S6] [S7] [S8] [S9] [S10] [S11] [S12]
```

---

## 2. Sheet Descriptions

### Sheet 1: Top / Integration Sheet

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Top-level interconnection and hierarchical block instantiation |
| **Key Components** | None (symbolic blocks only) |
| **Interfaces** | All inter-sheet port definitions |
| **Critical Nets** | Power rails (5V_SYS, 3V3_IO, 1V8), ground domains, global signals |
| **Review Priority** | High (defines overall connectivity) |
| **Notes** | This sheet shows all hierarchical blocks and their port-level connections |

### Sheet 2: Power Input and Surge Protection

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Vehicle power entry, fusing, transient protection, reverse polarity |
| **Key Components** | F1 (5A fuse), D1 (TVS diode), Q1 (80V PMOS) |
| **Interfaces** | Input: J100 vehicle connector power pins; Output: 12V_PROTECTED to Sheet 3 |
| **Critical Nets** | 12V_RAW, 12V_PROTECTED, PGND_IN |
| **Review Priority** | Critical (first line of defense, ISO 7637 compliance) |
| **Notes** | Must coordinate fuse rating with TVS clamping voltage |

### Sheet 3: Power Tree and Sequencing

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Voltage regulation, rail generation, power sequencing |
| **Key Components** | U1 (LM61460-Q1), U2 (TPS62130A-Q1), U3 (TLV75518-Q1) |
| **Interfaces** | Input: 12V_PROTECTED from Sheet 2; Output: 5V_SYS, 3V3_IO, 1V8 to all sheets |
| **Critical Nets** | 5V_SYS, 3V3_IO, 1V8, PG_5V, PG_3V3, EN_3V3, EN_1V8 |
| **Review Priority** | Critical (all subsystems depend on correct rail voltages) |
| **Notes** | Sequencing: 5V_SYS -> EN_3V3 -> PG_3V3 -> EN_1V8 |

### Sheet 4: SOM Interface Sheet

| Attribute | Detail |
|-----------|--------|
| **Purpose** | All signal connections between carrier and SoM module |
| **Key Components** | J5 (SOM connector), level shifters (if needed) |
| **Interfaces** | To/From: All subsystem sheets (CSI-2, I2C, SPI, UART, GPIO, CAN) |
| **Critical Nets** | CSI2_CLK/D[0:3]+/-, I2C_SCL/SDA, SPI_CLK/MOSI/MISO/CS_x, SOM_BOOT_OK |
| **Review Priority** | Critical (high-density, most complex routing) |
| **Notes** | Exact pin mapping per SoC profile; logical connections only (pin numbers are trade secret) |

### Sheet 5: Camera / Deserializer Sheet

| Attribute | Detail |
|-----------|--------|
| **Purpose** | DS90UB954-Q1 dual deserializer, FPD-Link III inputs, CSI-2 output |
| **Key Components** | U6 (DS90UB954-Q1), input coupling networks, PoC components |
| **Interfaces** | Input: J2/J3 (camera coax); Output: CSI-2 lanes to Sheet 4 (SOM) |
| **Critical Nets** | FPD_IN0+/-, FPD_IN1+/-, CSI2_CLK+/-, CSI2_D[0:3]+/-, LOCK |
| **Review Priority** | High (high-speed, impedance-critical) |
| **Notes** | VC mapping: Port0->VC0 (Forward), Port1->VC1 (DMS) |

### Sheet 6: Camera Module Assumptions / ICD Sheet

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Document camera module interface expectations (electrical assumptions) |
| **Key Components** | None (reference/ICD sheet) |
| **Interfaces** | Defines expected camera module electrical interface |
| **Critical Nets** | N/A (documentation sheet) |
| **Review Priority** | Medium (validation reference) |
| **Notes** | References Camera_Interface_Specification.md in 05_Interface_Control_Documents |

### Sheet 7: CAN-FD Sheet

| Attribute | Detail |
|-----------|--------|
| **Purpose** | CAN bus transceiver, termination, ESD protection, bus filtering |
| **Key Components** | U7 (TCAN1044AV-Q1), split termination network, ESD TVS |
| **Interfaces** | Input: CAN_TX/RX from Sheet 4 (SOM); Output: CAN_H/CAN_L to J100 |
| **Critical Nets** | CAN_TX, CAN_RX, CAN_H, CAN_L, CAN_STB, CAN_VIO |
| **Review Priority** | High (safety-relevant communication link) |
| **Notes** | Default mode: Normal (STB=LOW). TXD pull-up to VIO for recessive default |

### Sheet 8: USB / Storage / Debug Sheet

| Attribute | Detail |
|-----------|--------|
| **Purpose** | USB-C device interface, optional storage, debug access |
| **Key Components** | J4 (USB-C connector), ESD protection, CC resistors |
| **Interfaces** | USB_D+/D- to Sheet 4 (SOM); VBUS detection |
| **Critical Nets** | USB_DP, USB_DM, VBUS, CC1, CC2 |
| **Review Priority** | Medium (non-safety, development/logging) |
| **Notes** | Device mode only: 5.1k pulldowns on CC1/CC2 |

### Sheet 9: GNSS / IMU Sheet

| Attribute | Detail |
|-----------|--------|
| **Purpose** | GNSS receiver, active antenna bias, IMU sensor interface |
| **Key Components** | U8 (NEO-M9N-00B), U9 (BMI088), J7 (GNSS antenna) |
| **Interfaces** | UART (GNSS) to Sheet 4; SPI (IMU) to Sheet 4; PPS to SOM |
| **Critical Nets** | GNSS_TX, GNSS_RX, GNSS_PPS, IMU_SCLK, IMU_MOSI, IMU_MISO, IMU_CS_ACC, IMU_CS_GYR |
| **Review Priority** | Medium (precision timing, RF layout critical) |
| **Notes** | Both GNSS and IMU are DNI on Entry tier |

### Sheet 10: Watchdog / Reset / HMI Sheet

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Voltage supervisor, window watchdog, reset distribution, LED indicators |
| **Key Components** | U4 (TPS3808G33-Q1), U5 (TPS3431-Q1), status LEDs |
| **Interfaces** | Reset/WDI to Sheet 4 (SOM); SOM_BOOT_OK input from SOM |
| **Critical Nets** | nRESET, WDI, SOM_BOOT_OK, WDT_EN, PG_3V3 |
| **Review Priority** | High (safety-critical supervision) |
| **Notes** | Watchdog enable gated by SOM_BOOT_OK; disabled during boot |

### Sheet 11: IR Daughterboard Sheet

| Attribute | Detail |
|-----------|--------|
| **Purpose** | IR illumination control interface (J800 connector) |
| **Key Components** | J6 (8-pin header), enable/PWM buffer, current limit |
| **Interfaces** | IR_LED_EN, IR_PWM from Sheet 4 (SOM); FAULT_N back to SOM |
| **Critical Nets** | IR_LED_EN, IR_PWM, IR_FAULT_N, IR_VCC, IR_GND |
| **Review Priority** | Low (optional daughterboard, DNI on Entry) |
| **Notes** | Default state: OFF (enable pin pulled low) |

### Sheet 12: Connector / Harness Summary Sheet

| Attribute | Detail |
|-----------|--------|
| **Purpose** | All external connector pinouts, harness definition, mating table |
| **Key Components** | J100 (vehicle), J2/J3 (cameras), J4 (USB), J6 (IR), J7 (GNSS ant) |
| **Interfaces** | Summary of all external interfaces |
| **Critical Nets** | All connector-level nets |
| **Review Priority** | High (manufacturing and harness design reference) |
| **Notes** | Cross-references Vehicle_Connector_Interface_Specification.md |

---

## 3. Sheet Dependencies

```
Sheet 1 (Top)
  |
  +-- Sheet 2 (Power Input) --> Sheet 3 (Power Tree) --> All sheets
  |
  +-- Sheet 4 (SOM) <--> Sheet 5 (Camera)
  |                  <--> Sheet 7 (CAN)
  |                  <--> Sheet 8 (USB)
  |                  <--> Sheet 9 (GNSS/IMU)
  |                  <--> Sheet 10 (Watchdog)
  |                  <--> Sheet 11 (IR)
  |
  +-- Sheet 6 (Camera ICD) -- reference only
  |
  +-- Sheet 12 (Connector Summary) -- reference only
```

---

## 4. Review Priority Summary

| Priority | Sheets | Rationale |
|----------|--------|-----------|
| Critical | 2, 3, 4 | Power integrity and SOM connectivity affect all subsystems |
| High | 1, 5, 7, 10, 12 | Safety-relevant or high-speed signal integrity |
| Medium | 6, 8, 9 | Functional but lower risk |
| Low | 11 | Optional daughterboard interface |

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1.0 | 2024-01-15 | -- | Initial sheet hierarchy definition |
