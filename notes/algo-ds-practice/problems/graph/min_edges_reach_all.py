'''
You are given a directed graph and a source node 'src'.
Find the min number of edges that are needed to be added to the graph such that all nodes in the graph are reachable from src node.

SOLUTION:

Step 1:
First of all run a DFS from src to mark all reachable nodes.

Step 2:
Then among all the unreachable nodes, choose the nodes with 0 in-degree.
Add an edge from src to each of these nodes.
Now, run DFS from these nodes and again mark them as reachable.

Step 3:
Now, if there are still remaining unreachable nodes, it means that they must be a part of a cycle.
So, find the number of cycles among these unreachable nodes by doing repeated DFS.
Add an edge from src to each of those cycles to make them reachable.
Therefore, final answer is:
Number of nodes with 0 in-degree in step 2.
+
Number of cycles in step 3.

Complexity -> O(E+V)
'''
