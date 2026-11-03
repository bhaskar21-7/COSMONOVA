# Scientific Limitations

**Known Constraints, Gaps, and Honest Caveats**

> [!CAUTION]
> This document exists because scientific integrity demands explicit acknowledgment of what our tool **cannot do**, what it **does not know**, and where its claims are **weakest**. Ignoring these limitations would undermine the project's credibility.

---

## Fundamental Limitations of Terrestrial Analogs

### 1. No Complete Analog Exists
No Earth location reproduces all properties of the Moon or Mars simultaneously. Analog fidelity is always **per-property and per-objective**. Any tool claiming a "best analog" without stating the objective is wrong by construction.

### 2. Non-Reproducible Properties (Tier D)

| Property | Why It Cannot Be Matched | Implication |
|----------|------------------------|-------------|
| **Gravity** | Moon: 1.62 m/s², Mars: 3.71 m/s², Earth: 9.81 m/s² | Affects regolith mechanics, rover dynamics, dust behavior |
| **Atmospheric pressure** | Mars: ~600 Pa; Earth high plateaus: ~50,000 Pa | Affects thermal regulation, aeolian transport, human physiology |
| **Radiation** | No magnetosphere on Moon/Mars; Earth surface is shielded | Affects material degradation, biological hazard |
| **PSR temperatures** | Lunar cold traps: <40 K; coldest Earth surface: ~184 K | No thermal analog for volatile trapping |

These are not limitations of the tool — they are **fundamental properties of the physical universe**.

### 3. No Ground Truth for "Analogness"
There is no labeled dataset where planetary scientists have rated sites on a continuous analog-quality scale. This means:
- **Supervised machine learning is not applicable** — there is nothing to train on
- **Validation is limited to face-validity** — do our rankings agree with expert intuition for well-known sites?
- Face-validity can be circular if weights are tuned until controls rank well

---

## Data Limitations

### Resolution Mismatch
- Earth DEMs: ~30 m (SRTM, ASTER, Copernicus)
- Moon (LOLA): ~tens of meters globally, finer at poles
- Mars (MOLA): ~460 m; MOLA-HRSC blend: ~200 m

Computing slope at 5 m on the Moon and 30 m on Earth, then comparing them, is a **systematic methodological error**. All comparisons must use matched baselines (resample to the coarsest).

### Coverage Gaps
- **SRTM**: Does not cover >60°N or <56°S → no Devon Island, most of Iceland, Antarctica
- **HiRISE DTMs**: Available only for selected sites, not global
- **CRISM targeted**: ~18 m resolution but sparse spatial coverage
- **LOLA polar**: Finer near poles but interpolated between tracks at high resolution

### Instrument Differences
- Earth thermal data (ECOSTRESS, MODIS, Landsat TIRS) measures through an atmosphere
- Moon thermal data (Diviner) measures in vacuum
- Comparing these directly inflates or deflates differences depending on atmospheric conditions

### Indian Data Access
- GSI Bhukosh and ISRO Bhuvan may require registration with access restrictions
- Data formats and projections may differ from international standards
- **Verify access during preparation, not during the hackathon**

---

## Methodological Limitations

### Spatial Autocorrelation
Raster pixels are spatially autocorrelated. A naive pixel-level bootstrap or significance test produces falsely tight confidence intervals and inflated significance. Block bootstrap with variogram-calibrated block sizes partially addresses this, but the block size choice itself introduces uncertainty.

### Weight Subjectivity
In multi-criteria analysis, weights carry all the scientific judgment. They are normative (expressing values), not estimated from data. SMAA with weight ranges provides sensitivity analysis, but the ranges themselves are subjective.

### Scale Incomparability
A crater (~km scale) and a desert (~10⁴–10⁵ km²) are fundamentally different spatial entities. Fixed-tile comparison (5–10 km) is a pragmatic choice, not a scientifically perfect one.

### Proxy Relationships (Tier C)
Spectral band ratios used as mineral proxies on Earth, Moon, and Mars come from different instruments with different band passes, noise characteristics, and atmospheric effects. Any cross-body spectral comparison is inherently approximate.

---

## Project-Specific Limitations

### Indian Site Candidacy
- **Lonar Crater**: Justifiable with published literature, but it is a small (~1.8 km), monsoon-affected site. It is an analog for impact-in-basalt morphology, not for general lunar surface conditions.
- **Ladakh**: A defensible exploratory hypothesis for cold-desert terrain, but mineralogic similarity to Moon/Mars is **unproven**.
- **Rann of Kutch**: The weakest candidate. No established analog literature for Moon or Mars. Extremely flat terrain does not resemble rugged lunar polar surfaces.

### Scope Constraints
- 48-hour hackathon limits depth of analysis
- Team expertise may not include planetary science specialists
- Pre-computed results may not generalize to sites not in the initial candidate set

---

## How We Address Limitations

| Limitation | Our Approach |
|-----------|-------------|
| No complete analog | Report per-property vectors, never a single score |
| Tier D properties | Explicit failure flags in every comparison |
| No ground truth | Face-validity with positive/negative controls; state clearly |
| Resolution mismatch | Matched-baseline resampling before all comparisons |
| Coverage gaps | Report coverage fraction; do not impute across bodies |
| Weight subjectivity | SMAA with weight ranges; state that weights are normative |
| Spatial autocorrelation | Block bootstrap with variogram-calibrated blocks |
| Indian sites | Present as hypotheses; report negative results transparently |

---

## What We Will NOT Claim

1. ❌ That any Earth site is a "confirmed analog" for the Moon or Mars
2. ❌ That our similarity scores represent physical truth
3. ❌ That our rankings are endorsed by NASA or any space agency
4. ❌ That supervised ML can identify analogs
5. ❌ That a single number captures analog quality
6. ❌ That our Indian site analysis constitutes a discovery

---

*Document status: Pre-hackathon limitations document. To be updated as additional limitations are identified during preparation and the hackathon.*
