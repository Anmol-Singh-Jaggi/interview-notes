from ds.graph.graph_core import GraphCore
from collections import deque


class AlgoState:
    def __init__(self):
        self.visit_stack = deque()
        self.on_stack = set()
        # When was this vertex discovered.
        self.index = {}
        # The discovery time of the lowest vertex reachable
        # from subtree rooted at this vertex including at max 1 back edge.
        self.ancestor_index = {}
        # The global index count.
        self.index_count = 0
        # The mapping used to store the final answer.
        self.parent_mapping = {}


def visit(src, graph, algo_state):
    index, ancestor_index = algo_state.index, algo_state.ancestor_index
    visit_stack, on_stack = algo_state.visit_stack, algo_state.on_stack
    index[src] = algo_state.index_count
    ancestor_index[src] = algo_state.index_count
    algo_state.index_count += 1
    visit_stack.append(src)
    on_stack.add(src)
    for neigh in graph.get_edges(src):
        if neigh not in index:
            # Tree-edge
            visit(neigh, graph, algo_state)
            ancestor_index[src] = min(ancestor_index[src],
                                      ancestor_index[neigh])
        elif neigh in on_stack:
            # Back-edge
            # neigh is in the SCC.
            # Note that no point in using min(ancestor[src], ancestor[neigh])
            # as ancestor of neigh might not have been correctly computed at this point.
            ancestor_index[src] = min(ancestor_index[src], index[neigh])
        else:
            # Cross-edge
            pass

    parent_mapping = algo_state.parent_mapping
    if index[src] == ancestor_index[src]:
        # Generate new SCC.
        while True:
            node = visit_stack.pop()
            on_stack.remove(node)
            parent_mapping[node] = src
            if node == src:
                break


def get_strongly_connected_components(graph: GraphCore):
    algo_state = AlgoState()
    for src in graph.vertices:
        if src not in algo_state.index:
            visit(src, graph, algo_state)
    return algo_state.parent_mapping


def main():
    graph = GraphCore(False)
    graph.add_edge(1, 2)
    graph.add_edge(2, 1)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 2)
    print(graph)
    parent_mapping = get_strongly_connected_components(graph)
    print(parent_mapping)


if __name__ == "__main__":
    main()
