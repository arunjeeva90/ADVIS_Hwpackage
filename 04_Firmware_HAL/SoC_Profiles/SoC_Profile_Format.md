# ADVIS SoC Profile Configuration Format

**Document ID:** ADVIS-FW-SOC-001  
**Version:** 0.1.0  
**Status:** Draft  
**Last Updated:** 2024-01-15

---

## 1. Purpose

This document defines the SoC profile configuration format used by the ADVIS platform
abstraction layer. Each supported SoC has a profile that describes its hardware
capabilities, peripheral assignments, clock configuration, and power characteristics.
The HAL uses these profiles to configure itself at runtime without SoC-specific
code paths in the application layer.

---

## 2. Profile Architecture

```
+-------------------------------------------------------+
|  Application Layer                                     |
|  (Does not know which SoC is running)                 |
+-------------------------------------------------------+
|  Platform Abstraction API                              |
|  (Reads profile, configures accordingly)              |
+-------------------------------------------------------+
|  SoC Profile (YAML/JSON config file)                  |
|  +-- pin_mux definitions                              |
|  +-- clock tree assignments                           |
|  +-- peripheral instance mapping                      |
|  +-- power domain configuration                       |
|  +-- capability flags                                 |
+-------------------------------------------------------+
|  Linux BSP (Device Tree + Kernel Drivers)             |
+-------------------------------------------------------+
```

---

## 3. Profile File Structure

### 3.1 Format

Profiles are stored as YAML files in `/etc/advis/soc_profiles/`:

```
/etc/advis/soc_profiles/
    am68a.yaml        (primary target)
    tda4vm.yaml       (secondary target)
    am62a.yaml        (entry tier)
    default.yaml      (fallback/test)
```

### 3.2 Top-Level Schema

```yaml
# SoC Profile Schema
profile:
  name: "string"           # Human-readable SoC name
  vendor: "string"         # Silicon vendor
  family: "string"         # SoC family (e.g., "Jacinto", "Sitara")
  revision: "string"       # Silicon revision
  compatible: "string"     # Device tree compatible string

capabilities:
  ai_accelerator: bool     # Hardware AI/ML accelerator present
  ai_tops: float           # AI performance in TOPS
  csi2_ports: int          # Number of CSI-2 receiver ports
  csi2_max_lanes: int      # Max lanes per CSI-2 port
  can_fd: bool             # CAN-FD support
  usb_ports: int           # Number of USB ports
  spi_buses: int           # Number of SPI controllers
  i2c_buses: int           # Number of I2C controllers
  uart_ports: int          # Number of UART controllers
  gpu_present: bool        # GPU available
  dsp_cores: int           # Number of DSP cores
  arm_cores: int           # Number of ARM cores
  arm_type: "string"       # ARM core type (A72, A53, etc.)
  max_ddr_gb: float        # Maximum DDR capacity

power:
  core_voltage: float      # Core voltage (V)
  io_voltage: float        # I/O voltage (V)
  typical_power_w: float   # Typical power consumption
  max_power_w: float       # Maximum power consumption
  thermal_limit_c: int     # Junction temperature limit
  power_domains:           # List of power domain names
    - "string"

peripherals:
  camera:
    i2c_bus: "string"      # I2C bus instance for DS90UB954
    i2c_address: int       # I2C address (hex)
    csi2_instance: int     # CSI-2 receiver instance number
    lock_gpio: "string"    # GPIO name for LOCK signal

  can:
    controller: "string"   # CAN controller instance
    stb_gpio: "string"     # GPIO name for STB pin

  gnss:
    uart: "string"         # UART instance for NEO-M9N
    pps_gpio: "string"     # GPIO name for PPS input

  imu:
    spi_bus: "string"      # SPI bus instance
    cs_accel: int          # Chip-select index for accelerometer
    cs_gyro: int           # Chip-select index for gyroscope
    int_accel_gpio: "str"  # GPIO name for accel interrupt
    int_gyro_gpio: "str"   # GPIO name for gyro interrupt

  watchdog:
    wdi_gpio: "string"     # GPIO name for WDI output
    boot_ok_gpio: "string" # GPIO name for SOM_BOOT_OK
    enable_gpio: "string"  # GPIO name for WDT enable (if separate)

  ir:
    enable_gpio: "string"  # GPIO name for IR_LED_EN
    pwm_channel: "string"  # PWM instance for IR_PWM
    fault_gpio: "string"   # GPIO name for IR_FAULT_N

  usb:
    controller: "string"   # USB controller instance
    vbus_gpio: "string"    # GPIO for VBUS detection

clock_config:
  system_clock_mhz: int   # Main system clock
  csi2_clock_mhz: int     # CSI-2 reference clock
  can_clock_mhz: int      # CAN controller clock source
  spi_max_mhz: int        # SPI maximum clock
  i2c_speed_khz: int      # I2C bus speed

pin_mux:
  # Pin mux is SoC-specific and loaded from device tree
  # Profile only references the DT overlay file name
  dt_overlay: "string"    # Device tree overlay file for this SoC
```

---

## 4. Example Profile (AM68A)

```yaml
profile:
  name: "AM68A"
  vendor: "Texas Instruments"
  family: "Jacinto 7"
  revision: "SR2.0"
  compatible: "ti,am68-sk"

capabilities:
  ai_accelerator: true
  ai_tops: 8.0
  csi2_ports: 2
  csi2_max_lanes: 4
  can_fd: true
  usb_ports: 2
  spi_buses: 4
  i2c_buses: 6
  uart_ports: 10
  gpu_present: true
  dsp_cores: 2
  arm_cores: 2
  arm_type: "Cortex-A72"
  max_ddr_gb: 4.0

power:
  core_voltage: 0.85
  io_voltage: 3.3
  typical_power_w: 8.0
  max_power_w: 15.0
  thermal_limit_c: 125
  power_domains:
    - "WKUP"
    - "MCU"
    - "MAIN"

peripherals:
  camera:
    i2c_bus: "i2c2"
    i2c_address: 0x3D
    csi2_instance: 0
    lock_gpio: "gpio0_14"
  can:
    controller: "mcan0"
    stb_gpio: "gpio0_22"
  gnss:
    uart: "uart4"
    pps_gpio: "gpio0_30"
  imu:
    spi_bus: "spi1"
    cs_accel: 0
    cs_gyro: 1
    int_accel_gpio: "gpio1_5"
    int_gyro_gpio: "gpio1_6"
  watchdog:
    wdi_gpio: "gpio0_25"
    boot_ok_gpio: "gpio0_26"
    enable_gpio: "gpio0_26"
  ir:
    enable_gpio: "gpio1_10"
    pwm_channel: "pwm0_ch1"
    fault_gpio: "gpio1_11"
  usb:
    controller: "usb0"
    vbus_gpio: "gpio0_28"

clock_config:
  system_clock_mhz: 2000
  csi2_clock_mhz: 400
  can_clock_mhz: 80
  spi_max_mhz: 48
  i2c_speed_khz: 400

pin_mux:
  dt_overlay: "advis-carrier-v1-am68a.dtbo"
```

**Note:** GPIO names shown above are illustrative. Actual GPIO assignments are
trade secrets and are stored in the production overlay files, not in public documentation.

---

## 5. Profile Selection at Boot

### 5.1 Selection Algorithm

```
1. Read SOM EEPROM board ID
2. Extract SoC type from EEPROM data
3. Map SoC type to profile filename
4. Load profile YAML from /etc/advis/soc_profiles/
5. Validate profile against running hardware (sanity checks)
6. If validation fails: fall back to default.yaml (limited mode)
7. Pass profile to Platform Abstraction API for initialization
```

### 5.2 Validation Rules

Before accepting a profile, the HAL validates:

| Check | Method | Failure Action |
|-------|--------|----------------|
| SoC compatible match | Compare DT root compatible | Reject profile |
| I2C bus exists | Check /dev/i2c-X | Disable camera subsystem |
| SPI bus exists | Check /dev/spidevX.Y | Disable IMU |
| UART exists | Check /dev/ttyX | Disable GNSS |
| GPIO accessible | Check /sys/class/gpio export | Log warning |
| CAN interface exists | Check /sys/class/net/canX | Disable CAN |

---

## 6. Adding a New SoC

To add support for a new SoC variant:

1. Create new profile YAML file (copy closest existing profile as template)
2. Update peripheral instance mappings to match new SoC
3. Create SoC-specific device tree overlay
4. Update pin mux values for all carrier signals
5. Build and test BSP with new device tree combination
6. Validate all peripherals probe and function correctly
7. Run HAL integration test suite against new profile
8. Document any SoC-specific limitations or differences

---

## 7. Profile Versioning

| Field | Purpose |
|-------|---------|
| Profile schema version | Indicates which fields are expected |
| SoC revision | Tracks silicon errata and workarounds |
| Carrier board revision | May affect GPIO routing on different PCB revs |

Profiles are versioned alongside the firmware release. A firmware version is always
tested against a specific set of profile versions.

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1.0 | 2024-01-15 | -- | Initial SoC profile format definition |
