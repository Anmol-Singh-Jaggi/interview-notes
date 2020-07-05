from ds.tree.binary_tree import BinaryTreeNode
from ds.tree.tree_core import Tree
import math
'''
Given a binary tree in which each node element contains a number.
Find the maximum possible sum from one leaf node to another.
'''


def get_max_path_leaves(root: BinaryTreeNode):
    '''
    Returns (first, second) where
    first = Max path from root to any of its leaves.
    second = Max path from one leaf to another in subtree rooted at root.
    So second is the final answer we want.
    '''
    if root is None:
        # CAREFUL: Note the base cases; it cant be 0, 0
        return -math.inf, -math.inf
    if root.left is None and root.right is None:
        return root.data, -math.inf
    sub_ans = None
    # CAREFUL: We are handling one child null case separately.
    if root.left is None:
        sub_ans = get_max_path_leaves(root.right)
    if root.right is None:
        sub_ans = get_max_path_leaves(root.left)
    if sub_ans is not None:
        return sub_ans[0] + root.data, sub_ans[1]
    max_path_leaf_left, max_path_left = get_max_path_leaves(root.left)
    max_path_leaf_right, max_path_right = get_max_path_leaves(root.right)
    # It could be that the 2 leaves both are in the left subtree.
    ans1 = max_path_left
    # It could be that the 2 leaves both are in the right subtree.
    ans2 = max_path_right
    # Or both leaves are on either side of root; meaning root is in the max path.
    ans3 = max_path_leaf_left + max_path_leaf_right + root.data
    return max(max_path_leaf_left, max_path_leaf_right) + root.data, max(
        ans1, ans2, ans3)


def main():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root2 = BinaryTreeNode(100)
    root2.left = root
    print(Tree(root2))
    print(get_max_path_leaves(root2))


main()
