class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_list(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head2.val < head1.val:
        head1, head2 = head2, head1
    head1.next = merge_list(head1.next, head2)
    return head1


def get_size(head):
    curr = head
    count = 0
    while curr is not None:
        curr = curr.next
        count += 1
    return count


def partition(head):
    size = get_size(head)
    if size <= 2:
        return head, size
    curr = head
    for i in range(size//2):
        curr = curr.next
    return curr, size


def sort_list(head: ListNode) -> ListNode:
    if head is None:
        return None
    mid, size = partition(head)
    if size == 1:
        return head
    mid_next = mid.next
    mid.next = None
    head = sort_list(head)
    mid_next = sort_list(mid_next)
    head = merge_list(head, mid_next)
    return head


def print_list(head):
    while head is not None:
        print(head.val)
        head = head.next


def main():
    node1 = ListNode(4)
    node2 = ListNode(3)
    node3 = ListNode(2)
    node1.next = node2
    node2.next = node3
    ans = sort_list(node1)
    print_list(ans)


main()
