'''
Longest subsequence whose average is less than K

Given an array of N positive integers and Q queries consisting of an integer K, the task is to print the length of the longest subsequence whose average is less than K.

Examples:

    Input: a[] = {1, 3, 2, 5, 4}
    Query1: K = 3
    Query2: K = 5


    Output:
    4
    5
    Query1: The subsequence is: {1, 3, 2, 4} or {1, 3, 2, 5}
    Query2: The subsequence is: {1, 3, 2, 5, 4}

SOLUTION:

An efficient approach is to sort the array elements and find the average of elements starting from the left.
Insert the average of elements computed from the left into the container(vector or arrays).
Sort the container’s element and then use binary search to search for the number K in the container.
The length of the longest subsequence will thus be the index number which upper_bound() returns for every query.
'''
