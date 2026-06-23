# ADVIS Yield Tracking Methodology

| Field | Value |
|-------|-------|
| Document ID | ADVIS-MFG-YLD-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Manufacturing Quality Team |
| Date | 2024-01-15 |
| Classification | CONFIDENTIAL |

---

## 1. Scope

This document defines the yield tracking methodology for ADVIS ECU production, including metrics definitions, defect categorization, Pareto analysis procedures, yield improvement targets, and SPC chart requirements.

## 2. Yield Metrics Definitions

### 2.1 Primary Metrics

| Metric | Definition | Formula |
|--------|-----------|---------|
| First-Pass Yield (FPY) | % of units passing all tests on first attempt | (Units pass first time / Total units tested) x 100% |
| Final Yield (FY) | % of units shipped vs. units started | (Units shipped / Units started) x 100% |
| Rolled Throughput Yield (RTY) | Product of FPY at each process step | FPY_1 x FPY_2 x ... x FPY_n |
| Defects Per Million Opportunities (DPMO) | Normalized defect rate | (Defects / Opportunities) x 10^6 |
| Rework Rate | % of units requiring rework | (Units reworked / Total units) x 100% |
| Scrap Rate | % of units scrapped (non-repairable) | (Units scrapped / Total units) x 100% |

### 2.2 Process Step Yields

| Process Step | Metric | Target FPY |
|--------------|--------|------------|
| Solder paste print (SPI) | SPI pass rate | >= 99.5% |
| Component placement | Placement accuracy | >= 99.9% |
| Reflow soldering | Post-reflow AOI pass | >= 98.5% |
| X-ray inspection | X-ray pass rate | >= 99.0% |
| Selective soldering | Visual inspection pass | >= 99.5% |
| ICT (In-Circuit Test) | ICT first-pass yield | >= 98.0% |
| Functional test | Functional test FPY | >= 97.0% |
| HASS screen | HASS pass rate | >= 98.0% |
| Final QC | Final inspection pass | >= 99.5% |
| **Overall RTY** | **Product of all steps** | **>= 92.0%** |

## 3. Defect Categorization

### 3.1 Defect Category Hierarchy

```
  Defect
  |
  +-- Manufacturing Defect
  |   +-- Solder Defect
  |   |   +-- Insufficient solder
  |   |   +-- Excess solder / bridge
  |   |   +-- Cold solder joint
  |   |   +-- Tombstone
  |   |   +-- Void (BGA/QFN)
  |   |   +-- Head-in-pillow (BGA)
  |   |
  |   +-- Component Defect
  |   |   +-- Missing component
  |   |   +-- Wrong component (value)
  |   |   +-- Wrong orientation / polarity
  |   |   +-- Damaged component (cracked)
  |   |   +-- Counterfeit component
  |   |
  |   +-- PCB Defect
  |       +-- Open trace
  |       +-- Short (copper defect)
  |       +-- Delamination
  |       +-- Solder mask defect
  |       +-- Drill defect (via)
  |
  +-- Test Defect (Functional Failure)
  |   +-- Power rail out-of-spec
  |   +-- Communication failure (CAN, I2C, SPI)
  |   +-- Camera interface failure
  |   +-- Sensor failure (IMU, GNSS)
  |   +-- Timing failure (watchdog, boot)
  |   +-- Current consumption out-of-range
  |
  +-- Cosmetic Defect
      +-- Marking error
      +-- Label defect
      +-- Enclosure scratch/dent
      +-- Solder splash (non-functional)
```

### 3.2 Defect Severity Classification

| Severity | Definition | Disposition |
|----------|-----------|-------------|
| Critical | Safety-related or field failure likely | Scrap (no rework for critical) |
| Major | Functional failure, detectable by test | Rework if repairable; scrap if not |
| Minor | Cosmetic or non-functional deviation | Rework; may accept with concession |
| Informational | Observation, within spec but trending | Log for monitoring only |

### 3.3 Standard Defect Codes

| Code | Description | Category | Typical Cause |
|------|-------------|----------|---------------|
| S01 | Solder bridge | Solder | Excess paste, stencil wear |
| S02 | Insufficient solder | Solder | Low paste volume, stencil block |
| S03 | Tombstone | Solder | Unbalanced pads, reflow profile |
| S04 | Cold joint | Solder | Insufficient reflow temperature |
| S05 | BGA void (> 25%) | Solder | Outgassing, flux residue |
| S06 | Head-in-pillow | Solder | Board warpage, BGA coplanarity |
| C01 | Missing component | Component | Feeder empty, pick failure |
| C02 | Wrong value | Component | Feeder mislabeled, reel swap |
| C03 | Wrong polarity | Component | Programming error, mark ambiguity |
| C04 | Cracked component | Component | Pick force, thermal shock |
| C05 | Lifted lead | Component | Rework damage, pad adhesion |
| P01 | Open trace | PCB | Fab defect, over-etch |
| P02 | Short (copper) | PCB | Under-etch, debris |
| F01 | Power rail failure | Functional | Component defect, solder issue |
| F02 | Communication failure | Functional | Solder issue, component defect |
| F03 | No boot | Functional | SoM connection, power sequencing |

## 4. Pareto Analysis Process

### 4.1 Pareto Data Collection

| Data Source | Information Collected | Frequency |
|-------------|----------------------|-----------|
| SPI system | Paste defect type, location | Real-time (every board) |
| AOI system | Component defect type, reference designator | Real-time (every board) |
| X-ray system | Void percentage, location | Real-time (inspected boards) |
| ICT system | Failed test, measurement value | Real-time (every board) |
| Functional test | Failed step, measurement | Real-time (every board) |
| Repair station | Defect found, root cause, repair action | Per repair event |

### 4.2 Pareto Chart Requirements

Generate Pareto charts at the following intervals:

| Frequency | Scope | Audience | Action Threshold |
|-----------|-------|----------|------------------|
| Daily | Shift-level defects | Production supervisor | Top defect > 5x target |
| Weekly | Production line totals | Manufacturing engineering | Top 3 defects for 3+ days |
| Monthly | Plant-wide, by product | Quality management | Any defect type > 1% rate |
| Quarterly | Trend analysis | Executive review | Yield below target for 2+ months |

### 4.3 Pareto Action Rules

| Rule | Condition | Required Action |
|------|-----------|----------------|
| 80/20 rule | Top 20% of defect types cause 80% of failures | Focus improvement on top defects |
| Repeat offender | Same defect type #1 for 3 consecutive weeks | Root cause investigation (8D) |
| New defect | Previously unseen defect type appears | Immediate containment and investigation |
| Trend violation | Defect rate increasing for 3+ data points | Process audit and corrective action |

## 5. Yield Improvement Targets

### 5.1 Phase-Based Targets

| Phase | FPY Target (Functional) | RTY Target | Timeline |
|-------|------------------------|------------|----------|
| Prototype (A-sample) | >= 80% | >= 70% | Initial build |
| Pre-production (B-sample) | >= 90% | >= 85% | +3 months |
| Production ramp (C-sample) | >= 95% | >= 90% | +6 months |
| Steady-state production | >= 97% | >= 92% | +12 months |
| Mature production | >= 98.5% | >= 95% | +24 months |

### 5.2 Continuous Improvement Goals

| Metric | Current Baseline | 6-Month Target | 12-Month Target |
|--------|-----------------|----------------|-----------------|
| FPY (overall) | [Measure] | +2% absolute | +4% absolute |
| DPMO | [Measure] | -30% | -50% |
| Rework rate | [Measure] | -25% | -50% |
| Scrap rate | [Measure] | -20% | -40% |
| Test time | [Measure] | -10% | -20% |

### 5.3 Improvement Project Prioritization

| Priority | Criteria |
|----------|----------|
| 1 (Immediate) | Yield < target by > 5%, customer impact |
| 2 (High) | Top Pareto defect, clear root cause identified |
| 3 (Medium) | Yield improvement opportunity, ROI > 3:1 |
| 4 (Low) | Minor improvement, low ROI, nice-to-have |

## 6. SPC (Statistical Process Control) Requirements

### 6.1 SPC Chart Types

| Application | Chart Type | Subgroup Size | Control Limits |
|-------------|-----------|---------------|----------------|
| Continuous measurement (voltage, current) | X-bar/R or X-bar/S | 5 units | +/- 3 sigma |
| Individual measurements (cycle time) | I-MR (Individuals/Moving Range) | 1 | +/- 3 sigma |
| Attribute data (pass/fail) | P-chart or NP-chart | >= 50 units | +/- 3 sigma |
| Defect count per unit | C-chart or U-chart | Variable | +/- 3 sigma |
| Yield per shift | P-chart | Shift production | +/- 3 sigma |

### 6.2 SPC Parameters to Monitor

| Parameter | Chart Type | Sampling | UCL/LCL Source |
|-----------|-----------|----------|----------------|
| Solder paste volume (SPI) | X-bar/R | Every board, critical pads | Statistical (25 subgroups) |
| Reflow peak temperature | I-MR | Every profile run | Statistical |
| 5V rail voltage (functional test) | X-bar/R | Every 5 units | Statistical |
| 3.3V rail voltage | X-bar/R | Every 5 units | Statistical |
| 1.8V rail voltage | X-bar/R | Every 5 units | Statistical |
| ICT FPY (per shift) | P-chart | All units per shift | Statistical |
| Functional test FPY (per shift) | P-chart | All units per shift | Statistical |
| Current consumption (idle) | X-bar/R | Every 5 units | Statistical |
| BGA void percentage (X-ray) | I-MR | Every inspected unit | Statistical |

### 6.3 SPC Rules for Out-of-Control

| Rule | Pattern | Action |
|------|---------|--------|
| Rule 1 | One point beyond 3-sigma | Stop, investigate, correct |
| Rule 2 | 9 consecutive points on one side of center | Process shift investigation |
| Rule 3 | 6 consecutive points increasing or decreasing | Trend investigation |
| Rule 4 | 14 consecutive points alternating up/down | Investigate mixing/over-adjustment |
| Rule 5 | 2 of 3 points beyond 2-sigma (same side) | Warning, increase monitoring |
| Rule 6 | 4 of 5 points beyond 1-sigma (same side) | Warning, process review |

### 6.4 SPC Response Procedure

```
  Out-of-Control Signal Detected
           |
           v
  +------------------+
  | Stop production  |
  | (if Rule 1)      |
  +--------+---------+
           |
           v
  +------------------+
  | Identify root    |
  | cause            |
  +--------+---------+
           |
           v
  +------------------+     No      +------------------+
  | Assignable cause | ----------> | Recalculate      |
  | found?           |             | control limits   |
  +--------+---------+             +------------------+
           | Yes
           v
  +------------------+
  | Implement        |
  | corrective action|
  +--------+---------+
           |
           v
  +------------------+
  | Verify process   |
  | returns to       |
  | control          |
  +------------------+
```

## 7. Reporting

### 7.1 Standard Reports

| Report | Frequency | Audience | Content |
|--------|-----------|----------|---------|
| Daily yield report | Daily | Production, Quality | FPY by test step, top 5 defects |
| Weekly Pareto | Weekly | Engineering, Management | Defect Pareto, trend charts |
| Monthly quality review | Monthly | All stakeholders | Yield trend, improvement projects, SPC |
| Quarterly business review | Quarterly | Executive | Cost of quality, yield vs. target, forecast |

### 7.2 Yield Dashboard (Real-Time)

| Display | Data Source | Update Rate |
|---------|-------------|-------------|
| Current shift FPY | Test system | Real-time |
| Cumulative daily yield | MES | Every 15 minutes |
| Top defect (current) | AOI + Test | Real-time |
| SPC charts (active) | Test system | Per measurement |
| Units produced vs. plan | MES | Hourly |

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2024-01-15 | Manufacturing Quality Team | Initial draft |
