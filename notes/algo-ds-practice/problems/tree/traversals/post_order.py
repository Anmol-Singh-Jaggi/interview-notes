from ds.tree.binary_tree import BinaryTreeNode as Node


def postorder(root: Node, traversal):
    if root is None:
        return
    postorder(root.left, traversal)
    postorder(root.right, traversal)
    traversal.append(root)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)
    order = []
    postorder(root, order)
    print(order)


main()
