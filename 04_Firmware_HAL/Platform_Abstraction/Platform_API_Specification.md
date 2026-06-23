# ADVIS Platform Abstraction API Specification

**Document ID:** ADVIS-FW-API-001  
**Version:** 0.1.0  
**Status:** Draft  
**Last Updated:** 2024-01-15

---

## 1. Purpose

This document defines the SoC-agnostic Platform Abstraction API for the ADVIS system.
This API enables application-layer software to interact with hardware peripherals without
knowledge of the underlying SoC or BSP implementation, supporting portability across
TDA4VM, AM68A, AM62A, and future SoC variants.

---

## 2. Architecture

```
+-----------------------------------------------------------+
|          Application Layer                                  |
|  (Perception, DMS, Logging, Diagnostics, CAN Services)    |
+-----------------------------------------------------------+
|          Platform Abstraction API  <-- THIS DOCUMENT       |
|  camera_*  can_*  gnss_*  imu_*  ir_*  wdt_*  stor_*     |
+-----------------------------------------------------------+
|          SoC-Specific Implementation                       |
|  (TDA4VM driver | AM68A driver | AM62A driver)            |
+-----------------------------------------------------------+
|          Linux BSP / Device Drivers                        |
+-----------------------------------------------------------+
```

---

## 3. Common Conventions

### 3.1 Error Codes

All API functions return `int` status codes:

| Code | Name | Meaning |
|------|------|---------|
| 0 | PLAT_OK | Success |
| -1 | PLAT_ERR_GENERAL | Unspecified error |
| -2 | PLAT_ERR_TIMEOUT | Operation timed out |
| -3 | PLAT_ERR_BUSY | Resource busy |
| -4 | PLAT_ERR_INVALID | Invalid parameter |
| -5 | PLAT_ERR_NO_DEVICE | Device not present or not responding |
| -6 | PLAT_ERR_NOT_READY | Device not initialized |
| -7 | PLAT_ERR_OVERFLOW | Buffer overflow |
| -8 | PLAT_ERR_PERMISSION | Insufficient privileges |

### 3.2 Thread Safety

| Category | Policy |
|----------|--------|
| Init functions | NOT thread-safe (call once from main thread) |
| Read functions | Thread-safe (concurrent reads allowed) |
| Write/Send functions | Thread-safe (internally serialized) |
| Callback registration | NOT thread-safe (register before init complete) |

### 3.3 Naming Convention

- Module prefix: `camera_`, `can_`, `gnss_`, `imu_`, `ir_`, `watchdog_`, `storage_`
- Init functions: `<module>_init()`
- Teardown: `<module>_deinit()`
- Synchronous read: `<module>_read()` or `<module>_get_<data>()`
- Asynchronous: `<module>_register_callback()`

---

## 4. Camera API

### 4.1 Functions

```c
/**
 * Initialize camera subsystem (DS90UB954 + CSI-2 receiver)
 * @param config  Camera configuration parameters
 * @return PLAT_OK on success, error code on failure
 */
int camera_init(const camera_config_t *config);

/**
 * Get a frame from the specified virtual channel
 * @param channel  Virtual channel (0=Forward, 1=DMS)
 * @param frame    Output frame buffer descriptor
 * @param timeout_ms  Maximum wait time (0=non-blocking)
 * @return PLAT_OK on success, PLAT_ERR_TIMEOUT if no frame
 */
int camera_get_frame(uint8_t channel, frame_buffer_t *frame, uint32_t timeout_ms);

/**
 * Release frame buffer back to pool
 * @param frame  Previously acquired frame
 * @return PLAT_OK on success
 */
int camera_release_frame(frame_buffer_t *frame);

/**
 * Get camera lock status
 * @param channel  Virtual channel (0 or 1)
 * @return 1 if locked, 0 if unlocked, negative on error
 */
int camera_get_lock_status(uint8_t channel);

/**
 * Register frame-available callback (zero-copy notification)
 * @param channel  Virtual channel
 * @param cb       Callback function
 * @param ctx      User context pointer
 */
int camera_register_callback(uint8_t channel, camera_frame_cb_t cb, void *ctx);

/**
 * Deinitialize camera subsystem
 */
int camera_deinit(void);
```

### 4.2 Data Types

```c
typedef struct {
    uint16_t width;
    uint16_t height;
    uint8_t format;         /* YUYV, NV12, RAW10, etc. */
    uint8_t num_channels;   /* 1 or 2 */
} camera_config_t;

typedef struct {
    void *data;
    uint32_t size;
    uint64_t timestamp_ns;
    uint16_t width;
    uint16_t height;
    uint8_t channel;
    uint32_t sequence;
} frame_buffer_t;
```

---

## 5. CAN API

### 5.1 Functions

```c
/**
 * Initialize CAN interface
 * @param bitrate    Nominal bit rate (e.g., 500000 for 500 kbps)
 * @param fd_bitrate FD data phase bit rate (e.g., 2000000 for 2 Mbps)
 * @return PLAT_OK on success
 */
int can_init(uint32_t bitrate, uint32_t fd_bitrate);

/**
 * Send a CAN/CAN-FD frame
 * @param frame  Frame to transmit
 * @param timeout_ms  Transmit timeout
 * @return PLAT_OK on success, PLAT_ERR_TIMEOUT on bus busy
 */
int can_send(const can_frame_t *frame, uint32_t timeout_ms);

/**
 * Receive a CAN/CAN-FD frame (blocking)
 * @param frame  Output frame buffer
 * @param timeout_ms  Maximum wait time
 * @return PLAT_OK on frame received, PLAT_ERR_TIMEOUT if none
 */
int can_receive(can_frame_t *frame, uint32_t timeout_ms);

/**
 * Set message acceptance filter
 * @param id    Filter ID
 * @param mask  Filter mask
 * @return PLAT_OK on success
 */
int can_set_filter(uint32_t id, uint32_t mask);

/**
 * Set transceiver mode (Normal, Standby, Listen)
 * @param mode  Desired operating mode
 */
int can_set_mode(can_mode_t mode);

/**
 * Get bus error counters
 * @param tx_err  Transmit error counter output
 * @param rx_err  Receive error counter output
 */
int can_get_error_counters(uint8_t *tx_err, uint8_t *rx_err);

int can_deinit(void);
```

### 5.2 Data Types

```c
typedef struct {
    uint32_t id;        /* 11-bit or 29-bit identifier */
    uint8_t data[64];   /* Payload (8 bytes CAN, up to 64 CAN-FD) */
    uint8_t dlc;        /* Data length code */
    bool is_extended;   /* True for 29-bit ID */
    bool is_fd;         /* True for CAN-FD frame */
    bool brs;           /* Bit rate switch (FD only) */
    uint64_t timestamp; /* Receive timestamp (ns) */
} can_frame_t;

typedef enum {
    CAN_MODE_NORMAL,
    CAN_MODE_STANDBY,
    CAN_MODE_LISTEN
} can_mode_t;
```

---

## 6. GNSS API

### 6.1 Functions

```c
/**
 * Initialize GNSS receiver
 * @param uart_baud  UART baud rate for communication
 * @return PLAT_OK on success
 */
int gnss_init(uint32_t uart_baud);

/**
 * Get latest position fix
 * @param pos  Output position structure
 * @return PLAT_OK if valid fix available, PLAT_ERR_NOT_READY if no fix
 */
int gnss_get_position(gnss_position_t *pos);

/**
 * Get last PPS edge timestamp (system clock domain)
 * @return Timestamp in nanoseconds, 0 if no PPS received
 */
uint64_t gnss_get_pps_timestamp(void);

/**
 * Get satellite visibility information
 * @param info  Output satellite info structure
 */
int gnss_get_satellite_info(gnss_sat_info_t *info);

/**
 * Get GNSS receiver health status
 * @param status  Output health status
 */
int gnss_get_health(gnss_health_t *status);

int gnss_deinit(void);
```

---

## 7. IMU API

### 7.1 Functions

```c
/**
 * Initialize IMU (BMI088)
 * @param acc_range  Accelerometer range in g (3, 6, 12, or 24)
 * @param gyr_range  Gyroscope range in deg/s (125, 250, 500, 1000, 2000)
 * @return PLAT_OK on success
 */
int imu_init(uint8_t acc_range, uint16_t gyr_range);

/**
 * Read latest IMU sample (accelerometer + gyroscope)
 * @param data  Output IMU data structure
 * @return PLAT_OK on success
 */
int imu_read(imu_data_t *data);

/**
 * Perform IMU self-test
 * @return PLAT_OK if self-test passes, error code if failed
 */
int imu_self_test(void);

/**
 * Get IMU die temperature
 * @param temp_c  Output temperature in degrees Celsius
 */
int imu_get_temperature(float *temp_c);

/**
 * Register data-ready callback
 * @param cb   Callback function (called from ISR context)
 * @param ctx  User context
 */
int imu_register_data_ready_cb(imu_data_ready_cb_t cb, void *ctx);

int imu_deinit(void);
```

---

## 8. IR Illumination API

### 8.1 Functions

```c
/**
 * Initialize IR daughterboard interface
 * @return PLAT_OK on success, PLAT_ERR_NO_DEVICE if not populated
 */
int ir_init(void);

/**
 * Set IR illumination mode
 * @param enable  True to enable IR LEDs
 * @param pwm_duty  PWM duty cycle 0-100 (percent)
 * @return PLAT_OK on success
 */
int ir_set_mode(bool enable, uint8_t pwm_duty);

/**
 * Get IR fault status
 * @return 1 if fault active, 0 if normal, negative on error
 */
int ir_get_fault_status(void);

int ir_deinit(void);
```

### 8.2 Safety Notes

- IR LEDs default to OFF (enable pin pulled low in hardware)
- Maximum continuous duty cycle limited to prevent thermal damage
- Fault pin (IR_FAULT_N) monitored; auto-disable on fault assertion
- IR enable requires explicit application request after boot

---

## 9. Watchdog API

### 9.1 Functions

```c
/**
 * Enable watchdog (asserts SOM_BOOT_OK, starts TPS3431)
 * @return PLAT_OK on success
 */
int watchdog_enable(void);

/**
 * Kick watchdog (must be called within timeout period)
 */
void watchdog_kick(void);

/**
 * Get time remaining before watchdog expires
 * @return Milliseconds remaining, 0 if not enabled
 */
uint32_t watchdog_get_remaining_ms(void);

/**
 * Check if last system reset was caused by watchdog
 * @return True if watchdog reset occurred
 */
bool watchdog_was_reset_source(void);

/**
 * Start automatic watchdog service thread
 * @param interval_ms  Kick interval in milliseconds
 * @return PLAT_OK on success
 */
int watchdog_start_service(uint32_t interval_ms);
```

---

## 10. Storage API

### 10.1 Functions

```c
/**
 * Initialize storage interface (USB mass storage or eMMC)
 * @param path  Mount point path
 * @return PLAT_OK on success
 */
int storage_init(const char *path);

/**
 * Write data to storage (append to log file)
 * @param filename  Target file name
 * @param data      Data buffer
 * @param len       Data length in bytes
 * @return Bytes written, or negative error code
 */
int storage_write(const char *filename, const void *data, uint32_t len);

/**
 * Flush pending writes to storage medium
 * @return PLAT_OK on success
 */
int storage_flush(void);

/**
 * Get available storage space
 * @return Available bytes, or negative error code
 */
int64_t storage_get_free_bytes(void);

int storage_deinit(void);
```

---

## 11. Platform Lifecycle

### 11.1 Initialization Order

```
1. platform_early_init()   -- GPIO, clocks, basic I/O
2. camera_init()           -- Deserializer + CSI-2
3. can_init()              -- CAN controller + PHY
4. gnss_init()             -- GNSS receiver
5. imu_init()              -- IMU sensor
6. ir_init()               -- IR interface (if populated)
7. storage_init()          -- Storage media
8. watchdog_enable()       -- Must be LAST (starts timeout)
9. watchdog_start_service() -- Auto-kick thread
```

### 11.2 Shutdown Order

```
1. watchdog_kick()         -- Final kick before shutdown
2. ir_deinit()             -- Disable IR LEDs
3. camera_deinit()         -- Stop video streaming
4. can_deinit()            -- Set CAN to standby
5. gnss_deinit()           -- Power down GNSS
6. imu_deinit()            -- Power down IMU
7. storage_flush()         -- Flush all pending writes
8. storage_deinit()        -- Unmount storage
```

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1.0 | 2024-01-15 | -- | Initial platform API specification |
