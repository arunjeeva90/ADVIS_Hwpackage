# ADVIS Device Tree Strategy

**Document ID:** ADVIS-FW-DTS-001  
**Version:** 0.1.0  
**Status:** Draft  
**Last Updated:** 2024-01-15

---

## 1. Purpose

This document defines the device tree strategy for the ADVIS platform, enabling support
for multiple SoC variants (TDA4VM, AM68A, AM62A, future SoCs) from a common carrier
board design. The strategy uses a base + overlay architecture to maximize reuse while
accommodating SoC-specific differences.

---

## 2. Device Tree Architecture

### 2.1 Layered Structure

```
+----------------------------------------------------------+
|  SoC Vendor Base DTS                                      |
|  (e.g., k3-am68-sk.dts from TI SDK)                     |
+----------------------------------------------------------+
|  SoM Module Overlay                                       |
|  (e.g., phycore-am68a-som.dtso)                          |
|  Defines: SoM-specific memory, eMMC, Ethernet            |
+----------------------------------------------------------+
|  ADVIS Carrier Overlay    <-- THIS IS OUR IP             |
|  (advis-carrier-v1.dtso)                                 |
|  Defines: All carrier peripherals and connections        |
+----------------------------------------------------------+
|  Variant/Feature Overlays (optional)                      |
|  (advis-gnss-enable.dtso, advis-ir-enable.dtso)         |
+----------------------------------------------------------+
```

### 2.2 File Naming Convention

| File | Purpose |
|------|---------|
| `advis-carrier-v1.dtso` | Main carrier board device tree overlay |
| `advis-carrier-v1-tda4vm.dtso` | TDA4VM-specific pin mux adjustments |
| `advis-carrier-v1-am68a.dtso` | AM68A-specific pin mux adjustments |
| `advis-carrier-v1-am62a.dtso` | AM62A-specific pin mux adjustments |
| `advis-gnss-enable.dtso` | GNSS module enable (Mid/High tier) |
| `advis-imu-enable.dtso` | IMU enable (Mid/High tier) |
| `advis-ir-enable.dtso` | IR daughterboard enable (Mid/High tier) |

---

## 3. Base Carrier Overlay Structure

### 3.1 Top-Level Organization

```dts
/* advis-carrier-v1.dtso - ADVIS Carrier Board Overlay */
/dts-v1/;
/plugin/;

/ {
    compatible = "advis,carrier-v1";

    fragment@0 { /* I2C bus for DS90UB954 */ };
    fragment@1 { /* SPI bus for BMI088 */ };
    fragment@2 { /* UART for NEO-M9N */ };
    fragment@3 { /* CAN controller */ };
    fragment@4 { /* CSI-2 receiver */ };
    fragment@5 { /* GPIO definitions */ };
    fragment@6 { /* USB controller */ };
    fragment@7 { /* Power management GPIOs */ };
    fragment@8 { /* LED / HMI indicators */ };
};
```

### 3.2 Peripheral Node Definitions

#### DS90UB954-Q1 (I2C Device)

```dts
/* Camera deserializer on I2C bus */
&i2c_carrier {
    status = "okay";
    clock-frequency = <400000>;

    ds90ub954: deser@3d {
        compatible = "ti,ds90ub954-q1";
        reg = <0x3d>;
        interrupt-parent = <&gpio_carrier>;
        interrupts = <LOCK_GPIO IRQ_TYPE_EDGE_BOTH>;

        ports {
            #address-cells = <1>;
            #size-cells = <0>;

            port@0 { /* FPD-Link III input 0 (Forward Camera) */ };
            port@1 { /* FPD-Link III input 1 (DMS Camera) */ };
            port@2 { /* CSI-2 output to SOM */ };
        };
    };
};
```

#### BMI088 (SPI Device)

```dts
/* IMU on SPI bus */
&spi_carrier {
    status = "okay";

    bmi088_accel: accel@0 {
        compatible = "bosch,bmi088-accel";
        reg = <0>;  /* CS0 = accelerometer */
        spi-max-frequency = <10000000>;
        interrupt-parent = <&gpio_carrier>;
        interrupts = <INT1_ACC_GPIO IRQ_TYPE_RISING>;
    };

    bmi088_gyro: gyro@1 {
        compatible = "bosch,bmi088-gyro";
        reg = <1>;  /* CS1 = gyroscope */
        spi-max-frequency = <10000000>;
        interrupt-parent = <&gpio_carrier>;
        interrupts = <INT1_GYR_GPIO IRQ_TYPE_RISING>;
    };
};
```

#### NEO-M9N (UART Device)

```dts
/* GNSS receiver on UART */
&uart_gnss {
    status = "okay";
    current-speed = <115200>;

    gnss: gnss {
        compatible = "u-blox,neo-m9n";
        timepulse-gpios = <&gpio_carrier PPS_GPIO GPIO_ACTIVE_HIGH>;
    };
};
```

#### TCAN1044AV-Q1 (CAN PHY)

```dts
/* CAN transceiver */
&can_controller {
    status = "okay";

    can_phy: can-phy {
        compatible = "ti,tcan1044a";
        standby-gpios = <&gpio_carrier CAN_STB_GPIO GPIO_ACTIVE_HIGH>;
        max-bitrate = <5000000>;
    };
};
```

---

## 4. SoC-Specific Overlays

### 4.1 What Varies Per SoC

| Property | SoC-Dependent? | Handled By |
|----------|---------------|------------|
| I2C bus assignment | Yes | SoC overlay |
| SPI bus assignment | Yes | SoC overlay |
| UART assignment | Yes | SoC overlay |
| CAN controller instance | Yes | SoC overlay |
| CSI-2 receiver instance | Yes | SoC overlay |
| GPIO bank/pin numbers | Yes | SoC overlay |
| Pin mux registers | Yes | SoC overlay |
| Clock parent assignments | Yes | SoC overlay |
| Interrupt controller mapping | Yes | SoC overlay |
| Peripheral register addresses | No | Vendor base DTS |
| Device compatible strings | No | Carrier overlay |
| I2C addresses | No | Carrier overlay |
| SPI modes/frequencies | No | Carrier overlay |

### 4.2 Overlay Application Order

```
Boot sequence:
1. U-Boot loads vendor base DTB (e.g., k3-am68-sk.dtb)
2. U-Boot applies SoM overlay (e.g., phycore-am68a-som.dtbo)
3. U-Boot applies ADVIS carrier overlay (advis-carrier-v1.dtbo)
4. U-Boot applies SoC-specific carrier adjustments (advis-carrier-v1-am68a.dtbo)
5. U-Boot applies feature overlays based on EEPROM/config:
   - advis-gnss-enable.dtbo (if GNSS populated)
   - advis-imu-enable.dtbo (if IMU populated)
   - advis-ir-enable.dtbo (if IR board connected)
6. Kernel boots with merged device tree
```

---

## 5. Runtime Configuration

### 5.1 Board Detection

The carrier board includes an I2C EEPROM (or SOM EEPROM section) storing:

| Field | Size | Content |
|-------|------|---------|
| Board ID | 4 bytes | "ADV1" (ADVIS carrier v1) |
| HW Revision | 2 bytes | PCB revision (e.g., 0x0100 = Rev A) |
| Tier Config | 1 byte | 0x01=Entry, 0x02=Mid, 0x03=High |
| Serial Number | 16 bytes | Unique board serial |
| MAC Address | 6 bytes | Ethernet MAC (if applicable) |

### 5.2 Overlay Selection Logic (U-Boot)

```
read_eeprom_board_id()
  |
  +-- "ADV1" confirmed --> load advis-carrier-v1.dtbo
  |
  +-- read SoC type from SoM EEPROM
  |     +-- AM68A --> load advis-carrier-v1-am68a.dtbo
  |     +-- TDA4VM --> load advis-carrier-v1-tda4vm.dtbo
  |     +-- AM62A --> load advis-carrier-v1-am62a.dtbo
  |
  +-- read tier_config
        +-- 0x02 or 0x03 --> load advis-gnss-enable.dtbo
        +-- 0x02 or 0x03 --> load advis-imu-enable.dtbo
        +-- 0x02 or 0x03 --> load advis-ir-enable.dtbo
```

---

## 6. GPIO Abstraction

### 6.1 Named GPIO Strategy

Rather than hard-coding GPIO numbers, the carrier overlay uses named GPIOs:

```dts
/ {
    advis-gpios {
        compatible = "advis,carrier-gpios";

        som-boot-ok-gpios = <&gpio_x N GPIO_ACTIVE_HIGH>;
        wdi-gpios = <&gpio_x N GPIO_ACTIVE_HIGH>;
        can-stb-gpios = <&gpio_x N GPIO_ACTIVE_HIGH>;
        camera-lock-gpios = <&gpio_x N GPIO_ACTIVE_HIGH>;
        ir-enable-gpios = <&gpio_x N GPIO_ACTIVE_LOW>;
        ir-fault-gpios = <&gpio_x N GPIO_ACTIVE_LOW>;
    };
};
```

Firmware accesses GPIOs by name through the Linux GPIO consumer interface,
making the code SoC-independent.

---

## 7. Validation and Testing

### 7.1 DTS Compilation Checks

| Check | Tool | Criteria |
|-------|------|----------|
| Syntax validation | dtc (device tree compiler) | Zero errors |
| Overlay application | fdtoverlay | Clean merge, no conflicts |
| Schema validation | dt-schema (yamllint) | Conforms to bindings |
| Runtime verification | /proc/device-tree inspection | All nodes present |
| Peripheral probe | dmesg / sysfs | All drivers bound successfully |

### 7.2 Test Matrix

| SoC | SoM | Carrier Rev | Tier | Status |
|-----|-----|-------------|------|--------|
| AM68A | phyCORE | Rev A | High | Primary target |
| TDA4VM | phyCORE | Rev A | High | Secondary target |
| AM62A | TBD | Rev A | Entry | Future |
| SA8295 | TBD | Rev B | Fusion | Planned |

---

## 8. Intellectual Property Notes

- The ADVIS carrier overlay (advis-carrier-v1.dtso) is proprietary IP
- SoC-specific pin mux values reference vendor public TRM documentation
- Exact GPIO pin assignments are trade secrets (mapped by number in the overlay
  source but not disclosed in public documentation)
- Compatible strings and device tree bindings follow upstream Linux conventions

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1.0 | 2024-01-15 | -- | Initial device tree strategy document |
