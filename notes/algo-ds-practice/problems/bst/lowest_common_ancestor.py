from ds.binary_search_tree.binary_search_tree import BinarySearchTree, BSTNode


def lowest_common_ancestor(root: BSTNode, val1, val2):
    if root is None:
        return None
    if root.data == val1 or root.data == val2:
        return root.data
    if val1 < root.data and val2 < root.data:
        return lowest_common_ancestor(root.left, val1, val2)
    if val1 > root.data and val2 > root.data:
        return lowest_common_ancestor(root.right, val1, val2)
    return root.data


def main():
    bst = BinarySearchTree(None)
    bst.insert(5)
    bst.insert(4)
    bst.insert(6)
    bst.insert(3)
    bst.insert(7)
    bst.insert(8)
    print(bst)
    ans = lowest_common_ancestor(bst.root, 3, 8)
    print(ans)


main()
