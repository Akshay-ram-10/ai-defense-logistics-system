import streamlit as st
import pandas as pd
import os
from sklearn.linear_model import LinearRegression
import numpy as np
import folium
from streamlit_folium import st_folium

# locate datasets
current_dir = os.path.dirname(__file__)
demand_path = os.path.join(current_dir, "..", "data", "demand_history.csv")
supply_path = os.path.join(current_dir, "..", "data", "supply_data.csv")

demand_df = pd.read_csv(demand_path)
supply_df = pd.read_csv(supply_path)

st.title("AI Defense Logistics Command Center")

# -------------------------
# Demand Data
# -------------------------

st.subheader("Historical Demand Data")
st.dataframe(demand_df)

bases = demand_df["base"].unique()
predictions = []

for base in bases:

    base_data = demand_df[demand_df["base"] == base]

    X = base_data[["day"]]
    y = base_data["food_demand"]

    model = LinearRegression()
    model.fit(X, y)

    next_day = np.array([[6]])

    prediction = model.predict(next_day)

    predictions.append((base, int(prediction[0])))

predictions.sort(key=lambda x: x[1], reverse=True)

prediction_df = pd.DataFrame(predictions, columns=["Base", "Predicted Demand"])

st.subheader("Predicted Demand Tomorrow")
st.dataframe(prediction_df)

st.bar_chart(prediction_df.set_index("Base"))

# -------------------------
# Map Visualization
# -------------------------

st.subheader("Supply Base Locations")

center_lat = supply_df["latitude"].mean()
center_lon = supply_df["longitude"].mean()

m = folium.Map(location=[center_lat, center_lon], zoom_start=10)

for _, row in supply_df.iterrows():

    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=f"{row['base']} | {row['supply_type']} | Qty:{row['quantity']}",
        icon=folium.Icon(color="blue")
    ).add_to(m)

st_folium(m, width=700)