"""
Given an array of distinct integers, find length of the longest subarray which contains numbers that can be arranged in a continuous sequence.
Note that [1, 3, 2] is also a valid subarray as it can be rearranged to consecutive elements [1, 2, 3].

Examples:

Input:  arr[] = {10, 12, 11};
Output: Length of the longest contiguous subarray is 3

Input:  arr[] = {14, 12, 11, 20};
Output: Length of the longest contiguous subarray is 2

Input:  arr[] = {1, 56, 58, 57, 90, 92, 94, 93, 91, 45};
Output: Length of the longest contiguous subarray is 5


Variation: Same problem as above but with duplicates allowed.


SOLUTION:

In a subarray from i to j, it has consecutive elements if `j-i == max(arr[i: j+1]) - min(arr[i: j+1])`.
So we'll generate all the n*2 subarrays and check this condition for them one-by-one.
We'll keep maintaining the max and min of the current subarray while we are generating the subarray.
So that max() and min() do not take any extra computations.
Complexity -> O(N*N)

SOLUTION to variation:
Solution is almost the same as above, just that now we'll simply ignore a subarray if it has duplicate elements.
We can check for duplicate elements using a hashset.
Complexity -> O(N*N).

ALTERNATE:

Use 2 pointer algo.
Maintain a self balaanced BST for the current window elements.
While considering a new element, just check if `arr[i] == window_max + 1` or `arr[i] == window_min - 1`.
If it is, then include it.
Else, start contracting the window from behind.
Complexity -> O(nlogn).
"""


def largest_consecutive_subarray(arr):
    ans = 0, 0
    for i in range(0, len(arr) - 1):
        subarr = [arr[i]]
        subarr_set = set(subarr)
        subarr_min = arr[i]
        subarr_max = arr[i]
        for j in range(i + 1, len(arr)):
            if arr[j] in subarr_set:
                break
            subarr_set.add(arr[j])
            subarr.append(arr[j])
            subarr_max = max(subarr_max, arr[j])
            subarr_min = min(subarr_min, arr[j])
            if subarr_max - subarr_min == j - i:
                if j - i > ans[1] - ans[0]:
                    ans = i, j
    return ans


def main():
    arr = [1, 56, 58, 57, 90, 92, 94, 93, 91, 45]
    ans = largest_consecutive_subarray(arr)
    print(ans)


main()
