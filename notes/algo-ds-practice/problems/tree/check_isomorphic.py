"""
Write a function to detect if two trees are isomorphic.
Two trees are called isomorphic if one of them can be obtained from other by a series of flips, i.e. by swapping left and right children of a number of nodes.
Any number of nodes at any level can have their children swapped.
Two empty trees are isomorphic.

See example here:
https://www.geeksforgeeks.org/tree-isomorphism-problem/

SOLUTION:

There are following two conditions for subtrees rooted with n1 and n2 to be isomorphic.
1) Data of n1 and n2 is same.
2) One of the following two is true for children of n1 and n2
  a) Left child of n1 is isomorphic to left child of n2 and right child of n1 is isomorphic to right child of n2.
  b) Left child of n1 is isomorphic to right child of n2 and right child of n1 is isomorphic to left child of n2.
"""

from ds.tree.binary_tree import BinaryTreeNode
from ds.tree.tree_core import Tree


def are_isomorphic(root1: BinaryTreeNode, root2: BinaryTreeNode):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.data != root2.data:
        return False
    possibility1 = are_isomorphic(root1.left, root2.left) and are_isomorphic(
        root1.right, root2.right
    )
    if possibility1:
        return True
    return are_isomorphic(root1.left, root2.right) and are_isomorphic(
        root1.right, root2.left
    )


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
    print(are_isomorphic(root, root))


main()
