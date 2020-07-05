def reverse(head, k):
    current = head
    next = None
    prev = None
    count = 0

    # Reverse first k nodes of the linked list
    while current is not None and count < k:
        next = current.next
        current.next = prev
        prev = current
        current = next
        count += 1

    # next is now a pointer to (k+1)th node
    # Recursively call for the list starting from current.
    # And make rest of the list as next of first node.
    if next is not None:
        head.next = reverse(next, k)

    # prev is new head of the input list
    return prev
