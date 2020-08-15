from math import inf
from ds.heap.heap_printer import HeapPrinter


class Heap:
    def __init__(self, elements=None, heapify=True, is_min_heap=True):
        # A map of item vs its index in the heap array.
        self.indices_map = {}
        # Keep a map of item vs its frequency
        # If any item is added more than once, then we just update the frequency map
        # An item is present only once in the actual heap array.
        self.frequency_map = {}
        self.is_min_heap = is_min_heap
        self.data = []
        # Since the data array does not store duplicates, hence
        # its necessary to keep the actual number of items in a
        # separate variable.
        self.num_items = 0
        if elements:
            self.num_items = len(elements)
            for item in elements:
                if item in self.frequency_map:
                    self.frequency_map[item] += 1
                    continue
                self.frequency_map[item] = 1
                self.data.append(item)
                self.indices_map[item] = len(self.data) - 1
        if heapify:
            self._heapify()

    def _copy(self):
        heap_copy = Heap()
        heap_copy.data = list(self.data)
        heap_copy.indices_map = dict(self.indices_map)
        heap_copy.frequency_map = dict(self.frequency_map)
        heap_copy.is_min_heap = self.is_min_heap
        heap_copy.num_items = self.num_items
        return heap_copy

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
        return self.num_items

    def displayTree(self):
        printer = HeapPrinter(self)
        printer.print()

    def top(self):
        if self.num_items > 0:
            return self.data[0]
        raise IndexError()

    def pop(self):
        top = self.top()
        self.frequency_map[top] -= 1
        self.num_items -= 1
        if self.frequency_map[top] > 0:
            return top
        # Bring the element at the last of the array to the top
        num_unique_items = len(self.data)
        self._swap_elements(0, num_unique_items - 1)
        # Delete the last element
        assert(self.data.pop() == top)
        assert(self.indices_map[top] == num_unique_items - 1)
        assert(self.frequency_map[top] == 0)
        del self.indices_map[top]
        del self.frequency_map[top]
        # Sift the new heap top down to its rightful place
        self._sift_down(0)
        return top

    def push(self, item):
        self.num_items += 1
        if item in self.frequency_map:
            self.frequency_map[item] += 1
            return
        self.frequency_map[item] = 1
        index = len(self.data)
        self.data.append(item)
        self.indices_map[item] = index
        self._sift_up(index)

    def replace(self, item, new_item):
        if not self.contains(item):
            raise Exception(f'Item {item} not found!')
        if item == new_item:
            return
        # Remove and push both are O(logn)
        self.remove(item)
        self.push(new_item)

    def remove(self, item):
        if not self.contains(item):
            raise Exception(f'Item {item} not found!')
        self.frequency_map[item] -= 1
        if self.frequency_map[item] > 0:
            self.num_items -= 1
            return
        del self.frequency_map[item]
        # Modify the value at index to inf or -inf and sift it up
        # so that it comes on top, and then simply call pop().
        sentinel = -inf if self.is_min_heap else inf
        index = self.indices_map[item]
        del self.indices_map[item]
        self.frequency_map[sentinel] = 1
        self.indices_map[sentinel] = index
        self.data[index] = sentinel
        self._sift_up(index)
        assert(self.top() == sentinel)
        self.pop()

    def contains(self, item):
        return item in self.frequency_map
    
    def get_all_items(self):
        all_items = []
        for item in self.data:
            freq = self.frequency_map[item]
            all_items.extend([item]*freq)
        return all_items

    def get_all_items_sorted(self):
        heap_copy = self._copy()
        result = []
        while heap_copy.size():
            result.append(heap_copy.pop())
        if not heap_copy.is_min_heap:
            result.reverse()
        return result


def main():
    elements = [20, 30, 20, 30, 10, 40, 50]
    heap = Heap(elements)
    heap.displayTree()
    heap.remove(20)
    heap.displayTree()
    heap.push(6)
    heap.push(41)
    heap.displayTree()
    heap.pop() # Remove 6
    heap.displayTree()
    print(heap.get_all_items())
    print(heap.get_all_items_sorted())
    heap.push(7)
    heap.push(6)
    heap.push(7)
    heap.remove(41)
    print(heap.contains(7))
    print(heap.contains(41))
    print(heap.get_all_items_sorted())
    heap.displayTree()



if __name__ == "__main__":
    main()
