'''
https://www.hackerrank.com/challenges/even-tree/problem

'''


class Graph:
    def __init__(self):
        self.edges = {}

    def add_vertex(self, src):
        if src not in self.edges:
            self.edges[src] = set()

    def add_edge(self, src, dst):
        self.add_vertex(src)
        self.add_vertex(dst)
        self.edges[src].add(dst)
        self.edges[dst].add(src)

    def get_neighbours(self, src):
        return self.edges[src]


def get_max_edge_cuts(graph: Graph, root, parent):
    neighbours = graph.get_neighbours(root)
    size = 1
    ans = 0
    for neigh in neighbours:
        if neigh == parent:
            continue
        ans_subtree, size_subtree = get_max_edge_cuts(graph, neigh, root)
        size += size_subtree
        ans += ans_subtree
        if size_subtree % 2 == 0:
            size -= size_subtree
            ans += 1
    return ans, size


def evenForest(num_nodes, t_edges, t_from, t_to):
    graph = Graph()
    for i in range(t_edges):
        graph.add_edge(t_from[i], t_to[i])
    ans = get_max_edge_cuts(graph, 1, None)
    return ans[0]
