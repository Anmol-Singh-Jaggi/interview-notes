from ds.tree.binary_tree import BinaryTreeNode as Node


def inorder(root: Node, traversal):
    if root is None:
        return
    inorder(root.left, traversal)
    traversal.append(root)
    inorder(root.right, traversal)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)
    order = []
    inorder(root, order)
    print(order)


main()
