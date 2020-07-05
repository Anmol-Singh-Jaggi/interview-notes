'''
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window.
Each time the sliding window moves right by one position.
Return the max number of every window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


SOLUTION:

O(n) solution:

For the window, we will maintain a deque which will contain only the 'useful' elements in the window.
This deque will always be in a decreasing order from left to right.
The first element of the deque will always contain the index of the max element of that window.
When the window shifts to the right:
1. If the leftmost element of the deque is also equal to the leftmost index of the deque, then remove that element from the deque.
2. Starting from right to left, delete all the elements from deque which are smaller than the new element.
3. The first element of the deque is the index of the max element.

If you observe, every index of the input array is added and removed from the deque exactly once.
Meaning time complexity -> O(n).
'''
