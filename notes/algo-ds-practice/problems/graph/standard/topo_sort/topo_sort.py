from queue import Queue
from ds.graph.graph_core import GraphCore


def compute_in_degrees(graph):
    in_degrees = {}
    for vertex in graph.vertices:
        in_degrees[vertex] = 0
    for vertex in graph.vertices:
        vertex_edges = graph.get_edges(vertex)
        for neigh in vertex_edges:
            in_degrees[neigh] += 1
    return in_degrees


def topo_sort(graph):
    topo_order = []
    in_degrees = compute_in_degrees(graph)
    # For lexicographic ordering, use PriorityQueue
    visit_queue = Queue()
    for vertex in in_degrees:
        if in_degrees[vertex] == 0:
            visit_queue.put(vertex)
    while not visit_queue.empty():
        current_vertex = visit_queue.get()
        topo_order.append(current_vertex)
        neighbours = graph.get_edges(current_vertex)
        for neigh in neighbours:
            in_degrees[neigh] -= 1
            if in_degrees[neigh] == 0:
                visit_queue.put(neigh)

    if len(topo_order) != len(in_degrees):
        # Found cycle
        print(topo_order)
        print(in_degrees)
        topo_order = None
    return topo_order


def main():
    graph = GraphCore()
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)
    graph.add_edge(4, 0)
    graph.add_edge(4, 1)
    graph.add_edge(5, 0)
    graph.add_edge(5, 2)
    topo_order = topo_sort(graph)
    print(topo_order)


if __name__ == "__main__":
    main()
