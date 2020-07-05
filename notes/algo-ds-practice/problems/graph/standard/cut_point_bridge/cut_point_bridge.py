from ds.graph.graph_core import GraphCore
'''
Cut points and bridges are defined only for undirected graphs,
even though the algo is very similar to Tarjan's Strongly Connected Components for directed graphs.
'''


class AlgoState:
    def __init__(self):
        self.cut_points = set()
        self.bridges = set()
        self.parent = {}
        # When was this vertex discovered.
        self.index = {}
        # The discovery time of the lowest vertex reachable
        # from subtree rooted at this vertex including at max 1 back edge.
        self.ancestor_index = {}
        # The global index count.
        self.index_count = 0


def visit(src, graph, algo_state):
    index, ancestor_index = algo_state.index, algo_state.ancestor_index
    cut_points, parent = algo_state.cut_points, algo_state.parent
    index[src] = algo_state.index_count
    ancestor_index[src] = algo_state.index_count
    algo_state.index_count += 1
    num_children_unvisited = 0
    for neigh in graph.get_edges(src):
        if neigh not in index:
            num_children_unvisited += 1
            parent[neigh] = src
            visit(neigh, graph, algo_state)
            ancestor_index[src] = min(ancestor_index[src],
                                      ancestor_index[neigh])
            if parent[src] is None and num_children_unvisited > 1:
                cut_points.add(src)
            if parent[src] is not None and ancestor_index[neigh] >= index[src]:
                cut_points.add(src)
            if ancestor_index[neigh] > index[src]:
                algo_state.bridges.add((src, neigh))
        elif neigh != parent[src]:
            # To know why we are not using ancestor_index[neigh]
            # read the last para of this:
            # https://www.quora.com/q/lbsknuilzujwaqtg/Cut-Vertex-Articulation-point
            ancestor_index[src] = min(ancestor_index[src], index[neigh])


def get_bridges_cut_points(graph: GraphCore):
    algo_state = AlgoState()
    for src in graph.vertices:
        if src not in algo_state.index:
            algo_state.parent[src] = None
            visit(src, graph, algo_state)
    return algo_state.cut_points, algo_state.bridges


def main():
    graph = GraphCore(True)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 3)
    graph.add_edge(4, 2)
    print(graph)
    ans = get_bridges_cut_points(graph)
    print(ans)


if __name__ == "__main__":
    main()
