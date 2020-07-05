from ds.graph.graph_core import GraphCore


def dfs_iterative(graph, start):
    visited = set()
    path = []
    dfs_q = [start]
    while dfs_q:
        current = dfs_q.pop()
        if current not in visited:
            visited.add(current)
            path.append(current)
            edges = graph.get_edges(current)
            dfs_q.extend(edges.keys())
    return path


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
    path = dfs_iterative(graph, 1)
    print(path)


if __name__ == "__main__":
    main()
