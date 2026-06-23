# ADVIS Engineering Change Order (ECO) Process

## 1. Purpose

This document defines the Engineering Change Order process for the ADVIS hardware platform. Any modification to a locked baseline item requires an ECO with proper impact assessment and approval before implementation.

## 2. When an ECO is Required

An ECO is required for changes to any item that has been locked or baselined:

| Change Type | ECO Required | Example |
|-------------|-------------|---------|
| Component substitution | Yes | Replacing LM61460-Q1 with alternative buck |
| Schematic modification | Yes | Adding/removing connections, changing values |
| PCB layout change (post-release) | Yes | Re-routing traces, adding vias |
| BOM value change | Yes | Changing decoupling cap from 100nF to 220nF |
| Interface reassignment | Yes | Moving SPI bus from Bus0 to Bus1 |
| Connector pinout change | Yes | Swapping pin assignments |
| Document correction (technical) | Yes | Correcting voltage values in specifications |
| Document formatting only | No | Fixing typos, reformatting tables |
| Adding new documentation | No | New technical notes, meeting minutes |

## 3. ECO Workflow

```
+-------------------+
| 1. INITIATION     |  Originator identifies need for change
+-------------------+
         |
         v
+-------------------+
| 2. DOCUMENTATION  |  Fill ECO form with description, rationale, impact
+-------------------+
         |
         v
+-------------------+
| 3. IMPACT ASSESS  |  Evaluate cost, schedule, performance, safety impact
+-------------------+
         |
         v
+-------------------+
| 4. REVIEW         |  Technical review by affected parties
+-------------------+
         |
         v
+-------------------+
| 5. APPROVAL       |  Approval authority signs off
+-------------------+
         |
         v
+-------------------+
| 6. IMPLEMENTATION |  Execute the change in design files
+-------------------+
         |
         v
+-------------------+
| 7. VERIFICATION   |  Verify change implemented correctly
+-------------------+
         |
         v
+-------------------+
| 8. CLOSE-OUT      |  Update affected documents, close ECO
+-------------------+
```

## 4. Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| Originator | Identifies need, fills ECO form, presents justification |
| Designer | Implements change, updates affected documents |
| Reviewer | Technical assessment of proposed change |
| Approver | Authorization to proceed (based on impact level) |
| Configuration Manager | Tracks ECO status, updates baseline records |
| Quality Engineer | Verifies process compliance (for critical changes) |

## 5. Approval Authority

| Impact Level | Criteria | Approver(s) Required |
|--------------|----------|---------------------|
| Minor | No cost/schedule impact, cosmetic or optimization | Hardware Lead |
| Moderate | <5% cost impact, no schedule slip, performance neutral | Hardware Lead + Systems Engineer |
| Major | >5% cost impact, schedule risk, or performance change | Hardware Lead + Systems + Program Manager |
| Critical | Safety impact, architecture change, or >15% cost | Full Review Board (as per CDR attendees) |

## 6. ECO Form Template

```
================================================================
ENGINEERING CHANGE ORDER
================================================================

ECO Number:       ECO-XXXX
Date Initiated:   YYYY-MM-DD
Originator:       [Name, Role]
Priority:         [Critical / High / Medium / Low]
Impact Level:     [Minor / Moderate / Major / Critical]

----------------------------------------------------------------
CHANGE DESCRIPTION
----------------------------------------------------------------

Title: [Brief descriptive title]

Current State:
[Describe what exists today]

Proposed Change:
[Describe what will be different]

Rationale:
[Why is this change needed? What problem does it solve?]

----------------------------------------------------------------
AFFECTED ITEMS
----------------------------------------------------------------

Documents Affected:
- [Document path/name] - [Nature of change]
- [Document path/name] - [Nature of change]

Components Affected:
- [RefDes] [Part] - [Add/Remove/Modify]

Interfaces Affected:
- [Interface name] - [Nature of change]

----------------------------------------------------------------
IMPACT ASSESSMENT
----------------------------------------------------------------

Cost Impact:      [None / +$X.XX per unit / -$X.XX per unit]
Schedule Impact:  [None / +X days / +X weeks]
Performance:      [None / Improved / Degraded (specify)]
Safety:           [None / Requires safety review]
EMC:              [None / Requires EMC re-evaluation]
Reliability:      [None / Requires reliability assessment]

Risk Assessment:
[What could go wrong? What is the fallback?]

----------------------------------------------------------------
APPROVAL
----------------------------------------------------------------

Reviewer:         [Name]        Date: ________  Approve / Reject
Reviewer:         [Name]        Date: ________  Approve / Reject
Approver:         [Name]        Date: ________  Approve / Reject

----------------------------------------------------------------
IMPLEMENTATION
----------------------------------------------------------------

Implemented By:   [Name]        Date: ________
Verified By:      [Name]        Date: ________
Closed By:        [Name]        Date: ________

================================================================
```

## 7. ECO Numbering

```
Format: ECO-YYYY-NNN

YYYY = Year of initiation
NNN  = Sequential number within year (001, 002, ...)

Example: ECO-2026-001 (first ECO of 2026)
```

## 8. Turnaround Time Targets

| Priority | Review Complete | Approval | Implementation |
|----------|----------------|----------|----------------|
| Critical | 1 business day | 2 business days | Per plan |
| High | 3 business days | 5 business days | Per plan |
| Medium | 5 business days | 10 business days | Next revision |
| Low | 10 business days | 15 business days | Convenience |

## 9. ECO Status Definitions

| Status | Definition |
|--------|-----------|
| Draft | Being prepared by originator |
| Submitted | Formally submitted for review |
| In Review | Under technical review |
| Approved | Approved, awaiting implementation |
| In Progress | Being implemented |
| Verification | Implementation complete, being verified |
| Closed | Verified and closed out |
| Rejected | Not approved (with rationale documented) |
| Withdrawn | Withdrawn by originator |

---

*ADVIS Hardware Platform - Configuration Management*
