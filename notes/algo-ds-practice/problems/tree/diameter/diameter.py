from ds.tree.binary_tree import BinaryTreeNode
from ds.tree.tree_core import Tree


def get_diameter(root: BinaryTreeNode):
    if root is None:
        return 0, 0
    left_diameter, left_height = get_diameter(root.left)
    right_diameter, right_height = get_diameter(root.right)
    diameter_root = left_height + right_height + 1
    height_root = max(left_height, right_height) + 1
    diameter_max = max(left_diameter, right_diameter, diameter_root)
    return diameter_max, height_root


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
    print(get_diameter(root))


main()
