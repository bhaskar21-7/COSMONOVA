# Development Environment Setup Guide

**Terrain Intelligence — NASA Space Apps Challenge 2026**

> [!NOTE]
> This guide is based on the actual system environment inspected on November 3, 2026. Commands are for Windows (PowerShell). Adapt for macOS/Linux as needed.

---

## Current System Environment

| Component | Detected Version | Status |
|-----------|-----------------|--------|
| **OS** | Windows 11 (NT 10.0.26300.0), x64 | ✅ Compatible |
| **Python** | 3.13.3 (MSC v.1943, 64-bit AMD64) | ⚠️ See note below |
| **pip** | 26.1.2 | ✅ Current |
| **Git** | 2.51.2.windows.1 | ✅ Current |
| **JupyterLab** | 4.5.6 | ✅ Installed |
| **VS Code** | 1.144.0 (Antigravity IDE variant) | ✅ Installed |

### Python Version Note

Python 3.13.3 is installed. While this is the latest stable Python, some geospatial libraries (particularly GDAL/rasterio binaries for Windows) may have **delayed support for Python 3.13**. Two options:

1. **Try with Python 3.13 first** — install dependencies and test. If rasterio/GDAL fail to install, use option 2.
2. **Install Python 3.11 or 3.12 as a secondary interpreter** — these have the broadest geospatial library support. Use `py -3.11 -m venv .venv` to create the environment.

**Recommendation**: Test with Python 3.13 first. Fall back to 3.11/3.12 only if binary wheels are unavailable.

---

## Already Installed (Global Python)

The following project-relevant packages are already available in the global Python environment:

| Package | Version | Needed? |
|---------|---------|---------|
| numpy | 2.4.6 | ✅ Yes |
| pandas | 3.0.3 | ✅ Yes |
| scipy | 1.18.0 | ✅ Yes |
| scikit-learn | 1.9.0 | ✅ Yes |
| plotly | 6.9.0 | ✅ Yes |
| pydeck | 0.9.1 | ✅ Yes |
| matplotlib | 3.11.1 | ✅ Yes |
| streamlit | 1.59.2 | ✅ Yes |
| jupyterlab | 4.5.6 | ✅ Yes |
| flake8 | 7.3.0 | ✅ Yes |
| black | 26.5.1 | ✅ Yes |

> [!NOTE]
> While these are available globally, we still recommend using a **virtual environment** to isolate project dependencies and ensure reproducibility.

---

## Step-by-Step Setup

### 1. Create a Virtual Environment

```powershell
# Navigate to the project directory
cd C:\Users\HP\.gemini\antigravity\scratch\terrain-intelligence

# Create virtual environment
python -m venv .venv

# Activate it
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation due to execution policy:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 2. Install Dependencies

```powershell
# Upgrade pip first
python -m pip install --upgrade pip

# Install from requirements.txt
pip install -r requirements.txt
```

#### Troubleshooting: Rasterio / GDAL on Windows

If `rasterio` fails to install (common on Windows with new Python versions):

**Option A** — Use pre-built wheels from Christoph Gohlke's archive:
```powershell
# Check https://github.com/cgohlke/geospatial-wheels for available wheels
# Download the appropriate .whl file for your Python version
pip install path\to\rasterio-X.Y.Z-cpXXX-win_amd64.whl
```

**Option B** — Use conda/mamba (if available):
```powershell
conda install -c conda-forge rasterio geopandas xarray
```

**Option C** — Fall back to Python 3.11:
```powershell
py -3.11 -m venv .venv311
.venv311\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 3. Verify Installation

```powershell
python -c "
import numpy; print(f'NumPy: {numpy.__version__}')
import pandas; print(f'Pandas: {pandas.__version__}')
import scipy; print(f'SciPy: {scipy.__version__}')
import sklearn; print(f'Scikit-learn: {sklearn.__version__}')
import plotly; print(f'Plotly: {plotly.__version__}')
# Geospatial — these may need special attention
try:
    import rasterio; print(f'Rasterio: {rasterio.__version__}')
except ImportError:
    print('Rasterio: NOT INSTALLED — see troubleshooting')
try:
    import geopandas; print(f'GeoPandas: {geopandas.__version__}')
except ImportError:
    print('GeoPandas: NOT INSTALLED — see troubleshooting')
print('Verification complete.')
"
```

### 4. Configure Jupyter

```powershell
# Register the virtual environment as a Jupyter kernel
python -m ipykernel install --user --name terrain-intelligence --display-name "Terrain Intelligence"
```

Then in JupyterLab, select the "Terrain Intelligence" kernel for notebooks.

### 5. Initialize Git

```powershell
cd C:\Users\HP\.gemini\antigravity\scratch\terrain-intelligence

# Initialize repository
git init

# Create .gitignore
@"
# Python
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/
.venv/
venv/

# Jupyter
.ipynb_checkpoints/

# Data (do not commit large datasets)
data/
*.tif
*.tiff
*.hdf
*.hdf5
*.nc
*.img

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/

# Environment
.env
"@ | Set-Content .gitignore

# Initial commit
git add .
git commit -m "docs: initial project structure and preparation documentation"
```

### 6. VS Code Configuration

Recommended extensions for this project:

| Extension | Purpose |
|-----------|---------|
| Python (ms-python.python) | Python language support |
| Pylance (ms-python.vscode-pylance) | Type checking and IntelliSense |
| Jupyter (ms-toolsai.jupyter) | Notebook support |
| GitLens (eamodio.gitlens) | Git history and blame |
| Markdown All in One (yzhang.markdown-all-in-one) | Markdown preview and editing |

Recommended `settings.json` additions:
```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
    "python.formatting.provider": "black",
    "python.linting.flake8Enabled": true,
    "editor.formatOnSave": true,
    "files.trimTrailingWhitespace": true
}
```

---

## Pre-Hackathon Verification Checklist

| # | Check | Status |
|---|-------|--------|
| 1 | Virtual environment created and activated | ☐ |
| 2 | All requirements.txt packages installed | ☐ |
| 3 | Rasterio imports successfully | ☐ |
| 4 | GeoPandas imports successfully | ☐ |
| 5 | Jupyter kernel registered and working | ☐ |
| 6 | Git initialized with .gitignore | ☐ |
| 7 | Can open one GeoTIFF with rasterio | ☐ |
| 8 | Can run Streamlit (`streamlit hello`) | ☐ |
| 9 | NASA Earthdata account created | ☐ |
| 10 | Copernicus Data Space account created | ☐ |

---

## Dependency Compatibility Notes

| Package | Notes |
|---------|-------|
| **rasterio** | Requires GDAL. Windows binary wheels may lag behind new Python versions. Test first. |
| **geopandas** | Depends on GDAL, GEOS, PROJ. Usually installs cleanly via pip on Windows with wheels. |
| **xarray** | Pure Python; no binary dependencies. Should install on any Python 3.9+. |
| **pyproj** | Requires PROJ. Usually available as wheel. |
| **shapely** | Requires GEOS. Version 2.0+ typically available as wheel. |
| **pydeck** | Requires `@deck.gl` JS libraries loaded by Streamlit/Jupyter. No special setup. |
| **streamlit** | Large dependency tree but well-maintained wheels. |

---

*Document status: Setup guide based on system inspection of November 3, 2026. Test all steps during prep week.*
