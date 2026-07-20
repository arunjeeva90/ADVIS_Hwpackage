# SoC-Agnostic Forward-Vision Sensor Selection Strategy

## Locked engineering position

ADVIS shall not be architecturally tied to one SoC vendor.

The camera design shall be split into four replaceable layers:

```text
Image sensor + lens
        ↓
Camera module and transport
        ↓
SoC camera receiver + ISP
        ↓
ADVIS normalized image / metadata HAL
        ↓
Perception pipeline
```

The perception application must consume a normalized contract rather than sensor-specific register settings.

## Recommended HAL boundaries

### Sensor driver layer

Responsible for:

- Power-up and reset sequence
- Sensor register configuration
- Exposure and analog/digital gain
- HDR exposure ratios
- LED-flicker mitigation mode
- Frame synchronization
- Temperature and sensor diagnostics
- OTP and calibration-memory access

### Transport layer

Interchangeable implementations:

- Native MIPI CSI-2
- DS90UB953/954/960-class FPD-Link
- MAX9295/9296 or equivalent GMSL
- Automotive Ethernet video
- USB/UVC for prototype-only paths
- FPGA/bridge for DVP or LVDS sensors

### ISP adaptation layer

Responsible for:

- RAW Bayer or RCCB/RCCC decoding
- PWL/decompanding
- Black-level and defective-pixel correction
- Lens-shading correction
- Demosaic
- HDR merge or tone mapping
- Color correction
- Noise reduction
- Fixed output geometry and pixel format

### Normalized ADVIS camera contract

Suggested outputs:

- Timestamped frame
- Frame counter and data-age status
- Sensor temperature
- Exposure and gain metadata
- HDR/LFM mode
- Image-quality confidence
- Camera calibration version
- Transport and CSI error status
- Blockage/blur/glare indicators

## Sensor-selection gates

1. Image performance under Indian sun/shadow, tunnel, rain, glare and night LEDs.
2. Detection range after applying the selected lens FOV.
3. Complete module availability rather than bare-die availability.
4. Working driver and ISP support for at least one target SoC.
5. Portability effort to the likely production SoC.
6. Sample and production price, including bridges and engineering support.
7. Automotive lifecycle, traceability, qualification and safety documentation.
8. Supply diversity and second-source feasibility.

## Recommended development sequence

### Stage 1 — Software and model bring-up

Use whichever camera is cheapest and best supported by the chosen board:

- IMX219 / OV5647 for minimal daytime demo
- IMX678 / IMX335 for high-resolution model work
- IMX462 / IMX585 for night-data studies

### Stage 2 — Automotive image-quality baseline

Use at least one true automotive HDR/LFM camera:

- IMX390
- OX03C10
- AR0233AT
- AR0341AT

### Stage 3 — Production RFQ competition

Request matched quotations for complete modules from:

- Sony module partners
- OmniVision module partners
- onsemi module partners
- Samsung ISOCELL Auto
- SmartSens
- ST
- Pixelplus
- Qualified Chinese module houses

### Stage 4 — Freeze by measured score

Freeze only after side-by-side tests using the same:

- Lens FOV and aperture
- Camera position
- Exposure target
- Object/lane/sign models
- Day/night routes
- Temperature points
- Preprocessing and ISP maturity level

## Practical ADVIS recommendation

- **Automotive benchmark:** IMX390
- **2–3 MP production candidates:** OX03C10, AR0233AT, AR0341AT, SmartSens SC360AT/SC220AT
- **5 MP premium benchmark:** IMX490
- **8 MP premium candidates:** AR0823AT, OX08D20/OX08D10, Samsung Auto 1H1, SmartSens SC860AT/SC850AT
- **Affordable algorithm camera:** IMX678
- **Affordable low-light camera:** IMX462
- **Cheapest meaningful MIPI camera:** IMX219
- **Absolute-cheapest daylight demo:** OV5647
