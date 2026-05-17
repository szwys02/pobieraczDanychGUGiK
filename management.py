# Import external modules
import geopandas as gpd
# Import project's modules
import get

wfs_get = get.wfs
# Manage downloaded data
# Management must be sensible to user's input
gdf = gpd.read_file(wfs_get)
gdf_subset = gdf[gdf['JPT_KOD_JE'].str.startswith('25')]
# gdf.to_file('~/gis/test.gpkg', driver='GPKG')
# gdf_subset.to_file('~/gis/test_sub.gpkg', driver='GPKG')
