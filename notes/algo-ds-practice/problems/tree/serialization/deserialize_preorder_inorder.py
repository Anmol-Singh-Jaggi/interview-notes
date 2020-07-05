from ds.tree.binary_tree import BinaryTreeNode as Node

# Note that the algo to deserialize using inorder and postorder is almost the same.
# Just that we start from reverse.


def build_reverse_map(arr):
    mapping = {}
    for i in range(len(arr)):
        mapping[arr[i]] = i
    deserialize.in_order_index_map = mapping


def deserialize(in_order, pre_order, in_start, in_end):
    if deserialize.in_order_index_map is None:
        build_reverse_map(in_order)
    if in_start > in_end:
        return None
    root = Node(pre_order[deserialize.pre_index])
    deserialize.pre_index += 1
    if in_start == in_end:
        return root
    root_in_index = deserialize.in_order_index_map[root.data]
    root.left = deserialize(in_order, pre_order, in_start, root_in_index - 1)
    root.right = deserialize(in_order, pre_order, root_in_index + 1, in_end)
    return root


def main():
    in_order = ["D", "B", "E", "A", "F", "C"]
    pre_order = ["A", "B", "D", "E", "C", "F"]
    deserialize.pre_index = 0
    deserialize.in_order_index_map = None
    root = deserialize(in_order, pre_order, 0, len(in_order) - 1)
    print(root.display())


main()
