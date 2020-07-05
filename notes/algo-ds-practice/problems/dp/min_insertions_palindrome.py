def min_insertions_palindrome(str1):
    """
    dp[size][i] = dp[size-2][i+1] if str[i] == str[j]
    else
    dp[size][i] = max(dp[size-1][i], dp[size-1][i+1]) + 1
    where dp[size][i] = Answer for substring of size `size` starting at index `i` is palindrome or not.
    Answer = dp[len(str)][0]
    """
    str_len = len(str1)
    dp = [[0 for j in range(str_len)] for i in range(str_len + 1)]
    for size in range(2, str_len + 1):
        for idx_left in range(0, str_len):
            idx_right = idx_left + size - 1
            if idx_right >= str_len:
                break
            if str1[idx_left] == str1[idx_right]:
                dp[size][idx_left] = dp[size - 2][idx_left + 1]
            else:
                dp[size][idx_left] = (
                    min(dp[size - 1][idx_left], dp[size - 1][idx_left + 1]) + 1
                )
    return dp[str_len][0]


def main():
    t = int(input())
    while t:
        t -= 1
        str1 = input()
        ans = min_insertions_palindrome(str1)
        print(ans)


main()
