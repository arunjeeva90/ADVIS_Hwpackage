# ADVIS Pin Multiplexing Strategy

## Version
v1.0 - June 2026

## Document ID
ICD-MUX-001

## Classification
CONFIDENTIAL - Strategy document only. Exact pin assignments per SoC variant are TRADE SECRET and maintained in separate, restricted-access documents.

---

## 1. Purpose

This document defines the pin multiplexing strategy for the ADVIS platform across supported SoC variants. It describes the methodology for allocating SoC peripheral functions to carrier board interfaces without revealing the specific pin-to-function mapping (which is trade-secret-protected).

---

## 2. Pin Mux Philosophy

Modern automotive SoCs provide hundreds of I/O pins, many of which can serve multiple functions through multiplexing registers. The ADVIS platform requires a consistent set of peripheral functions regardless of which SoC is installed. The pin mux strategy ensures:

1. All required carrier functions are available on every supported SoC
2. Pin conflicts between peripherals are resolved at design time
3. Firmware can apply the correct mux configuration based on SoC detection
4. Future SoC variants can be evaluated quickly for carrier compatibility

---

## 3. Required Peripheral Allocation

| Function | Peripheral Type | Instance | Priority |
|----------|----------------|----------|----------|
| Camera CSI-2 | MIPI CSI-2 Rx | 1 port, 4 lanes | MANDATORY |
| Camera I2C | I2C Master | 1 instance | MANDATORY |
| IMU SPI | SPI Master | 1 instance, 2 CS | MANDATORY |
| GNSS UART | UART | 1 instance (TX+RX) | MANDATORY |
| Debug UART | UART | 1 instance (TX+RX) | MANDATORY |
| CAN-FD | MCAN | 1 instance (TXD+RXD) | MANDATORY |
| USB 2.0 | USB | 1 port (D+/D-) | MANDATORY |
| SD/MMC | SDHC | 1 instance (4-bit) | MANDATORY |
| SOM_BOOT_OK | GPIO output | 1 pin | MANDATORY |
| RESET_N input | GPIO/Reset | 1 pin | MANDATORY |
| IR_LED_EN | GPIO output | 1 pin | MANDATORY |
| IR_PWM | PWM/Timer output | 1 pin | MANDATORY |
| CAN_STB | GPIO output | 1 pin | MANDATORY |
| IMU_INT_A | GPIO input (IRQ) | 1 pin | MANDATORY |
| IMU_INT_G | GPIO input (IRQ) | 1 pin | MANDATORY |
| GNSS_PPS | GPIO input (IRQ) | 1 pin | MANDATORY |
| WDI output | GPIO output | 1 pin | MANDATORY |
| Spare GPIO | GPIO | 4 pins minimum | DESIRABLE |

---

## 4. Allocation Methodology

### 4.1 Step 1: Identify Fixed-Function Pins

Some SoC pins are dedicated (not multiplexed):
- CSI-2 data lanes (differential, dedicated PHY pins)
- USB D+/D- (dedicated PHY pins)
- DDR interface (dedicated, SoM-internal)
- Power/ground pins

These are allocated first with no conflict risk.

### 4.2 Step 2: Allocate High-Speed Peripherals

Next priority goes to peripherals with routing constraints:
- SPI (requires short traces, matched if high-speed)
- I2C (requires specific pull-up values)
- CAN (requires proximity to PHY)

These are allocated to pins physically close to their corresponding carrier-board components.

### 4.3 Step 3: Allocate Standard Peripherals

- UART instances (GNSS, Debug)
- SD/MMC interface
- PWM (IR_PWM)

These have flexible routing requirements and can use any available mux option.

### 4.4 Step 4: Allocate GPIO

Remaining GPIO functions are assigned to pins that:
- Support interrupt capability (for INT_A, INT_G, PPS, FAULT_N)
- Are not consumed by higher-priority peripheral mux options
- Are physically accessible in the carrier layout

### 4.5 Step 5: Document Conflicts and Alternatives

For each SoC variant, document:
- Which mux options were selected
- Which mux options conflict (cannot be used simultaneously)
- Fallback pins if primary selection is unavailable

---

## 5. Per-SoC Variant Strategy

### 5.1 AM62A (ADVIS Assist / Fleet)

| Aspect | Strategy |
|--------|----------|
| CSI-2 | Single 4-lane port (only option) |
| I2C | Use dedicated I2C instance closest to SoM connector edge |
| SPI | Main SPI instance with 2 hardware CS |
| UART (GNSS) | UART instance on ball group facing GNSS module |
| UART (Debug) | Separate UART instance, accessible on debug header |
| CAN | MCAN0 preferred (proximity to connector) |
| USB | USB0 (device mode) |
| GPIO | Allocated from General Purpose I/O bank |
| Conflicts | SPI CS shares mux with some timer outputs - resolved by using GPIO-driven CS |

### 5.2 AM68A / TDA4VM (ADVIS Control)

| Aspect | Strategy |
|--------|----------|
| CSI-2 | Use first 4-lane CSI-2 Rx port |
| I2C | I2C instance shared with camera configuration path |
| SPI | Main SPI instance, hardware CS for both accelerometer and gyro |
| UART (GNSS) | UART instance near WKUP domain (for low-power GPS tracking) |
| UART (Debug) | MAIN domain UART, directly to debug header |
| CAN | MCAN0 (main domain) |
| USB | USB0 device mode (USB 2.0) |
| GPIO | Mix of MAIN and WKUP domain GPIO |
| Conflicts | Second CSI-2 port reserved for future expansion - not muxed away |

### 5.3 TDA4VH (ADVIS Fusion)

| Aspect | Strategy |
|--------|----------|
| CSI-2 | First 4-lane port for cameras, second reserved for radar/expansion |
| I2C | Multiple I2C instances available, one dedicated to camera |
| SPI | Two SPI instances available (one for IMU, one spare) |
| UART | Multiple UART instances, straightforward allocation |
| CAN | MCAN0 for vehicle CAN, MCAN1 reserved for radar (future) |
| USB | USB0 device, USB1 reserved |
| GPIO | Abundant, no conflict expected |
| Conflicts | Minimal - TDA4VH has more peripherals than carrier requires |

### 5.4 SA8295P (ADVIS Fusion Premium)

| Aspect | Strategy |
|--------|----------|
| CSI-2 | Use QUP-based CSI-2 Rx |
| I2C | QUP instance configured as I2C master |
| SPI | QUP instance configured as SPI master |
| UART | QUP instances configured as UART |
| CAN | QUP-based CAN-FD interface |
| USB | USB controller (device mode) |
| GPIO | TLMM GPIO |
| Conflicts | QUP sharing requires careful instance planning |
| Notes | Different SoM form factor may require adapter |

---

## 6. Firmware Mux Configuration

### 6.1 Device Tree Approach (Linux-based SoMs)

Pin mux is configured in the device tree source (DTS) file specific to each SoC variant:

```
Carrier DTS files (one per SoC variant):
  advis-carrier-am62a.dts
  advis-carrier-am68a.dts
  advis-carrier-tda4vh.dts
```

Each DTS file contains the complete pinmux configuration for that SoC variant, mapping SoC pins to the correct peripheral functions as defined in the restricted pin mux tables.

### 6.2 SoC Detection at Boot

The bootloader identifies the installed SoM variant via:
1. I2C EEPROM on SoM (contains variant ID)
2. GPIO strap pins (if EEPROM not available)
3. SoC ID register readback

Based on detection, the correct device tree overlay is loaded.

---

## 7. Validation Checklist

| Check | Method | Pass Criteria |
|-------|--------|---------------|
| All MANDATORY peripherals allocated | Review mux table | No unallocated mandatory function |
| No pin conflicts | Cross-reference mux registers | No two functions share same pin |
| Interrupt-capable pins for IRQ functions | SoC datasheet review | INT_A, INT_G, PPS on IRQ-capable pins |
| PWM-capable pin for IR_PWM | SoC datasheet review | Timer/PWM peripheral available |
| Physical routing feasible | Layout review | Pin location allows clean routing |

---

## 8. Revision History

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| 1.0 | 2026-06 | Firmware Team | Initial strategy release |
