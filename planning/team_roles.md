# Team Roles

**Terrain Intelligence — NASA Space Apps Challenge 2026**

> [!NOTE]
> This document defines recommended team roles for the hackathon. Assignments should be made before the event starts.

---

## Recommended Structure (4-Person Team)

| Role | Responsibility | Key Skills | Must NOT Also Do |
|------|---------------|------------|-----------------|
| **Data & GIS Lead** | Data acquisition, CRS management, raster preprocessing, tiling | GDAL/rasterio, xarray, planetary CRS, earthaccess | Should not also fix statistics bugs |
| **Statistics Lead** | Feature extraction, distance computation, SMAA, uncertainty | NumPy/SciPy, scikit-learn, block bootstrap, MCDA | Should not also fix pipeline issues |
| **Visualization Lead** | Interactive map, comparison charts, failure-analysis cards, Streamlit app | Plotly, PyDeck, Streamlit, matplotlib | Should not also wrangle PDS formats |
| **Communication Lead** | Write-up, video, presentation, limitations documentation, submission | Scientific writing, presentation, video editing | Should not also write analysis code |

---

## Role Principles

1. **Each person owns one domain** — clear accountability reduces merge conflicts and scope creep.
2. **The Statistics Lead must not also be the pipeline fixer** — this was identified as a critical risk in the research report.
3. **The Communication Lead starts working at H28** (halfway), not at H44 — rushed write-ups lose "validity" points.
4. **Everyone reads the MVP question before starting** — no scope additions after H4.

---

## Pre-Hackathon Responsibilities

| Person | Pre-Hackathon Task |
|--------|--------------------|
| Data & GIS Lead | Test dataset downloads; verify CRS handling; set up data manifest |
| Statistics Lead | Review methodology document; implement no code, but understand the distance framework |
| Visualization Lead | Sketch UI wireframes; choose Plotly vs PyDeck for the map; test Streamlit locally |
| Communication Lead | Draft report template; prepare video storyboard; review judging rubric |

---

## Team Assignments

| Role | Name | Contact |
|------|------|---------|
| Data & GIS Lead | *[To be assigned]* | |
| Statistics Lead | *[To be assigned]* | |
| Visualization Lead | *[To be assigned]* | |
| Communication Lead | *[To be assigned]* | |

---

*Document status: Template. Assign team members before the hackathon.*
