# Lunar Environments

**Target Profiles for Analog Comparison**

> [!NOTE]
> These are reference descriptions of lunar environments, drawn from published literature. They should be treated as **target profiles to be quantified from data during the hackathon**, not as hard-coded values.

---

## Primary Target: Lunar South Pole

### Why the South Pole?

NASA's Artemis program focuses on the lunar south-polar region. In August 2022, NASA announced 13 candidate landing regions within ~6° of the south pole [verify exact list on nasa.gov]. These include areas around:

- **Shackleton Crater** rim
- **de Gerlache** rim
- **Haworth** crater
- **Malapert Massif**
- **Nobile** rim
- **Amundsen** rim

### Shackleton Crater
- **Diameter**: ~21 km
- **Depth**: ~4 km
- **Location**: Almost exactly on the south pole
- **Illumination**: Rim has high but not continuous illumination; interior floor is a candidate cold trap
- **Significance**: Both rim (potential base site) and interior (volatile resource) are of interest
- **Key reference**: Mazarico, E. et al. (2011). Illumination conditions of the lunar polar regions using LOLA topography. *Icarus* 211, 1066.

### Malapert Massif
- **Elevation**: ~5 km high massif near the south pole
- **Illumination**: Long illumination periods
- **Communication**: Line-of-sight to Earth (important for relay infrastructure)
- **Use case**: Frequently cited in communication-relay and base-siting proposals

---

## Surface Characteristics

### Illumination
- **Extreme and terrain-controlled**: Low Sun elevation produces near-horizontal light and long shadows
- **Modeled from**: LOLA topography (Mazarico et al. 2011)
- **Analog implication**: Terrain-derived horizon shadowing is the closest Earth analog; actual insolation levels differ

### Permanently Shadowed Regions (PSRs)
- **Temperature**: Diviner measured surface temperatures below ~40 K in some south-polar cold traps (Paige et al. 2010, *Science* 330, 479)
- **Analog implication**: **No Earth surface is within an order of magnitude of this temperature.** PSR thermal environments have no terrestrial analog. This is a Tier D mismatch.

### Regolith
- **Composition**: Fine-grained, sharp, low cohesion at surface, abrasive
- **Highland terrain**: Anorthositic
- **Mare terrain**: Basaltic
- **Polar composition**: Less constrained than equatorial regions
- **Key reference**: Heiken, G., Vaniman, D., French, B. (1991). *Lunar Sourcebook*. Cambridge Univ. Press.

### Morphology
- Heavily cratered terrain
- Steep crater walls
- Boulder fields on slopes
- Degraded old surfaces

---

## Key Datasets for Lunar Targets

| Dataset | Instrument | Measures | Resolution |
|---------|-----------|----------|------------|
| LOLA | Laser altimeter (LRO) | Elevation, slope, roughness | ~tens of m global; finer near poles |
| LROC NAC | Camera (LRO) | Imagery | ~0.5–2 m/px |
| LROC WAC | Camera (LRO) | Imagery | ~100 m/px |
| Diviner | Radiometer (LRO) | Surface temperature, rock abundance | ~hundreds of m |
| Lunar Geologic Map | USGS | Lithology units | 1:5M (global, coarse) |

**Access**: NASA PDS Geosciences Node, Moon Trek (trek.nasa.gov), QuickMap (quickmap.lroc.asu.edu).

---

## Terrain Properties to Extract

For rover-mobility analog comparison:
1. **Slope distribution** at matched baseline (resample Earth DEMs to match LOLA grid spacing)
2. **Surface roughness** at multiple scales (following Rosenburg et al. 2011 methodology)
3. **Boulder density** (from LROC NAC where available; time-intensive)
4. **Crater density** per area (from imagery; resolution-dependent)

---

## What Earth Cannot Reproduce

| Property | Lunar Value | Earth Approximation | Verdict |
|----------|------------|---------------------|---------|
| Gravity | 1.62 m/s² | 9.81 m/s² | **No analog** — Tier D |
| Atmosphere | Effectively vacuum | ~101 kPa at sea level | **No analog** — Tier D |
| Radiation | Unshielded GCR + SEP | Magnetosphere-shielded | **No analog** — Tier D |
| PSR temperature | <40 K | Coldest on Earth: ~184 K (Vostok) | **No analog** — Tier D |
| Regolith texture | Sharp, abrasive, no weathering | Weathered, rounded | **Partial** — Tier C |
| Illumination geometry | Near-horizontal, extreme shadows | Similar at high latitudes | **Partial** — Tier B |

---

*Document status: Pre-hackathon research. Sources require human verification before citation in final submission.*
