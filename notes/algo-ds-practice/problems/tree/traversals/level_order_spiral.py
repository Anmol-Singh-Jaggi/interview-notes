from ds.tree.binary_tree import BinaryTreeNode as Node
from collections import deque


def get_level_order_spiral_traversal(root: Node):
    level_spiral_traversal = []
    if root is None:
        return level_spiral_traversal
    dq = deque()
    dq.append(True)
    dq.append(root)
    while dq:
        should_reverse = dq.popleft()
        if not dq:
            break
        if should_reverse:
            level_spiral_traversal.extend(reversed(dq))
        else:
            level_spiral_traversal.extend(dq)
        row = dq
        dq = deque()
        dq.append(not should_reverse)
        for node in row:
            if node.left is not None:
                dq.append(node.left)
            if node.right is not None:
                dq.append(node.right)
    return level_spiral_traversal


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)
    level_spiral_traversal = get_level_order_spiral_traversal(root)
    level_spiral_traversal = [node.data for node in level_spiral_traversal]
    print(level_spiral_traversal)


main()
