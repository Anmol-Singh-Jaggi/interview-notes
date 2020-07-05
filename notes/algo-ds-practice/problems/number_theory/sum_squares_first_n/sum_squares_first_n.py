"""
Sum of square of first n even numbers.
Input : 3
Output : 56
22 + 42 + 62 = 56

Input : 8
Output : 816
22 + 42 + 62 + 82 + 102 + 122 + 142 + 162

Solution:

We can use directly the formula:
sum = 2 * n * (n + 1) * (2 * n + 1)/3

Derivation:
We know that sum of square of first n natural numbers is = n(n+1)(2n+1)/6

Sum of square of first n even natural numbers =
        2^2 + 4^2 + .... + (2n)^2
      = 4 * (1^2 + 2^2 + .... + n^2)
      = 4 * n(n+1)(2n+1) / 6
      = 2 * n(n+1)(2n+1)/3
"""
