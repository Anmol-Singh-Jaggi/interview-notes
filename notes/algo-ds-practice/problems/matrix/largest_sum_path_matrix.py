"""
Given a N X N  matrix Matrix[N][N] of positive integers.
There are only three possible moves from a cell Matrix[r][c].

1. Matrix[r+1][c]
2. Matrix[r+1][c-1]
3. Matrix[r+1][c+1]

Starting from any column in row 0, return the largest sum of **any** of the paths up to row N-1.
"""


def largest_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            ans1 = ans2 = ans3 = 0
            if i - 1 >= 0:
                ans1 = matrix[i - 1][j]
            if i - 1 >= 0 and j - 1 >= 0:
                ans2 = matrix[i - 1][j - 1]
            if i - 1 >= 0 and j + 1 < cols:
                ans3 = matrix[i - 1][j + 1]
            matrix[i][j] += max(ans1, ans2, ans3)
    return max(matrix[rows - 1])


def main():
    matrix = []
    matrix.append([348, 391])
    matrix.append([618, 193])
    ans = largest_sum(matrix)
    print(ans)


main()
