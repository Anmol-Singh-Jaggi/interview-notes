'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6


SOLUTION 1:
For each (i, j) compute height[i][j] which is the number of consecutive 1's up to that point from above.
Do this for every row.
Then assume that row is the base and the problem reduces to finding largest rectangle in a histogram.

Complexity -> O(n*m).

Note that this algo can be easily extended for the problem 'Larget subrectangle with all same values'.
See this - https://stackoverflow.com/questions/27779198/maximum-size-submatrix-with-same-integers
Basically for each row, rather than feeding the entire row into the histogram algorithm, we will break the row into
different histograms, one for each unique value, and then compute their area separately.
The complexity will still remain the same.
'''
