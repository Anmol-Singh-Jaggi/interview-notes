"""
Given an array where every element occurs three times, except one element which occurs only once.
Find the element that occurs once.
Expected time complexity is O(n) and O(1) extra space.

We can sum the bits in same positions for all the numbers and take modulo with 3.
The bits for which sum is not multiple of 3, are the bits of number with single occurrence.
Let us consider the example array {5, 5, 5, 8}. The 0101, 0101, 0101, 1000
Sum of first bits%3 = (1 + 1 + 1 + 0)%3 = 0;
Sum of second bits%3 = (0 + 0 + 0 + 0)%0 = 0;
Sum of third bits%3 = (1 + 1 + 1 + 0)%3 = 0;
Sum of fourth bits%3 = (1)%3 = 1;
Hence number which appears once is 1000

NOTE:
This logic can be extended to the problem where all the elements occur 'k' times except one which occurs only once.
"""

# Python 3 program to find unique element where
# every element appears k times except one
import sys


def findUnique(a, n, k):

    # Create a count array to store count of
    # numbers that have a particular bit set.
    # count[i] stores count of array elements
    # with i-th bit set.
    INT_SIZE = 8 * sys.getsizeof(int)
    count = [0] * INT_SIZE

    # AND(bitwise) each element of the array
    # with each set digit (one at a time)
    # to get the count of set bits at each
    # position
    for i in range(INT_SIZE):
        for j in range(n):
            if (a[j] & (1 << i)) != 0:
                count[i] += 1

    # Now consider all bits whose count is
    # not multiple of k to form the required
    # number.
    res = 0
    for i in range(INT_SIZE):
        res += (count[i] % k) * (1 << i)
    return res
