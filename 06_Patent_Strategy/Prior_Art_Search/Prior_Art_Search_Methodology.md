# Prior Art Search Methodology

## Purpose

This document defines the systematic approach for conducting prior art searches across all ADVIS invention disclosures. A thorough prior art search is essential to assess patentability, identify blocking patents, and inform claim drafting strategy.

---

## Search Databases

| Database | Coverage | Access | Priority |
|----------|----------|--------|----------|
| USPTO Full-Text | US patents and published applications | patents.uspto.gov | Primary |
| EPO Espacenet | Worldwide patent documents (100+ countries) | worldwide.espacenet.com | Primary |
| WIPO PATENTSCOPE | PCT international applications | patentscope.wipo.int | Primary |
| Google Patents | Aggregated global patent data + scholar | patents.google.com | Secondary |
| IEEE Xplore | Technical publications, conference papers | ieeexplore.ieee.org | Secondary |
| SAE MOBILUS | Automotive-specific technical papers | saemobilus.sae.org | Secondary |
| Derwent Innovation | Enhanced patent analytics, family mapping | clarivate.com | If available |
| Semantic Scholar | AI/ML research papers | semanticscholar.org | For algorithm claims |

---

## Search Terms by Disclosure

### ID-001: SoC-Adaptive Dual-Vision Smart Camera Platform

| Category | Search Terms |
|----------|-------------|
| Primary | "adaptive platform" AND "system on module" AND automotive |
| Primary | "SoC variant" AND "carrier board" AND "power sequencing" |
| Primary | "module identity" AND "power profile" AND vehicle |
| Secondary | "interchangeable processing module" AND camera |
| Secondary | "hardware autonomous" AND "boot configuration" |
| CPC Classes | H05K 1/18 (modular circuits), B60R 11/04 (vehicle electronics) |

### ID-002: Compact Dual-Facing Windshield Module + Thermal/EMC Stack

| Category | Search Terms |
|----------|-------------|
| Primary | "windshield mount" AND camera AND "thermal management" |
| Primary | "dual camera" AND "opposing direction" AND vehicle |
| Primary | "EMC" AND "thermal" AND "integrated stack" AND camera |
| Secondary | "compact camera module" AND automotive AND "heat dissipation" |
| Secondary | "windshield" AND "driver monitoring" AND "ADAS" AND single |
| CPC Classes | B60R 1/00 (mirrors/cameras), H05K 7/20 (thermal management) |

### ID-003: Risk-Coupled ADAS+DMS Decision Fusion

| Category | Search Terms |
|----------|-------------|
| Primary | "driver attention" AND "collision risk" AND "coupled" |
| Primary | "DMS" AND "ADAS" AND "fusion" AND "risk assessment" |
| Primary | "driver monitoring" AND "intervention threshold" AND adaptive |
| Secondary | "gaze" AND "forward collision" AND "modulate" |
| Secondary | "driver state" AND "warning threshold" AND vehicle |
| CPC Classes | B60W 40/08 (driver condition), B60W 30/09 (collision avoidance) |

### ID-004: Dual-Camera Mutual Self-Calibration

| Category | Search Terms |
|----------|-------------|
| Primary | "dual camera" AND "mutual calibration" AND vehicle |
| Primary | "self-calibration" AND "reference feature" AND "vehicle geometry" |
| Primary | "opposing camera" AND "cross-validation" AND calibration |
| Secondary | "online calibration" AND camera AND automotive AND "without target" |
| Secondary | "windshield" AND camera AND "drift correction" |
| CPC Classes | G06T 7/80 (camera calibration), B60R 11/04 (vehicle electronics) |

### ID-005: Risk-Aware Power, Sensor and IR Mode Control

| Category | Search Terms |
|----------|-------------|
| Primary | "power management" AND camera AND "driving context" AND vehicle |
| Primary | "adaptive power mode" AND "risk level" AND automotive |
| Primary | "sensor mode" AND "frame rate" AND "driving condition" |
| Secondary | "IR illumination" AND "adaptive" AND "driver monitoring" |
| Secondary | "predictive power" AND "navigation" AND "pre-staging" |
| CPC Classes | H04N 23/00 (cameras), B60W 50/00 (vehicle control systems) |

---

## Competitor Patent Portfolios to Review

### Mobileye (Intel)

- EyeQ processor architecture patents
- Forward collision warning methods
- Lane departure detection algorithms
- Road model construction from single camera
- **Focus**: Any patents covering adaptive processing based on driving context

### Continental

- Camera-based ADAS system patents (MFC series)
- Multi-function camera architectures
- Sensor fusion methods
- **Focus**: Compact camera thermal management

### Bosch

- MPC camera module patents
- Video-based object detection
- Camera calibration methods (particularly service calibration)
- **Focus**: Sensor power management, calibration procedures

### Seeing Machines

- Driver monitoring gaze detection
- Drowsiness and distraction classification
- IR illumination for DMS
- **Focus**: Any patents coupling DMS with ADAS functions

### Smart Eye

- Eye tracking technology
- Head pose estimation
- Driver attention measurement
- **Focus**: Attention metric computation and application

### Denso

- Vision system integration
- Thermal management for vehicle electronics
- Compact camera modules
- **Focus**: Windshield-mount thermal solutions

### Valeo

- Parking camera systems
- Multi-camera calibration
- Camera power management
- **Focus**: Camera self-calibration without targets

---

## Search Process

### Phase 1: Preliminary Search (2 weeks per disclosure)

1. Execute primary search terms across USPTO, EPO, WIPO
2. Review top 50 results per term combination
3. Identify potentially blocking references
4. Classify: blocking / relevant / background / no concern
5. Document findings in Prior Art Report

### Phase 2: Deep Search (2 weeks per disclosure)

1. Review patent citations of blocking references (forward + backward)
2. Search patent family members for additional claims
3. Review non-patent literature (IEEE, SAE papers)
4. Analyze competitor portfolios for relevant filings
5. Identify design-around opportunities

### Phase 3: Attorney Review (1 week per disclosure)

1. Present findings to patent attorney
2. Discuss claim scope implications
3. Identify need for additional searching
4. Refine claims based on prior art landscape
5. Document final search opinion

---

## Search Documentation Requirements

Each search must be documented with:

- Date range of search
- Databases searched
- Exact search queries used
- Number of results reviewed
- Key references identified (with relevance assessment)
- Searcher name and qualifications
- Conclusions and recommendations

---

## Quality Criteria

A search is considered complete when:

- [ ] All primary search terms executed across all primary databases
- [ ] Top 100 results per disclosure reviewed
- [ ] Competitor portfolios analyzed for relevant filings
- [ ] Non-patent literature surveyed
- [ ] Forward/backward citation trees explored for blocking references
- [ ] Report reviewed by patent attorney
- [ ] No known gaps in search coverage documented

---

**Document Version:** 1.0  
**Last Updated:** 2025-01  
**Classification:** CONFIDENTIAL - Internal Use Only
