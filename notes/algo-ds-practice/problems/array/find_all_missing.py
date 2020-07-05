"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

SOLUTION:

Iterate over the array.
For every index i, mark arr[arr[i]-1] as -ve.
At the end, again iterate through the array; all the indices where arr[i] is +ve are the missing numbers.
For example:
In case of [4,3,2,7,8,2,3,1], after first round it will become:
[-4, -3, -2, -7, 8, 2, -3, -1]
Since arr[4] and arr[5] are still +ve, means that numbers 5 and 6 were absent.
"""


def find_all_missing(arr):
    arr = arr
    if not arr:
        return []
    for i in range(0, len(arr)):
        val = abs(arr[i])
        arr[val - 1] = -abs(arr[val - 1])
    ans = []
    print(arr)
    for i in range(0, len(arr)):
        if arr[i] > 0:
            ans.append(i + 1)
    return ans


def main():
    arr = [4, 3, 2, 7, 8, 2, 3, 1]
    ans = find_all_missing(arr)
    print(ans)


main()
