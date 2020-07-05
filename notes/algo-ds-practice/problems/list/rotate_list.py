"""
Given a singly linked list, rotate the linked list counter-clockwise by k nodes.
Where k is a given positive integer.
For example, if the given linked list is 10->20->30->40->50->60 and k is 4,
the list should be modified to 50->60->10->20->30->40.
Assume that k is smaller than the count of nodes in linked list.

SOLUTION:

To rotate the linked list, we need to change next of kth node to NULL,
next of the last node to the previous head node, and finally, change head to (k+1)th node.
So we need to get hold of three nodes: kth node, (k+1)th node and last node.
Traverse the list from the beginning and stop at kth node.
Store pointer to kth node. We can get (k+1)th node using kthNode->next.
Keep traversing till the end and store pointer to last node also.
Finally, change pointers as stated above.
"""
