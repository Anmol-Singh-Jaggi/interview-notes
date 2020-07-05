"""
Given an unsorted array of integers, sort the array into a wave like array.
An array ‘arr[0..n-1]’ is sorted in wave form if arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= …..

Examples:

Input:  arr[] = {10, 5, 6, 3, 2, 20, 100, 80}
 Output: arr[] = {10, 5, 6, 2, 20, 3, 100, 80} OR
                 {20, 5, 10, 2, 80, 6, 100, 3} OR
                 any other array that is in wave form

 Input:  arr[] = {20, 10, 8, 6, 4, 2}
 Output: arr[] = {20, 8, 10, 4, 6, 2} OR
                 {10, 8, 20, 2, 6, 4} OR
                 any other array that is in wave form

 Input:  arr[] = {2, 4, 6, 8, 10, 20}
 Output: arr[] = {4, 2, 8, 6, 20, 10} OR
                 any other array that is in wave form

 Input:  arr[] = {3, 6, 5, 10, 7, 20}
 Output: arr[] = {6, 3, 10, 5, 20, 7} OR
                 any other array that is in wave form


SOLUTION 1:
Sort the array and then swap adjacent elements.
O(nlogn)

SOLUTION 2:
The idea is based on the fact that if we make sure that all even positioned (at index 0, 2, 4, ..) elements are greater than their adjacent odd elements, we don’t need to worry about odd positioned element.
Following are simple steps.
1) Traverse all even positioned elements of input array, and do following.
….a) If current element is smaller than previous odd element, swap previous and current.
….b) If current element is smaller than next odd element, swap next and current.

NOTE: This solution will not work if the elements have to be strictly > or <.
"""


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def wiggle_sort(arr):
    i = 0
    while i < len(arr):
        if i - 1 >= 0 and arr[i] < arr[i - 1]:
            swap(arr, i, i - 1)
        if i + 1 < len(arr) and arr[i] < arr[i + 1]:
            swap(arr, i, i + 1)
        i += 2


def wiggle_sort2(arr):
    less = True
    for i in range(0, len(arr) - 1):
        if less and arr[i] > arr[i + 1]:
            swap(arr, i, i + 1)
        if not less and arr[i] < arr[i + 1]:
            swap(arr, i, i + 1)
        less = not less


def main():
    arr = [10, 90, 49, 2, 1, 5, 23]
    wiggle_sort2(arr)
    print(arr)


main()
