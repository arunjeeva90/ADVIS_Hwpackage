# 06 - Patent Strategy

## Purpose

This folder contains the intellectual property strategy for the IND-VIAS platform, including invention disclosures, prior art research, patent claim drafts, and filing timelines.

## Sub-folders

| Folder | Contents |
|--------|----------|
| Invention_Disclosures/ | Formal invention disclosure forms for each patentable concept |
| Prior_Art_Search/ | Prior art search reports, patent landscape analysis |
| Claim_Drafts/ | Draft patent claims for attorney review |
| Design_Patents/ | Design patent applications (form factor, connector system, enclosure) |
| Utility_Patents/ | Utility patent applications (methods, architectures, algorithms) |
| Trade_Secrets_Register/ | Catalog of trade-secret-protected IP elements |
| Freedom_To_Operate/ | FTO analysis ensuring our designs don't infringe existing patents |
| Patent_Landscape_Maps/ | Visual maps of competitive patent positions |
| Filing_Timeline/ | Filing schedule, provisional deadlines, priority dates |

## Patent-Worthy Concepts Identified (v0.4.4)

### Utility Patent Candidates

1. **Auto-adapting power sequencing** - Carrier board that detects SoM power profile and adjusts regulator enable sequencing without hardware modification
2. **Single-connector vehicle integration** - Hybrid connector carrying power, data, and coax camera links in one sealed automotive unit
3. **Runtime-configurable PoC network** - Digitally adjustable Power-over-Coax parameters based on detected camera module identity
4. **Watchdog-gated peripheral activation** - Safety architecture where peripherals activate only after firmware health confirmation
5. **SoM identity auto-configuration** - Hardware platform that reads module identity at boot and reconfigures carrier subsystems accordingly

### Design Patent Candidates

1. ECU form factor and enclosure design
2. Modular SoM blade connector system
3. Single-cable harness connector industrial design

### Trade Secret Elements

1. Carrier-to-SoM proprietary pinout specification
2. Optimized high-speed signal routing topology
3. Platform configuration database and variant generation method

## Process

1. Engineer identifies patentable concept during design
2. Invention Disclosure form completed and filed here
3. Prior art search performed and documented
4. Decision: Utility patent / Design patent / Trade secret
5. Claim drafts prepared for patent attorney review
6. Filing timeline established based on priority and budget

## Important Notes

- File provisional patent applications BEFORE any public disclosure
- 12-month grace period (US only) from first public disclosure - do not rely on this
- All invention disclosures should be timestamped and witnessed
- Keep trade secrets OUT of any public-facing documentation
