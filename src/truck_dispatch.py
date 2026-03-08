import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import os

# locate dataset
current_dir = os.path.dirname(__file__)
data_path = os.path.join(current_dir, "..", "data", "demand_history.csv")

df = pd.read_csv(data_path)

bases = df["base"].unique()

predictions = []

# predict demand
for base in bases:

    base_data = df[df["base"] == base]

    X = base_data[["day"]]
    y = base_data["food_demand"]

    model = LinearRegression()
    model.fit(X, y)

    next_day = np.array([[6]])

    prediction = model.predict(next_day)

    predictions.append((base, int(prediction[0])))

# sort by highest demand
predictions.sort(key=lambda x: x[1], reverse=True)

# simulate trucks
truck_number = 1

print("\nTruck Dispatch Plan\n")

for base, demand in predictions:

    print(f"Truck {truck_number} → {base} | Supply Needed: {demand}")
    truck_number += 1