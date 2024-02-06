import matplotlib.pyplot as plt
import networkx as nx


def print_table(distances):
    # Верхній рядок таблиці
    print("{:<10} {:^10}".format("Вершина", "Відстань"))
    print("-" * 20)

    # Вивід даних для кожної вершини
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)

        print("{:<10} {:^10}".format(vertex, distance))
    print("\n")


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)
    return distances


if __name__ == "__main__":

    austria_roads = {
        'Vienna': {'Linz': 125, 'Modling': 30},
        'Linz': {'Wels': 30, 'Vienna': 125},
        'Modling': {'Vienna': 30, 'Graz': 120, 'Eisenstadt': 35},
        'Wels': {'Linz': 30, 'Salzburg': 70, 'Graz': 145},
        'Salzburg': {'Innsbruk': 130, 'Villach': 145, 'Wels': 70},
        'Villach': {'Salzburg': 145, 'Klagenfurt': 30},
        'Innsbruk': {'Bregenz': 130, 'Salzburg': 130},
        'Bregenz': {'Innsbruk': 130},
        'Graz': {'Klagenfurt': 95, 'Modling': 120, 'Wels': 145},
        'Klagenfurt': {'Villach': 30, 'Graz': 95},
        'Eisenstadt': {'Modling': 35},
    }
    G = nx.Graph()
    for src, data in austria_roads.items():
        G.add_node(src)

        for dst, weight in data.items():
            G.add_node(dst)
            G.add_edge(src, dst, weight=weight)

    nx.draw(G, with_labels=True)
    plt.show()

    distances_from_wien = dijkstra(austria_roads, 'Vienna')
    print_table(distances_from_wien)
