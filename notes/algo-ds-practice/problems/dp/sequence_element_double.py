"""
Given two integers m & n, find the number of possible sequences of length n such that
each of the next element is greater than or equal to twice of the previous element but less than or equal to m.

Examples :

Input : m = 10, n = 4
Output : 4
There should be n elements and value of last
element should be at-most m.
The sequences are {1, 2, 4, 8}, {1, 2, 4, 9},
                 {1, 2, 4, 10}, {1, 2, 5, 10}

Input : m = 5, n = 2
Output : 6
The sequences are {1, 2}, {1, 3}, {1, 4},
                  {1, 5}, {2, 4}, {2, 5}


SOLUTION:

As per the given condition the n-th value of the sequence can be at most m.
There can be two cases for n-th element:
 - If it is m, then the (n-1)th element is at most m/2. We recur for m/2 and n-1.
 - If it is not m, then the n-1th element is at most is m-1. We recur for (m-1) and n.
"""
from functools import lru_cache


@lru_cache(None)
def num_seqs(max_allowed, size):
    if max_allowed < size:
        return 0
    if size == 0:
        return 1
    ans1 = num_seqs(max_allowed - 1, size)
    ans2 = num_seqs(max_allowed // 2, size - 1)
    return ans1 + ans2


def main():
    max_allowed = 10
    size = 4
    ans = num_seqs(max_allowed, size)
    print(ans)


main()
