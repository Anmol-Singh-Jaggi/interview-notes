"""
Give a sorted matrix such that the first element of a row is greater
than the last element of the previous row, search for an element.

EXAMPLE:

Input: mat = {
{1,   3,  5,  7},
{10, 11, 16, 20},
{23, 30, 34, 50}}
K = 3
Output: Found


SOLUTION:

We will first narrow down the rows by using binary search on the middle element of each row.
At each step we will remove half of the rows from the search space based on whether matrix[mid][0] is
greater or less than needle.
At each point we check if matrix[mid] can contain the needle or not by comparing needle with matrix[mid][0]
and matrix[mid][cols-1].
It it does, then we binary search on that row and stop the algo.

Complexity -> O(logn + logm)

EXAMPLE:
Consider:    | 1  2  3  4|
x = 3, mat = | 5  6  7  8|   Middle column:
            | 9 10 11 12|    = {2, 6, 10, 14}
            |13 14 15 16|   perform binary search on them
                            since, x < 6, discard the
                            last 2 rows as 'a' will
                            not lie in them(sorted matrix)
Now, only two rows are left
            | 1  2  3  4|
x = 3, mat = | 5  6  7  8|

ALTERNATE SOLUTION:
Do a lower bound on the first column get the largest element < needle.
We can be sure that needle will be in this row only.
So we can then binary search for needle in this row.
"""


from algo.searching.binary_search.binary_search import binary_search


def search_in_sorted_matrix(matrix, needle):
    rows, cols = len(matrix), len(matrix[0])
    low, high = 0, rows - 1
    while low <= high:
        mid = (low + high) // 2
        if needle >= matrix[mid][0] and needle <= matrix[mid][cols - 1]:
            return (mid, binary_search(matrix[mid], needle))
        if needle < matrix[mid][0]:
            high = mid - 1
        else:
            low = mid + 1
    return (None, None)


def main():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    needle = 16
    ans = search_in_sorted_matrix(matrix, needle)
    print(ans)


main()
