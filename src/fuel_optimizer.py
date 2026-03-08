import pandas as pd
import os

# locate dataset
current_dir = os.path.dirname(__file__)
data_path = os.path.join(current_dir, "..", "data", "supply_data.csv")

df = pd.read_csv(data_path)

# assume HQ coordinates
hq_lat = df["latitude"].mean()
hq_lon = df["longitude"].mean()

# truck efficiency
fuel_efficiency = 10  # km per litre

total_fuel = 0

print("\nFuel Optimization Report\n")

for _, row in df.iterrows():

    base = row["base"]

    # simple distance approximation
    distance = abs(row["latitude"] - hq_lat) * 111 + abs(row["longitude"] - hq_lon) * 111

    fuel_used = distance / fuel_efficiency

    total_fuel += fuel_used

    print(f"{base}")
    print(f"Distance ≈ {round(distance,2)} km")
    print(f"Fuel Used ≈ {round(fuel_used,2)} L\n")

print("Total Fuel Required:", round(total_fuel,2), "L")