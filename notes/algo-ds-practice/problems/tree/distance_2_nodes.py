'''
Find the distance between two keys in a binary tree, no parent pointers are given.
Distance between two nodes is the minimum number of edges to be traversed to reach one node from other.

SOLUTION:

Following is the formula.
Dist(n1, n2) = Dist(root, n1) + Dist(root, n2) - 2*Dist(root, lca)
'''
