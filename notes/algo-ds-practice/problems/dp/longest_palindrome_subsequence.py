def longest_palin_subsequence(str1):
    """
    dp[size][i] = dp[size-2][i+1] + 2 if str[i] == str[j]
    else
    dp[size][i] = max(dp[size-1][i], dp[size-1][i+1])
    where dp[size][i] = answer for substring of size `size` starting at index `i`.
    """
    str_len = len(str1)
    longest_palin = [[0 for j in range(str_len)] for i in range(str_len + 1)]
    for i in range(str_len):
        longest_palin[0][i] = 0
        longest_palin[1][i] = 1
    ans = 1
    for size in range(2, str_len + 1):
        for idx_left in range(0, str_len):
            idx_right = idx_left + size - 1
            if idx_right >= str_len:
                break
            if str1[idx_left] == str1[idx_right]:
                longest_palin[size][idx_left] = longest_palin[size - 2][idx_left] + 2
                if longest_palin[size][idx_left] > ans:
                    ans = longest_palin[size][idx_left]
            else:
                longest_palin[size][idx_left] = max(
                    longest_palin[size - 1][idx_left],
                    longest_palin[size - 1][idx_left + 1],
                )
    return ans


def main():
    str1 = "abcddefg"
    ans = longest_palin_subsequence(str1)
    print(ans)


main()
