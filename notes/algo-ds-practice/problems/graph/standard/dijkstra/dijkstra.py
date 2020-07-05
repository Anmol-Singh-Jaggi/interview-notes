import heapq
import math

from ds.graph.graph_core import GraphCore


def dijkstra(graph, src):
    '''
    Complexity = O(ElogV)
    '''
    distances = {}
    visited = set()
    for vertex in graph.vertices:
        distances[vertex] = math.inf
    distances[src] = 0
    heap = [(0, src)]
    heapq.heapify(heap)
    while heap:
        current_dist, current_vertex = heapq.heappop(heap)
        if current_vertex in visited:
            continue
        visited.add(current_vertex)
        for neigh in graph.get_edges(current_vertex):
            edge_weight = graph.get_edge(current_vertex, neigh)['weight']
            new_potential_dist = current_dist + edge_weight
            if new_potential_dist < distances[neigh]:
                distances[neigh] = new_potential_dist
                heapq.heappush(heap, (new_potential_dist, neigh))
    return distances


def main():
    graph = GraphCore()
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 1)
    graph.add_edge(1, 2, 2)
    graph.add_edge(1, 4, 3)
    graph.add_edge(2, 1, 2)
    graph.add_edge(2, 3, 2)
    graph.add_edge(3, 4, 3)
    distances = dijkstra(graph, 0)
    print(distances)


if __name__ == "__main__":
    main()
