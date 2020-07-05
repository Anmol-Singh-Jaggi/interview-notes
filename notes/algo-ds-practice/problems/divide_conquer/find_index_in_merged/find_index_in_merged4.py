"""
Almost similar to how we find median in merged.
"""
from math import inf


def get_boundary_values(arr1, arr2, mid1, mid2):
    max_left1 = arr1[mid1] if mid1 >= 0 else -inf
    max_left2 = arr2[mid2] if mid2 >= 0 else -inf
    min_right1 = arr1[mid1 + 1] if mid1 + 1 < len(arr1) else inf
    min_right2 = arr2[mid2 + 1] if mid2 + 1 < len(arr2) else inf
    return max_left1, max_left2, min_right1, min_right2


def find_index_in_sorted_merged(arr1, arr2, idx):
    '''
    Complexity -> O(min(logn, logm))
    '''
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1
    low, high = 0, min(idx, len(arr1))
    if len(arr1) == 0:
        return arr2[idx]
    while low <= high:
        mid1 = (low + high) // 2
        mid2 = idx - mid1 - 1
        max_left1, max_left2, min_right1, min_right2 = get_boundary_values(
            arr1, arr2, mid1, mid2
        )
        if max_left1 <= min_right2 and max_left2 <= min_right1:
            return max(max_left1, max_left2)
        elif max_left1 > min_right2:
            high = mid1 - 1
        else:
            low = mid1 + 1
    # CAREFUL: Tricky implementation!
    return arr2[idx]


def main():
    arr1 = [1, 3, 8, 9, 15]
    arr2 = [7, 11, 18, 19, 21, 25]
    arr1 = [1, 2]
    arr2 = [3, 4]
    index = 3
    ans = find_index_in_sorted_merged(arr1, arr2, index)
    print(ans)
    arr1.extend(arr2)
    print(arr1[index])


main()
