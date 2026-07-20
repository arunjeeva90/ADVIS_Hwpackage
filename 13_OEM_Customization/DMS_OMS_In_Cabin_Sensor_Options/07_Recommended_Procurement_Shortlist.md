# Recommended Procurement Shortlist

| Objective | Sensor / module | Why | Action |
| --- | --- | --- | --- |
| Production cost-first DMS | OX01H1B | 1.5 MP mono GS, Nyxel NIR, mature automotive path | Primary RFQ baseline; ask for MIPI and SerDes module options |
| Production future cost-first DMS | OX01N1B | Newer 1.5 MP mono GS, 36% NIR QE, ASIL-B/cyber | Track sample/MP timing; do not freeze until module supply is real |
| Production non-OV second source | VB56G4A / VB56G6A | Excellent 940 nm efficiency and automotive credibility | Compare IR power, module cost and ST safety package |
| Production low-cost onsemi | AR0144AT | Simple 1 MP GS automotive DMS | Request exact automotive module; compare against OX01H1B |
| Production China-source | SC233AT | 2.3 MP BSI GS, HDR, built-in ISP, AEC-Q100 G2/ASIL-B | Strong RFQ candidate; validate image quality and support |
| Technical validation RGB-IR | OV2312 | 2 MP RGB-IR GS with many custom module listings | Best bridge from PoC to production concepts |
| Technical validation mono | OV2311 | 2 MP, 3 µm mono GS, strong gaze/eye fit | Use as high-quality NIR benchmark |
| Fast industrial validation | AR0234CS | 2.3 MP 120 fps GS and broad USB/MIPI ecosystem | Excellent for motion/head/eye testing, not production safety |
| Cheapest universal DMS PoC | OV9281 USB-UVC NoIR | 1 MP mono GS; ~US$23–25, Linux UVC | Best immediate purchase for SoC-agnostic PoC |
| Cheapest color GS PoC | OV9782 | 1 MP color GS; low-cost MIPI modules | Use when phone/hand/cabin color context matters |
| Cheapest rolling-shutter night demo | OV9732 NoIR | 720p, often US$6–21 | Acceptable only for low-cost software demo |
| India-local NoIR demo | IMX219 NoIR | Widely available around ₹1,565–1,945 | Raspberry Pi / supported CSI only; not global shutter |
| Premium whole-cabin OMS | OX05C1S | 5 MP GS-HDR RGB-IR | Future premium benchmark |
| Premium whole-cabin OMS alternative | IMX775 | 5 MP RGB-IR hybrid, high 940 nm sensitivity | Track 2026 module readiness |
| Premium China-source OMS | SC533AT | 5 MP automotive RGB-IR GS | Evaluate cost and module partner |
| Premium ST OMS | VB1940 / VD1940 | 5.1 MP RGB-NIR hybrid GS/RS | Strong full-cabin architecture option |

## Immediate purchase recommendation

For a compute-platform-independent first DMS prototype:

1. Buy **two OV9281 monochrome USB-UVC NoIR cameras** from different suppliers.
2. Buy one **850 nm illuminator** for easiest algorithm bring-up.
3. Add a **940 nm illuminator** for production-relevant comparison.
4. Use a **60–80° HFOV M12 lens**, not the extreme 149–166° lenses commonly advertised.
5. In parallel, obtain an **OV2312 RGB-IR MIPI sample** and an **AR0234CS USB/MIPI sample**.
6. Start automotive RFQs for **OX01H1B, AR0144AT, VB56G4A and SC233AT**.

## Decision recommendation

- **Driver-only cost product:** 1–1.5 MP mono global shutter, strong 940 nm NIR.
- **Driver + cabin context:** 2–3 MP RGB-IR global shutter.
- **Whole-cabin OMS:** 5 MP RGB-IR / RGB-NIR with HDR and wide-angle optics.
