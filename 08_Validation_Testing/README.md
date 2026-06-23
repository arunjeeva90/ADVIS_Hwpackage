# 08 - Validation & Testing

## Purpose

Test plans, procedures, and results for hardware validation across all domains: power integrity, signal integrity, EMC, environmental, and functional testing.

## Sub-folders

| Folder | Contents |
|--------|----------|
| Power_Integrity/ | Rail voltage accuracy, ripple, transient response, load regulation |
| Signal_Integrity/ | Eye diagrams, jitter, crosstalk for high-speed interfaces |
| EMC_EMI/ | Conducted/radiated emissions, immunity, bulk current injection |
| Environmental_Qualification/ | Temperature, humidity, vibration, shock per automotive standards |
| Functional_Test_Plans/ | Subsystem and system-level functional test procedures |
| DVT_Reports/ | Design Verification Test reports |
| Reliability_Testing/ | HALT, HASS, accelerated life testing |

## Key Test Points

| Test | Pass Criteria | Standard |
|------|---------------|----------|
| Input voltage range | 6V to 36V continuous, 40V load dump | ISO 7637-2 |
| Reverse polarity | No damage at -16V | OEM-specific |
| 5V rail accuracy | 5.0V +/- 2% at full load | Internal |
| CSI-2 eye diagram | Open eye at 1.5 Gbps/lane minimum | MIPI D-PHY |
| CAN-FD compliance | ISO 11898-2, 5 Mbps data phase | ISO 11898 |
| Operating temperature | -40C to +85C (T_ambient) | AEC-Q100 Grade 2 |
