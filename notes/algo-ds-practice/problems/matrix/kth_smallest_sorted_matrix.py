'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.

SOLUTION:
Create a heap of first element of every row.
Then pop() the lowest one while adding new one from the same row.
Keep popping k times.
Complexity -> O(klogn)
'''
