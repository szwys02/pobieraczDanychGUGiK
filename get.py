# Import external modules
from requests import Request

# Download data from geoportal
url = 'http://mapy.geoportal.gov.pl/wss/service/PZGIK/PRG/WFS/AdministrativeBoundaries?language=pol&SERVICE=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAMES='
url_rest = '&STARTINDEX=0&COUNT=999999&SRSNAME=urn:ogc:def:crs:EPSG::2180'
layer = 'ms:A02_Granice_powiatow'
full_url = url + layer + url_rest

wfs = Request('GET', full_url).prepare().url
