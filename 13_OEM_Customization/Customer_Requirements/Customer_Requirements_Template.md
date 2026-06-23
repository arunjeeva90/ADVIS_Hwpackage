# ADVIS OEM Customer Requirements Template

## Instructions

This template captures OEM-specific requirements for an ADVIS integration. Complete all mandatory sections (marked with *). Optional sections can be filled as requirements are defined.

---

## 1. Program Information*

| Field | Value |
|-------|-------|
| OEM Name* | [Company name] |
| Program Name* | [Vehicle program / platform code] |
| Contact Name* | [Technical contact] |
| Contact Email* | [Email] |
| Target SOP Date* | [Start of Production date] |
| Vehicle Class* | [Passenger / LCV / HCV / Off-highway] |
| Annual Volume Estimate* | [Units per year] |
| Program Duration* | [Years of production] |

---

## 2. ADVIS Product Selection*

| Selection | Choice |
|-----------|--------|
| Product Variant* | [ ] ADVIS Assist / [ ] ADVIS Control / [ ] ADVIS Fleet / [ ] ADVIS Fusion |
| SoC Tier* | [ ] Entry (AM62A) / [ ] Mid (AM68A) / [ ] High (TDA4VH) |
| Hardware Revision | [v0.4.4 baseline or specify] |

---

## 3. Camera Requirements*

### 3.1 Forward Camera

| Parameter | Requirement |
|-----------|-------------|
| Required* | [ ] Yes / [ ] No |
| Resolution | [e.g., 2MP / 5MP / 8MP] |
| Frame rate | [e.g., 30fps / 60fps] |
| Field of view (horizontal) | [e.g., 100 degrees] |
| Mounting location | [e.g., windshield, behind mirror] |
| Cable length to ECU | [meters] |
| Lens type | [e.g., standard / fisheye / auto-focus] |
| Camera module supplier | [Preferred vendor or TBD] |
| Night vision required | [ ] Yes / [ ] No |

### 3.2 DMS Camera

| Parameter | Requirement |
|-----------|-------------|
| Required* | [ ] Yes / [ ] No |
| Resolution | [e.g., 1.3MP / 2MP] |
| Frame rate | [e.g., 30fps] |
| Mounting location | [e.g., steering column, instrument cluster] |
| Cable length to ECU | [meters] |
| IR illumination required | [ ] Yes / [ ] No |
| IR wavelength preference | [e.g., 850nm / 940nm] |
| Sunglasses transparency req | [ ] Yes / [ ] No |

### 3.3 Additional Cameras (High Tier)

| Camera | Location | Resolution | Purpose |
|--------|----------|-----------|---------|
| Side Left | [Location] | [Resolution] | [BSM/surround] |
| Side Right | [Location] | [Resolution] | [BSM/surround] |
| Rear | [Location] | [Resolution] | [RCTA/parking] |
| Other | [Location] | [Resolution] | [Purpose] |

---

## 4. Feature Requirements*

### 4.1 ADAS Features

| Feature | Required | Priority | Notes |
|---------|----------|----------|-------|
| Forward Collision Warning (FCW) | [ ] Yes / [ ] No | [1-5] | |
| Lane Departure Warning (LDW) | [ ] Yes / [ ] No | [1-5] | |
| Traffic Sign Recognition (TSR) | [ ] Yes / [ ] No | [1-5] | |
| Pedestrian/Cyclist Warning | [ ] Yes / [ ] No | [1-5] | |
| AEB request output | [ ] Yes / [ ] No | [1-5] | |
| ACC request output | [ ] Yes / [ ] No | [1-5] | |
| LKA request output | [ ] Yes / [ ] No | [1-5] | |
| Headway monitoring | [ ] Yes / [ ] No | [1-5] | |
| Blind-spot detection | [ ] Yes / [ ] No | [1-5] | |

### 4.2 DMS Features

| Feature | Required | Priority | Notes |
|---------|----------|----------|-------|
| Drowsiness detection | [ ] Yes / [ ] No | [1-5] | |
| Distraction detection | [ ] Yes / [ ] No | [1-5] | |
| Phone use detection | [ ] Yes / [ ] No | [1-5] | |
| Seatbelt detection | [ ] Yes / [ ] No | [1-5] | |
| Driver identification | [ ] Yes / [ ] No | [1-5] | |
| Gaze tracking | [ ] Yes / [ ] No | [1-5] | |
| Emotion detection | [ ] Yes / [ ] No | [1-5] | |

### 4.3 Regulation Compliance

| Regulation | Required | Target Date |
|-----------|----------|-------------|
| Euro NCAP (specify year) | [ ] Yes / [ ] No | [Year] |
| EU GSR2 (General Safety Regulation) | [ ] Yes / [ ] No | [July 2024 / July 2026] |
| UN R130 (LDWS) | [ ] Yes / [ ] No | |
| UN R131 (AEBS) | [ ] Yes / [ ] No | |
| FMVSS (US, specify) | [ ] Yes / [ ] No | |
| China GB/T (specify) | [ ] Yes / [ ] No | |
| Other: [specify] | [ ] Yes / [ ] No | |

---

## 5. Interface Requirements*

### 5.1 CAN Bus

| Parameter | Requirement |
|-----------|-------------|
| CAN protocol* | [ ] CAN 2.0B / [ ] CAN-FD |
| Bus speed* | [e.g., 500kbps / 1Mbps / 2Mbps FD] |
| Number of CAN channels* | [1 / 2] |
| CAN database provided | [ ] Yes (attach DBC) / [ ] No (use ADVIS default) |
| Termination required | [ ] Yes (end-node) / [ ] No (mid-bus) |
| Wake/sleep support | [ ] Yes / [ ] No |
| Partial networking | [ ] Yes / [ ] No |
| Message list attached | [ ] Yes / [ ] No |

### 5.2 Connector Preference

| Parameter | Requirement |
|-----------|-------------|
| Connector family | [e.g., TE AMPSEAL / Molex MX150 / Aptiv / OEM standard] |
| Pin count | [Minimum required] |
| Sealed/unsealed | [ ] Sealed (IP67) / [ ] Unsealed |
| Keying/color | [Preference] |
| Mating cycles | [Minimum required] |
| Wire gauge | [e.g., 0.5mm2 / 0.75mm2] |

### 5.3 Power Input

| Parameter | Requirement |
|-----------|-------------|
| Nominal voltage* | [12V / 24V / 48V] |
| Voltage range | [Min-Max V] |
| Ignition-switched or permanent | [ ] Ignition / [ ] Permanent / [ ] Both |
| Sleep current requirement | [mA maximum in sleep mode] |
| Wake source | [CAN wake / ignition / timer] |

---

## 6. Environmental Requirements*

### 6.1 Operating Conditions

| Parameter | Requirement |
|-----------|-------------|
| Operating temperature* | [Min to Max, e.g., -40 to +85C] |
| Storage temperature | [Min to Max] |
| Humidity | [e.g., 95% RH non-condensing] |
| Altitude | [e.g., up to 5000m] |
| IP rating required | [e.g., IP54 / IP67] |

### 6.2 Mounting and Vibration

| Parameter | Requirement |
|-----------|-------------|
| Mounting location* | [e.g., behind dashboard, under seat, trunk] |
| Vibration profile | [e.g., ISO 16750-3 Table X] |
| Shock requirement | [e.g., ISO 16750-3 Table Y] |
| Orientation constraints | [Any mounting orientation restrictions] |

### 6.3 EMC Requirements

| Parameter | Requirement |
|-----------|-------------|
| Emissions standard | [e.g., CISPR 25 Class 5] |
| Immunity standard | [e.g., ISO 11452-2 Level III] |
| ESD requirement | [e.g., IEC 61000-4-2 Level 4] |
| Transient protection | [e.g., ISO 7637-2 all pulses] |
| Additional EMC specs | [OEM-specific] |

---

## 7. Volume and Timeline*

| Milestone | Target Date |
|-----------|-------------|
| Requirements freeze* | [Date] |
| A-sample delivery* | [Date] |
| B-sample delivery | [Date] |
| C-sample (production intent) | [Date] |
| PPAP / SOP* | [Date] |
| Annual volume (year 1)* | [Units] |
| Annual volume (peak) | [Units] |
| Program end-of-life | [Date] |

---

## 8. Certification Requirements

| Certification | Required | Responsible Party |
|---------------|----------|-------------------|
| E-Mark (ECE R10) | [ ] Yes / [ ] No | [ADVIS / OEM / Joint] |
| ISO 26262 assessment | [ ] Yes / [ ] No | [ADVIS / OEM / Joint] |
| IATF 16949 compliance | [ ] Yes / [ ] No | [ADVIS / OEM] |
| PPAP submission | [ ] Yes / [ ] No | [Level: 1/2/3/4/5] |
| Environmental (RoHS/REACH) | [ ] Yes / [ ] No | [ADVIS] |
| Conflict minerals reporting | [ ] Yes / [ ] No | [ADVIS] |
| Cybersecurity (ISO 21434) | [ ] Yes / [ ] No | [ADVIS / OEM / Joint] |
| SOTIF (ISO 21448) | [ ] Yes / [ ] No | [ADVIS / OEM / Joint] |

---

## 9. Customization Requests

### 9.1 Hardware Customization

| Request | Description | Priority |
|---------|-------------|----------|
| [Custom 1] | [Description] | [Must/Want/Nice] |
| [Custom 2] | [Description] | [Must/Want/Nice] |

### 9.2 Software Customization

| Request | Description | Priority |
|---------|-------------|----------|
| [Custom 1] | [Description] | [Must/Want/Nice] |
| [Custom 2] | [Description] | [Must/Want/Nice] |

### 9.3 Labeling and Branding

| Parameter | Requirement |
|-----------|-------------|
| Product label | [OEM branding / ADVIS branding / white-label] |
| Regulatory labels | [Required markings] |
| Serial number format | [OEM format or ADVIS default] |

---

## 10. Commercial Terms (Summary)

| Parameter | Value |
|-----------|-------|
| Target unit price | [At volume] |
| NRE budget | [For customization] |
| Warranty period | [Months/Years] |
| Service/support level | [Standard / Premium / On-site] |
| Logistics | [Delivery terms, Incoterms] |

---

## 11. Document Attachments

| Document | Status | Filename |
|----------|--------|----------|
| CAN database (DBC file) | [ ] Attached / [ ] TBD | [filename] |
| Vehicle harness drawing | [ ] Attached / [ ] TBD | [filename] |
| Mounting space envelope | [ ] Attached / [ ] TBD | [filename] |
| OEM EMC specification | [ ] Attached / [ ] TBD | [filename] |
| Vehicle electrical architecture | [ ] Attached / [ ] TBD | [filename] |
| Feature specification | [ ] Attached / [ ] TBD | [filename] |

---

## Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| OEM Technical Contact | | | |
| OEM Program Manager | | | |
| ADVIS Systems Engineer | | | |
| ADVIS Program Manager | | | |

---

*ADVIS Hardware Platform - OEM Customization*
