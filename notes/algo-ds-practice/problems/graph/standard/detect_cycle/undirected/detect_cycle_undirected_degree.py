from ds.graph.graph_core import GraphCore
from collections import deque


def get_cycle_nodes(graph: GraphCore):
    '''
    1. Append all the vertices whose degree is 1 to a queue.
    2. Pop the queue front and mark it visited.
    3. Then decrement neighbours degree by 1. If it becomes 1, add neigh to queue.
    4. Repeat 2-3.
    5. Whichever nodes are not visited, they are in the cycle.
    '''
    degrees = {}
    que = deque()
    for src in graph.vertices:
        edges = graph.get_edges(src)
        degrees[src] = len(edges.keys())
        if degrees[src] == 1:
            que.append(src)

    visited = set()
    while que:
        front = que.popleft()
        assert (front not in visited)
        visited.add(front)
        neighbours = graph.get_edges(front).keys()
        for neigh in neighbours:
            degrees[neigh] -= 1
            if degrees[neigh] == 1:
                que.append(neigh)
    return graph.vertices - visited


def main():
    graph = GraphCore(True)
    graph.add_edge(0, 1)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 2)
    print(graph)
    ans = get_cycle_nodes(graph)
    print(ans)


if __name__ == "__main__":
    main()
