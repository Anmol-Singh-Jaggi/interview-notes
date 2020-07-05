"""
Given an array of integers where each element represents the max number of steps that
can be made forward from that element.
The task is to find the minimum number of jumps to reach the end of the array (starting from the first element).
If an element is 0, then cannot move through that element.

Example:
Input:
2
11
1 3 5 8 9 2 6 7 6 8 9
6
1 4 3 2 6 7
Output:
3
2

Explanation:
Testcase 1: First jump from 1st element, and we jump to 2nd element with value 3.
Now, from here we jump to 5h element with value 9. and from here we will jump to last.
"""
import math
import sys


def min_steps(arr, idx, cache):
    # Complexity -> O(n*max), where max = max value of any element.
    # Will give TLE on geeks.
    # See the other solution for O(n).
    if idx in cache:
        return cache[idx]
    if idx == len(arr) - 1:
        ans = 0
        cache[idx] = 0
        return ans
    ans = math.inf
    for i in range(1, min(arr[idx] + 1, len(arr))):
        if idx + i < len(arr):
            ans = min(ans, 1 + min_steps(arr, idx + i, cache))
    cache[idx] = ans
    return ans


def main():
    sys.setrecursionlimit(1000000000)
    arr = [int(x) for x in "1 4 3 2 6 7".split()]
    ans = min_steps(arr, 0, {})
    print(ans)


main()
