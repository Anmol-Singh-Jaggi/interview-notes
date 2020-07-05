'''
Given two numeric strings, A and B.
A numeric string is a string that contains only digits [‘0’-‘9’].

The task is to make both the strings equal in minimum cost.
The only operation that you are allowed to do is to delete a character (i.e. digit) from any of the strings (A or B).
The cost of deleting a digit D is D units.

Examples:
Input : A = “7135”, B = “135”
Output : 7
To make both string identical we have to delete ‘7’ from string A.

Input : A = “9142”, B = “1429”
Output : 14
There are 2 ways to make string “9142” identical to “1429” i.e either by deleting ‘9’ from both the strings or by deleting ‘1’, ‘4’and ‘2’ from both the string.
Deleting 142 from both the string will cost 2*(1+4+2)=14 which is more optimal than deleting ‘9’.

SOLUTION 1:
Use DP:
ans(m,n) = ans(m-1, n-1) if str1[m] == str2[n]
else = min of:
str[m] + ans(m-1, n)
str[n] + ans(m, n-1)
str[m] + str[n] + ans(m-1, n-1)

SOLUTION 2:
Different DP:
Minimum weight to make string identical = costA + costB – 2*(cost of MWCS)
Where costA = Sum total of weights of string A.
MWCS = Max weight common subsequence.
How to compute MWCS??
mwcs(m, n) = mwcs(m-1,n-1) + str1[m] if str1[m] == str2[n]
else:
ans = max(lcs(dp, m - 1, n),
          lcs(dp, m, n - 1))
'''
