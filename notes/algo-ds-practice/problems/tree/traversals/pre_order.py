from ds.tree.binary_tree import BinaryTreeNode as Node


def preorder(root: Node, traversal):
    if root is None:
        return
    traversal.append(root)
    preorder(root.left, traversal)
    preorder(root.right, traversal)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)
    order = []
    preorder(root, order)
    print(order)


main()
