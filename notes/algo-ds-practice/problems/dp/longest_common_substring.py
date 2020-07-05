def longest_common_substring(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    dp = [[0 for j in range(len2)] for i in range(len1)]
    ans = 0
    for i in range(len1):
        for j in range(len2):
            if str1[i] == str2[j]:
                dp_previous = 0
                if i >= 1 and j >= 1:
                    dp_previous = dp[i - 1][j - 1]
                dp[i][j] = dp_previous + 1
            ans = max(ans, dp[i][j])
    return ans


def main():
    str1 = "OldSite:GeeksforGeeks.org"
    str2 = "NewSite:GeeksQuiz.com"
    ans = longest_common_substring(str1, str2)
    print(ans)


if __name__ == "__main__":
    main()
