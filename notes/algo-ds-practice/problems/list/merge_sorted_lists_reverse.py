'''
Given two linked lists sorted in increasing order. Merge them such a way that the result list is in decreasing order (reverse order).

Examples:

Input:  a: 5->10->15->40
        b: 2->3->20
Output: res: 40->20->15->10->5->3->2

Input:  a: NULL
        b: 2->3->20
Output: res: 20->3->2

You need to do it without reversing any list!

SOLUTION:

Do the same algo as merging in ascending order.
Just that while adding a new node the result list, add it to the front rather than the end.

'''
