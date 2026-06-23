# ADVIS Platform Modularity Concept

## Version
v1.0 - June 2026

---

## Core Principle

The ADVIS platform separates **compute** from **vehicle interface** through a standardized carrier-to-SoM boundary. The carrier board owns all vehicle-facing interfaces and protection. The SoM owns all compute and high-level processing. This separation is the foundation of platform IP.

---

## Architecture Layers

```
+-----------------------------------------------+
|              Vehicle Harness                    |
|   (12V, CAN, Cameras, GNSS Antenna)          |
+-----------------------------------------------+
          |
+-----------------------------------------------+
|           ADVIS CARRIER BOARD                 |
|                                                |
|  [Power Protection] [Camera Deser] [CAN PHY] |
|  [GNSS Rx] [IMU] [USB] [Storage] [IR I/F]   |
|                                                |
|  +---------+  Standardized                    |
|  | SoM     |  Interface                       |
|  | Module  |<-------------->                  |
|  |         |  (Power + Signals)               |
|  +---------+                                  |
|                                                |
+-----------------------------------------------+
```

---

## What the Carrier Owns (Fixed)

- 12V input protection (fuse, TVS, PMOS, filtering)
- Power generation (5V, 3.3V, 1.8V rails)
- Power sequencing and supervision
- Watchdog
- DS90UB954 deserializer (camera aggregation)
- TCAN1044AV CAN-FD PHY
- NEO-M9N GNSS receiver
- BMI088 IMU
- USB-C connector and ESD protection
- microSD interface
- IR daughterboard connector
- All vehicle-facing connectors
- All ESD/EMC protection
- Ground domain management

## What the SoM Owns (Swappable)

- Application processor / DSP / AI accelerator
- DDR memory
- eMMC/flash storage
- CSI-2 MIPI receive interface
- I2C/SPI/UART controllers
- USB controller
- CAN controller (protocol layer)
- Boot ROM and boot media
- Operating system

---

## SoM Swap Scenarios

| Scenario | Action Required |
|----------|-----------------|
| Same SoC family, different speed grade | SoM swap only, no carrier change |
| Different SoC family, same connector | SoM swap + firmware profile change |
| Different SoC family, different connector | New SoM adapter board OR new carrier variant |

---

## Interface Standard Requirements

Any compatible SoM must provide:

- 4-lane CSI-2 receive (MIPI D-PHY 1.5+ Gbps/lane)
- I2C master for camera configuration
- SPI master for IMU (2x CS, 2x INT GPIO)
- UART for GNSS
- UART for debug console
- CAN-FD controller output (TX/RX)
- USB 2.0 device controller
- SD/MMC interface
- GPIO for: SOM_BOOT_OK, IR_LED_EN, IR_PWM, CAN_STB
- Reset input (active-low, open-drain compatible)
- Power acceptance: 5V, 3.3V, 1.8V rails from carrier

---

## Why This Is Defensible IP

1. **Network effect**: More SoM vendors supporting the interface = more valuable platform
2. **Switching cost**: OEMs invested in ADVIS firmware + validation don't want to change carrier
3. **Integration cost**: Vehicle-side harness and qualification is tied to carrier, not SoM
4. **Time-to-market**: SoM swap is weeks, full board redesign is months
