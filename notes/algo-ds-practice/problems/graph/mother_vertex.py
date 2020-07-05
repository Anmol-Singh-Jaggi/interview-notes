'''
What is a Mother Vertex?
A mother vertex in a graph G = (V,E) is a vertex v such that all other vertices in G can be reached by a path from v.

How to find mother vertex?

    Case 1:- Undirected Connected Graph : In this case, all the vertices are mother vertices as we can reach to all the other nodes in the graph.
    Case 2:- Undirected/Directed Disconnected Graph : In this case, there is no mother vertices as we cannot reach to all the other nodes in the graph.
    Case 3:- Directed Connected Graph : In this case, we have to find a vertex -v in the graph such that we can reach to all the other nodes in the graph through a directed path.

SOLUTION:

If there exist mother vertex (or vertices), then one of the mother vertices is the last finished vertex in DFS. (Or a mother vertex has the maximum finish time in DFS traversal).

A vertex is said to be finished in DFS if a recursive call for its DFS is over, i.e., all descendants of the vertex have been visited.

Algorithm :

    Do DFS traversal of the given graph. While doing traversal keep track of last finished vertex ‘v’. This step takes O(V+E) time.
    If there exist mother vertex (or vetices), then v must be one (or one of them). Check if v is a mother vertex by doing DFS/BFS from v. This step also takes O(V+E) time.

Note that there is no need to literally store the finish time for each vertex.
We can just do:

...
...
if node not in visited:
    dfs(node)
    latest = node
...
...

# Check if latest is indeed a mother vertex.
'''
