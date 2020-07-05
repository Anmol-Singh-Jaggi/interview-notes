from random import randint


def partition(arr, start, end, pivot_index):
    '''
    Partitions the array such that all elements before pivot_index
    are <= pivot element, and all the elements after are >= pivot element.
    The pivot element will come at its rightful position at the end.
    Returns the rightful index of the pivot.
    '''
    arr[start], arr[pivot_index] = arr[pivot_index], arr[start]
    # CAREFUL: Dont forget this! The input pivot index need not be start always!
    pivot_index = start
    for i in range(start + 1, end):
        if arr[i] < arr[start]:
            pivot_index += 1
            arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
    # CAREFUL: Dont forget this step!
    arr[start], arr[pivot_index] = arr[pivot_index], arr[start]
    return pivot_index


def quick_sort(arr, start, end):
    if end - start <= 1:
        return
    pivot_index = randint(start, end - 1)
    assert (pivot_index >= start and pivot_index < end)
    pivot_index = partition(arr, start, end, pivot_index)
    # sCAREFUL: We can ignore the pivot element now!
    quick_sort(arr, start, pivot_index)
    quick_sort(arr, pivot_index + 1, end)


def main():
    arr = [5, 3, 2, 4, 1, 1]
    quick_sort(arr, 0, len(arr))
    print(arr)


if __name__ == "__main__":
    main()
