# ADVIS Peripheral Driver Specifications

**Document ID:** ADVIS-FW-DRV-001  
**Version:** 0.1.0  
**Status:** Draft  
**Last Updated:** 2024-01-15

---

## 1. Purpose

This document specifies the driver interfaces for all hardware peripherals on the ADVIS
ECU carrier board. Each driver section defines the hardware interface, configuration
parameters, runtime API, and error handling for its respective peripheral.

---

## 2. DS90UB954-Q1 Dual FPD-Link III Deserializer

### 2.1 Interface Summary

| Parameter | Value |
|-----------|-------|
| Bus | I2C (configuration), CSI-2 (data output) |
| I2C Address | 0x3D (default, configurable via ADDR pin) |
| I2C Speed | 400 kHz (Fast Mode) |
| CSI-2 Output | 4-lane MIPI, up to 2.5 Gbps/lane |
| Virtual Channels | VC0 = Forward camera, VC1 = DMS camera |
| Interrupts | LOCK/UNLOCK status change (GPIO) |

### 2.2 Configuration Sequence

```
1. Wait for power rail stable (1V8, 3V3 present)
2. Release PDB (Power-Down Bar) pin
3. Wait 10ms for internal PLL lock
4. Write PORT_CONFIG register: enable Port0, Port1
5. Write VC mapping: Port0 -> VC0, Port1 -> VC1
6. Write CSI-2 lane config: 4-lane output mode
7. Write serializer alias addresses for remote access
8. Verify LOCK status on both ports (poll LOCK register or GPIO)
9. Configure frame sync mode (if used)
10. Enable CSI-2 output (TX_EN)
```

### 2.3 Key Registers

| Register | Address | Purpose |
|----------|---------|---------|
| DEVICE_ID | 0x00 | Device identification and revision |
| RESET_CTL | 0x01 | Soft reset control |
| CSI_CTL | 0x33 | CSI-2 output configuration |
| FWD_CTL1 | 0x20 | Port 0 forwarding control |
| FWD_CTL2 | 0x21 | Port 1 forwarding control |
| RX_PORT_STS | 0x4D | Port lock/detect status |
| VC_MAP | 0x72 | Virtual channel mapping |

### 2.4 Lock Detection

- LOCK pin active-high when both ports have valid video lock
- Firmware must monitor lock status and report loss-of-lock events
- On lock loss: log event, attempt re-initialization (max 3 retries)
- Persistent lock loss: enter degraded mode, report via CAN diagnostic

### 2.5 Error Handling

| Error Condition | Detection | Recovery Action |
|----------------|-----------|-----------------|
| I2C NACK | No ACK on address phase | Retry 3x, then report fault |
| Port lock loss | GPIO interrupt or poll | Re-initialize port, log event |
| CSI-2 CRC error | SOM CSI-2 receiver status | Log error count, no recovery needed (per-frame) |
| PLL unlock | Status register | Full reset and re-init |
| Over-temperature | TEMP_STS register | Reduce frame rate or shutdown |

---

## 3. TCAN1044AV-Q1 CAN-FD Transceiver

### 3.1 Interface Summary

| Parameter | Value |
|-----------|-------|
| Bus (SOM side) | CAN TX/RX (digital logic) |
| Bus (vehicle side) | CAN_H / CAN_L differential |
| Mode Control | STB pin (GPIO) |
| Data Rate | CAN-FD up to 5 Mbps data phase |
| Supply Voltage | VCC = 5V, VIO = 3.3V |

### 3.2 Operating Modes

| Mode | STB Pin | Description | Current Draw |
|------|---------|-------------|--------------|
| Normal | LOW | Full transceiver operation | ~5mA |
| Standby | HIGH | Bus monitoring only, reduced power | ~10uA |
| Listen-Only | LOW + TXD HIGH | Receive only, no transmit | ~5mA |

### 3.3 Mode Control Driver

```c
/* Mode control interface */
typedef enum {
    CAN_MODE_NORMAL,    /* STB=LOW: full operation */
    CAN_MODE_STANDBY,   /* STB=HIGH: low-power monitoring */
    CAN_MODE_LISTEN     /* Software listen-only mode */
} can_phy_mode_t;

/* Set transceiver operating mode */
int can_phy_set_mode(can_phy_mode_t mode);

/* Get current transceiver mode */
can_phy_mode_t can_phy_get_mode(void);
```

### 3.4 Initialization

1. Assert STB HIGH (standby) during system boot
2. Wait for 5V and 3.3V rails stable
3. Configure SOM CAN controller (bit rate, FD mode, filters)
4. De-assert STB (set LOW) to enter Normal mode
5. Verify bus activity (optional: send diagnostic frame)

### 3.5 TXD Recessive Pull-up

The TXD input has an external pull-up resistor to VIO. This ensures the bus remains
recessive during SOM boot when the CAN controller output is tri-stated. No firmware
action required; this is a hardware fail-safe.

---

## 4. NEO-M9N-00B GNSS Receiver

### 4.1 Interface Summary

| Parameter | Value |
|-----------|-------|
| Primary Bus | UART (UBX + NMEA protocol) |
| UART Baud Rate | 115200 default (configurable to 921600) |
| Secondary Bus | I2C (backup, not primary) |
| PPS Output | 1Hz pulse-per-second, rising edge |
| Constellations | GPS, GLONASS, Galileo, BeiDou (concurrent) |

### 4.2 Protocol Handling

The driver supports dual-protocol parsing:

| Protocol | Usage | Format |
|----------|-------|--------|
| UBX (binary) | Configuration, status, precision data | TI-proprietary binary |
| NMEA 0183 | Position/velocity/time sentences | ASCII, checksummed |

### 4.3 Key UBX Messages

| Message Class/ID | Name | Purpose |
|------------------|------|---------|
| UBX-CFG-PRT (0x06, 0x00) | Port Configuration | UART baud rate, protocol |
| UBX-CFG-MSG (0x06, 0x01) | Message Rate | Enable/disable NMEA sentences |
| UBX-CFG-RATE (0x06, 0x08) | Navigation Rate | Fix interval (1Hz default) |
| UBX-NAV-PVT (0x01, 0x07) | Pos/Vel/Time | Primary navigation solution |
| UBX-NAV-STATUS (0x01, 0x03) | Fix Status | Fix type and validity flags |
| UBX-MON-HW (0x0A, 0x09) | HW Status | Antenna and jamming status |

### 4.4 PPS Timing

- PPS output: 100ms active-high pulse at UTC second boundary
- SOM captures PPS rising edge on timer-capture input
- Used for: CAN timestamp sync, log file timestamping, IMU data alignment
- PPS accuracy: +/- 30ns (once full fix acquired)

### 4.5 Driver API

```c
/* GNSS position data structure */
typedef struct {
    double latitude_deg;    /* WGS84 latitude in degrees */
    double longitude_deg;   /* WGS84 longitude in degrees */
    float altitude_m;       /* Height above MSL in meters */
    float speed_mps;        /* Ground speed in m/s */
    float heading_deg;      /* Heading of motion in degrees */
    uint8_t fix_type;       /* 0=none, 2=2D, 3=3D */
    uint8_t num_satellites;
    uint32_t utc_time_ms;   /* UTC time of fix */
    bool valid;
} gnss_position_t;

/* Initialize GNSS receiver with specified baud rate */
int gnss_init(uint32_t baud_rate);

/* Get latest position fix (non-blocking, returns last valid) */
int gnss_get_position(gnss_position_t *pos);

/* Get PPS timestamp (last captured edge, SOM timer ticks) */
uint64_t gnss_get_pps_timestamp(void);

/* Set navigation rate (Hz) */
int gnss_set_rate(uint8_t rate_hz);

/* Check antenna status */
int gnss_get_antenna_status(uint8_t *status);
```

### 4.6 Error Handling

| Error Condition | Detection | Recovery |
|----------------|-----------|----------|
| No UART data | Timeout (>2s no bytes) | Re-init UART, check power |
| Invalid checksum | NMEA/UBX checksum fail | Discard message, increment counter |
| No fix | fix_type == 0 for >60s | Report degraded, continue |
| Antenna fault | UBX-MON-HW status | Log fault, report via CAN |
| Jamming detected | UBX-MON-HW jamming indicator | Log warning, continue operation |

---

## 5. BMI088 6-axis IMU

### 5.1 Interface Summary

| Parameter | Value |
|-----------|-------|
| Bus | SPI (4-wire) |
| Chip Selects | CS_ACC (accelerometer), CS_GYR (gyroscope) |
| SPI Clock | Up to 10 MHz |
| SPI Mode | CPOL=0, CPHA=0 (Mode 0) for accel; CPOL=1, CPHA=1 (Mode 3) for gyro |
| Interrupts | INT1_ACC, INT1_GYR (data-ready) |
| Accelerometer Range | +/- 3g, 6g, 12g, 24g (configurable) |
| Gyroscope Range | +/- 125, 250, 500, 1000, 2000 deg/s |

### 5.2 Dual Chip-Select Architecture

The BMI088 contains two independent sensor dies with separate SPI interfaces:

```
SOM SPI Controller
    |
    +-- SCLK ---------> [ACC SCLK] [GYR SCLK]
    +-- MOSI ---------> [ACC SDI]  [GYR SDI]
    +-- MISO <--------- [ACC SDO]  [GYR SDO]  (active on respective CS)
    +-- CS_ACC -------> [ACC CSB]
    +-- CS_GYR -------> [GYR CSB]
```

### 5.3 Initialization Sequence

1. Power-on wait: 1ms (accelerometer), 30ms (gyroscope)
2. Read ACC chip ID (0x00) - expect 0x1E
3. Read GYR chip ID (0x00) - expect 0x0F
4. Configure accelerometer: range, bandwidth, output data rate
5. Configure gyroscope: range, bandwidth, output data rate
6. Configure interrupts: data-ready on INT1 pins
7. Verify data streaming (read and validate first samples)

### 5.4 Driver API

```c
/* IMU data structure */
typedef struct {
    float acc_x, acc_y, acc_z;  /* Acceleration in m/s^2 */
    float gyr_x, gyr_y, gyr_z; /* Angular rate in rad/s */
    uint32_t timestamp_us;       /* Microsecond timestamp */
    bool valid;
} imu_data_t;

/* Initialize IMU with specified ranges */
int imu_init(uint8_t acc_range_g, uint16_t gyr_range_dps);

/* Read latest IMU sample (blocking until data-ready) */
int imu_read(imu_data_t *data);

/* Read accelerometer only */
int imu_read_accel(float *x, float *y, float *z);

/* Read gyroscope only */
int imu_read_gyro(float *x, float *y, float *z);

/* Perform self-test (returns 0 on pass) */
int imu_self_test(void);

/* Get temperature (internal die temp, degrees C) */
int imu_get_temperature(float *temp_c);
```

### 5.5 Interrupt Handling

- INT1_ACC fires at accelerometer ODR (output data rate)
- INT1_GYR fires at gyroscope ODR
- ISR captures timestamp and sets data-ready flag
- Worker thread reads data on flag set (deferred processing)
- Maximum interrupt latency budget: 100us for timing accuracy

---

## 6. TPS3431-Q1 Window Watchdog

### 6.1 Interface Summary

| Parameter | Value |
|-----------|-------|
| WDI Input | GPIO (SOM heartbeat output) |
| RESET Output | Active-low reset to system |
| ENABLE Input | SOM_BOOT_OK (gates watchdog activation) |
| Window Type | Open-window only (no closed-window in typical config) |
| Timeout | Set by external resistor/capacitor |

### 6.2 Watchdog Timing

```
        |<--- Timeout Period (T_WD) --->|
        |                               |
   WDI  |_______|^|_______|^|__________|  <-- Must pulse before timeout
        |                               |
        |  Open Window                  |
        +-------------------------------+----> RESET asserted if no pulse
```

### 6.3 Driver Interface

```c
/* Kick the watchdog (toggle WDI pin) */
void watchdog_kick(void);

/* Get time remaining before timeout (milliseconds) */
uint32_t watchdog_get_remaining_ms(void);

/* Enable watchdog (assert SOM_BOOT_OK) */
int watchdog_enable(void);

/* Check if watchdog caused last reset */
bool watchdog_was_reset_source(void);
```

### 6.4 Service Requirements

- Watchdog must be serviced (kicked) within the configured timeout period
- First kick must occur within one timeout period after ENABLE assertion
- Firmware creates a high-priority periodic thread for watchdog servicing
- Watchdog service runs independently of application tasks
- If application hangs, watchdog service also stops (shared process space)

### 6.5 Boot Gating Logic

```
Power On --> Regulators stable --> SOM boots --> Application init
                                                      |
                                                      v
                                              SOM_BOOT_OK = HIGH
                                                      |
                                                      v
                                              TPS3431 ENABLED
                                                      |
                                                      v
                                              First WDI kick within T_WD
```

---

## 7. Driver Dependencies and Initialization Order

```
1. Power rails stable (hardware, no firmware action)
2. GPIO driver init (watchdog_kick, CAN_STB, LOCK monitoring)
3. I2C driver init (for DS90UB954 configuration)
4. SPI driver init (for BMI088)
5. UART driver init (for NEO-M9N)
6. CAN controller init (protocol stack)
7. DS90UB954 init (camera configuration)
8. TCAN1044AV mode set (Normal)
9. NEO-M9N init (GNSS configuration)
10. BMI088 init (IMU configuration)
11. Assert SOM_BOOT_OK (enables watchdog)
12. Start watchdog service thread
```

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1.0 | 2024-01-15 | -- | Initial driver specifications |
