# Verified on SPOJ - https://www.spoj.com/problems/MST/
from ds.graph.graph_core import GraphCore
from ds.disjoint_set.disjoint_set import DisjointSet


def kruskal(graph):
    '''
    Complexity = O(ElogE)
    '''
    edges = []
    for vertex in graph.vertices:
        vertex_edges = graph.get_edges(vertex)
        for dst, edge_props in vertex_edges.items():
            edges.append((edge_props["weight"], vertex, dst))
    edges.sort()
    dset = DisjointSet()
    edges_mst = []
    for edge in edges:
        src = edge[1]
        dst = edge[2]
        if dset.find_parent(src) != dset.find_parent(dst):
            dset.join(src, dst)
            edges_mst.append(edge)
    return edges_mst


def main():
    graph1 = GraphCore(True)
    graph1.add_edge(1, 2, 5)
    graph1.add_edge(2, 3, 6)
    graph1.add_edge(1, 3, 2)
    mst = kruskal(graph1)
    print(mst)


if __name__ == "__main__":
    main()
