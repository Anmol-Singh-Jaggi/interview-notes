class GraphCore:
    def __init__(self, bidirectional=False):
        # Graph is stored in an 'Adjacency map'.
        # adjMap[1] = {2: {'weight': 5}},
        #             {3: {'weight': 10}},....
        self.adjMap = {}
        self.bidirectional = bidirectional
        self.vertices = set()

    def add_edge(self, src, dst, edge_props=None):
        """
        Add an edge from `src` to `dst`. `edge_props` can be a int or dict().
        If int, then it is assumed to be weight, else arbitrary data;
        For example, {'weight': 5}.
        The existing edge prop will be overwritten if existing.
        """
        self.vertices.add(src)
        self.vertices.add(dst)
        # src_edges is a dict() containing all the edges from src.
        # It is of the form {2: {}, 3: {}}
        src_edges = self.adjMap.get(src, {})
        self.adjMap[src] = src_edges
        # edge is the specific edge from src to dst.
        # It is of the form {'weight': 5, 'key2': val2}
        edge = src_edges.get(dst, {})
        src_edges[dst] = edge
        if edge_props is not None:
            if not isinstance(edge_props, dict):
                edge_props = {"weight": edge_props}
            edge.update(edge_props)
        if self.bidirectional:
            edges_reverse = self.adjMap.get(dst, {})
            self.adjMap[dst] = edges_reverse
            edges_reverse[src] = edge

    def get_edges(self, src):
        return self.adjMap.get(src, {})

    def get_edge(self, src, dst):
        src_edges = self.adjMap.get(src, None)
        if src_edges is None:
            return None
        return src_edges.get(dst, None)

    def get_all_edges(self):
        return self.adjMap

    def remove_edges(self, src):
        if self.bidirectional:
            edges = self.adjMap[src]
            for neighbour in edges:
                if neighbour != src:
                    del self.adjMap[neighbour][src]
        self.adjMap[src] = {}

    def remove_edge(self, src, dst):
        del self.adjMap[src][dst]
        if self.bidirectional and src != dst:
            del self.adjMap[dst][src]

    def add_vertex(self, src):
        if src not in self.adjMap:
            self.adjMap[src] = {}
        self.vertices.add(src)

    def remove_vertex(self, src):
        self.remove_edges(src)
        if src in self.adjMap:
            del self.adjMap[src]
        self.vertices.remove(src)

    def get_transpose(self):
        '''
        Returns a new graph object with all edges reversed.
        Makes sense only for directional graphs.
        '''
        reverse_graph = GraphCore(False)
        for src, edges in self.get_all_edges().items():
            for dst, edge_props in edges.items():
                reverse_graph.add_edge(dst, src, dict(edge_props))
        for vertex in self.vertices:
            reverse_graph.add_vertex(vertex)
        return reverse_graph

    def __str__(self):
        output = ""
        for src in self.vertices:
            edges = self.adjMap.get(src, {})
            if not edges:
                output += "{};\n".format(src)
            for neighbour in edges:
                arrow = "->"
                if self.bidirectional:
                    if src > neighbour:
                        continue
                    arrow = "<->"
                edge = edges[neighbour]
                output += "{} {} {} = {};\n".format(src, arrow, neighbour, edge)
        return output


def main():
    g1 = GraphCore(True)
    g1.add_edge(1, 2)
    g1.add_edge(1, 3)
    g1.add_edge(1, 3, 10)
    g1.add_edge(1, 3, 15)
    g1.add_edge(3, 1, 3)
    g1.add_edge(3, 2, 3)
    g1.add_edge(1, 4, 15)
    g1.add_edge(1, 1)
    g1.add_edge(1, 1, 15)
    print(g1)
    g1.remove_vertex(1)
    print(g1)


if __name__ == "__main__":
    main()
