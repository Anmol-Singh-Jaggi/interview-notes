'''
 Two ﬁnite, strictly increasing, integer sequences are given.
 Any common integer between the two sequences constitute an intersection point.
 Take for example the following two sequences where intersection points are printed in bold:

    First= 3 5 7 9 20 25 30 40 55 56 57 60 62
    Second= 1 4 7 11 14 25 44 47 55 57 100

You can ‘walk” over these two sequences in the following way:

    You may start at the beginning of any of the two sequences. Now start moving forward.
    At each intersection point, you have the choice of either continuing with the same sequence you’re currently on, or switching to the other sequence.

The objective is ﬁnding a path that produces the maximum sum of data you walked over.
In the above example, the largest possible sum is 450, which is the result of adding 3, 5, 7, 9, 20, 25, 44, 47, 55, 56, 57, 60,and 62.

SOLUTION:

Use DP:

Let arrs[0] be the first array and arrs[1] be the second.
If arrs[k][i] present at 'idx' in arrs[1-k], then
we can either jump or not jump:
ans[k][i] = max(ans[k][i+1], ans[1-k][idx+1])
else
ans[k][i] = ans[k][i+1] + arr[i]
'''

import sys


def double_helix(arrs, cache, indices, k, i):
    if i >= len(arrs[k]):
        return 0
    elem = arrs[k][i]
    if cache[k][i] is not None:
        return cache[k][i]
    ans = None
    if elem in indices[1 - k]:
        ans1 = double_helix(arrs, cache, indices, k, i + 1)
        ans2 = double_helix(arrs, cache, indices, 1 - k, indices[1 - k][elem] + 1)
        ans = max(ans1, ans2) + elem
    else:
        ans = double_helix(arrs, cache, indices, k, i + 1) + elem
    cache[k][i] = ans
    return ans


def main():
    sys.setrecursionlimit(10000000)
    arr1 = [1, 3, 4, 5]
    arr2 = [5, 6, 7, 8, 9, 10]
    arrs = [arr1, arr2]
    cache = [{}, {}]
    indices = [{}, {}]
    for i in range(len(arr1)):
        indices[0][arr1[i]] = i
        cache[0][i] = None
    for i in range(len(arr2)):
        indices[1][arr2[i]] = i
        cache[1][i] = None
    ans1 = double_helix(arrs, cache, indices, 0, 0)
    ans2 = double_helix(arrs, cache, indices, 1, 0)
    ans = max(ans1, ans2)
    print(ans)

if __name__ == "__main__":
    main()
