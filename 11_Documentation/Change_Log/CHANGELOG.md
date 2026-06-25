# ADVIS Hardware Platform - Change Log

## Version Numbering Scheme

```
v{MAJOR}.{MINOR}.{PATCH}

MAJOR: Architectural generation (0 = pre-production development)
MINOR: Significant design milestone
PATCH: Incremental refinement within a milestone
```

---

## v0.4.4 - Architecture Lock (June 2026)

**Status:** A-sample production-intent baseline | Architecture LOCKED

### Changes
- Architecture formally locked via design review gate
- Consolidated handoff document finalized with all technical details
- Safety boundary explicitly defined: ADVIS does not directly actuate brake, steering, throttle or powertrain; ADVIS Assist provides warning/advisory outputs; ADVIS Control may generate safety-supervised actuation request messages over CAN/CAN-FD
- Power sequencing strategy finalized (cascaded enable with PG signals)
- Watchdog strategy locked: TPS3431 with boot-gated enable
- All component selections baselined with manufacturer part numbers
- Connector pinout intent documented (pending mechanical validation)
- SOM signal map finalized for all interfaces
- Ground domain star-point topology defined
- IR daughterboard interface specification complete
- Open items list formalized with owners and due dates

### Locked Items
- Power tree topology (LM61460 -> TPS62130A -> TLV75518)
- Camera architecture (single DS90UB954-Q1, dual VC)
- SOM interface assignments (CSI-2, SPI, I2C, UART, GPIO)
- Input protection topology (PMOS + TVS + fuse)
- CAN transceiver selection and mode (TCAN1044AV-Q1, Normal Mode)

---

## v0.4.0 - Near-Final Architecture (May 2026)

**Status:** Pre-lock review candidate

### Changes
- Safety boundary established: ECU generates actuation REQUESTS, not commands
- ASIL decomposition analysis completed (QM hardware + ASIL application)
- Reset/watchdog topology finalized (TPS3808G33 supervisor + TPS3431 WDT)
- SOM_BOOT_OK handshake mechanism defined for watchdog gating
- CAN transceiver operational mode locked to Normal Mode (STB=LOW)
- TXD recessive pull-up strategy defined (10k to 3V3_CAN)
- USB-C device mode confirmed with 5.1k CC pull-downs
- MicroSD interface added for field diagnostics and log storage
- Debug UART access defined (3-pin header, 115200 baud)

### Decisions
- Rejected ASIL-B hardware classification (observation ECU does not require)
- Confirmed single CAN channel sufficient for advisory/logging role
- Deferred Automotive Ethernet to High tier / future variants

---

## v0.3.5 - Interface Definitions (April 2026)

**Status:** Interface specification complete

### Changes
- All SOM-to-peripheral interfaces defined (bus type, speed, addressing)
- I2C address map established (DS90UB954=0x30, NEO-M9N=0x42)
- SPI bus assignment for BMI088 (dual chip-select architecture)
- GNSS interface selection: UART primary (NMEA/UBX), I2C secondary
- 1PPS timing interface from GNSS to SOM GPIO
- Ground domain strategy defined (PGND / DGND / AGND with star points)
- Antenna bias-T topology for active GNSS antenna
- FPD-Link III PoC (Power over Coax) specification confirmed
- Virtual channel mapping: VC0=Forward, VC1=DMS

### Decisions
- Selected SPI over I2C for BMI088 (higher throughput, lower latency)
- UART selected as primary GNSS interface (standard NMEA compatibility)
- Single star-point ground topology chosen over split-plane approach

---

## v0.3.0 - Key Component Selections (March 2026)

**Status:** Critical component selections finalized

### Changes
- DS90UB954-Q1 selected for dual FPD-Link III deserialization
- LM61460-Q1 selected as primary buck converter (12V to 5V, 6A)
- TPS62130A-Q1 selected for 3.3V generation (5V to 3.3V)
- TLV75518-Q1 selected for 1.8V LDO (low-noise for analog/RF)
- TPS3808G33-Q1 selected as voltage supervisor
- TPS3431-Q1 selected as external watchdog timer
- TCAN1044AV-Q1 selected for CAN-FD interface
- NEO-M9N-00B selected for multi-constellation GNSS
- BMI088 selected for 6-axis IMU (automotive vibration performance)
- 80V PMOS selected for reverse-polarity protection
- Power tree trade study completed and documented (TN-001)

### Decisions
- Discrete power topology preferred over integrated PMIC (flexibility, sourcing)
- Single deserializer (DS90UB954) preferred over dual DS90UB933 (BOM reduction)
- External watchdog preferred over SOM-internal only (independence requirement)

---

## v0.2.0 - Architecture Exploration (February 2026)

**Status:** Architecture options evaluated

### Changes
- SoC candidates evaluated: TDA4VM, AM68A, SA8295, S32V, V3H
- TDA4VM/AM68A class selected as baseline (performance/power/ecosystem balance)
- Phytec phyCORE-AM68A SOM selected as compute module
- Two-track hardware strategy defined:
  - Track 1: Compact production module (cost-down, minimal connectors)
  - Track 2: Modular IP platform (SoC-adaptive, OEM-configurable)
- Camera architecture options evaluated (FPD-Link III vs direct MIPI vs GMSL2)
- FPD-Link III selected for Track 2 (cable length, PoC, TI ecosystem)
- Power architecture options evaluated (single buck, cascaded, PMIC, hybrid)
- Product family defined: Assist, Control, Fleet, Fusion variants
- SoC tier structure established: Entry (AM62A), Mid (AM68A/TDA4VM), High (TDA4VH)

### Decisions
- SOM-based design preferred over custom SoC integration (time-to-market, risk)
- Modular platform approach enables multiple products from single carrier PCB
- FPD-Link III for IP platform; direct MIPI as production cost-down option

---

## v0.1.0 - Initial Concept (January 2026)

**Status:** Concept exploration

### Changes
- Project initiated: vehicle-mounted ADAS + DMS edge compute ECU
- Target market: OEM Tier-1 supply, aftermarket fleet
- Core use cases defined: forward collision warning, lane departure, driver monitoring
- Preliminary requirements captured from target OEM discussions
- Form factor targets: compact automotive module, single vehicle connector
- Environmental requirements baselined: -40C to +85C, IP54, ISO 16750
- Initial cost targets established per tier (Entry/Mid/High)
- Patent strategy initiated (adaptive power sequencing, single-connector integration)
- Platform scalability requirement: single carrier design spanning Entry to High tier

### Decisions
- Combined ADAS+DMS in single ECU (vs separate boxes) for cost and integration
- Linux-based software stack (vs AUTOSAR Classic) for AI/ML flexibility
- Observation-only safety concept to avoid ASIL hardware requirements

---

*ADVIS Hardware Platform - Configuration Management*
