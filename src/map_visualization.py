import pandas as pd
import folium
import os

# locate dataset
current_dir = os.path.dirname(__file__)
data_path = os.path.join(current_dir, "..", "data", "supply_data.csv")

df = pd.read_csv(data_path)

# center map
center_lat = df["latitude"].mean()
center_lon = df["longitude"].mean()

m = folium.Map(location=[center_lat, center_lon], zoom_start=10)

# add HQ location
hq_lat = center_lat
hq_lon = center_lon

folium.Marker(
    location=[hq_lat, hq_lon],
    popup="HQ",
    icon=folium.Icon(color="red")
).add_to(m)

# store coordinates
coordinates = [[hq_lat, hq_lon]]

# add base markers
for _, row in df.iterrows():

    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=f"{row['base']} | {row['supply_type']} | Qty:{row['quantity']}",
        icon=folium.Icon(color="blue")
    ).add_to(m)

    coordinates.append([row["latitude"], row["longitude"]])

# draw route
folium.PolyLine(
    locations=coordinates,
    color="green",
    weight=4
).add_to(m)

# save map
m.save("logistics_route_map.html")

print("Map created: logistics_route_map.html")