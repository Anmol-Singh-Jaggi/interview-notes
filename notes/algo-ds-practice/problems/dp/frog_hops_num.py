"""
A frog jumps either 1, 2 or 3 steps to go to top. In how many ways can it reach the top.
Example:
Input:
2
1
5
Output:
1
13
"""


def ways_frog_hops(target):
    dp = [None for i in range(max(4, target + 1))]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    # Just like fibonacci
    for i in range(4, target + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[target]
