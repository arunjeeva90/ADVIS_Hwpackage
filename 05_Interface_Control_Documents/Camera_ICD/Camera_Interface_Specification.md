# ADVIS Camera Interface Specification

## Version
v1.0 - June 2026

## Document ID
ICD-CAM-001

---

## 1. Purpose

This Interface Control Document defines the camera interface specification for both the Forward-facing ADAS camera and the Driver Monitoring System (DMS) camera connected to the ADVIS ECU via FPD-Link III.

---

## 2. Camera System Overview

```
+----------+     FPD-Link III      +-----------+     CSI-2      +------+
| Forward  |----(Coax + PoC)------>| DS90UB954 |---(4-lane)---->| SoM  |
| Camera   |     RX0 Port         | -Q1       |    MIPI D-PHY  |      |
| (VC0)    |                      | Dual Deser|                |      |
+----------+                      |           |                |      |
                                  |           |                |      |
+----------+     FPD-Link III     |           |                |      |
| DMS      |----(Coax + PoC)----->|           |                |      |
| Camera   |     RX1 Port        |           |                |      |
| (VC1)    |                      +-----------+                +------+
+----------+                           ^
                                       |
                                  I2C Config
                                  (from SoM)
```

---

## 3. FPD-Link III Interface Specification

### 3.1 Physical Layer

| Parameter | Forward Camera (RX0) | DMS Camera (RX1) |
|-----------|---------------------|-------------------|
| Standard | TI FPD-Link III | TI FPD-Link III |
| Serializer (camera side) | DS90UB953-Q1 (or compatible) | DS90UB953-Q1 (or compatible) |
| Deserializer (ECU side) | DS90UB954-Q1 Port 0 | DS90UB954-Q1 Port 1 |
| Cable type | 50-ohm coaxial, automotive-grade | 50-ohm coaxial, automotive-grade |
| Connector (ECU side) | FAKRA Z-code (or mini-FAKRA) | FAKRA Z-code (or mini-FAKRA) |
| Connector (camera side) | Per camera module vendor | Per camera module vendor |

### 3.2 Cable Requirements

| Parameter | Specification |
|-----------|---------------|
| Impedance | 50 ohm +/- 10% |
| Attenuation at 750 MHz | < 15 dB/m |
| Maximum cable length | 15m (per TI DS90UB954 datasheet) |
| Typical installation length | 0.5m to 3m |
| Shield effectiveness | > 60 dB (100 MHz to 1 GHz) |
| Temperature rating | -40C to +105C |
| Bend radius (minimum) | 5x cable outer diameter |
| Jacket material | Automotive-grade (flame retardant, UV resistant) |

### 3.3 Power over Coax (PoC)

| Parameter | Specification |
|-----------|---------------|
| PoC voltage | Carrier-supplied through DS90UB954 back-power |
| PoC current per port | Per camera module requirement (typical 300mA) |
| PoC filtering | On-board inductor + capacitor network |
| Back-channel | Bidirectional control channel embedded in coax |
| PoC enable | Controlled by DS90UB954 register configuration |

---

## 4. Virtual Channel Assignment

| Virtual Channel | Camera | Data Type | Priority |
|-----------------|--------|-----------|----------|
| VC0 | Forward ADAS camera | RAW/YUV video | High |
| VC1 | DMS cabin camera | RAW/YUV video | High |
| VC2 | Reserved (future) | N/A | N/A |
| VC3 | Reserved (future) | N/A | N/A |

The DS90UB954 multiplexes both camera streams onto a single 4-lane CSI-2 output using virtual channel tagging. The SoM CSI-2 receiver demultiplexes based on VC ID.

---

## 5. Data Rate Budget

| Parameter | Forward Camera | DMS Camera | Combined |
|-----------|---------------|------------|----------|
| Resolution | Up to 2MP (1920x1080) | Up to 1MP (1280x720) | N/A |
| Frame rate | 30 fps | 30 fps | N/A |
| Pixel format | RAW12 or YUV422 | RAW12 (IR-enhanced) | N/A |
| Bits per pixel | 12 (RAW12) | 12 (RAW12) | N/A |
| Bandwidth per camera | ~750 Mbps | ~330 Mbps | ~1080 Mbps |
| CSI-2 4-lane capacity | N/A | N/A | 6000 Mbps |
| Utilization | N/A | N/A | ~18% (comfortable) |

---

## 6. Camera Module Requirements

### 6.1 Forward ADAS Camera

| Parameter | Requirement |
|-----------|-------------|
| Sensor type | Global shutter preferred, rolling shutter acceptable |
| Resolution | Minimum 1MP, target 2MP |
| Field of view | Horizontal 50-70 degrees (standard ADAS) |
| Dynamic range | > 100 dB HDR |
| Operating temperature | -40C to +85C |
| Serializer | DS90UB953-Q1 compatible |
| Optical filter | IR-cut filter (visible band only) |
| Lens mount | Integrated (fixed focus to infinity) |

### 6.2 DMS Cabin Camera

| Parameter | Requirement |
|-----------|-------------|
| Sensor type | Global shutter preferred |
| Resolution | Minimum 0.3MP, target 1MP |
| Field of view | Horizontal 80-120 degrees (wide for cabin coverage) |
| IR sensitivity | Responsive at 850nm and/or 940nm |
| Operating temperature | -40C to +85C |
| Serializer | DS90UB953-Q1 compatible |
| Optical filter | Visible + NIR pass (no IR-cut filter) |
| Lens mount | Integrated (fixed focus, 0.5m to 1.5m optimized) |

---

## 7. Shielding and EMC Requirements

| Parameter | Specification |
|-----------|---------------|
| Cable shield | Single braid (minimum 85% coverage) or foil + braid |
| Shield termination (ECU) | 360-degree termination at FAKRA connector shell |
| Shield ground reference | CHASSIS_GND (via connector shell to enclosure) |
| Common-mode rejection | > 30 dB at frequencies up to 1 GHz |
| Radiated emission target | Per CISPR 25 Class 5 |

---

## 8. I2C Camera Configuration

| Parameter | Specification |
|-----------|---------------|
| I2C bus | Shared bus from SoM through DS90UB954 back-channel |
| DS90UB954 address | 0x3D (7-bit, default) |
| Serializer access | Via DS90UB954 alias registers |
| Camera sensor access | Via DS90UB954 -> serializer -> sensor I2C bridge |
| Bus speed | 400 kHz (carrier-side), 100/400 kHz (camera-side via back-channel) |
| Pull-ups | 2.2k ohm to 3V3_IO (on carrier) |

---

## 9. Connector Mating and Unmating

| Parameter | Specification |
|-----------|---------------|
| Hot-plug support | NOT supported (power must be off during connect/disconnect) |
| Mating force | Per FAKRA connector specification |
| Keying | Color-coded FAKRA connectors to prevent mis-mating |
| Retention force | > 50N axial pull |
| Mating cycles | Minimum 25 cycles (service life) |
| Connector orientation | Defined by mechanical envelope (top face for FWD, front for DMS) |

---

## 10. Failure Modes and Detection

| Failure Mode | Detection Method | System Response |
|--------------|-----------------|-----------------|
| Cable disconnected | DS90UB954 lock-loss interrupt | Log event, disable VC processing |
| Camera sensor fault | I2C communication timeout | Log event, retry initialization |
| PoC overcurrent | DS90UB954 OC flag | Disable PoC, log event |
| Link quality degradation | CRC error counter in DS90UB954 | Log warning, monitor trend |
| Camera thermal fault | Camera-reported via I2C status | Reduce frame rate or disable |

---

## 11. Revision History

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| 1.0 | 2026-06 | Interface Team | Initial release |
