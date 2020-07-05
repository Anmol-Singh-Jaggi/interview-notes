from ds.graph.graph_core import GraphCore


def get_connected_components(graph: GraphCore):
    visited = set()
    component_set = []
    for src in graph.vertices:
        if src in visited:
            continue
        path = []
        dfs(graph, src, visited, path)
        component_set.append(path)
    return component_set


def dfs(graph, src, visited, path):
    visited.add(src)
    path.append(src)
    src_edges = graph.get_edges(src)
    for neighbour in src_edges:
        if neighbour not in visited:
            dfs(graph, neighbour, visited, path)


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
