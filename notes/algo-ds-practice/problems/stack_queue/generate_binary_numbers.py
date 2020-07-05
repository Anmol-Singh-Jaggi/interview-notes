'''
Given a number n, write a function that generates and prints all binary numbers with decimal values from 1 to n.
Examples:

Input: n = 2
Output: 1, 10

Input: n = 5
Output: 1, 10, 11, 100, 101

SOLUTION:

We can ofcourse do it the normal way, but here is an interesting method using queues:

1) Create an empty queue of strings
2) Enqueue the first binary number “1” to queue.
3) Now run a loop for generating and printing n binary numbers.
……a) Dequeue and Print the front of queue.
……b) Append “0” at the end of front item and enqueue it.
……c) Append “1” at the end of front item and enqueue it.

Example to understand:

1
10
11
100
101
110
111
1000
1001
1010
'''
