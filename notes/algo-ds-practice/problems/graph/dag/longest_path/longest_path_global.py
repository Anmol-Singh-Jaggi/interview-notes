'''
How to find the globally longest path in a DAG, from any vertex to another?
1. Find topo sort.
2. For every vertex 'v' in the topo_sort, update dist[v] = max(dist[v], dist[u] + edge(u, v)).
3. max(dist) would be the globally longest path in the graph.

Complexity -> O(V+E)
Think about why it works!
'''
