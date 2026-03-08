import pandas as pd
import networkx as nx
import os

# get path
current_dir = os.path.dirname(__file__)
data_path = os.path.join(current_dir, "..", "data", "supply_data.csv")

# load data
df = pd.read_csv(data_path)

# create graph
G = nx.Graph()

# add HQ
G.add_node("HQ")

# connect HQ to bases
for index, row in df.iterrows():

    base = row["base"]

    # random example distance
    distance = (index + 1) * 5

    G.add_edge("HQ", base, weight=distance)

# find best route
path = nx.shortest_path(G, "HQ", "Base_E", weight="weight")

print("Best Route:", path)