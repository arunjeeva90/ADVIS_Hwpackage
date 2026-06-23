# ADVIS Environmental Compliance (RoHS / REACH)

| Field | Value |
|-------|-------|
| Document ID | ADVIS-CS-ENV-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Environmental Compliance Team |
| Date | 2024-01-15 |
| Classification | INTERNAL |

---

## 1. Scope

This document defines the environmental compliance strategy for the ADVIS ECU, covering EU RoHS Directive, REACH Regulation, conflict minerals reporting, and material declaration processes. All components, materials, and processes used in ADVIS production shall comply with applicable environmental regulations.

## 2. Applicable Regulations

| Regulation | Scope | ADVIS Applicability |
|------------|-------|---------------------|
| EU RoHS (2011/65/EU + 2015/863) | Restriction of hazardous substances | Full compliance required |
| EU REACH (EC 1907/2006) | Chemical registration and authorization | SVHC reporting required |
| EU ELV (2000/53/EC) | End-of-life vehicles | Applicable (automotive component) |
| China RoHS (GB/T 26572) | China hazardous substance restrictions | Required for China market |
| US Conflict Minerals (Dodd-Frank Act) | Tin, tantalum, tungsten, gold (3TG) | Due diligence required |
| EU Conflict Minerals (2017/821) | 3TG sourcing | Due diligence required |
| GADSL | Global Automotive Declarable Substance List | Customer requirement |
| IMDS | International Material Data System | OEM submission required |

## 3. RoHS Compliance

### 3.1 Restricted Substances (EU RoHS)

| Substance | Maximum Concentration | ADVIS Status |
|-----------|-----------------------|--------------|
| Lead (Pb) | 0.1% (1000 ppm) by weight in homogeneous material | Compliant (lead-free solder) |
| Mercury (Hg) | 0.1% (1000 ppm) | Compliant (no mercury components) |
| Cadmium (Cd) | 0.01% (100 ppm) | Compliant |
| Hexavalent chromium (Cr6+) | 0.1% (1000 ppm) | Compliant (RoHS-compliant plating) |
| PBB (polybrominated biphenyls) | 0.1% (1000 ppm) | Compliant (halogen-free PCB) |
| PBDE (polybrominated diphenyl ethers) | 0.1% (1000 ppm) | Compliant (halogen-free PCB) |
| DEHP (bis(2-ethylhexyl) phthalate) | 0.1% (1000 ppm) | Compliant |
| BBP (butyl benzyl phthalate) | 0.1% (1000 ppm) | Compliant |
| DBP (dibutyl phthalate) | 0.1% (1000 ppm) | Compliant |
| DIBP (diisobutyl phthalate) | 0.1% (1000 ppm) | Compliant |

### 3.2 RoHS Exemptions Used

| Exemption # | Description | Application in ADVIS | Expiry Date |
|-------------|-------------|---------------------|-------------|
| 7(c)-I | Lead in high-melting-point solders (> 85% Pb) | Not used (lead-free process) | N/A |
| 7(a) | Lead in glass of electronic components | Passive component internal (if applicable) | 2027 (review) |
| 15 | Lead in solders for flip chip | BGA underfill (if applicable) | 2027 (review) |

*Note: ADVIS targets fully lead-free assembly (SAC305 solder) with no RoHS exemptions where possible.*

### 3.3 RoHS Verification Process

1. **Component selection:** Verify RoHS compliance in component datasheet/environmental data
2. **Supplier declaration:** Obtain RoHS declaration of conformity from each supplier
3. **BOM review:** Flag any components lacking RoHS documentation
4. **Process verification:** Confirm lead-free soldering process (SAC305, peak 245C)
5. **Material testing (if required):** XRF screening for suspect materials
6. **Certificate of compliance:** Issue ADVIS-level RoHS declaration

## 4. REACH Compliance

### 4.1 SVHC (Substances of Very High Concern) Reporting

| Requirement | Threshold | ADVIS Action |
|-------------|-----------|--------------|
| SVHC communication (Art. 33) | > 0.1% w/w in article | Supplier must declare |
| SCIP database notification | > 0.1% w/w | Submit data to ECHA |
| SVHC list update monitoring | Bi-annual update | Review each new candidate list |

### 4.2 SVHC Screening Process

1. **Identify SVHC-containing materials:** Review current ECHA Candidate List (updated twice yearly)
2. **Supplier questionnaire:** Request SVHC declarations from all component suppliers
3. **Concentration assessment:** Calculate SVHC content per article (> 0.1% threshold)
4. **SCIP notification:** Submit to ECHA SCIP database if threshold exceeded
5. **Substitution planning:** Develop phase-out plan for SVHC-containing components

### 4.3 Current SVHC Watchlist for ADVIS

| Material / Substance | Potential Source | Risk Level | Action |
|---------------------|-----------------|------------|--------|
| Lead (CAS 7439-92-1) | Solder, component internal | Low (lead-free) | Monitor exemptions |
| Boric acid | Underfill / adhesive | Low | Verify with supplier |
| PFAS (per/polyfluoroalkyl) | Conformal coating | Medium | Confirm formulation |
| Cobalt compounds | Battery (if any) | N/A (no battery) | Not applicable |
| Nickel compounds | Plating | Low | Standard automotive plating |

## 5. Conflict Minerals

### 5.1 Due Diligence Framework

Per the OECD Due Diligence Guidance for Responsible Supply Chains of Minerals from Conflict-Affected and High-Risk Areas:

| Step | Action | ADVIS Implementation |
|------|--------|---------------------|
| 1 | Establish management systems | Conflict minerals policy |
| 2 | Identify and assess risks | CMRT (Conflict Minerals Reporting Template) |
| 3 | Design strategy to respond | Supplier engagement program |
| 4 | Third-party audit | RMI (Responsible Minerals Initiative) |
| 5 | Report | Annual disclosure (if public company) |

### 5.2 3TG Presence in ADVIS

| Mineral | Common Sources in Electronics | ADVIS Components |
|---------|------------------------------|------------------|
| Tin (Sn) | Solder (SAC305), tin plating | PCB assembly, component leads |
| Tantalum (Ta) | Tantalum capacitors | Power supply decoupling (if used) |
| Tungsten (W) | Vibration motor weights, contacts | Minimal use |
| Gold (Au) | Connector plating, wire bonding | Connectors, IC wire bonds |

### 5.3 Supplier Requirements

All Tier-1 suppliers shall:
- Complete the RMI Conflict Minerals Reporting Template (CMRT) annually
- Identify smelters/refiners in their supply chain
- Commit to sourcing from RMI-conformant smelters
- Respond within 30 days to conflict minerals inquiries

## 6. Material Declaration Process

### 6.1 IMDS Submission

For OEM customers using the International Material Data System:

| Step | Activity | Responsibility |
|------|----------|---------------|
| 1 | Collect material data from all component suppliers | Procurement |
| 2 | Create Material Data Sheets (MDS) for each component | Environmental Engineer |
| 3 | Build product tree in IMDS | Environmental Engineer |
| 4 | Calculate total product composition | IMDS system |
| 5 | Submit to OEM customer | Environmental Engineer |
| 6 | Respond to customer queries | Environmental Engineer |

### 6.2 Material Declaration Timeline

| Milestone | Timing | Deliverable |
|-----------|--------|-------------|
| Component MDS collection | BOM freeze + 4 weeks | Supplier MDS database |
| IMDS entry complete | BOM freeze + 8 weeks | IMDS product tree |
| Customer submission | Before PPAP | IMDS submission ID |
| Update (for ECOs) | Within 4 weeks of BOM change | Revised IMDS entry |

## 7. Supplier Compliance Requirements

### 7.1 Environmental Requirements for Suppliers

| Requirement | Documentation | Frequency |
|-------------|---------------|-----------|
| RoHS declaration | Signed DoC per component | Per qualification |
| REACH/SVHC declaration | Signed declaration or SCIP data | Annual update |
| Conflict minerals | CMRT (latest RMI version) | Annual |
| Material composition | Full material disclosure (FMD) or IMDS | Per qualification |
| Halogen-free declaration | IEC 61249-2-21 compliance | Per qualification |
| Process change notification | PCN with environmental impact assessment | As needed |

### 7.2 Non-Compliance Escalation

| Level | Trigger | Action |
|-------|---------|--------|
| 1 | Missing documentation | Request within 30 days |
| 2 | Incomplete data after 30 days | Formal escalation to supplier quality |
| 3 | Confirmed non-compliance | Material review, potential hold |
| 4 | Critical substance violation | Stop shipment, customer notification |

## 8. End-of-Life Vehicle (ELV) Compliance

### 8.1 Design for Recyclability

| Requirement | ADVIS Implementation |
|-------------|---------------------|
| Material marking (plastics > 25g) | Mark enclosure material (if applicable) |
| Disassembly considerations | Fasteners removable with standard tools |
| Material compatibility | Avoid incompatible material combinations |
| Recyclability rate target | >= 85% by weight (per ELV Directive) |
| Hazardous substance minimization | Lead-free, halogen-free design |

### 8.2 Recyclability Assessment

| Material | Estimated Weight (g) | Recyclable? | Method |
|----------|---------------------|-------------|--------|
| PCB (FR-4) | [TBD] | Yes | Copper recovery, pyrolysis |
| ICs (plastic packages) | [TBD] | Yes | Precious metal recovery |
| Connectors (LCP + gold) | [TBD] | Yes | Separation and recovery |
| Enclosure (if applicable) | [TBD] | Yes | Plastic recycling |
| Cables (copper + jacket) | [TBD] | Yes | Copper recovery |
| Thermal interface material | [TBD] | Limited | Incineration |

## 9. Compliance Documentation Matrix

| Document | Owner | Update Frequency | Storage |
|----------|-------|------------------|---------|
| RoHS Declaration of Conformity | Quality Manager | Per design change | QMS |
| REACH SVHC Communication | Environmental Engineer | Bi-annual (with SVHC list) | QMS |
| Conflict Minerals Report (CMRT) | Procurement | Annual | QMS |
| IMDS Submission | Environmental Engineer | Per BOM change | IMDS system |
| Halogen-Free Declaration | Quality Manager | Per design change | QMS |
| Environmental Compliance Certificates | Quality Manager | Per product release | QMS |

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2024-01-15 | Environmental Compliance Team | Initial draft |
