'''
Given a string s containing 0's and 1's.
You have to return a smallest positive integer C, such that the binary string can be cut into C pieces and each piece should be of the power of 5  with no leading zeros.

Example:
Input
3
101101101
1111101
00000
Output:
3
1
-1

Explanation:
1.We can split the given string into three “101”s, where 101 is the binary representation of 5.
2."1111101 " is 125 which is 5^3.
3.0 is not a power of 5.

SOLUTION:

Try all possible scenarios using DP.
One by one place the first cut at every index from 0 to n-1 and recurse for the left and right halves.
'''
