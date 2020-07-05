'''
Give a sorted matrix, search for an element.

EXAMPLE:

Input : mat[4][4] = { {10, 20, 30, 40},
                      {15, 25, 35, 45},
                      {27, 29, 37, 48},
                      {32, 33, 39, 50}};
              x = 29
Output : Found at (2, 1)


SOLUTION:
We can do a binary search in every row one at a time.
Complexity -> O(nlogm)

SOLUTION 2:

Better solution would be to start from the top right cell and either move left or down based on whether
the search element is greater or smaller than the current element.
Complexity -> O(n+m)

Note that we can also start from the bottom left element.
But not from top left or bottom right.

SOLUTION 3:

We can use divide and conquer similar to binary search:

Start with the middle element (n/2, n/2).
If needle > current
=> We can ignore the top left submatrix.
Meaning we can recursively call the search on rest of the 3 remaining submatrices.

Similarly if needle < current
We can ignore bottom right submatrix.

At each step we are reducing search space by 1/4th.
The base can be a submatrix which has size <= 2*2.

Complexity -> (n^1.6)
Note that the complexity is not O(log(nm))!
Its even worse than O(n).

'''
