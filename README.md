# 🪐 COSMONOVA

**Planetary Analog Intelligence Platform**  
*Where Physics Meets Probability, Beyond Earth.*

[![NASA Space Apps 2026](https://img.shields.io/badge/NASA_Space_Apps-2026-blue)]()
[![Status: Pre-Hackathon Preparation](https://img.shields.io/badge/Status-Pre--Hackathon_Preparation-orange)]()
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-green)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)]()

> **NASA Space Apps Challenge 2026**  
> *"Identify Earth Locations that Analog the Permanent Moon Base Locations and Mars"*  
> **Global Hackathon Window:** November 14–15, 2026

---

## 🌌 Project Introduction

**COSMONOVA** is a planetary analog discovery platform that explores Earth environments as potential analogs for lunar and Martian landscapes through geospatial data, statistical analysis, remote sensing, and scientific comparison.

Rather than relying on qualitative assumptions or uncalibrated composite scores, COSMONOVA introduces a disciplined, multi-tier comparability framework that evaluates terrestrial candidate sites against target planetary environments using matched spatial baselines, stochastic decision analysis, and transparent failure boundaries.

---

## 🎯 Problem Statement

Landing site selection, robotic rover traversability, and surface habitat architecture for lunar and Martian missions depend strictly on terrain topography, surface roughness, regolith mechanics, environmental temperature swings, and mineralogical composition. Before deploying high-value space hardware or human crews, space agencies rely on **terrestrial analog sites** — locations on Earth that reproduce specific planetary physical conditions.

However, as emphasized in the NASA Space Apps Challenge brief, analog sites are historically **"not entirely well characterized."** Prevailing tools and workflows suffer from critical shortcomings:

1. **Narrow Selection Bias**: Legacy missions repeatedly reuse a handful of famous sites (Atacama Desert, Devon Island, Death Valley), neglecting promising or more geographically accessible alternatives.
2. **The Single-Scalar Fallacy**: Most existing tools collapse complex, multi-dimensional environmental properties into a single misleading "similarity score" (e.g., "88% similar"), hiding critical terrain failures behind unrelated compositional matches.
3. **Absence of Mission-Specific Context**: A site ideal for rover suspension and wheel-slip testing over rocky slopes may be entirely useless for in-situ resource utilization (ISRU) or subsurface permafrost drilling.
4. **Omission of Failure Boundaries**: Existing comparisons routinely ignore where an analog *fails* — fundamental physical constraints that cannot be replicated on Earth (gravity, ambient vacuum, cosmic radiation, cryogenic cold traps).
5. **Ignored Spatial Uncertainty**: Sensor resolutions, ground sample distances (GSD), and instrument error profiles differ drastically between terrestrial DEMs (e.g., 30 m SRTM/Copernicus) and planetary altimeters (e.g., 5–20 m LOLA, 200 m MOLA), introducing numerical divergence if not rigorously harmonized.

---

## 🛰️ Project Objectives

- **Mission-Specific Screening**: Characterize candidate sites according to specific operational profiles (e.g., rover mobility vs. base habitat siting) rather than generic similarity.
- **Dimensional Integrity**: Deliver a multidimensional comparability vector with explicit confidence intervals rather than a single collapsed scalar score.
- **Transparent Failure Profiling**: Enforce primary reporting of invariant physical mismatches (Tier D constraints) to prevent overconfidence in field testing.
- **Harmonized Sensor Baselines**: Enforce common spatial baselines across disparate planetary and terrestrial coordinate reference systems and elevation models.
- **Open Science & Democratization**: Provide an open, reproducible framework leveraging open-access datasets from NASA, ESA, USGS, and ISRO.

---

## 🪐 The Earth–Moon–Mars Connection

COSMONOVA bridges terrestrial remote sensing with planetary exploration targets across three bodies:

| Planetary Target | Target Environment & Key Regions | Primary Data Products | Terrestrial Analog Relevance |
| :--- | :--- | :--- | :--- |
| **The Moon** | **Artemis South Pole Candidate Regions**<br>• Shackleton Crater Rim<br>• Connecting Ridge & de Gerlache<br>• Permanently Shadowed Regions (PSRs) | • LOLA GDR / Polar Altimetry (5–20 m)<br>• Diviner Lunar Radiometer (LST)<br>• LROC NAC / WAC Imagery | Basaltic impact breccia, steep crater slopes (15°–30°), micro-topographic boulder fields, extreme illumination angles. |
| **Mars** | **Paleo-Hydrological & Volcanic Basins**<br>• Jezero Crater (Deltaic sediments)<br>• Gale Crater (Mount Sharp layered sulfates)<br>• Meridiani Planum & Olympus mons flows | • MOLA–HRSC Blended DEM (200 m)<br>• THEMIS Thermal IR & Thermal Inertia<br>• CTX / HiRISE DTMs & Imagery | Cold hyperarid deserts, basaltic lava flows, periglacial stone polygons, evaporite playas, and alluvial fan geometries. |
| **Earth** | **8 Investigated Candidate Analog Sites**<br>• Lonar Crater (Basaltic impact, India)<br>• Ladakh High Desert (Periglacial arid, India)<br>• Rann of Kutch (Saline playa, India)<br>• Atacama Desert (Hyperarid Mars analog, Chile)<br>• Devon Island / Haughton (Polar impact crater, Canada)<br>• Askja / Holuhraun (Basaltic lava fields, Iceland)<br>• Death Valley (Hyperarid alluvial fans, USA)<br>• McMurdo Dry Valleys (Antarctic cold desert) | • Copernicus DEM GLO-30 & SRTM GL1<br>• Landsat 8/9 & Sentinel-2 MSI<br>• ECOSTRESS & MODIS LST<br>• ArcticDEM & REMA (Antarctica)<br>• GSI Bhukosh & ISRO Bhuvan | Field campaigns for rover traction testing, autonomous navigation, drill mechanisms, crew field training, and sensor calibration. |

---

## 🔬 Scientific Methodology Overview

COSMONOVA operates under four foundational methodological principles:

```
[Open Repositories] Earth (Copernicus/SRTM) | Moon (LOLA/Diviner) | Mars (MOLA-HRSC/THEMIS)
       ↓
[Data Acquisition] Manifest-guided downloads via STAC, earthaccess, PDS Geosciences
       ↓
[Quality Assessment] Coverage verification, latitude validity bounds, void/cloud masking
       ↓
[Geospatial Preprocessing] Planetary CRS harmonization (IAU Moon/Mars, WGS84) & matched GSD resampling
       ↓
[Feature Extraction] Tier A (Direct Terrain), Tier B (Thermal), Tier C (Composition), Tier D (Invariants)
       ↓
[Statistical Evaluation] Wasserstein-1 slope metric + Mahalanobis distance + SMAA weight acceptability
       ↓
[Uncertainty Assessment] Spatial block bootstrapping (variogram calibrated) + Monte Carlo DEM error
       ↓
[Interactive Exploration] Streamlit scientific dashboard + dual-body GIS maps + failure matrix cards
```

### The Four Comparability Tiers
1. **Tier A (Direct Equivalents)**: Topographic variables sharing identical sensor physics (slope distributions, multi-scale RMS roughness). Resampled to matched spatial baselines and evaluated via Wasserstein-1 and Mahalanobis distances.
2. **Tier B (Physical Equivalents with Boundary Shifts)**: Properties like surface skin temperature and diurnal thermal amplitude, which participate in distance formulations with explicit variance inflation penalties.
3. **Tier C (Proxy / Indirect Indices)**: Mineral band ratios and modeled thermal inertia, reported as qualitative secondary dimensions and never averaged directly into topographic scores.
4. **Tier D (Invariant Physical Failures)**: Invariant planetary physics (surface gravity, ambient vacuum, unshielded cosmic radiation, PSR cryogenic temperatures <40 K). **Strictly excluded from numerical similarity scores** and presented as primary Invariant Failure Flags.

---

## 💻 Main Application Features

COSMONOVA includes an interactive research dashboard built on Streamlit with a clean, light scientific visual theme:

- **1. Overview & Vision**: System architecture roadmap, four foundational scientific principles, and challenge alignment metrics.
- **2. Candidate Analog Explorer**: Interactive dual-view Plotly geospatial map featuring global candidate distribution, regional inset focus on the Indian subcontinent (Lonar, Ladakh, Rann of Kutch), evidence classification badges (Published, Exploratory, Speculative), and complete candidate scientific dossiers.
- **3. Dataset Catalogue (28 Products)**: Filterable, searchable inventory of 28 verified open datasets spanning Earth, Moon, and Mars with direct repository URLs and documented sensor limitations.
- **4. Comparability Tiers & Failure Analysis**: Methodological segregation schema and candidate-specific failure cards comparing planned Tier A/B parameters against Tier D invariant physical mismatches.
- **5. Technical Document Viewer**: In-dashboard reader for all 16 project specifications, methodologies, and architectural plans.
- **6. Verified Hackathon Schedule**: 48-hour execution milestone breakdown (H0–H48) and pre-defined scope reduction plan.

---

## 🛠️ Technology Stack

| Domain | Technology / Library | Application Purpose |
| :--- | :--- | :--- |
| **Core Language** | Python 3.11+ (tested on Python 3.13) | Computational backend and pipeline orchestration |
| **Data & Scientific** | NumPy, Pandas, SciPy, Scikit-Learn | Statistical distance metrics, matrix operations, data wrangling |
| **Geospatial Processing** | GeoPandas, Rasterio, Xarray, Shapely, PyProj | Raster elevation processing, CRS transforms, spatial tiling |
| **Visualization** | Plotly, PyDeck, Matplotlib | Interactive global/regional maps, vector charts, scatter geos |
| **Web Application** | Streamlit | Responsive, light scientific research dashboard |
| **Interactive Development** | JupyterLab, IPyKernel | Exploratory data analysis notebooks and verification |
| **Code Quality** | Flake8, Black | PEP 8 compliance and code formatting |

---

## 📁 Repository Structure

```
cosmonova/ (repository directory)
│
├── app.py                             # Interactive Streamlit scientific explorer dashboard
├── check_env.py                       # Automated system environment and dependency audit
├── requirements.txt                   # Project Python dependencies
├── CONTRIBUTING.md                    # Scientific contribution and git workflow guidelines
├── PROJECT_VISION.md                  # Problem statement, solution direction, and user needs
├── README.md                          # Comprehensive project documentation
│
├── docs/                              # Technical and scientific documentation
│   ├── challenge_understanding.md     # NASA challenge analysis and scoring alignment
│   ├── scientific_background.md       # Terrestrial analog fundamentals & literature
│   ├── lunar_environments.md          # Artemis South Pole target reference models
│   ├── martian_environments.md        # Mars crater & playa reference target models
│   ├── earth_analog_candidates.md     # 8 candidate sites scientific characterization
│   ├── dataset_catalogue.md           # 28 catalogued open datasets across Earth/Moon/Mars
│   ├── statistical_methodology.md     # Mathematical comparison framework (Wasserstein/SMAA)
│   ├── technical_architecture.md      # Modular pipeline and system architecture
│   ├── ui_ux_design_specification.md  # Scientific UI design principles and wireframes
│   ├── innovation_strategy.md         # Novelty, differentiation, and feasibility strategy
│   ├── scientific_limitations.md      # Honest caveats, constraints, and failure boundaries
│   └── references.md                  # Comprehensive bibliography and data repository links
│
├── planning/                          # Project management and execution plans
│   ├── hackathon_timeline.md          # 48-hour milestone execution schedule
│   ├── development_roadmap.md         # Pre-hackathon vs hackathon execution phases
│   ├── team_roles.md                  # 4-person domain specialization matrix
│   └── risk_register.md              # 15 identified scientific and technical risks
│
├── diagrams/                          # Architecture and workflow diagrams
│   └── README.md                      # Diagram index and Mermaid architecture sources
│
├── research/                          # Research dossiers and field literature
│   ├── earth_locations/               # Per-site terrestrial field research notes
│   ├── moon/                          # Lunar environment and orbital altimetry notes
│   ├── mars/                          # Martian crater and thermal inertia notes
│   └── nasa_datasets/                 # NASA PDS and Earthdata exploration logs
│
└── environment/                       # Environment configuration
    └── setup_guide.md                 # Complete platform installation and setup guide
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone <repository-url>
cd cosmonova  # or cd <cloned-folder-name>
```

### 2. Create and Activate Virtual Environment
```powershell
# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run System Environment Verification
Verify that your core scientific libraries, Python environment, and visualization packages are ready:
```bash
python check_env.py
```

### 5. Launch the COSMONOVA Streamlit Application
```bash
streamlit run app.py
```
The application will launch automatically in your browser at `http://localhost:8501`.

---

## ⚖️ Scientific Limitations & Disclaimers

1. **Pre-Hackathon Preparation Notice**: In strict accordance with hackathon competition rules, this repository contains preparation materials, literature inventories, data source manifests, and architectural designs. **No algorithmic scoring models or ranking calculations have been pre-computed.** All similarity pipelines will be executed during the competition weekend from raw open datasets.
2. **Terrestrial Analogs are Always Partial**: No Earth location can simultaneously replicate the Moon or Mars across all physical dimensions. Analog fidelity is strictly objective-dependent.
3. **Tier D Physical Impossibilities**: Fundamental planetary parameters — including lunar gravity ($1.62\text{ m/s}^2$), hard vacuum ($<10^{-10}\text{ Pa}$), solar cosmic ray exposure, and lunar south-polar Permanently Shadowed Region (PSR) cold-trap temperatures ($<40\text{ K}$) — cannot be replicated in outdoor Earth field sites.
4. **Candidate Sites as Hypotheses**: Evaluated sites (such as Lonar Crater, Ladakh, and Rann of Kutch) represent research screening hypotheses with varying evidence levels (from peer-reviewed literature to speculative hypotheses), not validated operational choices.

---

## 📄 License

This project is developed for the **NASA Space Apps Challenge 2026** under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments & Data Providers

- [NASA Space Apps Challenge](https://www.spaceappschallenge.org/)
- [NASA Earthdata](https://www.earthdata.nasa.gov/) & [LP DAAC](https://lpdaac.usgs.gov/)
- [NASA Planetary Data System (PDS)](https://pds.nasa.gov/)
- [USGS Astrogeology Science Center](https://astrogeology.usgs.gov/)
- [ESA Copernicus Open Access Hub](https://dataspace.copernicus.eu/)
- [ISRO Indian Space Science Data Centre (ISSDC)](https://pradan.issdc.gov.in/) & [Bhuvan](https://bhuvan.nrsc.gov.in/)
