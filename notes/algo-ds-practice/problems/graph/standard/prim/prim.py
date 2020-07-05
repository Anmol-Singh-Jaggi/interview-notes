# Verified on SPOJ - https://www.spoj.com/problems/MST/
from ds.graph.graph_core import GraphCore
from queue import PriorityQueue
from ds.heap.heap_advanced import Heap


def prim(graph: GraphCore):
    '''
    1. Let current vertex `u` be vertices[0]. (Any random vertex)
    2. Add `u` to the MST vertices set `vertices_in_mst`.
    3. Add all the edges (u, v) to a heap for all v not already in MST.
    4. Find the lowest edge from heap such that the destination vertex `v` is not already in MST.
    5. Let this vertex `v` be the next vertex to process. Goto 1.
    6. Loop will end when MST set size === number of vertices.
    Complexity = O(ElogE)
    Kruskal is easier to implement and reason about!!
    '''
    edges_in_mst = []
    vertices_in_mst = set()
    # A heap containing the edges connecting MST with non-MST vertices.
    connecting_edges_pq = PriorityQueue()
    current_vertex = next(iter(graph.vertices))
    vertices_in_mst.add(current_vertex)
    while len(vertices_in_mst) < len(graph.vertices):
        vertex_edges = graph.get_edges(current_vertex)
        for dst, edge_props in vertex_edges.items():
            if dst in vertices_in_mst:
                continue
            connecting_edges_pq.put((edge_props["weight"], current_vertex,
                                     dst))
        lightest_edge = connecting_edges_pq.get()
        dst = lightest_edge[2]
        while dst in vertices_in_mst:
            # CAREFUL: Most important step.
            # Make sure to ignore all the vertices already processed.
            # Note: We wouldn't have needed this if we could somehow remove
            # all the edges (*, dst) from the heap efficiently.
            lightest_edge = connecting_edges_pq.get()
            dst = lightest_edge[2]
        edges_in_mst.append(lightest_edge)
        vertices_in_mst.add(dst)
        current_vertex = dst
    return edges_in_mst


def prim2(graph: GraphCore):
    pq = Heap()
    visited = set()
    src = next(iter(graph.vertices))
    visited.add(src)
    edges = set()
    for edge in graph.get_edges(src).items():
        dst, edge_props = edge
        weight = edge_props['weight']
        pq.push((weight, src, dst))
    while len(visited) != len(graph.vertices) and pq.size() > 0:
        top = pq.pop()
        while pq.size() > 0:
            weight, src, dst = top
            if dst not in visited:
                break
            top = pq.pop()
        visited.add(dst)
        edges.add(top)
        if len(visited) == len(graph.vertices):
            break
        src = dst
        for edge in graph.get_edges(src).items():
            dst, edge_props = edge
            weight = edge_props['weight']
            if dst not in visited:
                pq.push((weight, src, dst))
    return edges


def main():
    # Will give wrong result if the graph is not bi-directional !!!
    graph1 = GraphCore(True)
    graph1.add_edge(1, 2, 5)
    graph1.add_edge(2, 3, 6)
    graph1.add_edge(1, 3, 2)
    mst = prim(graph1)
    print(mst)


if __name__ == "__main__":
    main()
