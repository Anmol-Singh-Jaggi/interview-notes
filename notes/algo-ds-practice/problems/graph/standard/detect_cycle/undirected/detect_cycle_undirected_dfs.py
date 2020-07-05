from ds.graph.graph_core import GraphCore


def is_cyclic(graph: GraphCore):
    visited = set()
    for src in graph.vertices:
        if src in visited:
            continue
        visited.add(src)
        ret = dfs(src, graph, visited, -1)
        if ret:
            return True
    return False


def dfs(index, graph, visited, parent):
    for neigh in graph.get_edges(index).keys():
        if neigh not in visited:
            visited.add(neigh)
            ret = dfs(neigh, graph, visited, index)
            if ret:
                return True
        elif neigh != parent:
            print(f'Back edge {index} -> {neigh}')
            return True
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
