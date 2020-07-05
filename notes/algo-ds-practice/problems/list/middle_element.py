def findMid(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow


'''
Method 3:
Initialize mid element as head and initialize a counter as 0.
Traverse the list from head, while traversing increment the counter and change mid to mid->next
whenever the counter is odd.
So the mid will move only half of the total length of the list.
'''
