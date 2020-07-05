'''
An efficient solution is based on sliding window technique that can be used to solve the problem. We use two pointers start and end to represent starting and ending point of sliding window. (Not that we need to find contiguous parts).

Initially both start and end point to the beginning of the array, i.e. index 0. Now, let’s try to add a new element el. There are two possible conditions.

1st case :
If sum is less than k, increment end by one position. So contiguous arrays this step produce are (end – start). We also add el to previous sum. There are as many such arrays as the length of the window.

2nd case :
If sum becomes greater than or equal to k, this means we need to subtract starting element from sum so that the sum again becomes less than k. So we adjust the window’s left border by incrementing start.

We follow the same procedure until end < array size.
NOTE: This works only for positive integer array.
'''
