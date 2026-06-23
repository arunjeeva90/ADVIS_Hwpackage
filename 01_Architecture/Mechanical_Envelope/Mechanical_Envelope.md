# ADVIS Mechanical Envelope

## Version
v1.0 - June 2026

## Document ID
ARCH-MECH-001

---

## 1. Overview

This document defines the mechanical envelope, mounting strategy, and physical constraints for the ADVIS ECU platform. The system is designed for windshield-mount or headliner-mount installation in passenger and commercial vehicles.

---

## 2. Target Form Factor

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Length | 140mm max | Along vehicle X-axis |
| Width | 90mm max | Along vehicle Y-axis |
| Height | 35mm max | Along vehicle Z-axis (depth from windshield) |
| Weight | 350g max (including enclosure) | Target for windshield adhesive mount |
| PCB dimensions | 120mm x 75mm | 4-layer minimum |
| PCB thickness | 1.6mm standard | FR4, Tg > 170C |

---

## 3. Enclosure Design

```
    TOP VIEW (looking toward windshield)
    +----------------------------------+
    |                                  |
    |  [Camera window FWD]  [DMS win]  |
    |                                  |
    |  +----------------------------+  |
    |  |        PCB AREA            |  |
    |  |                            |  |
    |  |  J100(rear)   J300(side)   |  |
    |  |                            |  |
    |  +----------------------------+  |
    |                                  |
    +----------------------------------+

    SIDE VIEW
    +---------+
    |  Lid    | <- Thermal interface to SoM heatsink
    |---------|
    |  PCB    |
    |---------|
    |  Base   | <- Mounting bracket interface
    +---------+
        |
    [Mount bracket / adhesive pad]
        |
    ===WINDSHIELD===
```

---

## 4. Enclosure Material Options

| Material | Pros | Cons | Recommended For |
|----------|------|------|-----------------|
| Aluminum (die-cast) | Excellent thermal, EMI shielding | Weight, cost | ADVIS Fusion (high thermal) |
| Aluminum (sheet) | Good thermal, lighter | Less EMI integrity | ADVIS Control |
| Glass-filled Nylon (PA66-GF30) | Light, low cost, mouldable | Poor thermal conduction | ADVIS Assist, Fleet |
| PC/ABS blend | Optical clarity for camera windows | Limited thermal | Camera window area only |

---

## 5. IP Rating Target

| Parameter | Target | Rationale |
|-----------|--------|-----------|
| Ingress Protection | IP54 minimum | Dust-protected, splash-proof |
| Seal method | Gasket between lid and base | Replaceable silicone gasket |
| Connector sealing | Sealed automotive connectors (J100) | IP67 at connector face |
| USB/SD access | Sealed cap (removable for service) | Not sealed during use |
| Camera windows | Bonded optical windows | No ingress path |

---

## 6. Connector Access Zones

| Connector | Location | Access Direction | Notes |
|-----------|----------|-----------------|-------|
| J100 (Vehicle) | Rear face | Horizontal (toward cabin) | Primary harness, must be accessible |
| J200 (FWD camera) | Top face | Vertical (toward windshield) | Short coax to camera module |
| J201 (DMS camera) | Front face | Horizontal (toward cabin) | Short coax to DMS module |
| J300 (USB-C) | Side face | Horizontal | Service access, capped |
| J400 (microSD) | Side face | Horizontal | Service access, capped |
| J500 (Debug UART) | Internal | N/A | Accessed only with lid removed |
| J800 (IR board) | Internal | Vertical stack | Daughter board connector |

---

## 7. Mounting Strategy

### 7.1 Primary Mount: Windshield Adhesive

| Parameter | Specification |
|-----------|---------------|
| Adhesive type | Automotive structural adhesive (3M VHB or equivalent) |
| Bond area | Minimum 30 cm^2 |
| Peel strength | > 15 N/cm at +85C |
| Surface prep | IPA wipe + primer |
| Removal method | Wire-cut (non-destructive to windshield) |

### 7.2 Alternative Mount: Headliner Bracket

| Parameter | Specification |
|-----------|---------------|
| Bracket material | Steel, powder-coated |
| Fastening | M5 bolts to roof structure (2 or 4 point) |
| Vibration isolation | Rubber grommets at mount points |
| Service access | Bracket allows enclosure removal without disconnecting harness |

---

## 8. Vibration and Shock Requirements

| Parameter | Specification | Standard |
|-----------|---------------|----------|
| Random vibration | 10-2000 Hz, per vehicle zone profile | ISO 16750-3, Table 12 |
| Mechanical shock | 50g, 6ms half-sine, 3 axes | ISO 16750-3, Table 1 |
| PCB resonance | First mode > 200 Hz (target) | Design for stiffness |
| Connector retention | 50N minimum pull force | Per connector datasheet |
| Solder joint life | > 10 years under thermal cycling | IPC-SM-785 analysis |

---

## 9. Weight Budget

| Item | Weight (g) | Notes |
|------|-----------|-------|
| PCB assembly | 80 | Components + solder + PCB |
| SoM module | 30 | Including heatsink |
| Enclosure (base + lid) | 150 | Aluminum target |
| Gaskets and TIM | 15 | Silicone gasket + thermal pads |
| Mounting bracket | 40 | If bracket-mounted |
| Connectors (mated) | 25 | J100 + camera connectors |
| **TOTAL** | **340** | Under 350g target |

---

## 10. Camera Window Requirements

| Parameter | Specification |
|-----------|---------------|
| Material | Optical-grade polycarbonate or glass |
| Transmission | > 92% at 850nm (for IR DMS) and visible (for FWD) |
| Anti-reflection coating | Recommended (both surfaces) |
| Scratch resistance | Hard-coat (pencil hardness > 3H) |
| Mounting | Bonded with optical adhesive (no air gap) |
| Field of view clearance | No vignetting for specified camera FOV |

---

## 11. Thermal Interface to Enclosure

| Interface Point | Method | Thermal Resistance Target |
|-----------------|--------|--------------------------|
| SoM to lid | Thermal pad (compressible) | < 2 C/W |
| PCB to base | Gap filler (optional, for high-power tiers) | < 5 C/W |
| Lid to ambient | Natural convection + radiation | Depends on enclosure area |

---

## 12. Revision History

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| 1.0 | 2026-06 | Mechanical Team | Initial release |
