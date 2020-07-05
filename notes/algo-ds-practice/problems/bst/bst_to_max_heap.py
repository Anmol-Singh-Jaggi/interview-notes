'''
Given a Binary Search Tree which is also a Complete Binary Tree.
The problem is to convert a given BST into a Special Max Heap with the condition that all the values in the left subtree of a node should be less than all the values in the right subtree of the node.
This condition is applied on all the nodes in the so converted Max Heap.

Examples:

Input :          4
               /   \
              2     6
            /  \   /  \
           1   3  5    7

Output :       7
             /   \
            3     6
          /   \  /   \
         1    2 4     5


SOLUTION:

First convert BST to sorted array.
Then arr[n-1] will be the root.
Do the same for left half and right half of the remaining array.
Note that this will return the max heap in the form of a binary tree.
To further get the heap array from it, just populate the array simply.

Pseudocode:

def to_max_heap_tree(arr, low, high){
    root = Node(high)
    root.left=  foo(arr, 0, high-low/2)
    root.right = ...
    return root
}

def to_array(root, idx){
    arr[idx] = root
    to_array(root.left, idx*2)
    to_array(root.right, idx*2 + 1)
}
'''
