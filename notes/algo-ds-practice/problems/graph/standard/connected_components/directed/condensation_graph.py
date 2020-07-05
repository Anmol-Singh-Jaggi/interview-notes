from ds.graph.graph_core import GraphCore
from problems.graph.standard.connected_components.directed.tarjan import get_strongly_connected_components


def get_condensation_graph(graph, parent_mapping):
    cond_graph = GraphCore(False)
    for src, edges in graph.get_all_edges().items():
        parent_src = parent_mapping[src]
        for dst in edges:
            parent_dst = parent_mapping[dst]
            if parent_src == parent_dst:
                continue
            else:
                cond_graph.add_edge(parent_src, parent_dst)
    # For all the vertices which are disconnected from the rest of the graph.
    for src in graph.vertices:
        if parent_mapping[src] == src:
            cond_graph.add_vertex(src)
    return cond_graph


def main():
    graph = GraphCore(False)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)
    graph.add_edge(5, 6)
    graph.add_edge(6, 5)
    graph.add_edge(1, 5)
    graph.add_edge(7, 6)
    print(graph)
    parent_mapping = get_strongly_connected_components(graph)
    print(parent_mapping)
    cond_graph = get_condensation_graph(graph, parent_mapping)
    print(cond_graph)


if __name__ == "__main__":
    main()
