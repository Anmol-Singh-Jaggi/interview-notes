"""

SOLUTION:

Boundary traversal is nothing but printing leftmost nodes, then the leaf nodes and then the rightmost nodes.
We can print the 3 separately.
The leftmost have to be printed in top-down manner.
The rightmost have to be printed in bottom-up manner.
The bottom leaf nodes have to be printed in left-to-right manner.
We also need to make sure that the lefmost and righmost leaves are not printed twice!
Also keep in mind to not print root multiple times!
"""

from ds.tree.binary_tree import BinaryTreeNode as Node


def get_leaves(root, leaves):
    if root is None:
        return
    get_leaves(root.left, leaves)
    # Print it if it is a leaf node
    if root.left is None and root.right is None:
        leaves.append(root)
    get_leaves(root.right, leaves)


def get_left_boundary_without_leaves(root, left_boundary):
    if root is None:
        return
    if root.left:
        # To ensure top down, print current node before calling for left
        left_boundary.append(root)
        get_left_boundary_without_leaves(root.left, left_boundary)
    elif root.right:
        left_boundary.append(root)
        get_left_boundary_without_leaves(root.right, left_boundary)
    else:
        # Do nothing if it is a leaf node.
        # This way we avoid duplicates in output.
        pass


def get_right_boundary_without_leaves(root, right_boundary):
    if root is None:
        return
    if root.right:
        # To ensure bottom, print current node after calling for right
        get_right_boundary_without_leaves(root.right, right_boundary)
        right_boundary.append(root)
    elif root.left:
        get_right_boundary_without_leaves(root.left, right_boundary)
        right_boundary.append(root)
    else:
        # Do nothing if it is a leaf node.
        # This way we avoid duplicates in output.
        pass


def get_boundary_traversal(root):
    traversal = []
    if root is None:
        return []
    # CAREFUL
    # Have to handle root separately
    traversal.append(root)

    left_boundary = []
    right_boundary = []
    leaves = []

    get_left_boundary_without_leaves(root.left, left_boundary)
    traversal.extend(left_boundary)

    get_leaves(root.left, leaves)
    get_leaves(root.right, leaves)
    traversal.extend(leaves)

    get_right_boundary_without_leaves(root.right, right_boundary)
    traversal.extend(right_boundary)
    return traversal


def main():
    root = Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right = Node(22)
    root.right.right = Node(25)
    boundary = get_boundary_traversal(root)
    boundary = [node.data for node in boundary]
    print(boundary)


main()
