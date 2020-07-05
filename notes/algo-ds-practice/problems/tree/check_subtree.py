from ds.tree.binary_tree import BinaryTreeNode as Node
from ds.tree.tree_core import Tree


def serialize_tree(root: Node, arr):
    if root is None:
        arr.append(' #')
        return
    # CAREFUL: The space is important!
    # So that ' 2 # #' is not marked as subtree of ' 12 # #'
    arr.append(' ' + str(root.data))
    serialize_tree(root.left, arr)
    serialize_tree(root.right, arr)


def is_subtree(big: Node, small: Node) -> bool:
    big_serialization = []
    serialize_tree(big, big_serialization)
    small_serialization = []
    serialize_tree(small, small_serialization)
    big_serialization = ''.join(big_serialization)
    small_serialization = ''.join(small_serialization)
    return small_serialization in big_serialization


def main():
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.right = Node(101)
    root.right.left.left = Node(102)

    print(Tree(root))
    root2 = root.left.left
    ans = is_subtree(root, root2)
    print(ans)


main()
