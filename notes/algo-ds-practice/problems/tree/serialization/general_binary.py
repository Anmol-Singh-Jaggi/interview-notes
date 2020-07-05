from ds.tree.binary_tree import BinaryTreeNode as Node
from ds.tree.tree_core import Tree


def serialize_tree(root: Node, arr):
    '''
    Pre-order traversal.
    '''
    if root is None:
        arr.append(None)
        return
    arr.append(root.data)
    serialize_tree(root.left, arr)
    serialize_tree(root.right, arr)


def deserialize_tree(arr, idx=0):
    '''
    idx is the index of the current element to be processed.
    Returns <root, idx> where idx is the index of the next element to be processed.
    '''
    if idx >= len(arr) or arr[idx] is None:
        return None, idx + 1
    node = Node(arr[idx])
    node.left, idx = deserialize_tree(arr, idx + 1)
    node.right, idx = deserialize_tree(arr, idx)
    return node, idx


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
    arr = []
    serialize_tree(root, arr)
    print(arr)
    root, idx = deserialize_tree(arr)
    print(Tree(root))


main()
