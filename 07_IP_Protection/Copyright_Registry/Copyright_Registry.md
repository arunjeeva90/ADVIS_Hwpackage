# ADVIS Copyright Registry

## Purpose

This document establishes the copyright registration plan for all copyrightable works created as part of the ADVIS platform development. While copyright protection is automatic upon creation, formal registration provides significant legal advantages including statutory damages and attorney's fees in infringement actions.

---

## Copyright Ownership Chain

### Work-for-Hire Doctrine

All works created by employees within the scope of their employment are automatically owned by the employer under the work-for-hire doctrine (17 USC 101). No separate assignment is needed for employee-created works.

### Contractor-Created Works

Works created by contractors or consultants require explicit written assignment. The following must be in place BEFORE work begins:

| Requirement | Document | Responsible |
|-------------|----------|-------------|
| Work-for-hire agreement | Contractor Agreement (Section IP) | Legal + Procurement |
| Copyright assignment clause | Same agreement or separate assignment | Legal |
| Pre-existing IP disclosure | Contractor's prior IP declaration | Contractor |
| Moral rights waiver (where applicable) | Included in agreement | Legal |

### Joint Works

If work is created jointly by employees and contractors:
- Company owns the unified work under work-for-hire
- Contractor's contribution is subject to assignment clause
- Joint authorship does NOT imply joint ownership when proper agreements are in place

---

## Registerable Works

### Category 1: Firmware and Software

| Work | Registration Priority | Est. Lines of Code | Registration Type |
|------|----------------------|-------------------|-------------------|
| ADVIS HAL (Hardware Abstraction Layer) | HIGH | 15,000-25,000 | Literary work |
| Device drivers (camera, CAN, GNSS, IMU) | HIGH | 10,000-20,000 | Literary work |
| Decision fusion algorithm implementation | HIGH | 5,000-10,000 | Literary work |
| Mutual calibration algorithm | HIGH | 3,000-8,000 | Literary work |
| Risk-aware power management firmware | MEDIUM | 3,000-5,000 | Literary work |
| Boot loader and configuration system | MEDIUM | 5,000-10,000 | Literary work |
| Manufacturing test software | MEDIUM | 5,000-8,000 | Literary work |
| Development tools and scripts | LOW | 2,000-5,000 | Literary work |

### Category 2: Documentation

| Work | Registration Priority | Page Count | Registration Type |
|------|----------------------|-----------|-------------------|
| ADVIS Technical Reference Manual | HIGH | 200+ pages | Literary work |
| Hardware Integration Guide | HIGH | 100+ pages | Literary work |
| API Reference Documentation | MEDIUM | 150+ pages | Literary work |
| System Architecture Documents | MEDIUM | 50+ pages | Literary work |
| Patent disclosures (as unpublished works) | LOW | 50+ pages | Literary work |
| Training materials | LOW | Various | Literary work |

### Category 3: Design Files

| Work | Registration Priority | Format | Registration Type |
|------|----------------------|--------|-------------------|
| Schematic design files | MEDIUM | OrCAD/Altium source | Literary work (code) |
| PCB layout files | MEDIUM | Gerber + source | Literary work (code) |
| Mechanical CAD models | MEDIUM | STEP/IGES | Pictorial/graphic work |
| IC symbol and footprint libraries | LOW | EDA library format | Literary work |

### Category 4: Datasets (Database Copyright)

| Work | Registration Priority | Size | Registration Type |
|------|----------------------|------|-------------------|
| Training dataset organization/structure | HIGH | N/A | Compilation |
| Test case library | MEDIUM | N/A | Compilation |
| Validation dataset organization | MEDIUM | N/A | Compilation |

**Note**: Individual data items (images, sensor readings) may not be copyrightable, but the selection, coordination, and arrangement of a database IS copyrightable as a compilation.

---

## Registration Process

### US Copyright Registration (Copyright Office)

```
Step 1: Prepare deposit copy
  |
  v
Step 2: Complete application (Form TX for literary works)
  |
  v
Step 3: Pay filing fee ($65 online / $125 paper per work)
  |
  v
Step 4: Submit via electronic Copyright Office (eCO) system
  |
  v
Step 5: Receive registration certificate (3-8 months typical)
```

### Registration Timing Strategy

| Timing | Benefit |
|--------|---------|
| Before publication | Statutory damages available from date of first infringement |
| Within 3 months of publication | Statutory damages available from date of first infringement |
| After 3 months of publication | Only actual damages available for pre-registration infringement |

**Recommendation**: Register HIGH-priority works BEFORE any external release or licensing.

### Deposit Requirements

| Work Type | Deposit Requirement |
|-----------|-------------------|
| Published software | First 25 pages + last 25 pages of source code |
| Unpublished software | Complete copy (with trade secrets redacted if needed) |
| Documentation | Complete copy (best edition) |
| Databases | 50 representative pages from the compilation |

### Trade Secret Redaction

For source code containing trade secrets:
- May redact up to 49% of deposited code (blocked out)
- OR deposit first 10 pages + last 10 pages only
- Must still demonstrate original authorship in deposited portion
- Redacted portions are still covered by registration (for the whole work)

---

## Registration Schedule

### Phase 1: Immediate (Months 1-3)

| Work | Action | Target Date |
|------|--------|-------------|
| Decision fusion algorithm | Register as unpublished work | Month 1 |
| ADVIS HAL core modules | Register as unpublished work | Month 2 |
| Technical Reference Manual | Register as unpublished work | Month 2 |
| Mutual calibration algorithm | Register as unpublished work | Month 3 |

### Phase 2: Pre-Release (Months 3-6)

| Work | Action | Target Date |
|------|--------|-------------|
| Complete firmware package | Register before first customer delivery | Month 5 |
| Hardware Integration Guide | Register before OEM distribution | Month 5 |
| API Reference Documentation | Register before developer release | Month 6 |
| Device driver collection | Register as compilation | Month 6 |

### Phase 3: Post-Release (Months 6-12)

| Work | Action | Target Date |
|------|--------|-------------|
| Design files (schematic + PCB) | Register before design license delivery | Month 7 |
| Training materials | Register before external training | Month 8 |
| Manufacturing test software | Register before CM delivery | Month 9 |
| Updated versions (as released) | Supplementary registrations | Ongoing |

---

## Copyright Notice Format

All copyrightable works should include the following notice:

### Source Code

```c
/*
 * Copyright (c) 2025 [Company Name]. All rights reserved.
 *
 * This software is proprietary and confidential. Unauthorized copying,
 * transfer, or use of this software, via any medium, is strictly prohibited.
 *
 * ADVIS Platform - [Module Name]
 */
```

### Documentation

```
Copyright 2025 [Company Name]. All rights reserved.

This document contains proprietary information. No part of this document may be
reproduced, stored in a retrieval system, or transmitted in any form without
prior written permission of [Company Name].
```

### Design Files

```
Copyright (c) 2025 [Company Name]. All rights reserved.
ADVIS Platform - [Design Name] - Proprietary and Confidential.
Unauthorized reproduction or distribution prohibited.
```

---

## Enforcement Strategy

### Monitoring

- Periodic search for unauthorized copies (GitHub, package registries)
- Customer/licensee audit rights (per license agreement)
- Automated code similarity detection for published open-source projects
- Monitor competitor products for copied documentation or UI elements

### Enforcement Actions (Escalation Ladder)

| Step | Action | Trigger |
|------|--------|---------|
| 1 | Internal documentation of infringement | Discovery |
| 2 | Cease-and-desist letter | Confirmed infringement |
| 3 | DMCA takedown notice (for online infringement) | Online publication |
| 4 | Demand letter with damages calculation | Continued infringement |
| 5 | Litigation | Failure to comply with demand |

### Registration Advantage in Litigation

| With Registration | Without Registration |
|------------------|---------------------|
| Statutory damages: $750-$150,000 per work | Actual damages only (often difficult to prove) |
| Willful infringement: up to $150,000 per work | No statutory damages enhancement |
| Attorney's fees recoverable | No fee shifting |
| Presumption of validity (if registered within 5 years) | Must prove ownership and originality |

---

## International Copyright Considerations

### Automatic Protection (Berne Convention)

Copyright is automatically protected in all 179 Berne Convention member countries without registration. However:

| Country | Registration Benefit |
|---------|---------------------|
| United States | Required for litigation; enables statutory damages |
| China | Recommended for enforcement; provides evidentiary presumption |
| India | Recommended; creates public record of ownership |
| EU countries | Not required; automatic protection under Berne Convention |
| Japan | Not required; automatic protection |

### Recommended International Registrations

For key markets where ADVIS will be manufactured or deployed:
1. **US**: Register all HIGH-priority works (required for enforcement)
2. **China**: Register firmware and documentation (recommended for enforcement)
3. **India**: Register firmware (recommended given local development presence)

---

## Budget Estimate

| Item | Count | Unit Cost | Total |
|------|-------|-----------|-------|
| US copyright registrations (Phase 1) | 4 | $65 | $260 |
| US copyright registrations (Phase 2) | 4 | $65 | $260 |
| US copyright registrations (Phase 3) | 4 | $65 | $260 |
| China copyright registrations | 3 | $200-500 | $600-1,500 |
| India copyright registrations | 2 | $100-200 | $200-400 |
| Attorney fees for preparation | Flat | $2,000-5,000 | $2,000-5,000 |
| **Total Year 1** | | | **$3,500-7,700** |

---

## Record Keeping

### Copyright Register Database

Maintain a register of all copyrightable works with:

| Field | Description |
|-------|-------------|
| Work ID | Unique identifier (CW-001, CW-002, etc.) |
| Title | Descriptive title of the work |
| Authors | All contributing authors |
| Creation date | Date of first fixation |
| Publication date | Date of first external distribution (if any) |
| Registration number | Copyright Office registration number |
| Registration date | Date registration certificate issued |
| Deposit copy location | Where the deposited version is archived |
| Version history | Major revisions and update registrations |

---

**Document Version:** 1.0  
**Last Updated:** 2025-01  
**Classification:** INTERNAL - IP Management
