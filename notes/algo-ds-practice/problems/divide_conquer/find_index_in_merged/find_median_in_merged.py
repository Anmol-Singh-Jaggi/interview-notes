"""
Given 2 sorted arrays, find the median of the merged array.
If the merged array is of even size, return the average of the middle values.

SOLUTION:

Our aim is to basically find an index 'idx1' in array1 and an index 'idx2' in array2 such that idx1 + idx2 == (len1 + len2 - 1) // 2 and all elements before idx1 are less than all the elements after index idx2 and all the elements before idx2 are less than elements after idx1.
See Tushar Roy's Youtube video for beautiful explanation.
"""
from math import inf


def get_boundary_values(arr1, arr2, mid1, mid2):
    max_left1 = arr1[mid1 - 1] if mid1 > 0 else -inf
    max_left2 = arr2[mid2 - 1] if mid2 > 0 else -inf
    min_right1 = arr1[mid1] if mid1 < len(arr1) else inf
    min_right2 = arr2[mid2] if mid2 < len(arr2) else inf
    return max_left1, max_left2, min_right1, min_right2


def get_median_from_boundary_values(arr1, arr2, mid1, mid2):
    max_left1, max_left2, min_right1, min_right2 = get_boundary_values(
        arr1, arr2, mid1, mid2
    )
    max_left = max(max_left1, max_left2)
    min_right = min(min_right1, min_right2)
    if (len(arr1) + len(arr2)) % 2 == 0:
        return (max_left + min_right) / 2
    else:
        return max_left


def get_median_of_sorted_array(arr):
    mid = len(arr) // 2
    if len(arr) % 2 == 0:
        return (arr[mid - 1] + arr[mid]) / 2
    else:
        return arr[mid]


def find_median_in_sorted_merged(arr1, arr2):
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1
    low, high = 0, len(arr1)
    if len(arr1) == 0:
        return get_median_of_sorted_array(arr2)
    while low <= high:
        mid1 = (low + high) // 2
        mid2 = (len(arr1) + len(arr2) + 1) // 2 - mid1
        max_left1, max_left2, min_right1, min_right2 = get_boundary_values(
            arr1, arr2, mid1, mid2
        )
        if max_left1 <= min_right2 and max_left2 <= min_right1:
            return get_median_from_boundary_values(arr1, arr2, mid1, mid2)
        elif max_left1 > min_right2:
            high = mid1 - 1
        else:
            low = mid1 + 1


def main():
    arr1 = [1, 3, 8, 9, 15]
    arr2 = [7, 11, 18, 19, 21, 25]
    arr1 = [1, 2]
    arr2 = [3, 4]
    median = find_median_in_sorted_merged(arr1, arr2)
    print(median)
    arr1.extend(arr2)
    arr1.sort()
    print(get_median_of_sorted_array(arr1))


main()
