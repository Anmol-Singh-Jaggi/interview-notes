from ds.graph.graph_core import GraphCore
from ds.disjoint_set.disjoint_set import DisjointSet


def get_connected_components(graph: GraphCore):
    disjoint_set = DisjointSet()
    for src in graph.vertices:
        disjoint_set._add_node_if_absent(src)
    for src, edges in graph.get_all_edges().items():
        for dst in edges.keys():
            disjoint_set.join(src, dst)
    return disjoint_set.get_groups()


def main():
    graph = GraphCore(True)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)
    graph.add_edge(5, 6)
    print(graph)
    ans = get_connected_components(graph)
    print(ans)


if __name__ == "__main__":
    main()
