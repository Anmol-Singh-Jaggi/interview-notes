def partition(arr, start, end, pivot_index):
    """
    Partitions the array such that all elements before pivot_index
    are <= pivot element, and all the elements after are >= pivot element.
    The pivot element will come at its rightful position at the end.
    Returns the rightful index of the pivot.
    """
    arr[start], arr[pivot_index] = arr[pivot_index], arr[start]
    pivot_index = start
    i = start + 1
    while i <= end:
        if arr[i] < arr[start]:
            pivot_index += 1
            arr[pivot_index], arr[i] = arr[i], arr[pivot_index]
        i += 1
    # CAREFUL: Dont forget this step!!
    arr[pivot_index], arr[start] = arr[start], arr[pivot_index]
    return pivot_index


def select_kth_smallest(arr, start, end, k):
    assert start <= end
    assert k >= 0
    print(k)
    print(start)
    print(end)
    assert k <= end - start
    if end - start < 5:
        arr_sorted = sorted(arr[start : end + 1])
        return arr_sorted[k]
    medians = []
    for i in range(start, end, 5):
        range_start = i
        range_end = min(end, i + 4)
        range_length = range_end - range_start + 1
        range_mid = range_length // 2
        range_median = select_kth_smallest(arr, range_start, range_end, range_mid)
        medians.append(range_median)
    mid_idx = len(medians) // 2
    median = select_kth_smallest(medians, 0, len(medians) - 1, mid_idx)
    median_index = None
    for i in range(start, end + 1):
        if arr[i] == median:
            median_index = i
            break
    pivot_index = partition(arr, start, end, median_index)
    if pivot_index == k:
        return arr[median_index]
    elif k < median_index:
        return select_kth_smallest(arr, start, k - 1, k)
    else:
        return select_kth_smallest(arr, k + 1, end, k - median_index - 1)


def main():
    arr = [5, 1, 3, 2, 4, 6, 7]
    k = 4
    print(sorted(arr))
    print(sorted(arr)[k])
    ans = select_kth_smallest(arr, 0, len(arr) - 1, 4)
    print(ans)


if __name__ == "__main__":
    main()
#https://rcoh.me/posts/linear-time-median-finding/

#https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-introduction-to-algorithms-sma-5503-fall-2005/video-lectures/lecture-6-order-statistics-median/
