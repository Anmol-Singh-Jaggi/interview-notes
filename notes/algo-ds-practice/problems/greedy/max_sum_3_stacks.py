'''
Given three stack of the positive numbers, the task is to find the possible equal maximum sum of the stacks with removal of top elements allowed. Stacks are represented as array, and the first index of the array represent the top element of the stack.

Examples:

Input:
  stack1[] = { 3, 10}
  stack2[] = { 4, 5 }
  stack3[] = { 2, 1 }
Output:
  0
Sum can only be equal after removing all elements from all stacks.

SOLUTION:

1. Find sum of all elements of in individual stacks.
2. If the sum of all three stacks is same, then this is the maximum sum.
   Else remove the top element of the stack having the maximum sum among three of stacks.
Repeat step 1 and step 2.
'''
