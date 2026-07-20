# DMS / OMS / In-Cabin Sensor Options

## Purpose

This package is the **SoC-agnostic Driver Monitoring System (DMS), Occupant Monitoring System (OMS), and in-cabin camera sensor selection and sourcing reference** for ADVIS.

ADVIS is **not locked to TI TDA, AM62A, TDA4, Rockchip, NXP, Qualcomm, Renesas, Ambarella, Horizon Robotics, NVIDIA, MediaTek, or any other single compute platform**. The image sensor shall be selected using measured cabin image quality, NIR performance, module availability, complete usable-camera cost, lifecycle, safety evidence, and integration support.

Supported transport approaches include:

- Native MIPI CSI-2
- FPD-Link III camera + deserializer
- GMSL2/GMSL3 camera + deserializer
- Automotive Ethernet camera
- USB/UVC prototype camera
- DVP/parallel through a native receiver or bridge

## Folder contents

| File / folder | Purpose |
|---|---|
| `01_SoC_Agnostic_Selection_Strategy.md` | Platform-independent DMS/OMS camera architecture and selection policy |
| `02_DMS_OMS_Sensor_Master_Reference.md` | Complete comparison from premium automotive OMS sensors to the cheapest usable DIY cameras |
| `03_Supplier_Sourcing_Reference.md` | Observed public prices, MOQ, seller and sourcing risks |
| `04_Alternative_Manufacturers.md` | Less-utilized and emerging sensor manufacturers |
| `05_Interface_Illumination_And_Compute_Compatibility.md` | MIPI/SerDes/USB compatibility, NIR illumination and universal HAL policy |
| `06_Supplier_RFQ_Checklist.md` | Exact technical and commercial questions before ordering |
| `07_Recommended_Procurement_Shortlist.md` | Recommended purchases by prototype, production and premium OMS objective |
| `data/` | CSV copies of comparison tables |
| `workbook_parts/` | Chunked Base64 copy of the Excel workbook |
| `tools/restore_workbook.py` | Reconstructs the exact Excel workbook |
| `sources/Official_Source_Index.md` | Official manufacturer and observed supplier links |

## Restoring the workbook

```bash
python tools/restore_workbook.py
```

This writes:

```text
ADVIS_DMS_OMS_In_Cabin_Sensor_Sourcing_Reference.xlsx
```

## Current engineering recommendation

1. **Production cost-first DMS:** OX01H1B / OX01N1B, AR0144AT, VB56G4A/G6A, and SC233AT.
2. **Best technical prototype bridge:** OV2312 RGB-IR and OV2311 mono.
3. **Best widely sourced industrial validation camera:** AR0234CS.
4. **Cheapest serious SoC-agnostic DMS PoC:** OV9281 monochrome USB-UVC NoIR camera.
5. **Premium whole-cabin OMS:** OX05C1S, IMX775, SC533AT, VB1940/VD1940 and OX05B1S.
6. **Do not evaluate production DMS quality using OV7670, OV2640 or OV5647.** They are software bring-up devices only.
7. Use a common ADVIS camera HAL so sensor register control, transport and ISP remain replaceable.

## Core sourcing rule

Compare the complete usable-camera cost:

> Sensor + optical filter + lens + module PCB + clocks + regulators + EEPROM + serializer/USB bridge + cable + deserializer/adapter + driver + ISP tuning + calibration + IR illuminator + mechanical housing.

An automotive-qualified sensor does **not** make an unqualified module automotive-grade. A cheap bare sensor or marketplace board is not equivalent to a working OEM camera.

## Data status

- Global sourcing scan date: **20 July 2026**
- Sensor specifications should be revalidated against the latest official data brief or NDA documentation before design freeze.
- Prices are indicative and may exclude GST, freight, customs, duty, tooling, NRE and lens customization.
- Marketplace entries are sourcing evidence, not approved supplier quotations.
