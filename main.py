# Import packages
import PySimpleGUI as gs
import pandas as pd
import geopandas as gpd
import requests
import zipfile
import io

# Download data from geoportal
# Create URL for every administrative border, WMS link: https://integracja.gugik.gov.pl/cgi-bin/PanstwowyRejestrGranic
# url = 'https://integracja.gugik.gov.pl/PRG/pobierz.php?jednostki_administracyjne_shp' 

print("Trwa pobieranie danych")
response = requests.get(url, stream = True)
zipf = zipfile.ZipFile(io.BytesIO(response.content))

zipf.extractall()
print("Wykononano zadanie")

# Create GUI with user's input
    # Ask user for administrative border
    # Choosing specific boundaries by name is optional

# Manage downloaded data
    # Management must be sensible to user's input
