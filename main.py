from requests import Request
import geopandas as gpd

# Download data from geoportal
url = 'http://mapy.geoportal.gov.pl/wss/service/PZGIK/PRG/WFS/AdministrativeBoundaries?language=pol&SERVICE=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAMES='
url_rest = '&STARTINDEX=0&COUNT=999999&SRSNAME=urn:ogc:def:crs:EPSG::2180'
layer = 'ms:A02_Granice_powiatow'
full_url = url + layer + url_rest

wfs_get = Request('GET', full_url).prepare().url

# Create GUI with user's input
    # Ask user for administrative border
    # Choosing specific boundaries by name is optional

# Manage downloaded data
# Management must be sensible to user's input
gdf = gpd.read_file(wfs_get)
gdf_subset = gdf[gdf['JPT_KOD_JE'].str.startswith('25')]
gdf.to_file('~/gis/test.gpkg', driver='GPKG')
gdf_subset.to_file('~/gis/test_sub.gpkg', driver='GPKG')
