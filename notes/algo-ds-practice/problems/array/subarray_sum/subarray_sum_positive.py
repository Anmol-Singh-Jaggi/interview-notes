def subarray_sum_non_negative(lst, target_sum):
    '''
    Simple 2-pointer-window.
    '''
    window_idx_left = 0
    window_idx_right = 1
    current_sum = lst[0]
    while True:
        if current_sum == target_sum:
            return window_idx_left, window_idx_right - 1
        if window_idx_right >= len(lst):
            break
        if current_sum < target_sum:
            current_sum += lst[window_idx_right]
            window_idx_right += 1
        else:
            current_sum -= lst[window_idx_left]
            window_idx_left += 1
            if window_idx_left == window_idx_right:
                assert (current_sum == 0)
                if window_idx_right < len(lst):
                    current_sum += lst[window_idx_right]
                window_idx_right += 1
    return -1, -1


def main():
    lst = [5, 1, 3, 4, 2]
    sum = 4
    i, j = subarray_sum_non_negative(lst, sum)
    print(f'{i}, {j}')


if __name__ == "__main__":
    main()
