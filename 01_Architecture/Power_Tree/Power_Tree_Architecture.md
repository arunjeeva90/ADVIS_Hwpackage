# ADVIS Power Tree Architecture

## Version
v1.0 - June 2026

## Document ID
ARCH-PWR-001

---

## 1. Overview

This document defines the complete power distribution tree for the ADVIS ECU platform, from the 12V vehicle battery input through all regulated output rails. The power architecture prioritizes automotive-grade protection, sequenced startup, and clean power for sensitive analog and digital loads.

**Safety boundary:** Power sequencing ensures the system enters a known-safe state on startup. The watchdog ensures the system returns to a safe state if the processor becomes unresponsive.

---

## 2. Power Tree Block Diagram

```
   VEHICLE 12V BATTERY
         |
         | (8V - 16V operating, 42V load dump survival)
         v
   +----------+
   | FUSE     |
   | 5A Blade |
   +----------+
         |
         v
   +----------+
   | TVS      |  Bidirectional, Vclamp < 42V
   | Diode    |  (absorbs load dump, reverse transients)
   +----------+
         |
         v
   +-----------+
   | PMOS      |  80V rated P-channel MOSFET
   | Reverse   |  Gate driven by voltage divider
   | Polarity  |  Blocks reverse battery connection
   | Protect   |
   +-----------+
         |
         | V_PROTECTED (9V - 16V, protected)
         v
   +================+
   | LM61460-Q1     |  Wide-VIN Synchronous Buck
   | 6A, 5V Output  |  Input: V_PROTECTED
   | Fsw: 2.1 MHz   |  Output: 5V_SYS +/- 3%
   | Automotive-Q    |  Enable: Always (follows input)
   +================+
         |
         | 5V_SYS Rail (6A max)
         |
         +------------------+--------------------+
         |                  |                    |
         v                  v                    v
   +-----------+    +-------------+    +-----------------+
   | SoM PMIC  |    | TPS62130A   |    | System Loads    |
   | Input     |    | -Q1         |    | (USB VBUS opt,  |
   | (5V)      |    | 3.3V, 3A   |    |  IR board pwr)  |
   |           |    | Buck        |    |                 |
   +-----------+    +-------------+    +-----------------+
                          |
                          | 3V3_IO Rail (3A max)
                          |
                          +--------+--------+--------+--------+
                          |        |        |        |        |
                          v        v        v        v        v
                    DS90UB954  TCAN1044  NEO-M9N  Level    TPS3808
                    (3.3V)    (3.3V)    (3.3V)   Shift    Supervisor
                                                  (3.3V)   (3.3V)
                          |
                          v
                    +-------------+
                    | TLV75518    |
                    | -Q1         |
                    | 1.8V, 500mA |
                    | LDO         |
                    +-------------+
                          |
                          | 1V8_IO Rail (500mA max)
                          |
                          +--------+--------+
                          |        |        |
                          v        v        v
                       BMI088   I/O Level  Misc 1.8V
                       (1.8V)   Xlators    Logic
```

---

## 3. Rail Specifications

| Rail Name | Voltage | Tolerance | Max Current | Regulator | Upstream Rail |
|-----------|---------|-----------|-------------|-----------|---------------|
| 12V_BAT | 8-16V | N/A | Fuse limited 5A | Vehicle | Battery |
| V_PROTECTED | 8-16V | N/A | 5A (post-protection) | Passive | 12V_BAT |
| 5V_SYS | 5.0V | +/- 3% | 6A | LM61460-Q1 | V_PROTECTED |
| 3V3_IO | 3.3V | +/- 3% | 3A | TPS62130A-Q1 | 5V_SYS |
| 1V8_IO | 1.8V | +/- 3% | 500mA | TLV75518-Q1 | 3V3_IO |

---

## 4. Current Budget

| Rail | Load | Estimated Current | Notes |
|------|------|-------------------|-------|
| 5V_SYS | SoM PMIC | 3.5A (peak) | Processor + DDR + eMMC |
| 5V_SYS | 3V3_IO stage (input) | 2.0A (equiv) | Feeds all 3.3V loads |
| 5V_SYS | USB VBUS (optional) | 0.5A | When host mode enabled |
| 5V_SYS | IR board power | 0.3A | Via J800 connector |
| 5V_SYS | **TOTAL** | **6.3A peak** | Margin: managed by duty cycle |
| 3V3_IO | DS90UB954-Q1 | 0.8A | Deserializer + PoC sourcing |
| 3V3_IO | TCAN1044AV-Q1 | 0.07A | CAN transceiver |
| 3V3_IO | NEO-M9N | 0.05A | GNSS receiver |
| 3V3_IO | Level shifters | 0.02A | I/O translation |
| 3V3_IO | TPS3808 supervisor | 0.001A | Negligible |
| 3V3_IO | 1V8_IO stage (input) | 0.3A (equiv) | Feeds 1.8V loads |
| 3V3_IO | **TOTAL** | **1.24A typ** | Well within 3A budget |
| 1V8_IO | BMI088 | 0.005A | IMU (accel + gyro) |
| 1V8_IO | Level translators | 0.02A | Mixed-voltage I/O |
| 1V8_IO | **TOTAL** | **0.025A typ** | Well within 500mA budget |

---

## 5. Power Sequencing

The ADVIS power-up sequence is critical for proper initialization:

```
TIME -->
        ___________________
5V_SYS |___/               |  t=0: Input applied, LM61460 starts
        ___________________________
3V3_IO |_______/                   |  t=t1: TPS62130A enables after 5V_SYS PG
        _________________________________
1V8_IO |___________/                     |  t=t2: TLV75518 enables after 3V3 PG
        _______________________________________
SoM    |_______________/                       |  t=t3: SoM PMIC sequences internally
        _______________________________________________
WDG_EN |_______________________/                       |  t=t4: After SOM_BOOT_OK asserts
```

### Sequencing Rules

| Step | Condition | Action | Timing |
|------|-----------|--------|--------|
| 1 | V_PROTECTED > UVLO | LM61460-Q1 starts switching | < 5ms soft-start |
| 2 | 5V_SYS PG asserts | TPS62130A-Q1 EN pulled high | < 2ms propagation |
| 3 | 3V3_IO PG asserts | TLV75518-Q1 EN pulled high | < 1ms propagation |
| 4 | All rails stable | SoM PMIC begins internal sequence | SoM-dependent |
| 5 | SoM boot complete | SOM_BOOT_OK GPIO asserts high | Application-dependent |
| 6 | SOM_BOOT_OK = HIGH | TPS3431 watchdog enabled | Immediate |

---

## 6. Power Good Signals

| Signal | Source | Destination | Active State | Function |
|--------|--------|-------------|--------------|----------|
| PG_5V | LM61460-Q1 | Sequencing logic | High | 5V_SYS within regulation |
| PG_3V3 | TPS62130A-Q1 | Sequencing logic | High | 3V3_IO within regulation |
| RESET_N | TPS3808G33-Q1 | SoM, peripherals | Low (active) | 3V3 below threshold |
| SOM_BOOT_OK | SoM GPIO | TPS3431 enable | High | Firmware ready |

---

## 7. Protection Features

| Protection | Component | Specification |
|------------|-----------|---------------|
| Overcurrent (input) | Blade fuse | 5A blow rating |
| Overvoltage transient | TVS diode | Clamp at 42V (load dump) |
| Reverse polarity | 80V PMOS | Blocks negative voltage |
| Undervoltage lockout | LM61460-Q1 internal | Shuts down below ~4V input |
| Output short circuit | Each regulator | Hiccup/foldback mode |
| Thermal shutdown | Each regulator | OTP per device datasheet |
| Supply supervision | TPS3808G33-Q1 | Asserts RESET_N if 3V3 drops |
| Watchdog timeout | TPS3431-Q1 | Asserts RESET if WDI not toggled |

---

## 8. Thermal Considerations

| Regulator | Max Power Dissipation | Package | Theta-JA |
|-----------|-----------------------|---------|----------|
| LM61460-Q1 | ~2.5W (at full load, 12V in) | HTSSOP-16 | 35 C/W |
| TPS62130A-Q1 | ~0.3W | QFN-16 | 45 C/W |
| TLV75518-Q1 | ~0.04W | SOT-23-5 | 150 C/W |
| PMOS | ~0.5W (Rds_on * I^2) | SO-8 | 60 C/W |

Total power subsystem dissipation (worst case): approximately 3.3W

---

## 9. Design Notes

- LM61460-Q1 switching frequency (2.1 MHz) chosen to stay above AM radio band
- Input capacitance must be adequate for load-dump energy absorption
- Power sequencing uses PG daisy-chain, not a sequencer IC (reduces BOM cost)
- Watchdog is held disabled during boot to prevent premature reset
- All regulators are automotive-qualified (AEC-Q100 Grade 1, -40C to +125C junction)

---

## 10. Revision History

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| 1.0 | 2026-06 | Power Team | Initial release |
