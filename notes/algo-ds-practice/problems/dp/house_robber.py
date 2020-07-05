'''
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

SOLUTION:

dp[i] = max(arr[i] + dp[i+2], dp[i+1])
'''


def ans(arr, idx, cache):
    if idx >= len(arr):
        return 0
    if idx == len(arr)-1:
        return arr[idx]
    if idx in cache:
        return cache[idx]
    ans1 = ans(arr, idx+1, cache)
    ans2 = arr[idx] + ans(arr, idx+2, cache)
    cache[idx] = max(ans1, ans2)
    return cache[idx]
