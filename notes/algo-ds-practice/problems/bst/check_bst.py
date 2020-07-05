from ds.tree.binary_tree import BinaryTreeNode
from ds.tree.tree_core import Tree
from functools import lru_cache
import math


@lru_cache(maxsize=None)
def get_max(root):
    if root.right is not None:
        return get_max(root.right)
    return root.data


@lru_cache(maxsize=None)
def get_min(root):
    if root.left is not None:
        return get_min(root.left)
    return root.data


def isBST(root):
    '''
    Note that we cannot just simply check if
    root.data > left.data and root.data < right.data
    We must check if root.data > max(left) and root.data < min(right).
    Example:
    |+++20
        |+++10
            |+++5
                |+++1
                    |---50
    '''
    if root is None:
        return True
    if root.left is not None:
        left_max = get_max(root.left)
        if left_max > root.data:
            return False
    if root.right is not None:
        right_min = get_min(root.right)
        if right_min < root.data:
            return False
    return isBST(root.left) and isBST(root.right)


def isBST_direct(root):
    if root is None:
        return True, math.inf, -math.inf
    left_bst, left_min, left_max = isBST_direct(root.left)
    right_bst, right_min, right_max = isBST_direct(root.right)
    if not left_bst or not right_bst:
        return False, None, None
    if left_max > root.data or right_min < root.data:
        return False, None, None
    return True, min(left_min, right_min, root.data), max(
        left_max, right_max, root.data)


def main():
    root = BinaryTreeNode(20)
    root.left = BinaryTreeNode(10)
    root.left.left = BinaryTreeNode(5)
    root.left.left.left = BinaryTreeNode(1)
    root.left.left.left.right = BinaryTreeNode(50)
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(3)
    root.right = BinaryTreeNode(2)
    print(Tree(root))
    print(isBST_direct(root))


main()
