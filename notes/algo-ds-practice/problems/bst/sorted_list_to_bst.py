'''
Given a sorted linked list, convert it into a BST.

SOLUTION 1:

Just like in the case of array, find middle element and make it as root.
Then recurse for left and right halves.
Complexity -> O(nlogn)

SOLUTION 2:
Rather than finding the middle element again and again, we can always maintain it properly.
For doing that, in each recursive call, we will make sure that the global variable head is
always pointing to the node next to the tail node of the list.
Complexity -> O(n)


'''
from ds.linked_list.linked_list import LinkedList
from ds.tree.binary_tree import BinaryTreeNode


head = None


def recurse(left, right):
    global head
    if left > right:
        return None
    mid = (left + right) // 2
    left_root = recurse(left, mid - 1)
    node = BinaryTreeNode(head.value)
    node.left = left_root
    # Maintain the invariant
    head = head.next
    node.right = recurse(mid + 1, right)
    return node


def sorted_list_to_bst(ll):
    size = ll.size
    global head
    head = ll.head
    return recurse(0, size-1)


def main():
    ll = LinkedList()
    ll.insert_at_tail(2)
    ll.insert_at_tail(3)
    ll.insert_at_tail(4)
    ll.insert_at_head(1)
    print(ll)
    root = sorted_list_to_bst(ll)
    print(root.display())


main()
