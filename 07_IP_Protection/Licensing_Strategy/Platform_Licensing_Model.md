# ADVIS Platform Licensing Model

## Purpose

This document defines the licensing strategy for the ADVIS platform intellectual property, covering per-unit royalties, design license fees, SoM certification programs, and full-stack licensing terms for various customer and partner tiers.

---

## Licensing Overview

```
+------------------------------------------------------------------+
|                  ADVIS Licensing Tiers                             |
|                                                                  |
|  +-------------------+  +-------------------+  +---------------+ |
|  | MODULE LICENSE     |  | DESIGN LICENSE    |  | ALGORITHM     | |
|  |                   |  |                   |  | LICENSE       | |
|  | Buy complete      |  | License to self-  |  | Software only | |
|  | modules from us   |  | manufacture       |  | for own HW    | |
|  |                   |  |                   |  |               | |
|  | Per-unit pricing  |  | One-time fee +    |  | Per-unit      | |
|  |                   |  | per-unit royalty  |  | royalty       | |
|  +-------------------+  +-------------------+  +---------------+ |
|                                                                  |
|  +-------------------+  +-------------------+                    |
|  | FULL STACK        |  | SoM CERTIFICATION |                    |
|  | LICENSE           |  | PROGRAM           |                    |
|  |                   |  |                   |                    |
|  | Complete platform |  | SoC vendors get   |                    |
|  | + firmware + tools|  | "ADVIS Compatible"|                    |
|  |                   |  | certification     |                    |
|  | One-time + royalty|  |                   |                    |
|  | + support fees    |  | One-time cert fee |                    |
|  +-------------------+  +-------------------+                    |
|                                                                  |
+------------------------------------------------------------------+
```

---

## License Tier Details

### Tier 1: Module License (Buy Complete)

**Description**: OEM purchases complete ADVIS modules (assembled, tested, ready to integrate) from authorized manufacturing partners.

| Element | Terms |
|---------|-------|
| **What is provided** | Complete assembled module, tested and calibrated |
| **IP included** | Embedded firmware license (binary only); no source access |
| **Unit pricing** | $80-150 per module (volume-dependent) |
| **Minimum order** | 1,000 units for production pricing |
| **Support** | Standard integration support (40 hours included) |
| **Customization** | Standard configuration options (ADAS tier, camera variants) |
| **Duration** | Per purchase order; ongoing supply agreement |
| **IP restrictions** | No reverse engineering; no teardown publications; return scrap units |

**Volume Discount Schedule**:

| Annual Volume | Discount from List |
|--------------|-------------------|
| 1,000 - 9,999 | Base price |
| 10,000 - 49,999 | 10% discount |
| 50,000 - 199,999 | 18% discount |
| 200,000 - 499,999 | 25% discount |
| 500,000+ | Negotiated (30%+ typical) |

### Tier 2: Design License (Self-Manufacture)

**Description**: OEM or Tier-1 obtains license to manufacture ADVIS modules using their own production facilities and supply chain.

| Element | Terms |
|---------|-------|
| **What is provided** | Complete design package: schematics, PCB layout, BOM, firmware source |
| **IP included** | Manufacturing rights; firmware source license; patent license |
| **One-time fee** | $500K - 2M (depending on scope and exclusivity) |
| **Per-unit royalty** | $2-5 per manufactured unit |
| **Support** | Engineering support during transfer (included in one-time fee) |
| **Duration** | 5-year term with renewal option |
| **IP restrictions** | No sublicensing; no derivative product development outside agreement |
| **Exclusivity** | Available; premium of 2-3x on one-time fee |

**Design Package Contents**:
- Schematic source files (OrCAD/Altium format)
- PCB layout files (Gerbers + source)
- Complete BOM with approved alternates
- Firmware source code (HAL + drivers + application)
- Manufacturing test specifications
- Assembly and soldering guidelines
- Qualification test procedures
- Integration documentation

### Tier 3: Algorithm License

**Description**: OEM or Tier-1 with their own camera hardware licenses ADVIS software algorithms (decision fusion, calibration, power management) for deployment on their own platform.

| Element | Terms |
|---------|-------|
| **What is provided** | Algorithm binaries or source (tier-dependent); API documentation |
| **IP included** | Software usage license; patent license for algorithm methods |
| **Per-unit royalty** | $3-8 per unit (depends on algorithm bundle selected) |
| **Minimum commitment** | 50,000 units over 3 years |
| **Support** | Integration support; algorithm tuning for customer platform |
| **Duration** | 3-year term with renewal |
| **IP restrictions** | No modification of algorithm internals; no reverse engineering |
| **Customization** | Algorithm tuning for customer-specific SoC and camera configuration |

**Algorithm Bundle Options**:

| Bundle | Contents | Per-Unit Royalty |
|--------|----------|-----------------|
| Decision Fusion | Risk-coupled ADAS+DMS fusion engine | $3-5 |
| Self-Calibration | Dual-camera mutual calibration system | $1-2 |
| Power Management | Risk-aware power and sensor control | $1-2 |
| Full Algorithm Stack | All of above + future algorithms | $6-8 |

### Tier 4: Full Stack License

**Description**: Comprehensive license for Tier-1 suppliers who want to offer ADVIS as part of their own product portfolio.

| Element | Terms |
|---------|-------|
| **What is provided** | Everything: design files, firmware, algorithms, tools, documentation |
| **IP included** | Full manufacturing + deployment rights; patent license; trademark license |
| **One-time fee** | $1.5M - 5M (depending on scope and territory) |
| **Per-unit royalty** | $5-10 per unit |
| **Support** | Dedicated engineering support team; quarterly reviews |
| **Duration** | 7-year term with renewal |
| **IP restrictions** | No sublicensing without written consent; field-of-use restrictions |
| **Trademark** | May use "Powered by ADVIS" branding under trademark license |
| **Updates** | Receives platform updates for duration of agreement |

### Tier 5: SoM Certification Program

**Description**: SoC vendors pay to certify their modules as "ADVIS Compatible" and join the ecosystem.

| Element | Terms |
|---------|-------|
| **What is provided** | Technical interface specification; validation test suite; certification mark |
| **Certification fee** | $50K - 100K per SoM variant |
| **Annual maintenance** | $15K per certified variant |
| **Requirement** | SoM must pass all compatibility tests on ADVIS carrier |
| **Benefit to vendor** | Listed as certified module; access to ADVIS customer base |
| **Support** | Technical guidance during development; test lab access |
| **Duration** | Annual certification; re-certification required for new variants |

---

## Exclusivity Options

### Regional Exclusivity

| Exclusivity Type | Premium | Duration | Territory Examples |
|-----------------|---------|----------|-------------------|
| Market segment exclusive | 2x one-time fee | 3 years | "Commercial vehicles in EU" |
| Regional exclusive | 2.5x one-time fee | 3 years | "Passenger vehicles in China" |
| Global exclusive (one segment) | 3x one-time fee | 5 years | "Luxury sedan segment worldwide" |
| Full exclusive | Case-by-case | Negotiated | Not recommended (limits revenue) |

### Exclusivity Conditions

- Volume commitments required to maintain exclusivity (minimum annual units)
- If volume commitments not met for 2 consecutive quarters, exclusivity converts to non-exclusive
- Exclusivity does not apply to new platform generations (future products)
- Advance notice required before granting exclusivity to competitor in adjacent segment

---

## Volume Commitments and Guarantees

### Minimum Annual Purchase/Royalty

| License Tier | Minimum Annual Commitment |
|-------------|--------------------------|
| Module License | 10,000 units (or $1M purchase value) |
| Design License | 25,000 units manufactured (or minimum royalty $75K) |
| Algorithm License | 50,000 units deployed (or minimum royalty $150K) |
| Full Stack License | 100,000 units (or minimum royalty $500K) |

### Shortfall Provisions

- If actual volume falls below commitment, licensee pays difference up to minimum
- Force majeure exceptions for industry-wide disruptions
- First year treated as ramp-up period (50% of minimum applies)

---

## License Fee Structure

### Payment Terms

| Payment Type | Standard Terms |
|-------------|---------------|
| One-time license fee | 50% on signing; 50% on delivery of design package |
| Per-unit royalty | Quarterly, in arrears, based on actual production/shipment |
| Support fees | Annual, payable in advance |
| Certification fees | On submission of certification application |
| Audit shortfall | Within 30 days of audit finding |

### Royalty Reporting

- Licensee provides quarterly production/shipment report
- Report includes: unit count, product variant, territory of sale
- Licensor has right to audit licensee records (once per year, at licensor's cost)
- Under-reporting penalty: 150% of under-reported royalties + audit costs

---

## Intellectual Property Warranties

### Licensor Warrants

- Licensed technology does not, to Licensor's knowledge, infringe valid third-party patents
- Licensor has right and authority to grant the license
- Licensed materials are original works of Licensor (or properly sublicensed)

### Licensor Does NOT Warrant

- Fitness for any particular purpose beyond documented specifications
- Compatibility with licensee's specific vehicle platform (integration is licensee's responsibility)
- Freedom from all possible third-party claims (FTO is shared responsibility)
- Specific performance levels in licensee's application environment

### Indemnification

- Licensor indemnifies licensee for IP infringement claims related to licensed technology
- Cap on indemnification: total license fees paid
- Licensee must notify promptly and cooperate in defense
- Licensor has right to modify licensed technology to avoid infringement

---

## Technology Transfer Process

### For Design License and Full Stack License

| Phase | Duration | Activities |
|-------|----------|------------|
| Phase 1: Transfer | 2-4 weeks | Deliver design package; initial training |
| Phase 2: Integration | 4-8 weeks | Licensee integrates into their processes; support available |
| Phase 3: Validation | 4-6 weeks | Licensee builds and validates first articles |
| Phase 4: Production Readiness | 2-4 weeks | Manufacturing line qualification |
| Phase 5: Ongoing | Duration of license | Quarterly technical reviews; update delivery |

### Deliverables by Phase

**Phase 1 Deliverables**:
- Complete design database (schematic, layout, BOM)
- Firmware source repository access
- Documentation package (specifications, test procedures)
- Training sessions (40 hours minimum)

**Phase 2 Support**:
- Engineering hotline access (business hours)
- Weekly technical sync meetings
- Design review of licensee modifications (if permitted)

**Phase 3 Support**:
- First article inspection guidance
- Test equipment setup support
- Yield analysis assistance

---

## Commercial Terms Summary

| License Tier | One-Time Fee | Per-Unit | Min. Commitment | Best For |
|-------------|-------------|----------|-----------------|----------|
| Module | N/A | $80-150 | 10K/year | Small OEMs; quick start |
| Design | $500K-2M | $2-5 | 25K/year | Large OEMs wanting control |
| Algorithm | N/A | $3-8 | 50K/3yr | OEMs with own hardware |
| Full Stack | $1.5M-5M | $5-10 | 100K/year | Tier-1 platform partners |
| SoM Cert | $50K-100K | N/A | N/A | SoC vendors |

---

## Competitive Positioning

### vs. Mobileye Licensing

- Mobileye: Black-box; OEM has no design visibility or manufacturing option
- ADVIS: Open licensing model; OEM can self-manufacture; algorithm is transparent at architecture level

### vs. Qualcomm Platform

- Qualcomm: Locked to Qualcomm silicon; high per-unit royalty
- ADVIS: Multi-SoC support; lower per-unit cost; no silicon lock-in

### vs. Open-Source (OpenCV, OpenPilot)

- Open-source: No support; no IP protection; no automotive qualification
- ADVIS: Production-ready; patent-protected; automotive-qualified; professional support

---

**Document Version:** 1.0  
**Last Updated:** 2025-01  
**Classification:** CONFIDENTIAL - Commercial Sensitive
