# 06 - Patent Strategy

## Purpose

This folder contains the intellectual property strategy for the ADVIS (Adaptive Driver & Vehicle Intelligence System) platform, including invention disclosures, prior art research, patent claim drafts, and filing timelines.

## Sub-folders

| Folder | Contents |
|--------|----------|
| Invention_Disclosures/ | Formal invention disclosure forms for each patentable concept |
| Prior_Art_Search/ | Prior art search reports, patent landscape analysis |
| Claim_Drafts/ | Draft patent claims for attorney review |
| Design_Patents/ | Design patent applications (form factor, connector system, enclosure) |
| Utility_Patents/ | Utility patent applications (methods, architectures, algorithms) |
| Trade_Secrets_Register/ | Catalog of trade-secret-protected IP elements |
| Freedom_To_Operate/ | FTO analysis ensuring our designs do not infringe existing patents |
| Patent_Landscape_Maps/ | Visual maps of competitive patent positions |
| Filing_Timeline/ | Filing schedule, provisional deadlines, priority dates |

## Top 5 Patent Filings

### Utility Patent Candidates

| Priority | ID | Title | Status |
|----------|------|-------|--------|
| 1 | ID-003 | Risk-Coupled ADAS+DMS Decision Fusion | DRAFT - Ready for prior art search |
| 2 | ID-001 | SoC-Adaptive Dual-Vision Smart Camera Platform | DRAFT - Ready for prior art search |
| 3 | ID-002 | Compact Dual-Facing Windshield Module + Thermal/EMC Stack | DRAFT - Ready for prior art search |
| 4 | ID-004 | Dual-Camera Mutual Self-Calibration | DRAFT - Ready for prior art search |
| 5 | ID-005 | Risk-Aware Power, Sensor and IR Mode Control | DRAFT - Ready for prior art search |

### Design Patent Candidates

1. **Windshield-mount module form factor** - Compact dual-facing camera housing
2. **Modular SoM blade connector system** - Scalable SoC-to-carrier interface
3. **Single-cable harness connector industrial design** - Unified vehicle integration connector

### Trade Secret Elements (NOT for patent filing)

1. Carrier-to-SoM proprietary pinout specification
2. Optimized high-speed signal routing topology (PCB layout rules)
3. Platform configuration database and variant generation method
4. Indian road dataset and training parameters
5. Calibration threshold values
6. EMI mitigation recipes
7. Model tuning parameters

## Process

```
+-------------------+     +-------------------+     +-------------------+
| 1. Concept        |---->| 2. Disclosure     |---->| 3. Prior Art      |
| Identification    |     | Form (17-section) |     | Search            |
+-------------------+     +-------------------+     +-------------------+
                                                            |
+-------------------+     +-------------------+     +------v------------+
| 6. Filing         |<----| 5. Claim Drafts   |<----| 4. Decision       |
| (Provisional)     |     | (Attorney Review) |     | Patent/Secret     |
+-------------------+     +-------------------+     +-------------------+
        |
+-------v-----------+     +-------------------+     +-------------------+
| 7. Prior Art      |---->| 8. Non-Provisional|---->| 9. PCT Filing     |
| (Full Search)     |     | Conversion        |     | (International)   |
+-------------------+     +-------------------+     +-------------------+
```

## Invention Disclosure Format (17 Sections)

All invention disclosures follow this standardized 17-section format:

1. Title
2. Date
3. Inventors
4. Status
5. Problem Statement
6. Background / Prior Art Summary
7. Proposed Solution
8. Key Novel Elements
9. Technical Implementation Details (architecture level - no trade secrets)
10. Advantages Over Prior Art
11. Alternative Embodiments
12. Potential Claims (3 independent + dependent claims)
13. Drawings / Figures Description
14. Commercial Value
15. Filing Recommendation
16. Confidentiality Classification
17. Next Steps

## Important Notes

- File provisional patent applications BEFORE any public disclosure
- 12-month grace period (US only) from first public disclosure - do not rely on this
- All invention disclosures should be timestamped and witnessed
- Keep trade secrets OUT of any public-facing documentation
- Safety boundary: ADVIS generates safety-supervised actuation REQUESTS to OEM vehicle ECUs. Final actuator authority remains with OEM. Do NOT claim direct actuation in any patent.
- Do NOT overclaim ASIL-C or ASIL-D safety integrity levels

---

**Document Version:** 1.0  
**Last Updated:** 2025-01  
**Classification:** CONFIDENTIAL - Internal Use Only
