from ds.tree.binary_tree import BinaryTreeNode


class BinaryTreeNodeCustom(BinaryTreeNode):
    def __init__(self, data):
        super().__init__(data)
        self.nextRight = None


def connect_level_nodes(root: BinaryTreeNodeCustom, root_depth, last_level_node_map):
    # We could also have used level-order traversal.
    if root is None:
        return
    last_node_level = last_level_node_map.get(root_depth, None)
    if last_node_level is not None:
        last_node_level.nextRight = root
    last_level_node_map[root_depth] = root
    root.nextRight = None
    connect_level_nodes(root.left, root_depth+1, last_level_node_map)
    connect_level_nodes(root.right, root_depth+1, last_level_node_map)


def main():
    root = BinaryTreeNodeCustom(1)
    root.left = BinaryTreeNodeCustom(2)
    root.right = BinaryTreeNodeCustom(3)
    connect_level_nodes(root, 0 , {})


main()
