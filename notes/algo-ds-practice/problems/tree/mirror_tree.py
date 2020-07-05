from ds.tree.binary_tree import BinaryTreeNode
from ds.tree.tree_core import Tree


def mirror(root: BinaryTreeNode):
    if root is None:
        return
    mirror(root.left)
    mirror(root.right)
    root.left, root.right = root.right, root.left


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
    mirror(root)
    print(Tree(root))


main()
