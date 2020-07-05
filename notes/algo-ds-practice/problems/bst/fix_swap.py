from ds.tree.binary_tree import BinaryTreeNode as Node
from ds.tree.tree_core import Tree


def get_inorder(root: Node, traversal):
    if root is None:
        return
    get_inorder(root.left, traversal)
    traversal.append(root)
    get_inorder(root.right, traversal)


def fix_2_nodes(root: Node):
    """
    In the inorder traversal, there will be exactly 2 elements out of sorted order.
    Just find out those 2 elements, then swap the nodes' data.
    There can be 2 cases:
    1. The 2 nodes are adjacent.
    2. The 2 nodes are not adjacent.
    """
    inorder = []
    get_inorder(root, inorder)
    idx1 = None
    idx2 = None
    for i in range(1, len(inorder)):
        if inorder[i].data < inorder[i - 1].data:
            idx2 = i
            if idx1 is None:
                idx1 = i - 1
    node1 = inorder[idx1]
    node2 = inorder[idx2]
    node1.data, node2.data = node2.data, node1.data


def fix_2_nodes_direct(root: Node):
    '''
    Same thing as above but in O(1) space.
    '''
    node1, node2, prev = None, None, None

    def inorder(root: Node):
        if root is None:
            return
        nonlocal node1
        nonlocal node2
        nonlocal prev
        inorder(root.left)
        if prev:
            if root.data < prev.data:
                node2 = root
                if node1 is None:
                    node1 = prev
        prev = root
        inorder(root.right)

    inorder(root)
    node1.data, node2.data = node2.data, node1.data


def main():
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(2)
    root.left.right = Node(20)
    root.right = Node(8)
    root = Node(1)
    root.left = Node(3)
    root.right = Node(2)
    print(Tree(root))
    fix_2_nodes_direct(root)
    print(Tree(root))


main()
