# Patent Claim Drafting Guidelines

## Purpose

This document provides guidelines for drafting patent claims for the ADVIS platform invention disclosures. Claims are the legal definition of what the patent protects; they must be precise, supported by the specification, and drafted to maximize protection while maintaining validity.

---

## General Principles

### Claim Structure

1. **Preamble**: Identifies the category of invention (method, system, apparatus, medium)
2. **Transitional phrase**: "comprising" (open-ended), "consisting of" (closed), "consisting essentially of" (semi-closed)
3. **Body**: Lists elements and their relationships

### Recommended Transitional Phrase

Use **"comprising"** for all independent claims unless there is a specific reason to limit scope. "Comprising" allows the claim to cover implementations that include additional unlisted elements.

---

## Independent Claim Strategy

### Three Independent Claims Per Disclosure

Each ADVIS invention disclosure should have at least three independent claims:

| Claim Type | Purpose | Typical Preamble |
|-----------|---------|------------------|
| Method claim | Protects the process/algorithm | "A method of..." |
| System/Apparatus claim | Protects the physical implementation | "A system comprising..." or "An apparatus comprising..." |
| Computer-readable medium | Protects the software implementation | "A non-transitory computer-readable medium storing instructions..." |

### Independent Claim Drafting Rules

1. **Breadth**: Draft as broadly as possible while maintaining novelty over prior art
2. **Minimalism**: Include only the elements essential to distinguish over prior art
3. **Functional language**: Describe what elements DO, not specific implementation details
4. **Avoid trade secrets**: Never include specific values, thresholds, or implementation recipes
5. **Safety boundary**: For actuation-related claims, always specify "generating a request" not "actuating"

---

## Dependent Claim Strategy

### Purpose of Dependent Claims

- Add specificity without narrowing the independent claim
- Provide fallback positions if independent claim is narrowed during prosecution
- Cover preferred embodiments and commercial implementations
- Create claim differentiation for broader portfolio licensing

### Dependent Claim Hierarchy

```
Independent Claim 1 (broadest)
  |
  +-- Dependent Claim 4 (adds element A)
  |     |
  |     +-- Dependent Claim 8 (adds element A + B)
  |
  +-- Dependent Claim 5 (adds element C)
  |
  +-- Dependent Claim 6 (adds element D)
```

### Recommended Dependent Claims Per Disclosure

- Minimum: 8-10 dependent claims per independent claim
- Optimal: 12-15 dependent claims across all independent claims
- Coverage: Each key feature variant should have at least one dependent claim

---

## Automotive-Specific Claim Language

### Do Use

| Term | Context |
|------|---------|
| "vehicle" | Generic term covering cars, trucks, buses |
| "automotive electronic control unit" | General ECU reference |
| "vehicle communication bus" | Generic for CAN, CAN-FD, Ethernet |
| "generating a request" | For safety-supervised outputs |
| "camera sensor" or "image sensor" | For camera hardware |
| "processor" | Generic computing element |
| "non-transitory computer-readable medium" | For software claims |

### Do NOT Use

| Term | Risk | Alternative |
|------|------|-------------|
| "CAN bus" (in independent claims) | Limits to one protocol | "vehicle communication bus" |
| "TDA4VM" or specific SoC names | Limits to one chip | "processor" or "system-on-chip" |
| "MIPI CSI-2" (in independent claims) | Limits to one interface | "serial image data interface" |
| "directly actuating" | Safety boundary violation | "generating an actuation request" |
| "ASIL-D" or specific safety ratings | Overclaims safety level | "safety-supervised" |
| Specific threshold values | Trade secret exposure | "predetermined threshold" |
| Brand names | Unnecessary limitation | Generic functional terms |

---

## Means-Plus-Function Considerations

### When to Use 35 USC 112(f) Language

Means-plus-function claiming ("means for...") is interpreted narrowly (limited to disclosed structure and equivalents). Use sparingly and only when:

- The structural implementation is truly secondary to the function
- Broad structural language would be too vague
- Competitor design-arounds are likely to use different structure for same function

### Preferred Alternative

Instead of "means for detecting module identity," write:
"an identification detection circuit configured to determine an identity of an installed module"

This provides functional claim language without triggering means-plus-function interpretation.

---

## Avoiding Prosecution History Estoppel

### During Drafting

1. Do not include limitations you will later need to remove
2. Draft claims at multiple levels of specificity (broad independent, narrow dependent)
3. Avoid unnecessary negative limitations ("without" or "not")
4. Include support in the specification for broader interpretations

### Claim Amendments to Avoid

- Narrowing amendments that surrender equivalents
- Adding limitations from the specification that were not originally claimed
- Accepting examiner's characterization of the invention without careful review

---

## ADVIS-Specific Claim Considerations

### Safety Boundary (Critical)

ALL claims that involve vehicle actuation MUST include language establishing that:
- ADVIS generates safety-supervised actuation REQUESTS
- Final actuator authority remains with OEM vehicle ECU
- The ADVIS system does not directly control vehicle brakes, steering, or throttle

**Example language:**
"...generating an actuation request and transmitting said request to a vehicle electronic control unit, wherein said vehicle electronic control unit retains final authority over vehicle actuation."

### Trade Secret Protection (Critical)

Claims must NEVER disclose:
- Specific numerical thresholds or calibration values
- Exact pinout configurations
- PCB routing rules or layer assignments
- Model training parameters or dataset descriptions
- EMI mitigation specific recipes

**Use instead:** "predetermined threshold," "configured according to a stored profile," "based on calibration parameters stored in memory"

### Multi-SoC Platform Claims

When claiming the adaptive platform:
- Claim the method of detection and adaptation generically
- Do not specify the number of supported SoC variants
- Use "plurality of" to keep scope open
- Reference "module connector interface" generically

---

## Claim Review Checklist

Before submitting claims for attorney review:

- [ ] Each independent claim covers a distinct statutory category (method, system, medium)
- [ ] No trade secrets appear in any claim language
- [ ] Safety boundary language present in all actuation-related claims
- [ ] "Comprising" used as transitional phrase (unless intentionally closed)
- [ ] No unnecessary brand names or specific part numbers
- [ ] Dependent claims form a logical hierarchy
- [ ] At least 10 dependent claims per disclosure
- [ ] Claims are supported by the specification (every element described somewhere)
- [ ] No means-plus-function language unless intentional
- [ ] Claims readable by a person skilled in the art without ambiguity

---

## Prosecution Strategy Notes

### Expected Office Actions

- Likely rejections under 35 USC 103 (obviousness) combining multiple references
- Prepare responses showing non-obvious combination (teaching away, unexpected results)
- Dependent claims provide fallback positions for narrowing if needed

### Interview Strategy

- Request examiner interview after first Office Action
- Present claim charts showing novelty over applied references
- Be prepared to amend to dependent claim scope if independent too broad

---

**Document Version:** 1.0  
**Last Updated:** 2025-01  
**Classification:** CONFIDENTIAL - Attorney-Client Privilege
