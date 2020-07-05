def merge_sorted(arr, start, mid, end):
    temp_arr = []
    pointer1 = start
    pointer2 = mid + 1
    while pointer1 <= mid and pointer2 <= end:
        if arr[pointer1] < arr[pointer2]:
            temp_arr.append(arr[pointer1])
            pointer1 += 1
        else:
            temp_arr.append(arr[pointer2])
            pointer2 += 1
    while pointer1 <= mid:
        temp_arr.append(arr[pointer1])
        pointer1 += 1
    while pointer2 <= end:
        temp_arr.append(arr[pointer2])
        pointer2 += 1
    for i in range(len(temp_arr)):
        arr[i + start] = temp_arr[i]


def merge_sort(arr, start, end):
    if end >= start:
        return
    mid = (start + end) // 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid + 1, end)
    merge_sorted(arr, start, mid, end)


def main():
    arr = [5, 3, 2, 4, 1, 1]
    merge_sort(arr, 0, len(arr) - 1)
    print(arr)


if __name__ == "__main__":
    main()
