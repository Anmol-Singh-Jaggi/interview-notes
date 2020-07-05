def lcs(string1, string2):
    len1 = len(string1)
    len2 = len(string2)
    dp_array = [[0] * (len2) for row in range(len1)]
    for i in range(0, len(dp_array)):
        for j in range(0, len(dp_array[0])):
            if string1[i] == string2[j]:
                dp_array[i][j] = dp_array[i-1][j-1] if (i >= 1 and j >= 1)\
                                                    else 0
                dp_array[i][j] += 1
            else:
                up = dp_array[i - 1][j] if i >= 1 else 0
                left = dp_array[i][j - 1] if j >= 1 else 0
                dp_array[i][j] = max(left, up)
    return dp_array[len1-1][len2-1]


def main():
    string1 = "abcdgh"
    string2 = "aedfhr"
    ans = lcs(string1, string2)
    print(ans)


if __name__ == "__main__":
    main()
