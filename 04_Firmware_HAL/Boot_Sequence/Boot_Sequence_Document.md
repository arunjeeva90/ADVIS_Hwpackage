# ADVIS Boot Sequence Document

**Document ID:** ADVIS-FW-BOOT-001  
**Version:** 0.1.0  
**Status:** Draft  
**Last Updated:** 2024-01-15

---

## 1. Purpose

This document defines the complete boot sequence for the ADVIS ECU from power-on through
system-ready state. It covers power sequencing, SOM initialization, peripheral bring-up,
watchdog activation, and the criteria for declaring the system operational.

---

## 2. Boot Flow Overview

```
                    POWER ON (IGN or WAKE)
                           |
                           v
              +------------------------+
              | Stage 1: Power Entry   |  t=0ms
              | 12V present on J100    |
              +------------------------+
                           |
                           v
              +------------------------+
              | Stage 2: Protection    |  t=0-5ms
              | PMOS gate charges      |
              | 12V_PROTECTED stable   |
              +------------------------+
                           |
                           v
              +------------------------+
              | Stage 3: 5V Rail       |  t=5-15ms
              | LM61460-Q1 soft-start  |
              | 5V_SYS stable, PG_5V   |
              +------------------------+
                           |
                           v
              +------------------------+
              | Stage 4: 3.3V Rail     |  t=15-25ms
              | TPS62130A-Q1 enabled   |
              | 3V3_IO stable, PG_3V3  |
              +------------------------+
                           |
                           v
              +------------------------+
              | Stage 5: 1.8V Rail     |  t=25-35ms
              | TLV75518-Q1 enabled    |
              | 1V8 stable             |
              +------------------------+
                           |
                           v
              +------------------------+
              | Stage 6: Supervisor    |  t=35-50ms
              | TPS3808G33 releases    |
              | nRESET de-asserted     |
              +------------------------+
                           |
                           v
              +------------------------+
              | Stage 7: SOM Boot      |  t=50ms - 5s
              | Bootloader -> Kernel   |
              | -> User space          |
              +------------------------+
                           |
                           v
              +------------------------+
              | Stage 8: HAL Init      |  t=5-8s
              | Peripheral drivers     |
              | Camera lock acquired   |
              +------------------------+
                           |
                           v
              +------------------------+
              | Stage 9: WDT Enable    |  t=8-9s
              | SOM_BOOT_OK asserted   |
              | TPS3431 enabled        |
              | First WDI kick sent    |
              +------------------------+
                           |
                           v
              +------------------------+
              | Stage 10: System Ready |  t=9-10s
              | CAN diagnostic: READY  |
              | Application starts     |
              +------------------------+
```

---

## 3. Detailed Stage Descriptions

### Stage 1: Power Entry (t=0)

| Event | Condition | Monitoring |
|-------|-----------|------------|
| 12V applied to J100 | Vehicle ignition ON or WAKE signal | None (passive) |
| Input current inrush | Limited by input capacitance and fuse | Fuse protects against short |
| Input voltage range | 9V to 16V nominal, 6V to 36V transient | TVS clamps transients |

### Stage 2: Protection Pass-through (t=0 to 5ms)

| Event | Condition | Timing |
|-------|-----------|--------|
| TVS standby | No clamping at nominal voltage | Immediate |
| PMOS gate charge | Gate driver charges PMOS gate | < 1ms |
| 12V_PROTECTED stable | PMOS fully enhanced, Rdson low | < 5ms |

### Stage 3: 5V Rail Generation (t=5 to 15ms)

| Event | Condition | Timing |
|-------|-----------|--------|
| LM61460-Q1 EN asserted | Always-on or tied to 12V_PROTECTED | At 12V_PROTECTED stable |
| Soft-start ramp | Output ramps monotonically to 5.0V | 5-10ms (SS capacitor) |
| PG_5V asserted | Output within 95% of target | After soft-start complete |
| 5V_SYS stable | Available for downstream loads | t=15ms |

### Stage 4: 3.3V Rail Generation (t=15 to 25ms)

| Event | Condition | Timing |
|-------|-----------|--------|
| TPS62130A-Q1 EN asserted | Triggered by PG_5V | At PG_5V assertion |
| Soft-start ramp | Output ramps to 3.3V | 5-10ms |
| PG_3V3 asserted | Output within regulation | After soft-start |
| 3V3_IO available | Supervisor and peripherals powered | t=25ms |

### Stage 5: 1.8V Rail Generation (t=25 to 35ms)

| Event | Condition | Timing |
|-------|-----------|--------|
| TLV75518-Q1 EN asserted | Triggered by PG_3V3 | At PG_3V3 assertion |
| LDO startup | Output reaches 1.8V | < 5ms (LDO, fast) |
| 1V8 available | SOM core domain powered | t=35ms |

### Stage 6: Supervisor Release (t=35 to 50ms)

| Event | Condition | Timing |
|-------|-----------|--------|
| TPS3808G33 monitors 3V3_IO | Threshold check passes | Continuous |
| Reset timer expires | Internal delay after threshold met | 10-15ms typical |
| nRESET de-asserted | SOM allowed to begin boot | t=50ms |
| Watchdog DISABLED | TPS3431 EN=LOW (SOM_BOOT_OK not yet asserted) | Remains off |

### Stage 7: SOM Boot (t=50ms to 5s)

| Event | Timing (typical) | Notes |
|-------|-------------------|-------|
| ROM bootloader | 50-200ms | SoC-internal, fixed |
| SPL/U-Boot | 200ms-2s | Board init, DRAM, clocks |
| Linux kernel | 2-4s | Device tree, driver probe |
| User-space init | 4-5s | systemd/init, HAL service start |

### Stage 8: HAL Initialization (t=5 to 8s)

| Peripheral | Init Action | Success Criteria | Timeout |
|-----------|-------------|------------------|---------|
| GPIO | Configure all control pins | Pin state readable | 100ms |
| I2C | Open bus, set speed 400kHz | Bus available | 200ms |
| SPI | Open bus, configure mode/speed | Bus available | 200ms |
| DS90UB954 | Full configuration (see Driver Spec) | Both ports LOCKED | 2s |
| TCAN1044AV | Set Normal mode (STB=LOW) | Bus active | 100ms |
| NEO-M9N | UART open, configure messages | First UBX response | 1s |
| BMI088 | SPI init, read chip IDs, configure | Valid data samples | 500ms |

### Stage 9: Watchdog Enable (t=8 to 9s)

| Event | Action | Timing |
|-------|--------|--------|
| All critical peripherals initialized | Prerequisite check | -- |
| SOM_BOOT_OK GPIO asserted HIGH | Firmware drives pin | Immediate |
| TPS3431 enable latches | WDT starts counting | Hardware, immediate |
| First WDI kick sent | Firmware toggles WDI | Within 100ms of enable |
| Watchdog service thread started | Periodic kick at configured interval | Continuous |

### Stage 10: System Ready (t=9 to 10s)

| Event | Action | Notes |
|-------|--------|-------|
| CAN diagnostic message sent | "System Ready" status frame | Indicates operational |
| Application layer started | Perception / DMS / Logging | Main processing begins |
| Status LED set | Solid green (or per HMI spec) | Visual confirmation |
| System timer baseline | Record boot completion time | Diagnostics logging |

---

## 4. Timing Budget Summary

| Stage | Duration | Cumulative | Critical Path |
|-------|----------|------------|---------------|
| Power Entry | 0ms | 0ms | -- |
| Protection | 5ms | 5ms | PMOS gate charge |
| 5V Generation | 10ms | 15ms | LM61460 soft-start |
| 3.3V Generation | 10ms | 25ms | TPS62130A soft-start |
| 1.8V Generation | 10ms | 35ms | TLV75518 startup |
| Supervisor Release | 15ms | 50ms | TPS3808 delay timer |
| SOM Boot | 5000ms | 5050ms | Linux kernel + init |
| HAL Init | 3000ms | 8050ms | Camera lock (longest) |
| Watchdog Enable | 100ms | 8150ms | GPIO assertion |
| System Ready | 500ms | 8650ms | CAN stack ready |

**Total boot time target: < 10 seconds from power-on to system ready**

---

## 5. Failure Modes and Recovery

| Failure | Detection | Recovery Action |
|---------|-----------|-----------------|
| 5V rail fails to start | No PG_5V after 50ms | System remains off (hardware protection) |
| 3.3V rail fails | No PG_3V3 after 50ms of PG_5V | System remains in reset |
| SOM fails to boot | No SOM_BOOT_OK after 30s | Hardware WDT not enabled; power cycle required |
| Camera no lock | LOCK pin stays low after 5s | Boot continues in degraded mode, log fault |
| CAN bus error | Bus-off detected | Auto-recovery per ISO 11898 |
| GNSS no response | UART timeout 5s | Continue without GNSS, log warning |
| IMU self-test fail | Self-test returns error | Continue without IMU, log critical |
| Watchdog timeout | TPS3431 asserts RESET | Full system reset, reboot from Stage 6 |

### 5.1 Safe State Definition

If the system cannot complete boot or a critical failure occurs:
- All actuation requests cease (CAN messages stop)
- IR LEDs disabled (hardware default)
- CAN diagnostic: fault frame transmitted (if bus available)
- System attempts reboot (watchdog reset)
- After 3 consecutive boot failures: remain in safe shutdown state

---

## 6. Power-Down Sequence

```
IGN OFF or SLEEP command
    |
    v
1. Send CAN "Going to Sleep" notification
2. Disable IR LEDs (ir_set_mode(false, 0))
3. Flush storage buffers
4. Stop camera streaming
5. Set CAN to Standby mode (STB=HIGH)
6. De-assert SOM_BOOT_OK (disables watchdog)
7. SOM initiates kernel shutdown
8. Power rails discharge in reverse order (1.8V -> 3.3V -> 5V)
9. System enters zero-current state
```

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1.0 | 2024-01-15 | -- | Initial boot sequence document |
