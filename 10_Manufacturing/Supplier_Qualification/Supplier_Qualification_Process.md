# ADVIS Supplier Qualification Process

| Field | Value |
|-------|-------|
| Document ID | ADVIS-MFG-SQ-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Supplier Quality Team |
| Date | 2024-01-15 |
| Classification | CONFIDENTIAL |

---

## 1. Scope

This document defines the supplier qualification framework for the ADVIS ECU program, covering PPAP (Production Part Approval Process) requirements, capability assessment, audit procedures, scoring criteria, approved supplier list (ASL) management, and second-source strategy for critical components.

## 2. Supplier Categories

| Category | Description | Examples | Qualification Level |
|----------|-------------|----------|---------------------|
| A - Critical | Single-source, high-impact, safety-related path | DS90UB954, SoM, BMI088 | Full PPAP + on-site audit |
| B - Important | Multiple sources available, moderate impact | MLCC, resistors, inductors | Reduced PPAP + documentation |
| C - Standard | Commodity, readily available, low impact | Standard passives, hardware | Self-declaration + sample test |

## 3. PPAP Requirements

### 3.1 PPAP Submission Levels

| Level | Description | Application |
|-------|-------------|-------------|
| Level 1 | Warrant only | Category C suppliers (standard) |
| Level 2 | Warrant + samples + limited data | Category B suppliers |
| Level 3 | Warrant + samples + complete data | Category A suppliers (default) |
| Level 4 | Warrant + complete data (per customer) | OEM customer requirement |
| Level 5 | Warrant + complete data + on-site review | New suppliers, critical changes |

### 3.2 PPAP Elements Required (Level 3)

| # | Element | Category A | Category B | Category C |
|---|---------|-----------|-----------|-----------|
| 1 | Design records (drawings, specs) | Required | Required | N/A |
| 2 | Engineering change documents | Required | Required | N/A |
| 3 | Customer engineering approval | If required | If required | N/A |
| 4 | Design FMEA | Required | Recommended | N/A |
| 5 | Process flow diagram | Required | Required | N/A |
| 6 | Process FMEA | Required | Recommended | N/A |
| 7 | Control plan | Required | Required | N/A |
| 8 | Measurement system analysis (MSA) | Required | Recommended | N/A |
| 9 | Dimensional results | Required | Required | Sample only |
| 10 | Material/performance test results | Required | Required | Certificate |
| 11 | Initial process studies (Cpk) | Required | Recommended | N/A |
| 12 | Qualified laboratory documentation | Required | Required | N/A |
| 13 | Appearance approval report | If applicable | If applicable | N/A |
| 14 | Sample production parts | Required | Required | Required |
| 15 | Master sample | Required | Optional | N/A |
| 16 | Checking aids | If applicable | N/A | N/A |
| 17 | Customer-specific requirements | Per OEM | Per OEM | Per OEM |
| 18 | Part submission warrant (PSW) | Required | Required | Required |

### 3.3 Process Capability Requirements

| Parameter | Requirement |
|-----------|-------------|
| Initial Cpk (PPAP submission) | >= 1.67 |
| Ongoing Cpk (production) | >= 1.33 |
| Sample size for initial study | >= 30 pieces (consecutive) |
| Measurement system (Gage R&R) | <= 10% of tolerance |

## 4. Supplier Capability Assessment

### 4.1 Assessment Areas

| Area | Weight | Scoring Method |
|------|--------|---------------|
| Quality system (ISO 9001 / IATF 16949) | 25% | Certificate + audit score |
| Technical capability | 25% | Process review + sample quality |
| Delivery performance | 20% | On-time delivery history |
| Financial stability | 15% | D&B report, annual revenue |
| Capacity and scalability | 15% | Capacity utilization, growth plan |

### 4.2 Quality System Requirements

| Requirement | Category A | Category B | Category C |
|-------------|-----------|-----------|-----------|
| IATF 16949 certification | Required | Preferred | Not required |
| ISO 9001 certification | Required (minimum) | Required | Preferred |
| Internal audit program | Required | Required | Recommended |
| APQP capability | Required | Recommended | Not required |
| 8D corrective action process | Required | Required | Required |
| Statistical process control (SPC) | Required | Recommended | Not required |
| Traceability system | Required | Required | Lot-level minimum |

### 4.3 Technical Capability Evaluation

| Criterion | Assessment Method | Minimum Score |
|-----------|-------------------|---------------|
| Process technology | On-site review / capability presentation | Meet spec requirements |
| Equipment calibration | Calibration records review | 100% current |
| Testing capability | In-process and final test review | Adequate for specification |
| Failure analysis capability | FA lab or contracted service | Available within 48 hours |
| Continuous improvement | Evidence of PDCA, kaizen | Active program |
| ESD controls | Audit of ESD-protected areas | ANSI/ESD S20.20 |
| Moisture control (MSL) | Dry storage, bake-out capability | Per J-STD-033 |

## 5. Supplier Audit Process

### 5.1 Audit Types

| Type | Trigger | Scope | Frequency |
|------|---------|-------|-----------|
| Initial qualification | New supplier | Full system + process | One-time |
| Surveillance | Ongoing monitoring | Selected processes | Annual (Cat A), biennial (Cat B) |
| Product-specific | New product introduction | Product-specific process | Per NPI |
| Corrective action | Quality escape | Root cause area | As needed |
| Re-qualification | Major change at supplier | Affected processes | As needed |

### 5.2 Audit Checklist (Key Areas)

| Section | Items Reviewed |
|---------|---------------|
| Management | Quality policy, objectives, management review |
| Documents | Document control, record retention |
| Resources | Training, competency, equipment |
| Purchasing | Sub-supplier control, incoming inspection |
| Production | Process control, work instructions, monitoring |
| Inspection | In-process, final, measurement equipment |
| Nonconforming product | Identification, segregation, disposition |
| Corrective action | Root cause analysis, effectiveness verification |
| Continual improvement | Metrics, targets, improvement projects |
| Customer-specific | Automotive requirements (if IATF) |

### 5.3 Audit Scoring

| Score Range | Rating | Action |
|-------------|--------|--------|
| 90-100% | Approved (Green) | Full approval, normal business |
| 75-89% | Conditional (Yellow) | Approved with corrective action plan (60-day deadline) |
| 60-74% | Probation (Orange) | Limited approval, re-audit within 90 days |
| < 60% | Rejected (Red) | Not approved, new business held |

## 6. Approved Supplier List (ASL) Management

### 6.1 ASL Structure

| Field | Description |
|-------|-------------|
| Supplier ID | Unique identifier |
| Supplier name | Legal entity name |
| Category | A, B, or C |
| Commodity | Component type (IC, passive, connector, PCB, assembly) |
| Qualification status | Approved / Conditional / Probation / Removed |
| Qualification date | Date of last approval |
| Next audit due | Scheduled surveillance date |
| Scorecard rating | Current performance score |
| Contact | Primary quality contact |
| Location | Manufacturing site(s) |
| IATF / ISO cert # | Certificate number and expiry |

### 6.2 ASL Maintenance

| Activity | Trigger | Responsible |
|----------|---------|-------------|
| Add new supplier | Qualification complete | Supplier Quality Manager |
| Update status | Audit result, scorecard change | Supplier Quality Manager |
| Remove supplier | Consistent underperformance, closure | CCB approval |
| Annual review | Calendar | Procurement + Quality |

### 6.3 Supplier Performance Scorecard

| Metric | Weight | Measurement | Target |
|--------|--------|-------------|--------|
| Quality (PPM) | 30% | Defective parts per million | < 50 PPM |
| On-time delivery | 25% | % shipments within +/- 2 days | >= 95% |
| Corrective action response | 15% | 8D submitted within deadline | 100% on-time |
| Cost competitiveness | 15% | Price vs. market benchmark | Within 5% of benchmark |
| Technical support | 15% | Responsiveness to engineering queries | < 48-hour response |

## 7. Second-Source Strategy

### 7.1 Second-Source Requirements

| Component Risk | Second Source Required? | Strategy |
|----------------|----------------------|----------|
| Single-source, long lead time | Yes (mandatory) | Qualify alternate or bridge stock |
| Dual-source available | Yes (preferred) | Qualify at least 2 sources |
| Commodity (>= 3 sources) | Recommended | AVL with 2+ approved sources |
| Custom / proprietary | Risk mitigation required | Strategic inventory or redesign option |

### 7.2 ADVIS Critical Component Second-Source Plan

| Component | Primary Source | Second Source | Strategy |
|-----------|---------------|--------------|----------|
| DS90UB954-Q1 | Texas Instruments | None available | Strategic inventory (12-month buffer) |
| TDA4VM SoM | Phytec | [Alternate SoM vendor] | Qualify alternate SoM with same interface |
| BMI088 | Bosch Sensortec | TDK InvenSense ICM-42688 | Pre-qualify alternate IMU |
| NEO-M9N | u-blox | Quectel LC29H | Pre-qualify alternate GNSS |
| LM61460-Q1 | Texas Instruments | MPS MPQ4430-AEC1 | Qualify pin-compatible alternate |
| TPS62130A-Q1 | Texas Instruments | MPS MP2315-AEC1 | Qualify alternate buck (re-layout may be needed) |
| TCAN1044AV-Q1 | Texas Instruments | NXP TJA1443 | Qualify alternate CAN-FD transceiver |
| TPS3431-Q1 | Texas Instruments | Maxim MAX6381 | Qualify alternate watchdog |

### 7.3 Second-Source Qualification Criteria

A second source is considered qualified when:
1. Component meets all ADVIS electrical/mechanical specifications
2. PPAP Level 3 (or appropriate level) approved
3. Functional test pass (on ADVIS board, minimum 3 units)
4. EMC pre-compliance pass (if emissions-sensitive component)
5. Temperature cycling test pass (100 cycles minimum)
6. Approved by CCB and added to production BOM as alternate

## 8. Supplier Non-Conformance Management

### 8.1 Supplier Corrective Action Request (SCAR) Process

| Step | Activity | Timeline |
|------|----------|----------|
| 1 | Issue SCAR with defect description and evidence | Day 0 |
| 2 | Supplier acknowledges receipt | Day 1-2 |
| 3 | Containment action implemented | Day 3-5 |
| 4 | Root cause analysis (5-Why, fishbone) | Day 10-15 |
| 5 | Corrective action defined and implemented | Day 20-30 |
| 6 | Effectiveness verification (3 lots minimum) | Day 45-60 |
| 7 | SCAR closure | Day 60 |

### 8.2 Escalation Matrix

| Level | Trigger | Action | Approver |
|-------|---------|--------|----------|
| 1 | First quality escape | SCAR issued | Supplier Quality Engineer |
| 2 | Repeat issue (same failure mode) | Supplier on watch list | Supplier Quality Manager |
| 3 | 3+ escapes in 12 months | Supplier on probation, re-audit | Quality Director |
| 4 | Systemic failure, no improvement | Supplier removal from ASL | VP Operations |

## 9. Record Retention

| Document | Retention Period |
|----------|-----------------|
| PPAP packages | Product lifetime + 5 years |
| Audit reports | 10 years |
| SCARs | 10 years |
| Scorecards | 5 years |
| Qualification test data | Product lifetime + 5 years |
| Certificates (IATF/ISO) | Until expiry + 3 years |

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2024-01-15 | Supplier Quality Team | Initial draft |
