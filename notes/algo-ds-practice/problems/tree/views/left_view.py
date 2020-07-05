from ds.tree.binary_tree import BinaryTreeNode


def get_left_view(root: BinaryTreeNode, root_depth, left_view):
    if root is None:
        return
    if root_depth == len(left_view):
        left_view.append(root)
    get_left_view(root.left, root_depth + 1, left_view)
    get_left_view(root.right, root_depth + 1, left_view)


def main():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    left_view = []
    get_left_view(root, 0, left_view)
    print(left_view)


main()
