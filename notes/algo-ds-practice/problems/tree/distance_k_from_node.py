'''
Given a binary tree, a target node in the binary tree, and an integer value k, print all the nodes that are at distance k from the given target node. No parent pointers are available.

SOLUTION:

Lets see we have a function `printAtKDownwards(root, k)` which can print all the nodes at a distance k from a node in downwards direction.
We can use it as follows:

1. Print all the nodes at k distance from down the target node by calling `printAtKDownwards(target, k)`.
2. Now we need to print every node at distance k which is not in its subtree.
For that, we can recursively call `printAtKDownwards(ancestor.right, x)` for every ancestor of target starting from its parent, where the value of x will decrease as the ancestor gets farther from the target.
For example, if p1 means parent and p2 means grandparent of target and so on..
And if k = 5 for example:

Then we need to call:
printAtKDownwards(p1.right, 3)
printAtKDownwards(p2.right, 2)
printAtKDownwards(p3.right, 1)
...

'''
