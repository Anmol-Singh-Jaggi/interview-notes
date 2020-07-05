from math import inf
from functools import lru_cache

matrix_dims = []


@lru_cache(maxsize=None)
def min_matrix_chain(i, j):
    '''
    Note that complexity = O(N^3), not O(N^2) !!
    '''
    global matrix_dims
    if i == j:
        return 0
    if j == i + 1:
        return matrix_dims[i][0] * matrix_dims[i][1] * matrix_dims[j][1]
    ans = inf
    for k in range(i, j):
        ans1 = min_matrix_chain(i, k)
        ans2 = min_matrix_chain(k + 1, j)
        num_ops = matrix_dims[i][0] * matrix_dims[k][1] * matrix_dims[j][1]
        ans = min(ans, ans1 + ans2 + num_ops)
    return ans


def main():
    global matrix_dims
    matrix_dims = [(10, 30), (30, 5), (5, 60)]
    ans = min_matrix_chain(0, len(matrix_dims) - 1)
    print(ans)


main()
