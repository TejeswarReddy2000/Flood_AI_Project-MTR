import ee
import geemap

# Initialize Earth Engine
ee.Initialize(project='powered-flood-system')

# Select region (Andhra Pradesh)
region = ee.Geometry.Rectangle([79, 13, 84, 17])

# Load Sentinel-1
sentinel1 = (
    ee.ImageCollection("COPERNICUS/S1_GRD")
    .filterBounds(region)
    .filterDate("2024-07-01", "2024-07-10")
    .filter(ee.Filter.eq('instrumentMode', 'IW'))
    .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV'))
    .select('VV')
)

# Median image
median_image = sentinel1.median()

# Flood detection (threshold)
flood_mask = median_image.lt(-15)

# Create map
Map = geemap.Map(center=[15.5, 81], zoom=6)

# Add layers
Map.addLayer(median_image, {'min': -25, 'max': 0}, 'Sentinel-1 VV')
Map.addLayer(flood_mask.updateMask(flood_mask), {'palette': ['blue']}, 'Flood Area')

# Display map
Map
