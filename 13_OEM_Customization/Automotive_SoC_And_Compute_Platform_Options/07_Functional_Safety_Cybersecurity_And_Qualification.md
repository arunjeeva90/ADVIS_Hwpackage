# Functional Safety, Cybersecurity and Qualification

## 1. Terms that must not be mixed

| Term | Meaning |
|---|---|
| AEC-Q100 | Component stress qualification; not a functional-safety certification |
| ISO 26262 development | Product/process developed under automotive functional-safety practices |
| ASIL capability | Hardware/software may support a system safety goal under assumptions |
| ASIL-certified software | Specific component/version evaluated to a defined scope |
| ASIL-B ECU | Complete item safety case, not created by buying one ASIL-capable SoC |
| ISO 21434 | Automotive cybersecurity engineering process and work products |

## 2. Required SoC evidence

Request:

- safety manual
- FMEDA and diagnostic coverage assumptions
- dependent-failure analysis guidance
- fault-injection guide
- safety mechanism list and test interfaces
- lockstep/ECC/parity coverage
- clock/power/temperature monitors
- safety island isolation
- reset and recovery strategy
- MCAL/RTOS qualification certificates
- compiler/tool confidence evidence
- errata classification and safety impact
- lifecycle and safety-document maintenance commitment

## 3. Cybersecurity requirements

Minimum:

- immutable hardware root of trust
- secure boot with anti-rollback
- key derivation/storage
- debug authentication and production lock
- authenticated/encrypted update
- secure diagnostics
- memory/firewall isolation
- cryptographic acceleration
- true random number generator
- vulnerability and incident-response process
- SBOM and CVE handling
- lifecycle security updates

## 4. Prototype versus production

| Platform | Permitted use |
|---|---|
| Automotive SoC + safety BSP | production candidate after item-level safety case |
| AEC-Q100 accelerator + non-safety host | engineering candidate; system safety gap remains |
| Industrial SoM using automotive-grade IC | prototype or productization base; board qualification remains |
| Consumer SBC | model and integration prototype only |
| Closed full-stack ADAS | production through supplier programme, but limited ADVIS software ownership |

## 5. Exact-part rule

Never accept a family-level claim. Record:

- orderable part number
- silicon revision
- temperature grade
- package
- safety variant
- PMIC
- DDR type and ECC mode
- BSP/MCAL release
- compiler version
- safety document revision
- EOL/PCN terms

## 6. ADVIS safety boundary

For warning and request-capable products:

- perception can remain QM only if the safety architecture and item definition justify it
- independent monitors shall validate timing, data age, calibration, vehicle plausibility and output permissions
- DMS may alter warning escalation but must not suppress valid independent road protection
- actuation requests require OEM arbitration, vehicle-dynamics limits and a released vehicle-level safety case
