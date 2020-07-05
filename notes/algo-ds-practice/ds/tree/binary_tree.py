from ds.tree.tree_core import Tree, TreeNode


class BinaryTreeNode(TreeNode):
    def __init__(self, data, left_child=None, right_child=None):
        super().__init__(data)
        if left_child is not None:
            self.left = left_child
        if right_child is not None:
            self.right = right_child

    def set_left_child(self, node):
        self.set_child(0, node)

    def set_right_child(self, node):
        self.set_child(1, node)

    def get_left_child(self):
        return self.get_child(0)

    def get_right_child(self):
        return self.get_child(1)

    def is_leaf(self):
        return self.left is None and self.right is None

    left = property(get_left_child, set_left_child)
    right = property(get_right_child, set_right_child)


def main():
    root = BinaryTreeNode(1)

    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)

    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)
    root.left.left.right = BinaryTreeNode(101)
    root.right.left.left = BinaryTreeNode(102)

    tree1 = Tree(root)

    print(tree1)
    print(tree1.size())


if __name__ == "__main__":
    main()
