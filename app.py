"""
Terrain Intelligence — Pre-Hackathon Research & Architecture Explorer
NASA Space Apps Challenge 2026 Preparation

LIGHT SCIENTIFIC DESIGN SYSTEM
A clean, professional planetary-science dashboard for analog candidate research,
dataset exploration, comparability tier classification, and failure analysis.
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(
    page_title="Terrain Intelligence | NASA Space Apps 2026",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
# PROFESSIONAL LIGHT SCIENTIFIC DESIGN SYSTEM (CSS)
# ==============================================================================
st.markdown("""
<style>
    /* Base typography & palette */
    html, body, [class*="css"] {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        color: #1E293B;
    }
    
    /* Header typography */
    .main-header {
        font-size: 2.1rem;
        font-weight: 750;
        color: #0F172A; /* Dark Navy */
        letter-spacing: -0.025em;
        margin-bottom: 2px;
        line-height: 1.2;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #475569; /* Slate Grey */
        margin-bottom: 22px;
        font-weight: 400;
        line-height: 1.4;
    }
    .section-title {
        font-size: 1.25rem;
        font-weight: 650;
        color: #0F172A;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    /* Badges */
    .badge-prep {
        background-color: #E0F2FE;
        color: #0369A1;
        padding: 4px 10px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.8rem;
        border: 1px solid #BAE6FD;
        display: inline-block;
    }
    .badge-published {
        background-color: #E0F2FE;
        color: #0369A1;
        padding: 3px 9px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.78rem;
        border: 1px solid #BAE6FD;
        display: inline-block;
    }
    .badge-exploratory {
        background-color: #FEF3C7;
        color: #92400E;
        padding: 3px 9px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.78rem;
        border: 1px solid #FDE68A;
        display: inline-block;
    }
    .badge-speculative {
        background-color: #FEE2E2;
        color: #991B1B;
        padding: 3px 9px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.78rem;
        border: 1px solid #FECACA;
        display: inline-block;
    }

    /* Cards (Light Scientific Theme) */
    .card-light {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 18px 20px;
        margin-bottom: 14px;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04);
    }
    .card-tier-a {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-left: 5px solid #0284C7;
        border-radius: 6px;
        padding: 18px 20px;
        margin-bottom: 14px;
    }
    .card-tier-d {
        background-color: #FFFBFB;
        border: 1px solid #FEE2E2;
        border-left: 5px solid #DC2626;
        border-radius: 6px;
        padding: 18px 20px;
        margin-bottom: 14px;
    }

    /* Text details */
    .source-tag {
        font-size: 0.82rem;
        color: #64748B;
        font-style: italic;
    }
    .metric-title {
        font-size: 0.85rem;
        text-transform: uppercase;
        color: #64748B;
        font-weight: 600;
        letter-spacing: 0.04em;
    }
    .metric-value {
        font-size: 1.45rem;
        font-weight: 700;
        color: #0F172A;
    }
    
    /* Document container */
    .doc-viewer-box {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 24px;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# SIDEBAR (CLEAN NATIVE BRANDING — NO BROKEN EXTERNAL SVG)
# ==============================================================================
st.sidebar.markdown("""
<div style="padding: 4px 0 16px 0; border-bottom: 1px solid #E2E8F0; margin-bottom: 16px;">
    <div style="font-size: 0.76rem; font-weight: 700; color: #0284C7; letter-spacing: 0.08em; text-transform: uppercase;">
        NASA Space Apps 2026
    </div>
    <div style="font-size: 1.35rem; font-weight: 800; color: #0F172A; margin-top: 2px; letter-spacing: -0.01em;">
        TERRAIN INTELLIGENCE
    </div>
    <div style="margin-top: 6px;">
        <span class="badge-prep">PRE-HACKATHON WORKSPACE</span>
    </div>
</div>
""", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "Navigation Menu",
    [
        "1. Overview & Vision",
        "2. Candidate Analog Explorer",
        "3. Dataset Catalogue (28 Products)",
        "4. Comparability Tiers & Failure Analysis",
        "5. Technical Document Viewer",
        "6. Verified Hackathon Schedule"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style="font-size: 0.78rem; color: #64748B; line-height: 1.4;">
    <b>Research Workspace Status:</b><br>
    Architecture planning, dataset auditing, and candidate profiles established.<br>
    <i>Hackathon starts Nov 14, 2026.</i>
</div>
""", unsafe_allow_html=True)

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

    # Clean light metric cards
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown('<div class="card-light"><div class="metric-title">Event Window</div><div class="metric-value">Nov 14–15, 2026</div><div class="source-tag">48-hour global hackathon</div></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="card-light"><div class="metric-title">Planetary Targets</div><div class="metric-value">Moon & Mars</div><div class="source-tag">Artemis South Pole & Jezero/Gale</div></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="card-light"><div class="metric-title">Investigated Sites</div><div class="metric-value">8 Candidates</div><div class="source-tag">Deserts, impacts, volcanics, permafrost</div></div>', unsafe_allow_html=True)
    with m4:
        st.markdown('<div class="card-light"><div class="metric-title">Catalogued Products</div><div class="metric-value">28 Datasets</div><div class="source-tag">13 Earth · 8 Moon · 7 Mars</div></div>', unsafe_allow_html=True)

    st.info(
        "**NASA Challenge:** *'Identify Earth Locations that Analog the Permanent Moon Base Locations and Mars.'*\n\n"
        "**Proposed Engineering Objective:** Build a reproducible geospatial framework to evaluate terrestrial sites for specific exploration objectives "
        "(e.g., rover trafficability vs. base habitat siting) using matched spatial baselines, stochastic decision analysis, and transparent failure boundaries."
    )

    st.markdown('<div class="section-title">Four Foundational Methodological Principles</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="card-light">
            <h4 style="color: #0F172A; margin-top:0;">1. Rejection of Single Scalar Scores</h4>
            <p style="color: #334155; font-size: 0.92rem;">
                No single composite score can represent planetary fidelity. A site matching slope may fail completely on rock composition. 
                We output a multi-dimensional vector across distinct comparability tiers with uncertainty intervals.
            </p>
            <h4 style="color: #0F172A; margin-top:14px;">2. Primacy of Failure Analysis</h4>
            <p style="color: #334155; font-size: 0.92rem;">
                What an analog <i>cannot</i> match (surface gravity, ambient vacuum, cosmic ray radiation, cryogenic PSR cold traps) 
                is treated as primary scientific data, preventing misleading overconfidence in terrestrial test results.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="card-light">
            <h4 style="color: #0F172A; margin-top:0;">3. Matched Spatial Baseline Requirement</h4>
            <p style="color: #334155; font-size: 0.92rem;">
                Slope and roughness are scale-dependent derivatives. Comparing 5 m lunar altimetry directly against 30 m Earth DEMs 
                creates artificial numerical divergence. All data must be resampled to a common ground sample distance (GSD).
            </p>
            <h4 style="color: #0F172A; margin-top:14px;">4. Spatially Aware Uncertainty Bounds</h4>
            <p style="color: #334155; font-size: 0.92rem;">
                Spatial autocorrelation invalidates standard pixel bootstrapping. We propose spatial block bootstrapping 
                calibrated by variogram range to produce statistically honest confidence intervals.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Proposed Data & Analysis Flow (Pre-Hackathon Design)</div>', unsafe_allow_html=True)
    st.code("""
    [Data Sources] Earth (Copernicus/SRTM) | Moon (LOLA/Diviner) | Mars (MOLA-HRSC/THEMIS)
           ↓
    [Data Acquisition] Manifest-guided API downloads (earthaccess, PDS Geosciences, STAC)
           ↓
    [Quality Assessment] Coverage verification, latitude bounds, void/cloud masking
           ↓
    [Geospatial Preprocessing] Coordinate harmonization (IAU Moon/Mars, WGS84) & matched GSD resampling
           ↓
    [Feature Extraction] Tier A (Direct Terrain), Tier B (Thermal), Tier C (Composition), Tier D (Invariants)
           ↓
    [Statistical Evaluation] Wasserstein-1 / Mahalanobis distances + SMAA Stochastic Acceptability
           ↓
    [Uncertainty Quantification] Spatial block bootstrap (variogram calibrated) + Monte Carlo error
           ↓
    [Visualization & Reporting] Clean dual-body maps + Invariant Analog Failure Matrix Cards
    """, language="text")

# ==============================================================================
# 2. CANDIDATE ANALOG EXPLORER (LIGHT THEME MAP + INSET VIEWER)
# ==============================================================================
elif menu == "2. Candidate Analog Explorer":
    st.markdown('<div class="main-header">Earth Analog Candidates Explorer</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Geographic distribution and peer-reviewed scientific characterization of candidate sites</div>', unsafe_allow_html=True)

    # Master candidate dataset (Coordinates remain authentic & unmodified)
    candidates = [
        {
            "Site": "Atacama Desert (Chile)",
            "ShortName": "Atacama Desert",
            "Country": "Chile",
            "Region": "South America",
            "Lat": -24.50, "Lon": -69.20,
            "Environment": "Hyperarid desert, salars, extreme UV exposure, volcanic substrate",
            "Analog Target": "Martian hyperarid soil, microbial habitability limits, rover traverse",
            "Evidence Level": "Published Literature",
            "Key Citation": "Navarro-González et al. (2003). Science 302, 1018.",
            "Terrain Fidelity": "High for regolith aridity & low organic content; volcanic rocky substrate.",
            "Invariant Mismatches": "Atmospheric pressure ~50–60 kPa at elevation (vs Mars ~0.6 kPa); Earth gravity (9.81 vs 3.71 m/s²); episodic coastal fog events.",
            "Data Coverage": "Excellent (SRTM GL1, Copernicus GLO-30, Landsat, Sentinel-2, EMIT)."
        },
        {
            "Site": "Devon Island / Haughton (Canada)",
            "ShortName": "Devon Island",
            "Country": "Canada",
            "Region": "Arctic",
            "Lat": 75.40, "Lon": -89.80,
            "Environment": "Polar desert, ~23 km impact crater in sedimentary target, periglacial terrain",
            "Analog Target": "Mars impact cratering, periglacial landforms, crewed field operations",
            "Evidence Level": "Published Literature",
            "Key Citation": "Lee & Osinski (2005). Meteoritics & Planetary Science 40, 1759.",
            "Terrain Fidelity": "Moderate-high for degraded impact crater morphology and Arctic desert field trials.",
            "Invariant Mismatches": "Hydrological active season with liquid water run-off; lichen/microbial cover; temperature buffered compared to Mars.",
            "Data Coverage": "SRTM does NOT cover this latitude (>60°N). Must use Copernicus GLO-30 or ArcticDEM (~2m)."
        },
        {
            "Site": "Askja / Holuhraun (Iceland)",
            "ShortName": "Askja / Holuhraun",
            "Country": "Iceland",
            "Region": "North Atlantic",
            "Lat": 65.00, "Lon": -16.70,
            "Environment": "Basaltic lava fields, tuyas (subglacial volcanoes), hydrothermal alteration",
            "Analog Target": "Lunar mare volcanism, basaltic rover mobility, Apollo astronaut training heritage",
            "Evidence Level": "Published Literature",
            "Key Citation": "Historical Apollo field training; Mangold et al. (2011) Mars basalt weathering analogs.",
            "Terrain Fidelity": "High for basaltic flow morphology, vesicular textures, and palagonitization.",
            "Invariant Mismatches": "Wet maritime climate, dynamic glacial melt, persistent atmospheric humidity and precipitation.",
            "Data Coverage": "Near SRTM cutoff limit. Requires Copernicus GLO-30, ArcticDEM, or Sentinel-2."
        },
        {
            "Site": "Death Valley (USA)",
            "ShortName": "Death Valley",
            "Country": "United States",
            "Region": "North America",
            "Lat": 36.50, "Lon": -117.00,
            "Environment": "Hyperarid hot basin, alluvial fans, salt playas, active dune fields",
            "Analog Target": "Martian fan and playa geomorphology, rover mobility, extreme thermal swing",
            "Evidence Level": "Published Literature",
            "Key Citation": "Widely documented in planetary rover test campaigns and alluvial sedimentology.",
            "Terrain Fidelity": "High for gravelly alluvial slopes, evaporite salt crusts, and aeolian ripples.",
            "Invariant Mismatches": "High summer temperatures (>45°C) contrast with Martian cryogenic cold; thick oxidizing atmosphere.",
            "Data Coverage": "Complete (30m SRTM GL1, 30m ASTER GDEM, Landsat 8/9, Sentinel-2, USGS 3DEP)."
        },
        {
            "Site": "McMurdo Dry Valleys (Antarctica)",
            "ShortName": "McMurdo Dry Valleys",
            "Country": "Antarctica",
            "Region": "Antarctica",
            "Lat": -77.50, "Lon": 162.00,
            "Environment": "Cold hyperarid polar desert, permafrost, sandstone ventifacts, ice-covered lakes",
            "Analog Target": "Martian cold-desert permafrost, subsurface ice dynamics, cryptoendolithic biology",
            "Evidence Level": "Published Literature",
            "Key Citation": "Marchant & Head (2007). Icarus 192, 187; McKay (2004).",
            "Terrain Fidelity": "Very high for sublimation permafrost and dry permafrost polygons.",
            "Invariant Mismatches": "Zero SRTM coverage; thick atmosphere; ice sheet proximity; extreme logistical isolation.",
            "Data Coverage": "Must use REMA (Reference Elevation Model of Antarctica, 2–8m) and Landsat seasonal mosaics."
        },
        {
            "Site": "Lonar Crater (Maharashtra, India)",
            "ShortName": "Lonar Crater",
            "Country": "India",
            "Region": "South Asia",
            "Lat": 19.98, "Lon": 76.51,
            "Environment": "~1.8 km simple impact crater excavated entirely in Deccan flood basalt; alkaline saline lake",
            "Analog Target": "Impact cratering in basaltic targets (analog to Lunar Mare impacts and Martian basaltic crust)",
            "Evidence Level": "Published Literature",
            "Key Citation": "Hagerty & Newsom (2003). Meteoritics & Planetary Science 38, 1065.",
            "Terrain Fidelity": "High for basaltic impact breccia, shock metamorphism, and impact hydrothermal alteration.",
            "Invariant Mismatches": "Monsoon climate (~800mm annual rain), heavy seasonal vegetation, human settlement and agricultural buffer.",
            "Data Coverage": "Good (30m SRTM, Copernicus GLO-30, Landsat, Sentinel-2, GSI Bhukosh maps)."
        },
        {
            "Site": "Ladakh High Desert (India)",
            "ShortName": "Ladakh High Desert",
            "Country": "India",
            "Region": "South Asia",
            "Lat": 34.20, "Lon": 77.60,
            "Environment": "High-altitude cold arid desert (3,000–5,500m ASL), periglacial stone circles, ophiolites",
            "Analog Target": "Cold desert terrain trafficability, high UV radiation exposure, periglacial landforms",
            "Evidence Level": "Exploratory Research Hypothesis",
            "Key Citation": "Preliminary Indian space analog station concept proposals; astrobiological reconnaissance.",
            "Terrain Fidelity": "Moderate for cold arid periglacial slope processes; mineralogic Moon/Mars similarity unproven.",
            "Invariant Mismatches": "Atmospheric pressure at 4,500m is ~57 kPa (over 90× Mars surface pressure); glacial melt streams.",
            "Data Coverage": "Good (30m SRTM, Copernicus GLO-30, Landsat, Sentinel-2, ISRO Bhuvan)."
        },
        {
            "Site": "Rann of Kutch (Gujarat, India)",
            "ShortName": "Rann of Kutch",
            "Country": "India",
            "Region": "South Asia",
            "Lat": 23.80, "Lon": 70.00,
            "Environment": "Extensive seasonal salt mudflat, halite/gypsum crust, low relief playa",
            "Analog Target": "Martian playa trafficability and evaporite sediment crust testing (Hypothesis)",
            "Evidence Level": "Speculative / High-Risk Hypothesis",
            "Key Citation": "No established peer-reviewed planetary analog literature identified.",
            "Terrain Fidelity": "Weak for lunar polar terrain (flat plain vs rugged 25° crater rims); unverified for Mars sulfates.",
            "Invariant Mismatches": "Annual monsoon inundation transforms the site into a shallow sea; marine evaporite chemistry differs from Mars acidic sulfates.",
            "Data Coverage": "Good (SRTM, Copernicus GLO-30, Sentinel-2). Must account for seasonal flooding."
        }
    ]
    df_sites = pd.DataFrame(candidates)

    # Candidate selection dropdown at the top
    selected_site = st.selectbox(
        "Select Candidate Site to Inspect & Highlight on Map",
        df_sites["Site"],
        index=0
    )

    # Map presentation controls (clean light radio buttons)
    col_ctrl1, col_ctrl2 = st.columns([1, 1])
    with col_ctrl1:
        map_view_scope = st.radio(
            "Geographic Presentation View",
            ["Global World Overview", "Regional Inset: Indian Subcontinent Focus (Uncluttered)"],
            horizontal=True
        )
    with col_ctrl2:
        st.markdown("""
        <div style="font-size: 0.82rem; color: #64748B; padding-top: 6px;">
            <b>Evidence Classification Key:</b><br>
            <span style="color:#0284C7;">●</span> Published Literature &nbsp;|&nbsp; 
            <span style="color:#D97706;">●</span> Exploratory Research Hypothesis &nbsp;|&nbsp; 
            <span style="color:#DC2626;">●</span> Speculative / High-Risk Hypothesis
        </div>
        """, unsafe_allow_html=True)

    # Color mapping for evidence levels
    color_map = {
        "Published Literature": "#0284C7",             # Scientific blue
        "Exploratory Research Hypothesis": "#D97706",    # Amber
        "Speculative / High-Risk Hypothesis": "#DC2626"  # Restrained red
    }

    # Build the light scientific Plotly map
    fig = go.Figure()

    # Separate traces by evidence level to produce an accessible, crisp legend
    for ev_level in ["Published Literature", "Exploratory Research Hypothesis", "Speculative / High-Risk Hypothesis"]:
        sub_df = df_sites[df_sites["Evidence Level"] == ev_level]
        
        # Calculate marker styling: highlight selected candidate with larger size & dark border
        marker_sizes = []
        marker_line_widths = []
        marker_line_colors = []
        
        for _, row in sub_df.iterrows():
            if row["Site"] == selected_site:
                marker_sizes.append(18)           # Prominent highlight
                marker_line_widths.append(3)      # Bold outline
                marker_line_colors.append("#0F172A")
            else:
                marker_sizes.append(11)
                marker_line_widths.append(1.5)
                marker_line_colors.append("#FFFFFF")
        
        hover_texts = [
            f"<b>{r['ShortName']}</b> ({r['Country']})<br>"
            f"Evidence Level: {r['Evidence Level']}<br>"
            f"Environment: {r['Environment'][:45]}...<br>"
            f"Target: {r['Analog Target'][:40]}...<br>"
            f"Coordinates: {r['Lat']}°, {r['Lon']}°"
            for _, r in sub_df.iterrows()
        ]

        fig.add_trace(go.Scattergeo(
            lat=sub_df["Lat"],
            lon=sub_df["Lon"],
            mode="markers+text" if map_view_scope != "Global World Overview" else "markers",
            text=sub_df["ShortName"] if map_view_scope != "Global World Overview" else None,
            textposition="top center",
            textfont=dict(family="sans-serif", size=11, color="#0F172A"),
            marker=dict(
                size=marker_sizes,
                color=color_map[ev_level],
                opacity=0.92,
                line=dict(width=marker_line_widths, color=marker_line_colors)
            ),
            name=ev_level,
            hoverinfo="text",
            hovertext=hover_texts
        ))

    # Configure clean, light scientific geography
    if map_view_scope == "Global World Overview":
        geo_scope = dict(
            projection_type="natural earth",
            showland=True,
            landcolor="#F8FAFC",        # Very light grey-white land
            showocean=True,
            oceancolor="#EBF4FA",       # Clean light sky-blue water
            showcountries=True,
            countrycolor="#CBD5E1",     # Soft slate borders
            countrywidth=0.8,
            showcoastlines=True,
            coastlinecolor="#94A3B8",   # Subtle coastline definition
            coastlinewidth=0.9,
            bgcolor="#FFFFFF"
        )
        map_title = "Global Candidate Analog Locations (Selected Candidate Highlighted)"
    else:
        # Regional inset for Indian Subcontinent: reveals true 1600+ km separation of sites without overlap
        geo_scope = dict(
            projection_type="mercator",
            center=dict(lat=27.0, lon=75.0),
            lataxis=dict(range=[12, 38]),
            lonaxis=dict(range=[64, 88]),
            showland=True,
            landcolor="#F8FAFC",
            showocean=True,
            oceancolor="#EBF4FA",
            showcountries=True,
            countrycolor="#94A3B8",
            countrywidth=1.2,
            showsubunits=True,
            subunitcolor="#CBD5E1",
            showcoastlines=True,
            coastlinecolor="#64748B",
            bgcolor="#FFFFFF"
        )
        map_title = "Regional Inset Map: Indian Subcontinent Focus (Lonar, Ladakh, and Rann of Kutch)"

    fig.update_layout(
        title=dict(text=map_title, font=dict(family="sans-serif", size=14, color="#0F172A")),
        geo=geo_scope,
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        margin=dict(r=0, t=35, l=0, b=0),
        height=450,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0,
            font=dict(family="sans-serif", size=11, color="#334155"),
            bgcolor="rgba(255,255,255,0.9)",
            bordercolor="#E2E8F0",
            borderwidth=1
        )
    )

    st.plotly_chart(fig, use_container_width=True)

    # --------------------------------------------------------------------------
    # IMPROVED CANDIDATE INFORMATION CARD
    # --------------------------------------------------------------------------
    site = df_sites[df_sites["Site"] == selected_site].iloc[0]

    st.markdown("---")
    st.markdown('<div class="section-title">Selected Candidate Scientific Dossier</div>', unsafe_allow_html=True)

    # Badge formatting
    if site["Evidence Level"] == "Published Literature":
        badge_html = f'<span class="badge-published">{site["Evidence Level"]}</span>'
    elif site["Evidence Level"] == "Exploratory Research Hypothesis":
        badge_html = f'<span class="badge-exploratory">{site["Evidence Level"]}</span>'
    else:
        badge_html = f'<span class="badge-speculative">{site["Evidence Level"]}</span>'

    st.markdown(f"""
    <div class="card-light">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap;">
            <div>
                <h3 style="color: #0F172A; margin: 0 0 4px 0; font-size: 1.4rem;">{site['Site']}</h3>
                <div style="color: #64748B; font-size: 0.9rem;">
                    Coordinates: <b>{site['Lat']}°N, {site['Lon']}°E</b> &nbsp;·&nbsp; Country: <b>{site['Country']}</b>
                </div>
            </div>
            <div style="margin-top: 4px;">
                {badge_html}
            </div>
        </div>
        <hr style="border: 0; border-top: 1px solid #E2E8F0; margin: 12px 0;">
        <div style="font-size: 0.92rem; color: #334155; line-height: 1.5;">
            <b>Geological Setting:</b> {site['Environment']}<br>
            <b>Analog Mission Target:</b> {site['Analog Target']}<br>
            <b>Peer-Reviewed Literature Reference:</b> <i>{site['Key Citation']}</i>
        </div>
    </div>
    """, unsafe_allow_html=True)

    info_col1, info_col2 = st.columns(2)
    with info_col1:
        st.markdown(f"""
        <div class="card-tier-a">
            <h4 style="color: #0369A1; margin: 0 0 8px 0; font-size: 1.05rem;">
                ✓ Documented Analog Fidelity (Strengths)
            </h4>
            <p style="color: #334155; font-size: 0.92rem; line-height: 1.5; margin-bottom: 8px;">
                {site['Terrain Fidelity']}
            </p>
            <div class="source-tag"><b>Data Availability:</b> {site['Data Coverage']}</div>
        </div>
        """, unsafe_allow_html=True)

    with info_col2:
        st.markdown(f"""
        <div class="card-tier-d">
            <h4 style="color: #DC2626; margin: 0 0 8px 0; font-size: 1.05rem;">
                ⚠ Invariant Physical Mismatches (Limitations)
            </h4>
            <p style="color: #334155; font-size: 0.92rem; line-height: 1.5; margin-bottom: 8px;">
                {site['Invariant Mismatches']}
            </p>
            <div class="source-tag"><b>Scientific Rule:</b> Tier D physical mismatches cannot be analoged outdoors on Earth surface.</div>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# 3. DATASET CATALOGUE (28 PRODUCTS)
# ==============================================================================
elif menu == "3. Dataset Catalogue (28 Products)":
    st.markdown('<div class="main-header">NASA & Partner Agency Dataset Catalogue</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Structured inventory of 28 verified open datasets across Earth, Moon, and Mars</div>', unsafe_allow_html=True)

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

    fc1, fc2 = st.columns([1, 2])
    with fc1:
        b_filter = st.multiselect("Filter by Target Body", ["Earth", "Moon", "Mars"], default=["Earth", "Moon", "Mars"])
    with fc2:
        search_query = st.text_input("Search Dataset or Variable", placeholder="e.g. LOLA, Thermal, Elevation, Copernicus...")

    filtered_cat = df_cat[df_cat["Body"].isin(b_filter)]
    if search_query:
        mask = (
            filtered_cat["Dataset"].str.contains(search_query, case=False) |
            filtered_cat["Variable"].str.contains(search_query, case=False) |
            filtered_cat["Agency"].str.contains(search_query, case=False)
        )
        filtered_cat = filtered_cat[mask]

    st.markdown(f"**Displaying {len(filtered_cat)} of {len(all_datasets)} verified open datasets:**")

    st.dataframe(
        filtered_cat[["ID", "Body", "Dataset", "Agency", "Variable", "Resolution", "Format", "Limitation", "URL"]],
        column_config={
            "URL": st.column_config.LinkColumn("Official Repository Link")
        },
        use_container_width=True,
        hide_index=True
    )

# ==============================================================================
# 4. COMPARABILITY TIERS & FAILURE ANALYSIS (LIGHT THEME CARDS)
# ==============================================================================
elif menu == "4. Comparability Tiers & Failure Analysis":
    st.markdown('<div class="main-header">Comparability Tiers & Failure Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Methodological segregation of comparable physical quantities from invariant physical mismatches</div>', unsafe_allow_html=True)

    st.warning(
        "**Integrity Clarification:** No similarity calculations, numerical distances, or scoring algorithms have been executed. "
        "The analytical cards below present the scientific schema and invariant physical constraints established from peer-reviewed literature."
    )

    st.markdown("""
    | Tier | Scientific Definition | Example Physical Properties | Treatment in Terrain Intelligence |
    | :--- | :--- | :--- | :--- |
    | **Tier A** | Direct physical equivalence measured by comparable sensor physics | Elevation, Slope distribution, Multi-scale RMS roughness | **Enters distance calculation** (Wasserstein-1 / Mahalanobis with shrinkage) |
    | **Tier B** | Same physical quantity, altered by planetary boundary conditions | Skin surface temperature, Diurnal temperature amplitude | **Enters distance with inflated variance penalty** and explicit caveats |
    | **Tier C** | Proxy relationship or indirect spectral index | Spectral band ratios, Derived thermal inertia from models | **Evaluated as separate qualitative dimension**; never blended directly with terrain |
    | **Tier D** | Fundamental, invariant planetary physics that Earth CANNOT reproduce | Surface gravity, Atmospheric vacuum, Cosmic radiation, PSR cold traps | **STRICTLY EXCLUDED from numerical distance.** Reported as Invariant Failure Flags |
    """)

    st.markdown("---")
    st.markdown('<div class="section-title">Candidate Analog Failure Analysis Schema</div>', unsafe_allow_html=True)

    sel_candidate = st.selectbox(
        "Select Candidate Site to Review Analytical Schema vs Invariant Constraints",
        ["Lonar Crater (India)", "Atacama Desert (Chile)", "Devon Island / Haughton (Canada)"]
    )

    colA, colB = st.columns(2)
    with colA:
        st.markdown("""
        <div class="card-tier-a">
            <h4 style="color: #0369A1; margin: 0 0 10px 0; font-size: 1.1rem;">
                📐 Planned Tier A & B Analytical Properties
            </h4>
            <div style="font-size: 0.88rem; color: #475569; margin-bottom: 8px;">
                <b>Target Baseline:</b> Lunar South Pole (LOLA Altimetry harmonized to 30 m GSD)
            </div>
            <ul style="color: #1E293B; font-size: 0.92rem; line-height: 1.6; padding-left: 20px;">
                <li><b>Slope Distribution (Tier A):</b> Planned Wasserstein-1 metric on matched-baseline elevation models.<br>
                <span class="source-tag">Status: <i>Pending pipeline execution during hackathon (No value calculated yet).</i></span></li>
                <li><b>Surface Roughness (Tier A):</b> Planned root-mean-square (RMS) height deviation at decameter baselines.<br>
                <span class="source-tag">Status: <i>Pending pipeline execution during hackathon.</i></span></li>
                <li><b>Thermal Amplitude (Tier B):</b> Diurnal skin temperature comparison.<br>
                <span class="source-tag">Status: <i>Requires MODIS/ECOSTRESS vs Diviner matching.</i></span></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with colB:
        st.markdown("""
        <div class="card-tier-d">
            <h4 style="color: #991B1B; margin: 0 0 10px 0; font-size: 1.1rem;">
                ❌ Invariant Physical Mismatches (Tier D Failures)
            </h4>
            <div style="font-size: 0.88rem; color: #7F1D1D; margin-bottom: 8px;">
                <b>Physical Impossibilities on Earth Surface (Literature Grounded)</b>
            </div>
            <ul style="color: #1E293B; font-size: 0.92rem; line-height: 1.6; padding-left: 20px;">
                <li><b>Surface Gravity:</b> 1.62 m/s² (Moon) / 3.71 m/s² (Mars) vs 9.81 m/s² (Earth).<br>
                <span class="source-tag">Governs rover wheel slip, traction, and regolith bearing strength.</span></li>
                <li><b>Ambient Atmosphere:</b> Hard vacuum (&lt;10⁻¹⁰ Pa, Moon) / ~600 Pa (Mars) vs 101.3 kPa (Earth).<br>
                <span class="source-tag">Prevents outdoor reproduction of vacuum dust adhesion or low-pressure aeolian dynamics.</span></li>
                <li><b>Cosmic Radiation:</b> Unshielded GCR & Solar Energetic Particles vs Earth magnetosphere.<br>
                <span class="source-tag">Biological and material degradation cannot be replicated outdoors.</span></li>
                <li><b>PSR Cryogenic Cold:</b> Lunar south-polar cold traps sustain temperatures &lt;40 K (Diviner observations).<br>
                <span class="source-tag">Earth's coldest surface (~184 K at Vostok) is &gt;140 K warmer. Zero terrestrial thermal analog.</span></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.info(
        "**Scientific Principle:** Analog failure analysis is our key differentiator. Instead of outputting an unscientific '88% match', "
        "Terrain Intelligence explicitly details what can be tested in the field (slope traverse, basaltic impact shock) and what must be simulated in vacuum chambers."
    )

# ==============================================================================
# 5. TECHNICAL DOCUMENT VIEWER
# ==============================================================================
elif menu == "5. Technical Document Viewer":
    st.markdown('<div class="main-header">Technical Workspace Document Viewer</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Review pre-hackathon documentation, research notes, and engineering specifications</div>', unsafe_allow_html=True)

    docs = {
        "Project Vision & Scope": "PROJECT_VISION.md",
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
            content = f.read()
        st.markdown('<div class="doc-viewer-box">', unsafe_allow_html=True)
        st.markdown(content)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error(f"Documentation file not found: {docs[selected_doc]}")

# ==============================================================================
# 6. VERIFIED HACKATHON SCHEDULE
# ==============================================================================
elif menu == "6. Verified Hackathon Schedule":
    st.markdown('<div class="main-header">Verified Event Schedule & Execution Plan</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">NASA Space Apps Challenge 2026: Official Weekend November 14–15, 2026</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card-light">
        <h4 style="color: #0F172A; margin: 0 0 6px 0;">Official 48-Hour Global Hackathon Window</h4>
        <div style="font-size: 0.95rem; color: #334155; line-height: 1.5;">
            • <b>Start:</b> Saturday, November 14, 2026 (09:00 local time)<br>
            • <b>Finish:</b> Sunday, November 15, 2026 (23:59 local submission deadline)<br>
            • <b>Current Status:</b> Pre-hackathon preparation, literature cataloguing, environment verification.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">48-Hour Execution Milestone Breakdown</div>', unsafe_allow_html=True)
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
