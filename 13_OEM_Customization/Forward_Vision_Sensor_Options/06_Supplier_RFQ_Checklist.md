# Supplier RFQ and Sample-Acceptance Checklist

Use this checklist before ordering any camera or sensor.


| Check | What to require from supplier |
| --- | --- |
| Exact sensor | Require complete orderable part and die revision; reject “sensor optional” quotations. |
| Item type | Confirm bare IC, sensor board, lens module, serializer camera, USB camera or full enclosure. |
| Interface | MIPI CSI-2, FPD-Link III, GMSL2 and USB are not interchangeable. Confirm lanes, rate, RAW bits and connector. |
| Deserializer | For SerDes cameras, confirm serializer IC and matching deserializer/fusion board. |
| RAW access | Ask for uncompressed RAW Bayer. H.264/ISP-only modules may hide exposure/tone mapping. |
| HDR mode | Request exposure count, PWL curve, decompanding, motion artifacts and simultaneous LFM. |
| Exposure control | Confirm manual/auto exposure, gain, anti-flicker, sync, trigger and strobe. |
| Lens | Require HFOV/VFOV, focal length, f-number, distortion, MTF, focus, IR-cut and thermal shift. |
| Calibration | Require intrinsics, distortion coefficients, alignment tolerance and EEPROM format. |
| Temperature | Sensor AEC-Q100 does not make the module automotive-grade. Ask module validation. |
| Functional safety | Ask for safety manual, diagnostics, CRC/frame counter/error pin and FMEDA availability. |
| Lifecycle | Ask lifecycle, LTB policy, annual capacity, origin and traceable lot/date codes. |
| ISP support | Ask for target-SoC tuning/DCC files and custom lens tuning support. |
| Target board | Demand working driver/device tree/config for AXON, Jetson, Pi or TI TDA4. |
| Sample validation | Buy 2–5 identical samples and check identity, focus, hot pixels, hot operation and EMI. |
| True total cost | Compare lens + camera + serializer + cable + deserializer + adapter + enclosure + support. |

## Minimum sample package required

Ask the supplier to include:

- Exact sensor orderable part and revision
- Schematic or camera ICD
- Pinout and connector drawing
- Register initialization table
- Power sequence
- RAW output description
- Lens datasheet and distortion data
- Serializer configuration, where applicable
- Calibration EEPROM format
- Driver/device-tree package
- Sample images and RAW frames
- Temperature and qualification reports
- Lifecycle and MOQ quotation
