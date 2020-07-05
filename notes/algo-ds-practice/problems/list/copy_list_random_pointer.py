'''
You are given a linked list with one pointer of each node pointing to the next node just like the usual.
Every node, however, also has a second pointer that can point to any node in the list.
Now write a program to deep copy this list.

Solution 1:

First backup all the nodes' next pointers node to another array.
next_backup = [node1, node2, node3 ... None]
Meaning next_backup[0] = node[0].next = node1.
Note that these are just references.

Now just deep-copy the original linked list, only considering the next pointers.
While copying (or after it), point
`original_0.next = copy_0`
and
`copy_0.random = original_0`

Now, while traversing the copy list, set the random pointers of copies correctly:
copy.random = copy.random.random.next

Now, traverse the original list and fix back the next pointers using the next_backup array.

Total complexity -> O(n+n+n) = O(n)
Space complexity = O(n)

SOLUTION 2:
We can also do it in space complexity O(1).
This is actually easier to understand. ;)

For every node original_i, make a copy of it just in front of it.
For example, if original_0.next = original_1, then now it will become
`original_0.next = copy_0`
`copy_0.next = original_1`

Now, set the random pointers of copies:
`copy_i.random = original_i.random.next`
We can do this because we know that the copy of a node is just after the original.
Now, fix the next pointers of all the nodes:
original_i.next = original_i.next.next
copy_i.next = copy_i.next.next

Time complexity = O(n)
Space complexity = O(1)
'''
