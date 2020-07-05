"""
Given a rope of length n meters, cut the rope in different parts of integer lengths in a way that maximizes product of lengths of all parts.
You must make at least one cut. Assume that the length of rope is more than 2 meters.

Examples:

Input: n = 2
Output: 1 (Maximum obtainable product is 1*1)

Input: n = 3
Output: 2 (Maximum obtainable product is 1*2)

Input: n = 4
Output: 4 (Maximum obtainable product is 2*2)

Input: n = 5
Output: 6 (Maximum obtainable product is 2*3)

Input: n = 10
Output: 36 (Maximum obtainable product is 3*3*4)
"""
from functools import lru_cache


@lru_cache(maxsize=None)
def max_rod_product(size):
    '''
    O(n*n)
    '''
    if size < 2:
        return 0
    ans = 0
    for i in range(1, size):
        # CAREFUL: Tricky!
        ans = max(ans, i * (size - i), i * max_rod_product(size - i))
    return ans


def main():
    size = 10
    ans = max_rod_product(size)
    print(ans)


main()
