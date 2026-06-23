# ADVIS Design Review Process

## 1. Purpose

This document defines the formal design review process for the ADVIS hardware platform. Design reviews are mandatory quality gates that ensure technical correctness, manufacturing readiness, and compliance with requirements before advancing to the next development phase.

## 2. Review Types

### 2.1 Concept Design Review (CDR)

| Attribute | Definition |
|-----------|-----------|
| **Trigger** | Architecture definition complete |
| **Inputs** | System requirements, block diagrams, component trade studies |
| **Gate Criteria** | Architecture viable, major risks identified, BOM cost target achievable |
| **Output** | Approved architecture for schematic entry |

### 2.2 Schematic Design Review (SDR)

| Attribute | Definition |
|-----------|-----------|
| **Trigger** | Schematic capture complete, ERC clean |
| **Inputs** | Schematic sheets, netlist, BOM, ERC report |
| **Gate Criteria** | No ERC errors, all component values defined, power tree verified |
| **Output** | Approved schematic for layout |

### 2.3 Layout Design Review (LDR)

| Attribute | Definition |
|-----------|-----------|
| **Trigger** | PCB layout complete, DRC clean |
| **Inputs** | Gerbers, drill files, stackup, DFM report, impedance report |
| **Gate Criteria** | DRC clean, impedance targets met, thermal analysis pass |
| **Output** | Approved layout for fabrication |

### 2.4 Pre-Production Review (PPR)

| Attribute | Definition |
|-----------|-----------|
| **Trigger** | A-sample validation complete |
| **Inputs** | Test results, failure analysis, ECO list, updated BOM |
| **Gate Criteria** | All critical tests passed, known issues documented with workarounds |
| **Output** | Approved for B-sample / pilot production |

## 3. Attendee Roles

| Role | Responsibility | Required/Optional |
|------|---------------|-------------------|
| Design Owner | Present design, answer technical questions | Required |
| Reviewer (Peer) | Technical critique, identify errors/risks | Required (min 2) |
| Review Chair | Facilitate, ensure coverage, document decisions | Required |
| Systems Engineer | Verify requirements coverage | Required |
| Manufacturing Rep | DFM/DFA assessment | Required (LDR, PPR) |
| Quality Engineer | Process compliance verification | Required (PPR) |
| Project Manager | Schedule/cost impact assessment | Optional |

## 4. Review Process

### 4.1 Pre-Review (5 business days before)

1. Design owner distributes review package to all attendees
2. Attendees perform individual review and submit written comments
3. Review chair consolidates comments and prepares agenda

### 4.2 During Review

1. Design owner presents key design decisions (30 min max)
2. Structured walk-through of review checklist items
3. Discussion of pre-submitted comments
4. Each issue classified: Critical / Major / Minor / Enhancement
5. Action items assigned with owner and due date

### 4.3 Post-Review

1. Review chair publishes meeting minutes within 2 business days
2. Action items tracked to closure
3. Re-review required if any Critical items found
4. Sign-off collected from all required attendees

## 5. Issue Classification

| Severity | Definition | Gate Impact |
|----------|-----------|-------------|
| Critical | Design will not function or poses safety risk | BLOCKS gate passage |
| Major | Significant performance/reliability concern | Must resolve before gate |
| Minor | Cosmetic or minor optimization opportunity | Track, resolve by next review |
| Enhancement | Suggestion for future improvement | Log for consideration |

## 6. Checklist Requirements

Each review type has a mandatory checklist (stored in 02_Schematic/Review_Checklists/ and 03_PCB_Layout/DFM_Reports/). The checklist must be completed before the review meeting begins.

## 7. Sign-Off Authority

| Review Type | Approvers Required |
|-------------|-------------------|
| CDR | Hardware Lead + Systems Engineer |
| SDR | Hardware Lead + Peer Reviewer + Systems Engineer |
| LDR | Hardware Lead + Layout Lead + Manufacturing Rep |
| PPR | Hardware Lead + Quality + Manufacturing + Program Manager |

## 8. Records Retention

All review records, action items, and sign-off forms are retained in this folder (11_Documentation/Design_Reviews/) with the naming convention:

```
{ReviewType}_{Version}_{Date}_Record.md
```

Example: `SDR_v0.4.4_2026-06-15_Record.md`

---

*Document Version: 1.0 | ADVIS Hardware Platform*
