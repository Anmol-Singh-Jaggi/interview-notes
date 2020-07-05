'''
Given preorder traversal of a binary search tree, construct the BST.

For example, if the given traversal is {10, 5, 1, 7, 40, 50}, then the output should be root of following tree.
     10
   /   \
  5     40
 /  \      \
1    7      50

SOLUTION 1:
pre[0] will be the root.
We can find the closest greater element to the right of 0. let that index be 'g'.
Now root.left = foo(1, g-1)
root.right = goo(g, len - 1)

Complexity -> O(n*n)

SOLUTION 2:
We can compute the next greater element for each of the indices using the famous stack solution in O(n).
And then repeat the above algo.
Complexity -> O(n).
'''
