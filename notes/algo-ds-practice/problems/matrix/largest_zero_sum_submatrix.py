'''
Given a matrix with +ve and -ve integers, find the largest submatrix(rectangle) with zero sum.

SOLUTION:

Naive solution would be to calculate sum for every rectangle possible.
Complexity -> O(n^4)

SOLUTION 2:
We can use the solution for the 1-D problem (using hashmaps).
For every n*n column pairs (left, right), we can make a 1-D array with the sums of all the rows from 0 to n-1
within the column (left, right).
See `max_sum_submatrix` problem for more info.
Complexity -> O(n^3)
'''
