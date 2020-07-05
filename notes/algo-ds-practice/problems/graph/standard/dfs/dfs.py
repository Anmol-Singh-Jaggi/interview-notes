# Refer to assets/dfs_edges.pdf for detail.
from ds.graph.graph_core import GraphCore


class AlgoState:
    def __init__(self):
        self.parent = {}
        self.start_time = {}
        self.finish_time = {}
        self.tree_edges = set()
        self.back_edges = set()
        self.forward_edges = set()
        self.cross_edges = set()
        self.current_time = 0
        self.order = []

    def __repr__(self):
        res = ''
        res += f'Tree edges:\n{self.tree_edges}\n\n'
        res += f'Back edges:\n{self.back_edges}\n\n'
        res += f'Forward edges:\n{self.forward_edges}\n\n'
        res += f'Cross edges:\n{self.cross_edges}\n\n'
        res += f'Parent mapping:\n{self.parent}\n\n'
        res += f'Topo order:\n{self.order}\n\n'
        return res


def get_dfs_edges(graph):
    state = AlgoState()
    for vertex in graph.vertices:
        if vertex not in state.parent:
            state.parent[vertex] = None
            dfs(graph, vertex, state)
    return state


def dfs(graph, src, state):
    src_edges = graph.get_edges(src)
    state.start_time[src] = state.current_time
    state.current_time += 1
    for neighbour in src_edges:
        edge = (src, neighbour)
        if neighbour not in state.parent:
            state.parent[neighbour] = src
            state.tree_edges.add(edge)
            dfs(graph, neighbour, state)
        elif neighbour not in state.finish_time:
            state.back_edges.add(edge)
        elif state.start_time[neighbour] > state.start_time[src]:
            state.forward_edges.add(edge)
        else:
            state.cross_edges.add(edge)
    state.finish_time[src] = state.current_time
    state.current_time += 1
    state.order.append(src)


def main():
    graph = GraphCore(True)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(2, 5)
    graph.add_edge(3, 2)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    print(graph)
    state = get_dfs_edges(graph)
    print(state)


if __name__ == "__main__":
    main()
