from ds.tree.binary_tree import BinaryTreeNode as Node


def morris_inorder(root: Node):
    '''
    The complexity is O(n) because we are visiting each node twice at max.
    '''
    current = root
    traversal = []
    while current is not None:
        if current.left is None:
            traversal.append(current.data)
            current = current.right
        else:
            # Find the inorder predecessor of current
            pre = current.left
            while pre.right is not None and pre.right != current:
                pre = pre.right
            # Make current as right child of its inorder predecessor
            if pre.right is None:
                pre.right = current
                current = current.left
            # Revert the changes made in if part to restore the
            # original tree i.e., fix the right child of predecessor
            # This will get executed when we are visiting a node for the second time.
            else:
                pre.right = None
                traversal.append(current.data)
                current = current.right
    return traversal


def main():
    """
    Constructed binary tree is
                1
            / \
            2	 3
        / \
        4	 5
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    ans = morris_inorder(root)
    print(ans)


main()
