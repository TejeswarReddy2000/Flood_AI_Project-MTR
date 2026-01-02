import ee
import geemap
import webbrowser
import os

# Initialize Earth Engine
ee.Initialize(project='powered-flood-system')

def detect_flood_by_state(state_name, start_date, end_date):

    states = ee.FeatureCollection("FAO/GAUL/2015/level1")
    state = states.filter(ee.Filter.eq("ADM1_NAME", state_name))

    s1 = (
        ee.ImageCollection("COPERNICUS/S1_GRD")
        .filterBounds(state)
        .filterDate(start_date, end_date)
        .filter(ee.Filter.eq("instrumentMode", "IW"))
        .filter(ee.Filter.listContains("transmitterReceiverPolarisation", "VV"))
        .select("VV")
    )

    median = s1.median()
    flood = median.lt(-15)

    flood_area = (
        flood.multiply(ee.Image.pixelArea())
        .reduceRegion(
            reducer=ee.Reducer.sum(),
            geometry=state.geometry(),
            scale=10,
            maxPixels=1e13
        )
    )

    area_sqkm = ee.Number(flood_area.get("VV")).divide(1e6)

    return state, median, flood, area_sqkm


# -----------------------------
# USER INPUT
# -----------------------------
state_name = "Bihar"
start_date = "2024-11-01"
end_date = "2024-11-10"

state, radar, flood, area = detect_flood_by_state(
    state_name, start_date, end_date
)

# Print clear output
print("====================================")
print(f"🌊 Flood Analysis Report")
print(f"State       : {state_name}")
print(f"Date Range  : {start_date} to {end_date}")
print(f"Flood Area  : {area.getInfo():.2f} sq km")
print("====================================")

# Create map
Map = geemap.Map(zoom=6)
Map.centerObject(state, 6)
Map.addLayer(radar, {'min': -25, 'max': 0}, 'Sentinel-1 Radar')
Map.addLayer(flood.updateMask(flood), {'palette': ['0000FF']}, 'Flood Area')
Map.addLayer(state, {}, 'State Boundary')

# Save & open map
file_path = os.path.abspath("flood_state_map.html")
Map.to_html(file_path)
webbrowser.open("file://" + file_path)

print("🗺️ Flood map opened in browser")
