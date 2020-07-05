from ds.tree.binary_tree import BinaryTreeNode
from ds.tree.tree_core import Tree


def are_identical(root1: BinaryTreeNode, root2: BinaryTreeNode):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.data != root2.data:
        return False
    return are_identical(root1.left, root2.left) and are_identical(
        root1.right, root2.right)


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
    print(are_identical(root, root))


main()
