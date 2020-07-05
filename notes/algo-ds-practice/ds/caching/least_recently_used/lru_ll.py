from ds.linked_list.linked_list import LinkedList


class LRUCache:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.ll = LinkedList()
        self.values = {}
        self.ll_mapping = {}

    def _move_to_end(self, key):
        old_node = self.ll_mapping[key]
        self.ll.delete_by_node(old_node)
        new_node = self.ll.insert_at_tail(key)
        self.ll_mapping[key] = new_node

    def _pop_from_front(self):
        oldest_node = self.ll.delete_at_head()
        key_deleted = oldest_node.value
        del self.values[key_deleted]
        del self.ll_mapping[key_deleted]

    def put(self, key, value):
        if key not in self.values:
            new_node = self.ll.insert_at_tail(key)
            self.ll_mapping[key] = new_node
            self.values[key] = value
            if len(self.values) > self.maxsize:
                self._pop_from_front()
        else:
            self._move_to_end(key)
            self.values[key] = value

    def get(self, key):
        if key not in self.values:
            return -1
        self._move_to_end(key)
        return self.values[key]

    def __repr__(self):
        return f"{self.values}\n{self.ll_mapping}\n{self.ll}"


def main():
    lru = LRUCache(2)
    lru.put(2, 1)
    lru.put(1, 1)
    lru.put(2, 3)
    lru.put(4, 1)
    print(lru.get(1))
    print(lru.get(2))


main()
