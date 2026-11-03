"""
Terrain Intelligence — Pre-Hackathon Interactive Research Explorer
NASA Space Apps Challenge 2026 Preparation
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
from pathlib import Path

st.set_page_config(
    page_title="Terrain Intelligence | NASA Space Apps 2026",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for scientific styling
st.markdown("""
<style>
    .main-header { font-size: 2.2rem; font-weight: 700; color: #00E5FF; margin-bottom: 0px; }
    .sub-header { font-size: 1.1rem; color: #8892B0; margin-bottom: 25px; }
    .card-metric { background-color: #112240; padding: 16px; border-radius: 8px; border-left: 4px solid #00E5FF; }
    .card-failure { background-color: #2D1517; padding: 16px; border-radius: 8px; border-left: 4px solid #FF1744; }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.image("https://www.spaceappschallenge.org/static/images/space-apps-logo.svg", width=220)
st.sidebar.title("🌍 Terrain Intelligence")
st.sidebar.caption("NASA Space Apps 2026 · Pre-Hackathon Preparation")

menu = st.sidebar.radio(
    "Navigation",
    ["Overview & Vision", "Candidate Analog Explorer", "Dataset Catalogue", "Comparability Tiers & Failure Analysis", "Document Viewer", "Hackathon Timeline"]
)

BASE_DIR = Path(__file__).resolve().parent

# 1. OVERVIEW & VISION
if menu == "Overview & Vision":
    st.markdown('<div class="main-header">TERRAIN INTELLIGENCE</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Mission-Specific Earth Analog Discovery for Lunar and Martian Exploration</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Hackathon Starts", value="Nov 14, 2026")
    with col2:
        st.metric(label="Target Bodies", value="Moon & Mars")
    with col3:
        st.metric(label="Earth Candidates", value="8 Investigated")
    with col4:
        st.metric(label="Catalogued Datasets", value="28 Open Products")

    st.info("**Challenge Statement:** Identify Earth Locations that Analog the Permanent Moon Base Locations and Mars.")

    st.markdown("""
    ### Scientific Core Principles
    1. **Never a Single Scalar**: Analog fidelity is multi-dimensional. No Earth site matches Moon or Mars across all physical domains.
    2. **Analog Failure Analysis**: What an analog *cannot* match (gravity, vacuum, radiation, cryogenic PSR cold) is reported as first-class scientific data.
    3. **Matched Spatial Baseline**: DEM derivatives (slope, roughness) are always harmonized to a common spatial resolution before comparison.
    4. **Uncertainty Propagation**: Every similarity estimation is accompanied by spatial block bootstrap confidence bounds.
    """)

    st.markdown("### Conceptual Architecture Pipeline")
    st.code("""
    Data Sources (Earth / Moon / Mars)
           ↓
    Data Acquisition (earthaccess / STAC / PDS)
           ↓
    Data Quality Assessment (Coverage fraction & vertical error profiling)
           ↓
    Geospatial Preprocessing (CRS harmonization & matched-baseline resampling)
           ↓
    Scientific Feature Extraction (Terrain, thermal, lithology by comparability tiers)
           ↓
    Statistical Evaluation (Mahalanobis / Wasserstein distances & SMAA MCDA)
           ↓
    Uncertainty Assessment (Spatial block bootstrap & Monte Carlo error)
           ↓
    Visualization & Reporting (Interactive maps & analog failure cards)
    """, language="text")

# 2. CANDIDATE ANALOG EXPLORER
elif menu == "Candidate Analog Explorer":
    st.markdown('<div class="main-header">Earth Analog Candidates Explorer</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Geographic and geological profile of candidate screening locations</div>', unsafe_allow_html=True)

    candidates = [
        {"Site": "Atacama Desert", "Country": "Chile", "Lat": -24.5, "Lon": -69.2, "Type": "Hyperarid / Salars", "Target": "Mars Soil / Microbes", "Status": "Published Literature", "Caveat": "Pressure 50-60 kPa, Gravity, Fog events"},
        {"Site": "Devon Island / Haughton", "Country": "Canada", "Lat": 75.4, "Lon": -89.8, "Type": "Polar Desert Impact", "Target": "Mars / Moon Impact Geology", "Status": "Published Literature", "Caveat": "Arctic latitude limits SRTM (must use ArcticDEM)"},
        {"Site": "Askja / Holuhraun", "Country": "Iceland", "Lat": 65.0, "Lon": -16.7, "Type": "Basaltic Lava Fields", "Target": "Lunar Mare Volcanism", "Status": "Published Literature", "Caveat": "Water-rich maritime climate, vegetation"},
        {"Site": "Death Valley", "Country": "USA", "Lat": 36.5, "Lon": -117.0, "Type": "Hot Desert / Playas", "Target": "Mars Fan & Playa Morphology", "Status": "Published Literature", "Caveat": "Hot regime; Earth gravity & pressure"},
        {"Site": "McMurdo Dry Valleys", "Country": "Antarctica", "Lat": -77.5, "Lon": 162.0, "Type": "Hyperarid Cold Permafrost", "Target": "Mars Subsurface Ice", "Status": "Published Literature", "Caveat": "No SRTM coverage (REMA required); extreme logistics"},
        {"Site": "Lonar Crater", "Country": "India", "Lat": 19.98, "Lon": 76.51, "Type": "Basaltic Target Impact", "Target": "Lunar Mare / Mars Basalt", "Status": "Published Literature", "Caveat": "Small (1.8 km), monsoon precipitation, vegetation"},
        {"Site": "Ladakh High Desert", "Country": "India", "Lat": 34.2, "Lon": 77.6, "Type": "High-Altitude Cold Desert", "Target": "Mars Periglacial / Moon Cold", "Status": "Screening Hypothesis", "Caveat": "Pressure still half sea level; mineralogy unproven"},
        {"Site": "Rann of Kutch", "Country": "India", "Lat": 23.8, "Lon": 70.0, "Type": "Seasonal Salt Flat", "Target": "Mars Playa Trafficability", "Status": "High-Risk Hypothesis", "Caveat": "Flat terrain unlike rugged lunar pole; monsoon flooded"}
    ]
    df_sites = pd.DataFrame(candidates)

    fig = px.scatter_geo(
        df_sites,
        lat="Lat",
        lon="Lon",
        hover_name="Site",
        color="Status",
        size=[12]*len(df_sites),
        color_discrete_map={"Published Literature": "#00E5FF", "Screening Hypothesis": "#FFC107", "High-Risk Hypothesis": "#FF1744"},
        projection="natural earth",
        title="Global Earth Analog Screening Locations"
    )
    fig.update_geos(showcountries=True, countrycolor="#444444", showland=True, landcolor="#1A1F2C", bgcolor="#0E1117")
    fig.update_layout(paper_bgcolor="#0E1117", font_color="#FFFFFF", margin={"r":0,"t":40,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)

    selected_site = st.selectbox("Inspect Site Profile", df_sites["Site"])
    site_data = df_sites[df_sites["Site"] == selected_site].iloc[0]

    c1, c2, c3 = st.columns(3)
    c1.metric("Environment Type", site_data["Type"])
    c2.metric("Primary Target Potential", site_data["Target"])
    c3.metric("Evidence Level", site_data["Status"])

    st.warning(f"**Key Limitation / Physics Mismatch:** {site_data['Caveat']}")

# 3. DATASET CATALOGUE
elif menu == "Dataset Catalogue":
    st.markdown('<div class="main-header">NASA & Agency Dataset Inventory</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Structured catalogue of open Earth, Moon, and Mars data assets</div>', unsafe_allow_html=True)

    datasets = [
        {"Body": "Earth", "Dataset": "ASTER GDEM v3", "Agency": "NASA / METI", "Resolution": "~30 m", "Format": "GeoTIFF", "Access": "Open (Earthdata)", "Limitation": "Artifacts / noise at high relief"},
        {"Body": "Earth", "Dataset": "SRTM GL1 v003", "Agency": "NASA / NGA", "Resolution": "~30 m", "Format": "HGT / GeoTIFF", "Access": "Open (USGS)", "Limitation": "Cuts off at 60°N / 56°S"},
        {"Body": "Earth", "Dataset": "Copernicus DEM GLO-30", "Agency": "ESA", "Resolution": "30 m", "Format": "COG GeoTIFF", "Access": "AWS Open Data", "Limitation": "Surface model (canopy/structures)"},
        {"Body": "Earth", "Dataset": "ArcticDEM / REMA", "Agency": "PGC / NSF", "Resolution": "2-8 m", "Format": "GeoTIFF", "Access": "Open STAC", "Limitation": "Large file volumes"},
        {"Body": "Earth", "Dataset": "Landsat 8/9", "Agency": "USGS / NASA", "Resolution": "30m (TIRS 100m)", "Format": "COG", "Access": "Open", "Limitation": "Coarse mineral proxies"},
        {"Body": "Moon", "Dataset": "LOLA Altimeter", "Agency": "NASA LRO", "Resolution": "5-20 m (Polar)", "Format": "PDS / GeoTIFF", "Access": "PDS / Trek", "Limitation": "Interpolation between orbital tracks"},
        {"Body": "Moon", "Dataset": "LROC NAC", "Agency": "NASA / ASU", "Resolution": "0.5-2 m", "Format": "PDS / Tiles", "Access": "QuickMap", "Limitation": "Non-uniform lighting coverage"},
        {"Body": "Moon", "Dataset": "Diviner Radiometer", "Agency": "NASA / UCLA", "Resolution": "Hundreds of m", "Format": "Gridded PDS", "Access": "PDS Geosciences", "Limitation": "Local time sampling dependencies"},
        {"Body": "Mars", "Dataset": "MOLA-HRSC Blended DEM", "Agency": "USGS / NASA", "Resolution": "~200 m", "Format": "GeoTIFF", "Access": "USGS Astrogeology", "Limitation": "Coarser than Earth DEM baselines"},
        {"Body": "Mars", "Dataset": "THEMIS Thermal IR", "Agency": "NASA Odyssey", "Resolution": "~100 m", "Format": "PDS / GeoTIFF", "Access": "PDS Imaging", "Limitation": "Model-dependent thermal inertia"}
    ]
    df_datasets = pd.DataFrame(datasets)

    body_filter = st.multiselect("Filter by Planetary Body", ["Earth", "Moon", "Mars"], default=["Earth", "Moon", "Mars"])
    filtered_df = df_datasets[df_datasets["Body"].isin(body_filter)]
    st.dataframe(filtered_df, use_container_width=True)

# 4. COMPARABILITY TIERS & FAILURE ANALYSIS
elif menu == "Comparability Tiers & Failure Analysis":
    st.markdown('<div class="main-header">Comparability Tiers & Failure Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Separating comparable physical properties from invariant physical impossibilities</div>', unsafe_allow_html=True)

    st.markdown("""
    | Tier | Definition | Physical Example | Treatment in Terrain Intelligence |
    | :--- | :--- | :--- | :--- |
    | **Tier A** | Direct physical equivalence | Elevation, Slope, Roughness | Included in mathematical distance matrix |
    | **Tier B** | Same quantity, distinct physics | Skin Temperature / Thermal Swing | Distance with inflated uncertainty bound |
    | **Tier C** | Proxy relationship | Spectral band ratios, Thermal inertia | Categorical dimension; strong caveats |
    | **Tier D** | Invariant physical mismatch | Gravity, Vacuum, Radiation, PSR Cold | **NEVER in distance formula. Flagged as Failure** |
    """)

    st.markdown("### Conceptual Failure Analysis Card Generator")
    site_select = st.selectbox("Select Candidate to Preview Failure Card", ["Lonar Crater", "Ladakh Cold Desert", "Atacama Desert"])
    
    st.markdown(f"#### Analog Fidelity Card: {site_select} vs Lunar South Pole (Artemis Rim)")
    
    colA, colB = st.columns(2)
    with colA:
        st.markdown('<div class="card-metric"><h4>✅ Measured Analog Capabilities (Tier A & B)</h4>'
                    '<ul>'
                    '<li><b>Slope Distribution:</b> Matched baseline (30m) W1-distance: 0.18</li>'
                    '<li><b>Roughness Index:</b> Decameter RMS variation within target range</li>'
                    '<li><b>Lithology:</b> Shock-metamorphosed basaltic target (Lunar Mare analog)</li>'
                    '</ul></div>', unsafe_allow_html=True)
    with colB:
        st.markdown('<div class="card-failure"><h4>❌ Analog Failure Analysis (Tier D Invariants)</h4>'
                    '<ul>'
                    '<li><b>Surface Gravity:</b> 1.62 m/s² (Moon) vs 9.81 m/s² (Earth) — <i>Fails</i></li>'
                    '<li><b>Atmosphere:</b> Hard vacuum vs 101.3 kPa ambient air — <i>Fails</i></li>'
                    '<li><b>Cosmic Radiation:</b> Unshielded vs Magnetosphere protected — <i>Fails</i></li>'
                    '<li><b>PSR Cold Trap:</b> <40 K cryogenic environment — <i>No Earth counterpart</i></li>'
                    '</ul></div>', unsafe_allow_html=True)

# 5. DOCUMENT VIEWER
elif menu == "Document Viewer":
    st.markdown('<div class="main-header">Technical Workspace Document Viewer</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Read pre-hackathon specifications directly inside the workspace</div>', unsafe_allow_html=True)

    docs = {
        "Project Vision": "PROJECT_VISION.md",
        "Challenge Understanding": "docs/challenge_understanding.md",
        "Scientific Background": "docs/scientific_background.md",
        "Lunar Environments": "docs/lunar_environments.md",
        "Martian Environments": "docs/martian_environments.md",
        "Earth Analog Candidates": "docs/earth_analog_candidates.md",
        "Dataset Catalogue": "docs/dataset_catalogue.md",
        "Statistical Methodology": "docs/statistical_methodology.md",
        "Technical Architecture": "docs/technical_architecture.md",
        "UI/UX Design Specification": "docs/ui_ux_design_specification.md",
        "Innovation Strategy": "docs/innovation_strategy.md",
        "Scientific Limitations": "docs/scientific_limitations.md",
        "References": "docs/references.md",
        "Team Roles": "planning/team_roles.md",
        "Risk Register": "planning/risk_register.md",
        "Setup Guide": "environment/setup_guide.md"
    }

    selected_doc = st.selectbox("Select Document to View", list(docs.keys()))
    doc_path = BASE_DIR / docs[selected_doc]

    if doc_path.exists():
        with open(doc_path, "r", encoding="utf-8") as f:
            st.markdown(f.read())
    else:
        st.error(f"File not found: {docs[selected_doc]}")

# 6. HACKATHON TIMELINE
elif menu == "Hackathon Timeline":
    st.markdown('<div class="main-header">48-Hour Hackathon Execution Plan</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Structured execution roadmap for November 14–16, 2026</div>', unsafe_allow_html=True)

    st.markdown("""
    | Time Window | Block Focus | Milestone Deliverables |
    | :--- | :--- | :--- |
    | **H0 – H4** | **Scope Lock** | Lock MVP question; agree on 4 candidate sites; **no scope additions past H4** |
    | **H4 – H16** | **Data Pipeline** | Download LOLA tiles & Earth DEMs; CRS harmonization; matched baseline resampling |
    | **H16 – H28** | **Analysis & Uncertainty** | Wasserstein-1 slope distance; SMAA rank acceptability; block bootstrap CIs |
    | **H28 – H38** | **Visualization** | Interactive map; vector breakdown; analog failure cards in Streamlit |
    | **H38 – H44** | **Validation & Polish** | Validate with positive/negative controls; video recording; documentation |
    | **H44** | **CODE FREEZE** | Zero code edits past H44; submission packaging only |
    | **H44 – H48** | **Submission** | Final submission on Space Apps portal |
    """)

    st.error("""
    **Pre-Defined Scope Cut List (In order of elimination if behind schedule):**
    1. Cut second mission profile (habitat siting)
    2. Simplify thermal dimension to basic LST
    3. Drop interactive 3D map widgets for static charts
    4. Reduce Indian case study depth to literature mention
    5. Cut Mars comparison completely (focus 100% on Lunar South Pole)
    """)
