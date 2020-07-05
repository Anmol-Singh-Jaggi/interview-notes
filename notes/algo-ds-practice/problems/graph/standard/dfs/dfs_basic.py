from ds.graph.graph_core import GraphCore


def dfs(graph, src, dst, visited):
    if src in visited or dst in visited:
        return
    visited.add(src)
    src_edges = graph.get_edges(src)
    for neighbour in src_edges:
        dfs(graph, neighbour, dst, visited)


def main():
    graph = GraphCore(False)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(2, 5)
    graph.add_edge(3, 2)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    print(graph)
    visited = set()
    dfs(graph, 1, 4, visited)
    print(visited)


if __name__ == "__main__":
    main()
