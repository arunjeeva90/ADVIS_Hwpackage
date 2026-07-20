# ADAS Feature to Radar Deployment Matrix

## Feature mapping

| ADAS_Feature | Recommended_Deployment | Range_Target | Field_of_View_Target | Mandatory_Radar_Output | Fusion_Notes | Candidate_Direction |
|---|---|---|---|---|---|---|
| FCW | Front radar | 150–250 m minimum useful target | ±45–60° | Range, radial velocity, object list, target confidence | Camera improves object classification and relevance | Ainstein K-77; MR76; ARS408 benchmark; Aptiv FLR7/Tier-1 RFQ |
| ACC | Front long-range radar | 200–300 m preferred | ±45–60° | Stable lead-object track, cut-in/out, acceleration, covariance | Camera lane association and vehicle classification | Ainstein K-77 PoC; smartmicro DRVEGRD 171; Tier-1 production RFQ |
| AEB | Front radar + forward camera | 150–300 m with strong near-range coverage | ±45–60° | Low-latency tracks, stationary-object handling, health and interference state | Camera classification plus road-path overlap; independent safety gate | Production automotive radar mandatory; cheap kits are not sufficient |
| Cut-in / cut-out prediction | Front or front-corner radar | 100–200 m | Wide ±60–75° | Lateral velocity, object covariance and stable IDs | Camera lane geometry and object type | SRR7+/corner pairs; K-77 front; 4D radar improves separation |
| BSD / BSM | Rear corner radar pair | 50–100 m | Wide ±75° or more | Object list, lateral/longitudinal speed, zone state | Camera optional; improves two-wheeler/pedestrian interpretation | Ainstein T-79; Nanoradar SR73F/SR75; AWRL1432BOOST-BSD; low-cost kit for HMI only |
| Lane Change Assist | Rear corner radar pair | 80–150 m preferred | ±75° | Approach speed, time-to-zone, track continuity | Camera/lane model improves host-lane assignment | Premium corner radar or validated smart module |
| Rear Cross Traffic Alert | Rear corner radar pair | 30–80 m | Very wide side/rear coverage | Crossing-track detection and velocity | Rear camera improves classification and occlusion handling | T-79; SR73F; Tier-1 corner radar |
| Front Cross Traffic Alert | Front corner radar pair | 30–100 m | Wide corner coverage | Crossing targets and time-to-crossing | Front/side camera fusion | SRR7/SRR7+ class; smartmicro DRVEGRD 169; validated China corner radar |
| Door Opening Warning | Rear corner radar pair | 20–60 m | Wide rear-side coverage | Cyclist/vehicle approach speed and path | Camera optional but valuable for VRUs | Corner radar with low-speed/near-field mode |
| Moving Off Information System | Front/side near-field radar plus camera | 0.2–30 m | Ultra-wide, elevation helpful | Close VRU tracks, low minimum range, static/moving separation | Camera is important for VRU classification and legal use-case interpretation | Near-field/corner 4D radar; not a long-range-only sensor |
| Blind Spot Information System for trucks | Side radar(s) | 0.2–50 m or regulation-defined zone | Wide side coverage | Zone objects, VRU movement and robust multipath control | Side camera fusion recommended | CUB turn-assist system; smartmicro; validated Nanoradar/off-highway sensor |
| Low-speed collision avoidance / parking | Near-field 60/77/79 GHz radar | 0.1–20 m | Very wide | Point cloud or occupancy grid | Ultrasonic and camera fusion improve curb/low-object handling | AWRL1432; Acconeer/Infineon research; production near-field radar |
| Highway pilot / L2+ | Front imaging radar + corner radars | 300 m+ front | High angular/elevation resolution | Dense point cloud, free-space, object list, interference diagnostics | Multi-camera fusion mandatory | Continental ARS540; ZF imaging; Arbe/Uhnder/Vayyar/Altos; premium Tier-1 |
| Two-wheeler ARAS front collision warning | Compact front smart radar | 80–150 m practical | ±45–60° | Range/speed and stable two-wheeler/vehicle tracks | Monocular front camera for classification and curve/path relevance | Ainstein K-77/MR76 size-cost study; TI/Calterah custom cost-down |
| Two-wheeler BSD/LCA | Rear compact corner radar(s) | 30–80 m | Wide ±75°+ | Approach speed and warning zones | Rear camera optional; haptic/HMI integration critical | T-79/SR73F/custom AWRL1432; aftermarket kits only for non-safety demo |
| Child presence / cabin occupancy | 60 GHz in-cabin radar | 0–5 m typical cabin | Wide cabin coverage | Micro-motion, occupancy and vital-sign features | DMS/OMS camera for identity/posture | Acconeer A121/XM125; Infineon BGT60; dedicated automotive interior radar |

## Minimum recommended ADVIS radar configurations

### ADVIS Fusion Entry

```text
1 × front smart radar
+ forward camera
+ DMS camera
```

Features:
- radar-confirmed FCW
- ACC-ready lead tracking
- AEB confidence input
- cut-in robustness
- degraded-visibility support

### ADVIS Fusion Safety

```text
1 × front smart radar
+ 2 × rear corner radars
+ forward camera
+ DMS camera
```

Adds:
- BSD/BSM
- LCA
- RCTA
- DOW
- rear two-wheeler approach warning

### ADVIS Fusion 360

```text
1 × front long-range radar
+ 4 × corner radars
+ camera set
```

Adds:
- FCTA
- side VRU
- 360° object continuity
- enhanced AEB/ACC
- MOIS/near-field support depending corner minimum range and FoV

### ADVIS Imaging

```text
1 × front 4D imaging radar
+ 4 × corner radars
+ multi-camera perception
```

Adds:
- elevation
- richer stationary-object discrimination
- free-space/road-edge support
- high-density L2+/L3 perception research

## Important boundary

Radar count alone does not create a safe feature. Each function still needs:
- HARA and safety concept
- vehicle-dynamics inputs
- validated mounting and calibration
- sensor blockage/interference handling
- false-positive/false-negative validation
- OEM brake/EPS/powertrain arbitration where actuation is requested
