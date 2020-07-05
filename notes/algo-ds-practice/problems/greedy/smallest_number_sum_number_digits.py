'''
How to find the smallest number with given digit sum s and number of digits d ?
Examples :

Input  : s = 9, d = 2
Output : 18
There are many other possible numbers
like 45, 54, 90, etc with sum of digits
as 9 and number of digits as 2. The
smallest of them is 18.

Input  : s = 20, d = 3
Output : 299

SOLUTION:

Fill the last n-1 digits with the pattern 00009999...
And then put 1 at the first digit.
Greedy solution.
'''
