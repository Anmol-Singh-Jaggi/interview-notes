def is_interleaving(str1, str2, str3):
    if len(str3) != len(str1) + len(str2):
        return False
    size1 = len(str1)
    size2 = len(str2)
    dp = [[False for j in range(size2 + 1)] for i in range(size1 + 1)]
    for i in range(size1 + 1):
        for j in range(size2 + 1):
            k = i + j
            if i == 0 and j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = dp[i][j - 1] and str2[j - 1] == str3[k - 1]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] and str1[i - 1] == str3[k - 1]
            else:
                dp[i][j] |= dp[i - 1][j] and str1[i - 1] == str3[k - 1]
                dp[i][j] |= dp[i][j - 1] and str2[j - 1] == str3[k - 1]
    return dp[size1][size2]


def main():
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    ans = is_interleaving(s1, s2, s3)
    print(ans)


main()
