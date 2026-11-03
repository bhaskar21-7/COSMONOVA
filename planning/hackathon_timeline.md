# Hackathon Timeline

**48-Hour Execution Plan — November 14–16, 2026**

> [!IMPORTANT]
> This timeline is a plan, not a contract. Adjust in real time, but **do not add scope after H4**.

---

## Guiding Principles

1. **Lock scope early** — no new features after Hour 4
2. **Freeze code at H44** — last 4 hours are submission-only
3. **Cut features, not quality** — a credible small result beats a broken large one
4. **The cut list is pre-defined** — if running behind, cut in order (see below)

---

## Hour-by-Hour Plan

### Block 1: Scope Lock (H0–H4)

| Hour | Activity | Owner | Deliverable |
|------|----------|-------|-------------|
| H0 | Team sync; review MVP question | All | Verbal agreement |
| H1 | Confirm data access; download priority datasets | Data Lead | Downloaded tiles |
| H2 | Finalize feature list and comparison dimensions | Stats Lead | Written feature list |
| H3 | Set up Git repo structure; create branches | All | Repo initialized |
| H4 | **SCOPE LOCK** — no additions past this point | All | Signed scope document |

### Block 2: Data Pipeline (H4–H16)

| Hour | Activity | Owner | Deliverable |
|------|----------|-------|-------------|
| H4–H8 | Download and validate Earth DEMs for candidate sites | Data Lead | GeoTIFF tiles |
| H4–H8 | Download LOLA south-polar tiles | Data Lead | Lunar DEM tiles |
| H8–H12 | CRS harmonization; resample to matched baseline | Data Lead | Analysis-ready arrays |
| H8–H12 | Begin terrain feature extraction (slope, roughness) | Stats Lead | Feature arrays |
| H12–H16 | Complete feature extraction; compute target profile | Stats Lead | Target distribution |
| H12–H16 | Begin Streamlit scaffold; placeholder map | Viz Lead | Running app skeleton |

### Block 3: Analysis (H16–H28)

| Hour | Activity | Owner | Deliverable |
|------|----------|-------|-------------|
| H16–H20 | Distance computation (per dimension) | Stats Lead | Distance vectors |
| H20–H24 | Hard constraints + SMAA rank acceptability | Stats Lead | Rankings with sensitivity |
| H20–H24 | Failure-analysis table (data + literature Tier D) | Stats + Comms | Failure cards |
| H24–H28 | Block bootstrap uncertainty intervals | Stats Lead | CI bands |
| H24–H28 | Begin report draft | Comms Lead | Report skeleton |

### Block 4: Visualization (H28–H38)

| Hour | Activity | Owner | Deliverable |
|------|----------|-------|-------------|
| H28–H32 | Interactive map with candidate sites and target region | Viz Lead | Map component |
| H32–H36 | Vector comparison charts with CI bands | Viz Lead | Chart components |
| H36–H38 | Failure-analysis card rendering in Streamlit | Viz Lead | Card component |
| H28–H38 | Continue report; draft limitations section | Comms Lead | Report ~80% |

### Block 5: Validation & Write-up (H38–H46)

| Hour | Activity | Owner | Deliverable |
|------|----------|-------|-------------|
| H38–H40 | Validation: positive and negative controls | Stats Lead | Validation results |
| H40–H42 | Integration testing; fix bugs | All | Working demo |
| H42–H44 | Finalize report; record video | Comms Lead | Report + video |
| H44 | **CODE FREEZE** | All | — |
| H44–H46 | Final review; polish presentation | All | Submission-ready |

### Block 6: Submission (H46–H48)

| Hour | Activity | Owner | Deliverable |
|------|----------|-------|-------------|
| H46–H48 | Submit to NASA Space Apps platform | Comms Lead | **Submitted** |

---

## Pre-Defined Cut List

If running behind schedule, cut features **in this order**:

1. ~~Second mission profile (habitat siting)~~ — cut first
2. ~~Thermal dimension complexity~~ — simplify to basic LST comparison
3. ~~Interactive widgets~~ — use static charts instead
4. ~~Indian case study depth~~ — reduce to a mention with data note
5. ~~Mars comparison~~ — cut entirely if needed

> [!CAUTION]
> Cutting is not failure. A well-executed MVP with honest limitations scores higher than an ambitious but broken prototype.

---

## Division of Labour Summary

| Role | Primary Block | Secondary Block |
|------|--------------|----------------|
| Data & GIS Lead | H4–H16 (pipeline) | H38–H42 (integration) |
| Statistics Lead | H16–H28 (analysis) | H38–H40 (validation) |
| Visualization Lead | H28–H38 (viz) | H12–H16 (scaffold) |
| Communication Lead | H28–H46 (report/video) | H20–H24 (failure cards) |

---

*Document status: Pre-hackathon plan. Adjust during the event based on actual progress.*
