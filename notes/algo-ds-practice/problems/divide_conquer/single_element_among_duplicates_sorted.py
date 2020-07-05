"""
Given a sorted array in which all elements appear twice (one after one)
and one element appears only once.
Find that element in O(log n) complexity.

SOLUTION:
An Efficient Solution can find the required element in O(Log n) time.
The idea is to use Binary Search. Below is an observation in input array.
All elements before the required have first occurrence at even index (0, 2, ..)
and next occurrence at odd index (1, 3, …).
And all elements after the required element have first occurrence at odd index and next occurrence at even index.

1) Find the middle index, say ‘mid’.
2) If ‘mid’ is even, then compare arr[mid] and arr[mid + 1].
If both are same, then the required element after ‘mid’ else before mid.
3) If ‘mid’ is odd, then compare arr[mid] and arr[mid – 1].
If both are same, then the required element after ‘mid’ else before mid.
"""


def search(arr, low, high):
    if low > high:
        return None
    if low == high:
        return arr[low]
    mid = low + (high - low) / 2
    # If mid is even and element next to mid is
    # same as mid, then output element lies on
    # right side, else on left side
    if mid % 2 == 0:
        if arr[mid] == arr[mid + 1]:
            return search(arr, mid + 2, high)
        else:
            return search(arr, low, mid)
    else:
        if arr[mid] == arr[mid - 1]:
            return search(arr, mid + 1, high)
        else:
            return search(arr, low, mid - 1)
