"""
COSMONOVA — Environment Verification Script
Planetary Analog Intelligence Platform
NASA Space Apps Challenge 2026 Preparation
"""

import sys
import platform
import io

# Ensure UTF-8 output on Windows consoles
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

print("=" * 70)
print("  [*] COSMONOVA - SYSTEM ENVIRONMENT AUDIT")
print("  [*] Planetary Analog Intelligence Platform")
print("=" * 70)

print(f"\n[System Info]")
print(f"  OS Platform      : {platform.system()} {platform.release()} ({platform.version()})")
print(f"  Architecture     : {platform.machine()}")
print(f"  Python Version   : {platform.python_version()} ({platform.architecture()[0]})")
print(f"  Python Binary    : {sys.executable}")

packages = [
    ("numpy", "NumPy (Numerical processing)"),
    ("pandas", "Pandas (Data analysis)"),
    ("scipy", "SciPy (Scientific computing)"),
    ("sklearn", "Scikit-Learn (Machine learning / clustering)"),
    ("plotly", "Plotly (Interactive visualization)"),
    ("pydeck", "PyDeck (Geospatial 3D visualization)"),
    ("streamlit", "Streamlit (Dashboard web framework)"),
    ("matplotlib", "Matplotlib (Static plotting)"),
    ("geopandas", "GeoPandas (Vector geospatial)"),
    ("rasterio", "Rasterio (Raster GDAL interface)"),
    ("xarray", "Xarray (Multidimensional arrays)"),
    ("shapely", "Shapely (Geometric operations)"),
    ("pyproj", "PyProj (Coordinate transformations)")
]

print(f"\n[Package Verification]")
all_core_ok = True
for pkg_name, desc in packages:
    try:
        mod = __import__(pkg_name)
        ver = getattr(mod, "__version__", "installed")
        print(f"  [OK]  {desc:<45}: v{ver}")
    except ImportError:
        if pkg_name in ["rasterio", "geopandas", "xarray", "shapely", "pyproj"]:
            print(f"  [--]  {desc:<45}: NOT INSTALLED (Geospatial optional for prep phase)")
        else:
            print(f"  [FAIL] {desc:<45}: NOT INSTALLED")
            all_core_ok = False

print("\n" + "=" * 70)
if all_core_ok:
    print("  STATUS: Core data analysis, web dashboard, and visualization stack is READY!")
    print("  To launch the interactive explorer dashboard, run:")
    print("    streamlit run app.py")
else:
    print("  STATUS: Some dependencies are missing. Run: pip install -r requirements.txt")
print("=" * 70 + "\n")
