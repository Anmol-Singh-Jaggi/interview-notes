"""
You are given an unsorted array with both positive and negative elements.
The positive numbers need not be in range from 1 to n !!
You have to find the smallest positive number missing from the array in O(n) time using constant extra space.
Examples

 Input:  {2, 3, 7, 6, 8, -1, -10, 15}
 Output: 1

 Input:  { 2, 3, -7, 6, 8, 1, -10, 15 }
 Output: 4

 Input: {1, 1, 0, -1, -2}
 Output: 2

SOLUTION:

Exactly same as the solution to `find_duplicates.py`.
Basically, we mark the occurrence of a number 'elem' by making arr[elem] as -ve.
Then we traverse the array; the first index i such that arr[i] is +ve is the answer.
Note that before doing this we'll need to bring all the non-positive elements to the left side to segregate them
since they dont matter.
"""


def segregate_non_positive(arr):
    # Stores the index of the slot where the next non-positive number will be swapped to.
    # This is also the index of the first positive number.
    # All the numbers arr[i] where i < next_slot, will be None.
    next_slot = 0
    for i in range(len(arr)):
        if arr[i] <= 0:
            arr[i], arr[next_slot] = arr[next_slot], arr[i]
            arr[next_slot] = None
            next_slot += 1
    return next_slot


def get_smallest_missing(arr):
    idx = segregate_non_positive(arr)
    for i in range(idx, len(arr)):
        slot = abs(arr[i]) - 1
        if slot >= len(arr):
            continue
        if arr[slot] is None:
            arr[slot] = 0
        elif arr[slot] > 0:
            arr[slot] = -arr[slot]
    for i in range(len(arr)):
        if arr[i] is None or arr[i] > 0:
            return i + 1
    return len(arr) + 1


def main():
    arr = [-1, 0, 5, 1, -2, -4, 6]
    arr = [-1]
    ans = get_smallest_missing(arr)
    print(ans)
    print(arr)


main()
