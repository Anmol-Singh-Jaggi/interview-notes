'''
Given an array of numbers, return true if given array can represent preorder traversal of a BST.

Examples:

Input:  pre[] = {2, 4, 3}
Output: true
Given array can represent preorder traversal
of below tree
    2

      4
     /
    3

Input:  pre[] = {2, 4, 1}
Output: false
Given array cannot represent preorder traversal
of a Binary Search Tree.

Input:  pre[] = {40, 30, 35, 80, 100}
Output: true
Given array can represent preorder traversal
of below tree
     40
   /
 30    80

  35     100


Input:  pre[] = {40, 30, 35, 20, 80, 100}
Output: false
Given array cannot represent preorder traversal
of a Binary Search Tree.


SOLUTION:

1) Find the first greater value on right side of current node.
   Let the index of this node be j.
   Return true if following conditions hold.
    (i)  All values after the above found greater value are
         greater than current node.
    (ii) Recursive calls for the subarrays pre[i+1..j-1] and
         pre[j..n-1] also return true.


If we do this naively, it will be O(n*n).
But we can precompute the next greater element using a stack in O(n).
And we can compute `min_right[i]` such that it contains the min value on the right side of i.
This way it will be O(n).
'''
