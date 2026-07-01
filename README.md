# ADVIS_Hwpackage

**IND-VIAS / ADVIS Hardware Package Repository**

Hardware architecture, BOM targets, and engineering references for the ADVIS (Advanced Driver and Vehicle Intelligence System) v0.5 single-ECU platform.

---

## Repository Structure

```
ADVIS_Hwpackage/
├── 01_Architecture/
│   └── Web_Interactive_Block_Diagram/   ← Interactive hardware diagram (see below)
│       ├── index.html
│       ├── README.md
│       └── assets/
└── README.md
```

---

## Interactive Web Block Diagram

**[→ Open Interactive Hardware Architecture Diagram](01_Architecture/Web_Interactive_Block_Diagram/index.html)**

Open locally in a browser to view the animated ADVIS v0.5 hardware architecture.

- No build steps required — open `index.html` directly.
- Animated startup sequence, signal flow lines, color-coded blocks.
- Mode selector: Assist Mode / Control Mode / Fleet Mode / Validation Board.
- Click-to-focus side panel with full block specifications and engineering notes.
- Hover tooltips on all architecture blocks.
- SoC candidate comparison panel.

See [`01_Architecture/Web_Interactive_Block_Diagram/README.md`](01_Architecture/Web_Interactive_Block_Diagram/README.md) for the full documentation including architecture baseline, safety boundary, open decisions, and interaction guide.

---

## Architecture Summary

**v0.5 — Direct MIPI CSI-2 Production Target**

- Single windshield-mounted ECU
- Forward road camera (OX03C10-class, MIPI CSI-2 4-lane, direct)
- In-cabin DMS camera (OX01N1B/OX01H1B-class, MIPI CSI-2 2-lane, direct)
- Shared SoC compute: ADAS + DMS risk-coupled intelligence
- Primary Assist candidate: TDA4VL-Q1 (4 TOPS)
- Primary Control candidate: TDA4VM-Q1 (8 TOPS)
- CAN-FD vehicle interface (ADAS request messages — OEM ECUs retain final authority)
- Optional Ethernet for diagnostics / OTA
- ASIL-B capable warning/request path target (subject to safety analysis)

**v0.4.4 — SOM/FPD-Link Validation Baseline**

- SOM + FPD-Link camera serialization chain
- Validation and hardware bring-up reference only
- Not the v0.5 production architecture

---

## Key Engineering Positions

| Topic | Position |
|-------|----------|
| ASIL | ASIL-B capable warning/request path — design target · subject to full safety analysis · no certification claimed |
| Actuation | ADVIS sends ADAS request messages over CAN-FD · Final actuator authority with OEM ECUs |
| Sensors | Planning class unless datasheet-confirmed |
| BOM | Target/direction · subject to vendor quotes and production volume |

---

*IND-VIAS / ADVIS Hardware Package — v0.5*
