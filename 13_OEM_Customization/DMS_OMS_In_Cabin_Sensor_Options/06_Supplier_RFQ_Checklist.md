# Supplier RFQ and Sample-Buying Checklist

| Area | Mandatory question / evidence |
| --- | --- |
| Identity | Exact sensor part number and die revision; photo of sensor marking; module model number |
| Qualification | AEC-Q100 grade for sensor and module; operating temperature; PPAP/traceability availability |
| Safety/cyber | Safety manual, FMEDA assumptions, ASIL support level, frame CRC/counter/diagnostics, cybersecurity features |
| Output | RAW8/10/12, YUV or compressed output; full mode table; actual frame rate at full resolution |
| Interface | MIPI lane count/data rate, DVP, USB-UVC, FPD-Link/GMSL serializer, connector and pin map |
| Host support | Validated Linux/V4L2 driver and tested SoCs/boards; ISP tuning files; register script availability |
| NIR | Spectral response at 850/940 nm; IR-cut or band-pass filter; mono/RGB-IR CFA details |
| Illumination sync | Strobe/FSIN/trigger timing, supported LED/VCSEL synchronization, exposure contexts |
| UVC controls | Manual exposure, analog/digital gain, frame rate, gamma, black level and trigger controls |
| Lens | HFOV/VFOV/DFOV, EFL, F-number, distortion, chief-ray angle, focus distance 40 cm–1.2 m, M12 availability |
| Calibration | Intrinsic calibration, distortion coefficients, shading table, OTP/EEPROM and serial number |
| Module mechanics | PCB dimensions, mounting holes, lens holder, cable length, enclosure and thermal design |
| Electrical | Supply rails/current, peak IR-sync current, power sequencing, clock, I/O voltage |
| Image quality | Dark current, SNR, dynamic range, NIR QE, PRNU/DSNU, hot-pixel behavior and temperature effects |
| Commercial | Sample, 5, 100, 1k, 10k and 100k pricing; tooling/NRE; MOQ; lead time; lifecycle notice |
| Legal/source | Authorized channel statement, country of origin, warranty and counterfeit/remarked-part controls |
| Eye safety | Illuminator wavelength, optical power, pulse width/duty cycle and IEC 62471 assessment support |

## Minimum sample acceptance package

A sample is not accepted only because video appears in Linux. The supplier must provide:

1. Exact module model and populated sensor.
2. Pinout / UVC mode table / SerDes ICD.
3. Lens specification and measured FOV.
4. Confirmation of IR-cut or band-pass filter.
5. Frame-rate, resolution and output-format table.
6. Exposure/gain/trigger/strobe control method.
7. Power, temperature and mechanical drawing.
8. Driver/register script and tested host list.
9. Commercial quotation at prototype and production quantities.

## Supplier message summary

> We need a SoC-agnostic DMS/OMS camera module optimized for driver face and eye monitoring. Please quote exact sensor/module options in MIPI CSI-2, USB-UVC and optional FPD-Link III/GMSL2 versions. Global shutter and 940 nm NIR are preferred. Provide exact part number, frame modes, lens FOV, IR filter, strobe synchronization, Linux driver support, mechanical drawing, qualification/safety evidence and prices for 2, 5, 100, 1k and 10k units.
