from ds.tree.binary_tree import BinaryTreeNode
from ds.tree.tree_core import Tree
'''
Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes from some
starting node to any node in the tree along the parent-child connections.
The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''
import math


def get_max_path(root: BinaryTreeNode):
    '''
    Returns (first, second) where
    first = Answer for root.
    second = Max path from root to any of the descendants containing root.
    '''
    if root is None:
        # CAREFUL: Note the base cases; it cant be 0, 0
        return -math.inf, -math.inf
    ans_left, ans_left_root = get_max_path(root.left)
    ans_right, ans_right_root = get_max_path(root.right)
    ans_containing_root = max(ans_left_root, ans_right_root, 0) + root.data
    ans = max(ans_containing_root, ans_left, ans_right,
              ans_left_root + ans_right_root + root.data)
    return ans, ans_containing_root


def main():
    root = BinaryTreeNode(1)

    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    print(Tree(root))
    print(get_max_path(root))


main()
