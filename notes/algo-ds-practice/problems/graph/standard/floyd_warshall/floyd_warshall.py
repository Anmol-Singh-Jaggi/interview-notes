from math import inf
from ds.graph.graph_core import GraphCore


def floyd_warshall(graph):
    '''
    Complexity = O(n^3)
    '''
    vertices = graph.vertices
    num_vertices = len(vertices)
    dp = [[inf for i in range(num_vertices)] for j in range(num_vertices)]
    path_next = [[None for i in range(num_vertices)] for j in range(num_vertices)]
    all_edges = graph.get_all_edges()
    # Initialize the dp values.
    for src in all_edges:
        edges = graph.get_edges(src)
        for dst, edge_props in edges.items():
            dp[src][dst] = edge_props["weight"]
            path_next[src][dst] = dst
    for i in range(num_vertices):
        dp[i][i] = 0
        path_next[i][i] = i
    # Compute all-source shortest path.
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                intermediate_dist = dp[i][k] + dp[k][j]
                if intermediate_dist < dp[i][j]:
                    dp[i][j] = intermediate_dist
                    # CAREFUL
                    path_next[i][j] = path_next[i][k]
    return dp, path_next


def print_path(path_next, src, dst):
    if path_next[src][dst] is None:
        return []
    path = [src]
    while src != dst:
        src = path_next[src][dst]
        path.append(src)
    return path


def main():
    graph = GraphCore()
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 1)
    graph.add_edge(1, 2, 2)
    graph.add_edge(1, 4, 3)
    graph.add_edge(2, 1, 2)
    graph.add_edge(2, 3, 2)
    graph.add_edge(3, 4, 3)
    distances, paths = floyd_warshall(graph)
    print(distances)
    print(paths)


if __name__ == "__main__":
    main()
