# 09 - Compliance & Safety

## Purpose

Automotive compliance documentation, safety analysis, and certification tracking.

## Sub-folders

| Folder | Contents |
|--------|----------|
| Automotive_Standards/ | ISO 26262, AEC-Q qualification evidence |
| IEC_62471_Eye_Safety/ | IR illumination eye safety analysis and classification |
| EMC_Certifications/ | CISPR 25, ISO 11452 test reports and certificates |
| Environmental_RoHS_REACH/ | Material compliance declarations |
| FMEA/ | Failure Mode and Effects Analysis documents |

## Applicable Standards

| Standard | Scope | Applicability |
|----------|-------|---------------|
| ISO 26262 | Functional safety | ASIL classification TBD (non-actuation = QM likely) |
| AEC-Q100 | IC qualification | All ICs must be AEC-Q100 qualified |
| AEC-Q200 | Passive qualification | Critical passives must be AEC-Q200 |
| CISPR 25 | Vehicle EMC | Conducted/radiated emissions limits |
| ISO 11452 | Vehicle EMC immunity | Bulk current injection, radiated immunity |
| IEC 62471 | Photobiological safety | IR LED eye safety classification |
| EU RoHS | Hazardous substances | Full compliance required |
| EU REACH | Chemical registration | SVHC reporting required |

## Safety Boundary (Critical)

ADVIS does not directly actuate brake, steering, throttle or powertrain.

ADVIS Assist provides warning/advisory outputs.

ADVIS Control may generate perception-validated, safety-supervised actuation request messages over CAN/CAN-FD, depending on OEM integration.

Final actuator authority, arbitration and vehicle-level safety release remain with the OEM brake, EPS and powertrain ECUs.

ADVIS does not claim:
- Direct brake actuation
- Direct steering actuation
- Direct throttle actuation
- ASIL-C or ASIL-D system-level compliance

This limits functional safety classification to QM (Quality Management) for most failure modes.
