from ds.tree.binary_tree import BinaryTreeNode as Node
from collections import deque


def level_order_traversal(root: Node):
    level_traversal = []
    if root is None:
        return level_traversal
    dq = deque()
    dq.append(root)
    while dq:
        node = dq.popleft()
        level_traversal.append(node)
        if node.left is not None:
            dq.append(node.left)
        if node.right is not None:
            dq.append(node.right)
    return level_traversal


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)
    level_traversal = level_order_traversal(root)
    level_traversal = [node.data for node in level_traversal]
    print(level_traversal)


main()
