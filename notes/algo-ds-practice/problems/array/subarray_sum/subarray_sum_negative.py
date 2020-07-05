def subarray_sum_negative_largest(lst, target_sum):
    """
    Handles negative numbers also.
    Returns the largest subarray of sum 'target_sum'.
    1. Make a cumulative sum array 'sum_left'.
    2. Iterate through all the elements of sum_left.
       For example, if the current sum is 100, and target sum was 60,
       then that means we need to find a subarray with the sum 60 ending
       before i. This data would be in a hash-map of <sum> vs <leftmost-index>.
    This is very similar to the problem 'Largest subarray with equal number of 0's and 1's'
    """
    # Mapping of sum vs the first(leftmost) index at which this sum happened.
    sum_vs_idx_map = {0: -1}
    ans_left = -1
    ans_right = -2
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
        sum_leftmost_idx = sum_vs_idx_map.get(sum, None)
        if sum_leftmost_idx is None:
            sum_vs_idx_map[sum] = i
        sum_diff = sum - target_sum
        sum_diff_idx = sum_vs_idx_map.get(sum_diff, None)
        if sum_diff_idx is not None:
            temp_ans_right = i
            temp_ans_left = sum_diff_idx + 1
            temp_ans_length = temp_ans_right - temp_ans_left
            old_ans_length = ans_right - ans_left
            if temp_ans_length > old_ans_length:
                ans_left = temp_ans_left
                ans_right = temp_ans_right

    return ans_left, ans_right


def subarray_sum_negative_first(lst, target_sum):
    """
    Returns the first subarray with the target_sum.
    It might not be the largest such subarray.
    """
    sum_vs_idx_map = {0: -1}
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
        sum_leftmost_idx = sum_vs_idx_map.get(sum, None)
        if sum_leftmost_idx is None:
            sum_vs_idx_map[sum] = i
        sum_diff = sum - target_sum
        sum_diff_idx = sum_vs_idx_map.get(sum_diff, None)
        if sum_diff_idx is not None:
            return f"{sum_diff_idx + 2} {i + 1}"
    return "-1"


def main():
    t = int(input())
    while t:
        t -= 1
        n, target_sum = [int(x) for x in input().strip().split()]
        elems = [int(x) for x in input().strip().split()]
        ans = subarray_sum_negative_first(elems, target_sum)
        print(ans)


if __name__ == "__main__":
    main()
