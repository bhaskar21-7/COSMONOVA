# 🌍 TERRAIN INTELLIGENCE

**Mission-Specific Earth Analog Discovery for Lunar and Martian Exploration**

[![NASA Space Apps 2026](https://img.shields.io/badge/NASA_Space_Apps-2026-blue)]()
[![Status: Pre-Hackathon Preparation](https://img.shields.io/badge/Status-Pre--Hackathon_Preparation-orange)]()
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-green)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)]()

> **NASA Space Apps Challenge 2026**
> *"Identify Earth Locations that Analog the Permanent Moon Base Locations and Mars"*
>
> Hackathon Date: November 14, 2026

---

## 🎯 What Is This?

Terrain Intelligence is a scientific software project designed to help researchers:

- **Identify** potential Earth analog locations for lunar and Martian environments
- **Compare** Earth terrain with Moon and Mars surface characteristics
- **Evaluate** geological, geomorphic, and thermal similarities
- **Assess** locations for specific mission requirements (rover mobility, habitat siting)
- **Quantify** uncertainty and scientific limitations of analog comparisons
- **Visualize** multi-dimensional findings on interactive maps

> [!IMPORTANT]
> This repository contains **preparation materials only** — documentation, research organization, environment configuration, and architecture planning. The competition solution will be built during the hackathon event (Nov 14, 2026).

---

## 📁 Repository Structure

```
terrain-intelligence/
│
├── README.md                          # This file
├── PROJECT_VISION.md                  # Problem statement, solution direction, users
├── CONTRIBUTING.md                    # Contribution guidelines
├── requirements.txt                   # Python dependencies (for hackathon use)
│
├── docs/                              # Technical and scientific documentation
│   ├── challenge_understanding.md     # NASA challenge analysis
│   ├── scientific_background.md       # Analog science fundamentals
│   ├── lunar_environments.md          # Moon target environments
│   ├── martian_environments.md        # Mars target environments
│   ├── earth_analog_candidates.md     # Candidate Earth sites
│   ├── dataset_catalogue.md           # Structured dataset inventory
│   ├── statistical_methodology.md     # Statistical framework
│   ├── technical_architecture.md      # System architecture
│   ├── innovation_strategy.md         # Differentiation and novelty
│   ├── scientific_limitations.md      # Known constraints and gaps
│   └── references.md                  # Bibliography and source URLs
│
├── research/                          # Research artifacts (populated during prep)
│   ├── earth_locations/               # Per-site research notes
│   ├── moon/                          # Lunar environment research
│   ├── mars/                          # Martian environment research
│   └── nasa_datasets/                 # Dataset exploration notes
│
├── planning/                          # Project management
│   ├── team_roles.md                  # Team structure and responsibilities
│   ├── development_roadmap.md         # Pre-hackathon and event roadmap
│   ├── hackathon_timeline.md          # 48-hour execution plan
│   └── risk_register.md              # Technical and scientific risks
│
├── diagrams/                          # Architecture and workflow diagrams
│
└── environment/                       # Development environment
    └── setup_guide.md                 # Environment setup instructions
```

---

## 🛠 Technology Stack

| Category | Tools |
|----------|-------|
| **Programming** | Python 3.11+ |
| **Data Analysis** | Pandas, NumPy, SciPy, Scikit-learn |
| **Geospatial** | GeoPandas, Rasterio, Xarray, Shapely, PyProj |
| **Visualization** | Plotly, PyDeck |
| **Application** | Streamlit |
| **Development** | VS Code, Git, GitHub, Jupyter Notebook |

See [`environment/setup_guide.md`](environment/setup_guide.md) for detailed setup instructions.

---

## 🚀 Getting Started

> [!NOTE]
> These instructions are for **pre-hackathon preparation**. The full application will be developed during the event.

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd terrain-intelligence
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Read the documentation**
   - Start with [`PROJECT_VISION.md`](PROJECT_VISION.md)
   - Review [`docs/challenge_understanding.md`](docs/challenge_understanding.md)
   - Study [`docs/dataset_catalogue.md`](docs/dataset_catalogue.md)

---

## 📊 Scientific Integrity

This project adheres to strict scientific standards:

- All datasets reference official NASA, ESA, USGS, and ISRO sources
- No fabricated data, API endpoints, or scientific results
- Candidate analog sites are presented as **hypotheses**, not validated claims
- Uncertainty is quantified and reported, never hidden
- Limitations are documented alongside capabilities

See [`docs/scientific_limitations.md`](docs/scientific_limitations.md) for details.

---

## 📄 License

This project is prepared for the NASA Space Apps Challenge 2026. See the challenge rules for submission terms.

---

## 🙏 Acknowledgments

- [NASA Space Apps Challenge](https://www.spaceappschallenge.org/)
- [NASA Earthdata](https://www.earthdata.nasa.gov/)
- [NASA Planetary Data System](https://pds.nasa.gov/)
- [USGS Astrogeology](https://astrogeology.usgs.gov/)
- [ESA Copernicus](https://dataspace.copernicus.eu/)
