from ds.tree.binary_tree import BinaryTreeNode as Node
from ds.tree.tree_core import Tree


def get_lca(root: Node, val1, val2):
    """
    Returns (LCA, if val1 found in subtree, if val2 found in subtree).
    Note that subtree includes root itself.
    If one node absent, then returns the other node.
    If both absent, then returns None.
    """
    if root is None:
        return None, False, False
    lca_left, val1_found_left, val2_found_left = get_lca(root.left, val1, val2)
    if val1_found_left and val2_found_left:
        return lca_left, True, True
    lca_right, val1_found_right, val2_found_right = get_lca(root.right, val1, val2)
    if val1_found_right and val2_found_right:
        return lca_right, True, True
    # CAREFUL: Tricky implementation!
    lca = None
    val1_found = val1_found_left or val1_found_right or root.data == val1
    val2_found = val2_found_left or val2_found_right or root.data == val2
    if val1_found or val2_found:
        if lca_left is not None:
            lca = lca_left
        if lca_right is not None:
            lca = lca_right
    if val1_found and val2_found:
        lca = root
    return lca, val1_found, val2_found


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    print(Tree(root))
    print((get_lca(root, 20, 10)))


main()
