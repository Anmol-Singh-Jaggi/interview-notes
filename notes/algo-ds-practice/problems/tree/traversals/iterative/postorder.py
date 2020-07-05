from ds.tree.binary_tree import BinaryTreeNode as Node


def postorder_iterative(root: Node):
    if root is None:
        return []
    parent_map = {root: None}
    traversal = []
    current = root
    while current:
        if current.left is not None and current.left not in parent_map:
            parent_map[current.left] = current
            current = current.left
        elif current.right is not None and current.right not in parent_map:
            parent_map[current.right] = current
            current = current.right
        else:
            traversal.append(current)
            current = parent_map[current]
    return traversal


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)
    order = postorder_iterative(root)
    print(order)


main()
