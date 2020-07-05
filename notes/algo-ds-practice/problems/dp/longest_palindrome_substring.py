def longest_palin_substring(str1):
    """
    dp[size][i] = dp[size-2][i+1] if str[i] == str[j]
    else
    dp[size][i] = False
    where dp[size][i] = If substring of size `size` starting at index `i` is palindrome or not.
    Answer = max of all (j-i+1) where dp[i][j] is True.
    """
    str_len = len(str1)
    is_palin = [[False for j in range(str_len)] for i in range(str_len + 1)]
    for i in range(str_len):
        is_palin[0][i] = True
        is_palin[1][i] = True
    ans_idx_left = 0
    ans_idx_right = 0
    for size in range(2, str_len + 1):
        for idx_left in range(0, str_len):
            idx_right = idx_left + size - 1
            if idx_right >= str_len:
                break
            if str1[idx_left] == str1[idx_right]:
                if is_palin[size - 2][idx_left + 1]:
                    is_palin[size][idx_left] = True
                    # Only update if it is strictly greater.
                    # Which means in case of conflict, the lefmost palindrome
                    # will be printed.
                    if idx_right - idx_left > ans_idx_right - ans_idx_left:
                        ans_idx_left = idx_left
                        ans_idx_right = idx_right
    return (ans_idx_left, ans_idx_right)


def longest_palin__substring_space_optimized(str1):
    """
    Find all odd-length palindromes first in O(n*n).
    Do this by choosing all the characters as the centre one-by-one and
    then expanding outwards.
    Next, find all the even-length palindromes in O(n*n).
    Do this by taking all the adjacent character pairs and expanding.
    Then compute the maximum of both.
    """
    pass
