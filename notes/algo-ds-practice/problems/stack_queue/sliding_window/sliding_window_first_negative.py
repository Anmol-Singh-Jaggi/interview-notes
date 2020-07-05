'''
Given an array and a positive integer k, find the first negative integer for each window(contiguous subarray) of size k.
If a window does not contain a negative integer, then print 0 for that window.

Examples:

Input : arr[] = {-8, 2, 3, -6, 10}, k = 2
Output : -8 0 -6 -6
First negative integer for each window of size k
{-8, 2} = -8
{2, 3} = 0 (does not contain a negative integer)
{3, -6} = -6
{-6, 10} = -6

Input : arr[] = {12, -1, -7, 8, -15, 30, 16, 28} , k = 3
Output : -1 -1 -7 -15 -15 0

SOLUTION:

It is a variation of the problem of Sliding Window Maximum.
We create a Dequeue capacity k, that stores only useful elements of the current window of k elements.
An element is useful if it is in the current window and it is a negative integer.
We process all array elements one by one and maintain deque to contain useful elements of current window and these useful elements are all negative integers.
'''
