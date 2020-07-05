from ds.graph.graph_core import GraphCore
from enum import Enum


class NodeStatus(Enum):
    VISITED = 0
    VISITING = 1
    UNVISITED = 2


def is_cyclic(graph: GraphCore):
    color = {}
    for src in graph.vertices:
        color[src] = NodeStatus.UNVISITED
    for src in graph.vertices:
        if color[src] == NodeStatus.VISITED:
            continue
        color[src] = NodeStatus.VISITING
        ret = dfs(src, graph, color)
        if ret:
            return True
    return False


def dfs(index, graph, color):
    for neigh in graph.get_edges(index).keys():
        if color[neigh] == NodeStatus.VISITING:
            # Found a back-edge from index to neigh.
            print(f'Back-edge from {index} -> {neigh}!')
            return True
        if color[neigh] != NodeStatus.VISITED:
            color[neigh] = NodeStatus.VISITING
            ret = dfs(neigh, graph, color)
            if ret:
                return True
    color[index] = NodeStatus.VISITED
    return False


def main():
    graph = GraphCore(False)
    graph.add_edge(0, 1)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 2)
    print(graph)
    ans = is_cyclic(graph)
    print(ans)


if __name__ == "__main__":
    main()
