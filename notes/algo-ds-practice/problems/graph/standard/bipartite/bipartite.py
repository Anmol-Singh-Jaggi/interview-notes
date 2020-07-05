from queue import Queue
from ds.graph.graph_core import GraphCore


def is_bipartite(graph):
    graph_vertices = graph.vertices
    visited = set()
    vertex_color = {}
    for src in graph_vertices:
        if src in visited:
            continue
        bfs_queue = Queue()
        bfs_queue.put(src)
        visited.add(src)
        vertex_color[src] = True
        while not bfs_queue.empty():
            current = bfs_queue.get()
            current_edges = graph.get_edges(current)
            for neighbour in current_edges:
                if neighbour not in visited:
                    bfs_queue.put(neighbour)
                    vertex_color[neighbour] = not vertex_color[src]
                    visited.add(neighbour)
                else:
                    if vertex_color[src] == vertex_color[neighbour]:
                        return False
    return True


def main():
    graph = GraphCore(True)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    print(graph)
    is_it_really = is_bipartite(graph)
    print(is_it_really)


if __name__ == "__main__":
    main()
