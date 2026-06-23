# ADVIS Watchdog Service Design

**Document ID:** ADVIS-FW-WDT-001  
**Version:** 0.1.0  
**Status:** Draft  
**Last Updated:** 2024-01-15

---

## 1. Purpose

This document describes the design of the watchdog service for the ADVIS ECU. The service
manages the TPS3431-Q1 window watchdog, ensuring system health monitoring, boot gating,
and controlled failure recovery.

---

## 2. Hardware Context

### 2.1 TPS3431-Q1 Characteristics

| Parameter | Value | Notes |
|-----------|-------|-------|
| Device | TPS3431-Q1 | Automotive-qualified window watchdog |
| Watchdog Input | WDI (pulse edge sensitive) | Rising or falling edge resets timer |
| Reset Output | nRESET (active low, open-drain) | Drives system reset when timeout expires |
| Enable Input | ENABLE (active high) | Connected to SOM_BOOT_OK |
| Timeout Period | Set by external R/C network | Target: 1.0s to 2.0s (application-dependent) |
| Window Type | Open window (configurable) | Timeout starts after last kick |
| VCC Range | 1.5V to 6.5V | Powered from 3V3_IO rail |

### 2.2 Connection Diagram

```
                +-------------------+
                |    TPS3431-Q1     |
                |                   |
SOM GPIO A ---->| ENABLE            |
                |                   |
SOM GPIO B ---->| WDI              |
                |                   |
                |        nRESET ----|----> System Reset Network
                |                   |
     3V3_IO --->| VCC          GND |----> BOARD_GND
                +-------------------+
                     |         |
                    [R_SET]  [C_SET]  (timeout period setting)
```

---

## 3. SOM_BOOT_OK Gating Logic

### 3.1 Enable Criteria

The watchdog MUST NOT be enabled until all of the following conditions are met:

| # | Condition | Verification Method |
|---|-----------|-------------------|
| 1 | All power rails stable (5V, 3.3V, 1.8V) | Power Good signals read via GPIO |
| 2 | SOM kernel booted to user space | HAL service process running |
| 3 | Critical peripheral drivers initialized | Driver init return codes checked |
| 4 | DS90UB954 has video lock on at least one port | LOCK GPIO or I2C status |
| 5 | CAN controller initialized and bus-on | CAN driver status check |
| 6 | Watchdog service thread created and ready | Thread start confirmation |

### 3.2 Enable Sequence

```c
/* Watchdog enable procedure */
int watchdog_enable(void)
{
    /* Verify all prerequisites */
    if (!power_rails_ok())    return PLAT_ERR_NOT_READY;
    if (!camera_locked())     return PLAT_ERR_NOT_READY;
    if (!can_bus_active())    return PLAT_ERR_NOT_READY;
    if (!wdt_thread_ready())  return PLAT_ERR_NOT_READY;

    /* Assert SOM_BOOT_OK (enables TPS3431) */
    gpio_set(GPIO_SOM_BOOT_OK, HIGH);

    /* Immediately send first kick (within hardware setup time) */
    gpio_toggle(GPIO_WDI);

    /* Record enable timestamp for diagnostics */
    wdt_state.enabled_timestamp = get_system_time_ms();
    wdt_state.enabled = true;

    return PLAT_OK;
}
```

### 3.3 Why Gating is Critical

Without boot gating, the watchdog would fire during the multi-second Linux boot process
(before firmware can service it), causing an infinite reset loop. The ENABLE pin
physically prevents the TPS3431 from asserting reset until the firmware explicitly
signals readiness.

---

## 4. Heartbeat Service Thread

### 4.1 Thread Architecture

```
+-------------------------------------------------------+
| Main Application                                       |
|                                                       |
|  +------------------+   +------------------+          |
|  | Perception Task  |   | DMS Task         |          |
|  +------------------+   +------------------+          |
|                                                       |
+-------------------------------------------------------+
| Watchdog Service Thread (highest priority)             |
|                                                       |
|  while (running) {                                    |
|      check_system_health();                           |
|      if (health_ok) watchdog_kick();                  |
|      sleep(kick_interval);                            |
|  }                                                    |
+-------------------------------------------------------+
```

### 4.2 Service Thread Parameters

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Thread priority | Highest (real-time) | Must not be preempted by application |
| Scheduling policy | SCHED_FIFO | Deterministic timing |
| Kick interval | T_WD / 3 | Provides 2x margin before timeout |
| Stack size | 8 KB | Minimal, no dynamic allocation |
| CPU affinity | Core 0 (or dedicated) | Avoid migration latency |

### 4.3 Kick Interval Calculation

```
T_WD = Watchdog timeout period (hardware-set, e.g., 1.6s)

Kick interval = T_WD / 3 = 533ms

This provides:
- Normal operation: kick every 533ms, timeout at 1600ms
- If one kick is delayed: next kick at 1066ms (still within window)
- Two consecutive missed kicks: timeout at 1600ms, reset occurs
```

### 4.4 Health Check Integration

The watchdog service does not blindly kick. Before each kick, it verifies system health:

```c
typedef struct {
    bool camera_streaming;     /* At least one camera producing frames */
    bool can_bus_on;           /* CAN bus not in bus-off state */
    bool memory_ok;            /* No critical memory faults detected */
    bool cpu_temp_ok;          /* Junction temp below threshold */
    uint32_t app_heartbeat;    /* Application layer heartbeat counter */
} system_health_t;

bool check_system_health(void)
{
    system_health_t h;
    get_system_health(&h);

    /* Critical checks - do NOT kick if these fail */
    if (!h.can_bus_on) return false;
    if (!h.memory_ok) return false;

    /* Degraded checks - kick but log warning */
    if (!h.camera_streaming) log_warning("Camera not streaming");
    if (!h.cpu_temp_ok) log_warning("CPU temperature high");

    /* Application liveness - kick but escalate if stale */
    if (app_heartbeat_stale(h.app_heartbeat)) {
        log_warning("Application heartbeat stale");
        /* Still kick - let application monitoring handle this */
    }

    return true;
}
```

---

## 5. Failure Recovery

### 5.1 Watchdog Reset Path

```
WDI not toggled within T_WD
         |
         v
TPS3431 asserts nRESET (active low)
         |
         v
Reset distributed to SOM and carrier
         |
         v
SOM performs cold reset
         |
         v
Full reboot from Stage 6 (supervisor release)
         |
         v
Boot counter incremented in non-volatile storage
         |
         v
If boot_count < MAX_RETRIES(3): normal boot
If boot_count >= MAX_RETRIES: enter safe shutdown mode
```

### 5.2 Reset Cause Detection

On boot, firmware reads reset cause registers to determine why the system restarted:

| Reset Source | Detection Method | Action |
|-------------|-----------------|--------|
| Power-on reset | Supervisor POR flag | Normal boot, reset counters |
| Watchdog reset | TPS3431 status or SOM register | Increment failure counter, log |
| Software reset | SOM internal flag | Normal restart |
| External reset | Manual button (if present) | Normal boot |

### 5.3 Boot Failure Counter

```c
#define MAX_BOOT_FAILURES 3

void check_boot_failure_count(void)
{
    uint32_t count = nv_read_boot_failures();

    if (count >= MAX_BOOT_FAILURES) {
        /* Enter safe shutdown mode */
        log_critical("Max boot failures reached, entering safe state");
        can_send_fault_frame(FAULT_REPEATED_WDT_RESET);
        enter_safe_shutdown();
        /* Does not return */
    }

    /* Increment counter (cleared after successful steady-state operation) */
    nv_write_boot_failures(count + 1);
}

void clear_boot_failure_counter(void)
{
    /* Called after N seconds of successful operation */
    nv_write_boot_failures(0);
}
```

---

## 6. Safe State Definition

When the watchdog triggers and recovery is exhausted, the system enters safe state:

| Subsystem | Safe State | Rationale |
|-----------|-----------|-----------|
| CAN bus | Transmit final fault frame, then silent | No spurious actuation requests |
| Camera | Streaming stopped | Reduce power, no false detections |
| IR LEDs | Disabled (hardware default) | Thermal and eye safety |
| GNSS | Powered down | Reduce current draw |
| IMU | Powered down | Not needed in safe state |
| SOM | Remains powered (for diagnostics) | Allow OBD-II query response |
| Watchdog | Remains enabled | System stays in reset if issue persists |

### 6.1 Safety Boundary Reminder

ADVIS is an observation/processing/logging system. It generates actuation REQUESTS
to OEM controllers but does not directly control any vehicle actuator. Therefore, a
watchdog reset results in loss of perception/advisory capability only. The OEM
controller independently handles the absence of ADVIS advisory messages through its
own timeout mechanism.

---

## 7. Diagnostics and Logging

### 7.1 Watchdog Status CAN Messages

| CAN ID | Frequency | Content |
|--------|-----------|---------|
| 0x7E0 (example) | 1 Hz | WDT status, kick count, health flags |
| 0x7FF (example) | On-event | Fault frame (timeout occurred, reset cause) |

### 7.2 Logged Parameters

| Parameter | Storage | Retention |
|-----------|---------|-----------|
| Boot failure count | Non-volatile (EEPROM/flash) | Persistent across power cycles |
| Last reset cause | Non-volatile | Until next normal boot |
| Kick count since boot | RAM | Cleared on reset |
| Last health check result | RAM | Current state only |
| Watchdog enable timestamp | Flash log | Persistent |

---

## 8. Testing and Validation

### 8.1 Test Cases

| Test | Method | Expected Result |
|------|--------|-----------------|
| Normal operation | Run system for 24h | No watchdog resets |
| Kick thread kill | Kill WDT thread in test mode | System resets within T_WD |
| Slow kick | Delay kick beyond timeout | System resets |
| Boot gating | Prevent SOM_BOOT_OK assertion | WDT never enables, no resets |
| Health check fail | Inject CAN bus-off condition | WDT stops kicking, system resets |
| Recovery limit | Force 3 consecutive WDT resets | System enters safe shutdown |
| Cold start | Power cycle from 0V | Clean boot, WDT enables after init |

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1.0 | 2024-01-15 | -- | Initial watchdog service design |
