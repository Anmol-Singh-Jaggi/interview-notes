def merge(head_a, head_b):
    if head_b is None:
        return head_a
    if head_a is None:
        return head_b
    if head_b.data < head_a.data:
        head_a, head_b = head_b, head_a
    head_a.next = merge(head_a.next, head_b)
    return head_a


def merge_iterative(head_a, head_b):
    # A dummy node whose next value would be the head of the merged list.
    # We could have done without it too but it would have complicated the code slightly.
    pre_head = ListNode()
    tail = pre_head
    while True:
        if head_b is None:
            tail.next = head_a
            break
        if head_a is None:
            tail.next = head_b
            break
        if head_a.data < head_b.data:
            tail.next = head_a
            head_a = head_a.next
        else:
            tail.next = head_b
            head_b = head_b.next
        tail = tail.next
    return pre_head.next
