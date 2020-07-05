from ds.graph.graph_core import GraphCore
from problems.graph.standard.topo_sort.topo_sort import compute_in_degrees


def compute_longest_path_starting_at(graph: GraphCore, src, longest_distances):
    if src in longest_distances:
        return longest_distances[src]
    longest_path_distance = 1
    for neigh, edge_weight in graph.get_edges(src).items():
        longest_path_distance = max(
            longest_path_distance,
            compute_longest_path_starting_at(graph, neigh, longest_distances)
            + edge_weight["weight"],
        )
    longest_distances[src] = longest_path_distance
    return longest_path_distance


def longest_path_dag_dp(graph: GraphCore):
    '''
    Computes the longest path starting from any vertex.
    Works for negative edges also!
    Starting from all the vertices whose in-degree is 0,
    we will apply the following algo for every neighour:
    ans[current] = max(ans[neigh] + edge_weight[current][neigh])
    Note that there is no need for doing topo sort.
    '''
    in_degrees = compute_in_degrees(graph)
    in_degrees_zero = set()
    # longest_distances[5] means the length of the longest path starting at node 5.
    longest_distances = {}
    for vertex, in_degree in in_degrees.items():
        if in_degree == 0:
            in_degrees_zero.add(vertex)
    for vertex in in_degrees_zero:
        compute_longest_path_starting_at(graph, vertex, longest_distances)
    if not longest_distances:
        return 0
    # Return the absolute longest path starting from any node to any other node.
    return max(longest_distances.values())


def main():
    graph = GraphCore()
    graph.add_edge(2, 3, 1)
    graph.add_edge(3, 1, 1)
    graph.add_edge(4, 0, 1)
    graph.add_edge(4, 1, 1)
    graph.add_edge(5, 0, 1)
    graph.add_edge(5, 2, 1)
    longest_path = longest_path_dag_dp(graph)
    print(graph)
    print(longest_path)


if __name__ == "__main__":
    main()
