# NASA Dataset Exploration

This directory contains notes from exploring and testing NASA and agency datasets.

## Expected Contents

- `earthdata_access_test.md` — Notes from testing NASA Earthdata login and earthaccess
- `copernicus_access_test.md` — Notes from testing Copernicus Data Space access
- `lola_format_notes.md` — Notes on LOLA PDS data format and reading with Python
- `geotiff_test.md` — Notes from reading a test GeoTIFF with rasterio
- `data_manifest.md` — Master list of datasets with verified URLs, checksums, and license terms

## Pre-Hackathon Tasks

- [ ] Create NASA Earthdata account
- [ ] Create Copernicus Data Space account
- [ ] Test downloading one Copernicus GLO-30 tile
- [ ] Test downloading one LOLA product from PDS
- [ ] Test reading a GeoTIFF with rasterio
- [ ] Test reading a PDS IMG file (if applicable)
- [ ] Verify GSI Bhukosh access for Indian geological maps
- [ ] Verify ISRO Bhuvan access

## Data Manifest Template

For each dataset, verify and record:

```
Dataset: [name]
URL: [verified URL]
Access method: [download / API / STAC]
Format: [GeoTIFF / HDF5 / PDS IMG / etc.]
CRS: [EPSG code or IAU definition]
File size (approx): [per tile / total]
License: [terms summary with link]
Last verified: [date]
Status: [✅ accessible / ⚠️ requires registration / ❌ inaccessible]
```

