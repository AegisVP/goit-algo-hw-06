import matplotlib.pyplot as plt
import networkx as nx

austria_roads = {
    'Vienna': ['Linz', 'Modling'],
    'Linz': ['Wels', 'Vienna'],
    'Wels': ['Salzburg', 'Linz', 'Graz'],
    'Salzburg': ['Innsbruk', 'Wels', 'Villach'],
    'Innsbruk': ['Bregenz', 'Salzburg'],
    'Bregenz': ['Innsbruk'],
    'Villach': ['Salzburg', 'Klagenfurt'],
    'Klagenfurt': ['Graz', 'Villach'],
    'Graz': ['Modling', 'Klagenfurt', 'Wels'],
    'Modling': ['Graz', 'Vienna', 'Eisenstadt'],
    'Eisenstadt': ['Modling']
}


if __name__ == "__main__":
    G = nx.Graph(austria_roads)

    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")
    print(f"Is connected: {nx.is_connected(G)}")
    print(f"Degree of node 'Vienna': {G.degree['Vienna']}")
    print(f"Betweenness centrality: {nx.betweenness_centrality(G)}")

    nx.draw(G, with_labels=True)
    plt.show()
