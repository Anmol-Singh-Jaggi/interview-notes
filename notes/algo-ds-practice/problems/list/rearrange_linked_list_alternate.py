'''
Rearrange a given linked list in-place.

Given a singly linked list L0 -> L1 -> … -> Ln-1 -> Ln.
Rearrange the nodes in the list so that the new formed list is : L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 …

You are required to do this in-place without altering the nodes’ values.
Examples:

Input:  1 -> 2 -> 3 -> 4
Output: 1 -> 4 -> 2 -> 3

Input:  1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 5 -> 2 -> 4 -> 3

SOLUTION 1:
Find the middle of the linked list using tortoise hare method.
Now reverse the second half.
Now merge the 2 halves.

SOLUTION 2:
Make a deque of the linked list.
Then replace the elements by alternaingly popping from front and back.
Note that this requires O(N) space.


SOLUTION 3:
Using recursion  (O(n) space due to recursion stack.)

ListNode * reorderList(ListNode *head, int len){
    if(len == 0)
        return NULL;
    if( len == 1 )
        return head;
    if( len == 2 )
        return head->next;
    ListNode * tail = reorderList(head->next, len-2);
    ListNode * tmp = tail->next;
    tail->next = tail->next->next;
    tmp->next = head->next;
    head->next = tmp;
    return tail;
}

void reorderList(ListNode *head) {  //recursive
    ListNode  * tail = NULL;
    tail = reorderList(head, getLength(head));
}

Given a example, 1->2->3->4->5, the solution will reorder node(3), then reorder 2 and 4 to have (2->4->3), then 1 and 5 get have 1->5->2->4->3. Each call of reorderList(ListNode* head, int len) will return the last element after this reorderList() call.
'''
