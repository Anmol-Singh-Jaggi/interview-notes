import math
from ds.heap.heap_printer import HeapPrinter


class Heap:
    def __init__(self, elements=None, heapify=True, is_min_heap=True):
        # Stores the current indices of the elements.
        # Is a hashmap between <entry> and <set of indices for that entry>.
        self.indices = {}
        self.is_min_heap = is_min_heap
        self.data = []
        if elements:
            self.data = [elem for elem in elements]
            for idx, elem in enumerate(self.data):
                indices_set = self.indices.get(elem, set())
                indices_set.add(idx)
                self.indices[elem] = indices_set
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
        if self.data[idx1] == self.data[idx2]:
            return
        self.data[idx1], self.data[idx2] = self.data[idx2], self.data[idx1]
        self.indices[self.data[idx1]].remove(idx2)
        self.indices[self.data[idx1]].add(idx1)
        self.indices[self.data[idx2]].remove(idx1)
        self.indices[self.data[idx2]].add(idx2)

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
            if lchild < self.size() and self._compare_elements(lchild, min_idx, False):
                min_idx = lchild
            if rchild < self.size() and self._compare_elements(rchild, min_idx, False):
                min_idx = rchild
            if min_idx == index:
                break
            self._swap_elements(index, min_idx)
            index = min_idx

    def _heapify(self):
        # CAREFUL: We use `sift_down()` here!
        # If we use `sift_up` complexity will become O(nlogn).
        # We use `sift_up()` for `push()` and `remove()`.
        # For `heapify()` and `pop()`, we use `sift_down()`.
        for idx in range(self.size() - 1, -1, -1):
            self._sift_down(idx)

    def size(self):
        return len(self.data)

    def displayTree(self):
        printer = HeapPrinter(self)
        printer.print()

    def top(self):
        if self.size():
            return self.data[0]
        raise IndexError()

    def pop(self):
        top = self.top()
        # Bring the last element to the top
        num_elements = self.size()
        self._swap_elements(0, num_elements - 1)
        # Delete the last element
        self.indices[self.data.pop()].remove(num_elements - 1)
        # Sift it downwards
        self._sift_down(0)
        return top

    def push(self, key):
        index = self.size()
        self.data.append(key)
        indices_set = self.indices.get(key, set())
        indices_set.add(index)
        self.indices[key] = indices_set
        self._sift_up(index)

    def replace(self, key, new_key):
        # If new_key < key, then sift-up, else sift-down
        # TODO: Implement!
        pass

    def remove(self, elem):
        """
        Removes all occurences of elem!
        """
        sentinel = -math.inf
        if not self.is_min_heap:
            sentinel = math.inf
        while self.indices[elem]:
            index = next(iter(self.indices[elem]))
            # Modify the value at index to inf, sift_up() on it so that it comes on top and then pop().
            self.indices[self.data[index]].remove(index)
            self.data[index] = sentinel
            indices_set = self.indices.get(sentinel, set())
            indices_set.add(index)
            self.indices[sentinel] = indices_set
            self._sift_up(index)
            # inf would have reached the top, so call pop()
            self.pop()
        del self.indices[elem]

    def exists(self, elem):
        return elem in self.indices


def heap_sort(heap):
    heap_copy = Heap(heap.data, False, heap.is_min_heap)
    result = []
    while heap_copy.size():
        result.append(heap_copy.pop())
    if not heap.is_min_heap:
        result.reverse()
    return result


def main():
    elements = [10, 20, 30, 40, 50]
    heap = Heap(elements)
    heap.displayTree()
    heap.push(6)
    heap.push(41)
    heap.displayTree()
    heap.pop()

    heap_sorted = heap_sort(heap)
    print(heap_sorted)
    heap.displayTree()
    heap.push(7)
    heap.push(6)
    heap.push(7)
    heap.displayTree()
    heap.remove(7)
    print(heap.exists(7))
    print(heap.exists(6))
    heap.displayTree()


if __name__ == "__main__":
    main()
