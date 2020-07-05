'''
An eulerian path is a path visiting every edge once.
A eulerian circuit is an eulerian path ending at the starting vertex.

For undirected graph:
    Algorithm to detect eulerian path:
    1. All vertices with non-zero degree should be connnected.
    2. All vertices should have even degree except 2 vertices.
    Note that in an undirected graph, its not possible for just 1 vertex to have an odd degree, since sum of all degrees is even.

    Algorithm to detect eulerian circuit:
    1. Same as above.
    2. All vertices should have even degree without exception.

For directed graph, the net degree (in - out) should be same.
'''
