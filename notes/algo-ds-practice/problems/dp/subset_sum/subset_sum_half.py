from problems.dp.subset_sum.subset_sum import is_subset_sum_exists

"""
Check if array can be divided into 2 subsets with equal sum.
"""


def main():
    arr = [1, 5, 5, 11]
    arr_sum = sum(arr)
    # If sum of array is odd, then not possible anyway.
    if arr_sum & 1:
        print("NO")
        return
    target_sum = arr_sum >> 1
    ans = is_subset_sum_exists(arr, target_sum)
    print(ans)


main()

