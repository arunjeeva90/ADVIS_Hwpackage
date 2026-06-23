# ADVIS Trade Secret Register

## Purpose

This document catalogs all technical information protected as trade secrets for the ADVIS (Adaptive Driver & Vehicle Intelligence System) platform. These items must NEVER appear in:
- Patent applications (which become public)
- Marketing materials
- Conference presentations
- Public GitHub repositories
- Customer-facing documentation (unless under NDA)
- Academic publications

**Legal basis**: Trade secrets are protected under the Defend Trade Secrets Act (DTSA, US) and equivalent laws in other jurisdictions, provided reasonable measures are taken to maintain secrecy.

---

## Active Trade Secrets

### Critical (Highest Protection Level)

| ID | Description | Category | Access Control |
|----|-------------|----------|----------------|
| TS-001 | Carrier-to-SoM connector pinout specification | Hardware | Named engineers only; encrypted storage |
| TS-002 | High-speed signal routing topology and PCB layer assignment rules | Hardware | HW team lead + layout contractor under NDA |
| TS-003 | Indian road scene dataset (collection, labeling, augmentation methods) | Software/ML | ML team only; air-gapped storage |
| TS-004 | Model tuning parameters and neural network weights | Software/ML | ML team only; version-controlled with access audit |
| TS-005 | Calibration threshold values (ADAS + DMS production parameters) | System | System engineering team; per-OEM variants under separate NDA |

### High Protection Level

| ID | Description | Category | Access Control |
|----|-------------|----------|----------------|
| TS-006 | EMI mitigation recipes (filter values, trace geometry, shielding placement) | Hardware | EMC engineer + HW team lead |
| TS-007 | Power sequencing timing parameters per SoC variant | Hardware | HW + FW teams |
| TS-008 | Risk coupling exponent (alpha) and gain parameters for decision fusion | Algorithm | System architect + ML team lead |
| TS-009 | Platform configuration database structure and variant generation algorithm | System | FW team + system architect |
| TS-010 | Thermal interface material selection and application specification | Hardware | Thermal engineer + manufacturing |
| TS-011 | Mutual calibration confidence thresholds and correction limits | Algorithm | Vision team + system architect |
| TS-012 | IR LED drive current profiles and duty cycle patterns | Hardware | Optics engineer + HW team |

### Medium Protection Level

| ID | Description | Category | Access Control |
|----|-------------|----------|----------------|
| TS-013 | Power mode transition timing and pre-staging parameters | System | Engineering team |
| TS-014 | Manufacturing test sequences and pass/fail criteria | Manufacturing | Test engineering + CM under NDA |
| TS-015 | BOM cost structure and vendor pricing | Commercial | Procurement + finance |
| TS-016 | OEM-specific customization parameters | Commercial | Per-OEM NDA; program managers |
| TS-017 | Variant generation algorithm and BOM derivation rules | System | Engineering + operations |
| TS-018 | Sensor characterization data (camera response curves, noise profiles) | Hardware | Vision team + HW team |
| TS-019 | Thermal simulation models and boundary conditions | Hardware | Thermal engineer + system architect |
| TS-020 | SoM detection circuit implementation details | Hardware | HW team |

---

## Trade Secret Categories

### Hardware Trade Secrets

Protect physical design details that are not visible from external inspection of the product and are not filed in patent applications:
- PCB stackup details, trace geometry, via structure
- Component selection rationale and specific part numbers beyond public BOM
- Thermal management material specifications
- EMC compliance solutions and filter circuits
- Connector pinout and mating specifications

### Algorithm/Software Trade Secrets

Protect the specific implementation details of patented methods:
- Neural network architectures, layer configurations, activation functions
- Training procedures, hyperparameters, augmentation strategies
- Threshold values that determine system behavior
- Calibration algorithms and convergence parameters
- Power mode state machine implementation details

### Dataset Trade Secrets

Protect the training and validation data that gives ADVIS competitive advantage:
- Indian road scene dataset (collection methodology, labeling guidelines, scene diversity)
- DMS training dataset (subject diversity, lighting conditions, pose coverage)
- Edge case collections (rare scenarios, failure modes)
- Synthetic data generation parameters

### Commercial Trade Secrets

Protect business-sensitive information:
- OEM pricing and discount structures
- Vendor agreements and component costs
- Product roadmap and feature prioritization
- Market analysis and competitive intelligence findings

---

## Protection Measures

### Technical Controls

| Control | Implementation | Scope |
|---------|---------------|-------|
| Repository access | Role-based access control (RBAC) | All code and design files |
| Encryption at rest | AES-256 for Critical and High TS | TS-001 through TS-012 |
| Encryption in transit | TLS 1.3 minimum | All transfers |
| Air-gapped storage | Physically isolated system | TS-003 (Indian road dataset) |
| Access logging | Immutable audit log of all accesses | All TS documents |
| DLP (Data Loss Prevention) | Automated scanning for TS keywords in outbound comm | Email, file sharing |
| Code review gates | No merge without reviewer confirming no TS exposure | Public-facing repos |
| Watermarking | Digital watermarks on shared documents | Documents shared under NDA |

### Administrative Controls

| Control | Frequency | Responsible |
|---------|-----------|-------------|
| IP assignment agreement signing | At hire | HR + Legal |
| Trade secret acknowledgment | At hire + annually | HR + Legal |
| Access list review | Quarterly | IP Manager |
| Exit interview with TS reminder | At separation | HR + Manager |
| Vendor NDA verification | Before any disclosure | Procurement + Legal |
| Annual trade secret audit | Annually | IP Manager + Legal |
| Training on TS handling | At hire + annually | Engineering Management |

### Physical Controls

| Control | Implementation | Scope |
|---------|---------------|-------|
| Secure lab access | Badge + PIN | Prototype hardware |
| Prototype tracking | Serial number registry | All physical units |
| Prototype destruction | Witnessed physical destruction + certificate | Scrapped units |
| Visitor management | Escorted access only in engineering areas | All facilities |
| Clean desk policy | No TS documents visible unattended | All workspaces |
| Secure disposal | Cross-cut shredding for paper; secure wipe for digital | All TS materials |

---

## Access Control Matrix

```
                    TS-001  TS-002  TS-003  TS-004  TS-005  TS-006  TS-007  TS-008
System Architect      R       R       -       R       R       R       R       R
HW Team Lead          R       R       -       -       -       R       R       -
HW Engineer           -       R       -       -       -       R       R       -
FW Team Lead          -       -       -       R       R       -       R       R
ML Team Lead          -       -       R       R       -       -       -       R
Layout Contractor*    -       R       -       -       -       -       -       -
CM Partner*           -       -       -       -       -       -       -       -

R = Read access    * = Under NDA    - = No access
```

---

## Breach Response Plan

### Detection

- Automated DLP alerts for TS keywords in unauthorized channels
- Employee self-reporting mechanism (anonymous hotline)
- Competitor product analysis revealing potential TS exposure
- Audit log anomaly detection (unusual access patterns)

### Response (within 24 hours of detection)

1. **Contain**: Immediately revoke access of suspected source; preserve evidence
2. **Assess**: Determine scope of exposure (which TS items, to whom, how)
3. **Notify**: Alert legal counsel, IP Manager, and executive team
4. **Investigate**: Forensic analysis of access logs, communications, device activity
5. **Remediate**: Demand return/destruction from recipients; send cease-and-desist
6. **Litigate**: If warranted, pursue injunctive relief under DTSA or state laws
7. **Prevent**: Update controls to prevent recurrence; document lessons learned

### Documentation

All breach incidents must be documented with:
- Date and time of discovery
- Trade secret(s) affected (by TS-ID)
- Suspected source and recipient
- Containment actions taken
- Investigation findings
- Legal actions pursued
- Preventive measures implemented

---

## Review Schedule

| Review Type | Frequency | Participants |
|-------------|-----------|--------------|
| Catalog completeness review | Quarterly | IP Manager + Engineering Leads |
| Access control audit | Quarterly | IP Manager + IT Security |
| Full compliance audit | Annually | IP Manager + Legal + External Auditor |
| Personnel change update | On event | HR + IP Manager |
| Vendor NDA renewal check | Semi-annually | Procurement + Legal |

---

## Patent/Trade Secret Boundary

For each ADVIS invention disclosure, the following boundary applies:

| Disclosure | Patent (Public) | Trade Secret (Private) |
|-----------|-----------------|----------------------|
| ID-001 (Platform) | Adaptive concept, block diagrams | Exact pinout, routing rules, timing values |
| ID-002 (Module) | Thermal/EMC architecture concept | Material specs, exact dimensions, EMI recipes |
| ID-003 (Fusion) | Coupling function concept, claims | Alpha values, thresholds, training data |
| ID-004 (Calibration) | Mutual calibration method | Feature detection parameters, confidence thresholds |
| ID-005 (Power) | Risk-aware mode concept | Mode transition thresholds, pre-staging timing |

**Rule**: If in doubt whether information should be in a patent disclosure or kept as trade secret, consult legal counsel. Default to trade secret until a deliberate filing decision is made.

---

**Document Version:** 2.0  
**Last Updated:** 2025-01  
**Classification:** CONFIDENTIAL - Restricted Distribution  
**Access**: IP Manager, Legal Counsel, Engineering Leadership only
