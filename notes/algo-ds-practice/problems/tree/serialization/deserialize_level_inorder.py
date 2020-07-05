"""
Given inorder and level-order traversals of a Binary Tree, construct the Binary Tree.

Example:
in[]    = {4, 8, 10, 12, 14, 20, 22};
level[] = {20, 8, 22, 4, 12, 10, 14};

SOLUTION:

We know that level[0] is root.
So, search for root in in[].
Now, we cannot just recurse for left and right as it will not work.
But we know that all nodes on the left of in[i] are the left children of node i and same for right.
So we can actually filter from level[1] to level[n] for all nodes in in[0] .. in[root-1].
These nodes will be a part of the left child in the correct order.
Same thing for right subtree.
Complexity:
T(N) = T(N-1) + O(N) at worst
 == O(n*n)

It looks tough at first but the concept is easy really!
This works only if all the node values are distinct.

"""
from ds.tree.binary_tree import BinaryTreeNode as Node


def deserialize_in_level(inorder, level, in_start, in_end, in_order_reverse_index):
    if in_end < in_start:
        return None
    # First node of level order is root
    root = Node(level[0])
    # Search root in inorder
    in_root_idx = in_order_reverse_index[root.data]

    # Insert all left nodes in hash table
    left_children = set()
    for i in range(in_start, in_root_idx):
        left_children.add(inorder[i])

    # Separate level order traversals of left and right.
    left_level = []
    right_level = []
    for i in range(1, len(level)):
        if level[i] in left_children:
            left_level.append(level[i])
        else:
            right_level.append(level[i])

    # Recursively build left and right subtrees and return root.
    root.left = deserialize_in_level(
        inorder, left_level, in_start, in_root_idx - 1, in_order_reverse_index
    )
    root.right = deserialize_in_level(
        inorder, right_level, in_root_idx + 1, in_end, in_order_reverse_index
    )
    return root


def main():
    inorder = [4, 8, 10, 12, 14, 20, 22]
    level = [20, 8, 22, 4, 12, 10, 14]
    in_order_reverse_index = {}
    for i in range(0, len(inorder)):
        in_order_reverse_index[inorder[i]] = i
    root = deserialize_in_level(
        inorder, level, 0, len(inorder) - 1, in_order_reverse_index
    )
    print(root.display())


main()
