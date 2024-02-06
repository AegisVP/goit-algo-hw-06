from assignment1 import austria_roads

from collections import deque


def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()

    visited.add(vertex)
    print(vertex, end=' ')  # Відвідуємо вершину

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = set()

    if not queue:
        return

    vertex = queue.popleft()

    if vertex not in visited:
        print(vertex, end=" ")

        visited.add(vertex)

        queue.extend(set(graph[vertex]) - visited)
    bfs_recursive(graph, queue, visited)


if __name__ == "__main__":
    dfs_recursive(austria_roads, "Vienna")
    print()
    bfs_recursive(austria_roads, deque(["Vienna"]))
