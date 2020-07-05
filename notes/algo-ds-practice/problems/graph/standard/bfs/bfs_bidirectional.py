from collections import deque
from ds.graph.graph_core import GraphCore


class State:
    def __init__(self, graph, src):
        self.graph = graph
        self.visited = set()
        self.bfs_queue = deque()
        self.src = src
        self.bfs_queue.append(src)
        self.visited.add(src)
        self.parent = {}
        self.other_state = None

    def bfs(self):
        current = self.bfs_queue.popleft()
        current_edges = self.graph.get_edges(current)
        for neighbour in current_edges:
            if neighbour not in self.visited:
                self.parent[neighbour] = current
                if neighbour in self.other_state.visited:
                    return neighbour
                self.bfs_queue.append(neighbour)
                self.visited.add(neighbour)
        return None


def bfs_bidirectional(graph, src, dst):
    '''
    Basically run one iteration from the src and then one iteration from destination.
    During each run, check if the visited set of both iterations has an intersection or not.
    An optimization is to always choose the iteration whose `to_visit` queue is smaller among the two,
    rather than just alternating blindly.
    Assuming every node has k friends and there are n nodes between source and destination.
    Then complexity of bidirectional BFS is O(n^(k/2) + n(^k/2)) rather than O(n^k) like in normal BFS.
    '''
    state1 = State(graph, src)
    state2 = State(graph, dst)
    state1.other_state = state2
    state2.other_state = state1
    common_node = None
    while len(state1.bfs_queue) > 0 and len(state2.bfs_queue) > 0:
        curr_state = state1
        if len(state2.bfs_queue) < len(state1.bfs_queue):
            curr_state = state2
        common_node = curr_state.bfs()
        if common_node is not None:
            break
    if common_node is None:
        return None
    path1 = []
    curr = common_node
    while True:
        curr = state1.parent.get(curr, None)
        if curr is None:
            break
        path1.append(curr)
    path2 = []
    curr = common_node
    while True:
        curr = state2.parent.get(curr, None)
        if curr is None:
            break
        path2.append(curr)
    path1.reverse()
    path1.append(common_node)
    path1.extend(path2)
    return path1


def main():
    graph = GraphCore(True)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(5, 2)
    graph.add_edge(5, 3)
    graph.add_edge(5, 4)
    print(graph)
    dist = bfs_bidirectional(graph, 1, 5)
    print(dist)


if __name__ == "__main__":
    main()
