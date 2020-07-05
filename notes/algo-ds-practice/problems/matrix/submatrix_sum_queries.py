'''
Given a matrix, you will get queries to get the sum of a particular submatrix.

For example,

Input = (1, 2) to (4, 5)
Meaning (1, 2) is the top-left boundary and (4, 5) bottom-right boundary.


SOLUTION:

For an index (i, j), assuming we have answer for all top and left values, we can use DP

sum[i][j] = matrix[i][j] + sum[i-1][j] + sum[j-1][i] - sum[i-1][j-1]

Note that this sum(i, j) is actually sum from (0,0) to (i, j).

To get sum(i, j) - sum(a, b), we can do again use inclusion-exclusion principle.
'''
