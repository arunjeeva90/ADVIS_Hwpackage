# ADVIS v0.5 Compact Board 3D View - Visual Concept

**Classification:** CONFIDENTIAL - ENGINEERING USE ONLY  
**Status:** CONCEPTUAL - Not production layout, not mechanical CAD release  
**Version:** v0.1 - June 2026  
**Document ID:** ARCH-VIS-001

---

## 1. Purpose

This document describes the conceptual 3D isometric board view for the ADVIS v0.5 Compact Module. The accompanying SVG file provides a visual representation of component placement, optical paths, and signal flow on the windshield-mounted PCB assembly.

**Disclaimer:** Conceptual visualization only - not production layout, not mechanical CAD release. Component positions, sizes, and proportions are approximate and intended for architecture communication purposes only.

---

## 2. Visual Elements

The isometric board view illustrates the following labeled elements:

| Label | Component / Region | Notes |
|-------|-------------------|-------|
| Forward Camera | Image sensor (IMX390/OX03C10/AR0233 class) | Front-facing, direct MIPI CSI-2 to SoC Port 0 |
| DMS Camera | Image sensor (OX01N1B/OX01H1B class) | Cabin-facing, connected via flex cable to SoC Port 1 |
| DMS Flex | Rigid-flex cable (~50mm) | Carries MIPI CSI-2 + I2C from DMS PCBlet to main board |
| Main SoC | TDA4VL-Q1 / TDA4VM-Q1 (BGA, center of board) | Primary compute element |
| LPDDR4 | Memory IC (adjacent to SoC) | 2GB (Assist) or 4GB (Control) |
| eMMC | Storage IC | 16GB (Assist) or 32GB (Control) |
| PMIC/Power Tree | Power management cluster | LM61460 + TPS62130A + TLV75518 + sensor LDOs |
| CAN-FD PHY | TCAN1044AV-Q1 | Vehicle communication transceiver |
| Vehicle Connector | J100 automotive sealed connector | Power + CAN + ignition + wake |
| IR LEDs | IR illumination array (940nm) | DMS illumination, driven by LED driver IC |
| Thermal Spreader/Rear Plate | Aluminum rear plate | Structural + thermal dissipation path |
| Test Pads | Debug/programming access | UART + JTAG via pogo-pin fixture |

---

## 3. Signal Path Annotations

The visualization includes arrows indicating:

- **Optical paths:** Forward camera field of view (road-facing) and DMS camera field of view (cabin-facing)
- **MIPI signal paths:** CSI-2 data lanes from each camera sensor to the SoC
- **Power distribution:** From vehicle connector through protection and regulation stages to SoC and peripherals
- **Communication:** CAN-FD data path from SoC through PHY to vehicle connector

---

## 4. Color Coding

| Color | Meaning |
|-------|---------|
| Light blue | Digital / compute components (SoC, DDR, eMMC) |
| Light green | Camera / optical subsystem |
| Light orange | Power management components |
| Light purple | Communication interfaces (CAN, connector) |
| Light gray | Mechanical / structural (thermal plate, housing) |
| Red arrows | Optical paths |
| Blue arrows | Signal / data paths |

---

## 5. Related Files

- SVG Visualization: [ADVIS_v0.5_Compact_Board_3D_View.svg](./ADVIS_v0.5_Compact_Board_3D_View.svg)
- Exploded View: [ADVIS_v0.5_Compact_Module_Exploded_View.svg](./ADVIS_v0.5_Compact_Module_Exploded_View.svg)
- System Block Diagram: [ADVIS_v0.5_Compact_System_Block_Diagram.md](../System_Block_Diagrams/ADVIS_v0.5_Compact_System_Block_Diagram.md)

---

## 6. Revision History

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| 0.1 | 2026-06 | Architecture Team | Initial conceptual visualization document |

---

*Conceptual visualization only - not production layout, not mechanical CAD release.*

*End of Document*
