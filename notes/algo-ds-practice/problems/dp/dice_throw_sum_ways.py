"""
Given n dice each with m num_faces, numbered from 1 to m, find the number of ways to get sum X.
X is the summation of values on each face when all the dice are thrown.

SOLUTION:

ans(n, x) = ans(n-1, x-1) + ans(n-1, x-2) + ... ans(n-1, x-m)

Explanation:
Lets say in the first die we got 1, then no of ways = ans(n-1, x-1)
Similarly, we can get 2, 3, ... m in the first die.
Complexity -> O(m*n*x)
"""
from functools import lru_cache


num_faces = None


@lru_cache(maxsize=None)
def dice_sum_ways(num_dice, target):
    if target <= 0:
        return 0
    if num_dice == 1:
        if target > num_faces:
            return 0
        return 1
    ans = 0
    for face in range(1, num_faces + 1):
        ans += dice_sum_ways(num_dice - 1, target - face)
    return ans


def main():
    global num_faces
    num_dice = 8
    target = 25
    num_faces = 10
    ans = dice_sum_ways(num_dice, target)
    print(ans)


main()
