from ds.tree.binary_tree import BinaryTreeNode as Node
from ds.tree.tree_core import Tree


def tree_to_dll(root: Node):
    """
    Returns (head, tail) of the dll.
    First convert left subtree, then right.
    Then connect head to both of them.
    """
    if root is None:
        return None, None
    left_head, left_tail = tree_to_dll(root.left)
    right_head, right_tail = tree_to_dll(root.right)
    if left_tail is not None:
        left_tail.right = root
    root.left = left_tail
    if right_head is not None:
        right_head.left = root
    root.right = right_head
    head = left_head
    if head is None:
        head = root
    tail = right_tail
    if tail is None:
        tail = root
    return head, tail


def tree_to_dll_inorder(root: Node):
    """
    Do a reverse in-order (right, root, left).
    Keep the 'previous' node.
    Keep connecting the current node to the previous.
    The reason we are doing reverse in-order is so that
    at the end 'prev' contains the head of the list, not the tail.
    """
    prev = None

    def reverse_inorder(root: Node):
        nonlocal prev
        if root is None:
            return
        reverse_inorder(root.left)
        root.right = prev
        if prev is not None:
            prev.left = root
        prev = root
        reverse_inorder(root.right)

    reverse_inorder(root)
    return prev


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    print(Tree(root))


main()
