from math import inf
from copy import deepcopy
from ds.heap.heap_printer import HeapPrinter


# Can only store unique elements
class HeapUnique:
    def __init__(self, elements=None, heapify=True, is_min_heap=True, raise_exception_on_duplicate=True):
        # A map of item vs its index in the heap array.
        self.indices_map = {}
        self.is_min_heap = is_min_heap
        self.data = []
        self.sentinel = -inf if self.is_min_heap else inf
        if elements:
            for item in elements:
                if item in self.indices_map:
                    if raise_exception_on_duplicate:
                        raise Exception("Duplicate elements not allowed")
                    continue
                self.data.append(item)
                self.indices_map[item] = len(self.data) - 1
        if heapify:
            self._heapify()

    @staticmethod
    def _parent(index):
        return (index - 1) // 2

    @staticmethod
    def _left_child(index):
        return index * 2 + 1

    @staticmethod
    def _right_child(index):
        return Heap._left_child(index) + 1

    def __repr__(self):
        return "Heap: \n{}\n".format(self.data)

    def _swap_elements(self, idx1, idx2):
        self.indices_map[self.data[idx1]] = idx2
        self.indices_map[self.data[idx2]] = idx1
        self.data[idx1], self.data[idx2] = self.data[idx2], self.data[idx1]


    def _compare_elements(self, index1, index2, eq=True):
        elem1 = self.data[index1]
        elem2 = self.data[index2]
        if self.is_min_heap:
            return elem1 <= elem2 if eq else elem1 < elem2
        else:
            return elem1 >= elem2 if eq else elem1 > elem2

    def _sift_up(self, index):
        while True:
            parent = Heap._parent(index)
            if parent < 0:
                return
            if self._compare_elements(parent, index):
                return
            self._swap_elements(index, parent)
            index = parent

    def _sift_down(self, index):
        while True:
            lchild = Heap._left_child(index)
            rchild = Heap._right_child(index)
            min_idx = index
            if lchild < len(self.data) and self._compare_elements(lchild, min_idx, False):
                min_idx = lchild
            if rchild < len(self.data) and self._compare_elements(rchild, min_idx, False):
                min_idx = rchild
            if min_idx == index:
                break
            self._swap_elements(index, min_idx)
            index = min_idx

    def _heapify(self):
        # Given an array, convert it into a heap structure in O(n) time complexity.
        # CAREFUL: We use `sift_down()` here!
        # If we use `sift_up` complexity will become O(nlogn).
        # We use `sift_up()` for `push()` and `remove()`.
        # For `heapify()` and `pop()`, we use `sift_down()`.
        for idx in range(len(self.data) - 1, -1, -1):
            self._sift_down(idx)

    def size(self):
        return len(self.data)

    def displayTree(self):
        printer = HeapPrinter(self)
        printer.print()

    def top(self):
        if self.size() > 0:
            return self.data[0]
        raise IndexError()

    def pop(self):
        assert(self.size() > 0)
        top = self.top()
        # Bring the element at the last of the array to the top
        self._swap_elements(0, len(self.data) - 1)
        # Delete the last element
        assert(self.indices_map[top] == len(self.data) - 1)
        assert(self.data.pop() == top)
        del self.indices_map[top]
        # Sift the new heap top down to its rightful place
        self._sift_down(0)
        return top

    def push(self, item):
        index = len(self.data)
        self.data.append(item)
        self.indices_map[item] = index
        self._sift_up(index)

    def replace(self, item, new_item):
        if not self.contains(item):
            raise Exception(f'Item {item} not found!')
        if item == new_item:
            return
        self.remove(item)
        self.push(new_item)

    def _remove(self, index):
        item = self.data[index]
        # Modify the value at index to inf or -inf and sift it up
        # so that it comes on top, and then simply call pop().
        del self.indices_map[item]
        self.indices_map[self.sentinel] = index
        self.data[index] = self.sentinel
        self._sift_up(index)
        assert(self.top() == self.sentinel)
        self.pop()

    def remove(self, item):
        if not self.contains(item):
            raise Exception(f'Item {item} not found!')
        index = self.indices_map[item]
        assert(self.data[index] == item)
        self._remove(index)

    def contains(self, item):
        return item in self.indices_map
    
    def get_all_items(self):
        return list(self.data)

    def get_all_items_sorted(self):
        heap_copy = deepcopy(self)
        result = []
        while heap_copy.size():
            result.append(heap_copy.pop())
        if not heap_copy.is_min_heap:
            result.reverse()
        return result

    
    def __str__(self):
        return f'data = {self.data} || indices_map = {self.indices_map} || is_min_heap {self.is_min_heap} || all_items = {self.get_all_items()} || all_items_sorted = {self.get_all_items_sorted()}'


def main():
    elements = [20, 30, 10, 40, 50]
    heap = HeapUnique(elements)
    print(heap)
    heap.displayTree()
    heap.remove(20)
    heap.push(6)
    heap.push(41)
    heap.pop() # Remove 6
    print(heap)
    heap.displayTree()
    heap.push(7)
    heap.push(6)
    heap.push(7)
    heap.remove(41)
    print(heap.contains(7))
    print(heap.contains(41))
    print(heap)
    heap.displayTree()


if __name__ == "__main__":
    main()
