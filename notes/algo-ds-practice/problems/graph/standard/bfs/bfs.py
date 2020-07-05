from collections import deque
from ds.graph.graph_core import GraphCore


def bfs(graph, src, dst):
    visited = set()
    distance = {}
    bfs_queue = deque()

    bfs_queue.append(src)
    visited.add(src)
    distance[src] = 0
    while bfs_queue:
        current = bfs_queue.popleft()
        if current == dst:
            return distance[dst]
        current_dist = distance[current]
        current_edges = graph.get_edges(current)
        for neighbour in current_edges:
            if neighbour not in visited:
                bfs_queue.append(neighbour)
                distance[neighbour] = current_dist + 1
                visited.add(neighbour)
    return None


def main():
    graph = GraphCore(True)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    print(graph)
    dist = bfs(graph, 3, 1)
    print(dist)


if __name__ == "__main__":
    main()
