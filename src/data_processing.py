import pandas as pd
import os

# Get the absolute path of the current script
current_dir = os.path.dirname(__file__)

# Go one level up and access data folder
data_path = os.path.join(current_dir, "..", "data", "supply_data.csv")

def load_data():
    df = pd.read_csv(data_path)
    return df

def summary(df):
    print("Total locations:", df["base"].nunique())
    print("Supply types:", df["supply_type"].unique())

if __name__ == "__main__":
    df = load_data()
    summary(df)