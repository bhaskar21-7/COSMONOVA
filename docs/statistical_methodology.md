# Statistical Methodology

**Framework for Multi-Dimensional Analog Comparison — COSMONOVA Statistical Engine**

> [!IMPORTANT]
> This document describes a **proposed** statistical framework. No algorithms have been implemented. Methods will be refined and coded during the hackathon event.

---

## Core Principle: No Single Similarity Score

The central methodological commitment: **do not collapse multi-dimensional comparisons into one number.** A single "similarity score" hides trade-offs between incomparable physical properties. Instead, report a vector of per-dimension distances with tier labels and uncertainty bounds.

---

## 1. Data Normalization

### The Problem
Features measured in different units and scales (elevation in meters, temperature in Kelvin, slope in degrees) cannot be compared directly. A naive Euclidean distance would be dominated by whichever feature has the largest numerical range.

### Proposed Approach
Standardize using the **target distribution's own spread** plus measurement error, not the Earth candidate's spread:

$$z_j = \frac{x_j - \mu_{T,j}}{\sqrt{\sigma^2_{T,j} + \sigma^2_{\text{meas},j}}}$$

Where:
- $x_j$ = candidate site's value for feature $j$
- $\mu_{T,j}$ = target (lunar/Mars) mean for feature $j$
- $\sigma^2_{T,j}$ = target variance
- $\sigma^2_{\text{meas},j}$ = measurement error variance

Use **robust estimators** (median / MAD) where distributions are skewed — slope distributions typically are.

---

## 2. Similarity Measurement Concepts

### 2.1 Comparability Tiers

Before computing any distance, classify each comparison:

| Tier | Definition | Examples | Treatment |
|------|-----------|----------|-----------|
| **A** | Same physical quantity, comparable instruments | Elevation, slope, roughness | Full distance calculation |
| **B** | Same quantity, different instrument/physics | Surface temperature, diurnal range | Distance with inflated uncertainty; flagged |
| **C** | Proxy relationship | Spectral band ratios as mineralogy proxy; thermal inertia | Separate dimension; strong caveats |
| **D** | Non-equivalent / fixed mismatch | Gravity, pressure, radiation, PSR cold traps | **Never in a distance.** Reported as failure flags |

### 2.2 Distance Metrics

**Within a dimension** (Tier A features), use Mahalanobis distance from the target distribution:

$$D^2_M = (\mathbf{x} - \boldsymbol{\mu}_T)^\top \Sigma_T^{-1} (\mathbf{x} - \boldsymbol{\mu}_T)$$

With a **shrinkage covariance estimator** (Ledoit & Wolf 2004, *J. Multivariate Analysis*) because terrain features are highly collinear and $\Sigma_T$ can be near-singular.

**At the distribution level** (comparing site pixel populations to target pixel populations), prefer:
- **Wasserstein-1 distance** (earth mover's distance) — respects the metric structure of the feature space
- **Energy distance** — handles multivariate distributions without density estimation

These respect that a site is a *population of pixels*, not a single point.

### 2.3 What to Avoid

| Method | Why to Avoid |
|--------|-------------|
| Unscaled Euclidean distance | Units dominate; physically meaningless |
| PCA/UMAP/t-SNE distances as evidence | Fine for exploration; components are not physical quantities |
| Pixel-level significance tests | Spatial autocorrelation inflates significance |
| Cross-instrument raw spectral angle | Different band passes and noise characteristics |
| Deep learning for "analogness" | No ground-truth labels exist |

---

## 3. Multi-Criteria Decision Analysis (MCDA)

### 3.1 Mission-Specific Constraints

Mission profiles (rover mobility, habitat siting, geological exploration, astronaut training) differ in **constraints**, not just weights.

**Step 1**: Apply hard constraints first.
- Example: a rover-mobility test requires slope distribution within a stated range.
- A site failing a hard constraint is **excluded**, not penalized.

**Step 2**: Rank surviving candidates with a non-compensatory method.
- **Pareto front**: Identify sites that are not dominated on any dimension.
- **PROMETHEE/ELECTRE**: Outranking methods that do not allow good performance on one criterion to compensate for failure on another.

> [!WARNING]
> A weighted sum lets great slope similarity offset total failure on composition, which is **scientifically wrong** for many objectives. Use non-compensatory methods.

### 3.2 Weight Handling — SMAA

Weights in MCDA are **normative** (they express judgment), not estimated from data.

**Stochastic Multicriteria Acceptability Analysis (SMAA)** (Lahdelma et al. 1998, *Eur. J. Operational Research*):
1. Define plausible weight ranges (not point values)
2. Sample weights uniformly from those ranges
3. For each sample, compute rankings
4. Report the **rank acceptability index** per site — the probability that a site achieves each rank across all weight combinations

This provides:
- Built-in sensitivity analysis
- An honest answer to "who set the weights?"
- Robust rankings that do not depend on a single subjective weighting

> [!NOTE]
> If AHP pairwise comparisons are used to set initial weight ranges, be honest that the judgments come from students, not mission engineers.

---

## 4. Uncertainty Quantification

### 4.1 Spatial Block Bootstrap

**Problem**: Pixels in raster data are spatially autocorrelated. A naive pixel-level bootstrap treats each pixel as independent, producing falsely tight confidence intervals.

**Solution**: Spatial block bootstrap.
1. Determine block size from the **empirical variogram range** (the distance at which spatial autocorrelation drops below a threshold)
2. Resample blocks, not pixels
3. Recompute the statistic of interest for each resample
4. Report percentile-based confidence intervals

### 4.2 Measurement-Error Propagation

DEMs have published vertical error profiles. Slope and roughness are derivatives of elevation and are highly sensitive to noise at fine scales.

**Approach**: Monte Carlo perturbation.
1. Perturb DEM elevations by their published vertical error (e.g., ±5 m for SRTM)
2. Recompute slope and roughness for each perturbed DEM
3. Report the distribution of derived metrics

### 4.3 Missing Data

- **Do not impute across physically different regions** (e.g., do not impute lunar data gaps from Earth patterns)
- Allow multiple imputation only for **small gaps within a dimension**
- Otherwise report an **evidence-coverage fraction**: the share of features and area with usable data
- Let coverage fraction propagate into the final report

### 4.4 Confidence Reporting

Confidence is a **vector**, not a single number:
- Coverage fraction (how much of the site has data)
- Resolution mismatch factor
- Tier composition (proportion of Tier A vs B vs C features)
- Confidence interval width per dimension

A single composite "confidence score" would be as arbitrary as a single similarity score.

---

## 5. Sensitivity Analysis

### What to Test
1. **Weight sensitivity**: Via SMAA (see §3.2)
2. **Resolution sensitivity**: Recompute at different baselines to check if rankings change
3. **Feature subset sensitivity**: Remove one feature dimension at a time to assess robustness
4. **Error model sensitivity**: Vary the assumed DEM error magnitude

### Validation by Controls
- **Positive controls**: Do rankings recover sites planetary scientists already use (Haughton, Atacama, Dry Valleys, Iceland) for the objectives they are known for?
- **Negative controls**: Do rankings reject obviously poor sites (e.g., a tropical rainforest for Mars soil)?
- **Caveat**: This is face-validity, not proof. It can be circular if weights are tuned until controls rank well. **Fix controls and weight ranges before looking at results.**

---

## 6. Coordinate Systems and Resolution

### Coordinate Reference Systems
- **Moon**: IAU sphere (radius 1,737.4 km), polar stereographic for south pole analysis
- **Mars**: IAU sphere (radius 3,396.19 km [verify])
- **Earth**: WGS84 (EPSG:4326 for geographic; appropriate UTM zone for local analysis)

> [!CAUTION]
> **Never reproject a lunar raster as if it were Earth** (EPSG:4326 mislabeling is a classic error in planetary GIS). Use planetary-body-specific CRS definitions.

### Resampling Rules
- **Continuous variables** (elevation, temperature): area-weighted resampling
- **Categorical variables** (lithology): mode resampling
- **Direction**: Always resample to the **coarsest** resolution of the pair being compared

### Spatial Scale
A crater (~km scale) and a desert (~10⁴–10⁵ km²) are not comparable at the same tile size. Use **fixed tiles** (e.g., 5–10 km) as the unit of comparison.

---

## 7. Feature Engineering Notes

### Terrain Features
- **Slope**: Computed from DEM at matched baseline (resample all DEMs to a common ground sample distance first)
- **Roughness**: Multi-scale; follow Rosenburg et al. (2011) for lunar roughness methodology
- **References**: Rosenburg et al. (2011), *JGR Planets*; Kreslavsky et al. (2013), *Icarus*

### Thermal Features
- Mean surface temperature, diurnal amplitude, thermal inertia
- Earth's atmosphere buffers temperature → Tier B/C

### Geological Features
- Lithology class (from geological maps): categorical comparison
- Spectral indices: **convolve to a common band set** before comparison; never compare raw spectra from different instruments

---

## 8. Machine Learning Position

Machine learning is **secondary** in this project. There is no labeled dataset of analog quality, so supervised models have nothing valid to learn.

Acceptable ML uses:
- **Unsupervised terrain-unit mapping**: k-means, Gaussian mixtures, or HDBSCAN on geomorphometric features within each body, to describe terrain units and compare unit proportions
- **Feature importance exploration**: Random forest / permutation importance to explore which features separate known terrain classes — never as a similarity oracle
- **Spatial cross-validation**: Blocked CV whenever any model is evaluated

---

*Document status: Proposed methodology. Not implemented. To be refined and coded during the hackathon.*
