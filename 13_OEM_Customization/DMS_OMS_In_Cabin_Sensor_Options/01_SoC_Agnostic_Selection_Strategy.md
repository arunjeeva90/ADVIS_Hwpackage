# SoC-Agnostic DMS / OMS Sensor Selection Strategy

## Architecture position

ADVIS shall not be coupled to one sensor, module vendor, SerDes family or SoC.

```text
Image sensor + optical filter + lens + NIR illumination
        ↓
Camera module and transport
        ↓
SoC camera receiver + ISP / UVC decoder
        ↓
ADVIS normalized in-cabin camera HAL
        ↓
Face / eye / head / body / device perception
        ↓
Temporal driver and occupant state
```

## Replaceable layers

### 1. Sensor and optics

Controls sensor choice, mono versus RGB-IR, global/rolling shutter, 850/940 nm response, lens FOV, focus range, band-pass filter and optical distortion.

### 2. Camera transport

Interchangeable paths:

- Native MIPI CSI-2
- FPD-Link III through DS90UB953/954/960-class devices
- GMSL2/GMSL3 through MAX9295/9296-class devices
- USB-UVC for prototype and algorithm work
- Automotive Ethernet camera
- DVP/parallel through a native receiver or bridge

### 3. Sensor driver and ISP adaptation

Must hide:

- Power-up/reset and register sequences
- Exposure, analog gain, digital gain and black level
- Global-shutter timing and external trigger
- IR LED/VCSEL strobe synchronization
- RGB-IR separation or demosaic
- Defective-pixel, dark-frame and lens-shading correction
- Day/night contexts
- Frame counter, CRC and sensor health

### 4. Normalized ADVIS in-cabin contract

Suggested output metadata:

- Timestamp and frame counter
- Sensor exposure/gain/context
- IR wavelength and illumination state
- Sensor and illuminator temperature
- Face/eye usable-pixel density
- Blur, blockage, saturation, glare and occlusion indicators
- Camera calibration and lens profile version
- Transport/CSI/UVC error state
- DMS capability state

## Selection gates

1. Driver face and both eyes remain sufficiently resolved across the complete head box.
2. Eye-state and gaze performance is measured with glasses, sunglasses, reflections and head rotation.
3. 940 nm performance is measured at safe illumination power; 850 nm may be used for early PoC.
4. Global shutter is preferred for reliable eye/head motion, but a rolling-shutter camera may be accepted for early software bring-up.
5. Lens HFOV must match scope: focused DMS typically 50–75°; driver + front cabin 75–100°; whole-cabin OMS 100°+.
6. The complete working module, driver and ISP package must be available for at least one target compute board.
7. A second transport path or module partner should be feasible before production freeze.
8. Automotive qualification, traceability, safety manual, lifecycle and PPAP evidence must be evaluated independently for sensor and module.

## Development sequence

### Stage 1 — Universal software bring-up

Use USB-UVC OV9281 or AR0234CS when the target SoC is undecided. This avoids blocking the DMS model on MIPI driver work.

### Stage 2 — NIR and eye/gaze validation

Compare OV9281, OV2311, OV2312 and AR0234 under identical lens, distance, 850/940 nm illumination and exposure conditions.

### Stage 3 — Automotive production RFQ

Request matched complete-camera quotations for:

- OX01H1B and OX01N1B
- AR0144AT
- VB56G4A / VB56G6A
- SC233AT
- OV2311 / OV2312
- Optional premium OX05C1S / IMX775 / SC533AT / VB1940

### Stage 4 — Freeze by measured score

Use the same cabin fixture, lens class, NIR optical power, face/eye models, demographics, glasses conditions, temperature and motion profile. Do not compare supplier sample images or differently tuned ISPs.

## Practical platform policy

- The cheapest supported camera is acceptable for model bring-up.
- Production selection is based on measured image quality, safety evidence and complete BOM—not sensor brand.
- A MIPI module that works on one board is not automatically compatible with another board.
- FPD-Link/GMSL makes the camera transport largely SoC-agnostic at the ECU boundary, but sensor register support and ISP tuning remain platform work.
- USB-UVC is the most universal PoC path, but usually not the production transport.
