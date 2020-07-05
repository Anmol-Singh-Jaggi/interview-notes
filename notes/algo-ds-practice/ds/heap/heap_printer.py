from ds.tree.binary_tree import BinaryTreeNode


class HeapPrinter:
    """
    Helper class to print heap.
    It does so by first constructing a tree, and then displaying that tree.
    """

    def __init__(self, heap):
        heap_data = [(elem, idx) for (idx, elem) in enumerate(heap.data)]
        self.tree_root = self._build_tree_from_heap(heap_data)

    def _build_from_heap_recursive(self, heap_array, root_index):
        if root_index >= len(heap_array):
            return None
        root = BinaryTreeNode(heap_array[root_index])
        left_child_index = root_index * 2 + 1
        left_child = self._build_from_heap_recursive(heap_array, left_child_index)
        if left_child:
            root.set_left_child(left_child)

        right_child_index = left_child_index + 1
        right_child = self._build_from_heap_recursive(heap_array, right_child_index)
        if right_child:
            root.set_right_child(right_child)
        return root

    def _build_tree_from_heap(self, heap_array):
        return self._build_from_heap_recursive(heap_array, 0)

    def print(self):
        print(self.tree_root.display())


def main():
    hp = HeapPrinter([5, 4, 3, 2, 1])
    hp.print()


if __name__ == "__main__":
    main()
