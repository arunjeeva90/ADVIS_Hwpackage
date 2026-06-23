# ADVIS System Functional Test Plan

| Field | Value |
|-------|-------|
| Document ID | ADVIS-VT-FT-001 |
| Version | 0.1 |
| Status | Draft |
| Author | System Validation Team |
| Date | 2024-01-15 |
| Classification | CONFIDENTIAL |

---

## 1. Scope

This document defines the system-level functional test plan for the ADVIS ECU. Tests verify correct operation of all subsystems in an integrated configuration, covering power-on through steady-state operation and graceful shutdown.

## 2. Test Equipment

| Equipment | Purpose |
|-----------|---------|
| Automotive power supply (6-40V programmable) | Battery simulation |
| CAN-FD bus simulator (Vector CANoe or equivalent) | Vehicle bus emulation |
| Reference forward-facing camera module | ADAS camera stimulus |
| Reference DMS camera module (IR-sensitive) | Driver monitoring stimulus |
| GNSS RF simulator (Spirent or equivalent) | Controlled position/velocity |
| USB host/analyzer | USB device enumeration test |
| Logic analyzer (16+ channels) | Digital signal verification |
| Thermal chamber (-40C to +85C) | Temperature sweep |
| IR power meter (IEC 62471 rated) | IR illumination measurement |
| Target mannequin head (DMS reference) | DMS functional target |

## 3. Functional Test Cases

### 3.1 Power-On Sequence Verification

| Step | Stimulus | Expected Response | Pass Criteria |
|------|----------|-------------------|---------------|
| 1 | Apply 13.5V to input | TVS does not clamp (below threshold) | V_in present at PMOS gate |
| 2 | - | PMOS enables, VIN_PROT rises | V_PROT = VIN - V_DS(on) < 50mV |
| 3 | - | LM61460 starts, 5V_SYS rises | 5V_SYS = 5.0V +/- 2% within 5ms |
| 4 | - | TPS62130A starts, 3V3_IO rises | 3V3_IO = 3.3V +/- 3% within 10ms |
| 5 | - | TLV75518 starts, 1V8_CORE rises | 1V8_CORE = 1.8V +/- 3% within 12ms |
| 6 | - | TPS3808G33 deasserts RESET | RESET_N goes HIGH after 3V3 stable |
| 7 | - | SoM receives power enable | SOM_PWR_EN asserted |
| 8 | - | SoM boot begins | SOM_BOOT_OK remains LOW |
| 9 | - | SoM completes boot | SOM_BOOT_OK goes HIGH (< 30s) |
| 10 | - | Watchdog enabled | TPS3431 WDI toggling begins |
| 11 | - | System ready | CAN heartbeat transmitted |

### 3.2 Camera Lock and Streaming

#### Forward Camera (VC0)

| Step | Stimulus | Expected Response | Pass Criteria |
|------|----------|-------------------|---------------|
| 1 | Power-on complete | DS90UB954 initializes | I2C ACK from deserializer |
| 2 | Camera connected | FPD-Link III lock acquired | LOCK_STS register = 0x01 |
| 3 | - | CSI-2 VC0 streaming begins | Frame counter incrementing |
| 4 | - | Image data valid | No CRC errors for 1000 frames |
| 5 | Disconnect camera | Link loss detected | LOCK_STS = 0x00 within 100ms |
| 6 | Reconnect camera | Link re-established | Lock within 500ms |

#### DMS Camera (VC1)

| Step | Stimulus | Expected Response | Pass Criteria |
|------|----------|-------------------|---------------|
| 1 | Power-on complete | DS90UB954 VC1 initializes | I2C configuration successful |
| 2 | DMS camera connected | FPD-Link III lock on port 1 | LOCK_STS bit[1] = 1 |
| 3 | IR_LED_EN asserted | IR LEDs illuminate | IR power meter reads > 0 |
| 4 | IR_PWM active | IR intensity modulated | PWM duty matches commanded |
| 5 | - | DMS image visible (IR) | Frame valid, faces detectable |
| 6 | IR_LED_EN deasserted | IR LEDs off | IR power = 0, no residual glow |

### 3.3 CAN-FD Communication

| Step | Stimulus | Expected Response | Pass Criteria |
|------|----------|-------------------|---------------|
| 1 | System ready | CAN heartbeat TX | 100ms periodic, correct ID |
| 2 | Send CAN message to DUT | DUT processes message | ACK on bus, no error frame |
| 3 | Send 500kbps arbitration frame | Correct decode | Message content matches |
| 4 | Send 5Mbps data phase (FD) | Correct FD decode | Payload CRC valid |
| 5 | Bus-off recovery test | Force 256 error frames | DUT recovers < 2s |
| 6 | 70% bus load | DUT still communicates | No message loss in DUT TX |
| 7 | STB pin toggle | Standby mode entry | Bus driver enters low-power |

### 3.4 GNSS Acquisition

| Step | Stimulus | Expected Response | Pass Criteria |
|------|----------|-------------------|---------------|
| 1 | Power-on, antenna connected | NEO-M9N initializes | UART NMEA output begins |
| 2 | RF simulator: cold start | Time-to-first-fix (TTFF) | TTFF < 30s (cold) |
| 3 | RF simulator: warm start | TTFF warm | TTFF < 5s (warm) |
| 4 | RF simulator: known position | Position output | Accuracy < 2.5m CEP |
| 5 | RF simulator: velocity | Velocity output | Speed accuracy < 0.1 m/s |
| 6 | Antenna disconnect | Loss of fix reported | Fix status = "No Fix" within 5s |
| 7 | RF interference (CW) | Degraded but recoverable | Re-acquires within 10s after clear |

### 3.5 IMU Data Readout (BMI088)

| Step | Stimulus | Expected Response | Pass Criteria |
|------|----------|-------------------|---------------|
| 1 | SPI bus initialized | Chip ID readable | ACC: 0x1E, GYRO: 0x0F |
| 2 | Static (flat, no motion) | Accel reads ~0, 0, 1g | Z-axis: 9.81 +/- 0.5 m/s^2 |
| 3 | Static | Gyro reads ~0 | All axes < 1 deg/s |
| 4 | Known rotation (rate table) | Gyro output matches | Within +/- 1% of reference |
| 5 | Data rate = ODR max | All samples received | No SPI errors, no data gaps |
| 6 | Self-test (built-in) | Self-test response | Within BMI088 spec limits |
| 7 | Dual CS operation | Both dies respond | No bus contention |

### 3.6 Watchdog Operation (TPS3431)

| Step | Stimulus | Expected Response | Pass Criteria |
|------|----------|-------------------|---------------|
| 1 | During boot (WD disabled) | No reset | WDI not toggling, no timeout |
| 2 | SOM_BOOT_OK asserted | WD enable | WDI toggling begins at < t_wd |
| 3 | Normal operation | Periodic WDI toggle | RESET_N stays HIGH |
| 4 | Stop WDI toggle (simulate hang) | Watchdog timeout | RESET_N asserts within t_wd |
| 5 | After WD reset | System reboots | Full power sequence restarts |
| 6 | WDI toggle too fast | No false trigger | Normal operation maintained |
| 7 | WDI toggle just within window | No reset | Margin verified |

**Watchdog Timing:**
- Window: Configurable via external resistor
- Nominal timeout: 1.6s (typical TPS3431 configuration)
- Minimum toggle rate: > 100 ms before timeout

### 3.7 USB Enumeration

| Step | Stimulus | Expected Response | Pass Criteria |
|------|----------|-------------------|---------------|
| 1 | Connect USB-C cable to host | USB device detected | Host shows new device |
| 2 | - | Enumeration completes | Device descriptor readable |
| 3 | - | High-speed negotiation | 480 Mbps confirmed |
| 4 | Data transfer (bulk) | Correct data exchange | Zero errors in 1 GB transfer |
| 5 | Disconnect/reconnect | Re-enumeration | < 5s to re-enumerate |
| 6 | CC orientation detection | Both orientations work | Flip cable, re-test |
| 7 | Verify 5.1k CC pulldowns | Device mode maintained | No source mode assertion |

### 3.8 IR Daughterboard Control

| Step | Stimulus | Expected Response | Pass Criteria |
|------|----------|-------------------|---------------|
| 1 | IR_LED_EN = LOW | IR LEDs off | Zero emission (measured) |
| 2 | IR_LED_EN = HIGH, IR_PWM = 100% | Full IR illumination | Within +/- 10% of rated power |
| 3 | IR_PWM = 50% | Half intensity | Measured 50% +/- 5% of full |
| 4 | IR_PWM = 10% | Low intensity | Linear response verified |
| 5 | Thermal limit approach | IR current derated | No thermal damage |
| 6 | IR_LED_EN toggled rapidly | Clean on/off transitions | Rise/fall < 1 ms |
| 7 | IEC 62471 measurement | Eye safety compliance | Exempt or Risk Group 1 |

### 3.9 Thermal Protection

| Step | Stimulus | Expected Response | Pass Criteria |
|------|----------|-------------------|---------------|
| 1 | Monitor SoM temperature sensor | Reading in expected range | 25C +/- 10C at room temp |
| 2 | Apply thermal stress (chamber) | Temperature rising | Sensor tracks correctly |
| 3 | Cross warning threshold | System reports warning | CAN message with thermal flag |
| 4 | Cross critical threshold | Graceful shutdown initiated | Cameras disabled, then power |
| 5 | Temperature drops below hysteresis | System restarts | Full boot sequence |

## 4. Integration Test Matrix

| Test | Forward Cam | DMS Cam | CAN | GNSS | IMU | USB | IR | WDT |
|------|-------------|---------|-----|------|-----|-----|-----|-----|
| Boot sequence | - | - | - | - | - | - | - | Verify |
| Steady state | Stream | Stream | TX/RX | Fix | Read | Enum | On | Toggle |
| CAN bus-off | Stream | Stream | Recovery | Fix | Read | - | On | Toggle |
| Camera disconnect | Fail/recover | Stream | Report | Fix | Read | - | On | Toggle |
| GNSS jamming | Stream | Stream | TX/RX | Degrade | Read | - | On | Toggle |
| WDT timeout | - | - | - | - | - | - | - | Reset |
| Thermal shutdown | Off | Off | Last msg | Off | Off | Off | Off | Off |
| Power loss | - | - | - | - | - | - | - | - |

## 5. Pass/Fail Summary Template

| Test Case | Result | Notes | Tested By | Date |
|-----------|--------|-------|-----------|------|
| 3.1 Power-On Sequence | | | | |
| 3.2 Forward Camera | | | | |
| 3.2 DMS Camera | | | | |
| 3.3 CAN-FD | | | | |
| 3.4 GNSS | | | | |
| 3.5 IMU | | | | |
| 3.6 Watchdog | | | | |
| 3.7 USB | | | | |
| 3.8 IR Control | | | | |
| 3.9 Thermal Protection | | | | |

## 6. Test Environment Requirements

- All tests at 25C unless otherwise specified
- Temperature sweep tests: -40C, -20C, 0C, 25C, 55C, 85C
- Input voltage for most tests: 13.5V (sweep 6V-36V for power tests)
- CAN bus terminated with 120 ohm at each end
- GNSS antenna: active antenna or RF simulator

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2024-01-15 | System Validation Team | Initial draft |
