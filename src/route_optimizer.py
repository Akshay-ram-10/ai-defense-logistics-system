import networkx as nx

def create_graph():

    G = nx.Graph()

    # distances between locations
    G.add_edge("HQ", "Base_A", weight=10)
    G.add_edge("HQ", "Base_B", weight=6)
    G.add_edge("Base_A", "Base_C", weight=7)
    G.add_edge("Base_B", "Base_D", weight=5)
    G.add_edge("Base_C", "Base_E", weight=4)
    G.add_edge("Base_D", "Base_E", weight=8)

    return G


def best_route(G, start, end):

    path = nx.shortest_path(G, start, end, weight="weight")
    distance = nx.shortest_path_length(G, start, end, weight="weight")

    return path, distance


if __name__ == "__main__":

    G = create_graph()

    route, distance = best_route(G, "HQ", "Base_E")

    print("Best Route:", route)
    print("Total Distance:", distance)