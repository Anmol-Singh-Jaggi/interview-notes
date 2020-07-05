from math import inf

from ds.graph.graph_core import GraphCore
from problems.graph.standard.topo_sort.topo_sort import topo_sort


def longest_path_dag_topo(graph: GraphCore, src):
    """
    Single-Source Longest Path.
    Works even for negative edges!
    First get the topological sort order.
    Then in that order, do the following for every vertex 'curr':
    dist[neigh] = max(dist[neigh], dist[curr] + edge_weight).
    Complexity -> O(V+E)
    """
    topo_order = topo_sort(graph)
    assert(topo_order is not None)
    # distances[5] means the longest distance from node 'src' to node 5.
    distances = {}
    for vertex in graph.vertices:
        distances[vertex] = -inf
    distances[src] = 0
    for curr in topo_order:
        if distances[curr] == -inf:
            continue
        for neigh, edge_props in graph.get_edges(curr).items():
            weight = edge_props["weight"]
            distances[neigh] = max(distances[neigh], distances[curr] + weight)
    return distances


def main():
    graph = GraphCore()
    graph.add_edge(2, 3, 1)
    graph.add_edge(3, 1, 1)
    graph.add_edge(4, 0, 1)
    graph.add_edge(4, 1, 1)
    graph.add_edge(5, 0, 1)
    graph.add_edge(5, 2, 1)
    longest_path = longest_path_dag_topo(graph, 2)
    print(graph)
    print(longest_path)


if __name__ == "__main__":
    main()
