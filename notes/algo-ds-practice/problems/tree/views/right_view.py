from ds.tree.binary_tree import BinaryTreeNode as Node


def get_right_view(root: Node, root_depth, right_view):
    if root is None:
        return
    if root_depth == len(right_view):
        right_view.append(root)
    get_right_view(root.right, root_depth + 1, right_view)
    get_right_view(root.left, root_depth + 1, right_view)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    right_view = []
    get_right_view(root, 0, right_view)
    print(right_view)


main()
