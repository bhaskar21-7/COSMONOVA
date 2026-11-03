# Martian Environments

**Target Profiles for Analog Comparison**

> [!NOTE]
> These are reference descriptions of Martian environments, drawn from published literature. They should be treated as **target profiles to be quantified from data during the hackathon**, not as hard-coded values. Mars is a stretch goal for the hackathon MVP.

---

## Primary Reference Sites

### Jezero Crater
- **Diameter**: ~45 km
- **Location**: Syrtis Major region
- **Landing**: Perseverance rover, February 2021
- **Scientific targets**: Ancient delta and lake system; deltaic sediments, carbonates, olivine-rich units
- **Analog interest**: Deltaic morphology, lacustrine sediments, carbonate mineralogy

### Gale Crater
- **Diameter**: ~150 km
- **Feature**: Central mound (Mount Sharp / Aeolis Mons) of layered sedimentary deposits
- **Landing**: Curiosity rover, August 2012
- **Scientific targets**: Layered stratigraphy, clay minerals, sulfates
- **Analog interest**: Sedimentary stratigraphy, sulfate/clay mineralogy, thermal cycling

---

## Atmospheric and Thermal Conditions

- **Mean surface pressure**: ~600 Pa (~0.6% of Earth sea level)
- **Composition**: ~95% CO₂, ~2.7% N₂, ~1.6% Ar
- **Temperature**: Highly variable; at Gale Crater, diurnal swings of tens of K per sol with seasonal extremes
- **Key reference**: Martínez, G. M. et al. (2017). The modern near-surface Martian climate. *Space Sci. Rev.* 212.

> [!IMPORTANT]
> Earth's atmospheric pressure at the highest plateaus (~50–60 kPa) is still ~100× Mars surface pressure. **No Earth location reproduces Martian atmospheric conditions.** This is a Tier D mismatch.

---

## Soil Chemistry

- **Perchlorates**: Detected at the Phoenix landing site (Hecht et al. 2009, *Science* 325)
- **Sulfates**: Abundant at several landing sites; indicators of past water activity
- **Clays**: Detected by CRISM from orbit and confirmed in situ
- **Analog relevance**: Any Earth site claiming "Mars-like soil" must specify which soil property and at what depth. Perchlorate-bearing soils exist on Earth (e.g., Atacama) but context differs.

---

## Volcanic and Geomorphic Features

- **Tharsis province**: Massive shield volcanoes (Olympus Mons, Tharsis Montes)
- **Lava plains**: Extensive basaltic flows
- **Dune fields**: Active aeolian processes observed
- **Alluvial fans and deltas**: Evidence of past fluvial activity
- **Implications**: Each feature type implies a different analog objective — basaltic volcanism, aeolian transport, fluvial geomorphology

---

## Key Datasets for Mars Targets

| Dataset | Instrument | Measures | Resolution |
|---------|-----------|----------|------------|
| MOLA | MGS laser altimeter | Global elevation | ~460 m/px |
| MOLA–HRSC blend | USGS Astrogeology | Elevation | ~200 m/px |
| CTX | MRO camera | Imagery; site DTMs | ~6 m/px |
| HiRISE | MRO camera | High-res imagery; DTMs | ~25–50 cm/px |
| THEMIS | Odyssey IR | Thermal IR, thermal inertia | ~100 m/px |
| CRISM | MRO spectrometer | VIS/NIR spectroscopy | ~18 m targeted; ~200 m survey |

**Access**: NASA PDS (pds.nasa.gov), USGS Astrogeology (astrogeology.usgs.gov), Mars Trek (trek.nasa.gov).

> [!WARNING]
> Mars DEM resolution (~200–460 m) is much coarser than Earth DEMs (~30 m). This resolution mismatch must be addressed by resampling Earth data to the coarsest resolution before comparison. Comparing 30 m Earth slopes to 460 m Mars slopes is a systematic error.

---

## Terrain Properties to Extract

For analog comparison:
1. **Slope distribution** at Mars-matched baseline (~200 m or ~460 m)
2. **Surface roughness** at kilometer scales
3. **Thermal inertia** (from THEMIS; model-dependent, Tier B/C)
4. **Mineralogy class** (from CRISM; Tier C, complex processing)

---

## What Earth Cannot Reproduce (Mars)

| Property | Mars Value | Earth Approximation | Verdict |
|----------|-----------|---------------------|---------|
| Gravity | 3.71 m/s² | 9.81 m/s² | **No analog** — Tier D |
| Atmosphere | ~600 Pa, 95% CO₂ | ~101,325 Pa, 21% O₂ | **No analog** — Tier D |
| Radiation | Thin atmosphere, no magnetosphere | Shielded | **No analog** — Tier D |
| Aeolian transport | Low-pressure saltation dynamics | Different physics | **Partial** — Tier C |
| Soil perchlorates | Up to ~1 wt% | Present in Atacama, different context | **Partial** — Tier C |
| Temperature range | ~150–300 K (site-dependent) | Similar ranges available | **Partial** — Tier B |

---

## Mars as Stretch Goal

In the hackathon MVP, Mars comparison is a stretch goal. The lunar south-polar rover-mobility objective takes priority. If Mars is included:

1. Use the MOLA–HRSC blended DEM as the primary terrain dataset
2. Compare at ~200 m baseline
3. Focus on terrain dimensions only (slope, roughness)
4. Skip CRISM spectral processing (high prep burden)
5. Use THEMIS thermal inertia only if pre-processed products are accessible

---

*Document status: Pre-hackathon research. Sources require human verification before citation in final submission.*
