"""
You have an infinite stream of integers.
You have to return the median of the current collection of integers after every addition.

Solution:

Use 2 heaps - one min and max.<br>
Insert the incoming integer into one of the 2 heaps such that their sizes differ by atmost 1.<br>
The median will be the average of the top of the 2 heaps if the size is same, else the top of the bigger heap.

ALTERNATE SOLUTION:

Maintain a balanced BST.
The root of the BST will be the median in case of odd events.
In case of even numbers, the other node will be root.left if left substree is larger than right subtree, otherwise root.right.

"""
