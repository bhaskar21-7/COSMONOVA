"""
Terrain Intelligence — Pre-Hackathon Research & Architecture Explorer
NASA Space Apps Challenge 2026 Preparation

SCIENTIFIC INTEGRITY NOTICE:
This application is a pre-hackathon preparation and documentation dashboard.
In strict compliance with competition rules:
- No final similarity scoring algorithms have been executed.
- No calculated distances (e.g., W1 distances) or ranking scores are presented.
- All candidate comparisons and schemas are illustrative architectural designs.
- All catalogued datasets and literature citations reference official, public scientific sources.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="Terrain Intelligence | Pre-Hackathon Architecture Explorer",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling for scientific clarity and integrity distinctions
st.markdown("""
<style>
    .main-header { font-size: 2.1rem; font-weight: 700; color: #00E5FF; margin-bottom: 2px; }
    .sub-header { font-size: 1.05rem; color: #94A3B8; margin-bottom: 20px; }
    .badge-prep { background-color: #1E293B; color: #38BDF8; padding: 4px 10px; border-radius: 4px; font-weight: 600; font-size: 0.85rem; border: 1px solid #0284C7; }
    .card-metric { background-color: #0F172A; padding: 18px; border-radius: 8px; border-left: 4px solid #38BDF8; margin-bottom: 12px; }
    .card-failure { background-color: #1C1917; padding: 18px; border-radius: 8px; border-left: 4px solid #EF4444; margin-bottom: 12px; }
    .card-hypothesis { background-color: #1E1B4B; padding: 18px; border-radius: 8px; border-left: 4px solid #F59E0B; margin-bottom: 12px; }
    .source-tag { font-size: 0.82rem; color: #94A3B8; }
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.image("https://www.spaceappschallenge.org/static/images/space-apps-logo.svg", width=200)
st.sidebar.title("🌍 Terrain Intelligence")
st.sidebar.markdown('<span class="badge-prep">PRE-HACKATHON PREPARATION</span>', unsafe_allow_html=True)
st.sidebar.caption("NASA Space Apps 2026 · Challenge Preparation")

menu = st.sidebar.radio(
    "Workspace Navigation",
    [
        "1. Overview & Vision",
        "2. Candidate Analog Explorer",
        "3. Dataset Catalogue (28 Products)",
        "4. Comparability Tiers & Failure Analysis",
        "5. Technical Document Viewer",
        "6. Verified Hackathon Schedule"
    ]
)

BASE_DIR = Path(__file__).resolve().parent

# ==============================================================================
# 1. OVERVIEW & VISION
# ==============================================================================
if menu == "1. Overview & Vision":
    st.markdown('<div class="main-header">TERRAIN INTELLIGENCE</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Mission-Specific Earth Analog Discovery for Lunar and Martian Exploration</div>', unsafe_allow_html=True)

    st.warning(
        "**Scientific Integrity Notice:** This workspace contains pre-hackathon preparation, literature review, "
        "and architectural specifications. **No final competition solution, calculated similarity metrics, or automated rankings have been executed.** "
        "All calculations will be performed during the competition weekend from raw open datasets."
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Hackathon Window", value="Nov 14–15, 2026")
    with col2:
        st.metric(label="Target Planetary Bodies", value="Moon & Mars")
    with col3:
        st.metric(label="Investigated Candidates", value="8 Locations")
    with col4:
        st.metric(label="Catalogued Datasets", value="28 Products")

    st.info(
        "**NASA Challenge:** *'Identify Earth Locations that Analog the Permanent Moon Base Locations and Mars.'*\n\n"
        "**Core Architectural Goal:** Enable researchers to compare terrestrial terrain against planetary targets using "
        "matched spatial baselines, multi-criteria decision analysis (MCDA), explicit failure flags for non-reproducible physics, "
        "and spatial uncertainty quantification."
    )

    st.markdown("### Four Foundational Scientific Principles")
    st.markdown("""
    1. **Rejection of Single Scalar Scores:** No single number can capture multi-dimensional planetary fidelity. We report distinct vector dimensions (Terrain, Thermal, Compositional) with explicit confidence bounds.
    2. **Primacy of Analog Failure Analysis:** What an Earth site *cannot* match (e.g., surface gravity, atmospheric vacuum, cosmic radiation, cryogenic PSR cold traps) is treated as first-class scientific output, not hidden in footnotes.
    3. **Matched Spatial Baseline Requirement:** DEM derivatives (slope, roughness) computed at 5 m on the Moon and 30 m on Earth cannot be directly compared without inducing resolution artifacts. All data must be resampled to a common ground sample distance (GSD).
    4. **Rigorous Uncertainty Propagation:** Pixels are spatially autocorrelated. Confidence intervals must use spatial block bootstrapping and DEM error perturbation rather than naive independent pixel resampling.
    """)

    st.markdown("### Proposed Processing Pipeline (Conceptual)")
    st.code("""
    [1. Open Data Sources] Earth (Copernicus/SRTM) | Moon (LOLA/Diviner) | Mars (MOLA-HRSC/THEMIS)
               ↓
    [2. Acquisition & Manifest] Hash-verified download pipelines (earthaccess, PDS, STAC APIs)
               ↓
    [3. Quality & Boundary Audit] Coverage verification, latitude bounds, void/cloud masking
               ↓
    [4. Geospatial Preprocessing] Coordinate harmonization (IAU Moon/Mars, WGS84) & matched GSD resampling
               ↓
    [5. Feature Extraction by Tier] Tier A (Direct), Tier B (Physical diff), Tier C (Proxy), Tier D (Invariant)
               ↓
    [6. Statistical Evaluation] Wasserstein-1 / Mahalanobis distances + SMAA Stochastic Acceptability
               ↓
    [7. Uncertainty Quantification] Spatial block bootstrap (variogram calibrated) + Monte Carlo error
               ↓
    [8. Reporting & Visualization] Dual-body geospatial maps + Invariant Analog Failure Matrix
    """, language="text")

# ==============================================================================
# 2. CANDIDATE ANALOG EXPLORER
# ==============================================================================
elif menu == "2. Candidate Analog Explorer":
    st.markdown('<div class="main-header">Earth Analog Candidates Explorer</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Systematic geological characterization and published literature status</div>', unsafe_allow_html=True)

    st.info(
        "**Evidence Level Classification:**\n"
        "- **Published Literature:** Site utilized in peer-reviewed planetary analog research or astronaut field training.\n"
        "- **Exploratory Research Hypothesis:** Documented extreme environment with preliminary analog rationale; mineralogic/morphologic fidelity unproven.\n"
        "- **Speculative / High-Risk Hypothesis:** Hypothesized site with no established planetary analog literature; significant morphologic mismatches exist."
    )

    candidates = [
        {
            "Site": "Atacama Desert (Chile)",
            "Lat": -24.5, "Lon": -69.2,
            "Environment": "Hyperarid desert, salars, extreme UV, volcanic terrain",
            "Analog Target": "Martian hyperarid soil, microbial habitability limits, rover traverse",
            "Evidence Level": "Published Literature",
            "Key Citation": "Navarro-González et al. (2003). Science 302, 1018.",
            "Terrain Fidelity": "High for regolith aridity & low organic content; volcanic substrate",
            "Invariant Mismatches": "Atmospheric pressure ~50–60 kPa at elevation (vs Mars ~0.6 kPa); Earth gravity (9.81 vs 3.71 m/s²); episodic coastal fog events.",
            "Data Coverage": "Excellent (SRTM, Copernicus GLO-30, Landsat, Sentinel-2, EMIT)."
        },
        {
            "Site": "Devon Island / Haughton (Canada)",
            "Lat": 75.4, "Lon": -89.8,
            "Environment": "Polar desert, ~23 km impact crater structure in sedimentary target, periglacial",
            "Analog Target": "Mars impact cratering, periglacial landforms, crewed field operational protocols",
            "Evidence Level": "Published Literature",
            "Key Citation": "Lee & Osinski (2005). Meteoritics & Planetary Science 40, 1759.",
            "Terrain Fidelity": "Moderate-high for degraded impact crater morphology and Arctic desert operations",
            "Invariant Mismatches": "Hydrological active season with liquid water run-off; lichen/microbial cover; temperature buffered compared to Mars.",
            "Data Coverage": "SRTM does NOT cover this latitude (>60°N). Must use Copernicus GLO-30 or ArcticDEM (~2m)."
        },
        {
            "Site": "Askja / Holuhraun (Iceland)",
            "Lat": 65.0, "Lon": -16.7,
            "Environment": "Basaltic lava fields, tuyas (subglacial volcanoes), hydrothermal alteration",
            "Analog Target": "Lunar mare volcanism, basaltic rover mobility, Apollo astronaut training heritage",
            "Evidence Level": "Published Literature",
            "Key Citation": "Historical Apollo field training; Mangold et al. (2011) Mars basalt weathering analogs.",
            "Terrain Fidelity": "High for basaltic flow morphology, vesicular textures, and palagonitization",
            "Invariant Mismatches": "Wet maritime climate, dynamic glacial melt, persistent atmospheric humidity and precipitation.",
            "Data Coverage": "Near SRTM cutoff limit. Requires Copernicus GLO-30, ArcticDEM, or Sentinel-2."
        },
        {
            "Site": "Death Valley (USA)",
            "Lat": 36.5, "Lon": -117.0,
            "Environment": "Hyperarid hot basin, alluvial fans, salt playas, active dune fields",
            "Analog Target": "Martian fan and playa geomorphology, rover mobility, extreme thermal swing",
            "Evidence Level": "Published Literature",
            "Key Citation": "Widely documented in planetary rover test campaigns and alluvial sedimentology.",
            "Terrain Fidelity": "High for gravelly alluvial slopes, evaporite salt crusts, and aeolian ripples",
            "Invariant Mismatches": "High summer temperatures (>45°C) contrast with Martian cryogenic cold; thick oxidizing atmosphere.",
            "Data Coverage": "Complete (30m SRTM GL1, 30m ASTER GDEM, Landsat 8/9, Sentinel-2, USGS 3DEP)."
        },
        {
            "Site": "McMurdo Dry Valleys (Antarctica)",
            "Lat": -77.5, "Lon": 162.0,
            "Environment": "Cold hyperarid polar desert, permafrost, sandstone ventifacts, ice-covered lakes",
            "Analog Target": "Martian cold-desert permafrost, subsurface ice dynamics, cryptoendolithic biology",
            "Evidence Level": "Published Literature",
            "Key Citation": "Marchant & Head (2007). Icarus 192, 187; McKay (2004).",
            "Terrain Fidelity": "Very high for sublimation permafrost and dry permafrost polygons",
            "Invariant Mismatches": "Zero SRTM coverage; thick atmosphere; ice sheet proximity; extreme logistical isolation.",
            "Data Coverage": "Must use REMA (Reference Elevation Model of Antarctica, 2–8m) and Landsat seasonal mosaics."
        },
        {
            "Site": "Lonar Crater (Maharashtra, India)",
            "Lat": 19.98, "Lon": 76.51,
            "Environment": "~1.8 km simple impact crater excavated entirely in Deccan flood basalt; alkaline saline lake",
            "Analog Target": "Impact cratering in basaltic targets (analog to Lunar Mare impacts and Martian basaltic crust)",
            "Evidence Level": "Published Literature",
            "Key Citation": "Hagerty & Newsom (2003). Meteoritics & Planetary Science 38, 1065.",
            "Terrain Fidelity": "High for basaltic impact breccia, shock metamorphism, and impact hydrothermal alteration",
            "Invariant Mismatches": "Monsoon climate (~800mm annual rain), heavy seasonal vegetation, human settlement and agricultural buffer.",
            "Data Coverage": "Good (30m SRTM, Copernicus GLO-30, Landsat, Sentinel-2, GSI Bhukosh maps)."
        },
        {
            "Site": "Ladakh High Desert (India)",
            "Lat": 34.2, "Lon": 77.6,
            "Environment": "High-altitude cold arid desert (3,000–5,500m ASL), periglacial sorted stone circles, ophiolites, saline lakes",
            "Analog Target": "Cold desert terrain trafficability, high UV radiation exposure, periglacial landforms",
            "Evidence Level": "Exploratory Research Hypothesis",
            "Key Citation": "Preliminary Indian space analog station concept proposals; astrobiological reconnaissance.",
            "Terrain Fidelity": "Moderate for cold arid periglacial slope processes; mineralogic Moon/Mars similarity unproven",
            "Invariant Mismatches": "Atmospheric pressure at 4,500m is ~57 kPa (over 90× Mars surface pressure); glacial melt streams.",
            "Data Coverage": "Good (30m SRTM, Copernicus GLO-30, Landsat, Sentinel-2, ISRO Bhuvan)."
        },
        {
            "Site": "Rann of Kutch (Gujarat, India)",
            "Lat": 23.8, "Lon": 70.0,
            "Environment": "Extensive seasonal salt mudflat, halite/gypsum crust, low relief playa",
            "Analog Target": "Martian playa trafficability and evaporite sediment crust testing (Hypothesis)",
            "Evidence Level": "Speculative / High-Risk Hypothesis",
            "Key Citation": "No established peer-reviewed planetary analog literature identified.",
            "Terrain Fidelity": "Weak for lunar polar terrain (flat plain vs rugged 25° crater rims); unverified for Mars sulfates",
            "Invariant Mismatches": "Annual monsoon inundation transforms the site into a shallow sea; marine evaporite chemistry differs from Mars acidic sulfates.",
            "Data Coverage": "Good (SRTM, Copernicus GLO-30, Sentinel-2). Must account for seasonal flooding."
        }
    ]
    df_sites = pd.DataFrame(candidates)

    fig = px.scatter_geo(
        df_sites,
        lat="Lat",
        lon="Lon",
        hover_name="Site",
        color="Evidence Level",
        size=[12]*len(df_sites),
        color_discrete_map={
            "Published Literature": "#00E5FF",
            "Exploratory Research Hypothesis": "#F59E0B",
            "Speculative / High-Risk Hypothesis": "#EF4444"
        },
        projection="natural earth",
        title="Candidate Terrestrial Analog Locations by Scientific Evidence Level"
    )
    fig.update_geos(showcountries=True, countrycolor="#334155", showland=True, landcolor="#0F172A", bgcolor="#0B0F17")
    fig.update_layout(paper_bgcolor="#0B0F17", font_color="#E2E8F0", margin={"r":0,"t":40,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)

    selected_site = st.selectbox("Inspect Evidence-Supported Site Dossier", df_sites["Site"])
    site = df_sites[df_sites["Site"] == selected_site].iloc[0]

    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown(f"### {site['Site']}")
        st.markdown(f"**Evidence Classification:** `{site['Evidence Level']}`")
        st.markdown(f"**Peer-Reviewed Literature Citation:** *{site['Key Citation']}*")
        st.markdown(f"**Geological Setting:** {site['Environment']}")
        st.markdown(f"**Specific Analog Target:** {site['Analog Target']}")
    with c2:
        st.markdown("### Documented Fidelity & Incompatibilities")
        st.markdown(f"**Analog Strengths:** {site['Terrain Fidelity']}")
        st.error(f"**Known Invariant Physical Mismatches:** {site['Invariant Mismatches']}")
        st.markdown(f"**Data Availability & Caveats:** {site['Data Coverage']}")

# ==============================================================================
# 3. DATASET CATALOGUE (28 PRODUCTS)
# ==============================================================================
elif menu == "3. Dataset Catalogue (28 Products)":
    st.markdown('<div class="main-header">NASA & Partner Agency Dataset Catalogue</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">28 Verified Open Datasets across Earth, Moon, and Mars</div>', unsafe_allow_html=True)

    st.caption("All datasets listed below are documented in `docs/dataset_catalogue.md` with official repository URLs.")

    all_datasets = [
        # EARTH DATASETS (13)
        {"ID": "E1", "Body": "Earth", "Dataset": "ASTER GDEM v3", "Agency": "NASA / METI (LP DAAC)", "Variable": "Surface Elevation", "Resolution": "~30 m", "Format": "GeoTIFF", "URL": "https://lpdaac.usgs.gov/products/astgtmv003/", "Limitation": "Stacking artifacts and cloud anomalies"},
        {"ID": "E2", "Body": "Earth", "Dataset": "SRTM GL1 v003", "Agency": "NASA / NGA (LP DAAC)", "Variable": "Radar Elevation", "Resolution": "~30 m", "Format": "HGT / GeoTIFF", "URL": "https://lpdaac.usgs.gov/products/srtmgl1v003/", "Limitation": "Coverage cuts off at 60°N and 56°S"},
        {"ID": "E3", "Body": "Earth", "Dataset": "Copernicus DEM GLO-30", "Agency": "ESA / Copernicus", "Variable": "Surface Elevation", "Resolution": "30 m", "Format": "COG GeoTIFF", "URL": "https://registry.opendata.aws/copernicus-dem/", "Limitation": "Digital surface model includes vegetation canopy"},
        {"ID": "E4", "Body": "Earth", "Dataset": "ArcticDEM", "Agency": "PGC (NSF/NGA funded)", "Variable": "High-Res Arctic Elevation", "Resolution": "~2 m mosaics", "Format": "GeoTIFF", "URL": "https://www.pgc.umn.edu/data/arcticdem/", "Limitation": "Large file volumes; Arctic region only"},
        {"ID": "E5", "Body": "Earth", "Dataset": "REMA (Reference Elevation Model of Antarctica)", "Agency": "PGC (NSF/NGA funded)", "Variable": "High-Res Antarctic Elevation", "Resolution": "~2–8 m", "Format": "GeoTIFF", "URL": "https://www.pgc.umn.edu/data/rema/", "Limitation": "Antarctica only; large files"},
        {"ID": "E6", "Body": "Earth", "Dataset": "Landsat 8/9 OLI/TIRS", "Agency": "USGS / NASA", "Variable": "Multispectral & Thermal IR", "Resolution": "30 m (TIRS 100 m)", "Format": "COG GeoTIFF", "URL": "https://www.usgs.gov/landsat-missions", "Limitation": "Thermal data is snapshot; 16-day revisit"},
        {"ID": "E7", "Body": "Earth", "Dataset": "Sentinel-2 MSI", "Agency": "ESA / Copernicus", "Variable": "13-Band Multispectral", "Resolution": "10 / 20 / 60 m", "Format": "SAFE / COG", "URL": "https://dataspace.copernicus.eu/", "Limitation": "Atmospheric & cloud masking required"},
        {"ID": "E8", "Body": "Earth", "Dataset": "MODIS (Terra/Aqua)", "Agency": "NASA GSFC", "Variable": "Land Surface Temp (LST) & Albedo", "Resolution": "250 m – 1 km", "Format": "HDF / GeoTIFF", "URL": "https://modis.gsfc.nasa.gov/", "Limitation": "Coarse spatial resolution; baseline climatology only"},
        {"ID": "E9", "Body": "Earth", "Dataset": "ECOSTRESS", "Agency": "NASA JPL (ISS)", "Variable": "Land Surface Temp & Emissivity", "Resolution": "~70 m", "Format": "HDF5 / GeoTIFF", "URL": "https://ecostress.jpl.nasa.gov/", "Limitation": "Irregular orbital precessing sampling times"},
        {"ID": "E10", "Body": "Earth", "Dataset": "EMIT", "Agency": "NASA JPL (ISS)", "Variable": "Imaging Spectroscopy (380–2500 nm)", "Resolution": "~60 m", "Format": "NetCDF", "URL": "https://earth.jpl.nasa.gov/emit", "Limitation": "Prioritized for arid dust zones; sparse global coverage"},
        {"ID": "E11", "Body": "Earth", "Dataset": "NASA POWER Climatology", "Agency": "NASA LaRC", "Variable": "Modeled Solar Radiation & Temp", "Resolution": "~0.5° grid", "Format": "JSON / CSV / NetCDF", "URL": "https://power.larc.nasa.gov/", "Limitation": "Coarse model output; not terrain-specific"},
        {"ID": "E12", "Body": "Earth", "Dataset": "GSI Bhukosh", "Agency": "Geological Survey of India", "Variable": "Lithology & Structure Maps", "Resolution": "1:50,000 / 1:250,000", "Format": "Shapefile / WMS", "URL": "https://bhukosh.gsi.gov.in/", "Limitation": "Access may require registration; portal stability"},
        {"ID": "E13", "Body": "Earth", "Dataset": "ISRO Bhuvan Thematic Layers", "Agency": "ISRO NRSC", "Variable": "Geospatial Thematic Layers", "Resolution": "Varies", "Format": "WMS / GeoTIFF", "URL": "https://bhuvan.nrsc.gov.in/", "Limitation": "Indian territorial bounds only; registration"},

        # MOON DATASETS (8)
        {"ID": "M1", "Body": "Moon", "Dataset": "LOLA (Lunar Orbiter Laser Altimeter)", "Agency": "NASA LRO", "Variable": "Topography, Slope, Roughness", "Resolution": "~5–20 m polar, tens of m global", "Format": "PDS IMG / GeoTIFF", "URL": "https://pds-geosciences.wustl.edu/missions/lro/lola.htm", "Limitation": "Interpolation between orbital tracks"},
        {"ID": "M2", "Body": "Moon", "Dataset": "LROC NAC (Narrow Angle Camera)", "Agency": "NASA LRO / ASU", "Variable": "Visible Surface Imagery", "Resolution": "~0.5–2 m/px", "Format": "PDS IMG / Web Tiles", "URL": "https://lroc.asu.edu/", "Limitation": "High solar phase variations; patchy high-res coverage"},
        {"ID": "M3", "Body": "Moon", "Dataset": "LROC WAC (Wide Angle Camera)", "Agency": "NASA LRO / ASU", "Variable": "Global Multispectral Imagery", "Resolution": "~100 m/px", "Format": "PDS IMG / Web Tiles", "URL": "https://quickmap.lroc.asu.edu/", "Limitation": "Coarse resolution for micro-topography"},
        {"ID": "M4", "Body": "Moon", "Dataset": "Diviner Lunar Radiometer", "Agency": "NASA LRO / UCLA", "Variable": "Surface Brightness Temp & Rock Abundance", "Resolution": "Hundreds of m", "Format": "PDS Gridded Tables", "URL": "https://diviner.ucla.edu/", "Limitation": "PSR temperatures are model-constrained"},
        {"ID": "M5", "Body": "Moon", "Dataset": "Unified Geologic Map of the Moon", "Agency": "USGS Astrogeology", "Variable": "Global Lithology & Chronology", "Resolution": "1:5,000,000 global", "Format": "GIS Vector Layers", "URL": "https://astrogeology.usgs.gov/", "Limitation": "Regional scale only; coarse for site planning"},
        {"ID": "M6", "Body": "Moon", "Dataset": "NASA Moon Trek Portal Layers", "Agency": "NASA JPL", "Variable": "Integrated Lunar GIS Products", "Resolution": "Varies by layer", "Format": "WMTS / GeoTIFF", "URL": "https://trek.nasa.gov/", "Limitation": "Web API endpoint throttling"},
        {"ID": "M7", "Body": "Moon", "Dataset": "QuickMap LROC Layers", "Agency": "ASU / NASA", "Variable": "Interactive Altimetry & Imagery", "Resolution": "Varies", "Format": "WMS / Tiles", "URL": "https://quickmap.lroc.asu.edu/", "Limitation": "Portal-centric viewer"},
        {"ID": "M8", "Body": "Moon", "Dataset": "Chandrayaan-2/3 Data Products", "Agency": "ISRO ISSDC", "Variable": "OHRC High-Res Imagery & Radar", "Resolution": "Sub-metre (OHRC)", "Format": "PDS4", "URL": "https://pradan.issdc.gov.in/", "Limitation": "ISSDC registration and access terms"},

        # MARS DATASETS (7)
        {"ID": "R1", "Body": "Mars", "Dataset": "MOLA (Mars Orbiter Laser Altimeter)", "Agency": "NASA MGS", "Variable": "Global Elevation", "Resolution": "~460 m/px", "Format": "PDS / GeoTIFF", "URL": "https://pds-geosciences.wustl.edu/", "Limitation": "Coarse baseline compared to Earth 30m DEMs"},
        {"ID": "R2", "Body": "Mars", "Dataset": "MOLA–HRSC Blended DEM", "Agency": "USGS Astrogeology", "Variable": "High-Quality Topography", "Resolution": "~200 m/px", "Format": "GeoTIFF", "URL": "https://astrogeology.usgs.gov/", "Limitation": "Interpolation across data seams"},
        {"ID": "R3", "Body": "Mars", "Dataset": "CTX (Context Camera)", "Agency": "NASA MRO", "Variable": "Panchromatic Imagery & DTMs", "Resolution": "~6 m/px", "Format": "PDS / Mosaics", "URL": "https://pds-imaging.jpl.nasa.gov/", "Limitation": "Stereo DTMs available only for targeted footprints"},
        {"ID": "R4", "Body": "Mars", "Dataset": "HiRISE (High Resolution Imaging Science)", "Agency": "NASA MRO / UArizona", "Variable": "Sub-metre Imagery & DTMs", "Resolution": "~25–50 cm/px", "Format": "JP2 / PDS", "URL": "https://www.uahirise.org/", "Limitation": "Covers <3% of Mars surface"},
        {"ID": "R5", "Body": "Mars", "Dataset": "THEMIS Thermal IR", "Agency": "NASA Odyssey / ASU", "Variable": "Thermal IR & Thermal Inertia", "Resolution": "~100 m/px", "Format": "PDS / GeoTIFF", "URL": "https://themis.asu.edu/", "Limitation": "Derived thermal inertia is model-dependent"},
        {"ID": "R6", "Body": "Mars", "Dataset": "CRISM Spectrometer", "Agency": "NASA MRO / JHU APL", "Variable": "Visible/Near-IR Hyperspectral", "Resolution": "18 m targeted, 200 m survey", "Format": "PDS IMG", "URL": "https://crism.jhuapl.edu/", "Limitation": "Cryocooler degradation; high processing complexity"},
        {"ID": "R7", "Body": "Mars", "Dataset": "NASA Mars Trek Portal Layers", "Agency": "NASA JPL", "Variable": "Integrated Mars GIS Products", "Resolution": "Varies", "Format": "WMTS / GeoTIFF", "URL": "https://trek.nasa.gov/", "Limitation": "Web portal rate limits"}
    ]
    df_cat = pd.DataFrame(all_datasets)

    b_filter = st.multiselect("Filter by Planetary Target", ["Earth", "Moon", "Mars"], default=["Earth", "Moon", "Mars"])
    filtered_cat = df_cat[df_cat["Body"].isin(b_filter)]

    st.markdown(f"**Showing {len(filtered_cat)} of {len(all_datasets)} catalogued open datasets:**")

    # Render formatted table with clickable URLs
    display_df = filtered_cat[["ID", "Body", "Dataset", "Agency", "Variable", "Resolution", "Format", "Limitation", "URL"]].copy()
    st.dataframe(
        display_df,
        column_config={
            "URL": st.column_config.LinkColumn("Official Repository URL")
        },
        use_container_width=True,
        hide_index=True
    )

# ==============================================================================
# 4. COMPARABILITY TIERS & FAILURE ANALYSIS
# ==============================================================================
elif menu == "4. Comparability Tiers & Failure Analysis":
    st.markdown('<div class="main-header">Comparability Tiers & Analog Failure Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Methodological segregation of comparable physics vs invariant physical mismatches</div>', unsafe_allow_html=True)

    st.warning(
        "**Integrity Clarification:** In previous drafts, illustrative numbers (such as a W1-distance of 0.18) "
        "were inadvertently shown. **No similarity calculations or numerical distances have been computed.** "
        "The cards below represent the qualitative scientific schema and physics boundaries established from peer-reviewed literature."
    )

    st.markdown("### The Four Scientific Comparability Tiers")
    st.markdown("""
    | Tier | Scientific Definition | Example Quantities | Mathematical Treatment |
    | :--- | :--- | :--- | :--- |
    | **Tier A** | Directly comparable physical property measured by equivalent sensor physics | Elevation, Slope distribution, Multi-scale RMS roughness | **Enters distance calculation** (Wasserstein-1 / Mahalanobis with shrinkage) |
    | **Tier B** | Same physical quantity, but strongly altered by planetary boundary conditions | Skin temperature, Diurnal temperature amplitude | **Enters distance with inflated variance penalty** and explicit caveats |
    | **Tier C** | Proxy relationship or indirect spectral index | Spectral band ratios, Thermal inertia derived from models | **Evaluated as separate qualitative dimension**; never blended directly with terrain |
    | **Tier D** | Fundamental, invariant planetary physics that Earth CANNOT reproduce | Gravity, Ambient atmospheric pressure, Radiation flux, PSR cryogenic cold | **STRICTLY EXCLUDED from numerical distance.** Reported as Invariant Failure Flags |
    """)

    st.markdown("---")
    st.markdown("### Conceptual Failure Analysis Schema (Design Template)")

    selected_site = st.selectbox("Select Candidate to Inspect Theoretical Failure Boundaries", ["Lonar Crater (India)", "Atacama Desert (Chile)", "Devon Island (Canada)"])

    colA, colB = st.columns(2)
    with colA:
        st.markdown('<div class="card-metric"><h4>📐 Tier A & B Analytical Properties (To Be Computed at Hackathon)</h4>'
                    '<ul>'
                    '<li><b>Slope Distribution:</b> Planned Wasserstein-1 distance on matched-baseline (30m) elevation models.<br>'
                    '<span class="source-tag">Status: <i>Pending pipeline execution during hackathon (No value calculated yet).</i></span></li>'
                    '<li><b>Surface Roughness:</b> Planned root-mean-square (RMS) height deviation at decameter baselines.<br>'
                    '<span class="source-tag">Status: <i>Pending pipeline execution during hackathon.</i></span></li>'
                    '<li><b>Thermal Range (Tier B):</b> Diurnal skin temperature comparison.<br>'
                    '<span class="source-tag">Status: <i>Requires MODIS/ECOSTRESS vs Diviner matching.</i></span></li>'
                    '</ul></div>', unsafe_allow_html=True)
    with colB:
        st.markdown('<div class="card-failure"><h4>❌ Invariant Physical Mismatches (Tier D Failures)</h4>'
                    '<ul>'
                    '<li><b>Surface Gravity:</b> 1.62 m/s² (Moon) / 3.71 m/s² (Mars) vs 9.81 m/s² (Earth).<br>'
                    '<span class="source-tag">Scientific Implication: Governs rover traction, slip, and regolith mechanics. Cannot be analoged on Earth surface.</span></li>'
                    '<li><b>Atmospheric Pressure:</b> Hard vacuum (<10⁻¹⁰ Pa, Moon) / ~600 Pa (Mars) vs 101.3 kPa (Earth).<br>'
                    '<span class="source-tag">Scientific Implication: Vacuum alteration and low-pressure dust lofting cannot be reproduced outdoors.</span></li>'
                    '<li><b>Cosmic Radiation:</b> Unshielded GCR & Solar Energetic Particles vs Earth magnetosphere shielding.<br>'
                    '<span class="source-tag">Scientific Implication: Radiation-induced material degradation requires laboratory simulation chambers.</span></li>'
                    '<li><b>PSR Cryogenic Cold:</b> Diviner measured temperatures <40 K in lunar south-polar permanent cold traps.<br>'
                    '<span class="source-tag">Scientific Implication: Earth\'s coldest natural surface (~184 K at Vostok) is >140 K warmer. Zero natural Earth thermal analog.</span></li>'
                    '</ul></div>', unsafe_allow_html=True)

    st.info(
        "**Why Failure Analysis is Our Key Differentiator:** Most hackathon projects output a misleading '95% match' score. "
        "Terrain Intelligence explicitly isolates what Earth *can* test (e.g. slope geometry, basaltic impact fractures) from what it *cannot* test (gravity, atmosphere, radiation)."
    )

# ==============================================================================
# 5. TECHNICAL DOCUMENT VIEWER
# ==============================================================================
elif menu == "5. Technical Document Viewer":
    st.markdown('<div class="main-header">Technical Workspace Document Viewer</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Review pre-hackathon documentation, research notes, and engineering blueprints</div>', unsafe_allow_html=True)

    docs = {
        "Project Vision & MVP Scope": "PROJECT_VISION.md",
        "Challenge Understanding & Rubric": "docs/challenge_understanding.md",
        "Scientific Background & Analogs": "docs/scientific_background.md",
        "Lunar Reference Environments": "docs/lunar_environments.md",
        "Martian Reference Environments": "docs/martian_environments.md",
        "Candidate Analog Dossier": "docs/earth_analog_candidates.md",
        "Dataset Catalogue (28 Products)": "docs/dataset_catalogue.md",
        "Statistical Methodology (MCDA/SMAA)": "docs/statistical_methodology.md",
        "Technical Architecture": "docs/technical_architecture.md",
        "UI/UX Conceptual Design": "docs/ui_ux_design_specification.md",
        "Innovation Strategy": "docs/innovation_strategy.md",
        "Scientific Limitations & Integrity": "docs/scientific_limitations.md",
        "References & Citations": "docs/references.md",
        "Team Roles & Allocation": "planning/team_roles.md",
        "Risk Register (15 Risks)": "planning/risk_register.md",
        "Environment Setup Guide": "environment/setup_guide.md"
    }

    selected_doc = st.selectbox("Select Documentation File to Read", list(docs.keys()))
    doc_path = BASE_DIR / docs[selected_doc]

    if doc_path.exists():
        with open(doc_path, "r", encoding="utf-8") as f:
            st.markdown(f.read())
    else:
        st.error(f"Documentation file not found: {docs[selected_doc]}")

# ==============================================================================
# 6. VERIFIED HACKATHON SCHEDULE
# ==============================================================================
elif menu == "6. Verified Hackathon Schedule":
    st.markdown('<div class="main-header">Verified Event Schedule & Execution Plan</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">NASA Space Apps Challenge 2026: Official Weekend November 14–15, 2026</div>', unsafe_allow_html=True)

    st.markdown("""
    ### Official Hackathon Timeline Structure
    - **Global Event Window:** Saturday, November 14, 2026 (09:00 local time) through Sunday, November 15, 2026 (23:59 local deadline).
    - **Total Duration:** 48 hours.
    - **Current Phase:** Pre-hackathon preparation, literature review, environment setup, and data architecture planning.
    """)

    st.markdown("### 48-Hour Sprint Milestone Breakdown")
    st.markdown("""
    | Milestone Block | Timeframe | Technical Objectives | Integrity Checkpoint |
    | :--- | :--- | :--- | :--- |
    | **Block 1: Scope Lock** | H0 – H4 | Lock MVP question; confirm 4 priority Earth sites; freeze scope additions. | Verify dataset URLs and credentials. |
    | **Block 2: Data Pipeline** | H4 – H16 | Ingest LOLA south-polar tiles & Earth DEMs; CRS planetary harmonization; resample to matched GSD. | Audit for spatial resolution mismatches. |
    | **Block 3: Statistical Evaluation** | H16 – H28 | Compute Wasserstein-1 slope distances; execute SMAA weight perturbation; block bootstrap CIs. | Enforce Tier D exclusion from distances. |
    | **Block 4: Visualization & UX** | H28 – H38 | Render dual-body maps, vector similarity bar charts, and analog failure cards in Streamlit. | Label all uncertainty bounds. |
    | **Block 5: Validation & Controls** | H38 – H42 | Evaluate positive controls (Atacama/Devon) and negative controls (rainforest). | Record actual sensitivity variance. |
    | **Block 6: Submission Freeze** | H42 – H48 | **Code Freeze at H44.** Final documentation, demonstration video recording, portal submission. | Ensure zero unsupported claims. |
    """)

    st.error("""
    **Pre-Defined Scope Cut List (In order of elimination if behind schedule):**
    1. Cut second mission profile (habitat siting) — focus exclusively on rover mobility.
    2. Simplify thermal dimension to basic surface temperature climatology.
    3. Drop interactive 3D mesh rendering for standard 2D elevation colormaps.
    4. Reduce Indian case study depth to published literature review of Lonar Crater.
    5. Cut Mars comparison completely — commit 100% of effort to Lunar South Pole Artemis candidate regions.
    """)
