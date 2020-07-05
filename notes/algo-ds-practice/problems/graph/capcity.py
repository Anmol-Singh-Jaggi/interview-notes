"""
There are N cities in Flatland connected with M unidirectional roads.
The cities are numbered from 1 to N.
The Flat Circle of Flatland (FCF) wants to set up a new capital city for his kingdom.
For security reasons, the capital must be reachable from all other cities of Flatland.
FCF needs the list of all candidate capital cities.

Example

Input:
4 4 (4 vertices and 4 edges)
1 2
3 2
4 3
2 1

Output:
1 2
(2 candidate cities - 1 and 2)


SOLUTION:

1. Reverse the graph.
2. Find the strongly connected components.
3. Calculate the indegree of each Connected Component.
4. Find the number of CC's with 0 in-degree.
5. If more than 1 or 0, then no capital cities exist.
6. If exactly one CC is there, then the print the nodes of that CC.
"""

from ds.graph.graph_core import GraphCore
from problems.graph.standard.connected_components.directed.kosaraju import (
    get_strongly_connected_components,
)


def get_component_in_degrees(graph, parent_mapping):
    in_degrees = {}
    for src, edges in graph.get_all_edges().items():
        for dst in edges:
            if parent_mapping[src] != parent_mapping[dst]:
                old = in_degrees.get(parent_mapping[dst], 0)
                in_degrees[parent_mapping[dst]] = old
                in_degrees[parent_mapping[dst]] += 1
    for src, root in parent_mapping.items():
        if root not in in_degrees:
            in_degrees[root] = 0
    return in_degrees


def get_first_component_nodes(graph):
    parent_mapping = get_strongly_connected_components(graph)
    in_degrees = get_component_in_degrees(graph, parent_mapping)
    first_component_root = None
    for root, indegree in in_degrees.items():
        if indegree == 0:
            assert first_component_root is None
            first_component_root = root
    nodes = []
    for node, root in parent_mapping.items():
        if root == first_component_root:
            nodes.append(node)
    return nodes


def main():
    graph = GraphCore(False)
    num_vertices = 4
    edges_input = []
    edges_input.append((1, 2))
    edges_input.append((3, 2))
    edges_input.append((4, 3))
    edges_input.append((2, 1))
    for edge in edges_input:
        # Reverse edges.
        graph.add_edge(edge[1], edge[0])
    for vert in range(num_vertices):
        graph.add_vertex(vert + 1)
    ans = get_first_component_nodes(graph)
    print(ans)


main()

