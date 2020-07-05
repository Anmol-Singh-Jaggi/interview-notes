def subset_sum(arr, target_sum, i, cache):
    """
    Returns whether any subset(not contiguous) of the array has sum equal to target sum.
    """
    if target_sum == 0:
        return True, {}
    if i < 0:
        return False, {}
    if target_sum in cache[i]:
        return cache[i][target_sum]
    # Either include this element or not!
    sub_ans, sub_ans_indices = subset_sum(arr, target_sum, i - 1, cache)
    if not sub_ans and target_sum >= arr[i]:
        sub_ans, sub_ans_indices = subset_sum(arr, target_sum - arr[i], i - 1, cache)
        sub_ans_indices = set(sub_ans_indices)
        sub_ans_indices.add(i)
    if not sub_ans:
        sub_ans_indices = {}
    cache[i][target_sum] = sub_ans, sub_ans_indices
    return cache[i][target_sum]


def is_subset_sum_exists(arr, target_sum):
    arr.sort()
    cache = {}
    max_idx = -1
    # Preprocessing to remove all elements greater than target.
    for i in range(len(arr)):
        if arr[i] <= target_sum:
            cache[i] = {}
            max_idx = i
        else:
            break
    if max_idx == -1:
        return False
    arr = arr[: max_idx + 1]
    ans = subset_sum(arr, target_sum, len(arr) - 1, cache)
    return ans


def main():
    arr = [1, 5, 5, 11]
    target_sum = 22
    ans = is_subset_sum_exists(arr, target_sum)
    print(ans)


if __name__ == "__main__":
    main()
