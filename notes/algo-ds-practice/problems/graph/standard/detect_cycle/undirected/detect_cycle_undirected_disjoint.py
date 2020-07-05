from ds.graph.graph_core import GraphCore
from ds.disjoint_set.disjoint_set import DisjointSet


def is_cyclic(graph: GraphCore):
    disjoint_set = DisjointSet()
    for src, edges in graph.get_all_edges().items():
        for dst in edges.keys():
            if dst > src:
                # CAREFUL: This is important!!
                # So that we dont process an edge twice!
                continue
            if disjoint_set.find_parent(src) == disjoint_set.find_parent(dst):
                return True
            disjoint_set.join(src, dst)
    return False


def main():
    graph = GraphCore(True)
    graph.add_edge(0, 1)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 2)
    print(graph)
    ans = is_cyclic(graph)
    print(ans)


if __name__ == "__main__":
    main()
