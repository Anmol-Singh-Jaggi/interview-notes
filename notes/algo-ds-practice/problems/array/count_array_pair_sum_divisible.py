def count_pair_sum_divisible(arr, k):
    """
    Count number of pairs whose sum is divisible by k.
    """
    rem_freq_map = {}
    for elem in arr:
        rem = elem % k
        rem_freq_map[rem] = rem_freq_map.get(rem, 0) + 1
    ans = 0
    for rem, freq in rem_freq_map.items():
        if rem == 0 or rem * 2 == k:
            ans += (freq * (freq - 1)) // 2
        else:
            rem_inverse = k - rem
            # CAREFUL: We dont want to count a pair twice!
            if rem < rem_inverse:
                ans += freq * rem_freq_map.get(rem_inverse, 0)
    return ans


def main():
    arr = [2, 2, 1, 7, 5, 3]
    k = 4
    ans = count_pair_sum_divisible(arr, k)
    print(ans)


main()
