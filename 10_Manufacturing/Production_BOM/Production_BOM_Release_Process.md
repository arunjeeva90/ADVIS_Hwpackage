# ADVIS Production BOM Release Process

| Field | Value |
|-------|-------|
| Document ID | ADVIS-MFG-BOM-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Configuration Management Team |
| Date | 2024-01-15 |
| Classification | CONFIDENTIAL |

---

## 1. Scope

This document defines the process for transitioning the ADVIS engineering BOM (eBOM) to a production BOM (mBOM), managing BOM changes through the Engineering Change Order (ECO) process, and handling alternate parts, cost reductions, and component obsolescence.

## 2. BOM Lifecycle

```
  +----------+     +----------+     +----------+     +----------+
  | Concept  | --> | Engineer | --> | Production| --> | Sustaining|
  | BOM      |     | BOM      |     | BOM       |     | BOM       |
  | (cBOM)   |     | (eBOM)   |     | (mBOM)    |     | (updates) |
  +----------+     +----------+     +----------+     +----------+
       |                |                |                |
  Schematic        DVT build       PPAP approved     Field changes
  concept          validated       released to        ECOs
                                   production
```

## 3. Engineering BOM to Production BOM Transition

### 3.1 Transition Checklist

| Item | Requirement | Verified By |
|------|-------------|-------------|
| All components have approved manufacturer part numbers | No "TBD" or placeholder parts | Component Engineer |
| Second sources identified for critical components | At least 1 alternate per critical part | Component Engineer |
| AEC-Q100/Q200 qualification verified | All ICs and critical passives | Quality Engineer |
| RoHS/REACH compliance confirmed | All components declared compliant | Environmental Engineer |
| Component availability confirmed | Lead time < 16 weeks (or strategic stock) | Procurement |
| End-of-life (EOL) risk assessment | No components with < 5-year projected availability | Component Engineer |
| Packaging specifications defined | Tape & reel, tray, tube as applicable | Manufacturing Engineer |
| Approved vendor list (AVL) complete | Manufacturer + distributor identified | Procurement |
| Mechanical dimensions verified | Footprint matches physical component | Layout Engineer |
| Thermal ratings verified | All components derated per policy | Hardware Engineer |

### 3.2 BOM Data Requirements (Production)

| Field | Description | Example |
|-------|-------------|---------|
| Item # | Line item number (sequential) | 1, 2, 3... |
| Reference designator(s) | Schematic reference | R1, R2, R3 |
| Quantity | Count per board | 3 |
| Manufacturer | Component vendor | Texas Instruments |
| Manufacturer Part Number (MPN) | Exact orderable PN | LM61460AQRGTRQ1 |
| Description | Component description | Buck converter, 6A, 3.8-36V |
| Package | Physical package type | HTSSOP-20-EP |
| Value / Rating | Electrical value | 6A, 36V max |
| Tolerance | Component tolerance | +/- 1% |
| Voltage rating | Maximum voltage (capacitors) | 16V |
| Temperature range | Operating range | -40C to +125C |
| AEC-Q qualification | Qualification grade | AEC-Q100 Grade 1 |
| MSL level | Moisture sensitivity | MSL-3 |
| Alternate 1 MPN | First alternate source | [Alternate PN] |
| Alternate 1 Manufacturer | Alternate vendor | [Vendor] |
| DNP (Do Not Place) flag | If applicable | No |
| Notes | Special instructions | Critical component, no substitute without qual |

## 4. Engineering Change Order (ECO) Process

### 4.1 ECO Workflow

```
  [Change Request] --> [Impact Analysis] --> [Review Board] --> [Approval]
         |                    |                    |                |
         v                    v                    v                v
  Originator fills    Assess: cost,        CCB reviews:      Implement
  ECO form with       schedule, quality,   approve/reject/   change in
  justification       test requirements    modify            production
```

### 4.2 ECO Classification

| Class | Description | Approval Required | Example |
|-------|-------------|-------------------|---------|
| Class I | Form/fit/function change | Full CCB + customer | Component change affecting performance |
| Class II | No form/fit/function impact | Engineering + Quality | Alternate source (same spec) |
| Class III | Documentation only | Engineering | Drawing correction, note update |

### 4.3 ECO Required Information

| Field | Description |
|-------|-------------|
| ECO Number | Unique identifier (ADVIS-ECO-XXXX) |
| Originator | Person requesting change |
| Date | Submission date |
| Affected documents | BOM, schematic, PCB layout, test procedures |
| Affected part numbers | Components being changed |
| Reason for change | Technical justification |
| Change description | Detailed before/after |
| Impact assessment | Cost, schedule, qualification, inventory |
| Validation required | Test/qualification activities needed |
| Implementation point | Immediate, next build, inventory depletion |
| Disposition of existing stock | Use as-is, rework, scrap |
| Customer notification required | Yes/No (per contract) |

### 4.4 Change Control Board (CCB) Members

| Role | Responsibility |
|------|---------------|
| Hardware Engineering Lead | Technical approval |
| Quality Manager | Quality impact assessment |
| Manufacturing Engineering | Process impact, fixture changes |
| Procurement Manager | Supply chain, cost impact |
| Program Manager | Schedule, customer notification |
| Test Engineering | Test coverage, fixture update |
| Configuration Manager | Document control, BOM update |

## 5. Alternate Part Qualification

### 5.1 Alternate Qualification Levels

| Level | Scope | Required Testing | Application |
|-------|-------|------------------|-------------|
| Full qualification | Complete DVT retest | All applicable DVT tests | Different technology/design |
| Partial qualification | Targeted testing | Tests related to changed parameter | Same spec, different fab process |
| Similarity analysis | Engineering analysis only | Document review + limited bench | Same manufacturer, same die, different package option |

### 5.2 Alternate Qualification Checklist

| Criterion | Original Part | Proposed Alternate | Delta |
|-----------|---------------|-------------------|-------|
| Electrical specifications | [list key specs] | [verify match] | [difference] |
| Package/footprint | [original pkg] | [must match] | [none allowed] |
| Temperature range | [original range] | [must meet or exceed] | [margin] |
| AEC-Q qualification | [original grade] | [must match] | [none allowed] |
| Moisture sensitivity (MSL) | [original MSL] | [must match or better] | [acceptable] |
| RoHS/REACH compliance | Compliant | [must be compliant] | [none] |
| Lead time | [original LT] | [document] | [acceptable?] |
| Unit cost | [original cost] | [document] | [saving or premium] |

### 5.3 Critical Components (No Substitution Without Full Qualification)

| Component | Reason | Alternate Strategy |
|-----------|--------|-------------------|
| DS90UB954-Q1 | Single-source, algorithm-dependent | No direct alternate; design dual-source architecture |
| TDA4VM SoM | Platform-defining | SoM vendor manages silicon alternates |
| BMI088 | Calibration-specific | Qualify alternate IMU family in advance |
| NEO-M9N | Firmware-dependent GNSS protocol | Qualify alternate GNSS in advance |
| TCAN1044AV-Q1 | CAN-FD timing critical | Same-family alternates (TCAN1044V-Q1) |

## 6. Cost Reduction Process

### 6.1 Cost Reduction Categories

| Category | Description | Risk Level | Approval |
|----------|-------------|------------|----------|
| Commercial | Same part, better pricing (volume, negotiation) | Low | Procurement |
| Source change | Same spec, different manufacturer | Medium | Engineering + Quality |
| Design optimization | Different value/spec that meets function | High | Full ECO + retest |
| Value engineering | Remove unnecessary components or features | High | Full ECO + retest |

### 6.2 Cost Reduction Validation Matrix

| Category | Bench Test | DVT Retest | EMC Retest | Environmental | Customer Notification |
|----------|-----------|-----------|-----------|---------------|----------------------|
| Commercial | No | No | No | No | No |
| Source change | Yes (targeted) | Partial | If EMC-related | If reliability-related | Per contract |
| Design optimization | Yes | Yes (affected tests) | If emissions-related | If stressed differently | Yes |
| Value engineering | Yes | Full | Full | Full | Yes |

## 7. Obsolescence Management

### 7.1 Obsolescence Monitoring

| Activity | Frequency | Tool/Source |
|----------|-----------|-------------|
| EOL/PDN monitoring | Continuous | IHS/SiliconExpert, distributor alerts |
| Lifecycle assessment | Quarterly | Component database review |
| Last-time-buy evaluation | Upon PDN receipt | Procurement + Engineering |
| Redesign trigger | When LTB < 3-year supply | Engineering |

### 7.2 Obsolescence Response Plan

| Trigger | Response Time | Action |
|---------|--------------|--------|
| Product Discontinuance Notice (PDN) | Within 2 weeks | Assess impact, calculate LTB quantity |
| Lifecycle status: "Not recommended" | Within 4 weeks | Begin alternate qualification |
| Single-source with < 5 year horizon | Proactive | Identify and pre-qualify alternate |
| LTB deadline approaching | Immediately | Execute LTB order |

### 7.3 Last-Time-Buy Quantity Calculation

```
LTB Quantity = (Annual usage x Remaining program years x Safety factor)
             - Current inventory
             - On-order quantity

Safety factor = 1.2 (for yield loss, qualification, field spares)
```

## 8. BOM Revision Control

### 8.1 Revision Numbering

| Level | Format | Example | Trigger |
|-------|--------|---------|---------|
| Major revision | Letter (A, B, C...) | Rev B | Form/fit/function change |
| Minor revision | Number (.1, .2, .3...) | Rev B.1 | Alternate source, editorial |
| Draft | Numeric (01, 02...) | Draft 03 | Pre-release iterations |

### 8.2 BOM Configuration Record

| Revision | Date | ECO # | Description | Approved By |
|----------|------|-------|-------------|-------------|
| Draft 01 | [date] | - | Initial concept BOM | Engineering |
| Rev A | [date] | ECO-0001 | First eBOM release (A-sample) | CCB |
| Rev B | [date] | ECO-0002 | DVT corrections, alternate sources | CCB |
| Rev C | [date] | ECO-0003 | Production release (mBOM) | CCB + Customer |

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2024-01-15 | Configuration Management Team | Initial draft |
