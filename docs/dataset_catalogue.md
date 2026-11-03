# Dataset Catalogue

**Structured Inventory of Open Datasets for COSMONOVA**  
*Planetary Analog Intelligence Platform*

> [!IMPORTANT]
> Resolutions, formats, and URLs are from published documentation and prior knowledge. **Every URL, resolution, and license must be verified by a human before use.** Items marked [verify] are less certain.

---

## Earth Datasets

| # | Dataset | Agency | URL | Variables | Spatial Resolution | Format | Access | Possible Use | Limitations |
|---|---------|--------|-----|-----------|-------------------|--------|--------|-------------|-------------|
| E1 | ASTER GDEM v3 | NASA/METI (LP DAAC) | https://lpdaac.usgs.gov/products/astgtmv003/ | Elevation | ~30 m; ~83°N–83°S | GeoTIFF | Earthdata login; earthaccess | Global DEM incl. high latitude | Artifacts, noise, stacking errors |
| E2 | SRTM GL1 v003 | NASA/NGA (LP DAAC) | https://lpdaac.usgs.gov/products/srtmgl1v003/ | Elevation | ~30 m; 60°N–56°S only | HGT/GeoTIFF | Download | Clean for mid-latitude sites (Ladakh, Lonar, Kutch, Atacama, Death Valley) | **Does not cover Devon Island, most of Iceland, or Antarctica.** Voids; radar layover |
| E3 | Copernicus DEM GLO-30 | ESA/Copernicus | https://registry.opendata.aws/copernicus-dem/ and https://dataspace.copernicus.eu/ | Surface elevation | 30 m; global | COG GeoTIFF | AWS open data; STAC | Best global gap-filler for SRTM gaps | Surface model (includes canopy/buildings). Check license |
| E4 | ArcticDEM | PGC (NSF/NGA-funded) | https://www.pgc.umn.edu/data/arcticdem/ | High-res elevation (Arctic) | ~2 m mosaics | GeoTIFF | Download; STAC | Excellent for Devon Island and Iceland | Large files. Not NASA; verify terms [verify] |
| E5 | REMA | PGC (NSF/NGA-funded) | https://www.pgc.umn.edu/data/rema/ | High-res elevation (Antarctica) | ~2–8 m mosaics | GeoTIFF | Download; STAC | Antarctica (Dry Valleys) | Large files. Verify terms [verify] |
| E6 | Landsat 8/9 | USGS/NASA | https://www.usgs.gov/landsat-missions | Multispectral, thermal | 30 m optical; 100 m thermal (TIRS); 16-day revisit | COG/GeoTIFF | EarthExplorer; STAC; cloud | Multi-decade record; mineral band ratios (crude); thermal snapshot | Mineral band ratios are proxies only; thermal is a single time snapshot |
| E7 | Sentinel-2 | ESA | https://dataspace.copernicus.eu/ | 13-band multispectral | 10/20/60 m; ~5-day revisit | SAFE/COG | Copernicus Data Space; STAC | SWIR bands for coarse iron-oxide/clay proxies | Cloud/vegetation masking needed |
| E8 | MODIS (Terra/Aqua) | NASA | https://modis.gsfc.nasa.gov/ | LST, albedo, vegetation | 250 m–1 km; daily | HDF/GeoTIFF | Earthdata; earthaccess | Climatology baseline | Coarse; satellite aging [verify continuity] |
| E9 | ECOSTRESS | NASA JPL (ISS) | https://ecostress.jpl.nasa.gov/ | LST, emissivity | ~70 m; irregular ISS sampling | HDF5/GeoTIFF | LP DAAC | Diurnal thermal sampling | Irregular observation times [verify] |
| E10 | EMIT | NASA JPL (ISS) | https://earth.jpl.nasa.gov/emit | Imaging spectroscopy (~380–2500 nm) | ~60 m; arid regions prioritized | NetCDF | LP DAAC | Closest Earth analog to CRISM/M³-style spectra | Patchy coverage [verify] |
| E11 | NASA POWER | NASA LaRC | https://power.larc.nasa.gov/ | Modeled meteorology, solar radiation | ~0.5°; 1981+ | JSON/CSV/NetCDF | REST API | Site-level climate context | Too coarse for terrain; modeled, not measured |
| E12 | GSI Bhukosh | GSI (India) | https://bhukosh.gsi.gov.in/ | Lithology, structure, geological maps | Map scales vary | Shapefile/WMS | Registration required | Indian site geology | Access limits; may need registration [verify] |
| E13 | ISRO Bhuvan | ISRO (India) | https://bhuvan.nrsc.gov.in/ | Various Indian geospatial layers | Varies | WMS/download | Registration | Indian-specific terrain and thematic layers | Access terms vary [verify] |

---

## Moon Datasets

| # | Dataset | Agency/Instrument | URL | Variables | Resolution | Format | Access | Possible Use | Limitations |
|---|---------|-------------------|-----|-----------|------------|--------|--------|-------------|-------------|
| M1 | LOLA | NASA LRO | https://pds-geosciences.wustl.edu/missions/lro/lola.htm | Elevation, slope, roughness | Global gridded ~tens of m; polar products ~5–20 m [verify] | PDS IMG/LBL; GeoTIFF | PDS; Trek tiles | Core terrain target for slope/roughness | Interpolation between orbital tracks at high resolution |
| M2 | LROC NAC | NASA LRO (ASU) | https://lroc.asu.edu/ | High-res imagery | ~0.5–2 m/px | PDS IMG; web tiles | PDS; QuickMap; WMS | Boulders, craters, illumination context | Coverage not uniform |
| M3 | LROC WAC | NASA LRO (ASU) | https://lroc.asu.edu/ | Wide-angle imagery | ~100 m/px | PDS IMG; web tiles | PDS; QuickMap | Regional context | Lower resolution |
| M4 | Diviner | NASA LRO (UCLA) | https://diviner.ucla.edu/ | Surface brightness temperature, rock abundance | Footprint ~hundreds of m; gridded maps coarser | PDS tables; gridded | PDS Geosciences | Direct thermal target | PSR temperatures model-dependent |
| M5 | Lunar Geologic Map | USGS | https://astrogeology.usgs.gov/ | Unified 1:5M geologic map | Global, coarse | GIS layers | USGS Astrogeology | Geological context | Too coarse for site-level lithology |
| M6 | Moon Trek | NASA JPL | https://trek.nasa.gov/ | Web access to multiple layers | n/a | WMTS/WMS [verify] | Web portal | Fastest raster access without PDS processing | Portal interface; verify tile API |
| M7 | QuickMap | ASU | https://quickmap.lroc.asu.edu/ | Interactive lunar imagery and data layers | Multiple | Web/WMS | Web portal | Visual exploration and data identification | Portal interface |
| M8 | Chandrayaan-2/3 | ISRO | https://pradan.issdc.gov.in/ | High-res imaging, spectroscopy, radar | e.g., OHRC sub-metre [verify] | ISSDC portal | Registration required | Potential Indian-mission data linkage | Check access and format terms |

---

## Mars Datasets

| # | Dataset | Agency/Instrument | URL | Variables | Resolution | Format | Access | Possible Use | Limitations |
|---|---------|-------------------|-----|-----------|------------|--------|--------|-------------|-------------|
| R1 | MOLA | NASA MGS | PDS Geosciences Node | Global elevation | ~460 m/px | PDS; GeoTIFF | PDS | Coarse global terrain | Resolution mismatch vs Earth 30 m DEMs |
| R2 | MOLA–HRSC blended DEM | USGS Astrogeology (Fergason et al. 2018) | https://astrogeology.usgs.gov/ | Elevation | ~200 m/px | GeoTIFF | USGS Astrogeology | Good global terrain baseline | Verify current version [verify] |
| R3 | CTX | NASA MRO | PDS Imaging Node; astrogeology.usgs.gov | Imagery; site DTMs | ~6 m/px | PDS; mosaics | PDS | Wide context imagery; DTMs for selected sites | DTMs not globally available |
| R4 | HiRISE | NASA MRO (UArizona) | https://www.uahirise.org/ | High-res imagery; DTMs | ~25–50 cm/px | JP2; PDS | PDS | Rock/boulder detail (selected sites only) | Very limited spatial coverage |
| R5 | THEMIS | NASA Odyssey (ASU) | https://themis.asu.edu/ | Thermal IR, thermal inertia | ~100 m/px | PDS; mosaics | PDS | Thermal inertia proxy comparison | Interpretation model-dependent (Fergason et al. 2006 [verify]) |
| R6 | CRISM | NASA MRO (JHU/APL) | https://crism.jhuapl.edu/ | VIS/NIR spectroscopy | ~18 m targeted; ~200 m survey | PDS; complex | PDS Geosciences | Mineralogy identification | Heavy processing; sparse targeted coverage |
| R7 | Mars Trek | NASA JPL | https://trek.nasa.gov/ | Web access to multiple Mars layers | n/a | WMTS [verify] | Web portal | Fast prototyping access | Portal interface |

---

## Dataset Feasibility Matrix

Hackathon-oriented assessment: H = High, M = Medium, L = Low.

| Dataset | Ease of Access | Prep Burden | Value to MVP | Hackathon Risk |
|---------|---------------|-------------|-------------|----------------|
| Copernicus GLO-30 / ASTER / SRTM | H | L | H | L |
| LOLA (via Trek/QuickMap or PDS) | M | M | H | M (format handling) |
| Diviner gridded products | M | M | H | M |
| Mars MOLA/HRSC blend | H | L | M | L |
| THEMIS thermal inertia | M | M | M | M |
| Landsat/Sentinel-2 | H | M | M | L |
| EMIT vs CRISM/M³ spectra | M | H | M | H |
| HiRISE/LROC NAC (boulder counts) | M | H | M | H |
| NASA POWER | H | L | L–M | L |
| GSI/Bhuvan India layers | L–M | H | M (if Indian focus) | H |
| ArcticDEM/REMA | M | M | H (for Devon/Antarctica) | M |

---

## Licensing Summary

- **NASA, USGS, PDS data**: Generally open for reuse with attribution
- **Copernicus (Sentinel, DEM)**: Free and open with attribution under Copernicus licence
- **ISRO/GSI portals**: May have registration and specific terms — **read license page of each product**

> [!WARNING]
> License terms have not been verified as of this document's creation. Read the license page of each product before use and cite it in the submission.

---

## Data Access Tools

| Tool | Purpose | URL |
|------|---------|-----|
| earthaccess (Python) | NASA Earthdata search and download | https://github.com/nsidc/earthaccess |
| STAC clients | Spatiotemporal Asset Catalog for cloud-hosted data | Various (pystac, stackstac) |
| rasterio / rioxarray | Raster data reading and CRS management | PyPI |
| Moon Trek / Mars Trek | Browser-based layer exploration | https://trek.nasa.gov/ |
| QuickMap | Lunar data visualization | https://quickmap.lroc.asu.edu/ |

---

*Document status: Pre-hackathon catalogue. Every URL, resolution, and license must be verified before use in the competition.*
