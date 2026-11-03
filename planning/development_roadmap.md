# Development Roadmap

**COSMONOVA — Pre-Hackathon and Event Timeline**  
*Planetary Analog Intelligence Platform*

> [!NOTE]
> This roadmap separates **preparation activities** (allowed before the hackathon) from **implementation activities** (hackathon only). Do not build the competition solution during preparation.

---

## Phase 1: Preparation (Now → November 13, 2026)

**Goal**: Be ready to start coding at H0 with no setup delays.

### Week of Nov 3–9

| # | Task | Owner | Status |
|---|------|-------|--------|
| 1 | Set up Python virtual environment and install dependencies | All | ☐ |
| 2 | Verify dataset access: test one Earth DEM download (e.g., Copernicus GLO-30 tile) | Data Lead | ☐ |
| 3 | Verify dataset access: test one lunar LOLA product or Trek tile | Data Lead | ☐ |
| 4 | Create NASA Earthdata and Copernicus Data Space accounts | All | ☐ |
| 5 | Test GDAL/rasterio on one GeoTIFF file | Data Lead | ☐ |
| 6 | Read core papers (Mazarico 2011, Rosenburg 2011, Preston & Dartnell 2014) | All | ☐ |
| 7 | Review and finalize MVP question | All | ☐ |
| 8 | Assign team roles | All | ☐ |

### Week of Nov 10–13

| # | Task | Owner | Status |
|---|------|-------|--------|
| 9 | Write data manifest (URLs, checksums, licenses) | Data Lead | ☐ |
| 10 | Sketch UI wireframes for the dashboard | Viz Lead | ☐ |
| 11 | Draft report/presentation template | Comms Lead | ☐ |
| 12 | Review risk register and mitigation plans | All | ☐ |
| 13 | Test Streamlit locally with a placeholder page | Viz Lead | ☐ |
| 14 | Verify GSI Bhukosh / ISRO Bhuvan access for Indian sites | Data Lead | ☐ |
| 15 | **Final prep check**: environment works, data accessible, roles assigned | All | ☐ |

> [!WARNING]
> Do not build the scoring model, discovery engine, or app during preparation. Keep a dated prep log in case the rules require showing what pre-existed.

---

## Phase 2: Hackathon (November 14–16, 2026)

**48-hour execution plan**: See [`hackathon_timeline.md`](hackathon_timeline.md) for the detailed hour-by-hour schedule.

### Summary Blocks

| Block | Hours | Goal |
|-------|-------|------|
| **Scope Lock** | H0–H4 | Lock MVP question, sites, features. No scope additions after this |
| **Data Pipeline** | H4–H16 | Tiles, matched baselines, terrain features, lunar target profile |
| **Analysis** | H16–H28 | Distance + constraints + bootstrap + SMAA; failure-analysis table |
| **Visualization** | H28–H38 | Map/visual interface, report template |
| **Validation & Write-up** | H38–H46 | Validation with controls, write-up, limitations, video |
| **Submission** | H46–H48 | Submit. **Freeze code at H44.** |

---

## Phase 3: Post-Hackathon (Optional)

If the project continues beyond the hackathon:
- Publish code and documentation on GitHub
- Expand to additional Earth candidate sites
- Add Mars comparison dimension
- Refine uncertainty quantification
- Seek feedback from planetary science community

---

*Document status: Pre-hackathon roadmap. Update task statuses as they are completed.*
