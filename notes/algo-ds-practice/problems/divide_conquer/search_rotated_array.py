def find_pivot(arr, low, high):
    while low <= high:
        if low == high:
            return low
        mid = (low + high) // 2
        if arr[mid] > arr[mid + 1]:
            return mid
        # CAREFUL: Its arr[low] not arr[high]!!
        if arr[mid] < arr[low]:
            high = mid - 1
        else:
            low = mid + 1


def binary_search(items, item_to_search):
    start_index = 0
    end_index = len(items) - 1
    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        current_item = items[mid_index]
        if current_item == item_to_search:
            return mid_index
        elif current_item < item_to_search:
            start_index = mid_index + 1
        else:
            end_index = mid_index - 1
    return -1


def search_element_in_rotated(arr, low, high, elem):
    pivot_idx = find_pivot(arr, low, high)
    ans = binary_search(arr[low : pivot_idx + 1], elem)
    if ans != -1:
        return ans
    ans = binary_search(arr[pivot_idx + 1 : high + 1], elem)
    if ans == -1:
        return ans
    return ans + pivot_idx + 1


def search_element_in_rotated_direct(arr, low, high, elem):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == elem:
            return mid
        if elem < arr[mid]:
            if arr[low] > arr[mid] or arr[low] <= elem:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[high] < arr[mid] or arr[high] >= elem:
                low = mid + 1
            else:
                high = mid - 1
    return -1


def search_element_in_rotated_direct2(arr, l, h, key):
    if l > h:
        return -1

    mid = (l + h) // 2
    if arr[mid] == key:
        return mid

    # If arr[l...mid] is sorted
    if arr[l] <= arr[mid]:

        # As this subarray is sorted, we can quickly
        # check if key lies in half or other half
        if key >= arr[l] and key <= arr[mid]:
            return search_element_in_rotated_direct2(arr, l, mid - 1, key)
        return search_element_in_rotated_direct2(arr, mid + 1, h, key)

    # If arr[l..mid] is not sorted, then arr[mid... r] must be sorted
    if key >= arr[mid] and key <= arr[h]:
        return search_element_in_rotated_direct2(arr, mid + 1, h, key)
    return search_element_in_rotated_direct2(arr, l, mid - 1, key)


def main():
    arr = [30, 35, 40, 1, 2, 3, 4, 10, 15, 16, 20, 25, 27]
    ans = search_element_in_rotated_direct(arr, 0, len(arr) - 1, 25)
    print(ans)
    print(arr[ans])


main()
