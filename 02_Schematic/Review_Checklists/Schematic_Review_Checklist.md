# ADVIS Schematic Review Checklist

**Document ID:** ADVIS-SCH-CHK-001  
**Version:** 0.1.0  
**Status:** Template  
**Last Updated:** 2024-01-15

---

## 1. Overview

This checklist is used during formal schematic reviews of the ADVIS ECU carrier board.
Each subsystem has dedicated check items. All items must be signed off by the responsible
engineer before the schematic can advance to ERC-clean release status.

**Review Process:**
1. Pre-review: Designer self-check using this document
2. Peer review: Second engineer verifies each subsystem
3. Expert review: Domain expert reviews high-speed and power sections
4. Formal sign-off: Project lead approves for PCB handoff

---

## 2. Power Entry and Protection

| # | Check Item | Pass | Fail | N/A | Notes |
|---|-----------|------|------|-----|-------|
| P-01 | Input fuse rating matches system current budget (5A) | | | | |
| P-02 | TVS diode clamping voltage below PMOS absolute max rating | | | | |
| P-03 | PMOS reverse-polarity FET rated for max input voltage (80V min) | | | | |
| P-04 | PMOS gate drive circuit verified for turn-on/turn-off timing | | | | |
| P-05 | Input filter capacitors rated for ripple current | | | | |
| P-06 | Fuse coordination: TVS clamp < Fuse blow threshold | | | | |
| P-07 | Test points present on 12V_IN and post-protection node | | | | |
| P-08 | Transient immunity meets ISO 7637-2 pulse requirements | | | | |

---

## 3. Power Tree and Sequencing

| # | Check Item | Pass | Fail | N/A | Notes |
|---|-----------|------|------|-----|-------|
| V-01 | LM61460-Q1 input capacitance meets datasheet minimum (10uF ceramic min) | | | | |
| V-02 | LM61460-Q1 output capacitance meets transient response target | | | | |
| V-03 | LM61460-Q1 feedback resistor divider sets 5V output within 1% | | | | |
| V-04 | LM61460-Q1 soft-start configured for monotonic ramp | | | | |
| V-05 | TPS62130A-Q1 input from 5V_SYS, output verified at 3.3V | | | | |
| V-06 | TPS62130A-Q1 inductor rated for peak current including transients | | | | |
| V-07 | TLV75518-Q1 input from 3.3V rail, output 1.8V verified | | | | |
| V-08 | TLV75518-Q1 output capacitor ESR within stable range | | | | |
| V-09 | Power sequencing enforced: 5V -> 3.3V -> 1.8V order | | | | |
| V-10 | Power Good signals routed to SOM for health monitoring | | | | |
| V-11 | Enable chain implements correct sequencing dependencies | | | | |
| V-12 | Each rail has dedicated test point | | | | |
| V-13 | Total current budget per rail does not exceed regulator rating | | | | |

---

## 4. Supervisor and Reset

| # | Check Item | Pass | Fail | N/A | Notes |
|---|-----------|------|------|-----|-------|
| S-01 | TPS3808G33-Q1 threshold set for 3V3_IO monitoring | | | | |
| S-02 | Reset output connected to SOM reset input with correct polarity | | | | |
| S-03 | Reset pulse duration meets SOM datasheet minimum | | | | |
| S-04 | Manual reset button (if present) debounced | | | | |
| S-05 | Power-on reset timing verified against sequencing requirements | | | | |

---

## 5. Watchdog (TPS3431-Q1)

| # | Check Item | Pass | Fail | N/A | Notes |
|---|-----------|------|------|-----|-------|
| W-01 | WDI input connected to SOM heartbeat GPIO | | | | |
| W-02 | Window timing resistors set correct open/close window | | | | |
| W-03 | ENABLE pin gated by SOM_BOOT_OK signal | | | | |
| W-04 | Reset output drives appropriate system reset path | | | | |
| W-05 | Watchdog disabled during boot (ENABLE low until SOM_BOOT_OK) | | | | |
| W-06 | Test point on WDI for debug probing | | | | |

---

## 6. Camera Deserializer (DS90UB954-Q1)

| # | Check Item | Pass | Fail | N/A | Notes |
|---|-----------|------|------|-----|-------|
| C-01 | I2C address configuration resistors match firmware expectation | | | | |
| C-02 | PoC (Power-over-Coax) bias network correct for each port | | | | |
| C-03 | CSI-2 output lanes connected to SOM in correct lane order | | | | |
| C-04 | CSI-2 clock pair routed as differential pair | | | | |
| C-05 | Virtual channel mapping: VC0=Forward, VC1=DMS verified in config | | | | |
| C-06 | LOCK output connected to SOM GPIO for status monitoring | | | | |
| C-07 | Reference clock crystal/oscillator frequency correct | | | | |
| C-08 | Input termination resistors per FPD-Link III spec | | | | |
| C-09 | Decoupling capacitors on all VDD pins per datasheet | | | | |
| C-10 | ESD protection on coax input connectors | | | | |

---

## 7. CAN-FD Interface (TCAN1044AV-Q1)

| # | Check Item | Pass | Fail | N/A | Notes |
|---|-----------|------|------|-----|-------|
| N-01 | TXD recessive pull-up resistor present (value per datasheet) | | | | |
| N-02 | STB (Standby) pin connected to SOM GPIO for mode control | | | | |
| N-03 | Bus termination: 120 ohm split-termination with common-mode filter | | | | |
| N-04 | CAN_H and CAN_L routed as differential pair to connector | | | | |
| N-05 | ESD protection (TVS) on CAN bus lines at connector | | | | |
| N-06 | VIO level matches SOM I/O voltage (3.3V or 1.8V) | | | | |
| N-07 | Decoupling on VCC and VIO pins | | | | |

---

## 8. GNSS (NEO-M9N-00B)

| # | Check Item | Pass | Fail | N/A | Notes |
|---|-----------|------|------|-----|-------|
| G-01 | UART TX/RX connected to SOM with correct direction | | | | |
| G-02 | PPS output connected to SOM timer-capture input | | | | |
| G-03 | Antenna feed: RF connector with proper ground plane clearance | | | | |
| G-04 | LNA bias (if active antenna) power and filtering correct | | | | |
| G-05 | Backup battery for hot-start (if implemented) | | | | |
| G-06 | I2C address not conflicting with other bus devices | | | | |
| G-07 | Decoupling per u-blox hardware integration manual | | | | |

---

## 9. IMU (BMI088)

| # | Check Item | Pass | Fail | N/A | Notes |
|---|-----------|------|------|-----|-------|
| I-01 | Dual chip-select: separate CS for accelerometer and gyroscope | | | | |
| I-02 | SPI clock frequency within BMI088 maximum rating | | | | |
| I-03 | Interrupt outputs (INT1_ACC, INT1_GYR) connected to SOM GPIOs | | | | |
| I-04 | Mounting orientation documented and aligned with vehicle axes | | | | |
| I-05 | Decoupling capacitors per Bosch application note | | | | |
| I-06 | No other devices sharing SPI bus (or proper CS management) | | | | |

---

## 10. USB Interface

| # | Check Item | Pass | Fail | N/A | Notes |
|---|-----------|------|------|-----|-------|
| U-01 | USB-C connector CC1/CC2 pulldown resistors (5.1k) for device mode | | | | |
| U-02 | D+/D- routed as 90 ohm differential pair | | | | |
| U-03 | ESD protection on VBUS, D+, D-, CC lines | | | | |
| U-04 | VBUS detection circuit for SOM notification | | | | |
| U-05 | Shield connected to chassis ground through capacitor | | | | |

---

## 11. General Checks

| # | Check Item | Pass | Fail | N/A | Notes |
|---|-----------|------|------|-----|-------|
| X-01 | All unused IC pins handled per datasheet recommendation | | | | |
| X-02 | Silkscreen: RefDes visible, polarity marked, pin 1 indicated | | | | |
| X-03 | Decoupling strategy: 100nF per digital VDD pin minimum | | | | |
| X-04 | No floating inputs on any IC | | | | |
| X-05 | All pull-up/pull-down values documented with justification | | | | |
| X-06 | Voltage level compatibility verified at all domain crossings | | | | |
| X-07 | Test points on all critical signals (min: power rails, I2C, SPI, CAN) | | | | |
| X-08 | Net naming consistent with architecture signal names | | | | |
| X-09 | Ground domain connections match Ground_Domain_Architecture.md | | | | |
| X-10 | All component values within AEC-Q100/Q200 qualified range | | | | |

---

## 12. Review Sign-off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Designer | | | |
| Peer Reviewer | | | |
| Power Domain Expert | | | |
| Signal Integrity Expert | | | |
| Project Lead | | | |

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1.0 | 2024-01-15 | -- | Initial checklist template |
