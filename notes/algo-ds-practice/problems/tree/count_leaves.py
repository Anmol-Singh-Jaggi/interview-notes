from ds.tree.binary_tree import BinaryTreeNode
from ds.tree.tree_core import Tree


def count_leaves(root: BinaryTreeNode):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    leaves_left = count_leaves(root.left)
    leaves_right = count_leaves(root.right)
    return leaves_left + leaves_right


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
    print(count_leaves(root))


main()
