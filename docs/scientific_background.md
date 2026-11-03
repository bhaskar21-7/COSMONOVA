# Scientific Background

**Terrestrial Analogs for Lunar and Martian Exploration — COSMONOVA Scientific Framework**

> [!NOTE]
> This document summarizes the scientific foundations for the COSMONOVA project (Planetary Analog Intelligence Platform). All claims are sourced from published literature. Items marked [verify] require human verification of the citation before use.

---

## What Is a Terrestrial Analog?

A terrestrial analog is an Earth location that reproduces **some property** of a planetary environment **relevant to a specific objective** (Preston & Dartnell 2014, *Int. J. Astrobiology*).

Key principles:

1. **Analogs are always partial** — no Earth site matches the Moon or Mars in all properties.
2. **Analogs are objective-dependent** — a site that is excellent for rover mobility testing may be poor for habitat-siting studies.
3. **Analog fidelity is per-property** — stating that a site is "X% similar" to the Moon without specifying which properties, at what scale, and for what purpose is scientifically meaningless.

---

## Property Categories and Earth Reproducibility

| Property Class | Examples | Can Earth Reproduce It? |
|----------------|----------|------------------------|
| **Geomorphic / terrain** | Slope, roughness, crater/rock density, boulder fields | Yes, partially, at some scales |
| **Geological / compositional** | Basalt, anorthosite-like rocks, sulfates, clays, perchlorate-bearing soil | Partly; Earth lacks lunar highland anorthosite in comparable regolith |
| **Thermal (surface)** | Diurnal range, thermal inertia, extreme cold | Partly for Mars; essentially no for lunar PSRs |
| **Atmospheric** | Pressure, composition, dust loading | No — Mars ~600 Pa; Earth high plateaus still ~50–60 kPa |
| **Gravity** | 1.62 m/s² (Moon), 3.71 m/s² (Mars) | No — requires parabolic flight or offloading rigs |
| **Radiation** | Galactic cosmic rays, solar particle events | No at the surface |
| **Operational / logistics** | Isolation, communication delay, crew behavior | Yes — e.g., polar stations, field analog missions |

### Design Consequence

Only the first three rows (geomorphic, geological, thermal) can participate in a **data-driven similarity calculation**. Atmospheric, gravity, and radiation are **fixed mismatches** that should be reported as failure flags, not averaged into a score.

---

## History of Analog Research

### Established Analog Programs
- **Haughton-Mars Project** (Devon Island, Canada): Simulates Mars operations in an impact crater setting in a polar desert (Lee & Osinski 2005, *MAPS*).
- **Atacama Desert** (Chile): Used for Mars soil and microbiology studies due to hyperaridity and low organic content (Navarro-González et al. 2003, *Science*).
- **McMurdo Dry Valleys** (Antarctica): Polar desert with permafrost, used for Mars cold-desert process studies.
- **Iceland Volcanic Fields**: Basaltic terrain with palagonite formation, used since the Apollo era for lunar surface training [verify].

### Key Literature
- Preston, L. J. & Dartnell, L. R. (2014). Planetary habitability: lessons learned from terrestrial analogues. *Int. J. Astrobiology* 13.
- Léveillé, R. J. & Datta, S. (2010). Lava tubes and basaltic caves as astrobiological targets on Earth and Mars. *Planetary and Space Science* 58.

---

## Geological and Environmental Parameters for Comparison

### Terrain Parameters (Tier A — Directly Comparable)
- **Slope distribution**: Computed from DEMs at matched baselines (same ground sample distance for both bodies)
- **Surface roughness**: Multi-scale metric; must compare at equivalent spatial baselines (Rosenburg et al. 2011, *JGR Planets*)
- **Crater/rock density**: Counted from imagery; depends on resolution and counting area

> [!WARNING]
> Computing slope at 5 m on the Moon and 30 m on Earth, then comparing them, is a methodological error. All comparisons must use matched baselines.

### Thermal Parameters (Tier B — Same Quantity, Different Instrument Physics)
- **Surface temperature**: Diurnal and seasonal ranges
- **Thermal inertia**: Derived from temperature observations; model-dependent
- **Note**: Earth's atmosphere buffers surface temperature. Mars measurements (e.g., THEMIS thermal inertia) and lunar measurements (e.g., Diviner) have different observation geometries.

### Geological Parameters (Tier C — Proxy)
- **Lithology classification**: From geological maps (categorical comparison)
- **Spectral band ratios**: Mineral proxies from multispectral/hyperspectral data; instruments differ across bodies
- **Note**: Never compare raw spectra from different instruments without convolving to a common band set.

### Fixed Mismatches (Tier D — Not for Distance Calculation)
- Gravity
- Atmospheric pressure and composition
- Radiation environment
- Permanently Shadowed Region (PSR) temperatures (below ~40 K; no Earth equivalent)

---

## The Comparability Tier Framework

This framework, central to our methodology, classifies each property comparison:

| Tier | Definition | Treatment in Analysis |
|------|-----------|----------------------|
| **A** | Same physical quantity, comparable instruments | Full distance calculation |
| **B** | Same quantity, different instrument physics | Distance with inflated uncertainty; flagged |
| **C** | Related proxy, not direct measurement | Separate dimension; strong caveats |
| **D** | Non-equivalent / impossible on Earth | Never in distance; reported as failure flag |

---

## Implications for the Project

1. The system must **never produce a single universal similarity score** — this would mix incomparable physics.
2. Output must be a **vector of per-dimension similarities** with tier labels.
3. **Tier D mismatches** are not limitations of the tool — they are scientific facts about the nature of analog research.
4. Users must be able to see **which properties drive similarity** and which are unmeasurable.

---

*Document status: Pre-hackathon literature review. Sources require human verification before citation.*
