def check_pair_sum_divisible(arr, k):
    """
    Check if an array can be divided into pairs whose sum is divisible by k.
    """
    rem_freq_map = {}
    for elem in arr:
        rem = elem % k
        rem_freq_map[rem] = rem_freq_map.get(rem, 0) + 1
    for rem, freq in rem_freq_map.items():
        if rem == 0 or rem * 2 == k:
            if freq & 1:
                return False
        elif not freq == rem_freq_map.get(k - rem, 0):
            return False
    return True


def main():
    arr = [1, 1]
    k = 1
    ans = check_pair_sum_divisible(arr, k)
    print(ans)


main()
