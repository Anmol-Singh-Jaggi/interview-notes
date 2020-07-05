import math
import sys
from functools import lru_cache


@lru_cache(maxsize=None)
def min_trials(num_eggs, num_floors):
    '''
    min_trials[eggs][floor] =
    1 + max(min_trials[eggs-1][floor-1], min_trials[eggs][num_floors-floor])
    for floor = 1 .. num_floor
    That is, get the min of every floor's answer [if we start first drop from this floor].
    Where a floor's answer is max(breaks, doesn't break)
    [max() because we want the worst case].
    Complexity -> O(n*k*k)
    '''
    # CAREFUL: Note the base case!
    if num_eggs == 1 or num_floors <= 1:
        return num_floors
    ans = math.inf
    for floor in range(1, num_floors + 1):
        # Egg does not break on this floor.
        sub_ans1 = min_trials(num_eggs, num_floors - floor)
        # Egg breaks on this floor.
        sub_ans2 = min_trials(num_eggs - 1, floor - 1)
        sub_ans = 1 + max(sub_ans1, sub_ans2)
        ans = min(ans, sub_ans)
    return ans


def main():
    sys.setrecursionlimit(1000000)
    ans = min_trials(8, 16)
    print(ans)


main()
