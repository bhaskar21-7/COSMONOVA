# Risk Register

**COSMONOVA — Technical and Scientific Risks**  
*Planetary Analog Intelligence Platform*

> [!NOTE]
> Risks are assessed on Severity (Critical / High / Medium / Low) and include specific mitigations. Review this register before the hackathon and update during the event.

---

## Risk Matrix

| # | Risk | Severity | Likelihood | Mitigation |
|---|------|----------|-----------|------------|
| R1 | **Over-scoping** (6 features × 3 targets × 8 sites) | Critical | High | Enforce MVP scope; use pre-defined cut list; lock scope at H4 |
| R2 | **No ground truth for analogness** | High | Certain | Use positive/negative controls; explicit "not validated" language; no supervised ML |
| R3 | **SRTM gap at high latitudes** (Devon, Iceland, Antarctica) | High | Certain | Use Copernicus GLO-30, ASTER GDEM, ArcticDEM, or REMA instead |
| R4 | **Resolution/baseline mismatch inflating differences** | High | High | Matched-baseline resampling; Monte Carlo error propagation; document mismatch factor |
| R5 | **Spatial autocorrelation understating uncertainty** | High | High | Block bootstrap with variogram-calibrated blocks; never report pixel-level tests |
| R6 | **Weights interpreted as scientific truth** | High | Medium | SMAA with weight ranges; state that weights are normative, not estimated |
| R7 | **Data wrangling consumes the weekend** (PDS formats, HiRISE, CRISM) | High | High | Use derived products and tiles (Trek, QuickMap); skip CRISM/HiRISE in MVP |
| R8 | **Indian-site over-claiming** | High | Medium | Hypothesis language; show negative results if data is weak; distinguish Lonar (published) from Kutch (speculative) |
| R9 | **No Earth analog for PSR cold traps** | Certain | Certain | Report as a finding (Tier D flag), not a tool failure |
| R10 | **Site-level data patchy** (e.g., Bhukosh access) | Medium | Medium | Check access during prep, not at the event; have fallback sites ready |
| R11 | **Rules on pre-built work** | Medium | Low | Read official rules; keep prep limited to environment, data exploration, literature; maintain a dated log |
| R12 | **Team burnout** (48h event) | Medium | Medium | Enforce rest breaks; cap prep hours; define clear handoff points |
| R13 | **Streamlit performance with large rasters** | Medium | Medium | Pre-compute all results; Streamlit serves tiles/summaries, not raw data |
| R14 | **CRS mislabeling** (lunar raster treated as Earth EPSG:4326) | High | Medium | Explicit CRS checks in preprocessing code; IAU sphere definitions |
| R15 | **Dependency conflicts during setup** | Medium | Medium | Test full environment during prep week; pin dependency versions |

---

## Severity Definitions

| Level | Definition |
|-------|-----------|
| **Critical** | Could prevent submission or result in disqualification |
| **High** | Could significantly reduce scientific credibility or demo quality |
| **Medium** | Could reduce quality but is recoverable within the timeline |
| **Low** | Minor inconvenience; unlikely to affect outcome |

---

## Top 5 Risks to Monitor

1. **R1 — Over-scoping**: The single greatest threat. Enforce the cut list.
2. **R7 — Data wrangling time**: Use pre-processed products. Do not spend H4–H16 fighting PDS file formats.
3. **R4 — Resolution mismatch**: Must be addressed in the methodology, not ignored.
4. **R8 — Indian-site claims**: High visibility, high risk if unsupported.
5. **R2 — No ground truth**: Underpins the entire validation approach.

---

*Document status: Pre-hackathon risk assessment. Update likelihood ratings during the event.*
