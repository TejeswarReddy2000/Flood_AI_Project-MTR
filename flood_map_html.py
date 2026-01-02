import ee
import geemap
import webbrowser
import os

ee.Initialize(project='powered-flood-system')

region = ee.Geometry.Rectangle([79, 13, 84, 17])

sentinel1 = (
    ee.ImageCollection("COPERNICUS/S1_GRD")
    .filterBounds(region)
    .filterDate("2024-07-01", "2024-07-10")
    .filter(ee.Filter.eq('instrumentMode', 'IW'))
    .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV'))
    .select('VV')
)

median_image = sentinel1.median()
flood_mask = median_image.lt(-15)

Map = geemap.Map(center=[15.5, 81], zoom=6)
Map.addLayer(median_image, {'min': -25, 'max': 0}, 'Sentinel-1 VV')
Map.addLayer(
    flood_mask.updateMask(flood_mask),
    {'palette': ['0000FF']},
    'Flood Area'
)

file_path = os.path.abspath("flood_map.html")
Map.to_html(file_path)

webbrowser.open("file://" + file_path)

print("✅ Flood map opened in browser")
