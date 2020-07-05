class ListNode:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def append_digit(self, digit):
        self.next = ListNode(digit)
        self.next.previous = self
        return self.next

    def __repr__(self):
        ret = ''
        node = self
        while node:
            ret += str(node.data) + ' -> '
            node = node.next
        ret += 'None'
        return ret


class Listt:
    def __init__(self, head=None, digits=None):
        if head is not None:
            self.head = head
        if digits is not None:
            self.head = Listt._make_list(digits)

    def __repr__(self):
        ret = ''
        node = self.head
        while node:
            ret += str(node.data) + ' -> '
            node = node.next
        ret += 'None'
        return ret

    def digits(self):
        iter_node = self.head
        digits_list = []
        while iter_node:
            digits_list.append(iter_node.data)
            iter_node = iter_node.next
        return digits_list

    @staticmethod
    def _make_list(digits_list):
        node_last = None
        node_head = None
        for digit in digits_list:
            if node_last is None:
                node_last = ListNode(digit)
                node_head = node_last
                continue
            node_last = node_last.append_digit(digit)
        return node_head

    def size(self):
        node = self.head
        num = 0
        while node:
            num += 1
            node = node.next
        return num


def add_numbers(list1, list2):
    list1_size = list1.size()
    list2_size = list2.size()
    if list1_size == list2_size:
        return _add_numbers_equal_length(list1, list2)
    else:
        if list1_size < list2_size:
            list1, list2 = list2, list1
        return _add_numbers_different_length(list1, list2)


def _add_numbers_equal_length(list1, list2):
    node, carry = _add_numbers_equal_length_recurse(list1.head, list2.head)
    if carry:
        node_new = ListNode(carry)
        node_new.next = node
        return Listt(node_new)
    return Listt(node)


def _add_numbers_equal_length_recurse(node1, node2):
    if node1 is None:
        return None, 0
    node_result, carry = _add_numbers_equal_length_recurse(
        node1.next, node2.next)
    sum_here = node1.data + node2.data + carry
    units_digit = sum_here % 10
    carry = sum_here // 10
    node_here = ListNode(units_digit)
    node_here.next = node_result
    return node_here, carry


def _add_numbers_different_length(list1, list2):
    size_diff = list1.size() - list2.size()
    list1_middle = list1.head
    for i in range(size_diff):
        list1_middle = list1_middle.next
    result_middle, carry = _add_numbers_equal_length_recurse(
        list1_middle, list2.head)
    if carry:
        result, carry = _increment_number_recurse(list1.head, list1_middle)
    else:
        result, carry = _make_copy(list1.head, list1_middle), 0
    iter = result
    while iter.next:
        iter = iter.next
    iter.next = result_middle
    if carry:
        node_new = ListNode(carry)
        node_new.next = result
        return Listt(node_new)
    return Listt(result)


def _make_copy(head, end):
    if head is None or head == end:
        return None
    copy = _make_copy(head.next, end)
    new_node = ListNode(head.data)
    new_node.next = copy
    return new_node


def _increment_number_recurse(head, node_end):
    if head is None or head == node_end:
        return None, 1
    node_result, carry = _increment_number_recurse(head.next, node_end)
    sum_here = head.data + carry
    units_digit = sum_here % 10
    carry = sum_here // 10
    node_here = ListNode(units_digit)
    node_here.next = node_result
    return node_here, carry


def main():
    list1 = Listt(digits=[9, 9, 9, 9])
    list2 = Listt(digits=[1, 1, 1, 1])
    list3 = add_numbers(list1, list2)
    print(list3)


if __name__ == "__main__":
    main()
