'''
Given a graph where every edge has weight as either 0 or 1.
Find the shortest path from source vertex to every other vertex.

SOLUTION:

We will use Dijkstra.
Just that instead of a heap, we can simply use a dequeu.
While exploring the neighbours, we will appendLeft all the zero weighted neighbours and appendRight all the one weighted neighbours.
In this way, the nearest vertices will be processed first just like in Dijkstra.
'''
