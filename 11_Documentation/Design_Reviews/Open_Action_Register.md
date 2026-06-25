# ADVIS Open Action Register

**Classification:** Confidential - Engineering Use Only  
**Version:** 0.1  
**Date:** July 2026  
**Last Updated:** July 2026

---

## Purpose

This register tracks all open design actions, decisions, and deliverables across the ADVIS hardware program. Actions are tracked from creation through completion with assigned owners, priorities, and due dates.

---

## Status Legend

| Status | Meaning |
|--------|---------|
| Open | Not yet started |
| In Progress | Work underway |
| Blocked | Waiting on dependency |
| Complete | Done and verified |
| Cancelled | No longer required |

---

## Priority Legend

| Priority | Meaning |
|----------|---------|
| P1 | Critical path - blocks PCB release or architecture definition |
| P2 | High - required before design review gate |
| P3 | Medium - required before DVT |
| P4 | Low - nice to have, can defer |

---

## Open Actions

| ID | Action | Owner | Priority | Status | Due Date | Notes |
|----|--------|-------|----------|--------|----------|-------|
| ACT-001 | Decide and document v0.5 direct-MIPI compact baseline architecture | Systems Lead | P1 | In Progress | TBD | Architecture baseline document created; sensor and SoC selection pending |
| ACT-002 | Select forward camera sensor candidate | Systems / Optics | P1 | Open | TBD | Candidates: IMX390, OX03C10, AR0233 class; need evaluation samples |
| ACT-003 | Select DMS camera sensor candidate | Systems / Optics | P1 | Open | TBD | Candidates: OX01N1B, OX01H1B, RGB-IR, AR0144 class; NIR performance critical |
| ACT-004 | Confirm SoC option for compact board: TDA4VL / TDA4VM / AM62A / other | Systems Lead | P1 | Open | TBD | Depends on AI performance requirement, CSI port count, cost target |
| ACT-005 | Define DMS flex length and connector | Mechanical / Electrical | P2 | Open | TBD | Depends on housing geometry and DMS pod offset |
| ACT-006 | Create compact optical/mechanical ICD | Optics / Mechanical | P2 | Open | TBD | Baffle, IR window, lens stack, bracket interface |
| ACT-007 | Create direct-MIPI signal integrity assumptions | SI Engineer | P2 | Open | TBD | Trace length budget, impedance, crosstalk, eye diagram targets |
| ACT-008 | Prepare invention disclosure pack for patent attorney | IP Lead | P2 | Open | TBD | Five invention disclosures drafted; attorney review needed |
| ACT-009 | Create first ADVIS DVP&R (Design Verification Plan and Report) | Validation Lead | P2 | Open | TBD | Initial DVP&R v0.1 created; requires test method detail |
| ACT-010 | Create cost-down BOM comparison | Hardware Lead | P2 | Complete | July 2026 | BOM comparison document created |
| ACT-011 | Verify safety boundary wording across repository | Systems Lead | P1 | Complete | July 2026 | Updated all instances to tiered language |
| ACT-012 | Decide what remains trade secret vs. patent disclosure | IP Lead / Legal | P2 | Open | TBD | Must finalize before patent attorney briefing |
| ACT-013 | Prepare patent attorney briefing pack | IP Lead | P3 | Open | TBD | Blocked on ACT-012 completion |
| ACT-014 | Create v0.5 system block diagram | Systems Lead | P1 | Open | TBD | New block diagram without SerDes, showing direct MIPI |
| ACT-015 | Create v0.5 PCB placement concept | Layout Lead | P2 | Open | TBD | Blocked on SoC selection (ACT-004) and housing dimensions |

---

## Completed Actions (Archive)

| ID | Action | Owner | Completed | Notes |
|----|--------|-------|-----------|-------|
| ACT-010 | Create cost-down BOM comparison | Hardware Lead | July 2026 | See 02_Schematic/BOM/ADVIS_Cost_Down_BOM_Comparison_v0.1.md |
| ACT-011 | Verify safety boundary wording across repository | Systems Lead | July 2026 | All files updated to tiered safety language |

---

## Dependencies

| Action | Depends On | Notes |
|--------|-----------|-------|
| ACT-005 | ACT-003, housing geometry | Flex length driven by DMS sensor package and pod design |
| ACT-006 | ACT-002, ACT-003 | Optical ICD requires sensor selection |
| ACT-007 | ACT-004 | SI assumptions depend on SoC CSI port specifications |
| ACT-013 | ACT-012 | Cannot brief attorney until trade secret boundary is defined |
| ACT-015 | ACT-004 | Placement requires SoC package dimensions |

---

*End of Document*
