"""
https://leetcode.com/problems/russian-doll-envelopes/

You have a number of envelopes with widths and heights given as a pair of integers (w, h).
One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

SOLUTIONS:

Solution 1:
Just sort the boxes wrt (width, height) and then apply LIS O(n*n).

Solution 2:
Sort the boxes wrt (width asc, height desc), and then apply LIS O(n*logn) on just the heights.
It is crucial to sort this way since 'strictly greater'!!
If it was not strictly greater, then we would have sorted it in the regular way.

Solution 3:
Convert the input into a DAG and find the longest path.
Complexity -> O(V+E), where E can go upto N*N.
Therefore, it is as slow as solution 1 in worst case.
"""
from problems.dp.longest_increasing_subsequence import (
    longest_increasing_subsequence as lis,
)


def max_envelopes_slow(envelopes):
    envelopes.sort(reverse=True)
    dp = [1 for i in range(len(envelopes))]
    ans = dp[0]
    for i in range(1, len(envelopes)):
        for j in range(0, i):
            if envelopes[j][0] > envelopes[i][0] and envelopes[j][1] > envelopes[i][1]:
                dp[i] = max(dp[i], dp[j] + 1)
        ans = max(ans, dp[i])
    return ans


def max_envelopes_fast(envelopes):
    if not envelopes:
        return 0
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    heights = [envelope[1] for envelope in envelopes]
    return lis(heights)


def main():
    envelopes = []
    envelopes.append((5, 5))
    envelopes.append((5, 4))
    envelopes.append((6, 5))
    ans = max_envelopes_fast(envelopes)
    print(ans)


main()
