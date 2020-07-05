"""
Given two strings str1 and str2,
find the length of the smallest string which has both, str1 and str2 as its sub-sequences.

Example:
Input:
2
abcd xycd
efgh jghi
Output:
6
6


SOLUTION:

if str[i] == str[j], then dp[i][j] = dp[i-1][j-1] + 1
else, dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

Be careful when i-1 or j-1 is less than 0!

ALTERNATE:

Answer = len1 + len2 - (Length of LCS of two given strings)
"""


def shortest_common_supersequence(string1, string2):
    len1 = len(string1)
    len2 = len(string2)
    dp_array = [[0] * (len2) for row in range(len1)]
    for i in range(0, len(dp_array)):
        for j in range(0, len(dp_array[0])):
            if string1[i] == string2[j]:
                # CAREFUL: Note the `else max(i, j)`.
                # Also `j+1` and `i+1` in the next lines.
                dp_array[i][j] = (
                    dp_array[i - 1][j - 1] if (i >= 1 and j >= 1) else max(i, j)
                )
            else:
                up = dp_array[i - 1][j] if i >= 1 else j + 1
                left = dp_array[i][j - 1] if j >= 1 else i + 1
                dp_array[i][j] = min(left, up)
            dp_array[i][j] += 1
    return dp_array[len1 - 1][len2 - 1]


def main():
    str1 = "abcd"
    str2 = "xycd"
    ans = shortest_common_supersequence(str1, str2)
    print(ans)


main()

