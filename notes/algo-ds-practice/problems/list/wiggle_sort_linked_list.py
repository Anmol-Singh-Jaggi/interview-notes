'''
Given a linked list, rearrange it such that converted list should be of the form a < b > c < d > e < f .. where a, b, c.. are consecutive data node of linked list. Note that it is not allowed to swap data.

Examples:

Input:  1->2->3->4
Output: 1->3->2->4

Input:  11->15->20->5->10
Output: 11->20->5->15->10


SOLUTION:
We can do something similar to what we do for wiggle sorting an array.
The idea is to traverse the given linked list and check if current node maintains the zigzag order or not.
To check if given node maintains zigzag order or not, a variable ind is used.
If ind = 0, then the current node’s data should be less than its adjacent node’s data and if ind = 1, then current node’s data should be greater than its adjacent node’s data.
If the current node violates the zigzag order, then swap the position of both nodes.
For doing this step, maintain two pointers prev and next. prev stores previous node of current node and next stores new next node of current node.
To swap both nodes, the following steps are performed:

    Make next node of current node, the next node of previous node.
    Make the current node next node of its adjacent node.
    Make current node next = next node.
'''
