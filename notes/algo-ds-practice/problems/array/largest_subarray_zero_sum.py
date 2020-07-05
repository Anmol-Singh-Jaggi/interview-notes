'''
Given an array of integers, find the length of the longest subarray with sum equals to 0.


We can use Hashing to solve this problem in O(n) time.
The idea is to iterate through the array and for every element arr[i], calculate sum of elements form 0 to i (this can simply be done as sum += arr[i]).
If the current sum has been seen before, then there is a zero sum array.
Hashing is used to store the sum values, so that we can quickly store sum and find out whether the current sum is seen before or not.
Use a hash-map to check if the sum has been seen before or not.
'''


def largest_subarray_zero_sum(lst):
    sum_vs_idx_map = {0: -1}
    cum_sum = 0
    ans_left, ans_right = None, None
    for i in range(len(lst)):
        cum_sum += lst[i]
        sum_leftmost_idx = sum_vs_idx_map.get(cum_sum, None)
        if sum_leftmost_idx is not None:
            if ans_right is None:
                ans_left, ans_right = sum_leftmost_idx, i
            if i - sum_leftmost_idx > ans_right - ans_left:
                ans_left, ans_right = sum_leftmost_idx, i
        else:
            sum_vs_idx_map[cum_sum] = i
    if ans_left is None:
        return None
    return ans_left+1, ans_right


def main():
    # 10 11 13 11 10
    lst = [1, 2, 3, -2, 4, -3, -4, 5, 0, -5]
    ans = largest_subarray_zero_sum(lst)
    print(ans)


main()
