# 04 - Firmware HAL (Hardware Abstraction Layer)

## Purpose

This folder contains the firmware abstraction layer that enables the IND-VIAS platform to support multiple SoC variants with minimal software changes. The HAL is a key IP differentiator.

## Sub-folders

| Folder | Contents |
|--------|----------|
| Drivers/ | Peripheral drivers (DS90UB954, TCAN1044AV, NEO-M9N, BMI088, TPS3431) |
| BSP/ | Board Support Package configurations per SoC variant |
| Device_Trees/ | Linux device tree source files and overlays |
| Boot_Sequence/ | Boot flow documentation, power-on sequencing firmware |
| Watchdog_Service/ | TPS3431 heartbeat service, SOM_BOOT_OK assertion logic |
| Platform_Abstraction/ | SoC-agnostic API layer for all hardware interfaces |
| SoC_Profiles/ | Per-SoC configuration profiles (pin mux, clock, power) |
| Build_System/ | Yocto/Buildroot layer configuration, cross-compilation setup |

## HAL Architecture Concept

```
+---------------------------------------------------+
|              Application Layer                      |
|   (Perception, DMS, Logging, Diagnostics)         |
+---------------------------------------------------+
|           Platform Abstraction API                  |
|   (Camera, CAN, GNSS, IMU, Storage, IR)           |
+---------------------------------------------------+
|              SoC Profile Layer                      |
|   (TDA4VM | AM68A | AM62A | Future SoC)          |
+---------------------------------------------------+
|           Linux BSP / RTOS Layer                   |
+---------------------------------------------------+
|              Hardware                               |
+---------------------------------------------------+
```

## Key Firmware Responsibilities

- Assert SOM_BOOT_OK only after all critical peripherals initialized
- Service TPS3431 watchdog at configured interval
- Initialize DS90UB954 with correct VC mapping (VC0=Forward, VC1=DMS)
- Configure TCAN1044AV mode (Normal/Standby/Listen)
- Parse NEO-M9N UBX/NMEA streams and distribute PPS timing
- Read BMI088 accelerometer and gyroscope via dual-CS SPI
- Control IR daughterboard enable/PWM (default: OFF)
