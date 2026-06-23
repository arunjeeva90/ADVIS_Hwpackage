# 07 - IP Protection

## Purpose

This folder manages the broader intellectual property protection strategy for the ADVIS (Adaptive Driver & Vehicle Intelligence System) platform beyond patents, including trade secrets, copyright, licensing models, and competitive positioning.

## Sub-folders

| Folder | Contents |
|--------|----------|
| Copyright_Registry/ | Software copyright registrations, firmware code ownership |
| Trade_Secret_Controls/ | Access controls, confidentiality procedures, employee exit protocols |
| NDA_Templates/ | Non-disclosure agreements for vendors, partners, customers |
| Licensing_Strategy/ | Platform licensing models for OEM customers |
| Competitive_Analysis/ | Competitor product analysis, patent positions, market gaps |

## IP Protection Layers

### Layer 1: Patents (Offensive)
- 5 utility patents on novel methods and architectures (see 06_Patent_Strategy)
- 3 design patents on physical form factor and connectors
- Filed BEFORE any public disclosure
- International coverage via PCT in 6 priority territories

### Layer 2: Trade Secrets (Defensive)
- Carrier-to-SoM pinout specification
- Signal routing optimization techniques and PCB layout rules
- Platform configuration algorithms and variant generation
- Calibration thresholds and model tuning parameters
- Indian road dataset and ML training procedures
- EMI mitigation recipes and filter circuit designs
- Power sequencing timing values

### Layer 3: Copyright (Automatic)
- All firmware source code (HAL, drivers, application)
- All documentation (specifications, datasheets, user guides)
- All schematic/PCB design files (OrCAD, Altium project files)
- HAL API definitions and interface specifications
- Training datasets (database copyright)

### Layer 4: Contractual (Relational)
- NDAs with all vendors and partners (see NDA_Templates/)
- IP assignment clauses in employment agreements
- License terms restricting reverse engineering
- OEM customer agreements with IP protection clauses
- Contractor agreements with work-for-hire provisions

## Licensing Model Options

| Model | Description | Use Case |
|-------|-------------|----------|
| Platform License | OEM pays per-unit royalty for carrier + HAL | Volume OEM customers |
| Design License | OEM pays one-time fee for carrier design files | OEM wants to self-manufacture |
| SoM Certification | SoM vendors pay to be "ADVIS Compatible" | Ecosystem expansion |
| Full Stack License | Complete platform + firmware + tools | Tier-1 integration partners |
| Algorithm License | Decision fusion + calibration algorithms only | OEMs with own hardware |

## ADVIS IP Portfolio Summary

```
+------------------------------------------------------------------+
|                    ADVIS IP Protection Map                         |
|                                                                  |
|  PATENTS (Public, Offensive)          TRADE SECRETS (Private)     |
|  +----------------------------+      +-------------------------+  |
|  | ID-001: Adaptive Platform  |      | Exact pinout specs      |  |
|  | ID-002: Windshield Module  |      | PCB routing rules       |  |
|  | ID-003: Decision Fusion    |      | Calibration thresholds  |  |
|  | ID-004: Mutual Calibration |      | ML training data/params |  |
|  | ID-005: Power Control      |      | EMI mitigation recipes  |  |
|  | DP-001: Module Form Factor |      | Power timing values     |  |
|  | DP-002: SoM Blade Design   |      | Vendor pricing/costs    |  |
|  | DP-003: Connector Design   |      | OEM customization data  |  |
|  +----------------------------+      +-------------------------+  |
|                                                                  |
|  COPYRIGHT (Automatic)                CONTRACTUAL (Relational)    |
|  +----------------------------+      +-------------------------+  |
|  | Firmware source code       |      | Vendor NDAs             |  |
|  | Documentation              |      | Employee IP assignment  |  |
|  | Design files               |      | OEM license agreements  |  |
|  | Training datasets          |      | Contractor work-for-hire|  |
|  | API specifications         |      | Evaluation agreements   |  |
|  +----------------------------+      +-------------------------+  |
|                                                                  |
+------------------------------------------------------------------+
```

## Key Principles

1. **File before disclose**: No patentable concept may be disclosed publicly before provisional filing
2. **Defense in depth**: Each IP element is protected by multiple layers (patent + trade secret + contract)
3. **Need-to-know access**: Trade secrets accessible only to personnel who require them for their role
4. **Audit trail**: All access to sensitive IP is logged and auditable
5. **Separation of concerns**: Patent disclosures contain architecture-level detail only; implementation details remain trade secrets

---

**Document Version:** 2.0  
**Last Updated:** 2025-01  
**Classification:** CONFIDENTIAL - Internal Use Only
