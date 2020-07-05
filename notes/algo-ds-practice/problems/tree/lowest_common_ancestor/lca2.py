from ds.tree.binary_tree import BinaryTreeNode as Node
from ds.tree.tree_core import Tree


def get_lca(root, node1, node2):
    """
    If one node absent, then returns the other node.
    If both absent, then returns None.
    """
    if root is None:
        return None
    if root.val == node1.val or root.val == node2:
        return root
    left_lca = get_lca(root.left, node1, node2)
    right_lca = get_lca(root.right, node1, node2)
    if left_lca and right_lca:
        return root
    return left_lca if left_lca is not None else right_lca


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    print(Tree(root))
    print((get_lca(root, 20, 10)))


main()
