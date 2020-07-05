from ds.graph.graph_core import GraphCore
from collections import deque


def is_cyclic(graph: GraphCore):
    visited = set()
    for src in graph.vertices:
        if src in visited:
            continue
        visited.add(src)
        ret = bfs(graph, src, visited)
        if ret:
            return True
    return False


def bfs(graph, src, visited):
    bfs_queue = deque()
    parent = {}
    parent[src] = -1
    bfs_queue.append(src)
    while bfs_queue:
        current = bfs_queue.popleft()
        current_edges = graph.get_edges(current)
        for neighbour in current_edges:
            if neighbour not in visited:
                bfs_queue.append(neighbour)
                visited.add(neighbour)
                parent[neighbour] = current
            elif neighbour != parent[current]:
                print(f'Back edge {current} -> {neighbour}')
                return True
    return False


def main():
    graph = GraphCore(True)
    graph.add_edge(0, 1)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 2)
    print(graph)
    ans = is_cyclic(graph)
    print(ans)


if __name__ == "__main__":
    main()
