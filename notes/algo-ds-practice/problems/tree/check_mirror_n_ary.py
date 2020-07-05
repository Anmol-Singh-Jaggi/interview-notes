'''
Given two n-ary trees, the task is to check if they are mirror of each other or not.
Print “Yes” if they are mirror of each other else “No”.

SOLUTION 1:
Just like we do for binary tree, check whether:
root1.children[0] == root2.children[-1]
root1.children[1] == root2.children[-2]
... so on

SOLUTION 2:
The idea is to use Queue and Stack to check if given N-ary tree are mirror of each other or not.
Let first n-ary tree be t1 and second n-ary tree is t2.
For each node in t1, make stack and push its connected node in it.
Now, for each node in t2, make queue and push its connected node in it.
Now, for each corresponding node do following:
  While stack and Queue is not empty.
  a = top element of stack;
  b = front of stack;
  if (a != b)
    return false;
  pop element from stack and queue.
'''
