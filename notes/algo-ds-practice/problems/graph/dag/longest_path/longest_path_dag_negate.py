from ds.graph.graph_core import GraphCore
from problems.graph.dag.shortest_path.shortest_path_dag_topo import (
    shortest_path_dag_topo,
)


def longest_path_dag_negate(graph: GraphCore, src):
    """
    Computes the single-source longest path from a source vertex src.
    Works for negative edges also!
    First negate all the edges (5 becomes -5).
    Then find the shortest path from src to all nodes.
    Multipy the distances with -1 to reverse negation.
    """
    for _, edges in graph.get_all_edges().items():
        for __, edge in edges.items():
            edge["weight"] = -edge["weight"]
    distances = shortest_path_dag_topo(graph, src)
    for node in distances:
        distances[node] = -distances[node]
    return distances


def main():
    graph = GraphCore()
    graph.add_edge(2, 3, 1)
    graph.add_edge(3, 1, 1)
    graph.add_edge(4, 0, 1)
    graph.add_edge(4, 1, 1)
    graph.add_edge(5, 0, 1)
    graph.add_edge(5, 2, 1)
    distances = longest_path_dag_negate(graph, 2)
    print(graph)
    print(distances)


if __name__ == "__main__":
    main()
