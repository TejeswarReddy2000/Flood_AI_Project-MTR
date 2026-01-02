import ee

# Initialize Earth Engine with your project ID
ee.Initialize(project='powered-flood-system')

# -----------------------------
# 1. Select Area (Andhra Pradesh example)
# -----------------------------
region = ee.Geometry.Rectangle([79, 13, 84, 17])

# -----------------------------
# 2. Load Sentinel-1 Radar Data
# -----------------------------
sentinel1 = (
    ee.ImageCollection("COPERNICUS/S1_GRD")
    .filterBounds(region)
    .filterDate("2024-07-01", "2024-07-10")
    .filter(ee.Filter.eq('instrumentMode', 'IW'))
    .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV'))
    .select('VV')
)

# -----------------------------
# 3. Create Median Image
# -----------------------------
median_image = sentinel1.median()

# -----------------------------
# 4. Flood Detection Logic
# Water has LOW radar backscatter
# -----------------------------
flood_mask = median_image.lt(-15)

# -----------------------------
# 5. Calculate Flood Area
# -----------------------------
pixel_area = flood_mask.multiply(ee.Image.pixelArea())

flood_area = pixel_area.reduceRegion(
    reducer=ee.Reducer.sum(),
    geometry=region,
    scale=10,
    maxPixels=1e13
)

area_sqkm = ee.Number(flood_area.get('VV')).divide(1e6)

# -----------------------------
# 6. Print Result
# -----------------------------
print("🌊 Flood Detection Completed")
print("Estimated Flood Area (sq km):", area_sqkm.getInfo())
