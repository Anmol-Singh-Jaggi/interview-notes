'''
Given an array arr[0 … n-1] containing n positive integers, a subsequence of arr[] is called Bitonic if it is first increasing, then decreasing.
Write a function that takes an array as argument and returns the length of the longest bitonic subsequence.

Examples:

Input arr[] = {1, 11, 2, 10, 4, 5, 2, 1};
Output: 6 (A Longest Bitonic Subsequence of length 6 is 1, 2, 10, 4, 2, 1)

Input arr[] = {12, 11, 40, 5, 3, 1}
Output: 5 (A Longest Bitonic Subsequence of length 5 is 12, 11, 5, 3, 1)

Input arr[] = {80, 60, 30, 40, 20, 10}
Output: 5 (A Longest Bitonic Subsequence of length 5 is 80, 60, 30, 20, 10)


SOLUTION:

First calculate the Longest Increasing subsequence in forward direction - `lis[]`.
Then do it in reverse direction - `list_reverse()[]`.

Now, our answer is max ( lis[i] + lis_reverse[i] - 1) for every i.
Basically we can consider every i as the peak element one by one.
'''
