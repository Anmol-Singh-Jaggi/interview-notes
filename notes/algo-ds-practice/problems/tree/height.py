from ds.tree.binary_tree import BinaryTreeNode
from ds.tree.tree_core import Tree


def get_height(root: BinaryTreeNode):
    if root is None:
        return 0
    height_left = get_height(root.left)
    height_right = get_height(root.right)
    return max(height_left, height_right) + 1


def main():
    root = BinaryTreeNode(1)

    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)

    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)
    root.left.left.right = BinaryTreeNode(101)
    root.right.left.left = BinaryTreeNode(102)
    print(Tree(root))
    print(get_height(root))


main()
