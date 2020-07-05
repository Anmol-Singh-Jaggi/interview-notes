from ds.graph.graph_core import GraphCore
from enum import Enum


class NodeStatus(Enum):
    VISITED = 0
    VISITING = 1
    UNVISITED = 2


def dfs(index, graph, color, visit_order):
    for neigh in graph.get_edges(index).keys():
        if color[neigh] == NodeStatus.VISITING:
            # Found a back-edge from index to neigh.
            print(f'Back-edge from {index} -> {neigh}!')
            return True
        if color[neigh] != NodeStatus.VISITED:
            color[neigh] = NodeStatus.VISITING
            ret = dfs(neigh, graph, color, visit_order)
            if ret:
                return True
    visit_order.append(index)
    color[index] = NodeStatus.VISITED
    return False


def get_topo_sort(graph: GraphCore):
    color = {}
    visit_order = []
    for src in graph.vertices:
        color[src] = NodeStatus.UNVISITED
    for src in graph.vertices:
        if color[src] == NodeStatus.VISITED:
            continue
        color[src] = NodeStatus.VISITING
        ret = dfs(src, graph, color, visit_order)
        if ret:
            return None
    visit_order.reverse()
    return visit_order


def main():
    graph = GraphCore(False)
    graph.add_edge(0, 1)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    print(graph)
    ans = get_topo_sort(graph)
    print(ans)


if __name__ == "__main__":
    main()
