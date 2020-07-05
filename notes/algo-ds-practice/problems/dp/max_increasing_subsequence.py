"""
Given an array A of N positive integers.
Find the sum of maximum sum increasing subsequence of the given array.

Example:
Input:
2
7
1 101 2 3 100 4 5
4
10 5 4 3

Output:
106
10

Explanation:
Testcase 1:
All the increasing subsequences are : (1,101); (1,2,3,100); (1,2,3,4,5).
Out of these (1, 2, 3, 100) has maximum sum,i.e., 106.

SOLUTION:

Very similar to LIS.
"""


def max_increasing_subsequence(arr):
    dp = [arr[i] for i in range(len(arr))]
    ans = dp[0]
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[j] <= arr[i]:
                dp[i] = max(dp[i], arr[i] + dp[j])
        ans = max(ans, dp[i])
    return ans


def main():
    arr = [int(x) for x in "10 5 4 3".split()]
    ans = max_increasing_subsequence(arr)
    print(ans)


main()
