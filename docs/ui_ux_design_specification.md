# UI/UX Conceptual Design Specification

**COSMONOVA — Pre-Hackathon Conceptual Application Design**  
*Planetary Analog Intelligence Platform*

> [!IMPORTANT]
> This is a **conceptual design specification and wireframe blueprint** for the future hackathon application. In strict adherence to competition preparation rules, **no front-end code or production application has been implemented**.

---

## 1. Design Vision & Philosophy

COSMONOVA serves a dual audience: **planetary science researchers / mission planners** requiring rigorous multi-dimensional data, and **general challenge evaluators / students** seeking intuitive visual exploration.

The user interface is designed around four core principles:
1. **Never a Single Scalar**: Reject misleading "90% match" badges. Always display multi-dimensional vectors with clear tier labels (Tier A: Direct, Tier B: Physical diff, Tier C: Proxy, Tier D: Invariant mismatch).
2. **Prominence of Failure Analysis**: Analog mismatch flags (gravity, atmospheric pressure, radiation, PSR cryogenic cold) are given first-class visual priority, not hidden in footnotes.
3. **Transparent Uncertainty**: Every metric is accompanied by confidence intervals, spatial coverage fractions, and data resolution indicators.
4. **Mission Objective Filtering**: Hard operational constraints (e.g. slope thresholds for rover mobility vs. solar access for habitat siting) drive candidate exclusion before ranking.

---

## 2. Information Architecture & Layout Structure

The application will be organized into a multi-panel responsive scientific dashboard (built via Streamlit during the hackathon):

```
+----------------------------------------------------------------------------------------------------+
| 🪐 COSMONOVA  |  Planetary Analog Intelligence Platform  |  [Status: Pre-Hackathon Scientific Prototype]  |
+----------------------------------------------------------------------------------------------------+
| SIDEBAR: MISSION CONTROLS       | MAIN VIEWPORT: INTERACTIVE EXPLORATION & ANALYSIS                |
|                                 |                                                                  |
| 1. Mission Profile Selector     | [Tab 1: Global Map]  [Tab 2: Comparative Profile]  [Tab 3: Report]  |
|    (o) Lunar Rover Mobility     |------------------------------------------------------------------|
|    ( ) Lunar Base / Habitat     | TOP: Comparative Planetary Target vs. Earth Analog Overview      |
|    ( ) Mars Fluvial/Playa       | - Target: Shackleton Crater Rim (LOLA 20m)                       |
|    ( ) Custom Constraints       | - Candidate: Lonar Crater / Ladakh / Atacama                     |
|                                 |------------------------------------------------------------------|
| 2. Target Planetary Body        | LEFT: Geospatial Map View        | RIGHT: Telemetry & Evaluation |
|    [ Moon (Artemis S-Pole)  v ] |                                  | [ILLUSTRATIVE WIREFRAME MOCKUP|
|                                 | Interactive Leaflet/PyDeck Map   |  NO METRICS YET COMPUTED]     |
| 3. Earth Analog Filter          | - Candidate boundary layers      | [Similarity Vector Schema]    |
|    [x] High-Latitude Polar      | - Elevation heatmaps             | - Terrain Slope (Tier A): [W1]|
|    [x] Basaltic / Volcanic      | - Planetary target overlay inset | - Roughness (Tier A): [RMS]   |
|    [x] Cold / Arid Deserts      |                                  | - Thermal Range (Tier B): [ΔT]|
|    [x] Indian Candidates        |                                  | - Lithology (Tier C): [Class] |
|                                 |                                  |-------------------------------|
|                                 |                                  | [Analog Failure Matrix Tier D]|
| 4. Hard Constraints (Sliders)   |                                  | [!] Gravity: 1.62 vs 9.81 m/s²|
|    Max Slope Threshold: [15° ]  |                                  | [!] Pressure: Vac vs 101 kPa  |
|    Min Evidence Fraction: [80%] |                                  | [!] Radiation: Unshielded     |
|                                 |                                  | [!] PSR Temp (<40K): NONE     |
| [ Run SMAA Evaluation ]         |                                  |-------------------------------|
|                                 |                                  | [Uncertainty & Coverage Band] |
|                                 |                                  | - Coverage: [%] | CI: [±dev]  |
+---------------------------------+----------------------------------+-------------------------------+
```

---

## 3. Core Component Specifications

### 3.1 Mission Selection Interface
- **Preset Configurations**:
  - `Rover Mobility & Trafficability`: Emphasizes slope distribution (<15° cutoff), decameter roughness, rock abundance, micro-topography.
  - `Permanent Habitat Siting`: Prioritizes terrain stability, long-duration solar illumination proxy, line-of-sight communications, proximity to subsurface access/lava tubes.
  - `Astrobiology & Mineralogy`: Focuses on basaltic alteration, evaporites/sulfates, clays, hypersaline or hyperarid extremes.
- **Custom Constraint Sliders**: Allows researchers to set non-compensatory thresholds (candidates failing hard constraints are greyed out or dropped).

### 3.2 Dual-Body Geospatial Map (Interactive)
- **Engine**: PyDeck or Folium/Leaflet.
- **Base Layers**:
  - Earth: Satellite basemap + Copernicus GLO-30 / SRTM hillshade elevation overlay.
  - Planetary Inset: Synchronized or toggleable LOLA polar hillshade / MOLA global elevation.
- **Overlays**:
  - Candidate site boundary polygons (5–10 km standardized analysis tiles).
  - Slope class colormaps (green: 0–10°, yellow: 10–20°, red: >20°).
  - Data voids and no-coverage zones marked with distinct hatching.

### 3.3 Candidate Location Information Panel
Displays rich metadata for the selected Earth candidate:
- **Site Name & Country** (e.g., Lonar Impact Crater, Maharashtra, India).
- **Geographic Extent**: Latitude, Longitude, Elevation range (ASL).
- **Physical Environment**: Impact structure in Deccan flood basalt; alkaline saline caldera lake.
- **Published Literature Status**: Cited historical usage (e.g. Hagerty & Newsom 2003) vs. exploratory screening hypothesis.
- **Access Logistics & Caveats**: Monsoonal seasonal variation, anthropogenic settlement proximity, data provider (GSI / USGS).

### 3.4 Multi-Dimensional Similarity Breakdown
Visualized via horizontal bar charts with confidence intervals:
- Each bar represents a comparability dimension:
  - **Terrain Topography (Tier A)**: Wasserstein-1 distance on matched-baseline slope histograms.
  - **Surface Roughness (Tier A)**: Multi-scale RMS height variation.
  - **Thermal Amplitude (Tier B)**: Diurnal skin temperature swing.
  - **Lithology Match (Tier C)**: Categorical similarity from geological classification.
- **Visual Error Bars**: Displaying 95% spatial block bootstrap confidence intervals.

### 3.5 Analog Failure Analysis Card (The Differentiator)
A prominent callout component utilizing alert styling:
- **Status Badges**:
  - `CRITICAL MISMATCH (Tier D)`:
    - Surface gravity ($1.62\text{ m/s}^2$ Moon vs $9.81\text{ m/s}^2$ Earth).
    - Atmospheric shielding ($0\text{ Pa}$ Moon vs $101.3\text{ kPa}$ Earth).
    - Cosmic ray flux & solar energetic particles (Earth magnetosphere absorbs).
    - Cryogenic PSR cold traps ($<40\text{ K}$ permanent cold traps have zero Earth surface counterpart).
  - `DATA-DRIVEN MISMATCH`:
    - E.g., monsoon precipitation alters clay hydration rates compared to anhydrous lunar regolith.

### 3.6 Uncertainty & Evidence Indicators
- **Evidence Coverage Fraction Gauge**: Percentage of tile area with high-confidence sensor returns without cloud/vegetation interference.
- **Resolution Mismatch Warning**: Displays the Ground Sample Distance (GSD) ratio between sensors (e.g., LOLA 20m vs Earth 30m harmonized to 30m).
- **Sensitivity Index**: Probability rank acceptability from SMAA Monte Carlo weight perturbations.

---

## 4. Design Tokens & Visual Hierarchy

| Element | Specification | Rationale |
|---------|---------------|-----------|
| **Primary Theme** | Dark Mode (`#0E1117` background) | Matches deep-space / planetary observatory tools; reduces glare during nocturnal research |
| **Accent Colors** | Cyan (`#00E5FF`) for Moon, Red/Orange (`#FF6B4A`) for Mars, Emerald (`#00E676`) for Earth | Distinct cognitive association with target celestial bodies |
| **Alert Colors** | Crimson (`#FF1744`) for Tier D Failure, Amber (`#FFC107`) for Proxy/Caveats | Immediate recognition of physical impossibilities |
| **Typography** | Monospace (`Fira Code` / `Roboto Mono`) for numeric metrics; Sans-serif (`Inter`) for analysis prose | Clean readability of coordinates, resolutions, and uncertainties |

---

## 5. Screen Wireframes (ASCII Schematics)

### Screen 1: Rover Mobility Siting View (Illustrative Wireframe Template)
```
+-----------------------------------------------------------------------------+
| [Earth] Candidate Site (e.g. Lonar)   VS   [Moon] Artemis S-Pole Rim (LOLA) |
+-----------------------------------------------------------------------------+
| MAP VIEW                                    | EVALUATION VECTOR SCHEMA      |
| [=========================================] | Dimension       Metric  95% CI|
| [  * (Earth Candidate Extent)             ] | Terrain Slope   [W1-dist] [CI]|
| [    Elev: Min - Max                      ] | Micro-Roughness [RMS-dev] [CI]|
| [    Harmonized GSD: 30m                  ] | Thermal Range   [ΔT-band] [CI]|
| [=========================================] | Lithology Class [Categorical] |
| INSET: LOLA Lunar Altimetry Profile         |-------------------------------|
| [=========================================] | INVARIANT FAILURE FLAGS Tier D|
| [  O (Target Planetary Feature)           ] | [!] Gravity: 1.62 m/s² (FAIL) |
| [    LOLA Topography Profile              ] | [!] Pressure: Vacuum (FAIL)   |
| [=========================================] | [!] PSR Cold: <40K (FAIL)     |
+-----------------------------------------------------------------------------+
| [ILLUSTRATIVE WIREFRAME TEMPLATE — METRICS COMPUTED DURING HACKATHON SPRINT]|
+-----------------------------------------------------------------------------+
```

---

*Document status: Pre-hackathon UI/UX conceptual specification. Implementation scheduled for hackathon sprint (Nov 14–16, 2026).*

