"""
A vertex cover of an undirected graph is a subset of its vertices such that for every edge (u, v) of the graph, either ‘u’ or ‘v’ is in vertex cover. Although the name is Vertex Cover, the set covers all edges of the given graph.
For a graph, vertex cover is NP Complete.
But its not for trees.
Find the vertex cover for a tree.
For example:

Tree:
    2
  /  \
  1   3

Ans = 1 (vertex 2 only)
"""


from ds.tree.binary_tree import BinaryTreeNode as Node
from ds.tree.tree_core import Tree


def vertex_cover(root: Node):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        # Its 0 even for this case
        # CAREFUL
        return 0
    root_included = 1 + vertex_cover(root.left) + vertex_cover(root.right)
    root_excluded = 0
    if root.left is not None:
        # Definitely include left since root is not included.
        root_excluded += 1 + vertex_cover(root.left.left) + vertex_cover(root.left.right)
    if root.right is not None:
        # Definitely include right since root is not included.
        root_excluded += (
            1 + vertex_cover(root.right.left) + vertex_cover(root.right.right)
        )
    return min(root_excluded, root_included)


def main():
    root = Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right = Node(22)
    root.right.right = Node(25)
    print(Tree(root))
    ans = vertex_cover(root)
    print(ans)


main()
