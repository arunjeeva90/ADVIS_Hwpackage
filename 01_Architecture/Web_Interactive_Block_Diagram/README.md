# ADVIS v0.5 — Interactive Hardware Architecture Diagram

**IND-VIAS / ADVIS Hardware Block Diagram — Web Interactive Edition**

---

## Purpose

This interactive web diagram visually represents the ADVIS v0.5 hardware architecture for the IND-VIAS project. It is intended as a living engineering reference for:

- Hardware architecture review and stakeholder communication
- SoC candidate evaluation and comparison
- Mode-based configuration exploration (Assist / Control / Fleet / Validation Board)
- Safety boundary and signal flow documentation

The diagram is **not** a simulation, certification document, or final BOM. All values are targets or planning-class designations subject to engineering review, vendor quotes, and production validation.

---

## How to Open Locally

No build tools, no server, no dependencies required.

1. Open your file manager and navigate to this folder.
2. Double-click `index.html`.
3. It will open directly in your default browser.

Or from a terminal:

```bash
# macOS
open 01_Architecture/Web_Interactive_Block_Diagram/index.html

# Linux
xdg-open 01_Architecture/Web_Interactive_Block_Diagram/index.html

# Windows (Command Prompt)
start 01_Architecture/Web_Interactive_Block_Diagram/index.html
```

Tested in: Chrome 120+, Firefox 120+, Edge 120+, Safari 17+.

---

## File Structure

```
01_Architecture/Web_Interactive_Block_Diagram/
├── index.html          ← Main interactive diagram (self-contained)
├── README.md           ← This documentation file
└── assets/             ← Future assets folder (images, exports, PDFs)
    └── .gitkeep
```

All HTML, CSS, and JavaScript are embedded in `index.html`. No external CDN calls are made. The file is fully self-contained and works offline.

---

## Interaction Guide

| Action | Result |
|--------|--------|
| **Click a block** | Opens the side panel with full block details, specifications, and engineering notes |
| **Hover a block** | Shows a quick tooltip with key info |
| **Click background** | Closes the side panel and clears selection |
| **Mode selector (top bar)** | Switches the architecture view between Assist / Control / Fleet / Validation Board modes |
| **SoC Candidates chips** | Highlights a specific SoC and auto-switches to its associated mode |
| **✕ button (side panel)** | Closes the detail panel |

### Mode Descriptions

| Mode | Primary SoC | Description |
|------|------------|-------------|
| **Assist Mode** | TDA4VL-Q1 (4 TOPS) | ADAS-focused lane assist, forward collision warning. Primary Assist candidate. |
| **Control Mode** | TDA4VM-Q1 (8 TOPS) | Full ADAS+DMS with higher compute margin. Safest Control candidate. |
| **Fleet Mode** | AM62A7-Q1 (2 TOPS) | Fleet-lite, DMS-only, single-camera, or aggregated-input deployment. |
| **Validation Board** | SOM + FPD-Link (v0.4.4) | Validation baseline with FPD-Link serialization. Not v0.5 production architecture. |

---

## Architecture Baseline

### v0.5 — Compact Direct-MIPI Production Architecture

ADVIS v0.5 targets a **single windshield-mounted ECU** with:

- **Forward Road Camera** → Direct MIPI CSI-2 4-lane → Primary SoC
- **In-Cabin DMS Camera** → Direct MIPI CSI-2 2-lane → Primary SoC (shared compute)
- **No FPD-Link / serializer chain** — cameras connect directly via MIPI CSI-2 to the SoC
- **Single shared SoC** for both ADAS and DMS intelligence with risk-coupled fusion
- **CAN-FD vehicle interface** for ADAS request messages to OEM ECUs
- **Optional Ethernet** for diagnostics and OTA (not required for core operation)
- **Safety monitor and fallback path** for ASIL-B capable warning/request path (target)

### v0.4.4 — SOM/FPD-Link Validation Baseline

The v0.4.4 configuration uses:

- SOM (System-on-Module) platform
- FPD-Link camera serialization chain
- Used for hardware bring-up and validation only
- **Not the v0.5 production architecture**

The Validation Board mode in the diagram highlights this baseline for reference.

---

## SoC and Camera Positioning

### Primary SoC Candidates

| SoC | TOPS | Notes |
|-----|------|-------|
| **TDA4VL-Q1** | 4 TOPS | J721e-class. **Primary ADVIS Assist candidate.** GPU + MMA. ASIL-B capable (target). |
| **TDA4VM-Q1** | 8 TOPS | J721e-class. **Safest ADVIS Control candidate.** GPU + MMA. ASIL-B capable (target). |

### Comparison Candidates

| SoC | TOPS | Notes |
|-----|------|-------|
| **TDA4AL-Q1** | 8 TOPS | Analytics-focused. **No GPU** — not recommended for DNN inference workloads. Comparison only. |
| **TDA4VE-Q1** | 8 TOPS | J721S2-class. Higher-resource comparison candidate. Not default primary for v0.5. |
| **AM62A7-Q1** | 2 TOPS | Single-camera / DMS-only / Fleet-lite / aggregated-input. **Not default dual-independent-MIPI ADVIS v0.5.** |

### Camera Designations

| Camera | Class | Interface | Notes |
|--------|-------|-----------|-------|
| Forward Road Camera | OX03C10-class | MIPI CSI-2 4-lane | ~3 MP, planning class |
| In-Cabin DMS Camera | OX01N1B / OX01H1B-class | MIPI CSI-2 2-lane | ~1.3 MP, planning class |

---

## Safety Boundary

- The ASIL-B capable warning/request path is a **design target** for ADVIS v0.5, subject to full safety analysis per ISO 26262.
- **No final ASIL certification is claimed** for any ADVIS v0.5 component.
- ADVIS **does not directly control brake, steering, or throttle**.
- All vehicle intervention signals are **ADAS request messages over CAN-FD**.
- Final actuator authority remains with **OEM ECUs** in all operating modes.
- The safety fallback path sends a minimal advisory CAN message on fault — OEM ECUs determine actual vehicle response.

---

## Open Decisions (as of diagram date)

- Final SoC selection (TDA4VL-Q1 vs. TDA4VM-Q1) pending compute margin analysis and BOM cost review.
- LPDDR4X memory capacity TBD — pending final SoC selection.
- eMMC storage capacity TBD — pending firmware + model weight sizing.
- PMIC part number TBD — subject to vendor quotes and rail count.
- Ethernet inclusion (optional interface) — pending OTA and diagnostic requirements.
- AM62A7-Q1 fleet variant scope TBD — dependent on fleet customer requirements.
- ASIL-B safety analysis scope TBD — pending HARA and system-level safety review.

---

## Animation Logic

The diagram runs a startup sequence on page load:

1. **Overlay animation** — progress bar with system initialization messages.
2. **Block entrance** — all architecture blocks fade in with staggered scale animation.
3. **Signal flow dots** — animated dots travel along each signal path continuously, representing live data flow. Flow dots are color-coded by signal type.
4. **Mode transitions** — switching modes updates the SoC label, dims irrelevant blocks, and shows/hides signal paths.

### Signal Path Colors

| Color | Signal Type |
|-------|------------|
| Cyan (`#00e5ff`) | MIPI CSI-2 — Forward Road Camera |
| Green (`#30d158`) | MIPI CSI-2 — DMS Camera |
| Purple (`#bf5af2`) | Memory Bus (LPDDR4X / eMMC) |
| Orange (`#ff9f0a`) | CAN-FD — Vehicle Interface |
| Blue (`#0a84ff`) | Ethernet — Diagnostics/OTA (dashed) |
| Red (`#ff453a`) | Safety Monitor Link (dashed) |
| Salmon (`#ff6b6b`) | Safety Fallback Path (dashed) |
| Yellow (`#ffd60a`) | Power Rails (dashed) |

---

## Mode Behavior Details

### Assist Mode (TDA4VL-Q1)
- Forward camera MIPI, DMS camera MIPI, memory bus, CAN-FD, safety monitor, power, and fallback paths all active.
- Ethernet dimmed (not required for Assist operation).
- AM62A7-Q1 comparison block dimmed (not relevant to Assist architecture).

### Control Mode (TDA4VM-Q1)
- All signal paths active, including Ethernet.
- Higher-resource SoC; same J721e family as TDA4VL-Q1.
- TDA4AL-Q1 and AM62A7-Q1 dimmed.

### Fleet Mode (AM62A7-Q1)
- DMS camera path, CAN-FD, Ethernet, and power active.
- Forward road camera MIPI dimmed (single-camera or aggregated-input use case).
- Memory bus and safety fallback dimmed.

### Validation Board Mode (v0.4.4)
- SoC label updates to SOM + FPD-Link baseline.
- Validation baseline block revealed.
- Most v0.5-specific signal paths dimmed.
- CAN-FD, power, and safety monitor paths remain visible.

---

## Future Assets Folder

The `assets/` directory is reserved for:

- Exported PNG/SVG versions of the architecture diagram
- PDF print-ready versions
- Datasheets referenced in the diagram (if permitted to redistribute)
- Block diagram source files (draw.io, Lucidchart exports)
- Photos of validation hardware

---

## Disclaimers and Limitations

1. **BOM values** are target/direction only — subject to vendor quotes and production volume.
2. **Sensor specifications** are planning class unless explicitly datasheet-confirmed.
3. **ASIL-B claims** are design targets for the warning/request path only. Subject to full safety analysis. No certification is claimed.
4. **Actuation**: ADVIS does not directly control brake, steering, or throttle. All signals are ADAS request messages over CAN-FD. OEM ECUs retain final authority.
5. This diagram is a hardware architecture reference — it is not a schematic, layout, or manufacturing document.
6. Signal path routing in the diagram is illustrative — actual PCB routing will differ.
7. All SoC TOPS values are as published by Texas Instruments. ADVIS-achievable performance subject to workload profiling.

---

*IND-VIAS / ADVIS v0.5 Hardware Architecture — Web Interactive Block Diagram*
*Repository: ADVIS_Hwpackage*
