import math

from ds.graph.graph_core import GraphCore


def bellman_ford(graph, src):
    """
    Complexity = O(EV)
    Works for negative edges unlike Dijkstra.
    """
    distances = {}
    for vertex in graph.vertices:
        distances[vertex] = math.inf
    distances[src] = 0
    for _ in range(len(graph.vertices)):
        for src, edges in graph.get_all_edges().items():
            for neigh, edge in edges.items():
                wt = edge["weight"]
                distances[neigh] = min(distances[neigh], distances[src] + wt)

    # If there is no negative cycle, doing the relaxation one more time
    # will have no effect on any of the distances.
    for src, edges in graph.get_all_edges().items():
        for neigh, edge in edges.items():
            wt = edge["weight"]
            if distances[src] + wt < distances[neigh]:
                # Note that this will be reported only if any of the
                # negative cycle vertices are reachable from src.
                raise Exception("Negative cycle exists!")
    return distances


def main():
    graph = GraphCore()
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 1)
    graph.add_edge(1, 2, 2)
    graph.add_edge(1, 4, 3)
    graph.add_edge(2, 1, 2)
    graph.add_edge(2, 3, 2)
    graph.add_edge(3, 4, 3)
    # graph.add_edge(0, 10, 1)
    # graph.add_edge(10, 11, -1)
    # graph.add_edge(11, 10, -1)
    distances = bellman_ford(graph, 0)
    print(distances)


if __name__ == "__main__":
    main()
