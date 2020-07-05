class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_head(self, val):
        new_node = ListNode(val, next=self.head)
        if self.is_empty():
            self.tail = new_node
        else:
            self.head.prev = new_node
        self.head = new_node
        self.size += 1
        return new_node

    def insert_at_tail(self, val):
        new_node = ListNode(val, prev=self.tail)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1
        return new_node

    def search(self, val):
        current = self.head
        while current is not None and current.value != val:
            current = current.next
        return current

    def delete_at_head(self):
        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        self.size -= 1
        return temp

    def delete_at_tail(self):
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        if self.tail is None:
            self.head = None
        self.size -= 1
        return temp

    def delete_by_node(self, node_to_del):
        if node_to_del is self.head:
            self.delete_at_head()
            return
        if node_to_del is self.tail:
            self.delete_at_tail()
            return
        node_prev = node_to_del.prev
        node_next = node_to_del.next
        if node_prev is not None:
            node_prev.next = node_next
        if node_next is not None:
            node_next.prev = node_prev
        self.size -= 1

    def delete_by_value(self, val):
        val_node = self.search(val)
        if val_node is None:
            return None
        self.delete_by_node(val_node)
        return val_node

    def is_empty(self):
        return self.head is None

    @staticmethod
    def _from_list(lst):
        ll = LinkedList()
        for elem in lst:
            ll.insert_at_tail(elem)
        return ll

    def to_list(self):
        current = self.head
        lst = []
        while current is not None:
            lst.append(current.value)
            current = current.next
        return lst

    def make_copy(self):
        ll_list = self.to_list()
        return LinkedList._from_list(ll_list)

    def __repr__(self):
        self_repr = f"[{self.head} <..> {self.tail}][{self.size}] ==> "
        current = self.head
        while current is not None:
            self_repr += f"{current} -> "
            current = current.next
        self_repr += "None"
        return self_repr


class ListNode:
    def __init__(self, x, prev=None, next=None):
        self.value = x
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f"{self.value}"


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

    def exists(self, key):
        return key in self.values

    def __repr__(self):
        return f"{self.values}\n{self.ll_mapping}\n{self.ll}"


def main():
    tc = int(input())
    while tc:
        tc -= 1
        input()
        pages = [int(x) for x in '3 1 0 2 5 4 1 2'.split()]
        capacity = int(input())
        page_faults = 0
        lru = LRUCache(capacity)
        for page in pages:
            if not lru.exists(page):
                page_faults += 1
                lru.put(page, None)
        print(page_faults)


main()
