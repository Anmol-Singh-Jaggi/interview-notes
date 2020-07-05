"""
Given a positive integer n, check if it is perfect square or not using
only addition/subtraction operations and in minimum time complexity.

Solution:

Addition of first n odd numbers is always perfect square
1 + 3 = 4,
1 + 3 + 5 = 9,
1 + 3 + 5 + 7 + 9 + 11 = 36 ...
"""


def is_perfect_square(n):
    '''
    Time complexity - O(n)
    '''
    i = 1
    odd_sum = 0
    while odd_sum < n:
        odd_sum += i
        if odd_sum == n:
            return True
        i += 2
    return False
