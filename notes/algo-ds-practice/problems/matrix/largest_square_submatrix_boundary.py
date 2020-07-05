'''
Given a matrix, consisting of characters 'X' and 'O', find the largest square submatrix having X at all the boundary elements.

SOLUTION:

DP:
Let dp[i][j] denote the largest contiguous X 1-D array ending at matrix[i][j] in the ith row and jthe column.
Meaning that lets at dp[5][7] = (2, 5). It means that there is one X at matrix[5][6] and one at matrix[5][7] and there are 5 contiguous X's from matrix[1][7] to matrix[5][7].
Also, dp[i][j] = (0,0) for every matrix[i][j] = 'O'.

We can compute this dp recursively as follows:
dp[i][j] = (dp[i][j-1]+1, dp[i-1][j]+1)

Now to find the answer for a position (i, j),
lets say dp(i,j) = (3, 5).
Take min of these 2 numbers = min(3, 5) = 3
Now check if dp[i][j-3][0] >= 3. If it is then this is the answer.
Otherwise decrement min till 1 and perform the same algo.
Its hard to explain in writing.
See Tushar Roy's video.

Complexity -> O(n^3)

Note that this algo can extend easily for a sub rectangle instead of a subsquare.
'''
