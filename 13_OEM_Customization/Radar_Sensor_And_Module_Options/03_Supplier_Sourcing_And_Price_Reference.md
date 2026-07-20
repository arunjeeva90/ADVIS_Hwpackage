# Supplier Sourcing and Price Reference

## Interpretation rules

- Prices were observed during the scan on **20 July 2026**.
- GST, freight, customs, harnesses, adapters, software licences, NRE and calibration may be excluded.
- Tier-1 production radars are normally sold only through OEM/Tier-1 programmes; lack of public price is normal.
- Grey-market OEM radars may be locked to a vehicle, contain undocumented firmware, need wake/config messages, or lack a compatible CAN database.
- Alibaba/Made-in-China listings must be treated as leads, not validated specifications.
- A complete aftermarket warning kit may be cheaper than an open smart radar because it exposes only an alarm output and hides the object data.

## Observed listings

| Product | Item_Type | Seller_Platform | Region | Price_Seen | MOQ | Status | Risk_Interpretation | Product_Link |
|---|---|---|---|---|---|---|---|---|
| Texas Instruments AWR1843BOOST | Automotive radar EVM | Digi-Key India | India | ₹45,693.69 | 1 | Observed July 2026 | Development board only; no enclosure/automotive connector | https://www.digikey.in/en/products/detail/texas-instruments/AWR1843BOOST/8125054 |
| Texas Instruments IWR1843BOOST | Industrial mmWave EVM | Digi-Key India | India | ₹37,089.50 | 1 | Observed July 2026 | Good radar learning board; industrial prefix and exposed EVM | https://www.digikey.in/en/products/detail/texas-instruments/IWR1843BOOST/8125053 |
| Texas Instruments AWR2944EVM | 4Tx4Rx automotive radar EVM | Digi-Key catalog | India/global | ₹74,302.82 | 1 | Observed July 2026 | Powerful corner/imaging development platform; requires productization | https://www.ti.com/tool/AWR2944EVM |
| NXP S32R294 RADB | Radar processor development board | NXP | Global | US$1,400 | 1 | Public board price | Radar processor board only; transceiver/antenna kit separate | https://www.nxp.com/design/design-center/development-boards-and-designs/S32R294-RADB |
| NXP S32R41 EVB | Radar processor development board | NXP | Global | US$1,400 | 1 | Public board price | Complete TEF82 radar setup costs more and may require NDA | https://www.nxp.com/design/design-center/development-boards-and-designs/S32R41-EVB |
| Acconeer XE125 | 60 GHz XM125 evaluation board | Mouser India | India | ₹11,283.17 | 1 | 128 in stock when observed | Near-field/cabin/parking research; not road ADAS | https://www.mouser.in/ProductDetail/Acconeer/XE125 |
| OmniPreSense OPS243-C | 24 GHz FMCW range/speed/direction sensor | OmniPreSense | USA/global | US$244 | 1 | Direct retail | Easy universal interface; not automotive-grade road object radar | https://omnipresense.com/product/ops243-c-fmcw-radar-sensor/ |
| OmniPreSense OPS243-A | 24 GHz Doppler speed/direction sensor | OmniPreSense | USA/global | US$224 | 1 | Direct retail | No multi-object ranging or angular perception | https://omnipresense.com/product/ops243-a-doppler-radar-sensor/ |
| Continental ARS408-21 | 250 m smart radar sensor | SensorLidar reseller | Global | US$499.10–575.90 depending option | 1 | In stock listing | Check originality, firmware, harness and CAN database | https://www.sensorlidar.com/products/for-automotive-front-collision-warning-autonomous-emergency-braking-77ghz250m-ars408-21-germany-millimeter-wave-radar-sensor |
| Continental ARS408-21 | Grey-market/new/used listings | Ruten marketplace | Taiwan | TWD 13,200–43,000 typical; extreme outliers exist | 1 | Observed marketplace range | High authenticity and firmware risk; use only with serial/firmware verification | https://www.ruten.com.tw/find/?q=ars408-21 |
| Generic 77 GHz front FCW radar | Complete front collision module/system | Alibaba | China | US$155–160 typical | 1 | Public marketplace | Supplier claims require bench/road validation; request object-list protocol | https://www.alibaba.com/showroom/77ghz-radar.html |
| Nanoradar / generic 77 GHz FCW | Front collision radar | Alibaba | China | US$255 typical sample listing | 1 | Public marketplace | Confirm exact Nanoradar model, firmware, CAN ICD, lens/radome and support | https://www.alibaba.com/showroom/77ghz-radar.html |
| Generic 77 GHz BSD radar | Single or dual blind-spot kit | Alibaba | China | US$70–150 | 1–2 | Public marketplace | Usually proprietary warning outputs, not open object data | https://www.alibaba.com/showroom/77ghz-blind-spot-radar.html |
| Generic single 77 GHz BSM system | Aftermarket radar system | Alibaba | China | US$95 (1–9); $90 (10–99); $85 (100+) | 1 | Public product listing | Use for HMI/packaging demonstration only until protocol and qualification are proven | https://www.alibaba.com/product-detail/77GHz-Millimeter-Wave-Radar-Blind-Spot_1601085733425.html |
| RoadPassion two-radar kit | BSD/LCA/DOW/RCTA aftermarket kit | Alibaba | China | ₹13,769.49 (1–9); ₹13,199.72 (10–99); ₹12,819.87 (100+) | 1 | Observed INR-converted listing | Closed kit; radar object access and safety evidence uncertain | https://www.alibaba.com/product-detail/77GHz-Millimeter-Wave-Radar-Blind-Spot_1601085733425.html |
| Generic 77 GHz data-output radar | Smart radar/data logger module | Alibaba | China | US$72–130 | 1 | Public marketplace | Request raw/object data format, update rate, timestamping and target limits | https://www.alibaba.com/showroom/77ghz-radar.html |
| Generic 77 GHz safety/obstacle radar | Enclosed module | Alibaba | China | US$80–110 | 1 | Public marketplace | Often robotics/off-highway rather than homologated automotive | https://www.alibaba.com/showroom/77ghz-radar.html |
| DFRobot C4001 12 m | 24 GHz FMCW I2C/UART module | DFRobot | Global | US$12.90; $11.90 at 10+ | 1 | Direct retail | Human-presence/bench module; explicitly not exterior ADAS | https://www.dfrobot.com/product-2795.html |
| DFRobot C4001 25 m | 24 GHz FMCW UART module | DFRobot | Global | US$13.90 | 1 | Direct retail | Cheap range/speed learning; no useful road object angle/classification | https://www.dfrobot.com/product-2793.html |
| DFRobot SEN0395 | 24 GHz human-presence radar | DFRobot | Global | US$29 | 1 | Direct retail | Presence output only; not ADAS radar | https://www.dfrobot.com/product-2282.html |

## Price-band interpretation

| Approximate sample price | What is usually available | ADVIS interpretation |
|---:|---|---|
| `< US$30` | 24/60 GHz human-presence or maker module | Interface/HMI/cabin/near-field learning only |
| `US$70–160` | Marketplace BSD/FCW kit or generic enclosed radar | Packaging and warning demo; qualification and object ICD usually weak |
| `US$200–600` | Better development radar, ARS408-class reference, OPS243 or supplier sample | Useful PoC if data interface is open |
| `US$700–2,000+` | Automotive radar processor/Ethernet reference system | Custom radar development, not recurring production cost |
| `RFQ/OEM nomination` | Current Bosch/Continental/Aptiv/ZF/Valeo/Magna, imaging radar, automotive startups | Production or premium programme path |

## Marketplace purchase rules

Before buying, obtain:

1. Product and firmware part number.
2. Video showing live object data, not only an LED/buzzer.
3. Full CAN/CAN-FD DBC or Ethernet ICD.
4. Object count, update rate, timestamp and latency.
5. Range/FoV modes and target-RCS definition.
6. Power, connector and pinout.
7. Mounting and radome requirements.
8. Temperature/IP/EMC evidence.
9. Sample return policy.
10. Written statement on lifecycle, MOQ, NRE and customization.

## Used OEM radar warning

Used Bosch/Continental/Denso/Aptiv corner radars can be inexpensive donor devices, but they are frequently unsuitable for ADVIS because:

- CAN messages may be proprietary or gateway-authenticated.
- Calibration and vehicle coding may be required.
- Radar firmware may suppress output without OEM network messages.
- Sensor mounting and fascia calibration differ by vehicle.
- No supplier safety support or lifecycle exists.

Use them only for reverse engineering or bench education, not as the baseline product.
