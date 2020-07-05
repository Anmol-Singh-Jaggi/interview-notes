'''
Given a matrix with +ve and -ve integers, find the submatrix(rectangle) with the largest sum.

SOLUTION:

Naive solution would be to calculate sum for every rectangle possible.
Let (tl, br) denote the top left and bottom right of a rectangle.
Where tl and br themselves are coordinates.
The range of tl = (x, y) where x = (0, n) and y = (0, n)
Meaning tl can take n*n values (basically any cell can be the top left).
Similarly, br can also take n*n values.
Once we have the coordinates, we can get the sum in O(1) using precomputations.
So complexity -> O(n^4)

SOLUTION 2:
We can use the solution for the same problem for 1-d array (Kadane):
We iterate over all possible n*n column pairs (left, right).
For each pair (left, right), we can calculate the sum of every row from 0 to (n-1) in those columns.
Let this array of sums be `sumRows`. This will contain n numbers signifying sum of elements from
matrix[i][left] to matrix[i][right], i from 0 to n-1.
We can then run kadane on this array.
Let say kadane returns the pair (4, 7).
Meaning rows 4,5,6,7 have the greatest sum between (left, right) columns.
This will be our answer for (left, right) column pair.
We can do this for every n*n (left, right) pair.
Complexity -> O(n^3)
'''
