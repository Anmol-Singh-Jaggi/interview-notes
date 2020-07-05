'''
Given a initial number x and two operations which are given below:

    Multiply number by 2.
    Subtract 1 from the number.

The task is to find out minimum number of operation required to convert number x into y using only above two operations. We can apply these operations any number of times.

Constraints:
1 <= x, y <= 10000


Example:

Input : x = 4, y = 7
Output : 2
We can transform x into y using following
two operations.
1. 4*2  = 8
2. 8-1  = 7

Input  : x = 2, y = 5
Output : 4
We can transform x into y using following
four operations.
1. 2*2  = 4
2. 4-1   = 3
3. 3*2  = 6
4. 6-1   = 5
Answer = 4
Note that other sequences of two operations
would take more operations.

SOLUTION:

Use BFS.
'''
