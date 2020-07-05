'''
Given a N x N matrix, determine the maximum K such that K x K is a submatrix with all equal elements i.e., all the elements in this submatrix must be same.

EXAMPLES:
Input : a[][] = {{2, 3, 3},
                 {2, 3, 3},
                 {2, 2, 2}}
Output : 2
Explanation: A 2x2 matrix is formed from index A0,1 to A1,2

Input : a[][]  = {{9, 9, 9, 8},
                  {9, 9, 9, 6},
                  {9, 9, 9, 3},
                  {2, 2, 2, 2}
Output : 3
Explanation : A 3x3 matrix is formed from index A0,0 to A2,2

SOLUTION:

For every (i,j) we can check if this position can be used as the bottom-right corner of a square submatrix
with all equal elements.

dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
if (i,j) == (i-1,j) == (i,j-1) == (i-1,j-1)
else 1
'''


def largest_square_submatrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0 for j in range(cols)] for i in range(rows)]
    ans = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                dp[i][j] = 0
            elif i == 0 or j == 0:
                dp[i][j] = 1
            elif (
                matrix[i][j] == matrix[i - 1][j]
                and matrix[i][j] == matrix[i][j - 1]
                and matrix[i][j] == matrix[i - 1][j - 1]
            ):
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
            else:
                dp[i][j] = 1
            ans = max(ans, dp[i][j])
    return ans


def test1():
    matrix = [
        [0, 0, 3, 3, 0],
        [0, 1, 3, 3, 0],
        [1, 3, 3, 3, 0],
        [0, 0, 2, 1, 0]
    ]
    ans = largest_square_submatrix(matrix)
    print(ans)


def test2():
    matrix = [
        [0, 3, 3, 3, 0],
        [2, 3, 3, 3, 3],
        [1, 3, 3, 3, 2],
        [0, 0, 2, 1, 0]
    ]
    ans = largest_square_submatrix(matrix)
    print(ans*ans)


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
