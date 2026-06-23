# ADVIS Design-for-Manufacturing Checklist

**Document ID:** ADVIS-PCB-DFM-001  
**Version:** 0.1.0  
**Status:** Template  
**Last Updated:** 2024-01-15

---

## 1. Purpose

This checklist ensures the ADVIS ECU carrier board PCB design meets manufacturing
requirements for volume production. All items must be verified before Gerber release
to the fabrication house and assembly partner.

---

## 2. PCB Fabrication Constraints

### 2.1 Trace and Space

| Parameter | Minimum | Preferred | Notes |
|-----------|---------|-----------|-------|
| Trace width (outer) | 0.10mm | 0.125mm | Controlled impedance traces may differ |
| Trace width (inner) | 0.10mm | 0.100mm | Inner layers use thinner copper |
| Trace spacing (outer) | 0.10mm | 0.125mm | Between any copper features |
| Trace spacing (inner) | 0.10mm | 0.100mm | |
| Trace to board edge | 0.25mm | 0.50mm | Manufacturing panel routing |
| Annular ring (outer) | 0.10mm | 0.125mm | Pad overhang from drill edge |
| Annular ring (inner) | 0.075mm | 0.10mm | |

### 2.2 Via Specifications

| Parameter | Standard | Power | Micro-via |
|-----------|----------|-------|-----------|
| Drill diameter | 0.25mm | 0.35mm | 0.10mm |
| Pad diameter (outer) | 0.50mm | 0.65mm | 0.25mm |
| Pad diameter (inner) | 0.45mm | 0.60mm | N/A |
| Aspect ratio (max) | 8:1 | 6:1 | 1:1 |
| Via-to-via spacing | 0.20mm | 0.25mm | 0.15mm |
| Via-to-trace spacing | 0.15mm | 0.20mm | 0.15mm |

### 2.3 Solder Mask

| # | Check Item | Pass | Fail | Notes |
|---|-----------|------|------|-------|
| SM-01 | Solder mask opening >= pad size + 0.05mm per side | | | |
| SM-02 | Solder mask dam between pads >= 0.10mm | | | |
| SM-03 | Solder mask defined pads used for BGA (if applicable) | | | |
| SM-04 | Non-solder-mask-defined pads for QFN exposed pads | | | |
| SM-05 | Solder mask color specified (green standard) | | | |
| SM-06 | No solder mask over testpad targets | | | |
| SM-07 | Solder mask web between fine-pitch IC pads verified | | | |

---

## 3. Pad and Footprint Design

| # | Check Item | Pass | Fail | Notes |
|---|-----------|------|------|-------|
| PD-01 | All footprints verified against manufacturer recommended land pattern | | | |
| PD-02 | QFN exposed pad size per datasheet recommendation | | | |
| PD-03 | Thermal pad solder paste reduction applied (typically 50-70% coverage) | | | |
| PD-04 | Fine-pitch pads (< 0.5mm pitch) have solder paste aperture reduction | | | |
| PD-05 | Pad shapes appropriate for reflow (no acute angles) | | | |
| PD-06 | Component courtyard clearance maintained | | | |
| PD-07 | All pads have at least one net connection (no isolated copper) | | | |
| PD-08 | Through-hole pins have adequate annular ring for wave/selective solder | | | |

---

## 4. Fiducial and Alignment

| # | Check Item | Pass | Fail | Notes |
|---|-----------|------|------|-------|
| FD-01 | 3 global fiducial marks placed (triangle pattern) | | | |
| FD-02 | Fiducial size: 1.0mm diameter, 2.0mm clearance (no copper/mask) | | | |
| FD-03 | Local fiducials near fine-pitch components (QFP-64, etc.) | | | |
| FD-04 | Fiducials on both sides if double-sided assembly | | | |
| FD-05 | Fiducials not near board edge or mounting holes | | | |

---

## 5. Silkscreen and Markings

| # | Check Item | Pass | Fail | Notes |
|---|-----------|------|------|-------|
| SK-01 | All reference designators visible and legible (min 0.8mm height) | | | |
| SK-02 | Pin 1 indicators on all ICs | | | |
| SK-03 | Polarity markers on all diodes, electrolytic caps, LEDs | | | |
| SK-04 | Board name, revision, date code area marked | | | |
| SK-05 | Orientation arrows on asymmetric connectors | | | |
| SK-06 | No silkscreen over pads or solder mask openings | | | |
| SK-07 | Assembly variant marking area (Entry/Mid/High tier) | | | |
| SK-08 | ADVIS logo and part number placement | | | |
| SK-09 | RoHS/WEEE compliance markings | | | |
| SK-10 | Serial number area (barcode-scannable size) | | | |

---

## 6. Panelization

| # | Check Item | Pass | Fail | Notes |
|---|-----------|------|------|-------|
| PN-01 | Panel size within assembly machine limits | | | |
| PN-02 | Breakaway tabs with V-score or mouse-bite perforations | | | |
| PN-03 | No components within 5mm of breakaway edge | | | |
| PN-04 | Panel fiducials in addition to board fiducials | | | |
| PN-05 | Tooling holes for panel handling (minimum 2) | | | |
| PN-06 | Panel rail width sufficient for conveyor transport (min 5mm) | | | |
| PN-07 | Board orientation consistent in panel (no rotation) | | | |

---

## 7. Testpad and ICT Access

| # | Check Item | Pass | Fail | Notes |
|---|-----------|------|------|-------|
| TP-01 | Testpads on all power rails (5V_SYS, 3V3_IO, 1V8) | | | |
| TP-02 | Testpads on critical signals (SOM_BOOT_OK, nRESET, CAN_H/L) | | | |
| TP-03 | Testpad minimum size: 0.8mm diameter | | | |
| TP-04 | Testpad spacing: minimum 2.54mm (100mil) center-to-center | | | |
| TP-05 | All testpads accessible from one board side (top preferred) | | | |
| TP-06 | No testpads under tall components or connectors | | | |
| TP-07 | Testpad grid aligned where possible for fixture design | | | |
| TP-08 | Ground testpads distributed across board (min 4) | | | |

---

## 8. Copper Fill and Pour

| # | Check Item | Pass | Fail | Notes |
|---|-----------|------|------|-------|
| CF-01 | All plane layers have copper flood (no large void areas) | | | |
| CF-02 | Copper balance between layers within 20% | | | |
| CF-03 | Thermal relief connections on ground plane (4-spoke, 0.25mm) | | | |
| CF-04 | No isolated copper islands (DRC check) | | | |
| CF-05 | Ground stitching vias around board perimeter (every 10mm) | | | |
| CF-06 | Copper fill clearance to board edge: 0.5mm minimum | | | |
| CF-07 | Thieving pattern added in sparse areas (acid trap prevention) | | | |

---

## 9. Special Assembly Notes

| # | Check Item | Pass | Fail | Notes |
|---|-----------|------|------|-------|
| SA-01 | QFN thermal pad solder paste pattern defined (window pane or cross-hatch) | | | |
| SA-02 | Components requiring selective soldering identified | | | |
| SA-03 | Mixed-technology assembly sequence defined (SMT first, then TH) | | | |
| SA-04 | Tall components on one side only (or two-pass reflow documented) | | | |
| SA-05 | Temperature-sensitive components identified (max reflow cycles noted) | | | |
| SA-06 | Conformal coating keep-out areas marked (connectors, testpads) | | | |
| SA-07 | Assembly drawing references this checklist for special items | | | |

---

## 10. DFM Sign-off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| PCB Designer | | | |
| DFM Engineer | | | |
| Assembly Engineer | | | |
| Quality Engineer | | | |

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1.0 | 2024-01-15 | -- | Initial DFM checklist template |
