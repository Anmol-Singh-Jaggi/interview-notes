'''
Given a length n, count the number of strings of length n that can be made using ‘a’, ‘b’ and ‘c’ with at-most one ‘b’ and two ‘c’s allowed.

Examples :

Input : n = 3
Output : 19
Below strings follow given constraints:
aaa aab aac aba abc aca acb acc baa
bac bca bcc caa cab cac cba cbc cca ccb

Input  : n = 4
Output : 39

SOLUTION:

DP:

int countStr(int n, int bCount, int cCount)
{
    if (bCount < 0 || cCount < 0) return 0;
    if (n == 0) return 1;
    if (bCount == 0 && cCount == 0) return 1;
    int res = countStr(n-1, bCount, cCount);
    res += countStr(n-1, bCount-1, cCount);
    res += countStr(n-1, bCount, cCount-1);
    return res;
}

answer = countStr(n, 1, 2)
'''
