'''
Given a binary tree and a node, print all cousins of given node.
Note that siblings should not be printed.
2 nodes are cousins if they have different parents and same grandparent.

Example:

Input : root of below tree
             1
           /   \
          2     3
        /   \  /  \
       4    5  6   7
       and pointer to a node say 5.

Output : 6, 7

SOLUTION:

During the level order traversal, when for the parent node,
if parent->left == Node_to_find, or parent->right == Node_to_find,
then the children of this parent must not be pushed into the queue (as one is the node and other will be its sibling).
Push the remaining nodes at the same level in the queue and then exit the loop.
'''
