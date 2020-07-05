"""
Given three arrays sorted in non-decreasing order, print all common elements in these arrays.
Examples:
Input:
ar1[] = {1, 5, 10, 20, 40, 80}
ar2[] = {6, 7, 20, 80, 100}
ar3[] = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20, 80


Input:
ar1[] = {1, 5, 5}
ar2[] = {3, 4, 5, 5, 10}
ar3[] = {5, 5, 10, 20}
Output: 5, 5
"""


def intersection_3_arrays(arr1, arr2, arr3):
    i, j, k = 0, 0, 0
    intersection = []
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        # If x = y and y = z, print any of them and move ahead
        # in all arrays
        if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
            intersection.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1
