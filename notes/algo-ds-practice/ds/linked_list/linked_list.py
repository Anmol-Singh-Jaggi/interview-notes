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

    def get_size(self):
        node = self
        count = 1
        while node.next is not None:
            node = node.next
            count += 1
        return count

    def __repr__(self):
        return f"{self.value}"


def main():
    ll = LinkedList()
    ll.insert_at_tail(2)
    ll.insert_at_tail(3)
    ll.insert_at_tail(4)
    ll.insert_at_head(1)
    ll.delete_at_tail()
    ll2 = ll.make_copy()
    ll2.insert_at_tail(9)
    ll2.delete_by_value(1)
    print(ll2)
    print(ll)


if __name__ == "__main__":
    main()
