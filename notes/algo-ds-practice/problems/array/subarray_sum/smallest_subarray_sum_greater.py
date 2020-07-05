'''
Given an array of integers and a number x, find the smallest subarray with sum greater than the given value.

Examples:
arr[] = {1, 4, 45, 6, 0, 19}
   x  =  51
Output: 3
Minimum length subarray is {4, 45, 6}

arr[] = {1, 10, 5, 2, 7}
   x  = 9
Output: 1
Minimum length subarray is {10}

arr[] = {1, 11, 100, 1, 0, 200, 3, 2, 1, 250}
    x = 280
Output: 4
Minimum length subarray is {100, 1, 0, 200}

arr[] = {1, 2, 4}
    x = 8
Output : Not Possible
Whole array sum is smaller than 8.


SOLUTION:
If array contains only +ve integers and threshold sum is +ve.
 -> Use 2-pointer window algo
If array contains only +ve and threshold sum is -ve.
 -> Answer is 1.
If array contains -ve and +ve both and threshold sum is +ve.
 -> Apply the same 2-pointer window algo but simply ignore any window containing any -ve integer.
Remaining cases are trivial.
'''
