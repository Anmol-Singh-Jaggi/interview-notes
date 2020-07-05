from ds.tree.binary_tree import BinaryTreeNode


def get_bottom_view(root: BinaryTreeNode, x_pos, depth, bottom_view):
    # Can also be done using level-order.
    if root is None:
        return
    if x_pos not in bottom_view:
        bottom_view[x_pos] = (root, depth)
    else:
        prev_node, prev_depth = bottom_view[x_pos]
        if depth >= prev_depth:
            bottom_view[x_pos] = (root, depth)
    get_bottom_view(root.left, x_pos - 1, depth + 1, bottom_view)
    get_bottom_view(root.right, x_pos + 1, depth + 1, bottom_view)


def main():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    bottom_view = {}
    get_bottom_view(root, 0, 0, bottom_view)
    print(bottom_view)


main()
