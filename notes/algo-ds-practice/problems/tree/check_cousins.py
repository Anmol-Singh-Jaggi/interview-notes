"""
Given 2 nodes in a binary tree, tell if they are cousins or not.

SOLUTION:

2 nodes are cousins if they are at the same level but have different parents.
We can do a DFS to record the parents and depths of every node.
Complexity - O(n)
"""


def dfs(node, depth_map, parent_map, parent):
    if node is None:
        return
    depth_map[node] = 1 + depth_map.get(parent, -1)
    parent_map[node] = parent
    dfs(node.left, node)
    dfs(node.right, node)


def are_cousins(root, node1, node2):
    parent_map = {}
    depth_map = {}
    dfs(root, depth_map, parent_map, None)
    same_depth = depth_map[node1] == depth_map[node2]
    diff_parents = parent_map[node1] != parent_map[node2]
    return same_depth and diff_parents
