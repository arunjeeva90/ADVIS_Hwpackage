# ADVIS Assembly Drawing Requirements

**Document ID:** ADVIS-PCB-ASM-001  
**Version:** 0.1.0  
**Status:** Draft  
**Last Updated:** 2024-01-15

---

## 1. Purpose

This document defines the requirements for assembly drawings that accompany the ADVIS
ECU carrier board Gerber release package. Assembly drawings are used by the EMS
(Electronics Manufacturing Services) partner for production build, inspection,
and quality control.

---

## 2. Required Drawing Views

### 2.1 Mandatory Views

| View | Description | Layer Data Included |
|------|-------------|-------------------|
| Top Assembly | Component placement, top side | Silkscreen, Fab, Assembly, Courtyard |
| Bottom Assembly | Component placement, bottom side | Silkscreen, Fab, Assembly, Courtyard |
| Top Paste | Solder paste stencil pattern | Paste mask openings |
| Bottom Paste | Solder paste stencil pattern | Paste mask openings |
| Drill Drawing | All drill locations and sizes | Drill map, legend |
| Board Outline | Mechanical dimensions, cutouts | Board edge, mounting holes |
| Stackup Cross-section | Layer stackup reference | Diagrammatic (not Gerber) |

### 2.2 Optional Views (recommended for production)

| View | Description | When Required |
|------|-------------|---------------|
| Panelization Drawing | Panel layout with fiducials | Volume production |
| Selective Solder Map | Through-hole component locations | If TH components present |
| Conformal Coat Map | Areas to coat and keep-out zones | If conformal coating required |
| Stiffener Drawing | Board stiffener placement | If flex-rigid construction |

---

## 3. Layer-by-Layer Content Requirements

### 3.1 Top Assembly View

Must include:
- All component outlines with correct orientation
- Reference designators (legible, minimum 0.8mm text height)
- Pin 1 / polarity indicators on all ICs and polarized components
- Component placement coordinates (X, Y, rotation) in accompanying data file
- Board outline with dimensions
- Fiducial mark locations
- Mounting hole centers with diameter callout
- Drawing title block (board name, revision, date, drawn by)

### 3.2 Bottom Assembly View

Same requirements as top assembly, mirrored view (as seen from bottom looking up).

### 3.3 Drill Drawing

Must include:
- All drill locations plotted
- Drill legend table: tool number, size, quantity, plated/non-plated
- Finished hole size (after plating)
- Board origin reference (0,0 datum)
- Tolerances for drill position (+/- 0.05mm) and size (+/- 0.05mm)
- Slot locations and dimensions (if any)
- Via-in-pad notation (filled/capped where applicable)

---

## 4. Polarity and Orientation Markings

### 4.1 IC Orientation

| Package Type | Marking Method |
|-------------|----------------|
| QFN / DFN | Pin 1 dot on assembly layer, pad 1 distinguished in paste pattern |
| QFP | Pin 1 dot + bevel on outline |
| SOIC | Pin 1 dot on outline |
| SOT-23 | Pin 1 indicated on outline |
| BGA | Pin A1 dot + diagonal corner mark |

### 4.2 Passive Component Polarity

| Component | Marking Method |
|-----------|----------------|
| Electrolytic capacitor | "+" symbol at positive end |
| Tantalum capacitor | Band marking at anode end |
| Diode / TVS | Cathode band |
| LED | "K" at cathode, arrow symbol |
| Polarized connector | Pin 1 arrow, key marking |

---

## 5. Placement Coordinate File

In addition to graphical assembly drawings, a machine-readable placement file must be
provided with the following format:

| Column | Description | Example |
|--------|-------------|---------|
| RefDes | Reference designator | U1 |
| X | X coordinate from origin (mm) | 25.400 |
| Y | Y coordinate from origin (mm) | 12.700 |
| Rotation | Angle in degrees (CCW from X-axis) | 90 |
| Side | Top or Bottom | Top |
| Part Number | MPN from BOM | LM61460-Q1 |
| Package | Package description | HTSSOP-16 |
| Value | Component value (if applicable) | 5V 6A Buck |

---

## 6. Special Assembly Notes

The assembly drawing must include a notes section calling out:

### 6.1 Thermal Pad Requirements

| Component | Pad Treatment | Notes |
|-----------|---------------|-------|
| LM61460-Q1 | Solder paste with window-pane pattern | Prevent voiding, ensure thermal contact |
| TPS62130A-Q1 | Solder paste with cross-hatch pattern | Thermal pad on bottom |
| DS90UB954-Q1 | Solder paste, controlled reflow | Ensure ground contact |
| QFN packages (general) | 50-70% paste coverage on thermal pad | Voiding target < 25% |

### 6.2 Process Notes

1. Lead-free assembly process (SAC305 solder paste, peak reflow 245-250C)
2. Board must be baked if humidity exposure exceeds MSL requirements
3. Fine-pitch components (< 0.5mm pitch) require Type 4 solder paste minimum
4. Stencil thickness: 0.12mm (recommended for mix of fine and standard pitch)
5. Stencil aperture modifications noted in paste layer data
6. ESD-sensitive components: handle per ANSI/ESD S20.20

### 6.3 DNI Notations

Assembly drawings must clearly indicate DNI (Do Not Install) components:
- Marked with "DNI" text adjacent to component outline
- DNI components listed in separate table on drawing
- Variant-specific DNI matrix referenced (Entry/Mid/High tier)
- Assembly house receives tier-specific loading file per production order

---

## 7. BOM Cross-Reference

Assembly drawings must include or reference:
- BOM revision that matches the drawing revision
- Any BOM alternates approved for this build
- Component substitution rules (if EMS may substitute)
- Minimum: "Build to BOM Rev X.Y" note on drawing

---

## 8. Inspection Criteria

The assembly drawing defines workmanship standards:

| Criterion | Standard | Reference |
|-----------|----------|-----------|
| Solder joint quality | IPC-A-610 Class 2 (minimum) | IPC-A-610H |
| QFN void percentage | < 25% of thermal pad area | X-ray inspection required |
| Solder paste alignment | Per stencil, within 50% of pad | Visual/AOI inspection |
| Component presence | 100% AOI after reflow | Machine vision |
| Polarity verification | All polarized components | AOI + visual sampling |

---

## 9. Drawing Revision Control

| Field | Content |
|-------|---------|
| Drawing Number | ADVIS-ECU-CARRIER-ASM-[REV] |
| Revision | Matches Gerber/BOM revision |
| Date | Release date |
| Drawn By | Designer name |
| Checked By | Reviewer name |
| Approved By | HW Lead name |
| ECO Number | Engineering Change Order reference |

---

## 10. File Delivery Format

Assembly drawings delivered to EMS in the following formats:

| Format | Purpose |
|--------|---------|
| PDF | Visual reference, human-readable |
| DXF / DWG | CAD-importable for fixture design |
| Centroid file (CSV) | Pick-and-place machine programming |
| Gerber (assembly layers) | Machine-readable layer data |
| ODB++ or IPC-2581 | Complete fabrication/assembly dataset |

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1.0 | 2024-01-15 | -- | Initial assembly drawing requirements |
