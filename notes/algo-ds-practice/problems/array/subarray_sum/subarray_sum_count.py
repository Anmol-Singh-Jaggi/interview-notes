def subarray_sum_count(lst, target_sum):
    # Algo very similar to subarray sum for negative.
    # Mapping of sum vs all the indices at which this sum happened.
    sum_vs_idx_map = {0: set([-1])}
    sum = 0
    ans = 0
    for i in range(len(lst)):
        sum += lst[i]
        sum_indices = sum_vs_idx_map.get(sum, set())
        sum_indices.add(i)
        sum_vs_idx_map[sum] = sum_indices
        sum_diff = sum - target_sum
        sum_diff_indices = sum_vs_idx_map.get(sum_diff, set())
        ans += len(sum_diff_indices)
    return ans


def main():
    lst = [1, 2, 3, 2, 1, 1, 1]
    sum = 3
    ans = subarray_sum_count(lst, sum)
    print(ans)


if __name__ == "__main__":
    main()
