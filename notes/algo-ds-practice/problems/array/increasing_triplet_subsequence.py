"""
Given an array of n integers, find the 3 elements such that a[i] < a[j] < a[k] and i < j < k.
If there are multiple such triplets, then print any one of them.

Examples:

Input:  arr[] = {12, 11, 10, 5, 6, 2, 30}
Output: 5, 6, 30

Input:  arr[] = {1, 2, 3, 4}
Output: 1, 2, 3 OR 1, 2, 4 OR 2, 3, 4

Input:  arr[] = {4, 3, 2, 1}
Output: No such triplet


SOLUTION:

Solution 1:
1) Create an auxiliary array smaller[0..n-1].
smaller[i] should store the index of a number which is smaller than arr[i] and is on left side of arr[i].
smaller[i] should contain -1 if there is no such element.
2) Create another auxiliary array greater[0..n-1].
greater[i] should store the index of a number which is greater than arr[i] and is on right side of arr[i].
greater[i] should contain -1 if there is no such element.
3) Finally traverse both smaller[] and greater[] and find the index i for which both smaller[i] and greater[i] are not -1.
For computing smaller and greater, we can compute cumulative maximum and minimums.
O(n) time and space.

Solution 2:
See code
O(1) space and O(n) time.
"""
from math import inf


def increasing_triplet(arr):
    '''
    Note that small and big do not represent the triplets.
    The functions just returns true or false thats all.
    It cannot return the triplets themselves.
    '''
    small, big = inf, inf
    for num in arr:
        if num <= small:
            small = num
        elif num <= big:
            big = num
        else:
            return True
    return False
