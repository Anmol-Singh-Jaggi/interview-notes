from ds.tree.binary_tree import BinaryTreeNode as Node
from collections import deque


def preorder_iterative(root: Node):
    if root is None:
        return []
    stack = deque()
    stack.append(root)
    traversal = []
    while stack:
        top = stack.pop()
        traversal.append(top)
        if top.right is not None:
            traversal.append(top.right)
        if top.left is not None:
            traversal.append(top.left)
    return traversal


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)
    order = preorder_iterative(root)
    print(order)


main()
