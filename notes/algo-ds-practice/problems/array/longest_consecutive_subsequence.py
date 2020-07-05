"""
Given an array of integers, find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.
Examples:

Input: arr[] = {1, 9, 3, 10, 4, 20, 2}
Output: 4
The subsequence 1, 3, 4, 2 is the longest subsequence
of consecutive elements

Input: arr[] = {36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42}
Output: 5
The subsequence 36, 35, 33, 34, 32 is the longest subsequence
of consecutive elements.

Solution 1: DP (just try to find all the subsequence start positions)
Solution 2: Disjoint set (For every x, include x, x+1 and x-1 in the same group.)
"""


def ans_dp(num, hashset, cache):
    if num not in cache:
        if num not in hashset:
            cache[num] = 0
        else:
            cache[num] = ans_dp(num - 1, hashset, cache) + 1
    return cache[num]


def longest_conseq_subseq(arr):
    hashset = set()
    ans_max = 0
    cache = {}
    for elem in arr:
        hashset.add(elem)
    for elem in arr:
        ans_elem = ans_dp(elem, hashset, cache)
        ans_max = max(ans_max, ans_elem)
    return ans_max


def main():
    arr = [1, 9, 3, 10, 4, 20, 2]
    ans = longest_conseq_subseq(arr)
    print(ans)


if __name__ == "__main__":
    main()
