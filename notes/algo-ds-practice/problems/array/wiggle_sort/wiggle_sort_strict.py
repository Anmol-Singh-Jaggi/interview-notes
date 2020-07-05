"""
Given an unsorted array of integers, sort the array into a wave like array.
An array ‘arr[0..n-1]’ is sorted in wave form if arr[0] > arr[1] < arr[2] > arr[3] < arr[4] > …..

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].

Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

SOLUTION:

- Just put sorted numbers in array
- Put largest numbers(in reverse) in odd indexes first.
- Then put remaining numbers(in reverse) in even indexes.
- So even < odd > even.
- We are doing this in reverse to prevent duplicate numbers from being assigned adjacent indices.
- It might fail if we dont reverse, for example in [4,5,5,6].

Example nums = [1,2,...,7]      Example nums = [1,2,...,8]

Small half:  4 . 3 . 2 . 1      Small half:  4 . 3 . 2 . 1 .
Large half:  . 7 . 6 . 5 .      Large half:  . 8 . 7 . 6 . 5
--------------------------      --------------------------
Together:    4 7 3 6 2 5 1      Together:    4 8 3 7 2 6 1 5

Note that it is impossible to make it strictly wiggly if more than `len(arr)/2` elements are duplicate.
"""


def wiggle_sort_strict(nums):
    arr = sorted(nums)
    # CAREFUL: Tricky implementation.
    for i in range(1, len(nums), 2):
        nums[i] = arr.pop()
    for i in range(0, len(nums), 2):
        nums[i] = arr.pop()


def main():
    arr = [10, 90, 49, 2, 1, 5, 23]
    wiggle_sort_strict(arr)
    print(arr)


main()
