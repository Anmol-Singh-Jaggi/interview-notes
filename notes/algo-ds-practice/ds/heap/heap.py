from ds.heap.heap_unique import HeapUnique


class Heap(HeapUnique):
    def __init__(self, elements=None, heapify=True, is_min_heap=True):
        super().__init__(elements, heapify, is_min_heap, False)
        # Keep a map of item vs its frequency
        # If any item is added more than once, then we just update the frequency map
        # An item is present only once in the actual heap array.
        self.frequency_map = {}
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

    def size(self):
        return self.num_items

    def pop(self):
        top = self.top()
        self.frequency_map[top] -= 1
        if self.frequency_map[top] > 0:
            self.num_items -= 1
            return top
        assert(self.frequency_map[top] == 0)
        del self.frequency_map[top]
        data_size = len(self.data)
        assert(super().pop() == top)
        assert(len(self.data) == data_size - 1)
        self.num_items -= 1
        return top

    def push(self, item):
        self.num_items += 1
        if item in self.frequency_map:
            self.frequency_map[item] += 1
            return
        self.frequency_map[item] = 1
        super().push(item)

    def _remove(self, index):
        item = self.data[index]
        self.frequency_map[item] -= 1
        if self.frequency_map[item] > 0:
            self.num_items -= 1
            return
        assert(self.frequency_map[item] == 0)
        del self.frequency_map[item]
        self.frequency_map[self.sentinel] = 1
        super()._remove(index)
    
    def get_all_items(self):
        all_items = []
        for item in self.data:
            freq = self.frequency_map[item]
            all_items.extend([item]*freq)
        return all_items
    
    def __str__(self):
        return super().__str__() + f' || freq_map = {self.frequency_map}'


def main():
    elements = [20, 30, 20, 30, 10, 40, 50]
    heap = Heap(elements)
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
    print(heap)
    heap.displayTree()
    heap.remove(41)
    print(heap.contains(7))
    print(heap.contains(41))
    print(heap)
    heap.displayTree()


if __name__ == "__main__":
    main()