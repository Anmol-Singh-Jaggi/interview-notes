"""
Print the diagonal traversal of a tree.
"""
from ds.tree.binary_tree import BinaryTreeNode as Node


def dfs(root: Node, dist, diagonals):
    if root is None:
        return
    diagonal = diagonals.get(dist, [])
    diagonal.append(root)
    diagonals[dist] = diagonal
    # CAREFUL - We need to go to left first!
    dfs(root.left, dist + 1, diagonals)
    dfs(root.left, dist, diagonals)


def diagonal_traversal(root: Node):
    diagonals = {}
    dfs(root, 0, diagonals)
    diagonals_sorted = []
    for dist in sorted(diagonals.keys()):
        diagonals_sorted.append(diagonals[dist])
    return diagonals_sorted
