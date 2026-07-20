# Forward Vision Sensor Options

## Purpose

This package is the **SoC-agnostic forward-camera sensor selection and sourcing reference** for ADVIS.

ADVIS is **not locked to TI TDA, AM62A, TDA4VM, TDA4VL, or any other single compute platform**. The forward image sensor shall be selected using image quality, module availability, recurring cost, development support, lifecycle and safety evidence. The chosen sensor is then adapted to the selected compute platform through one of these transport paths:

- Native MIPI CSI-2
- FPD-Link III camera + deserializer
- GMSL2/GMSL3 camera + deserializer
- Automotive Ethernet camera
- USB/UVC prototype camera
- DVP/LVDS with an appropriate bridge

## Folder contents

| File / folder | Purpose |
|---|---|
| `01_SoC_Agnostic_Selection_Strategy.md` | Platform-independent sensor-selection policy and recommended ADVIS strategy |
| `02_Forward_Vision_Sensor_Master_Reference.md` | Complete master sensor comparison from flagship automotive parts to the cheapest usable DIY options |
| `03_Supplier_Sourcing_Reference.md` | Observed supplier, module, price, MOQ and sourcing-risk evidence |
| `04_Alternative_Manufacturers.md` | Samsung, SmartSens, ST, Pixelplus, Brigates and PixArt alternatives |
| `05_Interface_And_Compute_Compatibility.md` | Universal MIPI/SerDes/Ethernet/USB integration policy |
| `06_Supplier_RFQ_Checklist.md` | Mandatory questions before purchasing a sample or production camera |
| `data/` | CSV copies of every comparison table |
| `ADVIS_Forward_Vision_Sensor_Sourcing_Reference.xlsx.base64` | Exact workbook encoded as text for GitHub transport |
| `tools/restore_workbook.py` | Reconstructs the `.xlsx` workbook from the Base64 file |
| `sources/Official_Source_Index.md` | Official manufacturer and supplier URLs |

## Current recommendation

1. **Do not freeze a sensor based only on the SoC selected first.**
2. Use the **cheapest fully supported module** for the first compute-board PoC.
3. Keep **IMX390 as a mature automotive benchmark**, especially where a ready module and driver already exist.
4. Benchmark **OX03C10, AR0233AT and AR0341AT** as production-oriented 2–3 MP candidates.
5. Include **Samsung Auto 1H1, SmartSens SC860AT/SC850AT/SC360AT, ST and Pixelplus** in the RFQ list where vendor access is available.
6. Use **IMX678** for affordable high-resolution algorithm and dataset work.
7. Use **IMX219 or OV5647 only for basic daylight software demonstrations**.
8. Hide sensor-specific details behind a common ADVIS camera HAL so the perception stack is portable.

## Important sourcing rule

Compare the complete usable camera cost:

> Sensor + lens + module PCB + clock + regulators + EEPROM + serializer/bridge + cable + deserializer/adapter + driver + ISP tuning + calibration + enclosure.

A low bare-sensor price does not imply a low usable-camera cost.

## Data status

- Global sourcing scan date: **20 July 2026**
- Prices are indicative and may exclude GST, freight, customs, duties, tooling and NRE.
- Marketplace listings are evidence points, not approved suppliers or quotations.
- Automotive-grade sensor does not automatically make the full camera module automotive-grade.
