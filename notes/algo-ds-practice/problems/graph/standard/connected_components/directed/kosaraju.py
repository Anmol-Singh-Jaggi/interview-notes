from ds.graph.graph_core import GraphCore


def assign_component(src, graph_reverse: GraphCore, parent_mapping, root):
    if src in parent_mapping:
        return
    parent_mapping[src] = root
    for in_neigh in graph_reverse.get_edges(src):
        assign_component(in_neigh, graph_reverse, parent_mapping, root)


def visit(src, graph: GraphCore, visited, visit_order):
    visited.add(src)
    for neigh in graph.get_edges(src):
        if neigh not in visited:
            visit(neigh, graph, visited, visit_order)
    visit_order.append(src)


def get_strongly_connected_components(graph: GraphCore):
    visit_order = []
    visited = set()
    for src in graph.vertices:
        if src not in visited:
            visit(src, graph, visited, visit_order)
    graph_reverse = graph.get_transpose()
    visit_order.reverse()
    parent_mapping = {}
    for src in visit_order:
        assign_component(src, graph_reverse, parent_mapping, src)
    return parent_mapping


def main():
    graph = GraphCore(False)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)
    graph.add_edge(5, 6)
    print(graph)
    ans = get_strongly_connected_components(graph)
    print(ans)


if __name__ == "__main__":
    main()
