def min_swaps(arr):
    arr_sorted = sorted(arr)
    order = {}
    for idx, elem in enumerate(arr):
        order[elem] = idx
    ans = 0
    for i in range(len(arr)):
        correct_elem = arr_sorted[i]
        current_elem = arr[i]
        if current_elem == correct_elem:
            continue
        # Just try to bring the correct element at this position.
        correct_elem_pos = order[correct_elem]
        swapped_elem = arr[i]
        order[correct_elem] = i
        order[swapped_elem] = correct_elem_pos
        arr[i], arr[correct_elem_pos] = arr[correct_elem_pos], arr[i]
        ans += 1
    return ans


def main():
    arr = [1, 5, 4, 3, 2]
    print(min_swaps(arr))


main()
