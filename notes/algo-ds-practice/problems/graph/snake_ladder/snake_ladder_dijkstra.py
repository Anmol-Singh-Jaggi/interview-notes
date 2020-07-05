from ds.graph.graph_core import GraphCore
from problems.graph.standard.dijkstra.dijkstra import dijkstra


def snake_ladder_dijkstra(shortcuts):
    """
    Assuming the snake and ladder board is of size 30.
    Create a graph such that every number 'num' has an outward edge
    going to num+1, num+2, ... num+6 of cost 1.
    Also, create a 0-cost edge for every shortcut.
    Then apply dijkstra directly.
    Total number of edges = 6*30 + num_shortcuts
    Note: We do not need to apply Dijkstra at all. See the BFS solution!!
    """
    graph = GraphCore(False)
    for src in range(1, 31):
        for i in range(1, 7):
            dst = src + i
            if dst <= 30:
                graph.add_edge(src, dst, 1)
    for src, dst in shortcuts.items():
        if dst > src:
            graph.add_edge(src, dst, 0)
    return dijkstra(graph, 1)[30]


def main():
    shortcuts = {}
    shortcuts[12] = 18
    shortcuts[3] = 19
    print(snake_ladder_dijkstra(shortcuts))


main()
