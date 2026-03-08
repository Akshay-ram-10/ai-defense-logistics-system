import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import os

# locate dataset
current_dir = os.path.dirname(__file__)
data_path = os.path.join(current_dir, "..", "data", "demand_history.csv")

df = pd.read_csv(data_path)

# get unique bases
bases = df["base"].unique()

print("\nPredicted Demand Tomorrow\n")

for base in bases:

    base_data = df[df["base"] == base]

    X = base_data[["day"]]
    y = base_data["food_demand"]

    model = LinearRegression()
    model.fit(X, y)

    next_day = np.array([[6]])

    prediction = model.predict(next_day)

    print(base, "→", int(prediction[0]))