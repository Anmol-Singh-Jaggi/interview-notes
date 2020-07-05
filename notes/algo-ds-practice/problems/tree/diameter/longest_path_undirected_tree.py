'''
Given an undirected tree, we need to find the longest path of this tree where a path is defined as a sequence of nodes.

SOLUTION:

This problem is the same as finding diameter of an N-ary tree.
We can find that either by recursion (similar to the one in binary tree).
Or we can do another algorithm:
1. From any vertex v, find the farthest vertex 'x' using BFS. (Basically we are trying to find a leaf)
2. Find the farthest vertex 'y' from 'x'. The path between x and y is the longest.
'''
