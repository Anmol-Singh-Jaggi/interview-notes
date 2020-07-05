from algo.searching.binary_search_count.binary_search_count import lower_bound, upper_bound


def get_index_range(arr, elem):
    # Returns the lower bound and upper bound.
    # Lower bound = The number of elements strictly less than n.
    # Upper bound = The number of elements less than or equal to n.
    ub = upper_bound(arr, elem)
    lb = lower_bound(arr, elem)
    return [lb, ub]


def find_index_after_merge(arr1, arr2, index):
    '''
    Returns the element at this index in the final merged array.
    The target element can be either in array1 or array2.
    Given an element, we can find its lowest and highest indices in the merged array
    by using lower bound and upper bound.
    We will use this property here.
    We first start binary searching in array1.
    If target index is in between mid's lowest and highest indices, then return mid element.
    Else if target index < lowest index of mid, then target is less than mid element.
    Else target is bigger than mid element.
    If no such element exists in array1, then we swap the 2 arrays and repeat the process.
    Complexity -> O(logn * logm)
    '''
    low = 0
    high = len(arr1) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_elem = arr1[mid]
        lb1, ub1 = get_index_range(arr1, mid_elem)
        lb2, ub2 = get_index_range(arr2, mid_elem)
        mid_elem_lowest_index = lb1 + lb2
        mid_elem_highest_index = ub1 + ub2 - 1
        if index < mid_elem_lowest_index:
            high = mid - 1
        elif index > mid_elem_highest_index:
            low = mid + 1
        else:
            return mid_elem
    return None


def main():
    arr1 = [1, 2, 3, 4]
    arr2 = [1, 2, 3, 4]
    arr1 = [1, 2, 4, 6, 10]
    arr2 = [4, 5, 6, 9, 12]
    # 0 1 2 3 4 5 6 7 8  9
    # 1 2 4 4 5 6 6 9 10 12
    size = len(arr1)
    index = 4
    ans = find_index_after_merge(arr1, arr2, index)
    if ans is None:
        ans = find_index_after_merge(arr2, arr1, index)
    print(ans)


main()
