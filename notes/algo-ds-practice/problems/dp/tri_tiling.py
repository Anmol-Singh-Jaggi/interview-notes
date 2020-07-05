"""
Given a 3 x n board, find the number of ways to fill it with 2 x 1 dominoes.
See https://www.geeksforgeeks.org/tiling-with-dominoes/ for explanation.

SOLUTION:

Recurrence relation:
f(n) = f(n-2) + 2*g(n-1)
g(n) = f(n-1) + g(n-2)
"""


def tri_tiling_ways(n):
    F = [0] * (n + 1)
    G = [0] * (n + 1)
    F[0] = 1
    F[1] = 0
    G[0] = 0
    G[1] = 1
    for i in range(2, n + 1):
        F[i] = F[i - 2] + 2 * G[i - 1]
        G[i] = F[i - 1] + G[i - 2]
    return F[n]


def main():
    ans = tri_tiling_ways(7)
    print(ans)


main()
