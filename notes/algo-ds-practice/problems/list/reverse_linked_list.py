from ds.linked_list.linked_list import LinkedList


def reverse_list_recurse(head):
    if head is None or head.next is None:
        return head
    reverse_head = reverse_list_recurse(head.next)
    # head.next will now be pointing to null since its the tail of the reverse now.
    head.next.next = head
    # Making this node as the tail now.
    head.next = None
    return reverse_head


def reverse_list_iterative(ll):
    prev = None
    current = ll.head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    ll.head = prev


def reverse_doubly_ll(ll):
    current = ll.head
    original_head = ll.head
    head = None
    while current is not None:
        head = current
        next = current.next
        previous = current.prev
        current.next = previous
        current.prev = next
        current = next
    ll.head = head
    ll.tail = original_head


def main():
    ll = LinkedList()
    ll.insert_at_tail(2)
    ll.insert_at_tail(3)
    ll.insert_at_tail(4)
    ll.insert_at_head(1)
    ll.insert_at_head(0)
    print(ll)
    # reverse_list(ll)
    # reverse_list_iterative(ll)
    reverse_doubly_ll(ll)
    print(ll)


if __name__ == "__main__":
    main()
