def largest_subarrays(lst):
    '''
    1. Make an auxiliary array 'aux' such that
       aux[i] = Difference of number of 1's - 0's until i.
    2. Now task is to find 2 equal numbers in the auxiliary array
       which are as far apart as possible.
    3. Store the very first occurences of all the numbers in a hash-mmap.
    4. Then iterate through the aux array and update answer = max(answer, i - map[aux[i]]).
    Source - https://stackoverflow.com/a/31201586/1925388
    It is very similar to the problem 'Subarray with the given sum for negative integers'
    '''
    # Mapping of diff(1's - 0's) vs the lefmost index at which this diff happened.
    diff_vs_idx_map = {0: -1}
    num1 = 0
    num0 = 0
    ans = 0
    for i in range(len(lst)):
        if lst[i] == 1:
            num1 += 1
        else:
            num0 += 1
        diff = num1 - num0
        diff_leftmost_idx = diff_vs_idx_map.get(diff, None)
        if diff_leftmost_idx is not None:
            ans = max(ans, i - diff_leftmost_idx)
        else:
            diff_vs_idx_map[diff] = i
    return ans


def main():
    t = int(input())
    while t:
        t -= 1
        int(input())
        elems = [int(x) for x in input().strip().split()]
        ans = largest_subarrays(elems)
        print(ans)


if __name__ == "__main__":
    main()
